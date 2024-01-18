---
author: Sean Cavanaugh
date: 2018-04-16 00:00 UTC
description: Red Hat Ansible Engine can be used to quickly automate
  mitigation of CVEs based on instructions from networking vendors.
lang: en-us
title: Using Ansible to Mitigate Network Vulnerabilities
---

# Using Ansible to Mitigate Network Vulnerabilities

## Even Networks Aren't Immune

Just like with Windows and Linux servers, networking devices can be
exploited by vulnerabilities found in their operating systems. Many IT
organizations do not have a comprehensive strategy for mitigating
security vulnerabilities that span multiple teams (networking, servers,
storage, etc.). Since the majority of network operations is still
manual, the need to mitigate quickly and reliably across multiple
platforms consisting of hundreds of network devices becomes extremely
important.\
\
In Cisco's *March 2018 Semiannual Cisco IOS and IOS XE Software Security
Advisory Bundled Publication*, 22 vulnerabilities were detailed. While
Red Hat does not report or keep track of individual networking vendors
CVEs, [Red Hat Ansible Engine](/products/engine) can be used to quickly
automate mitigation of CVEs based on instructions from networking
vendors.\
\
In this blog post we are going to walk through
[CVE-2018-0171](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-20180328-smi2)
which is titled "Cisco IOS and IOS XE Software Smart Install Remote Code
Execution Vulnerability." This CVE is labeled as critical by Cisco, with
the following headline summary:

> *"\...a vulnerability in the Smart Install feature of Cisco IOS
> Software and Cisco IOS XE Software could allow an unauthenticated,
> remote attacker to trigger a reload of an affected device, resulting
> in a denial of service (DoS) condition, or to execute arbitrary code
> on an affected device."*

##  Gathering Information from Networks

