---
author: Bianca Henderson
date: 2018-04-24 00:00 UTC
description: Set up and connect to your Windows hosts with Ansible
  Engine.
lang: en-us
title: Connecting to a Windows Host
---

# Connecting to a Windows Host

Welcome to the first installment of our Windows-specific [Getting
Started](/blog/topic/getting-started) series!\
\
Would you like to automate some of your Windows hosts with Red Hat
Ansible Tower, but don't know how to set everything up? Are you worried
that Red Hat Ansible Engine won't be able to communicate with your
Windows servers without installing a bunch of extra software? Do you
want to easily automate everyone's best friend, Clippy?

![Ansible-Windows-Clippy](/images/posts/archive/Ansible-Windows/Ansible-Windows-Clippy.png)

We can't help with the last thing, but if you said yes to the other two
questions, you\'ve come to the right place. In this post, we'll walk you
through all the steps you need to take in order to set up and connect to
your Windows hosts with Ansible Engine.

## Why Automate Windows Hosts?

A few of the many things you can do for your Windows hosts with Ansible
Engine include:

-   Starting, stopping and managing services
-   Pushing and executing custom PowerShell scripts
-   Managing packages with the Chocolatey package manager

In addition to connecting to and automating Windows hosts using local or
domain users, you'll also be able to use `runas` to execute actions as
the Administrator (the Windows alternative to Linux's `sudo` or `su`),
so no privilege escalation ability is lost.

## What's Required?

Before we start, let's go over the [basic
requirements](http://docs.ansible.com/ansible/latest/user_guide/windows_setup.html#host-requirements.).
First, your control machine (where Ansible Engine will be executing your
chosen Windows modules from) needs to run Linux. Second, Windows support
has been evolving rapidly, so make sure to use the newest possible
version of Ansible Engine to get the latest features!\
\
For the target hosts, you should be running at least Windows 7 SP1 or
later or Windows Server 2008 SP1 or later. You don't want to be running
something from the 90's like Windows NT, because this might happen:

![Ansible-Windows-90s](/images/posts/archive/Ansible-Windows-90s.jpg)

Lastly, since Ansible connects to Windows machines and runs PowerShell
scripts by using [Windows Remote
Management](https://msdn.microsoft.com/en-us/library/aa384291(v=vs.85).aspx)
(WinRM) (as an alternative to SSH for Linux/Unix machines), a WinRM
listener should be created and activated. The good news is, connecting
to your Windows hosts can be done very easily and quickly using a
script, which we'll discuss in the section below.

## Step 1: Setting up WinRM

What's WinRM? It's a feature of Windows Vista and higher that lets
administrators run management scripts remotely; it handles those
connections by implementing the WS-Management Protocol, based on [Simple
Object Access
Protocol](https://msdn.microsoft.com/en-us/library/ms995800.aspx)
(commonly referred to as [SOAP](https://en.wikipedia.org/wiki/SOAP)).
With WinRM, you can do cool stuff like access, edit and update data from
local and remote computers as a network administrator.\
\
The reason WinRM is perfect for using with Ansible Engine is because you
can obtain hardware data from WS-Management protocol implementations
running on non-Windows operating systems (in this specific case, Linux).
It's basically like a translator that allows different types of
operating systems to work together.

So, how do we connect?

With most versions of Windows, WinRM ships in the box but isn't turned
on by default. There's a [Configure Remoting for
Ansible](https://raw.githubusercontent.com/ansible/ansible/devel/examples/scripts/ConfigureRemotingForAnsible.ps1)
script you can run on the remote Windows machine (in a PowerShell
console as an Admin) to turn on WinRM. To set up an https listener,
build a self-signed cert and execute PowerShell commands, just run the
script like in the example below (if you've got the `.ps1` file stored
locally on your machine):\
![Ansible-Windows-Powershell](/images/posts/archive/Ansible-Windows-Powershell.png)

Note: The
[win_psexec](http://docs.ansible.com/ansible/latest/modules/win_psexec_module.html)
module will help you enable WinRM on multiple machines if you have lots
of Windows hosts to set up in your environment.

For more information on WinRM and Ansible, check out the [Windows Remote
Management](http://docs.ansible.com/ansible/latest/user_guide/windows_winrm.html)
documentation page.

## Step 2: Install Pywinrm

Since pywinrm dependencies aren't shipped with Ansible Engine (and these
are necessary for using WinRM), make sure you install the
pywinrm-related library on the machine that Ansible is installed on. The
simplest method is to run `pip install pywinrm` in your Terminal.

## Step 3: Set Up Your Inventory File Correctly

In order to connect to your Windows hosts properly, you need to make
sure that you put in `ansible_connection=winrm` in the [host
vars](http://docs.ansible.com/ansible/latest/user_guide/intro_inventory.html#host-variables)
section of your inventory file so that Ansible Engine doesn't just keep
trying to connect to your Windows host via SSH.\
\
Also, the WinRM connection plugin defaults to communicating via https,
but it supports different modes like message-encrypted http. Since the
"Configure Remoting for Ansible" script we ran earlier set things up
with the self-signed cert, we need to tell Python, "Don't try to
validate this certificate because it's not going to be from a valid CA."
So in order to prevent an error, one more thing you need to put into the
`host vars` section is: `ansible_winrm_server_cert_validation=ignore`\
\
Just so you can see it in one place, here is an example host file
(please note, some details for your particular environment will be
different):\

``` {.line-numbers .language-yaml}
[win]
172.16.2.5 
172.16.2.6 

[win:vars]
ansible_user=vagrant
ansible_password=password
ansible_connection=winrm
ansible_winrm_server_cert_validation=ignore
```

## Step 4: Test Connection

Let's check to see if everything is working. To do this, go to your
control node's terminal and type
`ansible [host_group_name_in_inventory_file] -i hosts -m win_ping`. Your
output should look like this:

![Ansible-Windows-Screen-Grab](/images/posts/archive/Ansible-Windows-Screen-Grab.jpg)

Note: The `win_` prefix on all of the Windows modules indicates that
they are implemented in PowerShell and not Python.

## Troubleshooting WinRM

Because WinRM can be configured in so many different ways, errors that
seem Ansible Engine-related can actually be due to problems with host
setup instead. Some examples of WinRM errors that you might see include
an HTTP 401 or HTTP 500 error, timeout issues or a connection refusal.
To get tips on how to solve these problems, visit the [Common WinRM
Issues](http://docs.ansible.com/ansible/devel/user_guide/windows_setup.html#common-winrm-issues)
section of our Windows Setup documentation page.

## Conclusion

You should now be ready to automate your Windows hosts using Ansible,
without the need to install a ton of additional software! Keep in mind,
however, that even if you've followed the instructions above, some
Windows modules have additional specifications (e.g., a newer OS or more
recent PowerShell version). The best way to figure out if you're meeting
the right requirements is to check the
[module-specific](https://docs.ansible.com/ansible/latest/collections/index_module.html#ansible-windows){rel="noopener"}
documentation pages.\
\
For more in-depth information on how to use Ansible Engine to automate
your Windows hosts, check out our [Windows
FAQ](http://docs.ansible.com/ansible/latest/user_guide/windows_faq.html)
and [Windows
Support](http://docs.ansible.com/ansible/latest/user_guide/windows.html)
documentation page and stay tuned for more Windows-related blog posts!

