---
author: Nuno Martins
date: 2023-03-20 00:00 UTC
description: "We are adding more value to infrastructure as code with an
  addition to the Ansible Certified Content Collection: The Ansible
  provider for Terraform."
lang: en-us
title: Providing Terraform with that Ansible Magic
---

# Providing Terraform with that Ansible Magic

Late last year, we introduced a Red Hat Ansible Certified Collection
Collection for Terraform.
This was an important step in automation, as these two tools really are
great together and leveraging Ansible\'s ability to orchestrate other
tools in the enterprise made this a no-brainer. Terraform with its
infrastructure as code (IaC) provisioning and Ansible's strength in
configuration as code are a synergy that cannot be ignored - we are
better together! Organizations are now in the position to utilize their
existing infrastructure as code manifests and extend their automation
with Terraform and Ansible together.  

Now, we are back [ ]{style="font-size: 11px; color: #000000;"}with help
from our partners at Kyndryl and XLAB and adding more value and magic to
infrastructure as code - This time we have some extra muscle with an
addition to the Red Hat Ansible Certified Content Collection: The
Ansible provider for Terraform.

So what does the provider help us with?

Without a provider, we would need to rely on inventory plugins for the
different cloud platforms and use filters to grab instance information
from our freshly \"Terraformed\" infrastructure. This allows us to
update our inventory so we can run automated tasks against these hosts.
This is pretty smooth in a workflow especially if you are using the
automation controller with a workflow. However, this scenario is not
without complexity, and what about the Terraform users who are not
working with automation controller? How can we leverage Ansible and
bring these two tools together? The Ansible provider for Terraform is
here to help us!

With the Ansible provider in the Collection, we are able to define the
use of an Ansible inventory in the main.tf file and once the project is
initialized and built by Terraform, we can gather Terraform resource
information from the state file and push it into an inventory.

Let's look a bit closer:

``` yml
…main.tf

terraform {
  required_providers {                     #### ansible provider
    ansible = {
      version = "~> 0.0.1"
      source  = "terraform-ansible.com/ansibleprovider/ansible"
    }
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
  }
}
…

resource "ansible_host" "my_ec2" {          #### ansible host details
  name   = aws_instance.my_ec2.public_dns
  groups = ["nginx"]
  variables = {
    ansible_user                 = "ansible",
    ansible_ssh_private_key_file = "~/.ssh/id_rsa",
    ansible_python_interpreter   = "/usr/bin/python3"

  
  
```

[Using the provider in the
]{style="color: #000000;"}[main.tf]{style="color: #000000;"}[ allows us
to indicate that we want to use an Ansible inventory and allows us to
specify Ansible host details for the inventory. Terraform can then
initialize and plan the project and embed the details. If we look at the
resulting Terraform state file we can see host details
defined:]{style="color: #000000;"}

``` yml
…terraform.tfstate                      #### Inside main.tf


"mode": "managed",
      "type": "ansible_host",
      "name": "my_ec2",
      "provider": "provider[\"terraform-ansible.com/ansibleprovider/ansible\"]",
      "instances": [
        {
          "schema_version": 0,
          "attributes": {
            "groups": [
              "nginx"
            ],
            "id": "ec2-18-130-240-228.eu-west-2.compute.amazonaws.com",
            "name": "ec2-18-130-240-228.eu-west-2.compute.amazonaws.com",
            "variables": {
              "ansible_python_interpreter": "/usr/bin/python3",
              "ansible_ssh_private_key_file": "~/.ssh/id_rsa",
              "ansible_user": "ansible"
            }
          },
…

```

[Taking a deeper look at the inventory, we can see that the plugin has
populated instance data from the defined resource in the Terraform state
file.]{style="color: #000000;"}

``` yml
…inventory.yml
---
plugin: cloud.terraform.terraform_provider
```

``` yml
ansible-inventory -i inventory.yml --graph --vars

@all:
  |--@nginx:
  |  |--ec2-18-130-240-228.eu-west-2.compute.amazonaws.com
  |  |  |--{ansible_python_interpreter = /usr/bin/python3}
  |  |  |--{ansible_ssh_private_key_file = ~/.ssh/id_rsa}
  |  |  |--{ansible_user = ubuntu}
  |--@ungrouped:
```

[We are now able to run playbooks against this inventory and automate
the configuration or additional post-provisioning tasks on our hosts
without any hassle.]{style="font-size: 18px; color: #000000;"}

``` yml
Step 1: …terraform plan
Step 2: …terraform apply

…Deploying with Terraform…


Apply complete! Resources: 5 added, 0 changed, 0 destroyed.
++ ansible-playbook -i inventory.yml playbook.yml

PLAY [Install nginx on remote host] *****************************************************************************************

TASK [wait_for_connection] **************************************************************************************************
The authenticity of host 'ec2-18-130-240-228.eu-west-2.compute.amazonaws.com (18.130.240.228)' can't be established.
ECDSA key fingerprint is SHA256:jRqiAGPDzuYGe+l7jNsmQays2qb/C/SJqtnH6pc42ns.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
ok: [ec2-18-130-240-228.eu-west-2.compute.amazonaws.com]

TASK [setup] ****************************************************************************************************************
ok: [ec2-18-130-240-228.eu-west-2.compute.amazonaws.com]

TASK [Install nginx] ********************************************************************************************************
changed: [ec2-18-130-240-228.eu-west-2.compute.amazonaws.com]

TASK [Start nginx] **********************************************************************************************************
ok: [ec2-18-130-240-228.eu-west-2.compute.amazonaws.com]

PLAY RECAP ******************************************************************************************************************
ec2-18-130-240-228.eu-west-2.compute.amazonaws.com : ok=4    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

[This new provider is extremely useful when you are
using]{style="color: #000000;"}[ [Terraform for deployments while
leveraging Ansible for cloud operations like application deployments and
CI/CD pipelines, Lifecycle management and enforcement, OS patching and
maintenance.]{style="font-size: 18px;"}]{style="font-size: 12px; color: #000000;"}[[
]{style="font-size: 18px;"}With this provider being part of the Red Hat
Ansible Certified Content Collection, we also have ongoing maintenance
and support available! ]{style="color: #000000;"}
