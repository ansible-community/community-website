---
author: Ajay Chenampara
date: 2020-03-24 00:00 UTC
description: In this blog post we\'ll walk through a use case wherein,
  the user would like to use a Red Hat certified collection from
  Automation Hub and also use a community supported collection from
  Ansible Galaxy.
lang: en-us
title: Hands on with Ansible collections
---

# Hands on with Ansible collections

Ansible collections have been introduced previously through two of our
blogs [Getting Started with Ansible Content
Collections](https://www.ansible.com/blog/getting-started-with-ansible-collections)
and [The Future of Ansible Content
Delivery](https://www.ansible.com/blog/the-future-of-ansible-content-delivery).
In essence, Ansible Automation content is going to be delivered using
the collection packaging mechanism.  Ansible Content refers to Ansible
Playbooks, modules, module utilities and plugins. Basically all the
Ansible tools that users use to create their Ansible Automation. Content
is divided between two repositories:

1.  Ansible Galaxy
    ([https://galaxy.ansible.com](https://galaxy.ansible.com/))
2.  Automation Hub (<https://cloud.redhat.com/ansible/automation-hub>)

Ansible Galaxy is the upstream community for sharing Ansible
Collections.  Any community user can create a namespace and share
content with anyone. Access to Automation Hub is included with a Red Hat
Ansible Automation Platform subscription.  Automation Hub only contains
fully supported and certified content from Red Hat and our partners.
This makes it easier for Red Hat customers to determine which content is
the official certified, and importantly supported, content.  This
includes full content from partners such as Arista, Cisco, Checkpoint,
F5, IBM, Microsoft and NetApp. 

In this blog post we\'ll walk through a use case wherein, the user would
like to use a Red Hat certified collection from Automation Hub and also
use a community supported collection from Ansible Galaxy.

There are different ways to interact with Ansible Collections and your
Ansible Automation:

1.  Install into your runtime environment or virtual env
2.  Provide as part of your SCM tree
3.  Using a requirements file

Regardless of the method chosen, first you need to find, identity and
obtain the Ansible Collections you want to use.

## Ansible Playbook repo structure:

Here is my setup for this demonstration of Ansible Collections:

![Ajay blog
1](https://www.ansible.com/hs-fs/hubfs/Ajay%20blog%201.png?width=177&name=Ajay%20blog%201.png){width="177"
style="width: 177px;"
srcset="https://www.ansible.com/hs-fs/hubfs/Ajay%20blog%201.png?width=89&name=Ajay%20blog%201.png 89w, https://www.ansible.com/hs-fs/hubfs/Ajay%20blog%201.png?width=177&name=Ajay%20blog%201.png 177w, https://www.ansible.com/hs-fs/hubfs/Ajay%20blog%201.png?width=266&name=Ajay%20blog%201.png 266w, https://www.ansible.com/hs-fs/hubfs/Ajay%20blog%201.png?width=354&name=Ajay%20blog%201.png 354w, https://www.ansible.com/hs-fs/hubfs/Ajay%20blog%201.png?width=443&name=Ajay%20blog%201.png 443w, https://www.ansible.com/hs-fs/hubfs/Ajay%20blog%201.png?width=531&name=Ajay%20blog%201.png 531w"
sizes="(max-width: 177px) 100vw, 177px"}

-   ansible.cfg is the Ansible configuration file.  I will elaborate on
    this in the next section.
-   collections is a directory storing all Ansible Collections that my
    Ansible Playbook will use
-   inventory is a directory containing a inventory file named hosts
-   play.yaml is my Ansible Playbook

For my example this is a development environment where I just want to
download the latest and greatest.  I will use a gitignore file to ignore
the downloaded content and only track the requirements file.

![Ajay blog
2](https://www.ansible.com/hs-fs/hubfs/Ajay%20blog%202.png?width=551&name=Ajay%20blog%202.png){width="551"
style="width: 551px;"
srcset="https://www.ansible.com/hs-fs/hubfs/Ajay%20blog%202.png?width=276&name=Ajay%20blog%202.png 276w, https://www.ansible.com/hs-fs/hubfs/Ajay%20blog%202.png?width=551&name=Ajay%20blog%202.png 551w, https://www.ansible.com/hs-fs/hubfs/Ajay%20blog%202.png?width=827&name=Ajay%20blog%202.png 827w, https://www.ansible.com/hs-fs/hubfs/Ajay%20blog%202.png?width=1102&name=Ajay%20blog%202.png 1102w, https://www.ansible.com/hs-fs/hubfs/Ajay%20blog%202.png?width=1378&name=Ajay%20blog%202.png 1378w, https://www.ansible.com/hs-fs/hubfs/Ajay%20blog%202.png?width=1653&name=Ajay%20blog%202.png 1653w"
sizes="(max-width: 551px) 100vw, 551px"}

This gitignore file helps ensure that your playbook repository content
in the version control system only tracks your playbook and related
files.  If you want to track Ansible Collections being used in your SCM
just remove the Git ignore (e.g. the **2- Provide as part of your SCM
tree** in the introduction).  For a more in-depth look into using
collections and the folder structure please refer to the
[documentation](https://docs.ansible.com/ansible/latest/user_guide/collections_using.html#using-collections).

## Configuring access to Automation Hub and Galaxy 

For accessing certified content from the Automation Hub, you will need
to first get the token for authentication. Do this by logging into
[https://cloud.redhat.com](https://cloud.redhat.com/) and then
navigating to <https://cloud.redhat.com/ansible/automation-hub/token> 

![Ajay blog
3](https://www.ansible.com/hs-fs/hubfs/Ajay%20blog%203.png?width=1600&name=Ajay%20blog%203.png){width="1600"
style="width: 1600px;"
srcset="https://www.ansible.com/hs-fs/hubfs/Ajay%20blog%203.png?width=800&name=Ajay%20blog%203.png 800w, https://www.ansible.com/hs-fs/hubfs/Ajay%20blog%203.png?width=1600&name=Ajay%20blog%203.png 1600w, https://www.ansible.com/hs-fs/hubfs/Ajay%20blog%203.png?width=2400&name=Ajay%20blog%203.png 2400w, https://www.ansible.com/hs-fs/hubfs/Ajay%20blog%203.png?width=3200&name=Ajay%20blog%203.png 3200w, https://www.ansible.com/hs-fs/hubfs/Ajay%20blog%203.png?width=4000&name=Ajay%20blog%203.png 4000w, https://www.ansible.com/hs-fs/hubfs/Ajay%20blog%203.png?width=4800&name=Ajay%20blog%203.png 4800w"
sizes="(max-width: 1600px) 100vw, 1600px"}

Clicking on the ![ajay blog
4](https://www.ansible.com/hs-fs/hubfs/ajay%20blog%204.png?width=114&name=ajay%20blog%204.png){width="114"
style="width: 114px;"
srcset="https://www.ansible.com/hs-fs/hubfs/ajay%20blog%204.png?width=57&name=ajay%20blog%204.png 57w, https://www.ansible.com/hs-fs/hubfs/ajay%20blog%204.png?width=114&name=ajay%20blog%204.png 114w, https://www.ansible.com/hs-fs/hubfs/ajay%20blog%204.png?width=171&name=ajay%20blog%204.png 171w, https://www.ansible.com/hs-fs/hubfs/ajay%20blog%204.png?width=228&name=ajay%20blog%204.png 228w, https://www.ansible.com/hs-fs/hubfs/ajay%20blog%204.png?width=285&name=ajay%20blog%204.png 285w, https://www.ansible.com/hs-fs/hubfs/ajay%20blog%204.png?width=342&name=ajay%20blog%204.png 342w"
sizes="(max-width: 114px) 100vw, 114px"} button will reveal your
authentication token. Save this information somewhere, we will need to
enter this into the ansible.cfg file. Ansible Galaxy also has an API
token used for authentication and can be accessed by navigating to
<https://galaxy.ansible.com/me/preferences> after logging in.

![Ajay blog
5](https://www.ansible.com/hs-fs/hubfs/Ajay%20blog%205.png?width=1600&name=Ajay%20blog%205.png){width="1600"
style="width: 1600px;"
srcset="https://www.ansible.com/hs-fs/hubfs/Ajay%20blog%205.png?width=800&name=Ajay%20blog%205.png 800w, https://www.ansible.com/hs-fs/hubfs/Ajay%20blog%205.png?width=1600&name=Ajay%20blog%205.png 1600w, https://www.ansible.com/hs-fs/hubfs/Ajay%20blog%205.png?width=2400&name=Ajay%20blog%205.png 2400w, https://www.ansible.com/hs-fs/hubfs/Ajay%20blog%205.png?width=3200&name=Ajay%20blog%205.png 3200w, https://www.ansible.com/hs-fs/hubfs/Ajay%20blog%205.png?width=4000&name=Ajay%20blog%205.png 4000w, https://www.ansible.com/hs-fs/hubfs/Ajay%20blog%205.png?width=4800&name=Ajay%20blog%205.png 4800w"
sizes="(max-width: 1600px) 100vw, 1600px"}

Click on the ![Ajay blog
6](https://www.ansible.com/hs-fs/hubfs/Ajay%20blog%206.png?width=95&name=Ajay%20blog%206.png){width="95"
style="width: 95px;"
srcset="https://www.ansible.com/hs-fs/hubfs/Ajay%20blog%206.png?width=48&name=Ajay%20blog%206.png 48w, https://www.ansible.com/hs-fs/hubfs/Ajay%20blog%206.png?width=95&name=Ajay%20blog%206.png 95w, https://www.ansible.com/hs-fs/hubfs/Ajay%20blog%206.png?width=143&name=Ajay%20blog%206.png 143w, https://www.ansible.com/hs-fs/hubfs/Ajay%20blog%206.png?width=190&name=Ajay%20blog%206.png 190w, https://www.ansible.com/hs-fs/hubfs/Ajay%20blog%206.png?width=238&name=Ajay%20blog%206.png 238w, https://www.ansible.com/hs-fs/hubfs/Ajay%20blog%206.png?width=285&name=Ajay%20blog%206.png 285w"
sizes="(max-width: 95px) 100vw, 95px"} button to reveal your API key.

## Configuring your Ansible.cfg

We define the Galaxy servers under the **\[galaxy\]** section of the
Ansible configuration file (i.e. *ansible.cfg). * An Ansible
configuration file is an ini formatted file for configuring behavior
settings.  This includes settings such as changing the return output
from JSON to YAML. If you are unfamiliar with an Ansible configuration
file please refer to the
[documentation](https://docs.ansible.com/ansible/latest/installation_guide/intro_configuration.html). 
As a reminder the Ansible configuration file is searched in the
following order:\

1.  ansible.cfg (in the current directory)
2.  \~/.ansible.cfg (in the current home directory)
3.  /etc/ansible/ansible.cfg 

These tokens should be added now to the ansible.cfg file. An example of
this is shown below.  It is recommended when using more than one Galaxy
server to list them in server_list. The list should be in precedence
order with your primary location choice first, in this case Automation
Hub.

``` {.line-numbers .language-yaml}
[defaults]
stdout_callback = yaml
inventory = inventory/hosts
collections_paths = ./collections

[galaxy]

server_list = automation_hub, release_galaxy

[galaxy_server.automation_hub]
url=https://cloud.redhat.com/api/automation-hub/
auth_url=https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token
token=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

[galaxy_server.release_galaxy]
url=https://galaxy.ansible.com/
token=xxxxxxxxxxxxxxxxxxxxxx
```

Note the *url* and *auth_url* keys that define the Automation Hub
repository and authentication endpoint. Also note that this file defines
where the collections should be downloaded to via the collections_paths
parameter (e.g.. ./collections).  For more information on configuration
for Ansible Galaxy and Automation Hub please refer to the [Galaxy User
Guide](https://docs.ansible.com/ansible/latest/galaxy/user_guide.html#galaxy-user-guide).\
\

## Using a requirements file

For this example I am going to use the requirements.yml method where I
can install all the collections from a single list. If you are familiar
with the use of *requirements.yml*  file with roles, the file is very
similar for collections. This is best understood through an example:

``` {.line-numbers .language-yaml}
» cat collections/requirements.yml
collections:
  - name: junipernetworks.junos
    source: https://galaxy.ansible.com
 
  - name: f5networks.f5_modules
    source: https://cloud.redhat.com/api/automation-hub/
```

Here, we defined 2 collections that are needed for our test playbook.
The Juniper Networks *junos* collection is being downloaded from Ansible
Galaxy whereas the F5 Networks *f5_modules collection* is being
downloaded from Automation Hub.

## Installing the collections

The collections can now be installed using the command:

``` {.line-numbers .language-yaml}
ansible-galaxy collection install -r collections/requirements.yml 
```

Running this command in verbose mode helps us look at the endpoints
being accessed:

![Ajay Blog
7](https://www.ansible.com/hs-fs/hubfs/Ajay%20Blog%207.png?width=1600&name=Ajay%20Blog%207.png){width="1600"
style="width: 1600px;"
srcset="https://www.ansible.com/hs-fs/hubfs/Ajay%20Blog%207.png?width=800&name=Ajay%20Blog%207.png 800w, https://www.ansible.com/hs-fs/hubfs/Ajay%20Blog%207.png?width=1600&name=Ajay%20Blog%207.png 1600w, https://www.ansible.com/hs-fs/hubfs/Ajay%20Blog%207.png?width=2400&name=Ajay%20Blog%207.png 2400w, https://www.ansible.com/hs-fs/hubfs/Ajay%20Blog%207.png?width=3200&name=Ajay%20Blog%207.png 3200w, https://www.ansible.com/hs-fs/hubfs/Ajay%20Blog%207.png?width=4000&name=Ajay%20Blog%207.png 4000w, https://www.ansible.com/hs-fs/hubfs/Ajay%20Blog%207.png?width=4800&name=Ajay%20Blog%207.png 4800w"
sizes="(max-width: 1600px) 100vw, 1600px"}

To test the availability of modules from these new collections, you can
use the *ansible-doc* command:

``` {.line-numbers .language-yaml}
» ansible-doc f5networks.f5_modules.bigip_device_info 
```

Our simple playbook will collect facts from the Juniper and F5 device
(<https://github.com/termlen0/collections_demo/blob/master/play.yaml>).
We can test the playbook by running it from the command line:

![Ajay blog
8](https://www.ansible.com/hs-fs/hubfs/Ajay%20blog%208.png?width=1163&name=Ajay%20blog%208.png){width="1163"
style="width: 1163px;"
srcset="https://www.ansible.com/hs-fs/hubfs/Ajay%20blog%208.png?width=582&name=Ajay%20blog%208.png 582w, https://www.ansible.com/hs-fs/hubfs/Ajay%20blog%208.png?width=1163&name=Ajay%20blog%208.png 1163w, https://www.ansible.com/hs-fs/hubfs/Ajay%20blog%208.png?width=1745&name=Ajay%20blog%208.png 1745w, https://www.ansible.com/hs-fs/hubfs/Ajay%20blog%208.png?width=2326&name=Ajay%20blog%208.png 2326w, https://www.ansible.com/hs-fs/hubfs/Ajay%20blog%208.png?width=2908&name=Ajay%20blog%208.png 2908w, https://www.ansible.com/hs-fs/hubfs/Ajay%20blog%208.png?width=3489&name=Ajay%20blog%208.png 3489w"
sizes="(max-width: 1163px) 100vw, 1163px"}

If you don\'t want to dynamically load the latest collection content
every time, comment out or remove the requirements file.  This means you
can control which Ansible Collections are available by manually
installing each collection required for your Ansible Playbook into the
correct virtual environment.  For example to install the F5 Networks
collections you would perform this command:

``` {.line-numbers .language-yaml}
ansible-galaxy collection install f5networks.f5_modules 
```

Another way would be to package the required collections in your SCM
(source control management) with your other content.  This means you
would sync collections in your development environment versus the
Ansible Tower device.

In the future we will introduce a more standardized way around packaging
collections and a particular Ansible version and its dependencies.  

## Conclusion

Ansible Collections introduce a way to modularize and package automation
content effectively. Red Hat Automation Hub hosts certified, secure
collections that are validated and supported by Red Hat. Ansible Galaxy
hosts community contributed collections. Customers can access
collections from both content repositories. I think of collections as a
superchargers to the "batteries included" approach that Ansible takes.
It up-levels the nuances involved in building out automation, allowing
users to plug-n-play the latest and greatest automation content being
built by certified partners and the community.
