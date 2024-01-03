---
author: Gonéri Le Bouder
date: 2021-08-03 00:00 UTC
description: How you can use the modules available in Red Hat supported
  vmware.vmware_rest Ansible Content Collection to audit your vCenter
  Servers.
lang: en-us
title: Audit your VMware vCenter Server using Ansible
---


# Audit your VMware vCenter Server using Ansible

vCenter has a graphical user interface if you want to interact with it,
but what if you manage multiple vCenter servers and want to automate
audits or the maintenance of those servers? In this blog, we will see
how we can retrieve details about the VMware vCenter Server directly
using Ansible. The practices laid out in the blog will help system
administrators responsible for managing multiple vCenter servers. In
addition, Ansible automation becomes imperative in development
environments for testing against multiple instances in your CI/CD
pipeline.

The new
[vmware.vmware_rest](https://cloud.redhat.com/ansible/automation-hub/repo/published/vmware/vmware_rest)
Collection has recently been released and published, and it comes with a
new set of modules dedicated to vCenter Server (VCSA) management.

VMware vSphere (Product bundle that includes vCenter Server and other
features) 7.0.2 (a.k.a 7.0U2) comes with some new REST end-points. This
REST API does not cover all the features exposed over the SOAP
interface. Modules in the vmware.vmware_rest Collection are built on top
of this API and face the same limitations.

The vmware.vmware_rest Collection contains these modules, which is
supported by Red Hat and available on
[Ansible automation hub](https://cloud.redhat.com/ansible/automation-hub/repo/published/vmware/vmware_rest).

## Validate the state of a vCenter Server instance from Ansible

Taking our own dogfooding example (or drinking our own champagne!), our
cloud/infrastructure team maintains a CI to validate the VMware Ansible
modules. Everytime a new change is submitted, the full test suite is run
against a freshly deployed VMware lab. The initial deployment takes 15
minutes and so we cannot spawn a new environment before each of the
dozen of tests are run. Hence, it becomes important to keep our test
environments as clean as possible.

We use these new appliance modules to build an audit report of the
vCenter instance before and at the end of the test suite run. This way,
it will be easier to spot any inconsistency between test runs.

The appliance modules cover the following use cases.

-   Access → localaccounts, audit and control the Console, Direct
    Console UI, the Shell or even SSH.
-   Health → retrieve information about the state of the system
    component.
-   Networking → collect information about the network configuration and
    adjust it.
-   System → manage services, reboot the system, get the storage
    configuration, get the state of the updates, etc.
-   Time management → configure the NTP server, adjust the timezone.

## How to start using these modules

The latest release of vmware_rest Collection available on
[Ansible automation hub](https://cloud.redhat.com/ansible/automation-hub/repo/published/vmware/vmware_rest)
supports vSphere 7.0.2 and greater.

We can pass the authentication keys either through some environment
variables or with the module parameters. In the following example, we
use the first option. For example:

```
VMWARE_HOST=<vsphere_host>
VMWARE_PASSWORD=<vsphere_password>
VMWARE_USER=<vsphere_username>
```

Note: The community.vmware Collection uses the same environment
variables.

We will try to explain some sample use cases below for the readers to
understand how you can start using these modules.

## Collect information about a VCSA instance

In this first example, we secure the appliance by turning off any
potential user interfaces. The REST interface that the modules use
remains available. Here's how you can check that using the modules
available.

```
- name: Shell access should be disabled
  vmware.vmware_rest.appliance_access_shell_info:
- name: The Direct Console User Interface should also be disabled
  vmware.vmware_rest.appliance_access_dcui_info:
- name: We need the SSH access
  vmware.vmware_rest.appliance_access_ssh_info:
```

Response:

```
{
    "changed": false,
    "value": {
        "enabled": false,
        "timeout": 0
    }
}

{
    "changed": false,
    "value": false
}

{
    "changed": false,
    "value": true
}
```

## The health states

We can rely either on the appliance_health modules or the other info
modules to audit the state of your VCSA. For instance, here we check
that the system load and the database are in a *green* state.

```
- name: Ensure the database health status is green
  vmware.vmware_rest.appliance_health_database_info:


- name: Get the system load status
  vmware.vmware_rest.appliance_health_load_info:


- name: Get the system load status
  vmware.vmware_rest.appliance_health_system_info:
```

Response:

```
{
    "changed": false,
    "value": {
        "messages": [
            {
                "message": {
                    "args": [],
                    "default_message": "DB state is Degraded",
                    "id": "desc"
                },
                "severity": "WARNING"
            }
        ],
        "status": "DEGRADED"
    }
}

{
    "changed": false,
    "value": "gray"
}

{
    "changed": false,
    "value": "gray"
}
```

In this example, our database is in a degraded state and the rest of the
system is not in the optimal GREEN state.

## Network configuration

Ansible is also able to read and set the network configuration of the
VCSA. The appliance_networking_info modules return a system-wide
overview of the network configuration:

```
- name: Get network information
  vmware.vmware_rest.appliance_networking_info:
```

Response: 

```
{
    "changed": false,
    "value": {
        "dns": {
            "hostname": "vcenter.test",
            "mode": "DHCP",
            "servers": [
                "192.168.123.1"
            ]
        },
        "interfaces": {
            "nic0": {
                "ipv4": {
                    "address": "192.168.123.8",
                    "configurable": true,
                    "default_gateway": "192.168.123.1",
                    "mode": "DHCP",
                    "prefix": 24
                },
                "mac": "52:54:00:c9:06:64",
                "name": "nic0",
                "status": "up"
            }
        },
        "vcenter_base_url": "https://vcenter.test:443"
    }
}
```

But we can also collect the details one specific NIC:

```
- name: Get details about one network interfaces
  vmware.vmware_rest.appliance_networking_interfaces_info:
    interface_name: nic0
```

Response:

```
{
    "changed": false,
    "id": "nic0",
    "value": {
        "ipv4": {
            "address": "192.168.123.8",
            "configurable": true,
            "default_gateway": "192.168.123.1",
            "mode": "DHCP",
            "prefix": 24
        },
        "mac": "52:54:00:c9:06:64",
        "name": "nic0",
        "status": "up"
    }
}
```

## DNS configuration

The appliance_networking_dns_hostname_info module can be use to retrieve
the hostname of the VCSA.

```
- name: Get the hostname configuration
  vmware.vmware_rest.appliance_networking_dns_hostname_info:
```

Response:

```
{
    "changed": false,
    "value": "vcenter.test"
}
```

Use the appliance_networking_dns_servers_info to get DNS servers
currently in use:

```
- name: Get the DNS servers
  vmware.vmware_rest.appliance_networking_dns_servers_info:
```

Response:

```
{
    "changed": false,
    "value": {
        "mode": "dhcp",
        "servers": [
            "192.168.123.1"
        ]
    }
}
```

## Conclusion and next steps

These new modules are helpful to quickly retrieve information from a
running VCSA instance without relying on SSH. The outputs will fit well
in a regular Ansible Playbook. Finally, you can also use them to adjust
the configuration of the system (network, firewall, etc). An unsupported
version of this Collection is also available on [Ansible Galaxy](https://galaxy.ansible.com/vmware/vmware_rest).
