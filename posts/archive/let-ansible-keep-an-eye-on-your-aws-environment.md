---
author: Gomathi Selvi Srinivasan
date: 2022-10-31 00:00 UTC
description: In this blog post, we are going to take a few configuration
  use cases and show how Ansible's CloudTrail module can be used to
  automate the same.
lang: en-us
title: Let Ansible keep an eye on your AWS environment
---

# Let Ansible keep an eye on your AWS environment

![](https://lh3.googleusercontent.com/wnD_tVJOsdCuKcbGSj5HICH-2u2iUClJws9FFApathtciNREwPSdVyPvu0JK9EIXGvfgOCR3MVRF9JqX8EmW6ROWkVI5GBcEEJNrac-g6RYDTomeiXs8xmDXLXcucUpGQIiJo-4d8Rzll2gklU2-1LlWgd4gGKGYIhz6ou6GS6b_yn6EaSnv0tlL2g){width="624"
height="364" loading="lazy"}

In a cloud model, the security of the environment and compliance becomes
the responsibility of both the end users and the cloud provider. This is
what we call the shared responsibility model in which every part of the
cloud, including the hardware, data, configurations, access rights, and
operating system, are protected. Depending on the local legislation and
the origin of the data that is handled (for instance laws like HIPAA,
the GDPR in Europe, or the Californian CCPA),  you may have to enforce
strict rules on your environment and log events for audit purposes. AWS
CloudTrail will help you to achieve this goal. The service can collect
and record any kind of information coming from your environment and
store or send the events to a destination for audit. In addition to
security and compliance, this service helps keep track of resource
consumption.

Ansible's CloudTrail module is used to leverage the various features of
the CloudTrail service to monitor and audit user activities and API
calls in the AWS environment. A trail is a configuration that lets us
describe an event filter and decide where the matching entries should be
sent. The recent 5.0.0 release of the Amazon.aws collection comes with a
new Cloudtrail module. This module helps create, configure, and delete a
trail. The final destination of a trail can be an S3 bucket or a
CloudWatch log. We have also paired the cloudtrail module with a
cloudtrail_info module, which helps collect the information of all or a
specific trail.

In this blog post, we are going to take a few configuration use cases
and show how Ansible's CloudTrail module can be used to automate the
same.

To download the amazon.aws collection, you can download it from

