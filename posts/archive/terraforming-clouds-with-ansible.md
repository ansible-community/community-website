---
author: Nuno Martins
date: 2022-07-11 00:00 UTC
description: Many organizations use Terraform for quick infrastructure
  provisioning every day, but if we combine it with the power of
  Ansible, we can see that it builds into an efficient workflow.
lang: en-us
title: Terraforming Clouds with Ansible
---

# Terraforming Clouds with Ansible

![](https://lh3.googleusercontent.com/0qRLHuyDCJxCaBytGMpe-OzQtssgb_HcBjlh_ytyjsxw8wMP-0nmgzZDbLmFbfr7usCP3dttppu44NYWTeJveZS2lY17wlQ6itxDi8CKve-DQIg5HAxfQwSusrnB_9xSHtuA78ixeTlH4EHGsw){width="624"
height="229" loading="lazy"}

The wheel was invented in the 4th millennium BC. Now, in the 4th
millennium, I am sure the wheel was the hottest thing on the block, and
only the most popular Neolithic cool cats had wheels. Fast forward to
the present day, and we can all agree that the wheel is nothing really
to write home about. It is part of our daily lives. The wheel is not
sexy. If we want the wheel to become sexy again we just need to slap a
sports car together with all the latest gadgets and flux capacitors in a
nice Ansible red, and voilà! We have something we want to talk about. 

Like the sports car, Red Hat Ansible Automation Platform has the same
ability to turn existing resources into something a bit more intriguing.
It can enhance toolsets and extend them further into an automation
workflow. 

[Let\'s take Terraform. Terraform is a tool used often for
infrastructure-as-code. It is a great tool to use when provisioning
infrastructure in a repeatable way across multiple large public cloud
providers like Amazon Web Services (AWS), Microsoft Azure, and Google
Cloud Platform (GCP). Many organizations use Terraform for quick
infrastructure provisioning every day, but if we combine it with the
power of Ansible, we can see that it builds into an efficient
workflow. ]{style="color: #202124;"}

# Don't replace tooling - reuse, enhance and master it

As I said, Ansible has a way of enhancing existing tools and giving them
an overhaul. If an organization already uses Terraform, it would be a
shame to waste all of the man-hours used in building their manifests and
configurations. Instead, we can use what we have to create a workflow
that builds more Terraform manifests, automates the provisioning, and
provides a scalable method of triggering post-provisioning tasks. With
Ansible taking the lead, we are able to extend the infrastructure
provisioning with Terraform and allow for things like
configuration-as-code, application deployment, and compliance
automation. The list of possibilities is as endless as accessories on
the latest German car. 

The first thing to consider is the automation execution environment we
will need when using Terraform as part of our automation. Our execution
environment needs to be able to perform Terraform tasks, therefore we
need to make sure that Terraform is actually running on the execution
environment.

I did this by downloading the binaries and simply copying them into a
basic execution environment. 

I also embedded a keep_secrets file which we will use with Ansible
vault.

``` yml
[---
version: 1

build_arg_defaults:
    EE_BASE_IMAGE: < BASE EE > 

dependencies:
  galaxy: requirements.yml
  python: requirements.txt
  system: bindep.txt

additional_build_steps:
  prepend: |
    ADD terraform /sbin
    ADD keep_secrets /opt 
  append:
    - RUN echo This is a post-install command!
    - RUN ls -la /etc
```