Users leverage Ansible modules to access devices, retrieve information,
execute commands and handle systems using specific keywords. One of the
first things a CVE requires is collection of inventory. To mitigate a
CVE, the networking platform and specific version of code is required.
CVE-2018-0171 affects the IOS and IOS-XE network operating systems and
Ansible can obtain this information easily. Let's use the [ios_facts
module](http://docs.ansible.com/ansible/latest/modules/ios_facts_module.html)
which returns key-value pairs for use in subsequent tasks. For example:
`ansible_net_model` returns the model, and `ansible_net_image` returns
the image file the device is running. For a full list see the ios_facts
module
[documentation](http://docs.ansible.com/ansible/latest/modules/ios_facts_module.html)
page.\
\

```yml
- name: gather facts for ios platforms
  ios_facts:
    gather_subset: all

- name: output facts to terminal window
  debug:
    msg: >
      Device {{ansible_net_hostname}}, model 
{{ansible_net_model}}, running {{ansible_net_version}}            
```

When executing the playbook we get nice output like this:

```yml
ok: [rtr1] => {
    "msg": "Device rtr1, model CSR1000V, running 16.05.02\n"
}
ok: [rtr2] => {
    "msg": "Device rtr2, model CSR1000V, running 16.05.02\n"
}
ok: [switch] => {
    "msg": "Device c3850-1, model WS-C3850-24T, running 16.06.01\n"
}        
```

This allows us to quickly grab useful information about our network, and
check it against Cisco Security Advisory. In a demo on the [GitHub
network-automation
project](https://github.com/network-automation/ansible_inventory_report)
we show how to use network facts to quickly build a nice HTML report.\
\
The vulnerability CVE-2018-0171 specifies that to see if a device is
vulnerable we must run the `show vstack config` command. In my network,
I have three devices running IOS-XE, two are CSR1000V devices, and one
device is a 3850. The two CSR devices don't have the command, while the
3850 switch does. To make my playbook robust enough to handle errors
when a command doesn't exist, I can use the `ignore_errors` parameter.
Otherwise, the playbook would fail and exit when a target network node
doesn't have the ability to use that command. Alternatively, I could run
the playbook only on switches by [using a
limit](http://docs.ansible.com/ansible/devel/user_guide/playbooks_best_practices.html#top-level-playbooks-are-separated-by-role).
For this example, let's assume we are running the Cisco 3850 which has
the `show vstack config` command.

```yml
- name: run show vstack config
    ios_command:
      commands:
        - show vstack config
    register: showvstack            
```

In the playbook above I used the `register: showvstack`. The
`showvstack` is a user defined term (I chose it, it is not reserved). By
registering this I can use the output from the `show vstack config`
later in the playbook. We can use the debug module to look at the
`showvstack` variable to see how it's formatted:

```yml
ok: [switch] => {
    "showvstack": {
        "changed": false,
        "failed": false,
        "stdout": [
            "Capability: Director | Client\n Oper Mode: Disabled\n Role: NA\n Vstack Director IP address: 0.0.0.0\n\n *** Following configurations will be effective only on director ***\n Vstack default management vlan: 1\n Vstack start-up management vlan: 1\n Vstack management Vlans: none\n Join Window Details:\n\t Window: Open (default)\n\t Operation Mode: auto (default)\n Vstack Backup Details:\n\t Mode: On (default)\n\t Repository:"
        ],

<<rest of output removed for brevity>>
```

There is a stdout and a stdout_lines. To read more on the common return
values refer to the
[documentation](http://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#stdout).
Next, we will use my new favorite module, the [assert
module](http://docs.ansible.com/ansible/latest/modules/assert_module.html).
This enables us to check if given expressions are true, failing the task
if they are not. Cisco provides two outputs that we need to check for in
the result of the `show vstack config` command :

`switch1# show vstack config`\
`Role: Client (SmartInstall enabled)`

or

`switch2# show vstack config`\
`Capability: Client`\
`Oper Mode: Enabled`\
`Role: Client`

We can use the assert module to check the text we saved in the
`showvstack` variable:

```yml
- name: Check to make sure Cisco's Smart Install Client Feature is not enabled (1/2)
  assert:
    that:
      - "'SmartInstall enabled' not in showvstack.stdout"
      - "'Role' not in showvstack.stdout"
      - "'Client' not in showvstack.stdout" 
```

Each line in the assert module that is added means there is an implicit
AND, meaning all three need to be true for the task to pass.\
\
Similarly we can check the second statement:

```yml
- name: Check to make sure Cisco's Smart Install Client Feature is not enabled (1/1)
  assert:
    that:
      - "'Oper Mode' not in showvstack.stdout"
      - "'Enabled' not in showvstack.stdout"
      - "'Role' not in showvstack.stdout"
      - "'Client' not in showvstack.stdout"  
```

For this particular CVE it lists that there are no workarounds
available. On some CVEs we could use the ios_command or ios_config
modules to mitigate the CVE based on the instructions the vendor
provided. For this particular CVE it links to the documentation on how
to disable vstack using the command no vstack which could be sent using
the ios_command module. It also recommends for older releases to block
traffic on TCP port 4786, which could be pushed using the ios_config
module. Since no workaround is provided on the CVE, a network operator
needs to make an educated decision based on their environment.
Alternatively, for
[CVE-2018-0150](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-20180328-xesc#workarounds)
there is a workaround provided, and the ios_config could simply send
`no username cisco` to mitigate the CVE.\
\
Red Hat Ansible Engine and Red Hat Ansible Tower can be used to help
network operators and administrators scale repetitive tasks like
checking these dozens of CVEs and make sure their network is safe from
vulnerabilities. On the server side, when system administrators are
using [Red Hat
Insights](https://www.redhat.com/en/technologies/management/insights),
they can automatically [generate
playbooks](https://access.redhat.com/documentation/en-us/red_hat_insights/1.0/html/creating_insights_maintenance_plans_with_ansible_playbook_integration/running_a_playbook#running_ansible_playbook)
for Red Hat Enterprise Linux to help with vulnerabilities and
proactively identify threats to security, performance, and stability.
Ansible can be the common way to execute tasks across your entire IT
infrastructure.
