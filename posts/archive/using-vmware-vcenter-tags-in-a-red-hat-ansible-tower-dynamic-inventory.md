---
author: Raed Soliman
date: 2021-06-22 00:00 UTC
description: In Ansible Tower 3.8, native inventory plugins are
  supported directly in Tower supporting the full list of configs
  available to the plugin via the inventory source source_vars, which
  allows importing and using VCenter tags to group VMs in your inventory
  within Ansible Tower.
lang: en-us
title: Using VMware vCenter Tags in a Red Hat Ansible Tower Dynamic Inventory
---

# Using VMware vCenter Tags in a Red Hat Ansible Tower Dynamic Inventory

VMware vCenter Server tags are labels that can be applied to objects
like the system's environment and usage, therefore it is a very useful
method of asset management - also making tags a perfect fit in the
Ansible world to organize systems in an Ansible inventory. Red Hat
customers have regularly requested the ability to use vCenter Tags in
Red Hat Ansible Tower. This is now possible with an Ansible Tower
inventory source that supports tags and provides the
[vmware_vm_inventory](https://docs.ansible.com/ansible/latest/collections/community/vmware/vmware_vm_inventory_inventory.html)
plugin.

Ansible Automation Platform 1.2 brings completely native Ansible
inventory plugin support to Ansible Tower 3.8. In previous versions,
there were specific inventory plugin configurations based on the old
inventory scripts where a specific set of parameters surfaced in Ansible
Tower's user interface. For example: cloud region and a specific subset
of variables you could pass to those inventory scripts surfaced as
variables you could pass to the inventory source, which means that new
configuration parameters that come with Ansible inventory plugins are
not supported in order to maintain compatibility with the old inventory
scripts. 

The move to support native inventory plugins allows Red Hat Ansible
Automation Platform customers to use all the configuration parameters
available through the plugin, as well as supporting any future new
plugin features automatically.

So as an example, the screenshot below shows the source configuration
panel difference between an older version of Ansible Tower (3.7 in this
case) and the new source configuration in Ansible Tower 3.8. This
specific example is for an Amazon EC2 source in Ansible Tower 3.8:

![vcenter tags blog one](/images/posts/archive/vcenter-blog-one.png)

As you can see, the "Instance Filters" and "Regions" configuration
options are no longer a part of the user interface in Ansible Tower 3.8,
but the configuration can now be done in the "Source Variables" section
of the inventory source definition. This Ansible Tower instance was
actually upgraded from 3.7 to 3.8, and during the upgrade, the platform
installer takes old inventory sources and converts them to a compatible
inventory plugin configuration - therefore there will be a lot of
entries in the section to maintain the same outcome for upgraded
sources - groups created by default for example - as the old inventory
scripts.

Pretty exciting stuff!

# Environment Setup

So the
[vmware_vm_inventory](https://docs.ansible.com/ansible/latest/collections/community/vmware/vmware_vm_inventory_inventory.html)
plugin supports tags using a configuration parameter -
[with_tags](https://docs.ansible.com/ansible/latest/collections/community/vmware/vmware_vm_inventory_inventory.html#parameter-with_tags) -
which defaults to false - so we will need to set that to true in our
source definition, but as stated in the documentation linked above,
using this parameter requires the **vSphere Automation SDK** library to
be installed on the controller machine - in our case, the Ansible Tower
nodes. The documentation also links to this
[URL](https://code.vmware.com/web/sdk/7.0/vsphere-automation-python) for
the installation steps.

For this example, we will be using six VMs that were created:

| Name      | Type    | Tags          |
|-----------|---------|---------------|
| testvm_1  | RHEL7   | Dev, TestVM, Linux |
| testvm_2  | RHEL7   | Prod, TestVM, Linux |
| testvm_3  | RHEL8   | Dev, TestVM, Linux |
| testvm_4  | RHEL8   | Prod, TestVM, Linux |
| testvm_5  | Win2019 | Dev, TestVM, Windows |
| testvm_6  | Win2019 | Prod, TestVM, Windows |

First step is to make sure that our Ansible Tower nodes have the
required library to use this feature. As we can use an inventory source
with a custom python virtual environment, we will create a new python
virtual environment under `/opt/towervenvs` called `vmware-venv`, and will
be installing the required libraries in that environment (you can read
more about Ansible Tower's virtual environments and how to use them in the
[documentation](https://docs.ansible.com/ansible-tower/latest/html/upgrade-migration-guide/virtualenv.html)).

```bash
$ sudo /opt/towervenvs/vmware-venv/bin/pip3 install --upgrade pip setuptools
$ sudo /opt/towervenvs/vmware-venv/bin/pip3 install --upgrade  git+https://github.com/vmware/vsphere-automation-sdk-python.git
```

Make sure that the virtual environment and the required libraries are
installed on all nodes in the Ansible Tower cluster, and that Ansible
Tower is configured to look for virtual environments under the directory
they are defined in. This setting can be found under
**Settings > System > CUSTOM VIRTUAL ENVIRONMENT PATHS**

![vcenter tags blog two](/images/posts/archive/vcenter-blog-two.png)

Next, we need to configure a credential for vCenter that Ansible Tower
will use when syncing the inventory. 

In Ansible Tower, from the left hand panel under resources select
"Credentials" and click the add icon and add a new credential. In the
new credential configuration panel, enter a name for your new credential
and choose "VMware vCenter" as the credential type and fill in the
required information - here is what the credential definition looks
like:

![vcenter tags blog three](/images/posts/archive/vcenter-blog-three.png)

# Creating the dynamic inventory source in Ansible Tower

Now it\'s time to create the inventory. In Ansible Tower, from the left
hand panel under resources, select "Inventories" and click the add icon
and add a new inventory. Give the inventory a name and select an
organization for the inventory - we\'ll call ours \"VMware
Inventory\'\', and assign it to Red Hat Organization.

![vcenter tags blog four](/images/posts/archive/vcenter-blog-four.png)

Click "Save" and the sources tab is now enabled. Now go to the sources
tab, click the add icon to add a new source - Give it a name, and choose
VMware vCenter as the source, and choose the credential that we created
earlier (the credential may already be auto populated if it's the only
credential of the type "VMware vCenter" defined), and make sure to
select the virtual environment that has the required library installed
under it.

Under source variables we will add the following and click save:

```yaml
---
plugin: community.vmware.vmware_vm_inventory
hostnames:
- 'config.name'
properties:
- name
- network
- overallStatus
- value
- capability
- config
- guest
- runtime
- summary
with_nested_properties: true
with_tags: true
```

![vcenter tags blog five](/images/posts/archive/vcenter-blog-five.png)

Our new inventory source is now created and will appear under sources
Let's now click on the sync icon to pull in our list of virtual machines
(VMs). After the sync job completes, and the cloud icon next to the
source turns green, we can now go into the list of hosts and see all the
hosts that are in vCenter, and if we click on any of the hosts we can
see the associated tags under the "tags" key. Awesome!

![vcenter tags blog six](/images/posts/archive/vcenter-blog-six.png)

![vcenter tags blog seven](/images/posts/archive/vcenter-blog-seven.png)

# Creating inventory groups based on tags

The previous configuration will pull in all the hosts in vCenter with
their associated tags, and the guest attributes we defined based on what
is available in the inventory plugin's documentation. But we only want
to pull in VMs that have the tag "TestVM", and we want to create groups
based on the tags associated with the VMs that are imported, their power
state and their guest ID. So let\'s add some filters, as well as some
keyed groups definition. Go back to the inventory source we defined, and
replace the definition under source variables with the following:

```yaml
---
plugin: community.vmware.vmware_vm_inventory
hostnames:
- 'config.name'
properties:
- name
- network
- overallStatus
- value
- capability
- config
- guest
- runtime
- summary
with_nested_properties: true
with_tags: true
keyed_groups:
- key: tags
  prefix: "vm_tag_"
  separator: ""
- key: config.guestId
  prefix: ''
  separator: ''
- key: summary.runtime.powerState
  prefix: ''
  separator: ''
filters:
- "'TestVM' in tags"
```

And refresh the inventory source again.

And just like that, we have a list of only the hosts that are tagged
with TestVM, as well as groups created based on the tags defined in
vCenter.

![vcenter tags blog eight](/images/posts/archive/vcenter-blog-eight.png)

![vcenter tags blog nine](/images/posts/archive/vcenter-blog-nine.png)

The new native Ansible inventory plugin support may upgrade the level of
difficulty, as you will have to know how to configure the inventory
plugin you want to use, but it gives users a lot of flexibility.