Once I have pushed my execution environment to my p[rivate automation
hub](https://www.ansible.com/blog/the-ansible-cookie-magic-in-the-middle),
we are ready to get building! 

I\'m going to work on provisioning with Terraform with a simple use case
using three files:

  ----------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  main.tf           This holds all the configuration information I need for my infrastructure
  variables.tf      This will hold all the variables I use and reference in my main.tf file
  cloud-init.conf   I use the cloud-init to inject configuration information, such as users to create and ssh keys to add to authorized_keys - so my automation controller can connect and do its magic. 
  ----------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

All the components we need to deploy cloud infrastructure are part of
these manifests - this is our infrastructure-as-code. Using Terraform to
deploy them allows us to also destroy all the provisioned infrastructure
quickly and easily. This can be beneficial by not leaving any
configuration artifacts on your cloud platform and speeding up the whole
life cycle. 

To create these manifests we can use Jinja templates and use surveys in
our automation workflows. A survey in Ansible Automation Platform allows
us to present consumers of automation with the opportunity to input data
that we can use inside of our automation.  

![](https://lh6.googleusercontent.com/Unia0m2SLZyGJngh-oD6Hvqt17OpC2z1wL3o6OZuZEWmmddD6j2PA0fkB4jkUe8M6a9OO08deqgFOn_7BxMhS1Qb3G56asluEvhg2-XOJQ95gF8FtfJlgtLioyf602CIS2H0zUXozaw8tA7W4A){width="624"
height="424" loading="lazy"}

 

This means creating all the infrastructure-as-code components really
becomes a dynamic mechanism for our teams, making the process even
easier. With the Jinja templates, I create the variable manifest, and
the main.tf will then use all of those components to build and plan the
deployment. 

``` yml
…main.j2 > Summarized Example


resource "aws_instance" "ioc_basic" {
  for_each      = data.aws_subnet_ids.production.ids
  ami           = "${var.ami_number}"
  instance_type = "${var.instance_type}"
  subnet_id     = each.value
  key_name   = "${var.terraform_prov}"
  user_data = file("./cloud-init.conf")
  tags = {
      Name = "${var.instance_names}"
…
```

 

``` yml
… variables.j2 > Summarized Example


variable "ami_number" {
  default = "{{ ami_number }}"
}
variable "secret_key" {
  default = "{{ secret_key }}"
}
variable "instance_names" {
  default = "{{ instance_names }}"
}
variable "instance_type" {
  default = "{{ instance_type }}"
}
…
```

# Provision Infrastructure

![](https://lh3.googleusercontent.com/50gTNDXmh8QO--5DX541r6rdERrozzZ5uGnJlxBV1zfcBfyuEhVSVU6ctrNCfLN-LJHS2kjBI5Js8_WcQrXRIgeEQZ364GvW2HTtz1d6v_wHTOtiokiBIVBAaZxQCD9ZPRtisf3JqIzuTplmCw){width="570"
height="444" loading="lazy"}

With the survey data provided, we can get Ansible to create a project
folder for Terraform to work with. This should be stored in a source of
truth, for my example, I am using a Git repository. Once we have our
project folder, we will create all the manifests and configurations we
need for Terraform to build and deploy the infrastructure. Ansible
Automation Platform has modules we can use to trigger all the Terraform
actions from our playbooks, and it will trigger Terraform to initialize
this project folder during its build process to make sure it installs
the correct provisioner. 

I am currently working on AWS; however, if you wanted to provide access
to multiple providers for Terraform to use, this would be as simple as
creating a Jinja2 template for it and giving your users the option in a
workflow survey. In our playbook, we can now just use a Terraform module
to trigger the initialization, planning, and deployment of the IoC
manifest.

``` yml
- name: Creating Terraform IoC
  block:
   - name: Initialize Terraform Provider
     community.general.terraform:
       project_path: /{{ working_dir }}/{{  my_terraform_build }}
       state: absent
       force_init: true
    
    - name: Deploy Terraform Instance
      community.general.terraform:
        project_path: /{{ working_dir }}/{{ my_terraform_build }}
        state: present
      register: deployed_tf
```

Once Terraform deploys the infrastructure, it creates a state file that
is used to store your managed infrastructure configuration and map
resources. If we want to modify infrastructure, we will reuse the state
file. However, it can also be used as a source of information about that
instance for post-provisioning tasks. If we need to make a change to a
load balancer, for example, this file is a simple source of information
we can harness. Since our execution environments are ephemeral, we will
push these state files to our build repository once we have encrypted
them.

Now, Terraform is great at creating infrastructure as well as destroying
it. It simplifies the whole process and does a good job of cleaning
things up. We will need the variables manifest used to de-provision our
infrastructure, so It is best that we put these and our state files in
our build repository to not only be able to destroy the instance later,
but to also be able to reuse this configuration or modify the
infrastructure. Since these files will have sensitive information, we
can use Ansible to encrypt these files before we push them to our source
of truth using the secrets file we embedded in our execution
environment. 

# The wheels are turning, but now what?

Ansible Automation Platform allows us to use [dynamic inventory
plugins](https://www.ansible.com/blog/configuring-an-aws-dynamic-inventory-with-automation-controller),
so we will use the relevant plugin to allow us to update the inventory
to accommodate our newly provisioned host. One of the really cool things
here is that we can provide the tags we want in our Terraform manifest
files, and in Ansible we can narrow our inventory hosts with filters
looking specifically at these tags. 

``` yml
— example

regions:
  - "eu-west-2"

keyed_groups:
  - tag:Environment: terraform_dev

filters:
  instance-state-name: running
```

These filters in our dynamic inventory source allow the automation
controller to harvest just the instances that match these criteria and
simplify further tasks post provisioning. The last part of the
provisioning process is to create and update a survey for the
termination of the instance we created. To do this, we use Ansible to
create a listing of all the projects in our Terraform repository, and we
can pass this on to create a survey specification, which we update
whenever we run a create or destroy job. 

# Destroy Infrastructure

![](https://lh3.googleusercontent.com/YLLtlNYMkHXUVi27tn9dBnW4ml5VOTWYfQ0GOioE_9DUIUfl-8AqgZlqpCDrgOm-y8yxs2YfHOrKe7q25NOJEVvY_I8fvjMc-m0I1dvAib9Mm8IV40Ic5dBXl1tIN_tU08eJ7YJ_nTSgHB6JsQ){width="540"
height="370" loading="lazy"}

Since we used Terraform to provision our infrastructure, de-provisioning
it, is pretty straightforward. As I mentioned before, when Terraform
creates the infrastructure, it establishes a source of truth that can be
used as an easy way to de-provision infrastructure. We can use our
automation workflow to grab the correct Terraform build details from our
repository, make changes to any external systems that might be affected,
like load balancers, and then trigger Terraform to destroy the instance
it created from our playbook. 

``` yml
 - name: Destroy Terraform Instance
          community.general.terraform:
            project_path: /{{ working_dir }}/{{ my_terraform_build }}
            state: absent
```

# Start your engines! Post-provisioning

[We have created a renewable method of building and destroying
infrastructure using Ansible and Terraform. To extend the automation
further and do the important work of deploying workloads, system
hardening, and compliance, we only need to rely on Ansible. Ansible
Automation Platform allows us to create automation workflows that show
us a visual logical progression of the steps in automation and allow us
to combine tasks in an end-to-end process. Not only is this a great way
to view and inspect your automation process, but I find it beneficial in
pinpointing possible improvements or perhaps adding rollback features to
the process should a step fail or encounter
issues. ]{style="color: #000000;"}

[![](https://lh3.googleusercontent.com/1b8E18L_NMzSjL3CT2EQz9YIJOlYC434NF1Er1Ep07eRdpGZuQILf5TsV_Ns3SXaak8G_DxbAG7lZfhuco63m_-294Da0BZhDdAxTa3R1tKFYlGqCzjA4SKSlrEegGplBhdT3if_smPNuM06Sg){width="624"
height="167" loading="lazy"}]{style="color: #000000;"}

Time to Terraform your clouds bringing infrastructure-as-code and
configuration-as-code together with our centralized Ansible Automation
Platform!
