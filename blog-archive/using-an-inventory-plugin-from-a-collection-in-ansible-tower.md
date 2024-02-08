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

The answer to both of these questions is to use a [dynamic inventory](https://docs.ansible.com/ansible/latest/user_guide/intro_dynamic_inventory.html):
a script or a plugin that will go to a source of truth and discover the
nodes that need to be managed. It will also automatically classify the
nodes by putting them into groups, which can be used to more selectively
target devices when automating with Ansible.

[Inventory plugins](https://docs.ansible.com/ansible/latest/plugins/inventory.html#plugin-list)
allow Ansible users to use external platforms to dynamically discover
target hosts and use those platforms as a Source of Truth for their
Ansible inventory. Common sources of truth include AWS EC2, Google GCP
and Microsoft Azure , but there are a number of other inventory plugins
available with Ansible.

Ansible Tower ships with [a number of inventory plugins](https://docs.ansible.com/ansible-tower/latest/html/userguide/inventories.html#inventory-plugins)
that work out of the box. These include the cloud examples mentioned
earlier as well as VMware vCenter, Red Hat OpenStack Platform and  Red
Hat Satellite. To use these inventory plugins, credentials need to be
added that can query the source platform. Afterwards, the inventory
plugins can be used as a source for an inventory in Ansible Tower. 

There are additional inventory plugins available, which are not shipped
with Ansible Tower, but which are written by the Ansible community. With
the move to Red Hat Ansible Content Collections
these inventory plugins are being packaged as part of the corresponding
Collections.

In this example, we are having a look at the ServiceNow inventory
plugin. ServiceNow is a very popular IT Service Management platform and
customers often use the ServiceNow CMDB to store details of all of their
devices. A CMDB can provide additional context to automation. For
example, server owner, service level (production/non-production) and
patch & maintenance windows. Their Ansible Inventory plugin can be used
to query the ServiceNow CMDB and is delivered as part of the
[servicenow.servicenow collection available on galaxy](https://galaxy.ansible.com/servicenow/servicenow). 

 

# Git Repository 

To use an inventory plugin from a Collection in Ansible Tower, we need
to source it from a Project. A Project within Ansible Tower is the
integration of a source control repository like a git repository. In
Ansible Tower, projects are used to pull Ansible Playbooks but also
variables and inventories. 

The contents of my source control repository are very simple:

```bash
├── collections
│   └── requirements.yml
└── servicenow.yml
```

The servicenow.yml file contains the details for the inventory plugin.
In our case, we  specify the correct table in the ServiceNow CMDB that
we want to use. We also select the fields we want to add as host_vars
and some information on the groups that we want it to create.

```bash
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

The [collections/requirements.yml file](https://docs.ansible.com/ansible/latest/galaxy/user_guide.html#install-multiple-collections-with-a-requirements-file)
is needed so that Ansible Tower can download the Collection and
therefore the inventory plugin. Otherwise, we would have to install and
maintain the Collection on all of our Ansible Tower nodes manually.

```bash
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

![plugin blog image one](/images/posts/archive/plugin-blog-one.png)


# Create the ServiceNow Credential

As mentioned, the configuration in our repository does not include
credentials to use with ServiceNow, or the definition of the ServiceNow
instance to speak to. Thus we will create a credential in Ansible Tower
to define those values. Looking at the
[documentation for the ServiceNow inventory plugin](https://github.com/ServiceNowITOM/servicenow-ansible/blob/devel/docs/inventory.md),
we can see that there are a number of environment variables that we can
set to define the connection details. For example:

```yaml
= username
        The ServiceNow user account, it should have rights to read cmdb_ci_server (default), or table specified by SN_TABLE

        set_via:
        env:
        - name: SN_USERNAME
```

In this case, if the SN_USERNAME environment variable is set then the
inventory plugin will use it as the user account to connect to
ServiceNow.

The other variables we need to set are - `SN_INSTANCE` and `SN_PASSWORD`

However, in Ansible Tower, there is no credential type for ServiceNow
where we can enter these details. Luckily for such use cases, Ansible
Tower allows us to define [custom credential
types](https://docs.ansible.com/ansible-tower/latest/html/userguide/credential_types.html).

In our case, the input configuration for a custom credential for
ServiceNow is as follows:

```yaml
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

```yaml
env:
  SN_INSTANCE: '{{ SN_INSTANCE }}'
  SN_PASSWORD: '{{ SN_PASSWORD }}'
  SN_USERNAME: '{{ SN_USERNAME }}'
```

With the custom credential type defined, we can now add a ServiceNow
credential and set the instance, username and password as shown:

![plugin blog image two](/images/posts/archive/plugin-blog-two.png)


# Create the Inventory

The final step is to create the inventory within Ansible Tower. We need
a name - here ServiceNow: 

![plugin blog image three](/images/posts/archive/plugin-blog-three.png)

With the inventory created, we can now attach a source to it. Here we
specify the Project that we created earlier and enter the path to our
inventory YAML file in the source control repository- in this case, that
is servicenow.yml in the root of the project. We also need to associate
our ServiceNow credential.

![plugin blog image four](/images/posts/archive/plugin-blog-four.png)

To test the setup, we can try syncing with the source. Pressing the
button "**Sync all**" does just that. If everything was configured
correctly, the hosts should be imported into the inventory:

![plugin blog image 5](/images/posts/archive/plugin-blog-five.png)

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
