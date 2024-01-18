---
author: Bianca Henderson
date: 2020-05-04 00:00 UTC
description: The AWX Collection allows Ansible Playbooks to interact
  with AWX and Ansible Tower.
lang: en-us
title: Introducing the AWX and Ansible Tower Collections
---

# Introducing the AWX and Ansible Tower Collections

Ansible Content Collections are a new way of distributing content,
including modules, for Ansible. 

The AWX and Ansible Tower Collections allow Ansible Playbooks to
interact with AWX and Ansible Tower. Much like interacting with AWX or
Red Hat Ansible Tower via the web-based UI or the API, the modules
provided by the AWX Collection are another way to create, update or
delete objects as well as perform tasks such as run jobs, configure
Ansible Tower and more. This article will discuss new updates regarding
this collection, as well as an example playbook and details on how to
run it successfully.

The AWX Collection
[awx.awx](https://galaxy.ansible.com/awx/awx) is the
upstream community distribution available on Ansible Galaxy.  The
downstream supported Ansible Collection
[ansible.tower](https://cloud.redhat.com/ansible/automation-hub/ansible/tower)
is available on Automation Hub alongside the release of Ansible Tower
3.7.

This collection is a replacement for the
[Ansible Tower web modules](https://docs.ansible.com/ansible/latest/modules/list_of_web_infrastructure_modules.html#ansible-tower)
which were previously housed and maintained directly in the
[Ansible repo](https://github.com/ansible/ansible/tree/stable-2.9/lib/ansible/modules/web_infrastructure/ansible_tower).
The modules were initially [added to the AWX source](https://github.com/ansible/awx/pull/4701) in October of 2019,
when collections work began; the `tower_*` modules in Ansible Core were
[marked for official migration](https://github.com/ansible/ansible/pull/67233)
shortly after. 

## Improvements in the AWX Collection

The modules delivered by Ansible Core and the initial versions of the
AWX Collection had a dependency on libraries provided by the
[tower-cli](https://github.com/ansible/tower-cli) project.  Due to the
deprecation of tower-cli, there is work currently being done to remove
that dependency. This has led to a major update to the AWX Collection.

During the removal of tower-cli, we have tried to keep the modules
backwards-compatible with their corresponding version that shipped in
Ansible Core. This way, if you have already leveraged the `tower_*`
modules from Ansible Core, there should be very little work required
when switching to the AWX Collection. For more information, see the
[Deprecation Updates](https://docs.google.com/document/d/1HCPVLmLmNVX59MiAWlOAmnJUMKYfQed6pd64sr3tOLg/edit#heading=h.rfgzmyttyslb)
section below.

In addition, we have standardized the modules' operational logic, thus
making the collections modules more uniform. Previously, each module was
written individually (sometimes by different authors). This caused
subtle differences of behavior for the individual modules. The modules
distributed in the AWX Collection follow a standard pattern, which
provides consistency even if written by different authors.

The syncing of the collection to the Red Hat Ansible Tower versions also
allows the modules' parameters to be kept in sync with the options
available within the web UI and API. As part of the recent changes, we
have added some new
[tooling](https://github.com/ansible/awx/tree/devel/awx_collection/tools)
as well as updated many of the modules to now include parameters for
functionality which have been added to Ansible Tower since the modules
were initially released.

The collection now also provides better support for idempotency as well
as check_mode. In previous versions using check_mode, older modules
would simply ensure that they could connect to the Ansible Tower server
but not indicate if they would have actually made a change to an Ansible
Tower object. The AWX Collections modules will now more accurately
indicate if they would have changed a Tower object via check_mode. 

## Using the AWX Collection

It's very easy to get started with AWX Collection; all you need to do is
install the collection from [Ansible
Galaxy](https://galaxy.ansible.com/awx/awx) in order to interact with
Ansible Tower. This can be done with the command:

```bash
ansible-galaxy collection install awx.awx
```

Once the collection is installed, we can begin writing playbooks to
manage your instance of Ansible Tower.

**Note:** In order to communicate with your Red Hat Ansible Tower
environment, you need to have an instance of it running, with a
dedicated Ansible Tower host address.  

### Setting Up Authentication

The first thing we need to do in order to interact with Red Hat Ansible
Tower is provide authentication. This can be done in several ways, all
of which are backwards-compatible with the old version of the modules.
The following authentication options are available for use:

-   Specify the connection information as module parameters
-   Provide environment variables with the connection information
-   Reference an old tower_cli.cfg file that contains the connection
    information

Below is an example of a tower_cli.cfg file:

```yaml
host: [$HOST_ADDRESS]
verify_ssl: False
tower_username: [$TOWER_USERNAME]
tower_password: [$TOWER_PASSWORD]
oauth_token: [$OAUTH_TOKEN] (if using oauth instead of a password)
```

### Creating a Playbook

Once you have the AWX Collection installed and your authentication
method decided upon, we can begin [writing a
playbook](https://docs.ansible.com/ansible/latest/user_guide/playbooks_intro.html)
to interact with Ansible Tower. In order to activate the collection, the
following code snippet is required at the play level of your playbook:

```yaml
  collections:
    - awx.awx
```

Even if you are running on a version of Ansible that still ships with
the tower\_\* modules, this will cause Ansible to load the modules from
the AWXCollection instead of the versions shipped in Ansible Core. The
rest of your playbook would look identical to a playbook that did not
use the collection. 

In the example playbook below, the authentication information is not
specified in the tasks and would be loaded either from the environment
variables or a tower_cli.cfg file:

```yaml
---
- name: Playbook for Using a Variety of Tower Modules
  hosts: localhost
  gather_facts: false
  collections:
    - awx.awx

  tasks:

  - name: Create a new organization
    tower_organization:
      name: "New Org"
      description: "test org"
      state: present

  - name: Create an Inventory
    tower_inventory:
      name: "New Inventory"
      description: "test inv"
      organization: "New Org"
      state: present

  - name: Create a Host
    tower_host:
      name: "New Host"
      inventory: "New Inventory"
      state: present
      variables:
        foo: bar

  - name: Create a Project
    tower_project:
      name: "New Project"
      organization: "New Org"
      scm_type: git
      scm_url: https://github.com/ansible/test-playbooks.git

  - name: Create a Team
    tower_team:
      name: "Test Team"
      description: "test team"
      organization: "New Org"
      state: present
      validate_certs: false

  - name: Create a Job Template
    tower_job_template:
      name: "Job Template to Launch"
      project: "New Project"
      inventory: "New Inventory"
      playbook: debug.yml
      ask_extra_vars: yes

  - name: Launch the Job Template (w/ extra_vars)!
    tower_job_launch:
      job_template: "Job Template to Launch"
      extra_vars:
        var1: My First Variable
        var2: My Second Variable
        var3: My Third Variable
```


**Note:** Another way to tell Ansible to use a module from a collection
is to fully qualify the modules' name with the collection namespace, as
in this example below:

```yaml
 - name: Launch the Job Template (w/ extra_vars)
    awx.awx.tower_job_launch:
      job_template: "Job Template to Launch"
      extra_vars:
        var1: My First Variable
        var2: My Second Variable
        var3: My Third Variable
```

### Executing the Playbook

Assuming that the playbook above was saved in your current directory as
a file named configure_tower.yml, the following command would run this
playbook:

```bash
$ ansible-playbook -i localhost configure_tower.yml
```

**Note:** If you have issues with Python on your machine, changing the
ansible-playbook command to the following might help:

```bash
$ ansible-playbook -i localhost -e ansible_python_interpreter=$(which python) configure_tower.yml
```

With a properly-installed collection, configured authentication setup
and a correctly-formatted playbook, you should see output similar to
this:

![ansible-blog-screenshot-awx-collection](/images/posts/archive/ansible-blog-screenshot-awx-collection.png)

Upon completion of the playbook, If you navigate to the web UI of your
Red Hat Ansible Tower server, you should be able to see that the
following objects were created:

-   An organization called "New Org"
-   An inventory called "New Inventory" and host called "New Host" within that inventory
-   A project called "New Project"
-   A team called "New Team"
-   A job template called "Job Template to Launch"

In addition, you can see on the Jobs page that the playbook invoked the
job template with the specified extra_vars.  See below:

![bianca collections tower ui](/images/posts/archive/tower-ui-bianca-collections.png)

## Deprecation Updates

During the removal of tower-cli, we attempted to keep the modules as
similar as possible to ease the transition from the old Core modules to
the new collection. Inevitably, some minor changes had to be made;
details of these changes can be found in the "Release and Upgrade"
section of the AWX Collections
[README.md](https://github.com/ansible/awx/blob/devel/awx_collection/README.md#release-and-upgrade-notes)
file. Some changes to mention include:

-   extra_vars parameters no longer support load of variables from a
    file by specifying a `@<file name>` notation. Instead, they now take
    dictionaries. If you were previously loading a file, please use the
    lookup plugin to load the file instead.
-   Some modules no longer return values the way they used to. All
    returns have been unified across the modules and primarily return
    the ID of the object modified.


## Conclusion

It is quite simple and straightforward to get up and running with the
AWX Collection.  Amongst other things, collections enable users to store
their most frequently-used tasks inside of different playbooks, which
can be easily shared as needed.  In a follow-up blog post, we will
discuss contribution and development, as well as how to test any new or
updated modules you may want to add to the collection.
