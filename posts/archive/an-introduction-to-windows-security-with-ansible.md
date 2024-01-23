---
author: The Getting Started Team
date: 2018-06-21 00:00 UTC
description: An introduction to Windows security with Ansible.
lang: en-us
title: An Introduction to Windows Security with Ansible
---

# An Introduction to Windows Security with Ansible

Welcome to another installment of our Windows-centric Getting Started
Series! In the prior posts we talked about
connecting to Windows machines, gave a brief introduction on using
Ansible with Active Directory, and discussed package management options
on Windows with Ansible. In this post we'll talk a little about applying
security methodologies and practices in relation to our original topics.

## The Triad

In order to discuss security issues in relation to Ansible and Windows,
we'll be applying concepts from the popular CIA Triad: Confidentiality,
Integrity, and Availability.

Confidentiality is pretty self-evident --- protecting confidentiality
helps restrict private data to only authorized users and helps to
prevent non-authorized ones from seeing it. The way this is accomplished
involves several techniques such as authentication, authorization, and
encryption. When working with Windows, this means making sure the hosts
know all of the necessary identities, that each user is appropriately
verified, and that the data is protected (by, for example, encryption)
so that it can only be accessed by authorized parties.

Integrity is about making sure that the data is not tampered with or
damaged so that it is unusable. When you're sending data across a
network you want to make sure that it arrives in the same condition as
it was sent out. This will apply to the tasks in an Ansible Playbook,
any files that may be transferred, or packages that are installed (and
more!).

Availability is mainly about making data available to those authorized
users when they need to access it. Think about things like redundancy,
resiliency, high-availability, or clustering as ways to help ensure
availability of systems and data.

###  Confidentiality

As Bianca mentioned in the first installment of this series, Ansible
uses WinRM and sends user/password with variables (or, in the case of
Ansible Tower, by using credentials). In the example below, which shows
an inventory file that includes variables as `[win:vars]`, the
certificate is ignored:

```yml
[win:vars]
ansible_user=vagrant
ansible_connection=winrm
ansible_winrm_server_cert_validation=ignore
```

In an Active Directory environment the domain-joined hosts won't
require ignoring certificates that validate if your control node has
been set to trust the Active Directory CS.

### Integrity

Active Directory, discussed by John in the second installment, adds more
verification to credentials and authority for validating certificates on
domains in its scope. The directory services provide added strength to
confidentiality by being the authoritative credential store. Joining a
host to the domain establishes its trust, so as long as a user
requesting resources is valid, then a domain-joined host will have
established integrity.

Ansible is able to add and manage users
([win_domain_user](https://docs.ansible.com/ansible/latest/modules/win_domain_user_module.html#win-domain-user-module)),
groups
([win_domain_group](https://docs.ansible.com/ansible/latest/modules/win_domain_group_module.html#win-domain-group-module)),
or hosts
([win_domain_membership](https://docs.ansible.com/ansible/latest/modules/win_domain_membership_module.html#win-domain-membership-module))
securely and with valid domain credentials. See the example below for
how these tasks can be done with the use of a playbook:

```yaml
- name: Join to domain
  win_domain_membership:
    dns_domain_name: tycho.local
    hostname: mydomainclient
    domain_admin_user: "{{ win_domain_admin_user }}"
    domain_admin_password: "{{ win_domain_admin_password }}"
    domain_ou_path: "OU=Windows,OU=Servers,DC=tycho,DC=local"
    state: domain
  register: domain_state

- name: set group with delete protection enabled
  win_domain_group:
    name: Users
    scope: domainlocal
    category: security
    ignore_protection: no
```

### Availability

In the a recent Windows-related
post, which was about package
management, Jake gave a few examples that used the Ansible Modules
[win_package](https://docs.ansible.com/ansible/latest/modules/win_package_module.html#win-package-module)
and
[win_chocolatey](https://docs.ansible.com/ansible/latest/modules/win_chocolatey_module.html#win-chocolatey-module).
This is related to the third part of that security triad because the
data model's physical and transport layers get a lot of attention in
terms of obtainability, but fast and efficient software/patch management
is also a part of maintaining this availability. The less time eaten up
through rolling out updates reduces downtime. Shaving minutes or even
seconds in a rollout can pay off with more consistent service delivery.

An important availability-related security function which can be
executed using an Ansible module is related to updates. As the name
suggests,
[win_updates](https://docs.ansible.com/ansible/latest/modules/win_updates_module.html#win-updates-module)
searches, downloads, and installs updates on all Windows hosts
simultaneously by automating the Windows update client. Let's explore
this module further.

The example below is taken from the
[example](https://raw.githubusercontent.com/ansible/ansible-lockdown/master/meltdown-spectre-windows.yml)
that's part of a collection of [Ansible
Roles](https://github.com/ansible/ansible-lockdown) related to security
automation. Here you can see the win_updates module in action:

```yml
tasks:
 - name: Install security updates
   win_updates:
     category_names:
       - SecurityUpdates
     Notify: reboot windows system
```

Another example shows how you can use this module within a playbook for
patching Windows nodes, along with the win_reboot module which is used
for--- you guessed it!--- automating the restarting of Windows machines:

```yml
– name: Install missing updates
  win_updates:
    Category_names:
       – ServicePacks
       – UpdateRollups
       – CriticalUpdates
    Reboot: yes
```

###  Conclusion

Security is a complex and ever-evolving field that's dependent on each
organization's particular environment, vulnerabilities, and specific
needs. It's extremely important to read the above as a guideline and not
a checklist; no amount of implementation is going to have any
long-lasting effect if continual improvement isn't implemented.

We hope you found this information helpful, and that this five-part
series has provided you with the tools for automating your Windows hosts
with confidence by using Ansible to do the work for you!
