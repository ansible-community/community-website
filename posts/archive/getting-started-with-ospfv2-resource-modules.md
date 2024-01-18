---
author: Rohit Thakur
date: 2020-08-27 00:00 UTC
description: With the increasing size and complexity of modern
  enterprise networks, the demand on simplifying the networks management
  becomes more intense. The introduction of resources modules with
  Ansible 2.9 provide a path to users to ease the network management,
  especially across multiple different product vendors.
lang: en-us
title: Getting Started With OSPFV2 Resource Modules
---

# Getting Started With OSPFV2 Resource Modules

[With the increasing size and complexity of modern enterprise networks,
the demand on simplifying the networks management becomes more intense.
The ]{style="color: #333333;"}[introduction of resources modules with
Ansible
2.9](https://www.ansible.com/blog/network-features-coming-soon-in-ansible-engine-2.9)[
provide a path to users to ease the network management, especially
across multiple different product vendors.]{style="color: #333333;"}

[In the past, we've already covered resource modules for
]{style="color: #333333;"}[VLAN
management](https://www.ansible.com/blog/deep-dive-on-vlans-resource-modules-for-network-automation)[
and for
]{style="color: #333333;"}[ACLs](https://www.ansible.com/blog/deep-dive-on-cisco-asa-resource-modules)[.
However, simplifying network management is not limited to rather local
network setups: Open]{style="color: #333333;"}
[Shortest]{style="color: #333333;"} [Path First
]{style="color: #333333;"}[( OSPFv2)]{style="color: #333333;"}[ is a
protocol used to distribute IP routing information throughout a single
Autonomous System (AS). It is used in larger network setups, as the
]{style="color: #333333;"}[Wikipedia page so aptly
observes](https://en.wikipedia.org/w/index.php?title=Open_Shortest_Path_First&oldid=967345042)[:]{style="color: #333333;"}

*[OSPF is a widely used IGP in large enterprise networks. IS-IS, another
LSR-based protocol, is more common in large service provider
networks.]{style="color: #333333;"}*

[Managing OSPFv2 manually for a network device can be a very difficult
and tedious task, and more often this needs to be performed carefully,
as the manual process is more prone to human
error.]{style="color: #333333;"}

[This blog post goes through the OSPFV2 resource module for the VyOS
network platform. We will walk through several examples and describe the
use cases for each state parameter and how we envision these being used
in real world
scenarios]{style="color: #333333;"}[.]{style="font-size: 13.5pt; color: #333333;"}

 

# OSPFv2 resource modules example: Vyos

[The goal of OSPFv2 resource modules is to make sure configurations are
consistently applied across the infrastructure with less effort. It
simplifies management and makes it faster and easier to scale without
worrying about the actual implementation details of the network
platforms working under the hood.]{style="color: #333333;"}

[In October of 2019, as part of Red Hat Ansible Engine 2.9, the Ansible
Network Automation team]{style="color: #333333;"} [introduced the
concept of resource
modules](https://www.ansible.com/blog/network-features-coming-soon-in-ansible-engine-2.9)[
to  make network automation easier and more consistent for those
automating various network platforms in
production.]{style="color: #333333;"}

[Ansible Content refers to Ansible Playbooks, modules, module utilities
and plugins. Basically all of the Ansible tools that users utilize to
create their Ansible and the OSPFv2 resource module is part of Ansible
Content Collections. To learn more about Ansible Content Collections,
you can check out two of our blogs: ]{style="color: #333333;"}[Getting
Started with Ansible Content
Collections](https://www.ansible.com/blog/getting-started-with-ansible-collections)
[and]{style="color: #333333;"} [[The Future of Ansible Content
Delivery]{style="color: #1155cc; text-decoration: underline;"}](https://www.ansible.com/blog/the-future-of-ansible-content-delivery)[.]{style="color: #333333;"}

[Let's have a closer look at how the OSPFv2 resource modules work. As an
example, we pick the
vyos]{style="color: #333333;"}[\_](https://docs.ansible.com/ansible/latest/modules/eos_vlans_module.html){style="color: #337ab7;"}[ospfv2
resource module. In this blog, we'll be using a VyOS router with version
1.1.8 (helium) for all the configuration management specific operations.
Also, to better showcase the effect of the modules, we will start with
some ]{style="color: #333333;"}[OSPF version 2 specific
attributes](https://gist.github.com/rohitthakur2590/4446ba7c274659395381495e28229943)[
already configured. Check out the linked listing for further
details.]{style="color: #333333;"}

 

## Accessing and using the VyOS Collection

[To download the VyOS Collection, refer to Automation Hub (fully
supported, requires a Red Hat Ansible Automation Platform subscription)
or Ansible Galaxy (upstream community
supported):]{style="color: #333333;"}

-   [Automation Hub
    Collection](https://cloud.redhat.com/ansible/automation-hub/vyos/vyos)[:
    vyos.vyos]{style="color: #333333;"}
-   [Ansible Galaxy Collection](https://galaxy.ansible.com/vyos/vyos)[:
    vyos.vyos]{style="color: #333333;"}

[To learn more about how to configure downloading via the ansible.cfg
file or requirements.yml file, please refer to the blog,
"]{style="color: #333333;"}[Hands On With Ansible
Collections](https://www.ansible.com/blog/hands-on-with-ansible-collections)[."]{style="color: #333333;"}

[Before we get started, let's quickly explain the rationale behind
naming the network resource modules. Notice for resource modules that
configure OSPFV2 routes, the newly added modules will be named based on
the IP address type. This was done so that those using existing network
modules would not have their Ansible Playbooks stop working and have
sufficient time to migrate to the new network automation
modules.]{style="color: #333333;"}

[A module to configure OSPFv2 is also available for the following
supported platforms:]{style="color: #333333;"}

-   [Arista EOS ]{style="color: #333333;"}
    [(arista.eos.eos_ospfv2](https://galaxy.ansible.com/arista/eos)[) ]{style="color: #333333;"}
-   [Cisco IOS]{style="color: #333333;"}
    [(]{style="color: #333333;"}[cisco.ios.ios_ospfv2](https://galaxy.ansible.com/cisco/ios)[) ]{style="color: #333333;"}
-   [Cisco IOSXR]{style="color: #333333;"}
    [(]{style="color: #333333;"}[cisco.ios.iosxr_ospfv2](https://galaxy.ansible.com/cisco/iosxr)[) ]{style="color: #333333;"}
-   [Cisco NXOS]{style="color: #333333;"}
    [(]{style="color: #333333;"}[cisco.nxos.nxos_ospfv2](https://galaxy.ansible.com/cisco/nxos)[) ]{style="color: #333333;"}
-   [Juniper junos]{style="color: #333333;"}
    [(]{style="color: #333333;"}[junipernetwork.junos.junos_ospfv2](https://galaxy.ansible.com/junipernetworks/junos)[) ]{style="color: #333333;"}
-   [Vyos]{style="color: #333333;"}
    [(]{style="color: #333333;"}[vyos.vyos.vyos_ospfv2](https://galaxy.ansible.com/vyos/vyos)[) ]{style="color: #333333;"}

[The OSPFV2 resource module provides the same level functionality that a
user can achieve when configuring manually on to the VyOS device with
all advantages of Ansible, plus with an added edge of
A]{style="color: #333333;"}[nsible facts gathering and resource
module](https://www.ansible.com/blog/network-features-coming-soon-in-ansible-engine-2.9)
[approach, which is more closely aligned with network professionals day
to day working.]{style="color: #333333;"}

 

# Use Case: OSPFv2 configuration changes

## Using state gathered - Building an Ansible inventory

[Resource modules allow the user to read in existing network
configuration and convert that into a structured data model. The
]{style="color: #333333;"}**[state:
gathered]{style="color: #333333;"}**[ is the equivalent for gathering
Ansible Facts for this specific resource. This example will read in the
existing network configuration and store it as a
flat-file.]{style="color: #333333;"}

[Here is an Ansible Playbook example of using
]{style="color: #333333;"}**[state: gathered
]{style="color: #333333;"}**[and storing the result as YAML into
host_vars. If you are new to Ansible Inventory and want to learn about
group_vars and host_vars, please refer to the
]{style="color: #333333;"}[documentation
here.[]{style="color: #333333;"}](https://docs.ansible.com/ansible/latest/user_guide/intro_inventory.html)

``` 
---
- name: convert configured OSPFV2 resource to structured data
  hosts: vyos
  vars:
    inventory_dir: "lab_inventory"
    inventory_hostname: "vyos"
  gather_facts: false
  tasks:

  - name: Use the OSPFV2 resource module to gather the current config
    vyos.vyos.vyos_ospfv2:
      state: gathered
    register: ospfv2

  - name: Create inventory directory
    file:
      path: "{{ inventory_dir }}/host_vars/{{ inventory_hostname }}"
      state: directory

  - name: Write the OSPFV2 configuration to a file
    copy:
      content: "{{ {'ospfv2': ospfv2['gathered']} | to_nice_yaml }}"
      dest: "{{ inventory_dir }}/host_vars/{{ inventory_hostname }}/ospfv2.yaml"
```

[Execute the Ansible Playbook with the ansible-playbook
command:]{style="color: #333333;"}

[]{style="background-color: transparent;"}

``` 
$ ansible-playbook example.yml
```

[Here is the data structure that was created from reading/gathered
operation  in a brown-field configuration:]{style="color: #333333;"}

``` 
$ cat nw_inventory/host_vars/vyos/ospfv2.yaml
ospfv2:
  areas:
  - area_id: '2'
    area_type:
      normal: true
    authentication: plaintext-password
    shortcut: enable
  - area_id: '4'
    area_type:
      stub:
        default_cost: 20
        set: true
```

[You can check out the full detailed listing of the output of this
example in the ]{style="color: #333333;"}[state: gathered reference
gist](https://gist.github.com/rohitthakur2590/0e18173ee73a07a050d5b02ec6777c3d)[.]{style="color: #333333;"}

 

## Using state merged - Pushing configuration changes

[The state merged will take your Ansible configuration data (i.e.
Ansible variables) and merges them into the network device's running
configuration. This will not affect existing configuration not specified
in your Ansible configuration data. Let's walk through an
example.]{style="color: #333333;"}

[We will modify the flat-file created in the first example with a
]{style="color: #333333;"}[configuration to be
merged](https://gist.github.com/rohitthakur2590/31cf81adff5ff538ee201eae8f66fc7a)[.
Here are the most important pieces:]{style="color: #333333;"}

``` 
areas:
 - area_id: '2'
   area_type:
     normal: true
   authentication: "plaintext-password"
   shortcut: 'enable'
 - area_id: '3'
   area_type:
     nssa:
       set: true
```

[Now let's create an Ansible Playbook to merge this new configuration
into the network device's running
configuration:]{style="color: #333333;"}

``` 
---
- name: Merged state play
  hosts: vyos
  gather_facts: false
  tasks:
    - name: Merge OSPFV2 config with device existing OSPFV2 config
      vyos.vyos.vyos_ospfv2:
        state: merged
        config: "{{ ospfv2 }}"
```

[Execute the Ansible Playbook with the ansible-playbook
command:]{style="color: #333333;"}

``` 
$ ansible-playbook merged.yml
```

[And, once we run the respective Merge play, all of the provided
parameters will be configured on the VyOS router with Ansible
]{style="color: #333333;"}***[changed=True.]{style="color: #333333;"}***

[Note the network configuration after the merge
operation:]{style="color: #333333;"}

``` 
vyos@vyos:~$ show configuration commands | grep ospf
set protocols ospf area 2 area-type 'normal'
set protocols ospf area 2 authentication 'plaintext-password'
set protocols ospf area 2 shortcut 'enable'
set protocols ospf area 3 area-type 'nssa'
set protocols ospf area 4 area-type stub default-cost '20'
```

[Note that this listing only shows a few highlights; the full listing is
available in the ]{style="color: #333333;"}[merged
gist](https://gist.github.com/rohitthakur2590/9d59ca2b4e2b396bea1af32eefcc2d9d)[.]{style="color: #333333;"}

[Let's take a look at what has changed through this operation: if we go
through the device output, there are a few
observations:]{style="color: #333333;"}

-   [Attribute area with area_id '3' got added to the OSPF areas
    list. ]{style="color: #333333;"}
-   [The redistribute and parameter attribute got configured for
    OSPF.]{style="color: #333333;"}
-   [If there was an already configured OSPF with AREA and the user
    wanted to update any parameter for that particular AREA, then the
    user can also use the Merged state to update the AREA under
    OSPFV2.]{style="color: #333333;"}

[With the second run, the respective Merge Play runs again and Ansible
charm of Idempotency comes to picture. If nothing's changed, play run
results into changed=False,]{style="color: #333333;"} [which confirms to
the user that all of the provided configurations in the play are already
configured on the IOS device.]{style="color: #333333;"}

 

## Using state replaced - Replacing configuration

[If the user wants to re-configure the VyOS device entirely
pre-configured OSPFV2 with the provided OSPFV2 configuration, then the
resource module
]{style="color: #333333;"}*[replaced]{style="color: #333333;"}*[ state
comes into picture.]{style="color: #333333;"}

[The scope of the replaced operation is up to the individual processes.
In the case of VyOS only a single process is supported. As a result, the
replaced state acts similar to the overridden state. For that reason a
dedicated overridden state is not required with the VyOS modules. Other
network platforms that support multiple OSPFV2 processes do have the
overridden state operation.]{style="color: #333333;"}

[Using the overridden state, a user can override all OSPFV2 resource
attributes with user-provided OSPFV2 configuration. Since this resource
module state overrides all pre-existing attributes of the resource
module, the overridden state should be used cautiously, as OSPFV2
configurations are very important; if all the configurations are
mistakenly replaced with the play input configuration, it might create
unnecessary issues for the network
administrators. ]{style="color: #333333;"}

[In this scenario, OSPF with 'n' number AREAs are already configured on
the VyOS device, and now the user wants to update the AREA list with a
new set of AREAs and discard all the already configured OSPF AREAs.
Here, the resource module replaced state will be an ideal choice and, as
the name suggests, the replaced state will replace OSPF existing AREA
list with a new set of AREAs given as input by the
user.]{style="color: #333333;"}

[If a user tries to configure any new OSPFV2 AREA/attribute that's not
already pre-configured on the device, it'll act as a merged state and
the vyos_ospfv2 module will try to configure the OSPF AREAs given as
input by the user inside the replace play.]{style="color: #333333;"}

[We will modify the flat-file created in the first
example:]{style="color: #333333;"}

``` 
areas:
 - area_id: '2'
   area_type:
     normal: true
   authentication: "plaintext-password"
   shortcut: 'enable'
 - area_id: '4'
   area_type:
     stub:
      default_cost: 20
```

[Check out the ]{style="color: #333333;"}[full input config
structure](https://gist.github.com/rohitthakur2590/31b2cce1f5157382025ae6a9d89add04)[
if you want to learn more details.]{style="color: #333333;"}

[Again, we create an Ansible Playbook to merge this new configuration
into the network device's running
configuration:]{style="color: #333333;"}

``` 
---
- name: Replaced state play
  hosts: vyos
  gather_facts: false
  tasks:
    - name: Replace OSPFV2 config with device existing OSPFV2 config
      vyos.vyos.vyos_ospfv2:
        state: replaced
        config: "{{ ospfv2 }}"
```

[Once we run the respective Replaced play, all of the provided
parameters will override all the existing OSPFv2 resource specific
config on the VyOS router with Ansible
]{style="color: #333333;"}**[changed=True]{style="color: #333333;"}**[.]{style="color: #333333;"}

[The network device configuration after the Replaced
operation:]{style="color: #333333;"}

``` 
vyos@vyos:~$ show configuration commands | grep ospf
set protocols ospf area 2 area-type 'normal'
set protocols ospf area 2 authentication 'plaintext-password'
set protocols ospf area 2 shortcut 'enable'
set protocols ospf area 4 area-type stub default-cost '20'
set protocols ospf area 4 network '192.0.2.0/24'
```

[Check out the ]{style="color: #333333;"}[corresponding
gist](https://gist.github.com/rohitthakur2590/57bf71dbe2c8417426e7ddcb4f8fd7c0)[
for more details.]{style="color: #333333;"}

[If we dig into the above output, we note the following
changes:]{style="color: #333333;"}

-   [Replaced negates all of the pre-existing OSPFV2 resource-specific
    attributes and deletes those configurations, which are not present
    inside the replaced play. In the above example, ospfv2 area-id 3 got
    deleted.]{style="color: #333333;"}
-   [For the OSPFV2 configurations that are pre-existing and also in the
    play, vyos_ospfv2 replaced state will try to delete/negate all the
    pre-existing OSPFV2 config and then configure the new OSPFV2 config
    as mentioned in the play.]{style="color: #333333;"}
-   [For any non-existing OSPFV2 specific attribute, the replaced state
    will configure the OSPFV2 in the same manner as the Merged state. In
    the above example, a new network address configured for OSPFv2
    area-id 4.]{style="color: #333333;"}

[With the second run of the above play,]{style="color: #333333;"} [there
are no changes reported which satisfies the Ansible
idempotency.]{style="color: #333333;"}

 

## Using state deleted - Delete configuration

[Now that we've talked about how we can configure OSPFV2 specific
attributes on the VyOS device by using vyos_ospfv2 resource module
merged and replaced state, it's time we talk about how we can delete the
pre-configured OSPFV2 attributes and what level of granularity is
available with the deleted operational state for the
user.]{style="color: #333333;"}

[Deleting ]{style="color: #333333;"}**[ALL]{style="color: #333333;"}**
**[OSPFV2]{style="color: #333333;"}**[ config]{style="color: #333333;"}
[in one go leads to deleting all the pre-configured
]{style="color: #333333;"}***[OSPFV2
]{style="color: #333333;"}***[specific
attributes]{style="color: #333333;"} [from
the]{style="color: #333333;"}**[ VyOS]{style="color: #333333;"}**[
device. But that said, this is a very critical delete operation and if
not used judiciously, it has the power to delete all pre-configured
]{style="color: #333333;"}***[OSPFV2]{style="color: #333333;"}***[ and
can result in the production environment with the router having
]{style="color: #333333;"}***[no]{style="color: #333333;"}***[
pre-configured ]{style="color: #333333;"}***[ OSPFV2
attributes]{style="color: #333333;"}***[.]{style="color: #333333;"}

[Let's create an Ansible Playbook to merge this new configuration into
the network device's running configuration:]{style="color: #333333;"}

``` 
---
- name: Deleted state play
  hosts: vyos
  gather_facts: false
  tasks:
    - name: Delete ALL OSPFV2 config
      vyos.vyos.vyos_ospfv2:
        state: deleted
```

[After we execute the playbook, the network device configuration
changed:]{style="color: #333333;"}

``` 
vyos@vyos:~$ show configuration commands | grep ospf
vyos@vyos:~$
```

[Make sure to look at the ]{style="color: #333333;"}[full listing of the
changed
values](https://gist.github.com/rohitthakur2590/bb93302da90fe9f0865313b112998602)[.
If we dig into the above output briefly, we can see that all the ospfv2
resource-specific config has been removed from the network
configuration.]{style="color: #333333;"}

 

## Using state rendered - Development and working offline

[Ansible renders the provided configuration in the task in the
device-native format (for example, VyOS CLI). Ansible returns this
rendered configuration in the rendered key in the result. Note this
state does not communicate with the network device and can be used
offline.]{style="color: #333333;"}

[To have a config to be rendered, modify the YAML file created in the
first scenario.  For example, if this is the vyos_ospfv2 module, you can
just add a few more attributes to show we change the data model yet
again.]{style="color: #333333;"}

``` 
areas:
 - area_id: '2'
   area_type:
     normal: true
   authentication: "plaintext-password"
```

[See the full listing in the ]{style="color: #333333;"}[corresponding
rendered
gist](https://gist.github.com/rohitthakur2590/d6f6cd599c3e2fecb51dfe628d640a8f)[.]{style="color: #333333;"}

[We create a playbook to execute this:]{style="color: #333333;"}

``` 
---
- name: Rendered state play
  hosts: vyos
  gather_facts: false
  tasks:
    - name: Render the provided configuration
      vyos.vyos.vyos_ospfv2:
        config: "{{ ospfv2 }}"
        state: rendered
```

[This produces the following output:]{style="color: #333333;"}

``` 
"rendered": [
       "set protocols ospf log-adjacency-changes 'detail'",
       "set protocols ospf max-metric router-lsa administrative",
       "set protocols ospf max-metric router-lsa on-shutdown 10",
```

[Check out the ]{style="color: #333333;"}[corresponding
gist](https://gist.github.com/rohitthakur2590/862b2321283aafb7c41af342f227d1e8)[
for more details.]{style="color: #333333;"}

[If we dig into the above output, we can see that nothing has changed at
all; rendered doesn't even require the connection establishment with an
actual network device.]{style="color: #333333;"}

## Using state parsed - Development and working offline

[Ansible parses the configuration from the running_configuration option
into Ansible structured data in the parsed key in the result. Note this
does not gather the configuration from the network device, so this state
can be used offline.]{style="color: #333333;"}

[As the config to be parsed we take device-native format
configuration:]{style="color: #333333;"}

``` 
set protocols ospf area 2 area-type 'normal'
set protocols ospf area 2 authentication 'plaintext-password'
set protocols ospf area 2 shortcut 'enable'
set protocols ospf area 4 area-type stub default-cost '20'
set protocols ospf area 4 network '192.0.2.0/24'
set protocols ospf area 4 range 192.0.3.0/24 cost '10'
```

[The playbook to apply this configuration is:]{style="color: #333333;"}

``` 
---
- name: Parsed state play
  hosts: vyos
  gather_facts: false
  tasks:
    - name: Parse the provided OSPFV2 configuration
      vyos.vyos.vyos_ospfv2:
        running_config:
           "set protocols ospf area 2 area-type 'normal'
            set protocols ospf area 2 authentication 'plaintext-password'
            set protocols ospf area 2 shortcut 'enable'
        state: parsed
```

[Execute the playbook generates the following
output:]{style="color: #333333;"}

``` 
"parsed": {
        "areas": [
            {
                "area_id": "2",
                "area_type": {
                    "normal": true
                },
                "authentication": "plaintext-password",
                "shortcut": "enable"
             }
                
                ]
            }  
...
```

[If we dig into the above output, we can see that nothing has changed at
all, parsed operation doesn't even require the connection establishment
with an actual network device.]{style="color: #333333;"}[\
]{style="color: #333333;"}[Note: parsed input to be provided as value to
running_config key.]{style="color: #333333;"}

 

# Takeaways & Next Steps

[As shown above, with the help of the resource modules management of
OSPFV2, resource-specific configurations can be greatly simplified.
Users don\'t need to bother much about OSPFV2 implementation details for
each platform, they can just enter the actual data. By using the merged,
replaced and overridden parameters, we allow much more flexibility for
network engineers to adopt automation in incremental steps. The other
operations like gathered, rendered and parsed allow a better, user
friendly handling of the facts and the data managed within these
tasks.]{style="color: #333333;"}
