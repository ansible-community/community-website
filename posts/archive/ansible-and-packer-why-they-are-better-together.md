---
author: Sean Cavanaugh
date: 2022-10-03 00:00 UTC
description: This blog covers how we at Ansible use Ansible to
  orchestrate a pipeline for demos and workshops and how we integrate
  that with custom AMIs created with Packer.
lang: en-us
title: Using Ansible and Packer, From Provisioning to Orchestration
---

# Using Ansible and Packer, From Provisioning to Orchestration

Red Hat Ansible Automation Platform can help you orchestrate,
operationalize and govern your hybrid cloud deployments.  In my last
public cloud blog, I talked about [Two Simple Ways Automation Can Save
You Money on Your AWS
Bill](https://www.ansible.com/blog/two-simple-ways-automation-can-save-money-on-aws)
and similarly to Ashton's blog [Bringing Order to the Cloud: Day 2
Operations in AWS with
Ansible](https://www.ansible.com/blog/bringing-order-to-the-cloud-day-2-operations-in-aws-with-ansible),
we both wanted to look outside the common public cloud use-case of
provisioning and deprovisioning resources and instead look at automating
common operational tasks.  For this blog post I want to cover how the
Technical Marketing team for Ansible orchestrates a pipeline for demos
and workshops with Ansible and how we integrate that with custom AMIs
(Amazon Machine Images) created with [Packer](https://www.packer.io/). 
Packer is an open source tool that allows IT operators to standardize
and automate the process of building system images.

For some of our [self-paced interactive hands-on labs on
Ansible.com](https://red.ht/ansible_labs), we can quickly spin up images
in seconds.  In an example automation pipeline we will:

1.  Provision a virtual instance.
2.  Use Ansible Automation Platform to install an application; in my
    case, I am literally installing our product Ansible Automation
    Platform (is that too meta?).
3.  After the application install, set up the lab guides, pre-load
    automation controller with some job templates, create inventory and
    credentials and even set up SSL certificates.  

While this is fast, it might take a few minutes to load, and web users
are unlikely to be patient.  The Netflix era means that people want
instant gratification!  Installing automation controller might take five
to 10 minutes, so I need a faster method to deploy.

![](https://lh3.googleusercontent.com/uCdkHAIYl2LCg_J7dgkrY_msHqdQRmnl2MPDgVuar20I5j49jnvTDQT1ipgz75b024UBbUzNsTxgXDzr8BWVd35Byjhl4gWP-rAgV6k-Gwq2Bb9XzMrNWROVrrvIfWXF9_WOTx2S1WLaO7-AFCQGP_d1_9mbByp0jxD41JIGAd1x1mRxI-jqEuqURg){

What I can do is combine our normal Ansible automation pipeline with
Packer and pre-build the cloud instances so they already have the
application installed, and are configured and ready to go as soon as it
boots.  Packer will provision a specific machine image on my public
cloud (Azure, AWS, GCP), run the commands and changes I need, and then
publish a new image with all the changes I made to the base image.  In
my case I use Ansible the same way.  In my packer
[HCL](https://www.packer.io/docs/templates/hcl_templates) (HashiCorp
Configuration Language ) file I have an Ansible provisioner:

```json
 provisioner "ansible" {
      command = "ansible-playbook"
      playbook_file = "pre_build_controller.yml"
      user = "ec2-user"
      inventory_file_template = "controller ansible_host={{ .Host }} ansible_user={{ .User }} ansible_port={{ .Port }}\n"
      extra_arguments = local.extra_args

    }
```

Red Hat Ansible Tech Marketing Example can be found on
[Github](https://github.com/ansible/workshops/blob/devel/provisioner/packer/automation-controller.pkr.hcl)

This simple provisioner plugin is executing the Ansible Playbook
pre_build_controller.yml.  I can also use Ansible Automation Platform to
orchestrate the whole process by kicking off Packer and then continuing
on.  Anything that I can do ahead of time, I can pre-build into the
image.  This means there is less automation I need to do at boot time
(or what is sometimes referred to as "automation just in time").  The
new process looks like this diagram:

![](https://lh6.googleusercontent.com/B_20XvdYrI0W6ps4YeEmqWscRVpFqLGYO4UUL8NCdUGPWis3NnLuemS-HL1VWuocn6U7bgGFpCWS_nq5oMEgnOB6DEiIjN4MBAcrDdEwdOVIwR7FamntrktW4BCr8Jesp80DHUVfzQ6ihAsZ8nwO5iVihIXmw6m_n86-Hka7J2c56crDGF2ri7Jh6A){loading="lazy"
width="624" height="197"}


These two processes, building images and serving a demo environment, are
actually independent of each other.  Depending on how often a pre-built
image needs to be executed, we can schedule that in automation
controller, or even generate them on-demand via
[webhooks](https://docs.ansible.com/automation-controller/latest/html/userguide/webhooks.html).
On-demand generation means as soon as someone changes an Ansible
Playbook relevant to anything pre_build, we can have Ansible Automation
Platform create the new image immediately, and even test it!

# Sharing and copying cloud instances

Once we create a pre_built AMI, we need to make sure we can use it in
multiple regions, and on other accounts. With public marketplace
instances you can use cool automation tricks like using the
[ec2_ami_info module](https://docs.ansible.com/ansible/latest/collections/amazon/aws/ec2_ami_info_module.html)
for [dynamic lookups](https://www.ansible.com/blog/find-the-right-ami-everytime-make-your-aws-application-work-in-any-region),
but we have now essentially created private AMIs we can copy to other
regions, or share to other AWS accounts so they have access to these
pre_built images.  To solve this problem we can use automation, and I
have created an Ansible Content Collection for
[ansible_cloud.share_ami](https://galaxy.ansible.com/ansible_cloud/share_ami).  

This Collection currently has two roles available that will assist cloud
administrators, copy and share.

## Copy

This role will copy an AMI from one region, to any other specified
regions.  This means you can use Packer to create it just once, and have
Ansible take care of copying it to any other regions and return you with
a list of new AMIs per region.

```yml
  - name: copy ami
      include_role:
        name: ansible_cloud.share_ami.copy
      vars:
        ami_list: "{{ my_ami_list }}"
        copy_to_regions: "{{ my_copy_to_regions }}"
```

Where your variable file looks like this:

```yml
my_ami_list:
  ap-northeast-1: ami-01334example
  ap-southeast-1: ami-0b3f3example
  eu-central-1: ami-03a5732example
  us-east-1: ami-01da94de9cexample
my_copy_to_regions:
  - us-west-1
  - us-east-2
```

In this case, there will be four AMIs copied to us-west-1 and us-east-2
with a new AMI identifier returned to your terminal window or the
automation controller console.

## Share

This role will share an AMI
from one account and region to another account (in the same region). 
This allows you to share your pre_built AMIs to as many accounts as you
want really quickly.

```yml
    - name: share ami
      include_role:
        name: ansible_cloud.share_ami.share
      vars:
        user_id_list: "{{ account_list }}"
        ami_list: "{{ my_ami_list }}"
```

Where your variable file looks like this:

```yml
my_ami_list:
  ap-northeast-1: ami-01334example
  ap-southeast-1: ami-0b3f3example
  eu-central-1: ami-03a5732example
  us-east-1: ami-01da94de9cexample
  us-east-2: ami-009f8b2c6dexample
account_list:
  - "11463example"
  - "90073example"
  - "71963example"
  - "07923example"
```

This would share these five AMIs to the four accounts listed.  There are
also two optional variables for share AMI, new_ami_name and new_tag
which will name (e.g. add the tag name: "whatever you put") and add a
hard coded ansiblecloud tag (e.g. add the tag ansiblecloud: "whatever
you put").  This could be further customized to add as many tags as you
want to your AMIs to help keep track of them.

```yml
new_ami_name: "RHEL 8.6 with automation controller"
new_tag: "my test"
```

Now you can see one of the many ways that Ansible Automation Platform
and Packer can easily and seamlessly work together to accomplish cloud
automation tasks.  If you want more blogs on Ansible and Packer or
Ansible and Terraform, please let us know!
