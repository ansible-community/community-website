---
author: Paul Broadwith
date: 2020-08-26 00:00 UTC
description: Using Red Hat Ansible Automation Platform and Chocolatey,
  you can easily keep your software up-to-date and react quickly to bug
  fixes, security issues and 0-days on dozens, hundreds or thousands of
  nodes
lang: en-us
title: Ansible Certified Content Collection for Chocolatey
---

# Ansible Certified Content Collection for Chocolatey

It's a constant battle to keep your Windows estate updated and secure.
Using Red Hat Ansible Automation Platform and Chocolatey, you can easily
keep your software up-to-date and react quickly to bug fixes, security
issues and 0-days on dozens, hundreds or thousands of nodes.

We're going to take you through three simple steps to show you how
simple it is to deploy and update software using Chocolatey and Ansible.

 
## Before We Start: Windows Prerequisites

Ansible  uses Winrm by default to communicate with Windows machines.
Therefore, we need to ensure we have that enabled by running
`Enable-PSRemoting` on the remote Windows computer.

For production use, we recommend enabling
[HTTPS for WinRM](https://support.microsoft.com/en-gb/help/2019527/how-to-configure-winrm-for-https). 

The code examples shown below are all using the user 'ansible' as the
default. If you are using a different username, make sure you change it!

**Step 1: Configure Ansible to use Chocolatey.**

We need to install the Chocolatey module so that Ansible can use. The 
Chocolatey Ansible Content Collection is called
[chocolatey:chocolatey](https://galaxy.ansible.com/chocolatey/chocolatey)
and is maintained by the
[Chocolatey](https://github.com/chocolatey/chocolatey-ansible)
Team. To install the Collection, and therefore the win_chocolatey
modules, on your Ansible server, run:

```
ansible-galaxy collection install chocolatey.chocolatey
```

That's all there is to it! Ansible can now work with Chocolatey using
the modules in the Collection.

**Step 2: Install software on a remote computer**

Now that we have the win_chocolatey module installed, we can go ahead
and install or manage software on our remote computers.

Let's create a file called `install_notepadplusplus.yml` with the
following contents:

```yml
---
- hosts: all
  gather_facts: false

  vars_prompt:
    - name: password
      prompt: "Enter the password for the node"

  vars:
      ansible_user: ansible
      ansible_password: "{{ password }}"
      ansible_connection: winrm
      ansible_winrm_transport: ntlm
      ansible_winrm_server_cert_validation: ignore

  tasks:
      - name: Install Notepad++ version 7.8
        win_chocolatey:
          name: notepadplusplus
          version: ‘7.8’
```

Run `ansible-playbook install_notepadplusplus.yaml -i <ip address>,`
(note the comma after the IP address) to install Notepad++ on your
remote computer. Note that we are not installing the latest version in
this example as we will update to that in the next step.

Once installed, open Notepad++ and press `F1` to ensure we have
installed the requested version. 

**Step 3: Update software on a remote computer**

To ensure you always have the latest version of software installed on
your computers, you can use Chocolatey to upgrade them. We'll upgrade to
the latest version of Notepad++.

Create a file called `upgrade_notepadplusplus.yml` with the following
contents:

```yml
---
- hosts: all
  gather_facts: false

  vars_prompt:
    - name: password
      prompt: "Enter the password for the node"

  vars:
    ansible_user: ansible
    ansible_password: "{{ password }}"
    ansible_connection: winrm
    ansible_winrm_transport: ntlm
    ansible_winrm_server_cert_validation: ignore

  tasks:
    - name: Install latest Notepad++
      win_chocolatey:
        name: notepadplusplus
        state: latest
```

Run `ansible-playbook upgrade_notepadplusplus.yaml -i <ip address>,`
(note the comma after the IP address) to update, or install, the latest
Notepad++ on your remote computer. Once installed, open Notepad++ and
press `F1` to ensure we have installed the latest version. 

## Next Steps

While we have only worked with one remote computer in this blog post,
Ansible allows you to replicate this across dozens, hundreds and
thousands of remote computers.

Now that you have the Ansible Chocolatey modules installed, you can
install, uninstall, update and manage packages on your computers. Other
modules in the Chocolatey Ansible  Content Collection give you the
ability to manage the configuration, features and sources for Chocolatey
itself. You can find more information on the
[Ansible Galaxy Chocolatey collection page](https://galaxy.ansible.com/chocolatey/chocolatey).

Chocolatey has a [recommended architecture](https://chocolatey.org/docs/how-to-setup-internal-package-repository)
for organizations, which includes setting up an internal repository. To
speed up that process, there is a [Quick Deployment Environment](https://chocolatey.org/docs/quick-deployment-environment) that
allows you to be up and running with an internal repository with useful
packages already loaded, Jenkins for automation and Chocolatey Central
Management for reporting in around two hours.

For package management on Windows, Chocolatey is the package manager of
choice. Working in harmony with Ansible, you can use it to update and
manage your Windows computers in a similar way as you would with Linux.
