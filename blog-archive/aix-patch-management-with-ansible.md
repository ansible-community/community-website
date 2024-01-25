---
author: Talor Holloway
date: 2021-07-07 00:00 UTC
description: This blog will help AIX system administrators get started
  with Ansible on AIX, and introduce a patching use case.
lang: en-us
title: AIX Patch Management with Ansible
---


# AIX Patch Management with Ansible

Leading enterprises today use Red Hat Ansible Automation Platform to
provision, configure, manage, secure and orchestrate hybrid IT
environments. A common misconception is that Ansible is just used to
manage the Linux operating system. This is a false belief. Ansible
supports Linux, Windows, AIX, IBM i and IBM z/OS environments. This blog
will help AIX system administrators get started with Ansible on AIX, and
introduce a patching use case.

## Ansible Content Collections

When Ansible Automation Platform was released, Ansible Content
Collections became the de facto standard for distributing, maintaining
and consuming automation content. The shift to Collections increased
community participation and has exponentially increased the number of
stable and supported Ansible modules. Modules delivered via Collections
rather than packaged with Ansible Core have resulted in a faster release
cadence for new modules.

Let us explore the IBM provided Ansible Collection for AIX. It is
important to note that many of the Ansible modules for the Linux
operating system will also work on AIX (in addition to the IBM provided
AIX modules), making the use cases for Ansible on AIX very broad.

## Ansible and AIX, why?

The AIX operating system has been around for 35 years and is used to run
business-critical applications. Historically, AIX systems were managed
using the tools that ship with AIX, complimented by shell scripts
written by AIX system administrators. The problem with this approach is
that these scripts can become extremely complex over the years, and
often wind up being held together with "duct tape and zip ties".

As enterprises move to a modern, enterprise-wide automation strategy
with Ansible Automation Platform, extending automation to AIX is a great
method to simplify and develop consistency in the way AIX systems are
supported, all while using the same automation tools that can be used
across the enterprise.

## Ansible Concepts

