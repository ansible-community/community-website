---
author: Patrick Harrison
date: 2020-08-04 00:00 UTC
description: In this example, we are having a look at the ServiceNow
  inventory plugin. ServiceNow is a very popular IT Service Management
  platform
lang: en-us
title: Using an Inventory Plugin from a Collection in Ansible Tower
---

# Using an Inventory Plugin from a Collection in Ansible Tower

Many IT environments grow more and more complex. It is more important
than ever that an automation solution always has the most up to date
information about what nodes are present and need to be automated. To
answer this challenge, the Red Hat Ansible Automation Platform uses
[inventories](https://docs.ansible.com/ansible/latest/user_guide/intro_inventory.html#intro-inventory):
lists of managed nodes.

In its simplest form, inventories can be static files. This is ideal
when getting started with Ansible, but as the automation is scaled, a
static inventory file is not enough anymore:

1.  How do we update and maintain a list of all of our managed nodes if
    something changes, if workloads are spun up or teared down?
2.  How do we classify our infrastructure so that we can be more
    selective in what managed nodes we automate against?

The answer to both of these questions is to use a [[dynamic
inventory]{style="text-decoration: underline;"}](https://docs.ansible.com/ansible/latest/user_guide/intro_dynamic_inventory.html):
a script or a plugin that will go to a source of truth and discover the
nodes that need to be managed. It will also automatically classify the
nodes by putting them into groups, which can be used to more selectively
target devices when automating with Ansible.

[Inventory
plugins](https://docs.ansible.com/ansible/latest/plugins/inventory.html#plugin-list)
allow Ansible users to use external platforms to dynamically discover
target hosts and use those platforms as a Source of Truth for their
Ansible inventory. Common sources of truth include AWS EC2, Google GCP
and Microsoft Azure , but there are a number of other inventory plugins
available with Ansible.

Ansible Tower ships with [a number of inventory
plugins](https://docs.ansible.com/ansible-tower/latest/html/userguide/inventories.html#inventory-plugins)
that work out of the box. These include the cloud examples mentioned
earlier as well as VMware vCenter, Red Hat OpenStack Platform and  Red
Hat Satellite. To use these inventory plugins, credentials need to be
added that can query the source platform. Afterwards, the inventory
plugins can be used as a source for an inventory in Ansible Tower. 

There are additional inventory plugins available, which are not shipped
with Ansible Tower, but which are written by the Ansible community. With
the [move to Red Hat Ansible Content
Collections](https://www.ansible.com/blog/getting-started-with-ansible-collections),
these inventory plugins are being packaged as part of the corresponding
Collections.

In this example, we are having a look at the ServiceNow inventory
plugin. ServiceNow is a very popular IT Service Management platform and
customers often use the ServiceNow CMDB to store details of all of their
devices. A CMDB can provide additional context to automation. For
example, server owner, service level (production/non-production) and
patch & maintenance windows. Their Ansible Inventory plugin can be used
to query the ServiceNow CMDB and is delivered as part of the
[servicenow.servicenow collection available on
galaxy](https://galaxy.ansible.com/servicenow/servicenow). 

 

# Git Repository 

To use an inventory plugin from a Collection in Ansible Tower, we need
to source it from a Project. A Project within Ansible Tower is the
integration of a source control repository like a git repository. In
Ansible Tower, projects are used to pull Ansible Playbooks but also
variables and inventories. 

The contents of my source control repository are very simple:

``` 
├── collections
│   └── requirements.yml
└── servicenow.yml
```

The servicenow.yml file contains the details for the inventory plugin.
In our case, we  specify the correct table in the ServiceNow CMDB that
we want to use. We also select the fields we want to add as host_vars
and some information on the groups that we want it to create.

``` 
$ cat servicenow.yml
plugin: servicenow.servicenow.now
table: cmdb_ci_linux_server
fields: [ip_address,fqdn,host_name,sys_class_name,name,os]
keyed_groups:
  - key: sn_sys_class_name | lower
    prefix: ''
    separator: ''
  - key: sn_os | lower
    prefix: ''
    separator: ''
```

Note that no details of the ServiceNow instance that we want to connect
to or any credentials are defined here. Those will be configured within
Ansible Tower later on.

The [collections/requirements.yml[
file]{style="text-decoration: underline;"}](https://docs.ansible.com/ansible/latest/galaxy/user_guide.html#install-multiple-collections-with-a-requirements-file)
is needed so that Ansible Tower can download the Collection and
therefore the inventory plugin. Otherwise, we would have to install and
maintain the Collection on all of our Ansible Tower nodes manually.

``` 
$ cat collections/requirements.yml
---
collections:

- name: servicenow.servicenow
```

Once we have pushed this configuration into the source control
repository, we can create a project in Ansible Tower referencing the
repository. Below is an example that links Ansible Tower to my github
repository. Note the SCM URL. We can optionally specify a credential if
the repository is private and also specify a specific branch, tag or
commit to pull from.

![plugin blog image
1](https://www.ansible.com/hs-fs/hubfs/plugin%20blog%20image%201.png?width=1471&name=plugin%20blog%20image%201.png){width="1471"
style="width: 1471px;"
srcset="https://www.ansible.com/hs-fs/hubfs/plugin%20blog%20image%201.png?width=736&name=plugin%20blog%20image%201.png 736w, https://www.ansible.com/hs-fs/hubfs/plugin%20blog%20image%201.png?width=1471&name=plugin%20blog%20image%201.png 1471w, https://www.ansible.com/hs-fs/hubfs/plugin%20blog%20image%201.png?width=2207&name=plugin%20blog%20image%201.png 2207w, https://www.ansible.com/hs-fs/hubfs/plugin%20blog%20image%201.png?width=2942&name=plugin%20blog%20image%201.png 2942w, https://www.ansible.com/hs-fs/hubfs/plugin%20blog%20image%201.png?width=3678&name=plugin%20blog%20image%201.png 3678w, https://www.ansible.com/hs-fs/hubfs/plugin%20blog%20image%201.png?width=4413&name=plugin%20blog%20image%201.png 4413w"
sizes="(max-width: 1471px) 100vw, 1471px"}


# Create the ServiceNow Credential

As mentioned, the configuration in our repository does not include
credentials to use with ServiceNow, or the definition of the ServiceNow
instance to speak to. Thus we will create a credential in Ansible Tower
to define those values. Looking at the [documentation for the ServiceNow
inventory
plugin](https://github.com/ServiceNowITOM/servicenow-ansible/blob/devel/docs/inventory.md),
we can see that there are a number of environment variables that we can
set to define the connection details. For example:

``` 
= username
        The ServiceNow user account, it should have rights to read cmdb_ci_server (default), or table specified by SN_TABLE

        set_via:
        env:
        - name: SN_USERNAME
```

In this case, if the SN_USERNAME environment variable is set then the
inventory plugin will use it as the user account to connect to
ServiceNow.

The other variables we need to set are - SN_INSTANCE & SN_PASSWORD

However, in Ansible Tower, there is no credential type for ServiceNow
where we can enter these details. Luckily for such use cases, Ansible
Tower allows us to define [custom credential
types](https://docs.ansible.com/ansible-tower/latest/html/userguide/credential_types.html).
You can read more about custom credentials in our ["Ansible Tower
Feature Spotlight: Custom
Credentials"](https://www.ansible.com/blog/ansible-tower-feature-spotlight-custom-credentials)
by Bill Nottingham.

In our case, the input configuration for a custom credential for
ServiceNow is as follows:

``` 
fields:
  - id: SN_USERNAME
    type: string
    label: Username
  - id: SN_PASSWORD
    type: string
    label: Password
    secret: true
  - id: SN_INSTANCE
    type: string
    label: Snow Instance
required:
  - SN_USERNAME
  - SN_PASSWORD
  - SN_INSTANCE
```

The credentials will be exposed as environment variables of the same
name. This is described in the injector configuration:

``` 
env:
  SN_INSTANCE: '{{ SN_INSTANCE }}'
  SN_PASSWORD: '{{ SN_PASSWORD }}'
  SN_USERNAME: '{{ SN_USERNAME }}'
```

With the custom credential type defined, we can now add a ServiceNow
credential and set the instance, username and password as shown:

![plugin blog image
2](https://www.ansible.com/hs-fs/hubfs/plugin%20blog%20image%202.png?width=1517&name=plugin%20blog%20image%202.png){width="1517"
style="width: 1517px;"
srcset="https://www.ansible.com/hs-fs/hubfs/plugin%20blog%20image%202.png?width=759&name=plugin%20blog%20image%202.png 759w, https://www.ansible.com/hs-fs/hubfs/plugin%20blog%20image%202.png?width=1517&name=plugin%20blog%20image%202.png 1517w, https://www.ansible.com/hs-fs/hubfs/plugin%20blog%20image%202.png?width=2276&name=plugin%20blog%20image%202.png 2276w, https://www.ansible.com/hs-fs/hubfs/plugin%20blog%20image%202.png?width=3034&name=plugin%20blog%20image%202.png 3034w, https://www.ansible.com/hs-fs/hubfs/plugin%20blog%20image%202.png?width=3793&name=plugin%20blog%20image%202.png 3793w, https://www.ansible.com/hs-fs/hubfs/plugin%20blog%20image%202.png?width=4551&name=plugin%20blog%20image%202.png 4551w"
sizes="(max-width: 1517px) 100vw, 1517px"}


# Create the Inventory

The final step is to create the inventory within Ansible Tower. We need
a name - here ServiceNow: 

![plugin blog image
3](https://www.ansible.com/hs-fs/hubfs/plugin%20blog%20image%203.png?width=512&name=plugin%20blog%20image%203.png){width="512"
style="width: 512px;"
srcset="https://www.ansible.com/hs-fs/hubfs/plugin%20blog%20image%203.png?width=256&name=plugin%20blog%20image%203.png 256w, https://www.ansible.com/hs-fs/hubfs/plugin%20blog%20image%203.png?width=512&name=plugin%20blog%20image%203.png 512w, https://www.ansible.com/hs-fs/hubfs/plugin%20blog%20image%203.png?width=768&name=plugin%20blog%20image%203.png 768w, https://www.ansible.com/hs-fs/hubfs/plugin%20blog%20image%203.png?width=1024&name=plugin%20blog%20image%203.png 1024w, https://www.ansible.com/hs-fs/hubfs/plugin%20blog%20image%203.png?width=1280&name=plugin%20blog%20image%203.png 1280w, https://www.ansible.com/hs-fs/hubfs/plugin%20blog%20image%203.png?width=1536&name=plugin%20blog%20image%203.png 1536w"
sizes="(max-width: 512px) 100vw, 512px"}

With the inventory created, we can now attach a source to it. Here we
specify the Project that we created earlier and enter the path to our
inventory YAML file in the source control repository- in this case, that
is servicenow.yml in the root of the project. We also need to associate
our ServiceNow credential.

![plugin blog image
4](https://www.ansible.com/hs-fs/hubfs/plugin%20blog%20image%204.png?width=1461&name=plugin%20blog%20image%204.png){width="1461"
style="width: 1461px;"
srcset="https://www.ansible.com/hs-fs/hubfs/plugin%20blog%20image%204.png?width=731&name=plugin%20blog%20image%204.png 731w, https://www.ansible.com/hs-fs/hubfs/plugin%20blog%20image%204.png?width=1461&name=plugin%20blog%20image%204.png 1461w, https://www.ansible.com/hs-fs/hubfs/plugin%20blog%20image%204.png?width=2192&name=plugin%20blog%20image%204.png 2192w, https://www.ansible.com/hs-fs/hubfs/plugin%20blog%20image%204.png?width=2922&name=plugin%20blog%20image%204.png 2922w, https://www.ansible.com/hs-fs/hubfs/plugin%20blog%20image%204.png?width=3653&name=plugin%20blog%20image%204.png 3653w, https://www.ansible.com/hs-fs/hubfs/plugin%20blog%20image%204.png?width=4383&name=plugin%20blog%20image%204.png 4383w"
sizes="(max-width: 1461px) 100vw, 1461px"}

To test the setup, we can try syncing with the source. Pressing the
button "**Sync all**" does just that. If everything was configured
correctly, the hosts should be imported into the inventory:

![plugin blog image
5](https://www.ansible.com/hs-fs/hubfs/plugin%20blog%20image%205.png?width=1525&name=plugin%20blog%20image%205.png){width="1525"
style="width: 1525px;"
srcset="https://www.ansible.com/hs-fs/hubfs/plugin%20blog%20image%205.png?width=763&name=plugin%20blog%20image%205.png 763w, https://www.ansible.com/hs-fs/hubfs/plugin%20blog%20image%205.png?width=1525&name=plugin%20blog%20image%205.png 1525w, https://www.ansible.com/hs-fs/hubfs/plugin%20blog%20image%205.png?width=2288&name=plugin%20blog%20image%205.png 2288w, https://www.ansible.com/hs-fs/hubfs/plugin%20blog%20image%205.png?width=3050&name=plugin%20blog%20image%205.png 3050w, https://www.ansible.com/hs-fs/hubfs/plugin%20blog%20image%205.png?width=3813&name=plugin%20blog%20image%205.png 3813w, https://www.ansible.com/hs-fs/hubfs/plugin%20blog%20image%205.png?width=4575&name=plugin%20blog%20image%205.png 4575w"
sizes="(max-width: 1525px) 100vw, 1525px"}

Note the groups that we requested were also created.

# Summary

In this example, we have shown how to use inventory plugins from
Collections within  Ansible Tower using the ServiceNow inventory plugin.
We have also securely defined the credentials to authenticate to our
ServiceNow instance. Sourcing an inventory plugin from a Project is not
exclusive to third party or custom plugins either: this is a valid
method for modifying the behaviour of some of the built-in inventory
plugins as well. These capabilities enable the Ansible Automation
Platform to seamlessly integrate with existing tools while automating IT
environments of growing complexity. 
