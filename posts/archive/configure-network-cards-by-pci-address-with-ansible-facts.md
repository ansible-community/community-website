---
author: Till Maas
date: 2019-06-14 00:00 UTC
description: Learn advanced use of Ansible facts to configure Linux
  networking. Find out how to specify network devices by PCI address; no
  more hard-coding device names.
lang: en-us
title: Configure Network Cards by PCI Address with Ansible Facts
---

# Configure Network Cards by PCI Address with Ansible Facts

In this post, you will learn advanced applications of Ansible facts to
configure Linux networking. Instead of hard-coding device names, you
will find out how to specify network devices by PCI addresses. This
prepares your configuration to work on different Red Hat Enterprise
Linux releases with different network naming schemes.

## Red Hat Enterprise Linux System Roles

The [RHEL System Roles](https://access.redhat.com/articles/3050101)
provide a uniform configuration interface across multiple RHEL releases.
However, the names of network devices in modern Linux distributions can
often not be stable for various releases. In the past, the kernel named
the devices after their order of appearance. The first device got the
name `eth0`, the next `eth1`, and so on.

To make the device names more reliable, developers introduced
[other methods](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/networking_guide/ch-consistent_network_device_naming).
This interferes with creating a release-independent network
configuration based on interface names. An initial solution to this
problem is to address network cards by MAC address. But this will
require an up-to-date inventory with MAC addresses of all network cards.
Also, it requires updating the inventory after replacing broken
hardware. This results in extra work. To avoid this effort, it would be
great to be able to specify network cards by their PCI address. With a
uniform hardware setup (same model, same slot, same motherboard), the
PCI address should be stable. This is because it defines the PCI bus,
device and function.

## Ansible facts

Ansible facts already expose the PCI address for network cards as `pciid`.
The following playbook shows how to obtain the PCI address for the network card `enp0s31f6`:

```yaml
---
- hosts: localhost
  vars:
    nic: enp0s31f6
  tasks:
    - name: Show PCI address (pciid) for a network card
      debug:
        msg: "The PCI address for {{ nic }} is {{ ansible_facts[nic]['pciid'] }}."
```

When running the playbook, it shows that the PCI address in this case is `0000:00:1f.6`:

```bash
ansible-playbook show_pciid.yml
[...]

TASK [Show PCI address (pciid) for a network card] **************************
ok: [localhost] => {
    "msg": "The PCI address for enp0s31f6 is 0000:00:1f.6."
}

[...]
```

## Transforming the facts

Selecting a network card by PCI address is not always straightforward.
Ansible facts can't query devices by their attributes directly. Luckily,
there are [filters in Ansible](https://docs.ansible.com/ansible/latest/user_guide/playbooks_filters.html)
that make it possible to reorganize the facts. From them, the
[json_query](https://docs.ansible.com/ansible/latest/user_guide/playbooks_filters.html#json-query-filter)
filter allows users to reorganize and filter data using the JMESPath
query language for JSON. To be able to use it, you might need to install
the `python2-jmespath` or `python3-jmespath` package.
Ansible uses a dictionary with the device names as keys to organize the
network facts. But we need the key to be the PCI address. To do this, we
will use a JMESPath expression that extracts all values of the Ansible
facts dictionary (`@.*`)
and then selects only the values that contain a
`pciid` key (`[?pciid]`). Then we will
use the expression `{key: pciid, value: device}` to create a new
dictionary with an item named key for the PCI ID and one named value for
the interface name. This structure allows us to use the
[items2dict](https://docs.ansible.com/ansible/latest/user_guide/playbooks_filters.html#items2dict-filter)
filter (introduced in Ansible 2.7) to build the final dictionary.

## Example

The following playbook shows how to create the dictionary
`device_by_pci_address` this
way. It will contain a mapping from PCI address to device name:

```yaml
---
- hosts: localhost
  vars:
    pci_address: "0000:00:1f.6"
    device_by_pci_address: "{{
        ansible_facts | json_query('@.* | [?pciid].{key: pciid, value: device}') | items2dict
    }}"
```

The following tasks shows the structure of this dictionary and how to use it:

```yaml
tasks:
  - name: Show devices by PCI address
    debug:
      var: device_by_pci_address
  - name: "Show device with PCI address {{ pci_address }}"
    debug:
      msg: "The device {{ device_by_pci_address[pci_address] }} is at the
         PCI address {{ pci_address }}"
```

When running these tasks, Ansible outputs the following:

```bash
TASK [Show devices by PCI address] *****************************************
ok: [localhost] => {
    "device_by_pci_address": {
        "0000:00:1f.6": "enp0s31f6",
        "0000:3a:00.0": "wlp58s0",
        "6-1:1.0": "enp8s0u1"
    }
}

TASK [Show device with PCI address 0000:00:1f.6] ***************************
ok: [localhost] => {
    "msg": "The device enp0s31f6 is at the PCI address 0000:00:1f.6"
}
```

If you look carefully, you will notice one device has a different PCI address format (`6-1:1.0`).
This is actually a USB device. On virtual machines you might encounter other types of addresses.
Virtio devices have addresses like `virtio0`, `virtio1` and so on.
Using the device name in the configuration makes it still specific for certain releases.
With a small change it is also possible to look up MAC addresses:

```yaml
---
- hosts: localhost
  vars:
    pci_address: "0000:00:1f.6"
    macaddress_by_pci_address: "{{
        ansible_facts | json_query('@.* | [?pciid].{key: pciid, value: macaddress}') | items2dict
    }}"

[...]
```

Note that we changed `value: device` to `value: macaddress` here.

## Combining with the network role

To put this all together, here is an example about how to use these
variables with the [Network RHEL System Role](https://github.com/linux-system-roles/network):

```yaml
---
- hosts: localhost
  vars:
    pciid: "0000:00:1f.6"
    macaddress_by_pci_address: "{{
        ansible_facts | json_query('@.* | [?pciid].{key: pciid, value: macaddress}') | items2dict
    }}"
    network_connections:
      - name: internal_network
        mac: "{{ macaddress_by_pci_address[pciid] }}"
        type: ethernet
        state: up
        ip:
          address:
            - 192.0.2.73/31

  tasks:
    - name: Import network role
      import_role:
        name: rhel-system-roles.network
```

This will configure the connection profile internal_network. It limits
the profile to the device at the PCI address
`0000:00:1f.6` using the device's MAC address.

## Outlook

Since the on-disk configuration still uses the MAC address, changing a
network card will require to run the playbook again. To avoid this,
NetworkManager would need to allow specifying the PCI address in the
configuration directly. I filed an [RFE proposal](https://bugzilla.redhat.com/show_bug.cgi?id=1673321) for
NetworkManager to support this in the future. Depending on the installed
version of the Jinja2 templating engine, the
`dict()` constructor allows
to create the dictionary without
`items2dict`:

```yaml
vars:
  macaddress_by_pci_addresss: "{{
      dict(ansible_facts | json_query('@.* | [?pciid].[pciid, macaddress]'))
  }}"
```

This works on RHEL 8 and recent versions of Fedora now.
But, [RHEL 7 does not support it, yet](https://bugzilla.redhat.com/show_bug.cgi?id=1697237).

## Conclusion

In this post, we've learned about network interface naming in modern
versions of Linux. The ability to identify the PCI address for network
cards becomes useful in larger environments to maintain consistency.
Being able to transform facts in Ansible Automation allows for many
possibilities, including using facts to identify which device to
configure when used with RHEL System Roles or any other role for that
matter.

If you are interested in learning more about certified networking
modules approved by the Ansible community and Red Hat, check
out [nsible Automation Certified Content today! Or, you can learn
more about Ansible network automation solutions. 

