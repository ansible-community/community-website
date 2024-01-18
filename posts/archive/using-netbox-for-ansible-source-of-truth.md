---
author: Josh VanDeraa
date: 2020-12-08 00:00 UTC
description: The goal of this blog is to show some of the capabilities
  that make NetBox a terrific tool and will be using NetBox as your
  network Source of Truth for automation!
lang: en-us
title: Using NetBox for Ansible Source of Truth
---

# Using NetBox for Ansible Source of Truth

Here you will learn about NetBox at a high level, how it works to become
a Source of Truth (SoT), and look into the use of the Ansible Content
Collection, which is available on Ansible Galaxy. The goal is to show
some of the capabilities that make NetBox a terrific tool and why you
will want to use NetBox as your network Source of Truth for automation!

![Screen Shot 2020-12-08 at 9.27.19
AM](https://www.ansible.com/hs-fs/hubfs/Screen%20Shot%202020-12-08%20at%209.27.19%20AM.png?width=2034&name=Screen%20Shot%202020-12-08%20at%209.27.19%20AM.png){width="2034"
style="width: 2034px;"
srcset="https://www.ansible.com/hs-fs/hubfs/Screen%20Shot%202020-12-08%20at%209.27.19%20AM.png?width=1017&name=Screen%20Shot%202020-12-08%20at%209.27.19%20AM.png 1017w, https://www.ansible.com/hs-fs/hubfs/Screen%20Shot%202020-12-08%20at%209.27.19%20AM.png?width=2034&name=Screen%20Shot%202020-12-08%20at%209.27.19%20AM.png 2034w, https://www.ansible.com/hs-fs/hubfs/Screen%20Shot%202020-12-08%20at%209.27.19%20AM.png?width=3051&name=Screen%20Shot%202020-12-08%20at%209.27.19%20AM.png 3051w, https://www.ansible.com/hs-fs/hubfs/Screen%20Shot%202020-12-08%20at%209.27.19%20AM.png?width=4068&name=Screen%20Shot%202020-12-08%20at%209.27.19%20AM.png 4068w, https://www.ansible.com/hs-fs/hubfs/Screen%20Shot%202020-12-08%20at%209.27.19%20AM.png?width=5085&name=Screen%20Shot%202020-12-08%20at%209.27.19%20AM.png 5085w, https://www.ansible.com/hs-fs/hubfs/Screen%20Shot%202020-12-08%20at%209.27.19%20AM.png?width=6102&name=Screen%20Shot%202020-12-08%20at%209.27.19%20AM.png 6102w"
sizes="(max-width: 2034px) 100vw, 2034px"}

## Source of Truth

Why a Source of Truth? The Source of Truth is where you go to get the
intended state of the device. There does not need to be a single Source
of Truth, but you should have a single Source of Truth per data domain,
often referred to as the System of Record (SoR). For example, if you
have a database that maintains your physical sites that is used by teams
outside of the IT domain, that should be the Source of Truth on physical
sites. You can aggregate the data from the physical site Source of Truth
into other data sources for automation. Just be aware that when it comes
time to collect data, then it should come from that other tool.

The first step in creating a network automation framework is to identify
the Source of Truth for the data, which will be used in future
automations. Oftentimes for a traditional network, the device itself has
been considered the SoT. Reading the configuration off of the device
each time you need a configuration data point for automation is
inefficient, and presumes that the device configuration is as intended,
not simply left there in troubleshooting or otherwise inadvertently
left. When it comes to providing data to teams outside of the network
organization, exposing an API  can help to speed up gathering data
without having to check in with the device first.

## NetBox

