---
author: Nuno Martins
date: 2022-11-28 00:00 UTC
description: The Collection available on Ansible automation hub as of
  today allows for the management and provisioning of cloud
  infrastructure as code with Terraform within an automation execution
  environment.
lang: en-us
title: Walking on Clouds with Ansible
---

# Walking on Clouds with Ansible

Today is a good day, and when it\'s a day like this we often feel like
we are walking on clouds. With this latest announcement for the newest
Red Hat Ansible Certified Collections available to our customers on the
28th of November, I am sure many cloud practitioners will be
anticipating what the future will bring for their cloud automation. 

Over the last few months, there has been a fair amount of activity in
the Ansible team showing how Red Hat Ansible Automation Platform can
extend and connect different technologies. This has been a crucial
component of Ansible's success in cloud automation for many customers.

![cloud automation uses diagram](/images/posts/archive/cloud-automation-uses.png)

Cloud automation requires the ability to perform many different
complicated tasks and cover just as many domains. Often, organizations
have different technologies to meet specific requirements and needs. One
of the technologies widely used is Terraform.  

We have done a number of blogs recently on the topic, ranging from a
simple example of using Terraform with Ansible Automation Platform,
to in-depth looks at the differences between the tools.
AnsibleFest 2022 even featured a lab where we got to work with Terraform
through automation controller, allowing us to centralize the
provisioning and de-provisioning of cloud infrastructure with Terraform
while running post-provisioning configuration through Ansible.

Traditionally the modules used to work with Terraform have come from the
community, however, with the greater demand for an official Collection
with the backing of Red Hat support, we have announced cloud.terraform,
a Red Hat Ansible Certified Collection for Terraform. 

## So what is the cloud.terraform collection?

This Collection is available on Ansible automation hub as of today and
allows for the management and provisioning of cloud infrastructure as
code with Terraform within an automation execution environment. The
Collection currently contains two modules and example roles to assist
you in bringing your Terraform workloads onto Ansible Automation
Platform in a certified and supported way. 

These modules allow Ansible to apply Terraform plans as well as to
provision and deprovision infrastructure. Currently, we support **AWS**,
**Azure**, and **Google Cloud** as providers for Terraform and we
support **azurerm**, **gcs,** and **s3** as backends. One important note
is that we do not support the local backend for Terraform, and there are
two reasons for this.  Firstly, many practitioners of Terraform agree
that using the local backend is not a best practice to follow in
production, and secondly, since we trigger automation from execution
environments, the local backend storage is not persistent or the same
with each execution. 

Let us have a look at what module usage will look like in an Ansible
Playbook:

**Module:** **cloud.terraform.terraform**

This replaces the current community.general.terraform module for general
functionality.

``` yml
… example:

- name: Apply plan
  cloud.terraform.terraform:
    project_path: "{{ repo_dir }}"
    plan_file: "{{ plan_file }}"
    state: present  # applying a plan doesn't have a switch for this
    # optional config
    state_file: "{{ terraform_options.state_file | default(omit) }}"
    force_init: "{{ terraform_options.force_init | default(omit) }}"
    binary_path: "{{ terraform_options.binary_path | default(omit) }}"
    plugin_paths: "{{ terraform_options.plugin_paths | default(omit) }}"
    workspace: "{{ terraform_options.workspace | default(omit) }}"
    lock: "{{ terraform_options.lock | default(omit) }}"
    lock_timeout: "{{ terraform_options.lock_timeout | default(omit) }}"
    parallelism: "{{ terraform_options.parallelism | default(omit) }}"
```

**Module:** **cloud.terraform.output**

This module allows us to extract values from Terraform state files and
allows you to store them as facts.

``` yml
… example:

- name: Read outputs from state file
  cloud.terraform.terraform_output:
    state_file: "{{ state_file }}"
  register: terraform_output_state_file
  when: state_file is defined

- name: Add hosts from terraform_output
  ansible.builtin.add_host:
   name: "{{ item[mapping_variables.name] }}"
    groups: "{{ item[mapping_variables.group] }}"
    ansible_host: "{{ item[mapping_variables.ip] }}"
    ansible_user: "{{ item[mapping_variables.user] }}"
  loop: "{{ terraform_output.outputs[mapping_variables.host_list].value }}"
  vars:
    terraform_output: "{{ (terraform_output_project_path is success) | ternary(terraform_output_project_path,
terraform_output_state_file) }}”
```

In addition to these modules, the Collection also includes two example
roles to retrieve project files from Git repositories as well as a role
to create the in-memory inventory in the above example. 

## Ansible Automation Platform with Terraform, but why?

Although both Ansible and Terraform can provision infrastructure and
cloud workloads, many customers find themselves using Terraform for its
ease of use with infrastructure as code, however, after provisioning
there is a gap in the Terraform tooling. Being able to use Ansible
allows us to address this and bring a fully automated workflow with both
tools. This also means that customers who have spent time and money
building their Terraform manifests do not need to replace Terraform but
rather allow Ansible Automation Platform to orchestrate the provisioning
as well as configuration management. These tools are better together! 

![tooling diagram](/images/posts/archive/github-platform-terraform.png)

This is just the beginning, but great things are coming!
