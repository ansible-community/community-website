---
author: Alina Buzachis
date: 2023-06-22 00:00 UTC
description: This blog covers the latest release of the certified
  amazon.aws Collection for Ansible Automation Platform that brings a
  number of enhancements.
lang: en-us
slug: whats-new-cloud-automation-with-amazon.aws-6.0.0
title: What's New with Cloud Automation with amazon.aws 6.0.0
---

# What's New with Cloud Automation with amazon.aws 6.0.0

When it comes to Amazon Web Services (AWS) infrastructure automation,
the latest release of the certified
[amazon.aws](https://console.redhat.com/ansible/automation-hub/repo/published/amazon/aws)
Collection for Red Hat Ansible Automation Platform brings a number of
enhancements to improve the overall user experience and speed up the
process from development to production.

This blog post goes through changes and highlights what's new in the
6.0.0 release of this Ansible Content Collection. We have included
numerous bug fixes, features, and code quality improvements that further
enhance the amazon.aws Collection. Let's go through some of them!

## Forward-looking Changes

### New boto3/botocore Versioning

The amazon.aws Collection has dropped support for
`botocore<1.25.0` and `boto3<1.22.0`. Most modules
will continue to work with older versions of the AWS Software
Development Kit (SDK), however, compatibility with older versions of the
AWS SDK is not guaranteed and will not be tested. When using older
versions of the AWS SDK, a warning will be displayed by Ansible. Check
out the module
[documentation](https://docs.ansible.com/ansible/devel/collections/amazon/aws/index.html)
for the minimum required version for each module. 

### New Python Support Policy

On July 30, 2022, AWS
[announced](https://aws.amazon.com/blogs/developer/python-support-policy-updates-for-aws-sdks-and-tools/)
that the AWS Command Line Interface (AWS CLI) v1 and AWS SDK for Python
([boto3](https://github.com/boto/boto3) and
[botocore](https://github.com/boto/botocore)), will no longer support
Python 3.6. To continue supporting Red Hat's customers with secure and
maintainable tools, we will be aligning with these deprecations and we
will deprecate support for Python versions less than 3.7 by this
collection. However, support for Python versions less than 3.7 by this
collection will be removed in release 7.0.0. Additionally, support for
Python versions less than 3.8 is expected to be removed in a release
after 2024-12-01 based on currently available
[schedules](https://aws.amazon.com/blogs/developer/python-support-policy-updates-for-aws-sdks-and-tools/).

## Removed Features

The following features have been removed from this collection release.

- `ec2_vpc_endpoint_info` - Support for the query parameter has been removed.
  The `amazon.aws.ec2_vpc_endpoint_info` module now only queries for endpoints.
  Services can be queried using the amazon.aws.ec2_vpc_endpoint_service_info module.
- `s3_object` - Support for creating and deleting S3 buckets using the `amazon.aws.s3_object` module has been removed.
  S3 buckets can be created and deleted using the `amazon.aws.s3_bucket` module.

## Deprecated Features

This collection release also introduces some deprecations. For
consistency between the collection and AWS documentation, the
`boto3_profile` alias for the `profile` option has been
deprecated. Please use `profile` instead.

The `amazon.aws.s3_object` and `amazon.aws.s3_object_info`
modules have also undergone several deprecations.

-   Passing contemporarily `dualstack` and `endpoint_url` has been deprecated.
    The `dualstack` parameter is ignored when `endpoint_url`  is passed.
    Support will be removed in a release after 2024-12-01 .
-   Support for passing values of `overwrite` other than `always`, `never`, `different` or `last` has been deprecated.
    Boolean values should be replaced by the strings `always` or `never`.
    Support will be removed in a release after 2024-12-01.

## Code quality and CI improvement

Part of the effort in this release was dedicated to improving the
quality of the collection's code. We have adopted several linting and
formatting tools that help enforce coding conventions and best
practices, with all code following the same style and standards. The
linting tools help detect and flag code that may not be optimal, such as
unused variables or functions, unnecessary loops or conditions, detect
security vulnerabilities, and other inefficiencies. Formatting tools
help to automatically format and style the code to ensure consistency
and readability. 

Overall, this code quality improvement initiative aims to lead to more
reliable, efficient and maintainable software that provides a better
user experience and ultimately benefits both developers and end users.
In addition, several plugins have undergone refactoring (e.g., removing
duplicate code, simplifying complex logic and using design patterns
where appropriate) to make the code more efficient and maintainable. We
have also extended the coverage of unit tests so the code behaves as
expected.

This initiative does not stop here. We have also decided to move to
GitHub actions for CI from Zuul. This decision helps us simplify the CI
pipeline as it is natively integrated with GitHub and improves
scalability, collaboration, workflow management and the efficiency of
the development process.

Because improving code quality is a continuous process that requires
ongoing effort and attention, this work is ongoing and will be reflected
in future releases.

## Renamings

As naming might be generally tedious, a misleading module or option's
name may complicate the user experience.

We decided to rename the `amazon.aws.aws_secret` lookup plugin in this collection release.
This decision is a follow up of the renaming initiative started in release 5.0.0 of this collection.
Therefore, the `amazon.aws.aws_secret` module has been renamed to `amazon.aws.secretsmanager_secret`. 

We have also decided to rename the `amazon.aws.aws_ssm` lookup plugin to `amazon.aws.ssm_parameter`.

However, `aws_secret` and `aws_ssm` remain as aliases and they will be deprecated in the future. 

For consistency amongst our plugins and modules, we renamed the following options:

- `aws_profile` renamed to `profile` (`aws_profile` remains as an alias)
- `aws_access_key` renamed to `access_key` (`aws_access_key` remains as an alias)
- `aws_secret_key` renamed to `secret_key` (`aws_secret_key`  remains as an alias)
- `aws_security_token` renamed to `security_token` (`aws_security_token` remains as an alias)

These changes should not have observable effect for users outside the module/plugin documentation.

## New Modules

This release brings a number of new base supported modules that
implement AWS Backup capabilities. 

AWS Backup is a fully managed backup service that enables you to
centralize and automate the backup of data across AWS services and
on-premises applications,  eliminating the need for custom scripts and
manual processes. 

With AWS Backup, you can create backup policies that define backup
schedules and retention periods for your AWS resources, including Amazon
EBS volumes, Amazon RDS databases, Amazon DynamoDB tables, Amazon EFS
file systems, and Amazon EC2 instances. 

The following table highlights the functionalities covered by these new
Red Hat supported modules:

- `backup_restore_job_info` - Get detailed information about AWS Backup restore jobs initiated to restore a saved resource.
- `backup_vault` - Manage AWS Backup vaults.
- `backup_vault_info` - Get detailed information about an AWS Backup vault.
- `backup_plan` - Manage AWS Backup plans.
- `backup_plan_info` - Get detailed information about an AWS Backup Plan.
- `backup_selection` - Manages AWS Backup selections.
- `backup_selection_info` - Get detailed information about AWS Backup selections.
- `backup_tag` - Manage tags on an  AWS backup plan, AWS backup vault, AWS recovery point.
- `backup_tag_info` - List tags on AWS Backup resources.

### Automate backups of your AWS resources with the new AWS Backup supported modules

In this example, I show you how to backup an RDS instance tagged `backup: "daily"`. This example can
be extended to all currently supported resource types (e.g., EC2, EFS, EBS, DynamoDB) which are tagged with
`backup: "daily"`. The following playbook shows the the steps necessary to achieve that:

``` yml
- name: Automated backups of your AWS resources with AWS Backup
  hosts: localhost
  gather_facts: false


  tasks:
  - name: Create a mariadb instance tagged with “backup”; “daily”
     amazon.aws.rds_instance:
       id: "demo-backup-rdsinstance"
       state: present
       engine: mariadb
       username: 'test'
       password: 'test12345678'
       db_instance_class: 'db.t3.micro'
       allocated_storage: 20
       deletion_protection: true
       tags:
         backup: "daily"
     register: result


   - name: Create an IAM Role that is needed for AWS Backup
     community.aws.iam_role:
       name: "backup-role"
       assume_role_policy_document: '{{ lookup("file", "backup-policy.json") }}'
       create_instance_profile: no
       description: "Ansible AWS Backup Role"
       managed_policy:
         - "arn:aws:iam::aws:policy/service-role/AWSBackupServiceRolePolicyForBackup"
     register: iam_role


   - name: Create an AWS Backup vault for the plan to target
     # The AWS Backup vault is the data store for the backed up data.
     amazon.aws.backup_vault:
       backup_vault_name: "demo-backup-vault"


   - name: Get detailed information about the AWS Backup vault
     amazon.aws.backup_vault_info:
       backup_vault_names:
         - "demo-backup-vault"
     register: _info


   - name: Tag the AWS backup vault
     amazon.aws.backup_tag:
       resource: "{{ _info.backup_vaults.backup_vault_arn }}"
       tags:
           environment: test


   - name: Create an AWS Backup plan
     # A backup plan tells AWS Backup service to backup resources each day at 5 o’clock in the morning. In the backup rules we specify the AWS Backup vault to target for storing recovery points.
     amazon.aws.backup_plan:
       backup_plan_name: "demo-backup-plan"
       rules:
         - rule_name: daily
           target_backup_vault_name: "demo-backup-vault"
           schedule_expression: "cron(0 5 ? * * *)"
           start_window_minutes: 60
           completion_window_minutes: 1440
     register: backup_plan_create_result


   - name: Get detailed information about the AWS Backup plan
     amazon.aws.backup_plan_info:
       backup_plan_names:
         - "demo-backup-plan"
     register: backup_plan_info_result


   - name: Create an AWS Backup selection
     # AWS Backup selection supports tag-based resource selection. This means that resources that should be backed up by the AWS Backup plan needs to be tagged with “backup”: “daily” and they are then automatically backed up by AWS Backup.
     amazon.aws.backup_selection:
      selection_name: "demo-backup-selection"
      backup_plan_name: "demo-backup-plan"
      iam_role_arn: "{{ iam_role.iam_role.arn }}"
      list_of_tags:
         - condition_type: "STRINGEQUALS"
           condition_key: "backup"
           condition_value: "daily"
     register: backup_selection_create_result


   - name: Get detailed information about the AWS Backup selection
     amazon.aws.backup_selection_info:
       backup_plan_name: "demo-backup-plan"
```

Once this playbook has finished the execution, AWS Backup will start to
create daily backups of the resources tagged with
`backup=daily`. You can
monitor the status of the backup service demo on the AWS console. If we
go to Jobs, we see some backup jobs that have already been completed. A
backup job is the result of an AWS Backup plan rule and resource
selection. It will attempt to backup the selected resources, within the
time window defined in the backup plan rule.

![screenshot](/images/posts/archive/aws-backup-jobs.png)

If we're taking a look at the AWS Backup vault we created, you can see
it contains the recovery points of the RDS instance. A recovery point is
either a snapshot or a point-in-time recovery backup. The data inside a
recovery point cannot be edited. Tags and retention period can be
changed if the backup vault allows it. You can use the recovery point to
restore data.

![screenshot](aws-recovery-points.png)

An AWS Backup restore job is used to restore data from backups taken
with AWS Backup service. This release does not include the module that
enables you to create an AWS backup restore job, but we are planning to
include this feature in the future. However, in this release, we have
included the `amazon.aws.backup_restore_job_info` module to get
information about the restore job.

``` yml
- name: Get detailed information about the AWS Backup restore job
  amazon.aws.backup_restore_job_info:
    restore_job_id: "{{ restore_job_id }}"
```
