---
author: Sumit Jaiswal
date: 2020-10-12 00:00 UTC
description: In October 2019 as part of the Red Hat Ansible Engine 2.9
  release, the Ansible Network Automation team introduced the first
  resource modules. These opinionated network modules make network
  automation easier and more consistent for those automating various
  network platforms in production.
lang: en-us
title: Deep Dive, ACL Configuration Management Using Ansible Network Automation Resource Modules
---

# Deep Dive, ACL Configuration Management Using Ansible Network Automation Resource Modules

[In October 2019 as part of the Red Hat Ansible Engine 2.9 release, the
Ansible Network Automation team]{style="color: #333333;"} [introduced
the first resource
modules](https://www.ansible.com/blog/network-features-coming-soon-in-ansible-engine-2.9){style="color: #337ab7;"}[.
]{style="color: #333333;"}[These opinionated network modules make
network automation easier and more consistent for those automating
various network platforms in production. The goal for resource modules
is to avoid creating and maintaining overly complex jinja2 templates for
rendering and pushing network configuration. ]{style="color: #333333;"}

[This blog post covers the newly released
]{style="color: #333333;"}[ios_acls]{style="color: #333333; font-family: 'courier new', courier;"}[
resource module and how to automate manual processes associated with
switch and router configurations. These network automation modules are
used for configuring routers and switches from popular vendors (but not
limited to) Arista, Cisco, Juniper, and VyOS. The access control lists
(ACLs) network resource modules are able to read ACL configuration from
the network, provide the ability to modify and then push changes to the
network device. These opinionated network resource modules make network
automation easier and more consistent for those automating various
network platforms in production. I'll walk through several examples and
describe the use cases for each state parameter (including three newly
released state types) and how these are used in real world
scenarios.]{style="color: #333333;"}

## The Certified Content Collection

[This blog uses the
]{style="color: #000000;"}[cisco.ios]{style="color: #000000; font-family: 'courier new', courier;"}[
Collection maintained by the Ansible team, but there are other platforms
that also have ACL resource modules, such as
]{style="color: #000000;"}[arista.eos]{style="color: #000000; font-family: 'courier new', courier;"}[,
]{style="color: #000000;"}[junipernetworks.junos]{style="color: #000000; font-family: 'courier new', courier;"}[,
and
]{style="color: #000000;"}[vyos.vyos]{style="color: #000000; font-family: 'courier new', courier;"}[.]{style="color: #000000;"}

