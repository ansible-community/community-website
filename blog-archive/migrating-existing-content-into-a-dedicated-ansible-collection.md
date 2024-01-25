---
author: XLAB Steampunk
date: 2020-04-08 00:00 UTC
description: In this blog post we will demonstrate how to migrate part
  of the existing Ansible content (modules and plugins) into a dedicated
  Ansible Collection.
lang: en-us
title: Migrating existing content into a dedicated Ansible collection
---

# Migrating existing content into a dedicated Ansible collection

Today, we will demonstrate how to migrate part of the existing Ansible
content (modules and plugins) into a dedicated Ansible Collection. We
will be using modules for managing DigitalOcean's resources as an
example so you can follow along and test your development setup. But
first, let us get the big question out of the way: Why would we want to
do that? 

## Ansible on a Diet

In late March 2020, Ansible's main development branch lost almost all
of its modules and plugins. Where did they go? Many of them moved to the
[ansible-collections GitHub organization](https://github.com/ansible-collections).
More specifically, the vast majority landed in the
[community.general](https://github.com/ansible-collections/community.general)
GitHub repository that serves as their temporary home (refer to the
[Community overview README](https://github.com/ansible-collections/overview)
for more information). 

The ultimate goal is to get as much content in the community.general
Ansible Collection "adopted" by a caring team of developers and moved
into a dedicated upstream location, with a dedicated [Galaxy namespace](https://galaxy.ansible.com/docs/contributing/namespaces.html).
Maintainers of the newly migrated Ansible Collection can then set up the
development and release processes as they see fit, (almost) free from
the requirements of the comunity.general collection. For more
information about the future of Ansible content delivery, please refer
to [an official blog post](https://www.ansible.com/blog/the-future-of-ansible-content-delivery),
a [Steampunk perspective](https://steampunk.si/posts/the-galactic-future-of-ansible-content/),
as well as an [AnsibleFest talk](https://www.ansible.com/how-to-build-ansible-collections-experience-from-community-members)
about Ansible Collections. 

Without any further ado, let us get our hands dirty by creating a brand
new DigitalOcean Ansible Collection.

## The Migration Process

There are three main reasons why we selected DigitalOcean-related
content for migration:

1.  It contains just enough material that it is not entirely trivial to
    migrate (we will need to use some homemade tools during the
    migration process).
2.  DigitalOcean modules use standard features like documentation
    fragments and utility Python packages, which means that merely
    copying the modules over will not be enough.
3.  It is currently part of the community.general Ansible Collection.

**Edit (2020-09-23):** The DigitalOcean modules were moved to the
`community.digitalocean` collection in July 2020, so the last
point from the list above does not hold anymore. But I guess the move
confirmed that our selection of an example was correct

So it should not come as a surprise that content migration is a
multi-step process. We need to create a working directory, clone the
community.general Ansible Collection into it, and create an empty
destination collection. But before we can do any of that, we must decide
on the name of this new Ansible Collection.

It is a well known fact that there are only two hard things in Computer
Science: cache invalidation, naming things, and off-by-one errors ;)
Fortunately, in our case, finding a proper name is relatively simple:
because we are moving all modules for working with DigitalOcean's cloud
platform, we will name it *digital_ocean.digital_ocean*.

```bash
$ mkdir -p ~/work/ansible_collections
$ cd ~/work/ansible_collections
$ mkdir community
$ git clone --depth 1 --branch 0.2.0 \
    https://github.com/ansible-collections/community.general.git \
    community/general
$ ansible-galaxy collection init digital_ocean.digital_ocean
$ cd digital_ocean/digital_ocean
```

With the directories in place, we can start copying the content over
into our new Ansible Collection. But instead of just moving the modules
over, we will also take the opportunity to rename the modules. 

DigitalOcean-related module names all have the *digital_ocean_* prefix
because up until Ansible 2.8, all modules lived in the same global
namespace. Now that we are moving them into a separate namespace, we can
safely drop that prefix. We could do that manually, but writing a few
lines of Bash will be faster and more intellectually satisfying: 

```bash
$ source=../../community/general
$ mkdir -p plugins/modules
$ for m in $(find $source/plugins/modules/ -name 'digital_ocean_*.py' -type f)
> do
>   new_name=$(basename $m | sed 's/digital_ocean_//')
>   echo "  Copying $(basename $m) -> $new_name"
>   cp $m plugins/modules/$new_name
> done
```

Next, we need to copy over utility Python files that our modules use. We
can get a list of all such modules by searching for the *module_utils*
imports:

```bash
$ grep -h "ansible_collections.community.general.plugins.module_utils." \
    plugins/modules/*.py | sort | uniq
```

We need to move a single Python file over and then fix the import
statements, which is easy enough to automate:

```bash
$ mkdir plugins/module_utils
$ cp ../../community/general/plugins/module_utils/digital_ocean.py \
    plugins/module_utils/
$ sed -i -e 's/ansible_collections.community.general.plugins/./' \
    plugins/modules/*.py
```

The last thing that we need to fix is the documentation. Because we
renamed the modules during the move, we need to drop the
*digital_ocean_* prefix from the module: `digital_ocean_${module_name}`
part of the `DOCUMENTATION` block. We also need to adjust the EXAMPLES
section and replace the old module names with fully qualified ones. sed
time again:

```bash
$ sed -i -r \
    -e 's/module: +digital_ocean_([^ ]+)/module: 1/' \
    -e 's/digital_ocean_([^ ]+):/digital_ocean.digital_ocean.1:/' \
    plugins/modules/*.py
```

We also need to copy over any documentation fragments that our modules
use. We can identify them by searching for the *community.general.*
string in our modules: 

```bash
$ grep -h -- "- community.general." plugins/modules/*.py | sort | uniq
```

Now, we must repeat the steps we did with the utility files: copy the
documentation fragment files over and update the references. Again,
because our fragment now lives in its own dedicated namespace, we can
rename it into something more meaningful. Since our documentation
fragment contains definitions of common parameters, we will call it
*common*. And we promise that this is the last fix that we do using sed
and regular expressions. ;)

```bash
$ mkdir plugins/doc_fragments
$ cp ../../community/general/plugins/doc_fragments/digital_ocean.py \
    plugins/doc_fragments/common.py
$ sed -i -e 's/community.general.digital_ocean.documentation/digital_ocean.digital_ocean.common/' \
    plugins/modules/*.py
```

And we are done. Time to pat ourselves on the back and commit the work:

```bash
$ git init && git add . && git commit -m "Initial commit"
```

If you are only interested in the final result of this migration, you
can download it from the
[digital_ocean.digital_ocean](https://github.com/xlab-si/digital_ocean.digital_ocean)
GitHub repo. 

## Taking Our New Collection for a Ride

If we want to test our newly created DigitalOcean Ansible Collection, we
need to tell Ansible where it should search for it. We can do that by
settings the *ANSIBLE_COLLECTIONS_PATHS* environment variable to point
to our work directory. How will we know if things work? We will kindly
ask Ansible to print the module documentation for us. 

```bash
$ export ANSIBLE_COLLECTIONS_PATHS=~/work
$ ansible-doc digital_ocean.digital_ocean.domain
```

If all went according to plans, the last command brought up the
documentation for the domain module. Note that we used the domain
module's fully-qualified collection name (FQCN) in the last command. If
we leave out the namespace and collection name parts, Ansible will not
be able to find our module.

And as the ultimate test, we can also run a simple playbook like this one:

```yaml
---
- name: DigitalOcean test playbook
  hosts: localhost
  gather_facts: false

  tasks:
    - name: Create a new droplet
      digital_ocean.digital_ocean.droplet:
        name: mydroplet
        oauth_token: OAUTH_TOKEN
        size: 2gb
        region: sfo1
        image: centos-8-x64
        wait_timeout: 500
```

When we execute the ansible-playbook play.yaml command, Ansible will
yell at us because we provided an invalid authentication token. But we
should not be sad because the error message proves that our module is
working as expected. 

## Where to Go from Here

In today's post, we demonstrated what the initial steps of content
migration are. But the list does not end here. If we were serious about
maintaining Ansible Collections such as this, we would need to add tests
for our modules and set up the CI/CD integration. 

Another thing that we left out of this post is how to push the newly
created Ansible Collection to Ansible Galaxy. We did this not because
publishing a collection is particularly hard, but because it is almost
too easy. All one has to do is get hold of the digital_ocean namespace
and then run the next two commands:

```bash
$ ansible-galaxy collection build
$ ansible-galaxy collection publish \
    --api-key {galaxy API key here} \
    digital_ocean-digital_ocean-1.0.0.tar.gz
```

Publishing a collection that we do not intend to maintain would be a
disservice to the Ansible community. Quality over quantity.

If you need help with migrating existing content into a dedicated
Ansible Collection and maintaining it on the long run,
[contact our experts](https://steampunk.si/#contact-us)
and they will gladly help you out.

Cheers! 
