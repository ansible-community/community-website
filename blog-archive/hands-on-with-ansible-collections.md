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
blogs "Getting Started with Ansible Content Collections"
and "The Future of Ansible Content Delivery".
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

![Ajay blog one](/images/posts/archive/ajay-blog-one.png)

-   ansible.cfg is the Ansible configuration file.  I will elaborate on
    this in the next section.
-   collections is a directory storing all Ansible Collections that my
    Ansible Playbook will use
-   inventory is a directory containing a inventory file named hosts
-   play.yaml is my Ansible Playbook

For my example this is a development environment where I just want to
download the latest and greatest.  I will use a gitignore file to ignore
the downloaded content and only track the requirements file.

![Ajay blog two](/images/posts/archive/ajay-blog-two.png)

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

![Ajay blog three](/images/posts/archive/ajay-blog-three.png)

Clicking on the `Load token` button will reveal your
authentication token. Save this information somewhere, we will need to
enter this into the ansible.cfg file. Ansible Galaxy also has an API
token used for authentication and can be accessed by navigating to
<https://galaxy.ansible.com/me/preferences> after logging in.

![Ajay blog five](/images/posts/archive/ajay-blog-five.png)

Click on the `Show API key` button to reveal your API key.

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

```yaml
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
for Ansible Galaxy and Automation Hub please refer to the
[Galaxy User Guide](https://docs.ansible.com/ansible/latest/galaxy/user_guide.html#galaxy-user-guide).

## Using a requirements file

For this example I am going to use the requirements.yml method where I
can install all the collections from a single list. If you are familiar
with the use of *requirements.yml*  file with roles, the file is very
similar for collections. This is best understood through an example:

```yaml
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

```yaml
ansible-galaxy collection install -r collections/requirements.yml
```

Running this command in verbose mode helps us look at the endpoints
being accessed:

![Ajay Blog seven](/images/posts/archive/ajay-blog-seven.png)

To test the availability of modules from these new collections, you can
use the *ansible-doc* command:

```yaml
ansible-doc f5networks.f5_modules.bigip_device_info
```

Our simple playbook will collect facts from the Juniper and F5 device
(<https://github.com/termlen0/collections_demo/blob/master/play.yaml>).
We can test the playbook by running it from the command line:

![Ajay blog eight](/images/posts/archive/ajay-blog-eight.png)

If you don\'t want to dynamically load the latest collection content
every time, comment out or remove the requirements file.  This means you
can control which Ansible Collections are available by manually
installing each collection required for your Ansible Playbook into the
correct virtual environment.  For example to install the F5 Networks
collections you would perform this command:

```yaml
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