-   **[How to obtain the certified (supported) and upstream (community)
    Collection ]{style="color: #000000;"}[\
    ]{style="color: #000000;"}[\
    ]{style="color: #000000;"}**[The upstream community Collection can
    be found on Ansible Galaxy:
    ]{style="color: #000000;"}[https://galaxy.ansible.com/cisco/ios**[\
    ]{style="color: #000000;"}[\
    ]{style="color: #000000;"}**](https://galaxy.ansible.com/cisco/ios)[The
    downstream supported Collection can be found on Automation
    Hub:]{style="color: #000000;"}**[\
    ]{style="color: #000000;"}**[https://cloud.redhat.com/ansible/automation-hub/cisco/ios**[\
    ]{style="color: #000000;"}[\
    ]{style="color: #000000;"}**](https://cloud.redhat.com/ansible/automation-hub/cisco/ios)[For
    more information on Ansible Content Collections, please refer to the
    following documentation:
    ]{style="color: #000000;"}[https://docs.ansible.com/ansible/latest/user_guide/collections_using.html[]{style="color: #000000;"}](https://docs.ansible.com/ansible/latest/user_guide/collections_using.html)

[Before starting, let's quickly explain the rationale behind the naming
of the network resource modules. The newly added ACLs modules will be
plural
(]{style="color: #333333;"}[eos_acls]{style="color: #333333; font-family: 'courier new', courier;"}[,
]{style="color: #333333;"}[ios_acls]{style="color: #333333; font-family: 'courier new', courier;"}[,
]{style="color: #333333;"}[junos_acls]{style="color: #333333; font-family: 'courier new', courier;"}[,
]{style="color: #333333;"}[nxos_acls]{style="color: #333333; font-family: 'courier new', courier;"}[,
]{style="color: #333333;"}[iosxr_acls]{style="color: #333333; font-family: 'courier new', courier;"}[). 
The older singular form modules (e.g.
[ios_acl]{style="font-family: 'courier new', courier;"},
[nxos_acl]{style="font-family: 'courier new', courier;"}) will be
deprecated over time. This naming change was done so that those using
existing network modules would not have their Ansible Playbooks stop
working and have sufficient time to migrate to the new network
automation modules.]

## Platform support

[This module is also available for the following Ansible-maintained
platforms on both Automation Hub (supported) and Galaxy
(community):]{style="color: #000000;"}[\
\
]{style="color: #000000;"}

+-----------------+-----------------+-----------------+-----------------+
| [Plat           | [Full           | [Automation Hub | [Ansible Galaxy |
| form]{style="co | Collection      | Link (requires  | Link]{style="co |
| lor: #000000;"} | pa              | subscript       | lor: #000000;"} |
|                 | th]{style="colo | ion)]{style="co |                 |
|                 | r: #000000;"}[\ | lor: #000000;"} |                 |
|                 | ]{sty           |                 |                 |
|                 | le="color: #000 |                 |                 |
|                 | 000;"}[namespac |                 |                 |
|                 | e.collection.mo |                 |                 |
|                 | dule]{style="co |                 |                 |
|                 | lor: #000000;"} |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| [Arista         | [[ari           | [Automation     | [G              |
| EOS]{style="co  | sta.eos.eos_acl | Hub]            | alaxy](https:// |
| lor: #000000;"} | s]{style="font- | (https://cloud. | galaxy.ansible. |
|                 | family: 'courie | redhat.com/ansi | com/arista/eos) |
|                 | r new', courier | ble/automation- |                 |
|                 | ;"} ]{style="co | hub/arista/eos) |                 |
|                 | lor: #000000;"} |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| [Cisco          | [cisco.         | [Automation     | [               |
| IOS]{style="co  | ios.ios_acls]{s | Hub             | Galaxy](https:/ |
| lor: #000000;"} | tyle="color: #0 | ](https://cloud | /galaxy.ansible |
|                 | 00000; font-fam | .redhat.com/ans | .com/cisco/ios) |
|                 | ily: 'courier n | ible/automation |                 |
|                 | ew', courier;"} | -hub/cisco/ios) |                 |
+-----------------+-----------------+-----------------+-----------------+
| [Cisco          | [cisco.iosx     | [Automation     | [Ga             |
| I               | r.iosxr_acls]{s | Hub](           | laxy](https://g |
| OSXR]{style="co | tyle="color: #0 | https://cloud.r | alaxy.ansible.c |
| lor: #000000;"} | 00000; font-fam | edhat.com/ansib | om/cisco/iosxr) |
|                 | ily: 'courier n | le/automation-h |                 |
|                 | ew', courier;"} | ub/cisco/iosxr) |                 |
+-----------------+-----------------+-----------------+-----------------+
| [Cisco          | [cisco.nx       | [Automation     | [G              |
| NXOS]{style="co | os.nxos_acls]{s | Hub]            | alaxy](https:// |
| lor: #000000;"} | tyle="color: #0 | (https://cloud. | galaxy.ansible. |
|                 | 00000; font-fam | redhat.com/ansi | com/cisco/nxos) |
|                 | ily: 'courier n | ble/automation- |                 |
|                 | ew', courier;"} | hub/cisco/nxos) |                 |
+-----------------+-----------------+-----------------+-----------------+
| [Juniper        | [junip          | [Automation     | [Galaxy](http   |
| J               | ernetworks.juno | Hub](https://cl | s://galaxy.ansi |
| unOS]{style="co | s.junos_acls]{s | oud.redhat.com/ | ble.com/juniper |
| lor: #000000;"} | tyle="color: #0 | ansible/automat | networks/junos) |
|                 | 00000; font-fam | ion-hub/juniper |                 |
|                 | ily: 'courier n | networks/junos) |                 |
|                 | ew', courier;"} |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| [               | [vy             | [Automation     | [               |
| VyOs]{style="co | os.vyos.vyos_fi | Hub             | Galaxy](https:/ |
| lor: #000000;"} | rewall_rules]{s | ](https://cloud | /galaxy.ansible |
|                 | tyle="color: #0 | .redhat.com/ans | .com/vyos/vyos) |
|                 | 00000; font-fam | ible/automation |                 |
|                 | ily: 'courier n | -hub/vyos/vyos) |                 |
|                 | ew', courier;"} |                 |                 |
+-----------------+-----------------+-----------------+-----------------+

## Getting started - Managing the ACL configuration with Ansible

[An a]{style="color: #000000;"}[ccess control list (ACL) provides rules
that are applied to port numbers and/or IP addresses  permitted to
transit or reach that network device. ACL order of access control entry
(ACE) is critical because the ACEs sequence/order route decides which
rules are applied to inbound/outbound network
traffic.]{style="color: #333333;"}

[An ACL resource module provides the same level of functionality that a
user can achieve when configuring manually on the Cisco IOS device. But
combined with Ansible facts gathering and resource module approach, this
is more closely aligned with how network professionals work day to
day.]{style="color: #333333;"}

[I'll be using an IOS router with version 15.6(3)M2 for all the
configuration of this post. Below is the initial state of router ACLs
configuration and currently there are already active ACLs configured on
the device.]{style="color: #333333;"}

### Network device configuration

``` 
cisco#sh access-lists
Extended IP access list 110
  10 deny icmp 192.0.2.0 0.0.0.255 192.0.3.0 0.0.0.255 traceroute dscp ef ttl eq 10
  20 deny tcp host 198.51.100.0 host 198.51.110.0 eq telnet ack
Extended IP access list test_acl
  10 deny tcp 192.0.2.0 0.0.0.255 192.0.3.0 0.0.0.255 eq www fin option traceroute ttl eq 10
IPv6 access list R1_TRAFFIC
  deny tcp any eq www any eq telnet ack dscp af11 sequence 10
```

 

## Using state gathered - Building an Ansible inventory

Resource modules allow the user to read in an existing network
configuration and convert that into a structured data model. The
**state: gathered** is the equivalent for gathering Ansible facts for
this specific resource. This example will read in the existing network
configuration and store it as a flat file.

### Ansible Playbook Example

Here is an Ansible Playbook example of using **state: gathered** and
storing the result as YAML into host_vars.  If you are new to the
concept of Ansible inventory and want to learn more about
[group_vars]{style="font-family: 'courier new', courier;"} and
[host_vars]{style="font-family: 'courier new', courier;"}, please refer
to the [Ansible User Guide:
Inventory.](https://docs.ansible.com/ansible/latest/user_guide/intro_inventory.html)

``` 
---
- name: convert configured ACLs to structured data
  hosts: cisco
  gather_facts: false
  tasks:


    - name: Use the ACLs resource module to gather the current config
       cisco.ios.ios_acls:
           state: gathered
           register: acls

    - name: Create inventory directory
      file:
       path: "{{ inventory_dir }}/host_vars/{{ inventory_hostname }}"
       state: directory

    - name: Write the ACL configuration to a file
      copy:
        content: "{{ {‘acls’: acls['gathered']} | to_nice_yaml }}"
        dest: "{{ inventory_dir }}/host_vars/{{ inventory_hostname }}/acls.yaml"
```

Execute the Ansible Playbook with the ansible-playbook command:

[ansible-playbook
example.yml]{style="font-family: 'courier new', courier;"}

### Examine File contents

Here is the data structure that was created from reading in an existing
configuration:

``` 
$ cat lab_inventory/host_vars/rtr2/acls.yaml
acls:
- acls:
     - aces:
         - destination:
             address: 192.0.3.0
             wildcard_bits: 0.0.0.255
           dscp: ef
           grant: deny
           protocol: icmp
           protocol_options:
             icmp:
               traceroute: true
           sequence: 10
           source:
             address: 192.0.2.0
             wildcard_bits: 0.0.0.255
           ttl:
             eq: 10
         - destination:
             host: 198.51.110.0
             port_protocol:
               eq: telnet
           grant: deny
           protocol: tcp
           protocol_options:
             tcp:
               ack: true
           sequence: 20
           source:
             host: 198.51.100.0
       acl_type: extended
       name: '110'
     - aces:
         - destination:
             address: 192.0.3.0
             port_protocol:
                 eq: www
             wildcard_bits: 0.0.0.255
           grant: deny
           option:
               traceroute: true
           protocol: tcp
           protocol_options:
               tcp:
                   fin: true
           sequence: 10
           source:
             address: 192.0.2.0
             wildcard_bits: 0.0.0.255
           ttl:
               eq: 10
       acl_type: extended
       name: test_acl
   afi: ipv4
 - acls:
     - aces:
         - destination:
             any: true
             port_protocol:
               eq: telnet
           dscp: af11
           grant: deny
           protocol: tcp
           protocol_options:
             tcp:
               ack: true
           sequence: 10
           source:
             any: true
             port_protocol:
               eq: www
       name: R1_TRAFFIC
   afi: ipv6
```

In the above output (and future reference):

-   [afi]{style="font-family: 'courier new', courier;"} refers to
    address family identifier, either IPv4 or IPv6
-   [acls]{style="font-family: 'courier new', courier;"} refers to
    access control lists, and returns a list of dictionaries (ACEs)
-   [aces]{style="font-family: 'courier new', courier;"} refers to
    access control entry, or the specific rule and sequence 

 

## Using state merged - Pushing configuration changes

The state merged will take your Ansible configuration data (for example
Ansible variables) and merges them into the network device's network
configuration. This will not affect existing configuration not specified
in your Ansible configuration data. Let's walk through an example.

### Modify stored file

We will modify the flat file created in the first example. We will then
create an Ansible Playbook to merge this new configuration into the
network device's running configuration.

Reference link:
[https://gist.githubusercontent.com/justjais/bb2a65c373ab4e64d1eeb47bc425c613/raw/056d2a6a44910863cbbbf38cad2273435574db84/Merged.txt](https://gist.githubusercontent.com/justjais/bb2a65c373ab4e64d1eeb47bc425c613/raw/056d2a6a44910863cbbbf38cad2273435574db84/Merged.txt)

``` 
acls:
- afi: ipv4
  acls:
   - name: std_acl
     acl_type: standard
     aces:
       - grant: deny
         source:
           address: 192.168.1.200
       - grant: deny
         source:
           address: 192.168.2.0
           wildcard_bits: 0.0.0.255
   - name: 110
     aces:
       - grant: deny
         sequence: 10
         protocol_options:
           icmp:
             traceroute: true
         source:
           address: 192.0.2.0
           wildcard_bits: 0.0.0.255
         destination:
           address: 192.0.3.0
           wildcard_bits: 0.0.0.255
         dscp: ef
         ttl:
           eq: 10
       - grant: deny
         protocol_options:
           tcp:
             ack: true
         source:
           host: 198.51.100.0
         destination:
           host: 198.51.110.0
           port_protocol:
             eq: telnet
   - name: test
     acl_type: extended
     aces:
       - grant: deny
         protocol_options:
           tcp:
             fin: true
         source:
           address: 192.0.2.0
           wildcard_bits: 0.0.0.255
         destination:
           address: 192.0.3.0
           wildcard_bits: 0.0.0.255
           port_protocol:
             eq: www
         option:
           traceroute: true
         ttl:
           eq: 10
   - name: 123
     aces:
       - grant: deny
         protocol_options:
           tcp:
             ack: true
         source:
           address: 198.51.100.0
           wildcard_bits: 0.0.0.255
         destination:
           address: 198.51.101.0
           wildcard_bits: 0.0.0.255
           port_protocol:
             eq: telnet
         tos:
           service_value: 12
      - grant: deny
         protocol_options:
           tcp:
             ack: true
         source:
           address: 192.0.3.0
           wildcard_bits: 0.0.0.255
         destination:
           address: 192.0.4.0
           wildcard_bits: 0.0.0.255
           port_protocol:
             eq: www
         dscp: ef
         ttl:
           lt: 20
- afi: ipv6
  acls:
   - name: R1_TRAFFIC
     aces:
       - grant: deny
         protocol_options:
           tcp:
             ack: true
         source:
           any: true
           port_protocol:
             eq: www
         destination:
           any: true
           port_protocol:
             eq: telnet
         dscp: af11
```

Ansible Playbook Example

``` 
---
- name: Merged state play
  hosts: cisco
  gather_facts: false
  tasks:
    - name: Merge ACLs config with device existing ACLs config
      cisco.ios.ios_acls:
        state: merged
        config: "{{ acls }}"
```

Once we run the respective Merge play, all of the provided parameters
will be configured on the Cisco IOS router with Ansible
***changed=True***

[Network device configuration]{style="font-size: 14pt; color: #434343;"}

``` 
cisco#sh access-lists
Standard IP access list std_acl
   10 deny   192.168.1.200
   20 deny   192.168.2.0, wildcard bits 0.0.0.255
Extended IP access list 110
   10 deny icmp 192.0.2.0 0.0.0.255 192.0.3.0 0.0.0.255 traceroute dscp ef ttl eq 10
   20 deny tcp host 198.51.100.0 host 198.51.110.0 eq telnet ack
Extended IP access list 123
   10 deny tcp 198.51.100.0 0.0.0.255 198.51.101.0 0.0.0.255 eq telnet ack tos 12
   20 deny tcp 192.0.3.0 0.0.0.255 192.0.4.0 0.0.0.255 eq www ack dscp ef ttl lt 20
Extended IP access list test
   10 deny tcp 192.0.2.0 0.0.0.255 192.0.3.0 0.0.0.255 eq www fin option traceroute ttl eq 10
IPv6 access list R1_TRAFFIC
   deny tcp any eq www any eq telnet ack dscp af11 sequence 10
```

If we dig slightly into the device output, we make the following
observations:

-   Based on the AFI value, it's decided by the module to call IP/IPV6
    access-lists. 
-   The 'acl_type' key is required for named ACLs.
-   For ACLs identified by a number rather than a name, the 'acl_type'
    is derived from the platform's documented ACL number ranges. (eg
    Standard = 1--99 and 1300--1999, Extended = 100--199 and 2000--2699,
    etc)
-   If the sequence number is not mentioned in the ACE, it will be
    configured based on the order provided in the play. 
-   With the second run, the respective Merge Play runs again and
    Ansible charm of Idempotency comes to picture, and if nothing's
    changed, play run results into changed=False, which confirms to the
    user that all of the provided configurations in the play are already
    configured on the IOS device.

 

## Using state replaced - Pushing configuration changes

[The replaced parameter enforces the data model on the network device
for each configured ACL/ACE. If we modify any of the ACL/ACEs, it will
enforce all the parameters this resource module is aware of. To think of
this another way, the replaced parameter is aware of all the commands
that should and shouldn't be there.]{style="color: #000000;"}

[For this scenario, an ACL with some ACEs is already configured on the
Cisco IOS device, and now the user wants to update the ACL with a new
set of ACEs and discard all the already configured ACL ACEs. The
resource module that replaced "s" will replace ACL existing ACEs with a
new set of ACEs given as input by the user.]{style="color: #000000;"}

[Ref gist link:
]{style="color: #000000;"}<https://gist.githubusercontent.com/justjais/bb2a65c373ab4e64d1eeb47bc425c613/raw/056d2a6a44910863cbbbf38cad2273435574db84/Replaced.txt>[](https://gist.githubusercontent.com/justjais/bb2a65c373ab4e64d1eeb47bc425c613/raw/056d2a6a44910863cbbbf38cad2273435574db84/Replaced.txt)

``` 
acls:
- afi: ipv4
  acls:
   - name: 110
     aces:
       - grant: deny
         protocol_options:
           tcp:
             syn: true
         source:
           address: 192.0.2.0
           wildcard_bits: 0.0.0.255
         destination:
           address: 192.0.3.0
           wildcard_bits: 0.0.0.255
           port_protocol:
             eq: www
         dscp: ef
         ttl:
           eq: 10
   - name: 150
     aces:
       - grant: deny
         sequence: 20
         protocol_options:
           tcp:
             syn: true
         source:
           address: 198.51.100.0
           wildcard_bits: 0.0.0.255
           port_protocol:
             eq: telnet
         destination:
           address: 198.51.110.0
           wildcard_bits: 0.0.0.255
           port_protocol:
             eq: telnet
         dscp: ef
         ttl:
           eq: 10
```

Ansible Playbook Example

``` 
---
- name: Replaced state play
  hosts: cisco
  gather_facts: false
  tasks:
    - name: Replace ACLs config with device existing ACLs config
      cisco.ios.ios_acls:
        state: replaced
        config: "{{ acls }}"
```

[With the above play, the user is replacing the 123 extended ACL with
the provided ACL ACEs configuration and also configuring the 150
extended new ACL ACEs.]{style="color: #333333;"}

[Before running the
]{style="color: #333333;"}[replaced]{style="color: #333333;"}[ play
network device configuration:]{style="color: #333333;"}

``` 
cisco#sh access-lists
Standard IP access list std_acl
   10 deny   192.168.1.200
   20 deny   192.168.2.0, wildcard bits 0.0.0.255
Extended IP access list 110
   10 deny icmp 192.0.2.0 0.0.0.255 192.0.3.0 0.0.0.255 traceroute dscp ef ttl eq 10
   20 deny tcp host 198.51.100.0 host 198.51.110.0 eq telnet ack
Extended IP access list 123
   10 deny tcp 198.51.100.0 0.0.0.255 198.51.101.0 0.0.0.255 eq telnet ack tos 12
   20 deny tcp 192.0.3.0 0.0.0.255 192.0.4.0 0.0.0.255 eq www ack dscp ef ttl lt 20
Extended IP access list test
   10 deny tcp 192.0.2.0 0.0.0.255 192.0.3.0 0.0.0.255 eq www fin option traceroute ttl eq 10
IPv6 access list R1_TRAFFIC
   deny tcp any eq www any eq telnet ack dscp af11 sequence 10
```

With replaced Play run, commands that are fired:

``` 
- ip access-list extended 110
- no 10
- no 20
- deny tcp 192.0.2.0 0.0.0.255 192.0.3.0 0.0.0.255 eq www syn dscp ef ttl eq 10
- ip access-list extended 150
- 20 deny tcp 198.51.100.0 0.0.0.255 eq telnet 198.51.110.0 0.0.0.255 eq telnet syn  dscp ef ttl eq 10
```

After running the replaced play network device configuration:

``` 
cisco#sh access-lists
Standard IP access list std_acl
   10 deny   192.168.1.200
   20 deny   192.168.2.0, wildcard bits 0.0.0.255
Extended IP access list 110
   10 deny tcp 192.0.2.0 0.0.0.255 192.0.3.0 0.0.0.255 eq www syn dscp ef ttl eq 10
Extended IP access list 123
   10 deny tcp 198.51.100.0 0.0.0.255 198.51.101.0 0.0.0.255 eq telnet ack tos 12
   20 deny tcp 192.0.3.0 0.0.0.255 192.0.4.0 0.0.0.255 eq www ack dscp ef ttl lt 20
Extended IP access list 150
   20 deny tcp 198.51.100.0 0.0.0.255 eq telnet 198.51.110.0 0.0.0.255 eq telnet syn dscp ef ttl eq 10
Extended IP access list test
   10 deny tcp 192.0.2.0 0.0.0.255 192.0.3.0 0.0.0.255 eq www fin option traceroute ttl eq 10
IPv6 access list R1_TRAFFIC
   deny tcp any eq www any eq telnet ack dscp af11 sequence 10
```

[If we dig the output briefly, we may have following
observation:]{style="color: #333333;"}

-   [replaced]{style="font-family: 'courier new', courier;"} will negate
    all the pre-existing ACEs under the input ACL and then apply the
    configuration provided as input in the play. The same behaviour can
    be seen in the commands output above for numbered ACL 123, where the
    pre-existing ACEs at sequence 10 and 20 are negated first before
    applying the changes for newer ACE configuration.
-   For the 150 extended ACL ACEs, since it wasn't already
    pre-configured on the device, the module goes ahead and applies the
    ACE configuration provided as input in the play. One thing to note
    here is that in the play input configuration value to sequence is
    mentioned as 20, and as a result ACE is configured on sequence 20
    instead of 10, which would have been the case if value to sequence
    wasn't provided by the user.

[With the second run of the above play, changed comes as false, which
satisfies the Ansible idempotency.]{style="color: #333333;"}

## Using state overridden - Pushing configuration changes

For this example, we will mix it up slightly. Pretend you are a user
making a bespoke configuration on the network device (making a change
outside of automation).  The [state:
overridden]{style="font-family: 'courier new', courier;"} will circle
back on enforcing the data model (configuration policy enforcement) and
remove the bespoke change.

If the user wants to re-configure the Cisco IOS device entirely
pre-configured ACLs, then resource module overridden state is the most
appropriate. When using the overridden state, a user can override all
ACLs with user provided ACLs.

To show the difference between replaced and overridden state working, we
will be using the same play that we used for the replaced scenario,
keeping the pre-existing configuration the same as well.

Ref gist link:
[https://gist.githubusercontent.com/justjais/bb2a65c373ab4e64d1eeb47bc425c613/raw/056d2a6a44910863cbbbf38cad2273435574db84/Overridden.txt](https://gist.githubusercontent.com/justjais/bb2a65c373ab4e64d1eeb47bc425c613/raw/056d2a6a44910863cbbbf38cad2273435574db84/Overridden.txt)

ACLs configuration:

``` 
acls:
- afi: ipv4
  acls:
   - name: 110
     aces:
       - grant: deny
         sequence: 20
         protocol_options:
           tcp:
             ack: true
         source:
           address: 198.51.100.0
           wildcard_bits: 0.0.0.255
           port_protocol:
             eq: telnet
         destination:
           address: 198.51.110.0
           wildcard_bits: 0.0.0.255
           port_protocol:
             eq: www
         dscp: ef
         ttl:
           eq: 10
   - name: 150
     aces:
       - grant: deny
         sequence: 10
         protocol_options:
           tcp:
             syn: true
         source:
           address: 198.51.100.0
           wildcard_bits: 0.0.0.255
           port_protocol:
             eq: telnet
         destination:
           address: 198.51.110.0
           wildcard_bits: 0.0.0.255
           port_protocol:
             eq: telnet
         dscp: ef
         ttl:
           eq: 10
```

Ansible Playbook Example

``` 
---
- name: Overridden state play
  hosts: cisco
  gather_facts: false
  tasks:
    - name: Override ACLs config with device existing ACLs config
      cisco.ios.ios_acls:
        state: overridden
        config: "{{ acls }}"
```

[With the above play, the user is replacing the 123 extended ACL with
the provided ACL ACEs configuration and also configuring the 150
extended new ACL ACEs.]{style="color: #333333;"}

[Before running the Overridden play network device
configuration:]{style="color: #333333;"}

``` 
cisco#sh access-lists
Standard IP access list std_acl
   10 deny   192.168.1.200
   20 deny   192.168.2.0, wildcard bits 0.0.0.255
Extended IP access list 110
   10 deny icmp 192.0.2.0 0.0.0.255 192.0.3.0 0.0.0.255 traceroute dscp ef ttl eq 10
   20 deny tcp host 198.51.100.0 host 198.51.110.0 eq telnet ack
Extended IP access list 123
   10 deny tcp 198.51.100.0 0.0.0.255 198.51.101.0 0.0.0.255 eq telnet ack tos 12
   20 deny tcp 192.0.3.0 0.0.0.255 192.0.4.0 0.0.0.255 eq www ack dscp ef ttl lt 20
Extended IP access list test
   10 deny tcp 192.0.2.0 0.0.0.255 192.0.3.0 0.0.0.255 eq www fin option traceroute ttl eq 10
IPv6 access list R1_TRAFFIC
   deny tcp any eq www any eq telnet ack dscp af11 sequence 10
```

With Overridden play run, commands that are sent:

``` 
- no ip access-list standard std_acl
- no ip access-list extended 110
- no ip access-list extended 123
- no ip access-list extended 150
- no ip access-list extended test
- no ipv6 access-list R1_TRAFFIC
- ip access-list extended 150
- 10 deny tcp 198.51.100.0 0.0.0.255 eq telnet 198.51.110.0 0.0.0.255 eq telnet syn dscp ef ttl eq 10
- ip access-list extended 110
- 20 deny tcp 198.51.100.0 0.0.0.255 eq telnet 198.51.110.0 0.0.0.255 eq www ack dscp ef ttl eq 10
```

After running the
[Overridden]{style="font-size: 13.5pt; color: #333333;"} play network
device configuration:

``` 
cisco#sh access-lists
Extended IP access list 110
   20 deny tcp 198.51.100.0 0.0.0.255 eq telnet 198.51.110.0 0.0.0.255 eq www ack dscp ef ttl eq 10
Extended IP access list 150
   10 deny tcp 198.51.100.0 0.0.0.255 eq telnet 198.51.110.0 0.0.0.255 eq telnet syn dscp ef ttl eq 10
```

Now, again if we dig the overridden play output:

-   Overridden negates all of the pre-existing ACLs and deletes those
    configurations, which are not present inside the provided config.
-   For the ACL configurations that are pre-existing and also in the
    play, ios_acls overridden state will try to delete/negate all the
    pre-existing ACEs and then configure the new ACE as mentioned in the
    play
-   For any non-existing ACLs, overridden state will configure the ACL
    in a manner same as merged

Now that we talked about how we can configure ACLs and the ACEs on the
CISCO IOS device by using ios_acls resource module merged, replaced and
overridden state, it's time we talk about how we can delete the
pre-configured ACLs and ACEs and what level of granularity is available
with the deleted operational state for the user.

## Deleting configuration changes

If the user wants to delete the Cisco IOS device pre-configured ACLs
with the provided ACL configuration, then use the resource module delete
state.

Method 1: Delete individual ACLs **based on ACL number** (which means if the user needs to delete any specific ACLs configured under IPV4 or IPV6)

Ref gist link: 

[https://gist.githubusercontent.com/justjais/bb2a65c373ab4e64d1eeb47bc425c613/raw/056d2a6a44910863cbbbf38cad2273435574db84/Deleted.txt](https://gist.githubusercontent.com/justjais/bb2a65c373ab4e64d1eeb47bc425c613/raw/056d2a6a44910863cbbbf38cad2273435574db84/Deleted.txt)

ACLs that need to be deleted

``` 
acls:
- afi: ipv4
  acls:
    - name: test
      acl_type: extended
    - name: 110
    - name: 123
- afi: ipv6
  acls:
    - name: R1_TRAFFIC
```

Ansible Playbook Example

``` 
---
- name: Deleted state play
  hosts: cisco
  gather_facts: false
  tasks:
    - name: Delete ACLs based on ACL number
      cisco.ios.ios_acls:
        state: deleted
        config: "{{ acls }}"
```

Before running the Deleted play network device configuration:

``` 
cisco#sh access-lists
Standard IP access list std_acl
   10 deny   192.168.1.200
   20 deny   192.168.2.0, wildcard bits 0.0.0.255
Extended IP access list 110
   10 deny icmp 192.0.2.0 0.0.0.255 192.0.3.0 0.0.0.255 traceroute dscp ef ttl eq 10
   20 deny tcp host 198.51.100.0 host 198.51.110.0 eq telnet ack
Extended IP access list 123
   10 deny tcp 198.51.100.0 0.0.0.255 198.51.101.0 0.0.0.255 eq telnet ack tos 12
   20 deny tcp 192.0.3.0 0.0.0.255 192.0.4.0 0.0.0.255 eq www ack dscp ef ttl lt 20
Extended IP access list test
   10 deny tcp 192.0.2.0 0.0.0.255 192.0.3.0 0.0.0.255 eq www fin option traceroute ttl eq 10
IPv6 access list R1_TRAFFIC
   deny tcp any eq www any eq telnet ack dscp af11 sequence 10
```

With Delete by ACLs Play run, commands that are sent:

``` 
- no ip access-list extended test
- no ip access-list extended 110
- no ip access-list extended 123
- no ipv6 access-list R1_TRAFFIC
```

After running the [Deleted]{style="font-size: 13.5pt; color: #333333;"}
play network device configuration:

``` 
cisco#sh access-lists
Standard IP access list std_acl
   10 deny   192.168.1.200
   20 deny   192.168.2.0, wildcard bits 0.0.0.255
cisco#
```

 

Method 2: Deleting individual ACLs **based on it's AFI (i.e. Address Family Indicator)** which means if the user needs to delete all of the ACLs configured under IPV4 or IPV6

[Ref gist link:
]{style="font-size: 11pt; color: #000000;"}[https://gist.githubusercontent.com/justjais/bb2a65c373ab4e64d1eeb47bc425c613/raw/8c65946eae561ff569cfc5398879c51598ae050c/Deleted_by_AFI](https://gist.githubusercontent.com/justjais/bb2a65c373ab4e64d1eeb47bc425c613/raw/8c65946eae561ff569cfc5398879c51598ae050c/Deleted_by_AFI){style="font-size: 11pt;"}

[Ansible Playbook Example]{style="font-size: 14pt; color: #434343;"}

``` 
---
- name: Deleted state play
  hosts: cisco
  gather_facts: false
  tasks:
    - name: Delete ALL IPV4 configured ACLs
      cisco.ios.ios_acls:
        config:
          - afi: ipv4
        state: deleted
```

Before running the Deleted play network device configuration:

``` 
cisco#sh access-lists
Standard IP access list std_acl
   10 deny   192.168.1.200
   20 deny   192.168.2.0, wildcard bits 0.0.0.255
Extended IP access list 110
   10 deny icmp 192.0.2.0 0.0.0.255 192.0.3.0 0.0.0.255 traceroute dscp ef ttl eq 10
   20 deny tcp host 198.51.100.0 host 198.51.110.0 eq telnet ack
Extended IP access list 123
   10 deny tcp 198.51.100.0 0.0.0.255 198.51.101.0 0.0.0.255 eq telnet ack tos 12
   20 deny tcp 192.0.3.0 0.0.0.255 192.0.4.0 0.0.0.255 eq www ack dscp ef ttl lt 20
Extended IP access list test
   10 deny tcp 192.0.2.0 0.0.0.255 192.0.3.0 0.0.0.255 eq www fin option traceroute ttl eq 10
IPv6 access list R1_TRAFFIC
   deny tcp any eq www any eq telnet ack dscp af11 sequence 10
```

With Delete by ACLs Play run, commands that are fired:

``` 
- no ip access-list standard std_acl
- no ip access-list extended test
- no ip access-list extended 110
- no ip access-list extended 123
- no ip access-list extended test
```

After running the [Deleted]{style="font-size: 13.5pt; color: #333333;"}
play network device configuration:

``` 
cisco#sh access-lists
IPv6 access list R1_TRAFFIC
   deny tcp any eq www any eq telnet ack dscp af11 sequence 10
cisco#
```

 

Method 3: Delete ALL ACLs at once

> Note: this is a very critical delete operation and if not used judiciously, it has the power of deleting all pre-configured ACLs

[[Ref gist link:]{style="font-size: 18px;"}
]{style="font-size: 11pt; color: #000000;"}[https://gist.githubusercontent.com/justjais/bb2a65c373ab4e64d1eeb47bc425c613/raw/056d2a6a44910863cbbbf38cad2273435574db84/Deleted_wo_config.txt](https://gist.githubusercontent.com/justjais/bb2a65c373ab4e64d1eeb47bc425c613/raw/056d2a6a44910863cbbbf38cad2273435574db84/Deleted_wo_config.txt){style="font-size: 11pt;"}

[Ansible Playbook Example]{style="font-size: 14pt; color: #434343;"}

``` 
---
- name: Deleted state play
  hosts: cisco
  gather_facts: false
  tasks:
    - name: Delete ALL configured ACLs w/o passing any config
      cisco.ios.ios_acls:
        state: deleted
```

Before running the Deleted play network device configuration:

``` 
cisco#sh access-lists
Standard IP access list std_acl
   10 deny   192.168.1.200
   20 deny   192.168.2.0, wildcard bits 0.0.0.255
Extended IP access list 110
   10 deny icmp 192.0.2.0 0.0.0.255 192.0.3.0 0.0.0.255 traceroute dscp ef ttl eq 10
   20 deny tcp host 198.51.100.0 host 198.51.110.0 eq telnet ack
Extended IP access list 123
   10 deny tcp 198.51.100.0 0.0.0.255 198.51.101.0 0.0.0.255 eq telnet ack tos 12
   20 deny tcp 192.0.3.0 0.0.0.255 192.0.4.0 0.0.0.255 eq www ack dscp ef ttl lt 20
Extended IP access list test
   10 deny tcp 192.0.2.0 0.0.0.255 192.0.3.0 0.0.0.255 eq www fin option traceroute ttl eq 10
IPv6 access list R1_TRAFFIC
   deny tcp any eq www any eq telnet ack dscp af11 sequence 10
```

With Delete by ACLs Play run, commands that are fired:

``` 
- no ip access-list standard std_acl
- no ip access-list extended test
- no ip access-list extended 110
- no ip access-list extended 123
- no ip access-list extended test
- no ipv6 access-list R1_TRAFFIC
```

After running the
[Overridden]{style="font-size: 13.5pt; color: #333333;"} play network
device configuration:

``` 
cisco#sh access-lists
cisco#
```

 

## Using state rendered - Development and working offline

[The state rendered transforms the provided structured data model into
platform specific CLI commands. This state does not require a connection
to the end device. For this example, it will render the provided data
model into the Cisco IOS syntax commands.]{style="color: #000000;"}

[Ref gist link:
]{style="color: #000000;"}[https://gist.githubusercontent.com/justjais/bb2a65c373ab4e64d1eeb47bc425c613/raw/8c65946eae561ff569cfc5398879c51598ae050c/Rendered.txt](https://gist.githubusercontent.com/justjais/bb2a65c373ab4e64d1eeb47bc425c613/raw/8c65946eae561ff569cfc5398879c51598ae050c/Rendered.txt)

[ACLs Config that needs to be rendered]{style="color: #000000;"}

``` 
acls:
- afi: ipv4
  acls:
   - name: 110
     aces:
       - grant: deny
         sequence: 10
         protocol_options:
           tcp:
             syn: true
         source:
           address: 192.0.2.0
           wildcard_bits: 0.0.0.255
         destination:
           address: 192.0.3.0
           wildcard_bits: 0.0.0.255
           port_protocol:
             eq: www
         dscp: ef
         ttl:
           eq: 10
   - name: 150
     aces:
       - grant: deny
         protocol_options:
           tcp:
             syn: true
         source:
           address: 198.51.100.0
           wildcard_bits: 0.0.0.255
           port_protocol:
             eq: telnet
         destination:
           address: 198.51.110.0
           wildcard_bits: 0.0.0.255
           port_protocol:
             eq: telnet
         dscp: ef
         ttl:
           eq: 10   
```

Ansible Playbook Example

``` 
---
- name: Rendered state play
  hosts: cisco
  gather_facts: false
  tasks:
    - name: Render the provided configuration
      cisco.ios.ios_acls:
        config: "{{ acls }}"
        state: rendered
```

With Render state module execution results:

``` 
"rendered": [
   "ip access-list extended 110",
   "10 deny tcp 192.0.2.0 0.0.0.255 192.0.3.0 0.0.0.255 eq www syn dscp ef ttl eq 10",
   "ip access-list extended 150",
   "deny tcp 198.51.100.0 0.0.0.255 eq telnet 198.51.110.0 0.0.0.255 eq telnet syn dscp ef ttl eq 10"
]
```

[NOTE:]{style="text-decoration: underline;"} Render state won't change
anything from configuration end

 

## Using state parsed - Development and working offline

This state reads the configuration from running_config option and
transforms it into structured data (i.e. JSON). This is helpful if you
have off-line configurations, such as a backup text file, and want to
transform it into structured data. This is helpful for experimenting,
troubleshooting or offline creation of a source of truth for your data
models.

Ref gist link:
[https://gist.githubusercontent.com/justjais/bb2a65c373ab4e64d1eeb47bc425c613/raw/8c65946eae561ff569cfc5398879c51598ae050c/Parsed.txt](https://gist.githubusercontent.com/justjais/bb2a65c373ab4e64d1eeb47bc425c613/raw/8c65946eae561ff569cfc5398879c51598ae050c/Parsed.txt)

ACLs Config that needs to be Parsed

[Ansible Playbook Example]{style="font-size: 14pt; color: #434343;"}

``` 
---
- name: Parsed state play
  hosts: cisco
  gather_facts: false
  tasks:
    - name: Parse the provided ACLs configuration
      cisco.ios.ios_acls:
        running_config:
           "ipv6 access-list R1_TRAFFIC
           deny tcp any eq www any eq telnet ack dscp af11"
        state: parsed
```

With Parsed state module execution results:

``` 
"parsed": [
       {
           "acls": [
               {
                   "aces": [
                       {
                           "destination": {
                               "any": true,
                               "port_protocol": {
                                   "eq": "telnet"
                               }
                           },
                           "dscp": "af11",
                           "grant": "deny",
                           "protocol_options": {
                               "tcp": {
                                   "ack": true
                               }
                           },
                           "source": {
                               "any": true,
                               "port_protocol": {
                                   "eq": "www"
                               }
                           }
                       }
                   ],
                   "name": "R1_TRAFFIC"
               }
           ],
           "afi": "ipv6"
       }
   ]
```

## Conclusion

The ACLs resource modules provide an easy way for network engineers to
begin automating access lists on multiple network platforms. While some
configuration can remain static on network devices, ACLs might need
constant updates and verification. These resource modules allow users to
adopt automation in incremental steps to make it easy for organizations
to adopt.  As soon as you have transformed your ACLs into structured
data, any resource module from any network platform can read. Imagine
reading in ACLs for your Cisco IOS box and transforming them into Cisco
IOS-XR commands. 
