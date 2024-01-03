---
author: Ganesh Nalawade
date: 2020-11-24 00:00 UTC
description: We are introducing FIPS 140-2 readiness enablement by means
  of a newly developed Ansible SSH connection plugin that now utilizes
  the underlying LibSSH package in RHEL 8.
lang: en-us
title: New LibSSH Connection Plugin for Ansible Network Replaces Paramiko, Adds FIPS Mode Enablement
---

# New LibSSH Connection Plugin for Ansible Network Replaces Paramiko, Adds FIPS Mode Enablement

As Red Hat Ansible Automation Platform expands its footprint with a
growing customer base, security continues to be an important aspect of
organizations' overall strategy. Red Hat regularly reviews and enhances
the foundational codebase to follow better security practices. As part
of this effort, we are introducing [FIPS 140-2
readiness](https://www.sdxcentral.com/security/definitions/what-does-mean-fips-compliant/)
enablement by means of a newly developed Ansible SSH connection plugin
that uses the [libssh](https://www.libssh.org/) library.

## Ansible Network SSH Connection Basics

Since most network appliances don\'t support or have limited capability
for the local execution of a third party software, the Ansible network
modules are not copied to the remote host unlike linux hosts; instead,
they run on the control node itself. Hence, Ansible network can't use
the typical Ansible SSH connection plugin that is used with linux host.
Furthermore, due to this behavior, performance of the underlying SSH
subsystem is critical. Not only is the new LibSSH connection plugin
enabling FIPS readiness, but it was also designed to be [more performant
than the existing Paramiko SSH
subsystem](https://elegantnetwork.github.io/posts/comparing-ssh/).

![Screen Shot 2020-11-20 at 8.52.53
AM](https://www.ansible.com/hs-fs/hubfs/Screen%20Shot%202020-11-20%20at%208.52.53%20AM.png?width=687&name=Screen%20Shot%202020-11-20%20at%208.52.53%20AM.png){width="687"
style="width: 687px;"
srcset="https://www.ansible.com/hs-fs/hubfs/Screen%20Shot%202020-11-20%20at%208.52.53%20AM.png?width=344&name=Screen%20Shot%202020-11-20%20at%208.52.53%20AM.png 344w, https://www.ansible.com/hs-fs/hubfs/Screen%20Shot%202020-11-20%20at%208.52.53%20AM.png?width=687&name=Screen%20Shot%202020-11-20%20at%208.52.53%20AM.png 687w, https://www.ansible.com/hs-fs/hubfs/Screen%20Shot%202020-11-20%20at%208.52.53%20AM.png?width=1031&name=Screen%20Shot%202020-11-20%20at%208.52.53%20AM.png 1031w, https://www.ansible.com/hs-fs/hubfs/Screen%20Shot%202020-11-20%20at%208.52.53%20AM.png?width=1374&name=Screen%20Shot%202020-11-20%20at%208.52.53%20AM.png 1374w, https://www.ansible.com/hs-fs/hubfs/Screen%20Shot%202020-11-20%20at%208.52.53%20AM.png?width=1718&name=Screen%20Shot%202020-11-20%20at%208.52.53%20AM.png 1718w, https://www.ansible.com/hs-fs/hubfs/Screen%20Shot%202020-11-20%20at%208.52.53%20AM.png?width=2061&name=Screen%20Shot%202020-11-20%20at%208.52.53%20AM.png 2061w"
sizes="(max-width: 687px) 100vw, 687px"}

The top level
[network_cli]{style="font-family: 'courier new', courier;"} connection
plugin, provided by the ansible.netcommon Collection (specifically
ansible.netcommon.network_cli), provides an SSH based connection to the
network appliance. It in turn calls the ansible.builtin.paramiko_ssh
connection plugin that depends on the paramiko python library to
initialize the session between control node and the remote host. After
that, it creates a pseudo terminal (PTY) to send commands from the
control node to the network appliance and receive the responses.

## Why Replace Paramiko?

The primary reason to replace the paramiko library is that it doesn't
guarantee FIPS readiness and thus limits the Ansible network capability
to run in environments that mandate FIPS mode to be enabled. Paramiko
also isn't the speediest of connection plugins, so that can also be
enhanced. Therefore, the new ansible.netcommon.libssh connection plugin
can now be easily swapped in for paramiko. The ansible.netcommon
Collection now contains this by default, and can be used for testing
purposes until the codebase becomes more stable (it is currently
[Technology Preview](https://access.redhat.com/solutions/21101)).

Comparing the connection flow to the above, the top level
[network_cli]{style="font-family: 'courier new', courier;"} connection
plugin that is provided by the ansible.netcommon Collection
(specifically ansible.netcommon.network_cli) still provides an SSH based
connection to the network appliance. It in turn calls the
ansible.netcommon.libssh connection plugin that depends on the
[ansible-pylibssh
[python]{style="color: #1155cc; text-decoration: underline;"}
[library]{style="color: #1155cc; text-decoration: underline;"}](https://pypi.org/project/ansible-pylibssh/)
to initialize the session between control node and the remote host. This
python library is essentially a cython wrapper on top of the [libssh C
library](https://www.libssh.org/). It then creates pseudo terminals
(PTY) over SSH using python.

## Switching Ansible Playbooks to use LibSSH

With the ansible.netcommon Collection version 1.0.0, a new configuration
parameter within ansible.netcommon.network_cli connection plugin was
added, which allows for
[ssh_type]{style="font-family: 'courier new', courier;"} be set to
either libssh or paramiko. 

If the value of the configuration parameter is set to
[libssh]{style="font-family: 'courier new', courier;"}, it will use the
ansible.netcommon.libssh connection plugin, which in turn uses the
ansible-pylibssh python library that supports FIPS readiness. If the
value is set to paramiko, it will continue to use the default
ansible.builtin.paramiko connection plugin that relies on the
[paramiko]{style="font-family: 'courier new', courier;"} python
library. 

Again, the default value is set to paramiko, but in the future plans are
to change the default to libssh.

## Installing and Configuring LibSSH

In order to utilize the LibSSH plugin, you must first install the
ansible-pylibssh python library from PyPI via the following command:

``` 
pip install ansible-pylibssh
```

NOTES:

-   The current PyPI installation method bundles the correct version of
    LibSSH library and its dependencies as [platform-specific
    wheels](https://packaging.python.org/glossary/#term-Built-Distribution)
    that don't rely on any OS-level libraries in runtime.
-   Future plans include creation, publishing, and maintenance of
    stand-alone RPM and DEB packages for the ansible-pylibssh library
    that can be installed with well-known Linux package managers. These
    will install the required system libssh version and its dependencies
    on the control node. FYI, Red Hat Enterprise Linux 8.1 and later
    contains the proper libssh package version and its dependencies.
-   The current primary use case for using LibSSH with Ansible is for
    connecting to network devices. Connecting to other types of
    endpoints (such as Linux) will be officially enabled at a later
    date.

## Using LibSSH in Ansible Playbooks

Method 1:  The [ssh_type]{style="font-family: 'courier new', courier;"}
configuration parameter can be set to use
[libssh]{style="font-family: 'courier new', courier;"} in the active
[ansible.cfg]{style="font-family: 'courier new', courier;"} file of your
project as shown below:

``` 
[persistent_connection]
ssh_type = libssh
```

Method 2:  Set the ANSIBLE_NETWORK_CLI_SSH_TYPE environment variable as
shown below:

``` 
$export ANSIBLE_NETWORK_CLI_SSH_TYPE=libssh
```

Method 3:  Set the
[ansible_network_cli_ssh_type]{style="font-family: 'courier new', courier;"}
parameter to [libssh]{style="font-family: 'courier new', courier;"}
within your playbook at the play level (as shown in below example).

NOTE: This setting can be made at the individual task level, but only if
the connection to the remote network device is not already established.
That is, if the first task uses paramiko, then all subsequent tasks in
the play must use paramiko even if libssh is specified in any subsequent
tasks.

## Troubleshooting LibSSH Connections

To quickly verify the libssh transport is set correctly, you can run the
below playbook using the
[ansible-playbook]{style="font-family: 'courier new', courier;"} command
line with verbose flag (-vvvv) added. Before running, ensure the
inventory file is set correctly.

This example playbook uses the cisco.ios Collection and must first be
installed from Ansible Galaxy or Ansible Automation Platform on your
Ansible control node.

``` 
- hosts: "changeme"
  gather_facts: no
  connection: ansible.netcommon.network_cli
  vars:
    ansible_network_os: cisco.ios.ios
    ansible_user: "changeme"
    ansible_password: "changeme"
    ansible_network_cli_ssh_type: libssh
  tasks:
  - name: run show version command
    ansible.netcommon.cli_command:
      command: show version

  - name: run show interface command
    ansible.netcommon.cli_command:
       command: show interfaces
```

[https://gist.github.com/ganeshrn/78149adca85c809b69ed1b5f5262844c](https://gist.github.com/ganeshrn/78149adca85c809b69ed1b5f5262844c)

In the output verbose logs, you should see the line *"ssh type is set to
libssh"* displayed on the console, which confirms the configuration is
set correctly.

## Next Steps and Resources

-   Start testing your Ansible network playbooks by setting the
    configuration to use the ansible-pylibssh library.
-   Help with performance profiling of your existing playbook of 
    ansible-pylibssh library with respect to paramiko library.
-   Get involved with the ansible-pylibssh project
    ([https://github.com/ansible/pylibssh](https://github.com/ansible/pylibssh))
