---
author: Gonéri Le Bouder
date: 2020-09-29 00:00 UTC
description: The Ansible VMware modules as part of the current
  community.vmware Collection are extremely popular. According to
  GitHub, it\'s the second most forked Collection.
lang: en-us
title: Introducing the VMware REST Ansible Content Collection
---

# Introducing the VMware REST Ansible Content Collection

The VMware Ansible modules as part of the current [community.vmware Collection](https://galaxy.ansible.com/community/vmware)
are extremely popular. According to GitHub, it's the second most forked Collection, just after
[community.general](https://galaxy.ansible.com/community/general).
The VMware modules and plugins for Ansible have benefited from a stream
of contributions from dozens of users. Many IT infrastructure engineers
rely on managing their VMware infrastructure by means of a simple
Ansible Playbook. The vast majority of the current VMware modules are
built on top of a dependent python library called
[pyVmomi](https://github.com/vmware/pyvmomi),
also known as vSphere Automation SDK for Python.

## Why a new VMware Ansible Content Collection?

VMware has recently introduced the vSphere REST API for vSphere 6.0 and
later, which will likely replace the existing SOAP SDK used in the
[community.vmware](https://galaxy.ansible.com/community/vmware)
Collection.

Since the REST API's initial release, vSphere support for the REST API
has only improved. Furthermore, there is no longer a need for any
dependent python packages. In order to maintain the existing VMware
modules in the
[community.vmware](https://galaxy.ansible.com/community/vmware)
Collection, a set of modules specifically for interacting with the
VMware REST API is now available in the newly created
[vmware.vmware_rest](https://galaxy.ansible.com/vmware/vmware_rest)
Collection.

If you compare modules used with the VMware vSphere API (SOAP) to the
ones using the REST API, you'll notice the REST API modules are not yet
feature complete, as this is an early release of the Collection. For
example, there currently is no way to create a cluster or a folder using
the modules in the
[vmware.vmware_rest](https://galaxy.ansible.com/vmware/vmware_rest){rel="noopener"}
Collection, but the API provides all you need for a VMware guest for
future Collection enablement and much more.

## Using the VMware REST API

In order to understand how the new modules function against the new REST API, let's take a look at the REST API itself first.
For example, the `com.vmware.vcenter.vm.power` API endpoint changes the power state of a VM.
It's equivalent to the following sample URL:

```bash
https://vcenter.test/rest/vcenter/vm/\$vm/power
```

With the vCenter 7.0 release, 723 total REST endpoints are exposed,
which can be discovered using the following `curl` command:

```bash
$ curl -k https://vcenter.test/rest/com/vmware/vapi/metadata/cli/command|jq -r ".[][].path"|uniq|wc -l
723
```

The VMware REST APIs are documented in the Swagger 2.0 format. You can
find the JSON files on your vCenter node in the following directory
path:

```bash
root@vcenter [ /etc/vmware-vapi/apiexplorer/json ]# ls -lh
total 3.3M
-rw-r--r-- 1 vapiEndpoint users  145 Aug 31 15:37 api.json
-rw-r--r-- 1 vapiEndpoint users 396K Aug 31 15:36 appliance.json
-rw-r--r-- 1 vapiEndpoint users 153K Aug 31 15:36 cis.json
-rw-r--r-- 1 vapiEndpoint users 272K Aug 31 15:37 content.json
-rw-r--r-- 1 vapiEndpoint users 395K Aug 31 15:36 esx.json
-rw-r--r-- 1 vapiEndpoint users 153K Aug 31 15:36 stats.json
-rw-r--r-- 1 vapiEndpoint users 176K Aug 31 15:37 vapi.json
-rw-r--r-- 1 vapiEndpoint users 1.8M Aug 31 15:36 vcenter.json
```

To summarize, the
[vmware.vmware_rest](https://galaxy.ansible.com/vmware/vmware_rest)
Collection has all these REST endpoints ready to be consumed with the
descriptions in a well documented format.

## Building the vmware_rest Collection

The modules contained in this Collection are generated using a tool
called 
[vmware_rest_code_generator](https://github.com/ansible-collections/vmware_rest_code_generator),
which was developed and open sourced by the Ansible team. It loads the
Swagger files and then auto-generates a module per each resource,
generating more than 300 modules this way. You'll notice that not every
module has been released to the Collection. For purposes of starting
small, we are only generating modules against a subset of the endpoints
exposed, only those associated with guest management use cases. We may
expand and extend the number of modules over time.


## Using the vmware_rest Collection

The following tasks retrieve a list of the VM, shuts them down, and then deletes them:

```yaml
- name: Collect the list of the existing VM
  vcenter_vm_info:
  register: existing_vms
  until: existing_vms is not failed

- name: Turn off the VM
  vcenter_vm_power:
    state: stop
    vm: '{{ item.vm }}'
  with_items: "{{ existing_vms.value }}"
  ignore_errors: yes

- name: Delete some VM
  vcenter_vm:
    state: absent
    vm: '{{ item.vm }}'
  with_items: "{{ existing_vms.value }}"
```

Refer to the following gist file for more information:
[https://gist.github.com/goneri/6afd05397390cf5a0976f3611814949a](https://gist.github.com/goneri/6afd05397390cf5a0976f3611814949a)


## Downloading the vmware_rest Collection

The goal of this early release is to get as much community feedback as
possible.

The Collection is available on Ansible Galaxy, and requires the
following:

-   Ansible 2.9 or later 
-   Python 3.6 or later
-   The `aiohttp` package

Use the `ansible-galaxy` command to retrieve the Collection:

```bash
# ansible-galaxy collection install vmware.vmware_rest
```

If you use a virtualenv, you can install `aiohttp` with following command:

```bash
# pip install aiohttp
```

Else, you will need to download and install the `python3-aiohttp` package.

To read the module documentation, use the `ansible-doc` command.
For example, to read documentation for the `vcenter_cluster_info` module, refer to the following command:

```bash
# ansible-doc -t module vmware.vmware_rest.vcenter_cluster_info
```

## vCenter-Managed Object Reference ID

If you are already using the community.vmware Collection, the main
difference is that the newer modules rely on the MORef ID to identify
the elements instead of the name of the object. For example, if the user
creates a datacenter called dc1, the MORef ID using the new modules will
be datacenter-2. The community.vmware Collection uses the name and the
folder instead.

By using the MORef ID directly, the module is able to interact with the
resource without any time consuming preliminary look up.

## How can I contribute?

Because the modules are auto-generated, it GitHub pull requests should
be raised against the [code generator](https://github.com/ansible-collections/vmware_rest_code_generator)
itself, and not the resulting Collection contents.

Don't hesitate to report any issues on the GitHub project at
[https://github.com/ansible-collections/vmware_rest/issues](https://github.com/ansible-collections/vmware_rest/issues).


Reference:

The forks per collection can be found programmatically by accessing the Github API:
[https://api.github.com/orgs/ansible-collections/repos](https://api.github.com/orgs/ansible-collections/repos) 

This can be sorted, for example:

```bash
method: curl -s https://api.github.com/orgs/ansible-collections/repos|jq -r -c --sort-keys '.|sort_by(.forks)|reverse|.[]|[.name, .forks]'
```
