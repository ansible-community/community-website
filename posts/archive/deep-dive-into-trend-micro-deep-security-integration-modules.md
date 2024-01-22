---
author: Sumit Jaiswal
date: 2021-04-21 00:00 UTC
description: Deep dive on Trend Micro Deep Security automation modules,
  collections and Ansible integration.
lang: en-us
title: Deep dive into Trend Micro Deep Security integration modules
---

# Deep dive into Trend Micro Deep Security integration modules

At AnsibleFest 2020, we announced
the extension of our security automation initiative to support endpoint
protection use cases. If you have missed it, check out the recording of
the talk "Automate your endpoint protection using Ansible" on the
AnsibleFest page.

Today, following this announcement we release the supported Ansible
Content Collection for Trend Micro Deep Security. We will walk through
several examples and describe the use cases and how we envision the
Collection being used in real world scenarios.

## About Trend Micro Deep Security

Trend Micro Deep Security is one of the latest additions to the Ansible
security automation initiative. As an endpoint protection solution it
secures services and applications in virtual, cloud and container
environments. It provides automated security policies and consolidates
the security aspects across different environments in a single platform.

## How to install the Certified Ansible Content Collection for Trend Micro Deep Security

The Trend Micro Deep Security Collection is available to Red Hat Ansible
Automation Platform customers at [Automation
Hub](https://cloud.redhat.com/ansible/automation-hub), our
software-as-a-service offering on
[cloud.redhat.com](https://cloud.redhat.com/) and a place for Red Hat
subscribers to quickly find and use content that is supported by Red Hat
and our technology partners.

The blog post "Getting Started with Automation Hub"
gives an introduction to Automation Hub and how to configure your
Ansible command line tools to access Automation Hub for Collection
downloads.

Once that is done, the Collection is easily installed:

```bash
ansible-galaxy collection install trendmicro.deepsec
```

## What's in the Ansible Content Collection for Trend Micro Deep Security?

The focus of the Collection is on modules and plugins supporting them:
there are modules for interacting with Trend Micro Deep Security agents,
like `deepsec_firewallrules`, `deepsec_anti_malware`, `deepsec_log_inspectionrules` and
others. Basically the integration modules cover the REST APIs exposed by
TM Deep security firewall.  If you are familiar with firewall
Collections and modules of Ansible, you will recognize this pattern: all
these modules provide the most simple way of interacting with endpoint
security and firewall solutions. Using those, general data can be
received, arbitrary commands can be sent and configuration sections can
be managed.

While these modules provide a great value for environments where the
devices are not automated at all, the focus of this blog article is on
the endpoint security use-cases where  modules in the respective
Collection can help automate. Being modules they have a precise scope,
but enable users of the Collection to focus on that particular
resource/REST API scenario without being disturbed by other content or
configuration items. They also enable a simpler cross-product automation
since other security Collections follow the same pattern.

## Connect to Trend Micro Deep Security, the Collection way

The Collection supports **httpapi** as a connection type.

Trend Micro Deep security currently supports two ways for how their REST
API can be interacted with, and for each of the respective cases, the
Ansible inventory will be changed slightly as mentioned below:

In case of the [newer REST APIs](https://automation.deepsecurity.trendmicro.com/article/fr/api-reference/)
the Ansible inventory will work with the network OS `trendmicro.deepsec.deepsec`, a Trend Micro API secret key and ab api-version key:

```ini
[deepsec]
host_deepsec.example.com

[deepsec:vars]
ansible_network_os=trendmicro.deepsec.deepsec
ansible_httpapi_use_ssl=true
ansible_httpapi_validate_certs=false
ansible_connection=httpapi
ansible_python_interpreter=/usr/bin/python
ansible_httpapi_session_key={'api-secret-key': 'secret-key', 'api-version': 'v1'}
```

In case of APIs using the [legacy REST APIs](https://automation.deepsecurity.trendmicro.com/legacy-rest/12_5/index.html?env=onprem#overview), the Ansible inventory will also require the network OS `trendmicro.deepsec.deepsec`, but uses a username and a password.

```ini
[deepsec]
host_deepsec.example.com

[deepsec:vars]
ansible_network_os=trendmicro.deepsec.deepsec
ansible_user=admin
ansible_httpapi_pass=password
ansible_httpapi_use_ssl=true
ansible_httpapi_validate_certs=false
ansible_connection=ansible.netcommon.httpapi
ansible_python_interpreter=python
```

Note that in a productive environment those variables should be
supported in a secure way, for example, with the help of
[Red Hat Ansible Tower credentials](https://docs.ansible.com/ansible-tower/latest/html/userguide/credentials.html#network)

## Use Case: Firewall Rule Configuration

A firewall is highly flexible and users can configure it to be
restrictive or permissive. Like the intrusion prevention and web
reputation modules, firewall policies are based on two principles:
either they can permit any service unless it is explicitly denied or
they deny all services unless explicitly allowed.

For example, using Ansible and Trend Micro Deep Security integration,
modules users can take a restrictive firewall approach. This is often
the recommended practice from a security perspective: All traffic is
stopped by default and only traffic that's explicitly allowed is
permitted.

A playbook to implement the "deny all traffic" approach is shown in the
following listing:

```yaml
---
- name: Deny all traffic
  hosts: deepsec
  collections:
   - trendmicro.deepsec
  gather_facts: false
  tasks:
   - name: Create Restrictive firewall rule
     trendmicro.deepsec.deepsec_firewallrules:
       state: present
       name: deny_all_firewallrule
       description: Deny all traffic by default over tcp
       action: deny
       priority: "0"
       source_iptype: any
       destination_iptype: any
       direction: incoming
       protocol: tcp
       tcpflags:
         - syn
```

Running this play will create a firewall rule that'll explicitly
**deny** all TCP **syn** bound traffic. Keep in mind that the
`state` keyword is used and set to `present`. It means
that the specified rule is created and that the module will go ahead and
create the config rule. On the contrary, if the user wants to
delete/drop any specific firewall rule, then the `state` should be
set to `absent`: in that case, during the play run, the module will
check if the specified firewall rule pre-exists and if so the module
will go ahead and delete/drop the respective firewall rule config.

## Use Case: Antimalware Rule Configuration

Antimalware config helps agents on computers by providing real-time and
on-demand protection against a variety of file based threats including
malware, viruses, trojans and spyware. Using Ansible deepsec antimalware
config module, users can fire all types of available scans:

-   Real-time scan
-   Manual scan
-   Scheduled scan
-   Quick scan

The playbook example we'll be discussing here will be with respect to
real time scans as based on incident responses. Users can check for the
threats and quarantine the observed threats.

```yaml
---
- name: Scan and Quarantine in TrendMicro agents
  hosts: deepsec
  collections:
   - trendmicro.deepsec
  gather_facts: false
  tasks:
   - name: Create AntiMalware config
     trendmicro.deepsec.deepsec_anti_malware:
       name: scan_real_time
    description: scan and quarantine via anti-malware config
    scan_action_for_virus: pass
    alert_enabled: true
    scan_type: real-time
    real_time_scan: read-write
    cpu_usage: medium
       scan_action_for_virus: quarantine
       scan_action_for_trojans: quarantine
       scan_action_for_cve: quarantine
       scan_action_for_other_threats: quarantine
    state: present
```

The playbook listed above will create an antimalware config rule, which
will initiate a real-time scan over Trend Micro agents every time
there's a file received, copied, downloaded or modified. 

All files will be scanned for any security threats. If during the scan
the agents detect any threat based on virus, trojans, cve's and others,
the agents will display the information with respect to the infected
file and the respective files will be quarantined as specified in the
playbook.

## Use Case: Log Inspection Rule Configuration

The log inspection integration module helps users to identify events
that are generally logged at system/OS level. It also includes
application logs. Using the log rule configuration, users can forward
the logged events to the SIEM system or to some centralized logging
server for analytics, reporting and archiving.

Log inspection helps in real-time monitoring of third parties log files
as well. The playbook listed below creates a rule for log inspection.

```yaml
---
- name: Set up log inspection
  hosts: deepsec
  collections:
   - trendmicro.deepsec
  gather_facts: false
  tasks:
   - name: Create a Log inspection rule
     trendmicro.deepsec.deepsec_anti_malware:
       state: present
       name: custom log_rule for mysqld event
       description: some description
       minimum_agent_version: 6.0.0.0
       type: defined
       template: basic-rule
       pattern: name
       pattern_type: string
       rule_id: 100001
       rule_description: test rule description
       groups:
         - test
       alert_minimum_severity: 4
       alert_enabled: true
       log_files:
         - location: /var/log/mysqld.log
           format: mysql-log
     register: log
```
