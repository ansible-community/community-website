---
author: Andrius Benokraitis
date: 2020-12-17 00:00 UTC
description: Migrating to Ansible Collections (Webinar Q&A) from webinar
  hosted on Dec. 8th 2020
lang: en-us
title: Migrating to Ansible Collections Webinar
---

# Migrating to Ansible Collections (Webinar Q&A)

Sean Cavanaugh, Anshul Behl and I recently hosted a webinar entitled "Migrating to Ansible Collections".
Here is a link to the [on-demand webinar replay](https://www.youtube.com/watch?v=Al1ETaamWmc).
This webinar was focused on enabling the Ansible Playbook
writers, looking to move to the wonderful world of Ansible Collections
in existing Ansible 2.9 environments and
beyond.

The webinar was much more popular than we expected, so much so we
didn't have enough time to answer all the questions, so we took all the
questions and put them in this blog to make them available to
everyone.

**I would like to use Ansible to automate an application using a REST API (for example creating a new bitbucket project). Should I be writing a role or a custom module? And should I then publish that as a Collection?**

It depends on how much investment you'd like to make into the module or
role that you develop. For example, creating a role that references the
built-in Ansible URI module can be evaluated versus creating an Ansible
module written in Python. If you were to create a module, it can be
utilized via a role developed by you or the playbook author. Sometimes a
standalone role may be preferred, depending on the exact functionality
or requirements for interfacing with the REST API endpoint. Overall it
is important to keep a clean resource/module mapping, and avoid as much
as an operation/module. There is no right or wrong answer here
unfortunately ("it is in the eyes of the Ansible beholder"), regardless
an Ansible module and/or an Ansible role can be developed and then
included into a Collection for use in Ansible playbooks.  Collections
are the standard way for distributing Ansible Content, which includes
both roles and modules.

**When will we be able to install Collections using a requirements.yml file in an offline environment? Roles seem to work with Git repositories as upstream, but for Collections, it does not seem to work yet and I always want to look online to galaxy.ansible.com. That is, can I use a GitHub URL (like in roles)?**

You can point the ansible-galaxy CLI client to pull Collections from
different sources, please check out the
[following documentation page](https://docs.ansible.com/ansible/latest/user_guide/collections_using.html#installing-a-collection-from-a-git-repository).
Please note that pulling Collections from GitHub (or other sources)
would not be officially supported as part of the Ansible Automation
Platform. It would be best, even with using Community Collections, to
install from Ansible Galaxy.

**Certain modules require additional Python packages, for example pyvmomi for VMware modules. Will Collections at some point be able to include this Python code to make it work?**

In the future we will have a containered technology called Ansible
Execution Environments, which is an abstraction layer above Collections,
allowing for operating system-level components to be installed. There
were [some talks about this at AnsibleFest](https://www.ansible.com/ansiblefest), and a
blog talking about Ansible Builder,
but the current answer is venv's but Soon(tm) will be Execution
Environments.

**When will ansible-doc be able to show docs for a Collection? Using ansible-doc with a FQCN does not work yet.**

ansible-doc works FQCN currently; check the verbose logs to see if
there are some issues discovering the Collection by
ansible-doc.
For example, the following command does
function properly:

```bash
$ ansible-doc infoblox.nios_modules.nios_a_record
```

**How will Ansible Execution Environments work together?**

This topic is in a very active development stage at the moment and will
be covered in upcoming blogs, webinars, and docs. Coming soon, but watch
this space for more information.


**Any particular resources for network automation? I have been struggling to create playbooks on non-standard network devices. I just feel that the online documentation is lacking from the network side.**

Check out our [Network Getting Started guide](https://docs.ansible.com/ansible/latest/network/getting_started/index.html).
The current Ansible connection plug-ins (like `network_cli`, `netconf` and `httpapi`)
have enabled over 75 networking platforms to date. Also, using the
cli_command and cli_config, generic modules could be of help. Take a
look at
[github.com/ansible/workshops](http://github.com/ansible/workshops)
and see if that helps your searching. Also, reaching out to the network
device vendor directly may help, as they may have private Ansible
content available.

**When will Ansible 2.10 be available for Red Hat Linux via yum?**    

Ansible 2.10 will not be made available in RPM format downstream,
please refer to the following link for more details:
[https://access.redhat.com/articles/5392421](https://access.redhat.com/articles/5392421).


**When would Collections be a hard requirement and deprecating the old way (2.9 or earlier)?**

2.10 and newer require Collections, but if there was existing content
in 2.9 migrated out, the current playbooks should just work as they are
utilizing the global runtime.yml file as part of the 2.10 distribution.
Hence why we are focusing on 2.9 + Collections to elongate the
transition process.

**To future proof can I implement this to 2.9 and use FQCN?**

Yes, that should be fine, assuming the Collections were either migrated
from Ansible 2.9 or tested against it if
net-new.

**You can also just put collections: cyberark at the top of the playbook, right? Can you show what that looks like?**

You would need to specify the specific Cyberark namespace.collection
and not just the Cyberark namespace as you have stated. We also
recommend against using the collections keyword and instead use the
fully qualified collections name (FQCN) instead per task (see notes in
the slides).

Using the `collections` keyword:

![webinar Q&A blog 1](/images/posts/archive/webinar-blog-one.png)

Using the recommended way FQCN (fully qualified Collection name):

![Webinar Q&A blog 2](/images/posts/archive/webinar-blog-two.png)

**In our environment, we have customers that rely on cli's as the cli's get developed faster, example aws-cli. Do we anticipate vendors like AWS to contribute faster to the Collections side?**

The Ansible Engineering team actually maintains all AWS Ansible
content, and typically have a "CLI First" or "API First" mentality, but
in general, participating vendors have been great about updating their
Collections for new features!  One of the goals of Ansible Collections
was for partners and certified content to move faster and asynchronously
from Ansible Automation Platform releases, which means both the
community and customers will get new content
faster.

**What site licenses are needed for access to Automation Hub?**  

Any Red Hat Ansible Automation Platform subscription will provide
access to the Automation Hub, and the ability to run a private
Automation Hub in your environment.

**When is the Ansible Execution Environment scheduled to be released?**   

Tentatively the middle of next year (2021) as part of the product, but
the pieces will start becoming available in an ongoing fashion
upstream.

**If all the modules are being moved out into Collections [ansible.builtin] etc., what is still part of the Base/Core?**   

Well a few modules will still be in there, hence "builtin," but those
still might move async. But there is a lot of code running the actual
Ansible executable including how we do parallelism, constructs like
conditionals, loops, blocks, etc, and much moren. Many of which are
things that a lot of Ansible users don't really interact with (think of
it like an engine in your car).

**Is it possible to use multiple versions of a Collection within the same codebase? (ie list the version on the playbook level)**

That is not an option currently, you cannot pin the Collection version
in the playbook, this will most likely be ideal when using a venv or
future execution environments.

**Can the private Automation Hub be a repo in a binary repo like artifactory or nexus?**

No, private Automation Hub leverages the same content types in
cloud.redhat.com. Ansible Collection tarballs built and published to
Automation Hub are decompressed and contents are
shown.

**Could I use Ansible Collections on CentOS8?**

If Ansible 2.9 is installable on CentOS8 (or any other Linux
distribution), then Collections can be utilized
there.

**Would Galaxy be deprecated or still working in the future?** 

Galaxy is still the current place to publish and download Community
Ansible Collections!

**Ansible 2.9 doesn't support using private repos as placeholders for Collections, correct?**

You can use private Automation Hub to point to a self hosted instance
for your Collections and curate and control what your group has access
to.

**Is the private Automation Hub standalone or can it be clustered?**

It's currently only available as standalone, but may be cluster-enabled
in the future.

**How does the FQCN use the Collection and not the regular mapped module (in 2.9)?**

FQCN stands for fully qualified collection name and it will always
point to a Collection and not a module inside the standard Ansible 2.9
installation, as they reside in different locations on the Ansible
control node.

**What's the difference between Execution Environments and the Container Isolated Groups which are in tech preview in Red Hat Ansible Tower?**

Container Isolated Groups use the same execution principles. The
easiest way to think about this is that you can consider container
groups as being built on "Execution Environments v0.1." When Execution
Environments are released, this will become far superior than container
groups.

**Is there a means to download the :latest Collection version? Or is that what you get automatically?**

Latest version is pulled automatically, but you can specify the exact
version as well. You don't need to use :latest - that's what you get
automatically, assuming it doesn\'t have something like "-beta" or
prerelease versions (using hyphens) as part of it, which are not
considered GA releases (and skipped).

[![webinar Q&A blog 3](/images/posts/archive/webinar-blog-three.png)

**For roles we write ourselves, is there or will there be a way to organize related roles as a Collection?**

Multiple roles can be organized inside a Collection today as part of the /roles directory.

**Everything I've seen about Collections has been how to use ones (from Galaxy or other sources). Is there any documentation/reference about how to write our own Collection?**

Yes! Check out the [Developer Guide](https://docs.ansible.com/ansible/latest/dev_guide/index.html)

**Will Automation Hub contain the official/prominent vendor modules. An example is a NetApp or Dell module.**

Yes, it already contains that today, we have a certification program
and we have certified content from a lot of vendors like Dell and
Netapp. Automation Hub contains all supported and Certified Collections,
there is a public KBASE that lists them, please check
[https://access.redhat.com/articles/3642632](https://access.redhat.com/articles/3642632)[.

**If I choose to take a trial of Ansible Automation Platform, will it allow access to the Automation Hub?**

Yes it will as part of the subscription; an Ansible Automation Platform
subscription includes everything to trial, including all components and
connectivity to services on cloud.redhat.com, and the Red Hat Customer
Portal.

**Is deleting a Collection from ansible-galaxy CLI coming soon, or do we still have to go into the Collections directory to manually delete it?**

Right now, that is the only way to delete a collection.  You can
overwrite a collection using the
[force flag](https://docs.ansible.com/ansible/latest/cli/ansible-galaxy.html#cmdoption-ansible-galaxy-collection-init-f).

**Can we install the Collection somewhere besides the default ~/.ansible/collections?**

Yes, you can put them anywhere, but make sure the control node knows
where they are in the path. For example: `ansible-galaxy install -p /path/to/collections namespace.collection` and
[associated documentation](https://docs.ansible.com/ansible/latest/cli/ansible-galaxy.html#cmdoption-ansible-galaxy-collection-install-p).

**Can I check the version of an existing Collection on my server?**

The [ansible-galaxy collection list](https://docs.ansible.com/ansible/latest/cli/ansible-galaxy.html#collection-list)
command provides a list of Collections and versions for Ansible 2.10 and
newer.

**For adding a new host in RHV, I had to downgrade the last ansible version to 2.9.13 otherwise it did not work (a known bug by Red Hat). In which 2.9 version will the bug be solved?**

Do you have a GitHub issue we can see? We can make sure to follow up.
Bugs are usually tracked on GitHub Ansible project and the conversations
there should help you understand a timeline.

**What's the future path for users that have absolutely zero interest in things changing? I have been working toward changing department culture toward an automation friendly way of thinking for a year or two, and this will effectively put me back to square one, if not further back. Change resistant businesses don't like big changes just as they get ready to implement.**

We think we have created a win/win scenario
where customers and community members can now use Collections and get
new content faster, while maintaining backwards compatibility with
existing Ansible Automation.  While we encourage folks to start using
Collections and writing Ansible playbooks with FQCNs, there will be a
long period of time before customers are required to use them.  Red Hat
does offer long term support options/offerings, so you are not forced to
change for considerable time. Ansible 2.9 will be supported much longer
than originally planned, for subscribing
customers.

**Is there a set of paths that Ansible will check for runtime.yml defined in base ansible?**

Redirection rules currently follow a precedence, waterfall between the
following two files:

1.  The built-in `runtime.yml` file as part of the Ansible distribution. In this example, the [Ansible 2.10 built-in runtime.yml](https://github.com/ansible/ansible/blob/devel/lib/ansible/config/ansible_builtin_runtime.yml). This file is consulted first.
2.  The runtime.yml file as part of the actual Collection as the `/meta/runtime.yml`. This file is consulted next.
