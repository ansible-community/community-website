---
author: Sean Cavanaugh
date: 2020-02-19 00:00 UTC
description: This blog post goes through the eos_vlans module for the
  Arista EOS network platform.  We walk through several examples and
  describe the use cases for each state parameter and how we envision
  these being used in real world scenarios.
lang: en-us
title: Deep dive on VLANS resource modules for network automation
---

# Deep dive on VLANS resource modules for network automation

In October of 2019, as part of Red Hat Ansible Engine 2.9, the Ansible
Network Automation team [introduced the concept of resource
modules](https://www.ansible.com/blog/network-features-coming-soon-in-ansible-engine-2.9). 
These opinionated network modules make network automation easier and
more consistent for those automating various network platforms in
production.  The goal for resource modules was to avoid creating overly
complex jinja2 templates for rendering network configuration. This blog
post goes through the eos_vlans module for the Arista EOS network
platform.  I walk through several examples and describe the use cases
for each state parameter and how we envision these being used in real
world scenarios.

Before starting let's quickly explain the rationale behind naming of the
network resource modules. Notice for resource modules that configure
VLANs there is a singular form (eos_vlan, ios_vlan, junos_vlan, etc) and
a plural form (eos_vlans, ios_vlans, junos_vlans).  The new resource
modules are the plural form that we are covering today. We have
deprecated the singular form. This was done so that those using existing
network modules would not have their Ansible Playbooks stop working and
have sufficient time to migrate to the new network automation modules.

 

# VLAN Example

Let's start with an example of the
[eos_vlans](https://docs.ansible.com/ansible/latest/modules/eos_vlans_module.html)
resource module:

```yml
---
- name: add vlans
  hosts: arista
  gather_facts: false
  tasks:
    - name: add VLAN configuration
      eos_vlans:
        config:
          - name: desktops
            vlan_id: 20
          - name: servers
            vlan_id: 30
          - name: printers
            vlan_id: 40
          - name: DMZ
            vlan_id: 50
```

There is an implicit state parameter which defaults to merged (i.e.
state: merged).  If we run this Ansible Playbook VLANs 20,30,40 and 50
will be merged into the running configuration of any device in the
arista group.  The show vlan output on a new Arista switch will look
like the following:

```yml
rtr2#show vlan
VLAN  Name                             Status    Ports
----- -------------------------------- --------- -------------------------------
1     default                          active
20    desktops                         active
30    servers                          active
40    printers                         active
50    DMZ                              active
```

while the running configuration will look like the following:

```yml
rtr2#show running-config | s vlan
vlan 20
   name desktops
!
vlan 30
   name servers
!
vlan 40
   name printers
!
vlan 50
   name DMZ
```

Now let's make a change manually to the network configuration:

```yml
rtr2(config)#vlan 100
rtr2(config-vlan-100)#name artisanal_vlan
rtr2(config-vlan-100)#end
rtr2#wr
Copy completed successfully.
```

If I re-run the Ansible Playbook it returns with changed=0 because it
only cares about the VLANs 20, 30, 40 and 50. It won't remove VLAN 100
because we have the state parameter set to merged by default, so it only
will merged the data model it knows about. It is just enforcing
configuration policy of the VLANs I am sending.

## Using the \'state\' parameter

What happens if I change the state parameter to replaced?  Just change
the previous example to the following:

```yml
---
- name: add vlans
  hosts: arista
  gather_facts: false
  tasks:
    - name: add VLAN configuration
      eos_vlans:
        state: replaced
        config:
          - name: desktops
            vlan_id: 20
          - name: servers
            vlan_id: 30
          - name: printers
            vlan_id: 40
          - name: DMZ
            vlan_id: 50
```

The Ansible Playbook ran just like before with changed=0. Can we tell if
it removed the artisanal_vlan 100?

```yml
rtr2#show vlan
VLAN  Name                             Status    Ports
----- -------------------------------- --------- -------------------------------
1     default                          active
20    desktops                         active
30    servers                          active
40    printers                         active
50    DMZ                              active
100   artisanal_vlan                   active
```

Nope! The goal of resource modules is to update existing resources to
match the existing data model. Since our data model (the key, value
pairs that represent the VLANs, which are passed under the config
parameter in the playbook) only includes VLANs 20, 30, 40 and 50 the
eos_vlans module only updates parameters relevant to those particular
VLANs.

Why would I use this versus a merged? The major difference between a
merged and a replaced is that a merged just makes sure the commands are
present that are represented within the data model, whereas the replaced
parameter makes your resource match the data model. Let\'s look at the
eos_vlans module to see what it considers as part of the vlans resource.

There are three parameters currently used for the **vlans** resource:

-   name
-   state (active or suspend)
-   vlan_id (range between 1-4094)

Let\'s look at the following example:

+-----------------------------------+-----------------------------------+
| ::: {style="line-height: 1;"}     | ::: {style="line-height: 1;"}     |
| **  [Data Model Sent\             | **  [Existing Arista Config \     |
| \                                 | \                                 |
| \                                 | ]{style="font-size: 16px;"}**     |
| ]{style="font-size: 16px;"}**     | :::                               |
| :::                               |                                   |
|                                   |     vlan 200                      |
|     - name: desktops              |        state suspend              |
|       vlan_id: 200                |     !                             |
+-----------------------------------+-----------------------------------+

This is how merged compares to replaced:

+-----------------------------------+-----------------------------------+
| ::: {style="line-height: 1;"}     | ::: {style="l                     |
| ** [merged\                       | ine-height: 1; font-size: 16px;"} |
| \                                 | **replaced\                       |
| ]{style="font-size: 16px;"}**     | \                                 |
| :::                               | \                                 |
|                                   | **                                |
|     vlan 200                      | :::                               |
|       name desktops               |                                   |
|       state suspend               |     vlan 200                      |
|     !                             |        name desktops              |
|                                   |     !                             |
+-----------------------------------+-----------------------------------+

The replaced parameter enforces the data model on the network device for
each configured VLAN.  In the example above it will remove the \`state
suspend\` because it is not within the data model.  To think of this
another way, the replaced parameter is aware of commands that shouldn't
be there as well as what should.

## Using the overridden state parameter

What happens if I change the state parameter to overridden?  Just change
the original example to the following:

```yml
---
- name: add vlans
  hosts: arista
  gather_facts: false
  tasks:
    - name: add VLAN configuration
      eos_vlans:
        state: overridden
        config:
          - name: desktops
            vlan_id: 20
          - name: servers
            vlan_id: 30
          - name: printers
            vlan_id: 40
          - name: DMZ
            vlan_id: 50
```

Now run the Ansible Playbook:

![Sean Blog
2](https://www.ansible.com/hs-fs/hubfs/Sean%20Blog%202.png?width=1600&name=Sean%20Blog%202.png){width="1600"
style="width: 1600px;"
srcset="https://www.ansible.com/hs-fs/hubfs/Sean%20Blog%202.png?width=800&name=Sean%20Blog%202.png 800w, https://www.ansible.com/hs-fs/hubfs/Sean%20Blog%202.png?width=1600&name=Sean%20Blog%202.png 1600w, https://www.ansible.com/hs-fs/hubfs/Sean%20Blog%202.png?width=2400&name=Sean%20Blog%202.png 2400w, https://www.ansible.com/hs-fs/hubfs/Sean%20Blog%202.png?width=3200&name=Sean%20Blog%202.png 3200w, https://www.ansible.com/hs-fs/hubfs/Sean%20Blog%202.png?width=4000&name=Sean%20Blog%202.png 4000w, https://www.ansible.com/hs-fs/hubfs/Sean%20Blog%202.png?width=4800&name=Sean%20Blog%202.png 4800w"
sizes="(max-width: 1600px) 100vw, 1600px"}

The Ansible Playbook now has changed=1.  But did it remove the
artisanal_vlan 100?

Logging into one of the Arista devices confirms it did!

```yml
rtr2#show vlan
VLAN  Name                             Status    Ports
----- -------------------------------- --------- -------------------------------
1     default                          active
20    desktops                         active
30    servers                          active
40    printers                         active
50    DMZ                              active
```

The overridden parameter will enforce all **vlans** resources to the
data model.  This means it removes VLANs that are not defined in the
data model being sent.

## Takeaways

There are currently three ways to push configuration using resource
modules.  These are the merged, replaced and overridden parameters.
These allow much more flexibility for network engineers to adopt
automation in incremental steps.  We realize that most folks will start
with the merged parameter as they gain familiarity with the new resource
module concepts. Over time organizations will move towards the
overridden parameter as they adopt a standard SoT (source of truth) for
their data models, wherever they reside.
