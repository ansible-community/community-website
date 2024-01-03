---
author: Andrius Benokraitis
date: 2020-12-17 00:00 UTC
description: Migrating to Ansible Collections (Webinar Q&A) from webinar
  hosted on Dec. 8th 2020
lang: en-us
title: Migrating to Ansible Collections Webinar
---

# Migrating to Ansible Collections (Webinar Q&A)

[Sean Cavanaugh, Anshul Behl and I recently hosted a webinar entitled
"Migrating to Ansible Collections" (link to YouTube
]{style="color: #000000;"}[on-demand webinar
replay](https://www.youtube.com/watch?v=Al1ETaamWmc)[ and link to
]{style="color: #000000;"}[PDF
slides](https://www.ansible.com/hubfs/Webinar%20PDF%20slides/2020-Dec-08--Webinar%20Migrating%20to%20Ansible%20Collections.pdf)[
download). This webinar was focused on enabling the Ansible Playbook
writers, looking to move to the wonderful world of Ansible Collections
in existing Ansible 2.9 environments and
beyond.]{style="color: #000000;"}

[![Screen Shot 2020-12-16 at 4.04.32
PM](https://www.ansible.com/hs-fs/hubfs/Screen%20Shot%202020-12-16%20at%204.04.32%20PM.png?width=1310&name=Screen%20Shot%202020-12-16%20at%204.04.32%20PM.png){width="1310"
style="width: 1310px;"
srcset="https://www.ansible.com/hs-fs/hubfs/Screen%20Shot%202020-12-16%20at%204.04.32%20PM.png?width=655&name=Screen%20Shot%202020-12-16%20at%204.04.32%20PM.png 655w, https://www.ansible.com/hs-fs/hubfs/Screen%20Shot%202020-12-16%20at%204.04.32%20PM.png?width=1310&name=Screen%20Shot%202020-12-16%20at%204.04.32%20PM.png 1310w, https://www.ansible.com/hs-fs/hubfs/Screen%20Shot%202020-12-16%20at%204.04.32%20PM.png?width=1965&name=Screen%20Shot%202020-12-16%20at%204.04.32%20PM.png 1965w, https://www.ansible.com/hs-fs/hubfs/Screen%20Shot%202020-12-16%20at%204.04.32%20PM.png?width=2620&name=Screen%20Shot%202020-12-16%20at%204.04.32%20PM.png 2620w, https://www.ansible.com/hs-fs/hubfs/Screen%20Shot%202020-12-16%20at%204.04.32%20PM.png?width=3275&name=Screen%20Shot%202020-12-16%20at%204.04.32%20PM.png 3275w, https://www.ansible.com/hs-fs/hubfs/Screen%20Shot%202020-12-16%20at%204.04.32%20PM.png?width=3930&name=Screen%20Shot%202020-12-16%20at%204.04.32%20PM.png 3930w"
sizes="(max-width: 1310px) 100vw, 1310px"}]{style="color: #000000;"}

 

[The webinar was much more popular than we expected, so much so we
didn't have enough time to answer all the questions, so we took all the
questions and put them in this blog to make them available to
everyone.]{style="color: #000000;"}

 

**[I would like to use Ansible to automate an application using a REST
API (for example creating a new bitbucket project). Should I be writing
a role or a custom module? And should I then publish that as a
Collection? ]{style="color: #3d85c6;"}**[   ]{style="color: #000000;"}

[It depends on how much investment you'd like to make into the module or
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
both roles and modules.]{style="color: #000000;"}

 

**[When will we be able to install Collections using a requirements.yml
file in an offline environment? Roles seem to work with Git repositories
as upstream, but for Collections, it does not seem to work yet and I
always want to look online to galaxy.ansible.com. That is, can I use a
GitHub URL (like in
roles)?]{style="color: #3d85c6;"}**[  ]{style="color: #000000;"}

