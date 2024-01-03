---
author: Sumit Jaiswal
date: 2020-06-29 00:00 UTC
description: Security professionals are increasingly adopting automation
  as a way to help unify security operations into structured workflows
  that can reduce operational complexity, human error, time to respond
  and can be integrated into existing SIEM or SOAR
lang: en-us
title: Ansible security automation resource modules
---


# Ansible security automation resource modules

Security professionals are increasingly adopting automation as a way to
help unify security operations into structured workflows that can reduce
operational complexity, human error, time to respond and can be
integrated into existing SIEM (Security Information and Event
Management) or SOAR (Security Orchestration Automation and Response)
platforms.

In October of 2019 the Ansible network automation team
[introduced the concept of resource modules](https://www.ansible.com/blog/network-features-coming-soon-in-ansible-engine-2.9):

So what exactly is a "resource module?" Sections of a device's
configuration can be thought of as a resource provided by that device.
Network resource modules are intentionally scoped to configure a single
resource and can be combined as building blocks to configure complex
network services.

Keep in mind that the first network automation modules could either
execute arbitrary commands on target devices, or read in the device
configuration from a file and deploy it. These modules were quite
generic and provided no fine-tuning of certain services or resources.

In contrast, resource modules can make network automation easier and
more consistent for those automating multiple platforms in production by
avoiding large configuration file templates covering all kinds of
configuration. Instead they focus on the task at hand, providing
separate building blocks which can be used to describe complex
configurations.

The same principle can be applied in the security space, and we started
exploring the possibility with Ansible security automation.

# Resource modules in security automation

In security automation, many Collections already have more refined
modules targeting use cases or workflows of the corresponding target
environment. Therefore, there is little standardization or generic
abstraction in terms of product agnostic resources.

For example, if you have a closer look at our
[investigation enrichment blog post](https://www.ansible.com/blog/getting-started-with-ansible-security-automation-investigation-enrichment),
you will see that while we used a certain amount of modules, those were
usually very product specific and didn't offer much in terms of generic
resources.

At the same time, security automation does cover many tasks where
resource modules can add a lot of value. Whether it is granting and
denying access to networks via Access Control Lists (ACLs) or policies,
the management of rules in IDPS systems or the log forwarding of nodes
to a central SIEM: all those tasks are often executed on a well-defined
resource across multiple products, which makes these tasks good
candidates to be helped by resource modules.

# Security automation resource modules for Access Control Lists

Following this line of thought we have started to introduce ACLs
resource modules within Ansible. ACLs can help provide a first layer of
security when applied to interfaces, or globally as access rules, as
they permit or deny traffic flows in firewalls.

Within an ACL the order of Access Control Entries (ACEs) are crucial
since based on the ACEs sequence/order, appliances decide whether
traffic is allowed or not. Given this background, an ACL resource module
provides the same level of functionality that a user can achieve when
manually changing the configuration on a corresponding device. However,
the ACL resource module comes with the advantages of Ansible:

-   Automating things using Ansible can accelerate the time to become
    productive.
-   Ansible is powerful and users can automate a wide variety of tasks, 
    at both the user or enterprise level. This helps to orchestrate the
    complete app lifecycle including the ACLs, and makes the security
    automation part of the app deployment process and the entire
    technical business process.
-   Ansible has agentless architecture which uses the native
    communication protocols of the managed target nodes. This avoids the
    need to introduce and install new software and new security
    protocols in the managed environments.
-   Last but not least, with the help of Ansible's fact gathering, the
    data structures of managed nodes can be collected and made
    accessible in an efficient manner.

Please note that the naming convention for the new ACL resource modules
uses the plural form instead of singular: "acls" instead of "acl". If
the platform you're automating has modules with both names, the plural
form of the module is the newer one corresponding to the resource module
initiative. The singular form of the module will likely be deprecated in
a future release. This distinction was introduced to ease the transition
to resource modules and avoid disruption of the current automated
workflows.

# Example: Cisco ASA ACLs

A good way to understand the new ACLs resource modules is via an
example. For this, let's have a look at the
[Cisco ASA Collection](https://cloud.redhat.com/ansible/automation-hub/cisco/asa)
which targets the Cisco Adaptive Security Appliance family of security
devices. In this Collection you will find a module called `asa_acls` which
is the resource module to manage named or numbered ACLs on ASA devices.

As an example, let's first check the current documentation. For that, we
can use the capability of the module to gather the existing ACLs
configuration:

```
---
- name: Get structured data
  hosts: cisco
  gather_facts: false
  collections:
   - cisco.asa

  tasks:
  - name: Gather facts
    asa_acls:
      state: gathered
      register: gather
  - name: output data
    debug:
      vars: “{{ gather }}”
```

The output will be something along the lines of:

```
- acls:
   - aces:
       - destination:
           address: 192.0.3.0
           netmask: 255.255.255.0
           port_protocol:
                 eq: www
         grant: deny
…
```

Note that the output generated this way is purely focused on the
resource at hand - ACLs. This is in contrast to a generic fact gathering
wheremore data is provided, making it difficult to keep an overview and
handle the data subsequently.

Given the configuration at hand, let's assume for the sake of this
example that we analyze the gathered configuration, and want to make a
change to it. The next configuration looks like:

```
- acls:
  - name: global_access
    acl_type: extended
    aces:
    - grant: deny
      line: 1
      protocol_options:
        tcp: true
      source:
        address: 192.0.4.0
        netmask: 255.255.255.0
        port_protocol:
          eq: telnet
      destination:
        address: 192.0.5.0
        netmask: 255.255.255.0
        port_protocol:
          eq: www
```

This configuration describes that access from a defined source to a
target is denied. Note that this entire definition is mostly product
agnostic and can be used with other systems as well.

Given this description is available as the variable acls this can be
deployed with the cisco_acls module:

```
---
- name: Replace ACLs device configuration
  hosts: cisco
  gather_facts: false
  collections:
   - cisco.asa

  tasks:
  - name: Replaces device configuration of listed acls
    asa_acls:
      config: “{{ acls }}”
      state: replaced
```

As you see it is possible to apply an existing resource description to
an existing device. Resource modules allow the user to read in existing
configuration and convert that into a structured data model. These data
models can be used as a base to further deploy changed configuration on
the target nodes.

# Takeaways

Security professionals are in need of unification of their operational
workflows. Automation helps - even more so if the platform it is running
on provides a simpler means to control otherwise rather complex
structures. The Ansible security automation resource modules provided
are a building block in standardizing automation actions.
