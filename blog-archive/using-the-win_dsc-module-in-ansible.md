---
author: Bianca Henderson
date: 2018-07-31 00:00 UTC
description: In this article we'll be exploring what Desired State
  Configuration is, why it's useful, and how to utilize it with Ansible
  to manage your Windows nodes.
lang: en-us
title: Using the win_dsc Module in Ansible
---

# Using the win_dsc Module in Ansible

Hello, and welcome to another Getting Started with Ansible + Windows post! In
this article we'll be exploring what Desired State Configuration is, why
it's useful, and how to utilize it with Ansible to manage your Windows
nodes.

## What is DSC?

So what exactly is Desired State Configuration? It's basically a system
configuration management platform that uses the declarative model; in
other words, you tell DSC the "what", and it will figure out the "how".
Much like Ansible, DSC uses push-mode execution to send configurations
to the target hosts. This is very important to consider when delivering
resources to multiple targets.

This time-saving tool is built into PowerShell, defining Windows node
setup through code. It uses the Local Configuration Manager (which is
the DSC execution engine that runs on each node).

Microsoft fosters a community effort to build and maintain DSC resources
for a variety of technologies. The results of these efforts are curated
and published each month to the Powershell Gallery as the [DSC Resource
Kit](https://github.com/PowerShell/DscResources). If there isn't a
native Ansible module available for the technology you need to manage,
there may be a DSC resource.

## How Do You Use DSC with Ansible?

DSC Resources are distributed as PowerShell modules, which means that it
works similarly to Ansible, just implemented in a different manner. The
`win_dsc` module has been available since the release of Ansible 2.4,
and it can influence existing DSC resources whenever it interacts with a
Windows host.

To use this module, you will need PowerShell 5.1 or later. Once you make
sure that you have the correct version of PowerShell installed on your
Windows nodes, using DSC is as easy as executing a task using the
`win_dsc` module.

Let's look at it in action. For this example we'll ensure a DNS server
is installed, the `xDnsServer` DSC resource module is present, and also
use a couple of the DSC resources under it to define a zone and an A
Record:

```yml
- hosts: Erasmus
  tasks:
  - win_feature:
      name:
      - DNS
      - RSAT-DNS-Server
      state: present
  - win_psmodule:
      name: xDnsServer
      repository: PSGallery
  - win_dsc:
      resource_name: xDnsServerPrimaryZone
      Name: my-arbre.com
  - win_dsc:
      resource_name: xDnsRecord
      Name: test
      Zone: my-arbre.com
      Target: 192.168.17.75
      Type: ARecord
```

Let's walk through what's happening in the above playbook: it starts by
installing the DNS Server on the target, then the `xDnsServer` DSC
resource module is installed. With the DSC resources now installed the
`xDnsServerPrimaryZone` resource is called to create the zone, then the
`xDnsRecord` resource is invoked with arguments to fill in the zone
details for our `my-arbre.com` site. The `xDnsServer` resource is
downloaded from PowerShellGallery.com which has a reliable community for
DSC resources.

Keep in mind that the `win_dsc` module is designed for driving a single
DSC Resource provider to make it work like an Ansible module. It is not
intended to be used for defining the DSC equivalent of a playbook on the
host and running it.

A couple more points to remember:

-   The `resource_name` must be set to the name of a DSC resource
    already installed on the target when defining the task.
-   Matching the case to the documentation is best practices; this also
    makes it easier to tell the difference of DSC resource options from
    Ansible's `win_dsc` options.

## Conclusion

Now you know the basics of how to use DSC for your Windows nodes by
invoking the win_dsc module in an Ansible Playbook. To read more about
Ansible + DSC, check out our official [documentation page](https://docs.ansible.com/ansible/latest/user_guide/windows_dsc.html)
on the topic.

Special thanks to my teammate John Lieske for lots of technical assistance with this post.
And as always, happy automating!
