---
author: Sean Cavanaugh
date: 2019-02-06 00:00 UTC
description: This blog is a deep dive into Ansible 2.7\'s powerful
  agnostic network modules, cli_command and cli_config with the goal to
  simplify Ansible Playbooks for network engineers that deal with a
  variety of network platforms.
lang: en-us
title: Deep Dive on cli_command for Network Automation
---

# Deep Dive on cli_command for Network Automation

In October Ansible 2.7 was released and brought us two powerful agnostic
network modules,
[cli_command](https://docs.ansible.com/ansible/latest/modules/cli_command_module.html)
and
[cli_config](https://docs.ansible.com/ansible/latest/modules/cli_config_module.html).
Do you have two or more network vendors within your environment? The
goal of agnostic modules is to simplify Ansible Playbooks for network
engineers that deal with a variety of network platforms. Rather than
having to deal with platform specific modules (e.g. eos_config,
ios_config, junos_config), you can now use cli_command or cli_config to
reduce the amount of tasks and conditionals within a playbook, and make
the playbook easier to use. This post will demonstrate how to use these
modules and contrast them to platform specific modules. I'll show some
playbook examples and common use cases to help illustrate how you can
use these new platform agnostic modules.

Both the `cli_command` and `cli_config` only work with the
network_cli connection plugin.
The goal of network_cli is to make playbooks look, feel and operate on
network devices, the same way Ansible works on Linux hosts.

## What can you do with the cli_command?

The cli_command allows you to run arbitrary commands on network devices.
Let's show a simple example using the cli_command, on an Arista vEOS device.

```yaml
---
- name: RUN COMMAND AND PRINT TO TERMINAL WINDOW
  hosts: arista
  gather_facts: false

  tasks:

- name: RUN ARISTA COMMAND
  cli_command:
    command: show ip interface brief
  register: command_output

- name: PRINT TO TERMINAL WINDOW
  debug:
    msg: "{{command_output.stdout}}"
```

Previously this would require the eos_command module and would look
like this:

```yaml
---
- name: RUN COMMAND AND PRINT TO TERMINAL WINDOW
  hosts: arista
  gather_facts: false

  tasks:

- name: RUN ARISTA COMMAND
  eos_command:
    commands: show ip interface brief
  register: command_output

- name: PRINT TO TERMINAL WINDOW
  debug:
    msg: "{{command_output.stdout}}"
```

Both Ansible Playbooks are simple and will output identically. This is
what it would look like:

![screenshot](/images/posts/archive/Ansible-Agnostic--Network-Automation-Screen.png)

Now these two playbooks don't look much different yet, but when you add
multiple vendors the playbook complexity without these new agnostic
network modules can increase quickly. Previously if I had a mixed vendor
environment, I would see the playbook evolve a couple different ways.
Sometimes they would contain numerous conditionals (the when statement)
like this:

```yaml
- name: RUN ARISTA COMMAND
  eos_command:
    commands: show ip int br
  when: ansible_network_os == 'eos'

- name: RUN CISCO NXOS COMMAND
  nxos_command:
    commands: show ip int br
  when: ansible_network_os == 'nxos'

- name: RUN JUNOS COMMAND
  junos_command:
    commands: show interface terse
  when: ansible_network_os == 'junos'
```

Or somewhat better, network automation playbooks would evolve like this:

```yaml
- name: RUN JUNOS COMMAND
  include_tasks: “{{ansible_network_os}}”
```

This second method is much cleaner. The include_tasks calls an Ansible
Playbook named eos.yml, ios.yml, nxos.yml, etc and runs the
corresponding command or tasks that were needed. While this is much
better because you can separate Ansible Playbooks based on the network
platform, it is still not as succinct or easy as agnostic modules. The
underlying functionality is the same, but the Ansible Playbooks become
much simpler.

The reason I bring up this include_tasks method is that there is still
going to be a time and place, even with agnostic modules, to separate
out the playbook logic. For example the command shown above for Juniper
is different compared to Arista and Cisco (show ip interface brief
versus show interface terse).

With the cli_command let's look at how we can make this agnostic
playbook for Cisco, Juniper and Arista extremely simple:

```yaml
---
- name: RUN COMMAND AND PRINT TO TERMINAL WINDOW
  hosts: routers
  gather_facts: false

  tasks:
    - name: RUN SHOW COMMAND
      cli_command:
        command: "{{show_interfaces}}"
      register: command_output

    - name: PRINT TO TERMINAL WINDOW
      debug:
        msg: "{{command_output.stdout}}"
```

Three `*os_command` tasks are reduced to one task. The show_interfaces
variable is stored as a group variable on a per-platform basis. For a
full example look at this [GitHub repository](https://github.com/network-automation/agnostic_example).

## Backup example

Let's look at another use-case with the cli_command module. Backing up
network configurations is a common network operational task. Ansible
Network Automation modules have a backup parameter that helps network
engineers automate this mundane, yet critical, task. For example with
Arista EOS we can do this:

```yaml
---
- name: BACKUP NETWORK CONFIGURATIONS
  hosts: arista
  gather_facts: false

  tasks:

    - name: BACKUP CONFIG
      eos_config:
        backup: yes
```

The cli_command module does not have a backup parameter. Why? Because
the backup parameter can be quite inflexible and hard to manipulate. One
of the most common feature requests from Ansible users is for every
config module to be able to set the backup destination. Rather than
recreate an incredible amount of logic and code in each config module,
we can reuse an existing module. In this case we can leverage the
already widely used copy module!

```yaml
---
- name: RUN COMMAND AND PRINT TO TERMINAL WINDOW
  hosts: arista
  gather_facts: false

  tasks:

- name: RUN ARISTA COMMAND
  cli_command:
    command: show run
  register: backup

- name: PRINT TO TERMINAL WINDOW
  copy:
    content: "{{backup.stdout}}"
    dest: "{{inventory_hostname}}.backup"
```

This becomes easy to manipulate what command output we want to save. In
this case it is the running configuration, but now we can switch to
startup-config just as easily. It also gives the user the control to
pick the backup destination directory and file name. An example of an
agnostic playbook for backups for Arista EOS, Juniper Junos and Cisco
IOS can be found here:

https://github.com/network-automation/agnostic_example

There are a lot of incredible things we can do with the agnostic modules
that help make our Ansible Network Automation Playbooks much more
succinct and simple. The cli_comand and cli_config modules have been in
the Ansible project since October 2018. Consider upgrading if you have
not already. If you are already using the cli_command or cli_config
module, please share! I will be highlighting more examples using
agnostic modules in subsequent blog posts so stay tuned.