-   [Ansible Galaxy](https://galaxy.ansible.com/amazon/aws) - Community
-   [Ansible automation
    hub](https://console.redhat.com/ansible/automation-hub/repo/published/amazon/aws) -
    Fully supported and signed with your Red Hat subscription

## Use Case 1 - Get maximum visibility

Unless a trail is used for a specific activity in a specific region, it
is the best practice to enable CloudTrail for all regions. By doing so,
we maximize the visibility of the AWS environment so there is no
weakness (unmonitored region) that can be exploited by an attacker. This
will also make sure that we receive the event history for any new region
that AWS will launch in the future. 

``` yml
- name: create multi-region trail
  amazon.aws.cloudtrail:
    state: present
    name: myCloudTrail
    s3_bucket_name: mylogbucket
    region: us-east-1
    is_multi_region_trail: true
    tags:
      environment: dev
```

The cloudtrail_info module can be used to get all the information about
a particular trail or all the trails present. If a trail name is not
provided as input to this module, this module will get the information
of all trails, including shadow trails, by default. The shadow trails
can be skipped by setting
[include_shadow_trails]{style="color: #ff0000;"} to
[False]{style="color: #ff0000;"}.

``` yml
# Gather information about the multi-region trail
- amazon.aws.cloudtrail_info:
    trail_names:
      - arn:aws:cloudtrail:us-east-1:123456789012:trail/myCloudTrail
    include_shadow_trails: False
      register: trail_info

trail_info :
"trail_list": [
            {
                "has_custom_event_selectors": false,
                "has_insight_selectors": false,
                "home_region": "us-east-1",
                "include_global_service_events": true,
                "is_logging": true,
                "is_multi_region_trail": true,
                "is_organization_trail": false,
                "latest_delivery_attempt_succeeded": "",
                "latest_delivery_attempt_time": "",
                "latest_notification_attempt_succeeded": "",
                "latest_notification_attempt_time": "",
                "log_file_validation_enabled": false,
                "name": "myCloudTrail",
                "resource_id": "arn:aws:cloudtrail:us-east-1:123456789012:trail/myCloudTrail",
                "s3_bucket_name": "mylogbucket",
                "start_logging_time": "2022-09-29T11:41:41.752000-04:00",
                "tags": {"environment": "dev"},
                "time_logging_started": "2022-09-29T15:41:41Z",
                "time_logging_stopped": "",
                "trail_arn": "arn:aws:cloudtrail:us-east-1:123456789012:trail/myCloudTrail"
            }
        ]
```

## Use Case 2 - Manage access to S3 buckets

For this use case, we will manage the access given to the S3 buckets
where the trail logs are stored. As mentioned earlier, shared
responsibility includes sharing the security of the resources as well. 
S3 buckets are prone to incorrect configurations and are the major
source of data leaks. S3 buckets configured with public access allow
anyone on the internet to access the data. Ansible's s3_bucket  module
can be used to set CloudTrail's S3 bucket permissions and policies. This
S3 bucket can be passed to the CloudTrail module, which will be used as
the destination for the trail-generated logs.

``` yml
- amazon.aws.s3_bucket:
   name: mys3bucket
   state: present
   public_access:
       block_public_acls: true
       ignore_public_acls: true
       block_public_policy: false
       restrict_public_buckets: false

- name: Create trail with secured s3 bucket 
  amazon.aws.cloudtrail:
    state: present
    name: myCloudTrail
    s3_bucket_name: mys3bucket
    region: us-east-1
    tags:
      environment: dev
```

## Use Case 3 - Maintain CloudTrail logs integrity

CloudTrail logs are collected to verify the compliance and security of
the AWS environment. It is always possible that an attacker can gain
access and tamper with these logs to obscure their presence. By enabling
log file validation, a digital signature of the log file is generated,
which is used to check if the log files are valid and not tampered with.

``` yml
- name: create a trail with log file validation
  amazon.aws.cloudtrail:
    state: present
    name: myCloudTrail
    s3_bucket_name: mylogbucket
    region: us-east-1
    log_file_validation_enabled: true
    tags:
      environment: dev
 
# Gather information about the trail
- amazon.aws.cloudtrail_info:
    trail_names:
      - arn:aws:cloudtrail:us-east-1:123456789012:trail/myCloudTrail
    include_shadow_trails: False
      register: trail_info

trail_info :
"trail_list": [
            {
                "has_custom_event_selectors": false,
                "has_insight_selectors": false,
                "home_region": "us-east-1",
                "include_global_service_events": true,
                "is_logging": true,
                "is_multi_region_trail": fail,
                "is_organization_trail": false,
                "latest_delivery_attempt_succeeded": "",
                "latest_delivery_attempt_time": "",
                "latest_notification_attempt_succeeded": "",
                "latest_notification_attempt_time": "",
                "log_file_validation_enabled": true,
                "name": "myCloudTrail",
                "resource_id": "arn:aws:cloudtrail:us-east-1:123456789012:trail/myCloudTrail",
                "s3_bucket_name": "mylogbucket",
                "start_logging_time": "2022-09-29T11:41:41.752000-04:00",
                "tags": {"environment": "dev"},
                "time_logging_started": "2022-09-29T15:41:41Z",
                "time_logging_stopped": "",
                "trail_arn": "arn:aws:cloudtrail:us-east-1:123456789012:trail/myCloudTrail"
            }
        ]
```

## Use Case 4 - Encrypt the logs

By default, the S3 buckets are protected by an A[mazon server-side
encryption method and Amazon S3-managed encryption keys.
]{style="color: #222222;"}To add an extra layer of security, you can use
the AWS Key Management Service. This is directly manageable and helps
protect the log files from any attacker's survey of the environment.

``` yml
- name: Create an LMS key using lookup for policy JSON
  amazon.aws.kms_key:
    alias: my-kms-key
    policy: "{{ lookup('template', 'kms_iam_policy_template.json.j2') }}"
    state: present
  register: kms_key_for_logs
 
- name: Create a CloudTrail with kms_key for encryption
  amazon.aws.cloudtrail:
     state: present
     name: myCloudTrail
     s3_bucket_name: mylogbucket
     kms_key_id: "{{ kms_key_for_logs.key_id }}"
```

Similar to the use cases mentioned above, many parameters allow the
CloudTrail logs to be secure, compliant, and manageable. To get more
information on how to configure CloudTrail and get the configuration
information of an existing trail, please refer to
[amazon.aws.cloudtrail](https://ansible-collections.github.io/amazon.aws/branch/main/collections/amazon/aws/cloudtrail_module.html#ansible-collections-amazon-aws-cloudtrail-module)
and
[amazon.aws.cloudtrail_info](https://ansible-collections.github.io/amazon.aws/branch/main/collections/amazon/aws/cloudtrail_info_module.html#ansible-collections-amazon-aws-cloudtrail-info-module).

Now you can see four awesome use cases for Red Hat Ansible Automation
Platform and CloudTrail and how they can easily and seamlessly work
together to accomplish cloud automation tasks. If you want more blogs on
Ansible and AWS, please let us know!
