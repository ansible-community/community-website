---
author: Sean Cavanaugh
date: 2019-03-18 00:00 UTC
description: Sean Cavanaugh demonstrates how easy it is to import your
  existing Ansible inventory into Red Hat Ansible Tower
lang: en-us
title: Three quick ways to move your Ansible inventory into Red Hat Ansible Tower
---

# Three quick ways to move your Ansible inventory into Red Hat Ansible Tower

![3 Ways quick ways to your Ansible inventory to Red Hat Ansible
Tower](https://www.ansible.com/hubfs/Images/blog-social/Ansible-Blog-Instances.png)

If you've been using Ansible at the command line for a while, you
probably have a lot of servers, network devices, and other target nodes
listed in your inventory. You know that Red Hat Ansible Tower makes it
easier for everyone on your team to run your Ansible Playbooks. So
you've thought about using Ansible Tower to take your automation to the
next level, but you want to retain all the data and variables in your
existing inventory file or directory. Are you worried about transferring
your inventory from command-line use to Ansible Tower? Let me show you
how easy it is to import your existing Ansible inventory into Ansible
Tower!

This blog covers three quick and effective ways to connect your existing
Ansible inventory into Ansible Tower:

1.  Migrating an inventory file from the Ansible Tower control node
    (awx-manage)
2.  Migrating an inventory file from anywhere with a playbook
3.  Setting Tower to access a git source-controlled inventory file

If you don't have Ansible Tower yet and want to download and try it out,
please visit: <https://www.ansible.com/products/tower>

If you're using [dynamic inventory](https://docs.ansible.com/ansible-tower/latest/html/userguide/inventories.html),
you don\'t need to import your inventory into Ansible Tower. Dynamic
inventory retrieves your inventory from an existing source. With dynamic
inventory, you don't need to manage an inventory file at all, you just
retrieve the latest and most up-to-date listing every time. Ansible
[Tower seamlessly integrates](https://docs.ansible.com/ansible-tower/latest/html/userguide/inventories.html#credential-sources)
with popular dynamic inventory sources including Red Hat OpenStack
Platform, Red Hat Satellite, public cloud platforms (Amazon Web
Services/AWS, Google Compute Engine/GCE, Microsoft Azure), and
virtualization solutions like Red Hat Virtualization and VMware vCenter.
You can use scripts to integrate Infoblox DDI and ServiceNow CMDB for
dynamic inventory in Ansible Tower as well.

NOTE: This blog does not cover the importing of Ansible Playbooks or
Ansible Tower workflows into Ansible Tower and is strictly focused on
Ansible inventory portability.

## Migrating an inventory file from the Ansible Tower control node (awx-manage)

The command line tool
[awx-manage](https://docs.ansible.com/ansible-tower/latest/html/administration/tower-manage.html),
which comes with your Ansible Tower installation, is a simple and
effective tool to import your inventory. Using awx-manage makes the most
sense when your inventory is a flat file in YAML or ini format that
already lives on your Ansible control node. You run the command and
point to your existing inventory file then Ansible Tower will be loaded
with all the hosts.

1.  Using the WebUI login to Ansible Tower and create an empty
    inventory.\
    ![inventory](https://www.ansible.com/hs-fs/hubfs/inventory.gif?width=960&name=inventory.gif){width="960"
    style="width: 960px;"
    srcset="https://www.ansible.com/hs-fs/hubfs/inventory.gif?width=480&name=inventory.gif 480w, https://www.ansible.com/hs-fs/hubfs/inventory.gif?width=960&name=inventory.gif 960w, https://www.ansible.com/hs-fs/hubfs/inventory.gif?width=1440&name=inventory.gif 1440w, https://www.ansible.com/hs-fs/hubfs/inventory.gif?width=1920&name=inventory.gif 1920w, https://www.ansible.com/hs-fs/hubfs/inventory.gif?width=2400&name=inventory.gif 2400w, https://www.ansible.com/hs-fs/hubfs/inventory.gif?width=2880&name=inventory.gif 2880w"
    sizes="(max-width: 960px) 100vw, 960px"}

2.  Login via SSH to your Ansible Tower control node (This is the Linux
    machine that has Ansible Tower installed on it).

3.  Locate the flat-file that represents your Ansible inventory.

4.  Run the awx-manage inventory_import command like this

        sudo awx-manage inventory_import --source=/path/to/hosts --inventory-name="My Inventory"

    On the terminal window you will receive some output similar to the
    following:

        1.387 INFO Updating inventory 3: My Inventory 
        1.475 INFO Reading Ansible inventory source: /path/to/hosts 
        2.119 INFO Processing JSON output... 
        2.120 INFO Loaded 6 groups, 6 hosts 
        2.329 INFO Inventory import completed for (My Inventory - 9) in 0.9s

5.  Now when you login via the WebUI you will see all the hosts under
    the inventory\
    ![loaded_inventory](https://www.ansible.com/hs-fs/hubfs/loaded_inventory.gif?width=960&name=loaded_inventory.gif){width="960"
    style="width: 960px;"
    srcset="https://www.ansible.com/hs-fs/hubfs/loaded_inventory.gif?width=480&name=loaded_inventory.gif 480w, https://www.ansible.com/hs-fs/hubfs/loaded_inventory.gif?width=960&name=loaded_inventory.gif 960w, https://www.ansible.com/hs-fs/hubfs/loaded_inventory.gif?width=1440&name=loaded_inventory.gif 1440w, https://www.ansible.com/hs-fs/hubfs/loaded_inventory.gif?width=1920&name=loaded_inventory.gif 1920w, https://www.ansible.com/hs-fs/hubfs/loaded_inventory.gif?width=2400&name=loaded_inventory.gif 2400w, https://www.ansible.com/hs-fs/hubfs/loaded_inventory.gif?width=2880&name=loaded_inventory.gif 2880w"
    sizes="(max-width: 960px) 100vw, 960px"}

The awx-manage command line tool is very simple and fast. It only took
me a couple seconds to take my existing inventory and import it into
Ansible Tower.

For teams that use Ansible Tower to run playbooks, but manage inventory
outside of Ansible Tower, importing with awx-manage is not the best
option, since you would need to re-import the flat-file inventory every
time a change is made to your inventory file. If your team will continue
to manage inventory outside of Ansible Tower, you probably want to use
the GitHub option described below.

## Migrating an inventory file from anywhere with a playbook

You can use the [Ansible Tower
modules](https://docs.ansible.com/ansible/latest/modules/list_of_web_infrastructure_modules.html#ansible-tower)
to automate the transfer of your inventory into Ansible Tower. These
modules make it possible to use Ansible Playbooks to automate and manage
everything, including inventory, in your Ansible Tower instance. There
is a [tower_inventory
module](https://docs.ansible.com/ansible/latest/modules/tower_inventory_module.html#tower-inventory-module)
that will let us create an inventory, and there is a [tower_host
module](https://docs.ansible.com/ansible/latest/modules/tower_host_module.html#tower-host-module)
that lets us add a host to an existing inventory. Assume that we already
created an inventory called "Network Routers" and I will build an
Ansible Playbook to add all my routers in the group routers to that
inventory using the tower_host module. The Ansible Playbook will look
like this:

    - name: NETWORK SETUP
      hosts: routers
      connection: local
      become: yes
      gather_facts: no
      tasks:
        - name: ADD NETWORK HOSTS INTO TOWER
          tower_host:
                name: "{{ inventory_hostname }}"
                inventory: "Network Routers"
                tower_username: admin
                tower_password: ansible
                tower_host: https://localhost
                variables:
                  ansible_network_os: "{{ansible_network_os}}"
                  ansible_host: "{{ansible_host}}"
                  ansible_user: "{{ansible_user}}"
                  ansible_connection: "{{ansible_connection}}"
                  ansible_become: yes
                  ansible_become_method: enable

\

The Ansible Playbook will add all devices in the group routers
simultaneously. The playbook output will look similar to this: 

![Ansible-Playbook](https://www.ansible.com/hs-fs/hubfs/Images/blog-social/Tower-Instances-Screenshots/Ansible-Playbook.png?width=632&name=Ansible-Playbook.png){width="632"
style="width: 632px;"
srcset="https://www.ansible.com/hs-fs/hubfs/Images/blog-social/Tower-Instances-Screenshots/Ansible-Playbook.png?width=316&name=Ansible-Playbook.png 316w, https://www.ansible.com/hs-fs/hubfs/Images/blog-social/Tower-Instances-Screenshots/Ansible-Playbook.png?width=632&name=Ansible-Playbook.png 632w, https://www.ansible.com/hs-fs/hubfs/Images/blog-social/Tower-Instances-Screenshots/Ansible-Playbook.png?width=948&name=Ansible-Playbook.png 948w, https://www.ansible.com/hs-fs/hubfs/Images/blog-social/Tower-Instances-Screenshots/Ansible-Playbook.png?width=1264&name=Ansible-Playbook.png 1264w, https://www.ansible.com/hs-fs/hubfs/Images/blog-social/Tower-Instances-Screenshots/Ansible-Playbook.png?width=1580&name=Ansible-Playbook.png 1580w, https://www.ansible.com/hs-fs/hubfs/Images/blog-social/Tower-Instances-Screenshots/Ansible-Playbook.png?width=1896&name=Ansible-Playbook.png 1896w"
sizes="(max-width: 632px) 100vw, 632px"}

The advantage of this method is you don't have to be on the control
node, you can run the Ansible Playbook from anywhere. Like the
awx-manage option, transferring your inventory to Ansible Tower with an
Ansible Playbook works well only if you will manage your inventory in
Tower in future. These two methods are migration strategies to Tower.
Ansible If you use dynamic inventory or source control to manage
inventory, you'd have to re-run the playbook for Ansible Tower every
time you changed your inventory.

## Setting Tower to access a git source-controlled inventory file

The final method I want to cover in this post is using source control to
manage my inventory. I have a flat-file inventory file stored in a
Github repo. I made an example repo to illustrate this concept here:
<https://github.com/ipvsean/sample_inventory>

Unlike the previous two methods, this is not meant as a migration
strategy, but a more permanent way to manage your Ansible inventory
using git and source control. Inventory can be managed in Github and
Ansible Tower can simply reflect those changes. 

First we need to create an Ansible Tower Project. An Ansible Tower
Project is how we can sync Ansible Tower to source code management (SCM)
system supported by Ansible Tower, including Git, Subversion, and
Mercurial. I will add a Project named Sean's Github, set the SCM Type to
Git, and put the SCM URL I listed above.

![](https://lh3.googleusercontent.com/HNPw9OckoCLq6hcamxwnWfLqbPz10_EsrGh3iR--Iwk4Etz1iivre2fVVpq3LndsqH5QFwyplDZNPc-cDy4sJ5BhDhS-O_LVOxeGB0_etGC4RADu7SaWij2zJfYi6Z7x7qcT1TWp)

Now I need to create an Inventory that will use this Ansible Tower
project. I will:

1.  Create an inventory called Sean Github Inventory.
2.  Add a Source called Sean Github Source, and choose the Ansible Tower
    Project previously created (named Sean's Github).
3.  As soon as the Project is selected a drop down menu will appear and
    allow us to point directly the hosts flat-file.
4.  Once you create the source you can sync it using the circular arrow
    sync button. The hosts and groups will automatically show up under
    the hosts button as shown in the animation below.

 ![github_inventory](https://www.ansible.com/hs-fs/hubfs/github_inventory.gif?width=960&name=github_inventory.gif){width="960"
style="width: 960px;"
srcset="https://www.ansible.com/hs-fs/hubfs/github_inventory.gif?width=480&name=github_inventory.gif 480w, https://www.ansible.com/hs-fs/hubfs/github_inventory.gif?width=960&name=github_inventory.gif 960w, https://www.ansible.com/hs-fs/hubfs/github_inventory.gif?width=1440&name=github_inventory.gif 1440w, https://www.ansible.com/hs-fs/hubfs/github_inventory.gif?width=1920&name=github_inventory.gif 1920w, https://www.ansible.com/hs-fs/hubfs/github_inventory.gif?width=2400&name=github_inventory.gif 2400w, https://www.ansible.com/hs-fs/hubfs/github_inventory.gif?width=2880&name=github_inventory.gif 2880w"
sizes="(max-width: 960px) 100vw, 960px"}

![](https://lh3.googleusercontent.com/hj8LwyoHsmi9ldcO9Ny4SEOiyCK9x53wXC-lfSS14fV_iUpcVZub-PbXaGQojhdJ4AOFC_PNMlMLwKdSO97NjWM6aHAWd3cGBEnoqmpnCZXYA1hSHApwzW2G381_kGfERt12J_qw)

Using source control for managing inventory is popular with Ansible
Tower users and can scale really well.
