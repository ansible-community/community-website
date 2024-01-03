---
author: Elle Universal
date: 2022-05-19 00:00 UTC
description: Learn what is new after Summit 2022 with automation at the
  edge.
lang: en-us
title: Automation at the Edge, Summit 2022
---

# Automation at the Edge, Summit 2022

As some of you may know, Red Hat Summit was back in person in Boston
last week. For those who are not familiar, Red Hat Summit is the premier
enterprise open source event for IT professionals to learn, collaborate,
and innovate on technologies from the datacenter and public cloud to the
edge and beyond. Red Hat made a lot of exciting announcements, with
several that included Red Hat Ansible Automation Platform.
If you could not make the event or would like to revisit some of the
content, you can access any session [on demand](https://www.redhat.com/en/summit). 

One of the big
[announcements](https://www.redhat.com/en/about/press-releases/red-hat-unveils-new-levels-security-software-supply-chain-edge)
at Summit was the unveiling of new levels of security from the software
supply chain to the edge. In Ansible Automation Platform 2.2, Red Hat is
introducing a technical preview of Ansible content signing technology.
The new capability helps with software supply chain security by enabling
automation teams to validate that the automation content being executed
in their enterprise is verified and trusted. 

With the announcement of this new edge capability, we showcased a
session for Ansible and edge that is available on demand. The session
["GitOps your distributed edge computing model with Red Hat Ansible Automation Platform"](https://events.experiences.redhat.com/widget/redhat/sum22/SessionCatalog22/session/1640789672821001p0oM)
covers how Ansible Automation Platform, in combination with GitOps, can
decrease the time to market and repair time to deploy and operate
network edge infrastructure. It includes a demo that shows how to
describe a deployment in Git, which works as a single source of truth.
You will be able to see how Ansible Automation Platform enforces the
correct state of the network infrastructure of a large-scale
organization and its tracking through IT Service Management. 

Scaling automation anywhere using Ansible Automation Platform
[Red Hat introduced new cross-portfolio edge capabilities](https://www.redhat.com/en/about/press-releases/red-hat-introduces-new-cross-portfolio-edge-capabilities),
including features in Ansible Automation Platform that solves the
management and automation needs to drive visibility and consistency
across an organization's edge deployments. 

The session ["Ansible Automation Platform 2 automation mesh-starting locally, scaling globally"](https://events.experiences.redhat.com/widget/redhat/sum22/SessionCatalog22/session/1641398142450001vmkJ)
covers how to scale automation to successfully execute in distributed
edge locations. 

# Automating RHEL at the edge with Ansible

If you watched the keynote presentation, you heard about the release of
a [SaaS Edge Manager](https://www.redhat.com/en/about/press-releases/red-hat-introduces-new-cross-portfolio-edge-capabilities).
However, we realize not everyone can use the cloud to manage their
fleet. Below is how to add a postscript to your kickstart file to
register your devices directly to an Ansible Automation Platform
inventory so you can use it to manage your fleet.

```
%post
# Create ansible playbook to register device to Ansible automation platform
cat > /tmp/add_to_aap.yml <<EOF
---
- hosts: localhost
 vars:
   aap_url=https://AAPHOST.fqdn.com/api/v2/inventories/CHANGEME/hosts/
   aap_username=changeme
   aap_password=changeme
 gather_facts: true
 tasks:
   - name: create hostname from regex of mac address
     ansible.builtin.set_fact:
       edge_hostname: "{{ ansible_default_ipv4.macaddress | replace(':','') }}"
   - name: set hostname to mac ansible_all_ipv4_address
     ansible.builtin.hostname:
       name: "summit-demo-{{ edge_hostname }}"
       use: systemd
   - name: Update Ansible Tower inventory
     uri:
      url: "{{ aap_url }}"
      user: "{{ aap_ks_user }}"
      password: "{{ aap_ks_password }}"
      method: POST
      body:
        name: "{{ ansible_hostname }}"
        variables: '{ipaddress: "{{ ansible_all_ipv4_addresses }}", macaddress: "{{ ansible_default_ipv4.macaddress }}" }'
      force_basic_auth: yes
      status_code: 201
      body_format: json
      validate_certs: no
EOF
ansible-playbook /tmp/add_to_aap.yml
%end
```

## Step 1: Inventory creation

-   Create the inventory in Ansible Automation Platform, and get the
    inventory number.

    ![](https://lh4.googleusercontent.com/62Uvhz3AZ5z2RN6n17q5NzYAqfnb7JVpMzfw505slI6EvJyt1YBGJnIzq0jaJb4I9RhCzjhMueg1OkjFgwqjhzQAFV_NzV-sZromZq7maniyaCRvYimNuhKJGiWuZsCOP5nGhNinLV89L2Pr1w){width="312"
    height="116" loading="lazy"} 

-   [Get the URL: in this example, the inventory ID is 2:
    ]{style="font-size: 18px;"}

    [![](https://lh5.googleusercontent.com/Pt8Umgqdnc9AilqHT0mZaIZEV9mlKFAjgA6hj7E13aXYDI0cUtIvu5vK5OUofw4RwdqScEoe-zEWBxVrMdWq3IgoRRwOnnQDNluu6d6G35Kn9HvUMV6bEfLi3nMxGpLi09aKlo3uoBQUSGMzGQ){width="624"
    height="84" loading="lazy"}]{style="font-size: 12px;"}

    [[https://AAPHOST.fqdn.com/#/inventories/inventory/**[2]{style="color: #ee0000; text-decoration: underline;"}**[/details]{style="color: #ee0000; text-decoration: underline;"}](https://aaphost.fqdn.com/#/inventories/inventory/2/details){style="color: #ee0000;"}]{style="font-size: 18px;"}

 

-   Assign aap_url in vars section:\
    [aap_url ]{style="color: #569cd6; background-color: #1e1e1e;"}[=
    ]{style="color: #569cd6; background-color: #1e1e1e;"}[<https://AAPHOST.fqdn.com/api/v2/inventories/2/hosts/>]{style="color: #569cd6; background-color: #1e1e1e;"}

## Step 2: Create credentials in Ansible Automation Platform

-   Assign credentials to aap_ks_user and aap_ks_password in the Access Users tab in Ansible Automation Platform.


## Step 3: Check Ansible Automation Platform

-   You should now see your devices in Ansible Automation Platform after
    they boot up.

[![](https://lh4.googleusercontent.com/EQ_LvWTcDa33BJW_MqFzG7nCXRA5oE8e00azOoyK6z976Fgb6h9MWWf4bHsL_E_yIkb0sMkoXHDrCyjoS2Oo6GBxm5diLNiptzwABY5swo4HOHNKMM6fDL7P28rISmNaxmUZKkXfMMTvJ9Jmkg){width="226"
height="226" loading="lazy"}]{style="font-size: 11px;"}