[You can point the ansible-galaxy CLI client to pull Collections from
different sources, please check out the
]{style="color: #000000;"}[following documentation
page](https://docs.ansible.com/ansible/latest/user_guide/collections_using.html#installing-a-collection-from-a-git-repository)[.
Please note that pulling Collections from GitHub (or other sources)
would not be officially supported as part of the Ansible Automation
Platform. It would be best, even with using Community Collections, to
install from Ansible Galaxy.]{style="color: #000000;"}


**[Certain modules require additional Python packages, for example
pyvmomi for VMware modules. Will Collections at some point be able to
include this Python code to make it work? ]{style="color: #3d85c6;"}**

[In the future we will have a containered technology called Ansible
Execution Environments, which is an abstraction layer above Collections,
allowing for operating system-level components to be installed. There
were ]{style="color: #000000;"}[some talks about this at
AnsibleFest](https://www.ansible.com/ansiblefest)[, and a
]{style="color: #000000;"}[blog talking about Ansible
Builder](https://www.ansible.com/blog/introduction-to-ansible-builder)[,
but the current answer is venv\'s but Soon(tm) will be Execution
Environments.]{style="color: #000000;"}

**[When will ansible-doc be able to show docs for a Collection? Using
ansible-doc with a FQCN does not work
yet.]{style="color: #3d85c6;"}**[    ]{style="color: #000000;"}

[ansible-doc works FQCN currently; check the verbose logs to see if
there are some issues discovering the Collection by
ansible-doc.]{style="color: #000000;"}[\
]{style="color: #000000;"}[For example, the following command does
function properly:]{style="color: #000000;"}