First let us cover some basic Ansible concepts that will be used in the
example. Further information can be found on the
[Ansible documentation site](https://docs.ansible.com).

Playbooks, which are ordered lists of tasks and variables that are
performed against an inventory of hosts.

Tasks are a single unit of action in Ansible, which calls a module.

Modules are code that Ansible executes. Each module could be something
like copying a file to using NIM to trigger an AIX update.

Roles are repeatable bundles of tasks that are contained in a specific
directory structure.

Variables within Ansible are called like this "".

Task delegation is how tasks can be delegated to another host in the
inventory, other than the host that the Ansible run is targeted against.

## Getting started with Ansible

In this example, I'm using a Fedora Linux 34 workstation, so I'm going
to use the dnf package manager to install Ansible:

```bash
$ sudo dnf install -y ansible
```

Once Ansible is installed, I'm going to install the ibm.power_aix
Collection:

```bash
$ ansible-galaxy collection install ibm.power_aix
```

When Ansible is installed, a default inventory file /etc/ansible/hosts
is created. At this point, I'm going to include in the inventory the
hosts used in this example:

-   nim01 is our AIX 7.2 NIM Master which is functional and has an
    lpp_source defined.
-   bruce is an AIX 7.2 NIM client registered to the nim01 NIM master.
-   freddie is an AIX 7.2 NIM client registered to the nim01 NIM master.

```bash
$ cat /etc/ansible/hosts
nim01 ansible_host=10.0.0.5 ansible_user=root
bruce ansible_host=10.0.0.6 ansible_user=root
freddie ansible_host=10.0.0.7 ansible_user=root
```

I'm now going to connect to all the systems over SSH as "root". The
usual practice is to have a service account with "sudo" access, however
for this example I will use "root" in our lab environment. Using the
ssh-copy-id command, I can distribute my SSH public key to the AIX
servers.

```bash
$ ssh-copy-id root@nim01
$ ssh-copy-id root@bruce
$ ssh-copy-id root@freddie
```

The next step is to use the Ansible ping module to check that I can
connect to the three hosts in our inventory.

```bash
$ ansible -m ping all

PLAY [Ansible Ad-Hoc] ************************************************************************************************************************************************************************************************************************

TASK [ping] **********************************************************************************************************************************************************************************************************************************
ok: [nim01]
ok: [freddie]
ok: [bruce]

PLAY RECAP ***********************************************************************************************************************************************************************************************************************************
nim01                  : ok=1    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
bruce                  : ok=1    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
freddie                : ok=1    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

Ansible needs "python" to be installed on the AIX systems, and ideally
the "yum" package manager should also be configured on AIX. If your AIX
systems do not have these packages installed, or is a vanilla
installation of AIX, IBM provides an Ansible Role to "bootstrap" an AIX
system and manage it.

The playbook below uses the IBM provided role to prepare an AIX system
for Ansible automation.

```bash
cat aix_bootstrap.yml
---

- name: Prep AIX for Ansible
  hosts: all
  vars:
    pkgtype: yum
  collections:
    - ibm.power_aix
  roles:
    - power_aix_bootstrap
```

The following example demonstrates running the playbook; however, I can
see that the hosts Ansible is running against already have "python" and
"yum" installed, so there is no need for any changes to be made to these
hosts.

```bash
$ ansible-playbook aix_bootstrap.yml

PLAY [Prep AIX for Ansible] ******************************************************************************************************************************************************************************************************************

TASK [Gathering Facts] ***********************************************************************************************************************************************************************************************************************
ok: [bruce]
ok: [freddie]
ok: [nim01]

TASK [ibm.power_aix.power_aix_bootstrap : Fail if pkgtype not specified] *********************************************************************************************************************************************************************
skipping: [nim01]
skipping: [bruce]
skipping: [freddie]

TASK [ibm.power_aix.power_aix_bootstrap : Fail if download_dir not specified] ****************************************************************************************************************************************************************
skipping: [nim01]
skipping: [bruce]
skipping: [freddie]

TASK [ibm.power_aix.power_aix_bootstrap : Fail if target_dir not specified] ******************************************************************************************************************************************************************
skipping: [nim01]
skipping: [bruce]
skipping: [freddie]

TASK [ibm.power_aix.power_aix_bootstrap : Fail if rpm_src not specified] *********************************************************************************************************************************************************************
skipping: [nim01]
skipping: [bruce]
skipping: [freddie]

TASK [ibm.power_aix.power_aix_bootstrap : Fail if yum_src not specified] *********************************************************************************************************************************************************************
skipping: [nim01]
skipping: [bruce]
skipping: [freddie]

TASK [ibm.power_aix.power_aix_bootstrap : Bootstrap yum] *************************************************************************************************************************************************************************************
included: /home/tholloway/.ansible/collections/ansible_collections/ibm/power_aix/roles/power_aix_bootstrap/tasks/yum_install.yml for nim01, bruce, freddie

TASK [ibm.power_aix.power_aix_bootstrap : Check for existence of yum] ************************************************************************************************************************************************************************
changed: [bruce]
changed: [nim01]
changed: [freddie]

PLAY RECAP ***********************************************************************************************************************************************************************************************************************************
nim01                  : ok=3    changed=1    unreachable=0    failed=0    skipped=5    rescued=0    ignored=0
bruce                  : ok=3    changed=1    unreachable=0    failed=0    skipped=5    rescued=0    ignored=0
freddie                : ok=3    changed=1    unreachable=0    failed=0    skipped=5    rescued=0    ignored=0
```

Now that the platforms meet the required minimum components, I am now
ready to automate AIX operations.

## Running an AIX Update using NIM and Ansible

First off, I'll use a simple playbook to see what "oslevel" our NIM
master and NIM clients are on, before I start.

```bash
$ cat aix_oslevel_check.yml
---

- name: AIX oslevel checking playbook
  hosts: all
  tasks:

  - name: Gather LPP Facts
    shell: "oslevel -s"
    register: output_oslevel

  - name: Print the oslevel
    debug:
      msg: "{{ ansible_hostname }} has the AIX oslevel of {{ output_oslevel.stdout }}"
```

Running that playbook delivers the below result. I can see that bruce
and freddie are a service pack behind.

```bash
$ ansible-playbook aix_oslevel_check.yml

PLAY [AIX oslevel checking playbook ] *****************************************************************************************************************************************************************************************************************

TASK [Gathering Facts] ***********************************************************************************************************************************************************************************************************************
ok: [bruce]
ok: [freddie]
ok: [nim01]

TASK [Gather LPP Facts] **********************************************************************************************************************************************************************************************************************
changed: [freddie]
changed: [bruce]
changed: [nim01]

TASK [Print the oslevel] *********************************************************************************************************************************************************************************************************************
ok: [nim01] =>
  msg: nim01 has the AIX oslevel of 7200-05-02-2114
ok: [bruce] =>
  msg: bruce has the AIX oslevel of 7200-05-01-2038
ok: [freddie] =>
  msg: freddie has the AIX oslevel of 7200-05-01-2038

PLAY RECAP ***********************************************************************************************************************************************************************************************************************************
nim01                  : ok=3    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
bruce                  : ok=3    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
freddie                : ok=3    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

To ensure all systems are operating on the same OS level, I need to
download the latest service pack. It should define an "lpp_source" on
our NIM master. Make sure that the name of the "lpp_source" matches the
example below, or the Ansible module will not detect the "oslevel".

```bash
$ cat aix_download.yml
---

- name: AIX Patching Playbook
  hosts: nim01
  vars:
    oslevel: 7200-05-02
    nim_lpp_source: 7200-05-02-2114-lpp_source
  collections:
    - ibm.power_aix
  tasks:

  - name: Download AIX Updates
    nim_suma:
      action: download
      download_dir: "/export/nim/lpp_source"
      lpp_source_name: "{{ nim_lpp_source }}"
      oslevel: "{{ oslevel }}"
      targets: 'bruce, freddie'
```

Next step is to run the *download playbook*. It will download the
required updates from IBM Fix Central and define an "lpp_source" on the
NIM master:

```bash
$ ansible-playbook aix_download.yml

PLAY [AIX Patching Playbook] *****************************************************************************************************************************************************************************************************************

TASK [Gathering Facts] ***********************************************************************************************************************************************************************************************************************
ok: [nim01]

TASK [Download AIX Updates] ******************************************************************************************************************************************************************************************************************
changed: [nim01]

PLAY RECAP ***********************************************************************************************************************************************************************************************************************************
nim01                  : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

Now I can run a *patching playbook*, which will make use of the
"alt_disk" and "nim" Ansible modules. The playbook is going to perform
the following tasks:

-   Remove any existing "altinst_rootvg" "alt_disk_copy" that is left on
    the AIX system.
-   Create a new "alt_disk_copy" clone of the root volume group to a
    spare disk as a backup.
-   Run an application stop script.
-   Run the AIX update via task delegation to the NIM master.
-   Reboot.
-   Run an application start script.

```yaml
---

- name: AIX Patching Playbook
  hosts: bruce,freddie
  vars:
    nim_lpp_source: 7200-05-02-2114-lpp_source
    nim_master: nim01
  collections:
    - ibm.power_aix
  tasks:

  - name: Cleanup any existing alt_disk_copy
    alt_disk:
      action: clean

  - name: Create an alt_disk_copy for backup
    alt_disk:
      targets: hdisk1

  - name: Stop Application
    shell: /usr/local/bin/stop.sh

  - name: Run AIX Update
    nim:
      action: update
      lpp_source: "{{ nim_lpp_source }}"
      targets: "{{ ansible_hostname }}"
    delegate_to: "{{ nim_master }}"

  - name: Reboot
    reboot:
      post_reboot_delay: 180

  - name: Start Application
    shell: /usr/local/bin/start.sh
```

Now I will run the playbook and patch the NIM client systems "bruce" and
"freddie":

```bash
$ ansible-playbook aix_patching.yml

 PLAY [AIX Patching Playbook] *****************************************************************************************************************************************************************************************************************

TASK [Gathering Facts] ***********************************************************************************************************************************************************************************************************************
ok: [bruce]
ok: [freddie]

TASK [Cleanup any existing alt_disk_copy] ****************************************************************************************************************************************************************************************************
changed: [bruce]
changed: [freddie]

TASK [Create an alt_disk_copy for backup] ****************************************************************************************************************************************************************************************************
changed: [bruce]
changed: [freddie]

TASK [Stop Application] **********************************************************************************************************************************************************************************************************************
changed: [bruce]
changed: [freddie]

TASK [Run AIX Update] *************************************************************************************************************************************************************************************************************************
changed: [bruce -> 10.0.0.5]
changed: [freddie -> 10.0.0.5]

TASK [Reboot] ********************************************************************************************************************************************************************************************************************************
changed: [freddie]
changed: [bruce]

TASK [Start Application] *********************************************************************************************************************************************************************************************************************
changed: [bruce]
changed: [freddie]

PLAY RECAP ***********************************************************************************************************************************************************************************************************************************
bruce                 : ok=7    changed=6    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
freddie               : ok=7    changed=6    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

Next, I will run the aix_oslevel_check.yml playbook again and see that
the systems are all on AIX 7.2 TL5 SP2.

```bash
$ ansible-playbook aix_oslevel_check.yml

PLAY [AIX oslevel checking playbook ] *****************************************************************************************************************************************************************************************************************

TASK [Gathering Facts] ***********************************************************************************************************************************************************************************************************************
ok: [bruce]
ok: [freddie]
ok: [nim01]

TASK [Gather LPP Facts] **********************************************************************************************************************************************************************************************************************
changed: [freddie]
changed: [bruce]
changed: [nim01]

TASK [Print the oslevel] *********************************************************************************************************************************************************************************************************************
ok: [nim01] =>
  msg: nim01 has the AIX oslevel of 7200-05-02-2114
ok: [bruce] =>
  msg: bruce has the AIX oslevel of 7200-05-02-2114
ok: [freddie] =>
  msg: freddie has the AIX oslevel of 7200-05-02-2114

PLAY RECAP ***********************************************************************************************************************************************************************************************************************************
nim01                  : ok=3    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
bruce                  : ok=3    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
freddie                : ok=3    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

## Conclusion

As you can see from this example, Ansible provides a lot of value in
automating AIX operations. For additional information, see the
documentation for the supported Collection available from
[Automation Hub](https://cloud.redhat.com/ansible/automation-hub/repo/published/ibm/power_aix).
This Collection is also available to the community from
[Ansible Galaxy](https://galaxy.ansible.com/ibm/power_aix).