For a Source of Truth, one popular open source choice is NetBox. From
the primary documentation site
[netbox.readthedocs.io](https://netbox.readthedocs.io/){rel="noopener"},
*"NetBox is an open source web application designed to help manage and
document computer networks".* NetBox is currently designed to help
manage your:

-   DCIM (Data Center Infrastructure Management)
-   IPAM (IP Address Management)
-   Data Circuits
-   Connections (Network, console, and power)
-   Equipment racks
-   Virtualization
-   Secrets

Since NetBox is an IPAM tool, there are misconceptions at times about
what NetBox is able to do. To be clear, NetBox is not:

-   Network monitoring
-   DNS server
-   RADIUS server
-   Configuration management
-   Facilities management

## Why NetBox?

NetBox is a tool that is built on many common Python based open source
tools, using Postgres for the backend database and Python Django for the
back-end API and front-end UI. The API is extremely friendly as it
supports CRUD (Create, Read, Update, Delete) operations and is fully
documented with Swagger documentation. The NetBox Collection helps with
several aspects of NetBox including an inventory plugin, lookup plugin,
and several modules for updating data in NetBox.

NetBox gives a modern UI from the point of view of a network
organization to help document IP addressing, while keeping the primary
emphasis on network devices, system infrastructure,  and virtual
machines. This makes it ideal to use as your Source of Truth for
automating.

NetBox itself does not do any scanning of network resources. It is
intended to have humans maintain the data as this is going to be the
Source of Truth. It represents what the environment should look like. 

## Ansible Content Collection for NetBox

You will find the Collection within the netbox-community GitHub
organization
([github.com/netbox-community/](https://github.com/netbox-community/){rel="noopener"}).
Here you find a [Docker container
image](https://github.com/netbox-community/netbox-docker), [device-type
library](https://github.com/netbox-community/devicetype-library),
[community generated NetBox
reports](https://github.com/netbox-community/reports), and [source code
for NetBox](https://github.com/netbox-community/netbox) itself.\
\
If you are unfamiliar with what an Ansible Content Collection is, please
watch this brief [YouTube video.](https://youtu.be/WOcqhk7TdYc)

The Galaxy link for the Collection is at
[galaxy.ansible.com/netbox/netbox](https://galaxy.ansible.com/netbox/netbox){rel="noopener"}. 

The NetBox Collection allows you to get started quickly in adding
information into a NetBox instance. The only requirements are  to supply
an API key and a URL to get started. With this Collection, a base
inventory, and a NetBox environment you are able to get a Source of
Truth populated very quickly. 

Let's walk through the base setup to get to a place where you are
starting to use the NetBox Inventory Plugin as your Ansible inventory.
First is the example group_vars/all.yml file that will have the list of
items to be used with the tasks.

*Example -*
[*group_vars/all.yml*](https://gist.github.com/jvanderaa/c11f42c5dd6247808ec3d1acd8604f02)

``` 
---
site_list:
  - name: “NYC”
    time_zone: America/New_York
    status: Active
  - name: “CHI”
    time_zone: America/Chicago
    status: Active
  - name: “RTP”
    time_zone: America/New_York
    status: Active
manufacturers:  # In alphabetical order
  - Arista
  - Cisco
  - Juniper
device_types:
  - model: “ASAv”
    manufacturer: “Cisco”
    slug: “asav”
    part_number: “asav”
    Full_depth: False
  - model: “CSR1000v”
    manufacturer: “Cisco”
    slug: “csr1000v”
    part_number: “csr1000v”
    Full_depth: False
  - model: “vEOS”
    manufacturer: “Arista”
    slug: “veos”
    part_number: “veos”
    Full_depth: False
  - model: “vSRX”
    manufacturer: “Juniper”
    slug: “vsrx”
    part_number: “vsrx”
    Full_depth: False
platforms:
  - name: “ASA”
    slug: “asa”
  - name: “EOS”
    slug: “eos”
  - name: “IOS”
    slug: “ios”
  - name: “JUNOS”
    slug: “junos”
```

The first step is to create a site. Since NetBox models physical gear,
you install equipment at a physical location. Whether that is in your
own facilities or inside of a cloud, this is a site. The module for this
is the
[netbox.netbox.netbox_site]{style="font-family: 'courier new', courier;"}
module. A task in the playbook may be:

[*Example - Sites
Task*](https://gist.github.com/jvanderaa/e926451a17284bb6c5ec8cd7daa0c73e)

``` 
    - name: "TASK 10: SETUP SITES"
      netbox.netbox.netbox_site:
        netbox_url: "{{ lookup('ENV', 'NETBOX_URL') }}"
        netbox_token: "{{ lookup('ENV', 'NETBOX_API_KEY') }}"
        data: "{{ item }}"
      loop: "{{ site_list }}"
```

The next two pieces are the base to add devices to NetBox. In order to
create a specific device, you also need to have the device type and
manufacturer in your NetBox instance. To do this there are specific
modules available to create them. Platforms will help to identify what
OS the device is. I recommend that you use what your automation platform
is using---something like IOS, NXOS, and EOS are good choices and should
match up to your ansible_network_os choices. These tasks look like the
following:

[*Example - Manufacturers, Device Types, and
Platforms*](https://gist.github.com/jvanderaa/de4a57f05d963f9291c3f3a4adbb0f45)

``` 
- name: "TASK 20: SETUP MANUFACTURERS"
      netbox.netbox.netbox_manufacturer:
        netbox_url: "{{ lookup('ENV', 'NETBOX_URL') }}"
        netbox_token: "{{ lookup('ENV', 'NETBOX_API_KEY') }}"
        data:
          name: "{{ manufacturer }}"
      loop: "{{ manufacturers }}"
      loop_control:
        loop_var: manufacturer

   - name: "TASK 30: SETUP DEVICE TYPES"
      netbox.netbox.netbox_device_type:
        netbox_url: "{{ lookup('ENV', 'NETBOX_URL') }}"
        netbox_token: "{{ lookup('ENV', 'NETBOX_API_KEY') }}"
        data:
          model: "{{ device_type.model }}"
          manufacturer: "{{ device_type.manufacturer }}"
          slug: "{{ device_type.slug }}"
          part_number: "{{ device_type.part_number }}"
          is_full_depth: "{{ device_type.full_depth }}"
      loop: "{{ device_types }}"
      loop_control:
        loop_var: device_type
        label: "{{ device_type['model'] }}"

    - name: "TASK 40: SETUP PLATFORMS"
      netbox.netbox.netbox_platform:
        netbox_url: "{{ lookup('ENV', 'NETBOX_URL') }}"
        netbox_token: "{{ lookup('ENV', 'NETBOX_API_KEY') }}"
        data:
          name: "{{ platform.name }}"
          slug: "{{ platform.slug }}"
      loop: "{{ platforms }}"
      loop_control:
        loop_var: platform
        label: "{{ platform['name'] }}"
```

At this stage you are set to add devices and device information to
NetBox. The following tasks leverage the ansible_facts that Ansible
automatically gathers. So for these particular device types, no
additional parsing/data gathering is required outside of using Ansible
to gather facts. In this example for adding a device, you will notice
*custom_fields*. A nice extension of NetBox is that if there is not a
field already defined, you can set your own fields and use them within
the tool.

[Example - Add Devices &
Interfaces](https://gist.github.com/jvanderaa/b5881c5fa778b0601f494d3b73259c23){style="font-style: normal;"}

``` 
- name: "TASK 100: NETBOX >> ADD DEVICE TO NETBOX"
      netbox.netbox.netbox_device:
        netbox_url: "{{ lookup('ENV', 'NETBOX_URL') }}"
        netbox_token: "{{ lookup('ENV', 'NETBOX_API_KEY') }}"
        data:
          name: "{{ inventory_hostname }}"
          device_type: "{{ ansible_facts['net_model'] }}"
          platform: IOS  # May be able to use a filter to define in future
          serial: "{{ ansible_facts['net_serialnum'] }}"
          status: Active
          device_role: "{{ inventory_hostname | get_role_from_hostname }}"
          site: “ANSIBLE_DEMO_SITE"
          custom_fields:
            code_version: "{{ ansible_facts['net_version'] }}"

    - name: "TASK 110: NETBOX >> ADD INTERFACES TO NETBOX"
      netbox.netbox.netbox_device_interface:
        netbox_url: "{{ lookup('ENV', 'NETBOX_URL') }}"
        netbox_token: "{{ lookup('ENV', 'NETBOX_API_KEY') }}"
        data:
          device: "{{ inventory_hostname }}"
          name: "{{ item.key }}"
          form_factor: "{{ item.key | get_interface_type }}"  # Define types
          mac_address: "{{ item.value.macaddress | ansible.netcommon.hwaddr }}"
        state: present
      with_dict:
        - "{{ ansible_facts['net_interfaces'] }}"
```

Once you have the interfaces you can add in IP address information that
is included in the ansible_facts data, I show three steps. First is to
add a temporary interface (TASK 200), then add the IP address (TASK
210), and finally associate the IP address to the device (TASK 220).

[*Example - Add temp interface, add IP address, re-add device with the
IP address
associated*](https://gist.github.com/jvanderaa/5d890fc7906390e1dfdc01d297336965)

``` 
- name: "TASK 200: NETBOX >> Add temporary interface"
      netbox.netbox.netbox_device_interface:
        netbox_url: "{{ lookup('ENV', 'NETBOX_URL') }}"
        netbox_token: "{{ lookup('ENV', 'NETBOX_API_KEY') }}"
        data:
          device: "{{ inventory_hostname }}"
          name: Temporary_Interface
          form_factor: Virtual
        state: present

    - name: "TASK 210: NETBOX >> ADD IP ADDRESS OF ANSIBLE HOST"
      netbox.netbox.netbox_ip_address:
        netbox_url: "{{ lookup('ENV', 'NETBOX_URL') }}"
        netbox_token: "{{ lookup('ENV', 'NETBOX_API_KEY') }}"
        data:
          family: 4
          address: "{{ ansible_host }}/24"
          status: active
          interface:
            name: Temporary_Interface
            device: "{{ inventory_hostname }}"

    - name: "TASK 220: NETBOX >> ASSOCIATE IP ADDRESS TO DEVICE"
      netbox.netbox.netbox_device:
        netbox_url: "{{ lookup('ENV', 'NETBOX_URL') }}"
        netbox_token: "{{ lookup('ENV', 'NETBOX_API_KEY') }}"
        data:
          name: "{{ inventory_hostname }}"
          device_type: "{{ ansible_facts['net_model'] }}"
          platform: IOS
          serial: "{{ ansible_facts['net_serialnum'] }}"
          status: Active
          primary_ip4: "{{ ansible_host }}/24"
```

## Ansible Inventory Source

At this point you have NetBox populated with all of your devices that
were in your static inventory. It is now time to make the move to using
NetBox as the Source of Truth for your Ansible dynamic inventory plugin.
This way you don't have to keep finding all of the projects that need to
get updated when you make a change to the environment. You just need to
change your Source of Truth database - NetBox.

You define which inventory plugin to use with a YAML file that defines
the characteristics of how to configure your intended use of the plugin.
Below is an example, showing you are able to query many components of
NetBox for use within your Ansible inventory. You may wish to only make
an update to your access switches? Use the query_filters key to define
what NetBox API searches should be executed. Take a look at the plugin
documentation for updated supported parameters on
[GitHub](https://github.com/netbox-community/ansible_modules) or
[ReadTheDocs](https://netbox-ansible-collection.readthedocs.io/en/latest/).
The compose key allows you to pass in additional variables to be used by
Ansible, as such the platform from above would be used with the
ansible_network_os key. This is where you see the definition and what
would get passed from the inventory source.

This definition also has groups created based on the device_roles that
are defined in NetBox and the platforms. So you would be able to access
all platforms_ios devices or platforms_eos as an example, based on the
information in the Source of Truth.

[*Example -
netbox_inventory.yml*](https://gist.github.com/jvanderaa/6bc8f36e2ca1e45e4a4e5e61be4de435)

``` 
---
plugin: netbox.netbox.nb_inventory
api_endpoint: http://netbox03
validate_certs: false
config_context: false
group_by:
 - device_roles
 - platforms
compose:
 ansible_network_os: platform.slug
query_filters:
 - site: "minnesota01"
 - has_primary_ip: True
```

## Extending NetBox with Plugins

One of the more recent feature additions to NetBox itself is the ability
to extend it via your own or community driven plugins. From the wiki:
"Plugins are packaged Django apps that can be installed alongside NetBox
to provide custom functionality not present in the core application"
([GitHub
Link](https://github.com/netbox-community/netbox/wiki/Plugins)). You can
find some of the featured plugins in the community at that link. Some
include:

-   [Dynamic DNS Connector](https://github.com/sjm-steffann/netbox-ddns)
-   [NetBox Onboarding Plugin (from Network to Code) - This will read
    additional information about the device and make updates to
    NetBox](https://github.com/networktocode/ntc-netbox-plugin-onboarding){rel="noopener"}
-   [NetBox QR Code - Generate QR Codes about the
    device](https://github.com/k01ek/netbox-qrcode)
-   [SSO using
    SAML2](https://github.com/jeremyschulman/netbox-plugin-auth-saml2)

There are many plugins available to the community for you to choose
from---or you can write your own add ons! [Search on
GitHub](https://github.com/topics/netbox-plugi) for the topic *NetBox
Plugin.*


## Summary

NetBox and Ansible together are a great combination for your network
automation needs!

NetBox is an excellent open source tool that helps make it easy to
create, update, and consume as a Source of Truth. The APIs are easy to
use and make updates to the DB with, even if you did not want to use the
NetBox Collection available for Ansible. Having a tool that is flexible,
capable, and accurate is a must for delivering automation via a Source
of Truth. NetBox delivers on each of these. 

This post was inspired by a presentation done in March 2020 at the
Minneapolis Ansible Meetup. For additional material on this, I have many
of these tasks available as a working example on
[GitHub](https://github.com/jvanderaa/ansible_netbox_demo). The YouTube
recording of the presentation from the [Ansible Meetup is
available](https://www.youtube.com/watch?v=GyQf5F0gr3w).  