[[\$ ]{style="color: #000000;"}[ansible-doc
infoblox.nios_modules.nios_a\_record]{style="color: #000000;"}

 

**[How will Ansible Execution Environments work together? Guess this
isn\'t really part of the webinar :)]{style="color: #3d85c6;"}**

[This topic is in a very active development stage at the moment and will
be covered in upcoming blogs, webinars, and docs. Coming soon, but watch
this space for more information.]{style="color: #000000;"}

 

**[Any particular resources for network automation? I have been
struggling to create playbooks on non-standard network devices. I just
feel that the online documentation is lacking from the network
side.]{style="color: #3d85c6;"}**[    ]{style="color: #000000;"}

[Check out our]{style="color: #000000;"}[ Network Getting Started
guide](https://docs.ansible.com/ansible/latest/network/getting_started/index.html)[.
The current Ansible connection plug-ins (like
]{style="color: #000000;"}[[network_cli]{style="color: #000000;"}[,
]{style="color: #000000;"}[netconf]{style="color: #000000;"}[
and
]{style="color: #000000;"}[httpapi]{style="color: #000000; font-family: 'courier new', courier;"}[)
have enabled over 75 networking platforms to date. Also, using the
cli_command and cli_config, generic modules could be of help. Take a
look at
]{style="color: #000000;"}[github.com/ansible/workshops](http://github.com/ansible/workshops)[
and see if that helps your searching. Also, reaching out to the network
device vendor directly may help, as they may have private Ansible
content available.]{style="color: #000000;"}

 

**[When will Ansible 2.10 be available for Red Hat Linux via
yum?]{style="color: #3d85c6;"}**[    ]{style="color: #000000;"}

[Ansible 2.10 will not be made available in RPM format downstream,
please refer to the following link for more details:
]{style="color: #000000;"}[https://access.redhat.com/articles/5392421](https://access.redhat.com/articles/5392421)[.]{style="color: #000000;"}

 

**[When would Collections be a hard requirement and deprecating the old
way (2.9 or earlier)?]{style="color: #3d85c6;"}**

[2.10 and newer require Collections, but if there was existing content
in 2.9 migrated out, the current playbooks should just work as they are
utilizing the global runtime.yml file as part of the 2.10 distribution.
Hence why we are focusing on 2.9 + Collections to elongate the
transition process.]{style="color: #000000;"}

 

**[To future proof can I implement this to 2.9 and use FQCN?
]{style="color: #3d85c6;"}**[   ]{style="color: #000000;"}

[Yes, that should be fine, assuming the Collections were either migrated
from Ansible 2.9 or tested against it if
net-new.]{style="color: #000000;"}

 

**[You can also just put collections: cyberark at the top of the
playbook, right? Can you show what that looks
like?]{style="color: #3d85c6;"}**[    ]{style="color: #000000;"}

[You would need to specify the specific Cyberark namespace.collection
and not just the Cyberark namespace as you have stated. We also
recommend against using the collections keyword and instead use the
fully qualified collections name (FQCN) instead per task (see notes in
the slides).]{style="color: #000000;"}

[Using the
]{style="color: #000000;"}[collections]{style="color: #000000; font-family: 'courier new', courier;"}[
keyword: ]{style="color: #000000;"}

![webinar Q&A blog
1](https://www.ansible.com/hs-fs/hubfs/webinar%20Q%26A%20blog%201.png?width=1350&name=webinar%20Q%26A%20blog%201.png){style="width: 1350px;"
width="1350"
srcset="https://www.ansible.com/hs-fs/hubfs/webinar%20Q%26A%20blog%201.png?width=675&name=webinar%20Q%26A%20blog%201.png 675w, https://www.ansible.com/hs-fs/hubfs/webinar%20Q%26A%20blog%201.png?width=1350&name=webinar%20Q%26A%20blog%201.png 1350w, https://www.ansible.com/hs-fs/hubfs/webinar%20Q%26A%20blog%201.png?width=2025&name=webinar%20Q%26A%20blog%201.png 2025w, https://www.ansible.com/hs-fs/hubfs/webinar%20Q%26A%20blog%201.png?width=2700&name=webinar%20Q%26A%20blog%201.png 2700w, https://www.ansible.com/hs-fs/hubfs/webinar%20Q%26A%20blog%201.png?width=3375&name=webinar%20Q%26A%20blog%201.png 3375w, https://www.ansible.com/hs-fs/hubfs/webinar%20Q%26A%20blog%201.png?width=4050&name=webinar%20Q%26A%20blog%201.png 4050w"
sizes="(max-width: 1350px) 100vw, 1350px"}

Using the recommended way FQCN (fully qualified Collection name):

![Webinar Q&A blog
2](https://www.ansible.com/hs-fs/hubfs/Webinar%20Q%26A%20blog%202.png?width=689&name=Webinar%20Q%26A%20blog%202.png){style="width: 689px;"
width="689"
srcset="https://www.ansible.com/hs-fs/hubfs/Webinar%20Q%26A%20blog%202.png?width=345&name=Webinar%20Q%26A%20blog%202.png 345w, https://www.ansible.com/hs-fs/hubfs/Webinar%20Q%26A%20blog%202.png?width=689&name=Webinar%20Q%26A%20blog%202.png 689w, https://www.ansible.com/hs-fs/hubfs/Webinar%20Q%26A%20blog%202.png?width=1034&name=Webinar%20Q%26A%20blog%202.png 1034w, https://www.ansible.com/hs-fs/hubfs/Webinar%20Q%26A%20blog%202.png?width=1378&name=Webinar%20Q%26A%20blog%202.png 1378w, https://www.ansible.com/hs-fs/hubfs/Webinar%20Q%26A%20blog%202.png?width=1723&name=Webinar%20Q%26A%20blog%202.png 1723w, https://www.ansible.com/hs-fs/hubfs/Webinar%20Q%26A%20blog%202.png?width=2067&name=Webinar%20Q%26A%20blog%202.png 2067w"
sizes="(max-width: 689px) 100vw, 689px"}

 

**[In our environment, we have customers that rely on cli\'s as the
cli\'s get developed faster, example aws-cli. Do we anticipate vendors
like AWS to contribute faster to the Collections
side?]{style="color: #3d85c6;"}**[    ]{style="color: #000000;"}

[The Ansible Engineering team actually maintains all AWS Ansible
content, and typically have a "CLI First" or "API First" mentality, but
in general, participating vendors have been great about updating their
Collections for new features!  One of the goals of Ansible Collections
was for partners and certified content to move faster and asynchronously
from Ansible Automation Platform releases, which means both the
community and customers will get new content
faster.]{style="color: #000000;"}

 

**[What site licenses are needed for access to Automation
Hub?]{style="color: #3d85c6;"}**[    ]{style="color: #000000;"}

[Any Red Hat Ansible Automation Platform subscription will provide
access to the Automation Hub, and the ability to run a private
Automation Hub in your environment.]{style="color: #000000;"}

 

**[When is the Ansible Execution Environment scheduled to be
released?]{style="color: #3d85c6;"}**[    ]{style="color: #000000;"}

[Tentatively the middle of next year (2021) as part of the product, but
the pieces will start becoming available in an ongoing fashion
upstream.]{style="color: #000000;"}

 

**[If all the modules are being moved out into Collections
(]{style="color: #3d85c6;"}[ansible.builtin]{style="color: #3d85c6;"}[,
etc.), what is still part of the
Base/Core?]{style="color: #3d85c6;"}**[    ]{style="color: #000000;"}

[Well a few modules will still be in there, hence "builtin," but those
still might move async. But there is a lot of code running the actual
Ansible executable including how we do parallelism, constructs like
conditionals, loops, blocks, etc, and much moren. Many of which are
things that a lot of Ansible users don\'t really interact with (think of
it like an engine in your car).]{style="color: #000000;"}

 

**[Is it possible to use multiple versions of a Collection within the
same codebase? (ie list the version on the playbook
level)]{style="color: #3d85c6;"}**

[That is not an option currently, you cannot pin the Collection version
in the playbook, this will most likely be ideal when using a venv or
future execution environments.]{style="color: #000000;"}

 

**[Can the private Automation Hub be a repo in a binary repo like
artifactory or
nexus?]{style="color: #3d85c6;"}**[    ]{style="color: #000000;"}

[No, private Automation Hub leverages the same content types in
cloud.redhat.com. Ansible Collection tarballs built and published to
Automation Hub are decompressed and contents are
shown.]{style="color: #000000;"}

[\
]{style="color: #000000;"}**[Could I use Ansible Collections on
CentOS8?]{style="color: #3d85c6;"}**

[If Ansible 2.9 is installable on CentOS8 (or any other Linux
distribution), then Collections can be utilized
there.]{style="color: #000000;"}

 

**[Would Galaxy be deprecated or still working in the
future?]{style="color: #3d85c6;"}**[    ]{style="color: #000000;"}

[Galaxy is still the current place to publish and download Community
Ansible Collections!]{style="color: #000000;"}

 

**[Ansible 2.9 doesn\'t support using private repos as placeholders for
Collections, correct?]{style="color: #3d85c6;"}**

[You can use private Automation Hub to point to a self hosted instance
for your Collections and curate and control what your group has access
to.  Read more about ]{style="color: #000000;"}[Private Automation Hub
on our
blog](https://www.ansible.com/blog/control-your-content-with-private-automation-hub)[.]{style="color: #000000;"}

 

**[Is the private Automation Hub standalone or can it be
clustered?]{style="color: #3d85c6;"}**

[It's currently only available as standalone, but may be cluster-enabled
in the future.]{style="color: #000000;"}

 

**[How does the FQCN use the Collection and not the regular mapped
module (in 2.9) ?]{style="color: #3d85c6;"}**

[FQCN stands for fully qualified collection name and it will always
point to a Collection and not a module inside the standard Ansible 2.9
installation, as they reside in different locations on the Ansible
control node.]{style="color: #000000;"}

 

**[What\'s the difference between Execution Environments and the
Container Isolated Groups which are in tech preview in Red Hat Ansible
Tower?]{style="color: #3d85c6;"}**

[Container Isolated Groups use the same execution principles. The
easiest way to think about this is that you can consider container
groups as being built on "Execution Environments v0.1." When Execution
Environments are released, this will become far superior than container
groups.]{style="color: #000000;"}

 

**[Is there a means to download the :latest Collection version?  Or is
that what you get automatically?]{style="color: #3d85c6;"}**

[Latest version is pulled automatically, but you can specify the exact
version as well. You don\'t need to use :latest - that\'s what you get
automatically, assuming it doesn\'t have something like \"-beta\" or
prerelease versions (using hyphens) as part of it, which are not
considered GA releases (and skipped).]{style="color: #000000;"}[\
]{style="color: #000000;"}

[![webinar Q&A blog
3](https://www.ansible.com/hs-fs/hubfs/webinar%20Q%26A%20blog%203.png?width=1600&name=webinar%20Q%26A%20blog%203.png){style="width: 1600px;"
width="1600"
srcset="https://www.ansible.com/hs-fs/hubfs/webinar%20Q%26A%20blog%203.png?width=800&name=webinar%20Q%26A%20blog%203.png 800w, https://www.ansible.com/hs-fs/hubfs/webinar%20Q%26A%20blog%203.png?width=1600&name=webinar%20Q%26A%20blog%203.png 1600w, https://www.ansible.com/hs-fs/hubfs/webinar%20Q%26A%20blog%203.png?width=2400&name=webinar%20Q%26A%20blog%203.png 2400w, https://www.ansible.com/hs-fs/hubfs/webinar%20Q%26A%20blog%203.png?width=3200&name=webinar%20Q%26A%20blog%203.png 3200w, https://www.ansible.com/hs-fs/hubfs/webinar%20Q%26A%20blog%203.png?width=4000&name=webinar%20Q%26A%20blog%203.png 4000w, https://www.ansible.com/hs-fs/hubfs/webinar%20Q%26A%20blog%203.png?width=4800&name=webinar%20Q%26A%20blog%203.png 4800w"
sizes="(max-width: 1600px) 100vw, 1600px"}]{style="color: #000000;"}

**[For roles we write ourselves, is there or will there be a way to
organize related roles as a
Collection?]{style="color: #3d85c6;"}**[    ]{style="color: #000000;"}

[Multiple roles can be organized inside a Collection today as part of
the /roles directory.]{style="color: #000000;"}

[ ]{style="color: #000000;"}

**[Everything I\'ve seen about Collections has been how to use ones
(from Galaxy or other sources). Is there any documentation/reference
about how to write our own Collection?]{style="color: #3d85c6;"}**

[Yes! Check out the ]{style="color: #000000;"}[Developer
Guide](https://docs.ansible.com/ansible/latest/dev_guide/index.html)[ on
docs.redhat.com.]{style="color: #000000;"}

[ ]{style="color: #000000;"}

**[Will Automation Hub contain the official/prominent vendor modules. An
example is a NetApp or Dell
module.]{style="color: #3d85c6;"}**[ ]{style="color: #000000;"}

[Yes, it already contains that today, we have a certification program
and we have certified content from a lot of vendors like Dell and
Netapp. Automation Hub contains all supported and Certified Collections,
there is a public KBASE that lists them, please check
]{style="color: #000000;"}[https://access.redhat.com/articles/3642632](https://access.redhat.com/articles/3642632)[.]{style="color: #000000;"}

[ ]{style="color: #000000;"}

**[If I choose to take a trial of Ansible Automation Platform, will it
allow access to the Automation Hub?]{style="color: #3d85c6;"}**

[Yes it will as part of the subscription; an Ansible Automation Platform
subscription includes everything to trial, including all components and
connectivity to services on cloud.redhat.com, and the Red Hat Customer
Portal. To get a trial sign up at
]{style="color: #000000;"}[red.ht/try_ansible](https://red.ht/try_ansible)[.]{style="color: #000000;"}

[ ]{style="color: #000000;"}

**[Is deleting a Collection from ansible-galaxy CLI coming soon, or do
we still have to go into the Collections directory to manually delete
it?]{style="color: #3d85c6;"}**

[Right now, that is the only way to delete a collection.  You can
overwrite a collection using the ]{style="color: #000000;"}[force
flag](https://docs.ansible.com/ansible/latest/cli/ansible-galaxy.html#cmdoption-ansible-galaxy-collection-init-f)[.]{style="color: #000000;"}

[ ]{style="color: #000000;"}

**[Can we install the Collection somewhere besides the default -
\~/.ansible/collections?]{style="color: #3d85c6;"}**

[Yes, you can put them anywhere, but make sure the control node knows
where they are in the path. For example: ansible-galaxy install -p
/path/to/collections namespace.collection and
]{style="color: #000000;"}[associated
documentation](https://docs.ansible.com/ansible/latest/cli/ansible-galaxy.html#cmdoption-ansible-galaxy-collection-install-p)[.]{style="color: #000000;"}

[ ]{style="color: #000000;"}

**[Can I check the version of an existing Collection on my
server?]{style="color: #3d85c6;"}**

[The ]{style="color: #000000;"}[ansible-galaxy collection
list]{style="color: #000000; font-family: 'courier new', courier;"}
[command](https://docs.ansible.com/ansible/latest/cli/ansible-galaxy.html#collection-list)[
provides a list of Collections and versions for Ansible 2.10 and
newer.]{style="color: #000000;"}

[ ]{style="color: #000000;"}

**[For adding a new host in RHV, I had to downgrade the last ansible
version to 2.9.13 otherwise it did not work (a known bug by Red Hat). In
which 2.9 version will the bug be solved?]{style="color: #3d85c6;"}**

[Do you have a GitHub issue we can see? We can make sure to follow up.
Bugs are usually tracked on GitHub Ansible project and the conversations
there should help you understand a timeline.]{style="color: #000000;"}

[ ]{style="color: #000000;"}

**[What\'s the future path for users that have absolutely zero interest
in things changing? I have been working toward changing department
culture toward an automation friendly way of thinking for a year or two,
and this will effectively put me back to square one, if not further
back. Change resistant businesses don\'t like big changes just as they
get ready to implement.]{style="color: #3d85c6;"}**

[\
]{style="color: #000000;"}[We think we have created a win/win scenario
where customers and community members can now use Collections and get
new content faster, while maintaining backwards compatibility with
existing Ansible Automation.  While we encourage folks to start using
Collections and writing Ansible playbooks with FQCNs, there will be a
long period of time before customers are required to use them.  Red Hat
does offer long term support options/offerings, so you are not forced to
change for considerable time. Ansible 2.9 will be supported much longer
than originally planned, for subscribing
customers.]{style="color: #000000;"}

[ ]{style="color: #000000;"}

**[Is there a set of paths that Ansible will check for runtime.yml
defined in base ansible?]{style="color: #3d85c6;"}**

[Redirection rules currently follow a precedence, waterfall between the
following two files:]{style="color: #000000;"}

1.  [The built-in runtime.yml file as part of the Ansible distribution
    (in this example, the ]{style="color: #000000;"}[Ansible 2.10
    built-in
    runtime.yml](https://github.com/ansible/ansible/blob/devel/lib/ansible/config/ansible_builtin_runtime.yml)[.
    This file is consulted first.]{style="color: #000000;"}
2.  [The runtime.yml file as part of the actual Collection as the
    /meta/runtime.yml. This file is consulted
    next.]{style="color: #000000;"}
