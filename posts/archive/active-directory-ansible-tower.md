---
author: John Lieske
date: 2020-05-06 00:00 UTC
description: In this post learn ways you can use Ansible to manage Microsoft's Active Directory.
lang: en-us
title: Active Directory and Ansible Tower
---

# Active Directory & Ansible Tower

Welcome to the second installment of our Windows-centric Getting Started series!

Last time we walked you through how Ansible connects to a Windows
host. We've also previously
explored logging into Ansible Tower while authenticating against an LDAP
directory. In this post, we'll go over a few ways you can use Ansible to
manage Microsoft's Active Directory. Since AD plays a role in many
Windows environments, using Ansible to manage Windows will probably
include running commands against the Active Directory domain.

## First, Set Your Protocol

We'll be using WinRM to connect to Windows hosts, so this means making
sure Ansible or Tower knows that. Machine credentials in Ansible Tower
can be created and used along with variables, but when using Ansible in
a terminal the playbook should make it clear with variables:

```yml
---
- name: Your Windows Playbook
  hosts: win
  vars:
    ansible_ssh_user: administrator
    ansible_ssh_pass: ThisIsWhereStrongPassesGo
    ansible_connection: winrm
    ansible_winrm_server_cert_validation: ignore

- tasks:
```

Along with using the local admin account/pass, the WinRM connection
method is named specifically. The variable to ignore the certificate
validation is for standalone, non-domain hosts because a domain-joined
instance should have certificates validated on the domain.

###  Where's the Domain?

Speaking of domains, Ansible can spin up a new domain if one doesn't
exist.

In the following example, Ansible (using the previous settings) installs
the AD Domain Services features from Server Management `win_feature`,
and if there's no domain present it creates the new Active Directory
domain with the provided AD safe mode password `win_domain`:

```yml
- name: Install AD Services feature
  win_feature:
    name: AD-Domain-Services
    include_management_tools: yes
    include_sub_features: yes
    state: present
  register: result

- name: Create new forest
  win_domain:
    dns_domain_name: tycho.local
    safe_mode_password: RememberTheCant!
  register: result

- name: Reboot after creation
  win_reboot:
    msg: "Server config in progress; rebooting..."
  when: result.reboot_required
```

After creating the domain, the server sends a message to anyone logged
in that the server is rebooting and then commences to reboot. While not
a production-quality playbook, this is a good example of what can be
configured quickly with a few short plays.

If there's already a domain present for testing there's no need to
create one, but there may be a test machine that should be joined to an
existing domain. Ansible can similarly shorten that task with a few
plays as well:

```yaml
- name: Configure DNS
  win_dns_client:
    adapter_names: "Ethernet 2"
    ipv4_addresses:
    - 10.0.0.1

- name: Promote to member
  win_domain_membership:
    dns_domain_name: tycho.local
    domain_admin_user: drummer@tycho.local
    domain_admin_password: WeNeed2Hydrate!
    state: domain
  register: domain_state

- name: Reboot after joining
  win_reboot:
    msg: "Joining domain. Rebooting..."
  when: domain_state.reboot_required
```

The steps are self-explanatory, make sure the machine can communicate
with the directory server (`win_dns_client`), then join to the domain
(`win_domain_membership`). The target restarts to complete joining the
directory. Quick and easy.

###  What Can It Do?

Using the `win_feature` to manage the roles is similar to the
combination of the `Install-WindowsFeature` and `Add-WindowsFeature`
Powershell cmdlet. If you're not familiar with the name used for the
feature you're trying to install, use the `Get-WindowsFeature` cmdlet to
list available features to install.

The Windows domain modules ( `win_domain`, `win_domain_controller`,
`win_domain_group`, `win_domain_membership`, `win_domain_user` ) cover
the common tasks run against an Active Directory. For most of the
[Windows modules](http://docs.ansible.com/ansible/latest/modules/list_of_windows_modules.html)
a domain account with appropriate privileges should be set as a machine
credential (using DOMAIN/User or User@domain.tld), much like you would
for a local account.

### To Conclude

In this post, we used WinRM to connect to Windows hosts, had Ansible
install the AD Domain Services features from Server Management using the
`win_feature` module (or created the new Active Directory domain if
there isn't one already present by using the `win_domain` module), made
sure the machine can communicate with the directory server using
`win_dns_client`, then joined it to the domain using
`win_domain_membership`.

Don't forget to make sure that your playbook for Windows nodes sets the
connection variables by specifically stating `ansible_connection: winrm`
(required) as well as `ansible_winrm_server_cert_validation: ignore` (if
you haven't added your local CA as trusted). As shown in the beginning
of this post, those two variables go along with the connecting account
variables after `vars:` in an Ansible Playbook. In Ansible Tower, those
variables go in the job template.

So now you know how to use Ansible with Microsoft's Active Directory! In
our next post, we'll dive deeper into the package management abilities
you have with Ansible and Windows!
