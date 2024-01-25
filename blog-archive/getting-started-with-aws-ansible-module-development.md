---
author: Jill Rouleau
date: 2020-10-06 00:00 UTC
description: If you're already using the Ansible AWS modules, there are
  many ways to use your existing knowledge, skills and experience to
  contribute. If you need some ideas on where to contribute, take a look
  at the following post.
lang: en-us
title: Getting Started With AWS Ansible Module Development and Community Contribution
---

# Getting Started With AWS Ansible Module Development and Community Contribution

We often hear from cloud admins and developers that they're interested
in giving back to Ansible and using their knowledge to benefit the
community, but they don't know how to get started.  Lots of folks may
even already be carrying new Ansible modules or plugins in their local
environments, and are looking to get them included upstream for more
broad use.

Luckily, it doesn't take much to get started as an Ansible contributor.
If you're already using the Ansible AWS modules, there are many ways to
use your existing knowledge, skills and experience to contribute. If you
need some ideas on where to contribute, take a look at the following:

-   Creating integration tests: Creating [missing tests](https://github.com/orgs/ansible-collections/projects/4#column-9963846)
    for modules is a great way to get started, and integration tests are
    just Ansible tasks!
-   Module porting: If you're familiar with the
    [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
    Python library, there's also a [backlog of modules](https://github.com/orgs/ansible-collections/projects/4#column-9964369)
    that need to be ported from boto2 to boto3.
-   Repository issue triage: And of course there's always open Github
    [issues](https://github.com/ansible-collections/amazon.aws/issues?utf8=%E2%9C%93&q=is%3Aissue+is%3Aopen)
    and pull requests. Testing bugs or patches and providing feedback on
    your use cases and experiences is very valuable.

## The boto3

Starting with Ansible 2.10, the AWS modules have been migrated out of
the [Ansible GitHub repo](https://github.com/ansible/ansible) and into
two new [Collection](https://docs.ansible.com/ansible/latest/user_guide/collections_using.html)
repositories.

The [Ansible-maintained Collection](https://github.com/ansible-collections/amazon.aws),
(`amazon.aws`) houses the modules, plugins, and module utilities that are managed by the Ansible
Cloud team and are included in the downstream Red Hat Ansible Automation Platform product.

The [Community Collection](https://github.com/ansible-collections/community.aws)
(`community.aws`) houses the modules and plugins that are supported by the Ansible community. 
New modules and plugins developed by the community should be proposed to
`community.aws`. Content in this Collection that is stable and meets other acceptance criteria
has the potential to be promoted and migrated into amazon.aws.

For more information about how to contribute to any of the
Ansible-maintained Collections, including the AWS Collections, refer to
the [Contributing to Ansible-maintained Collections section on docs.ansible.com](https://docs.ansible.com/ansible/devel/community/contributing_maintained_collections.html).


## AWS module development basics

For starters, make sure you've read the
[Guidelines for Ansible Amazon AWS module development](https://docs.ansible.com/ansible/devel/dev_guide/platforms/aws_guidelines.html)
section of the Ansible Developer Guide. Some things to keep in mind:

If the module needs to poll an API and wait for a particular status to
be returned before proceeding, add a
[waiter](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/clients.html)
to the [waiters.py](https://github.com/ansible-collections/amazon.aws/blob/main/plugins/module_utils/waiters.py)
file in the `amazon.aws` collection rather than writing a loop inside your module. For example,
the `ec2_vpc_subnet` module supports a wait parameter. When true, this instructs the module
to wait for the resource to be in an expected state before returning.
The module code for this looks like the following:

```yaml
if module.params['wait']:
    handle_waiter(conn, module, 'subnet_exists', {'SubnetIds': [subnet['id']]}, start_time)
```

And the corresponding waiter:

```yaml
        "SubnetExists": {
            "delay": 5,
            "maxAttempts": 40,
            "operation": "DescribeSubnets",
            "acceptors": [
                {
                    "matcher": "path",
                    "expected": True,
                    "argument": "length(Subnets[]) > `0`",
                    "state": "success"
                },
                {
                    "matcher": "error",
                    "expected": "InvalidSubnetID.NotFound",
                    "state": "retry"
                },
            ]
        },
```

This polls the EC2 API for `describe_subnets(SubnetIds=[subnet['id']])`
until the list of returned Subnets is greater than zero before
proceeding. If an error of `InvalidSubnetID.NotFound`
is returned, this is an expected response and the waiter code will continue.

Use [paginators](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/paginators.html)
when boto returns paginated results and build the result from the
`.build_full_result()` method of the paginator, rather than writing loops.

Be sure to handle both `ClientError` and `BotoCoreError` in your except blocks.

```yaml
except (botocore.exceptions.ClientError, botocore.exceptions.BotoCoreError) as e:
    module.fail_json_aws(e, msg="Couldn't create subnet")
```

All new modules should support
[check_mode](https://docs.ansible.com/ansible/latest/user_guide/playbooks_checkmode.html#check-mode-dry)
if at all possible.

Ansible strives to provide
[idempotency](https://en.wikipedia.org/wiki/Idempotence). Sometimes
though, this is inconsistent with the way that AWS services operate.
Think about how users will interact with the service through Ansible
tasks, and what will happen if they run the same task multiple times. 
What API calls will be made?  What changed status will be reported by
Ansible on subsequent task executions?

Whenever possible, avoid hardcoding data in modules. Sometimes it's
unavoidable, but if your contribution includes a hardcoded list of
instance types or a hard-coded
[partition](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#arns-syntax),
this will likely be brought up in code review - for example,
`arn:aws:` will not match the GovCloud or China regions, and your module will not work for users
in these regions. If you've already determined there's no reasonable way
to avoid hard-coding something, please mention your findings in the pull
request.

## Module Utilities

There's a substantial collection of `module_utils` available for working with AWS located in the `amazon.aws` collection:

```bash
$ ls plugins/module_utils/
acm.py  batch.py  cloudfront_facts.py  cloud.py  core.py  direct_connect.py  ec2.py  elb_utils.py  elbv2.py  iam.py  __init__.py  rds.py  s3.py  urls.py  waf.py  waiters.py
```

Of particular note, `module_utils/core.py` contains `AnsibleAWSModule()`,
which is the required base class for all new modules. This provides some
nice helpers like `client()` setup, the `fail_json_aws()` method
(which will convert boto exceptions into nice error messages and handle
error message type conversion for Python2 and Python3), and the class
will handle boto library import checks for you.

AWS APIs tend to use and return [Camel case](https://en.wikipedia.org/wiki/Camel_case) values, while Ansible
prefers [Snake case](https://en.wikipedia.org/wiki/Snake_case). Helpers
for converting between these in are available in
`amazon.aws.module_utils.ec2`,
including
`ansible_dict_to_boto3_filter_list()`,
`boto3_tag_list_to_ansible_dict()`,
and a number of tag and policy related functions.

## Integration Tests

The AWS Collections primarily rely on [functional integration tests](https://docs.ansible.com/ansible/latest/dev_guide/testing_integration.html)
to exercise module and plugin code by creating, modifying, and deleting
resources on AWS. Test suites are located in the Collection repository
that contains the module being tested.  The preferred style for tests
looks like a role named for the module with a test suite per module.
Sometimes it makes sense to combine the tests for more than one module
into a single test suite, such as when a tightly coupled service
dependency exists. These will generally be named for the primary module
or service being tested.  For example,
`*_info` modules may
share a test with the service they provide information for. An aliases
file in the root of the test directory controls various settings,
including which tests are aliased to that test role.

```bash
tests/integration/targets/ecs_cluster$ ls
aliases  defaults  files  meta  tasks

tests/integration/targets/ecs_cluster$ cat aliases
cloud/aws
ecs_service_info
ecs_task
ecs_taskdefinition
ecs_taskdefinition_info
unsupported
```

In this case, several modules are combined into one test, because an
`ecs_cluster` must be
created before an
`ecs_taskdefinition` can
be created. There is a strong dependency here.

You may also notice that ECS is not currently supported in the Ansible
CI environment.  There's a few reasons that could be, but the most
common one is that we don't allow unrestricted resource usage in the CI
AWS account. We have to create [IAM policies](https://github.com/mattclay/aws-terminator/tree/master/aws/policy)
that allow the minimum possible access for the test coverage. Other
reasons for tests being unsupported might be because the module needs
resources that we don't have available in CI, such as a federated
identity provider. See the **CI Policies and Terminator Lambda** section
below for more information.

Another test suite status you might see is unstable. That means the test
has been observed to have a high rate of transient failures. Common
reasons include needing to wait for the resource to reach a given state
before proceeding or tests taking too long to run and exceeding the test
timer. These may require refactoring of module code or tests to be more
stable and reliable. Unstable tests only get run when the module they
cover is modified and may be retried if they fail. If you find you enjoy
testing, this is a great area to get started in!

Integration tests should generally check the following tasks or
functions both **with and without** check mode:

-   Resource creation
-   Resource creation again (idempotency)
-   Resource modification
-   Resource modification again (idempotency)
-   Resource deletion
-   Resource deletion (of a non-existent resource)

Use `module_defaults` for
credentials when creating your integration test task file, rather than
duplicating these parameters for every task. Values specified in
`module_defaults` can be
overridden per task if you need to test how the module handles bad
credentials, missing region parameters, etc.

```yaml
- name: set connection information for aws modules and run tasks
  module_defaults:
    group/aws:
      aws_access_key: "{{ aws_access_key }}"
      aws_secret_key: "{{ aws_secret_key }}"
      security_token: "{{ security_token | default(omit) }}"
      region: "{{ aws_region }}"

  block:

  - name: Test Handling of Bad Region
    ec2_instance:
    region: "us-nonexistent-7"
      ... params …

  - name: Do Something
    ec2_instance:
      ... params ...

  - name: Do Something Else
    ec2_instance:
      ... params ...
```

Integration tests should make use of
[blocks](https://docs.ansible.com/ansible/latest/user_guide/playbooks_blocks.html)
with test tasks in one or more blocks and a final
`always:` block that
deletes all resources created by the tests.

## Unit Tests

While most modules are tested with integration tests, sometimes this is
just not feasible.  An example is when testing AWS Direct Connect. The
`community.aws.aws_direct_connect*`
modules can be used to establish a network transit link between AWS and
a private data center. This is not a task that can be done simply or
repeatedly in a CI test system. For modules that cannot practically be
integration tested, we do require [unit tests](https://docs.ansible.com/ansible/devel/dev_guide/testing_units_modules.html#testing-units-modules)
for inclusion into any AWS Ansible Collection.  The
[placebo](https://pypi.org/project/placebo/) Python library provides a
nice mechanism for recording and mocking boto3 API responses and is
preferred to writing and maintaining AWS fixtures when possible.

## CI Policies and Terminator Lambda

The Ansible AWS CI environment has safeguards and specific tooling to
ensure resources are properly restricted, and that test resources are
cleaned up in a reasonable amount of time. These tools live in the
[aws-terminator](https://github.com/mattclay/aws-terminator) repository.
There are three main sections of this repository to be aware of:

1.  The `aws/policy/` directory
2.  The `aws/terminator/` directory
3.  The `hacking/` directory

The `aws/policy/` directory contains IAM policies used by the Ansible CI service.
We generally attempt to define the minimum AWS IAM Actions and Resources
necessary to execute comprehensive integration test coverage. For
example, rather than enabling `ec2:*`, we have multiple
statement IDs, [Sids](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_sid.html)
that specify different actions for different resource specifications.

We permit `ec2:DescribeImages` fairly broadly in the region our CI runs in:

```yaml
  Resource:
      - "*"
    Condition:
      StringEquals:
        ec2:Region:
          - '{{ aws_region }}'
```

But are more restrictive on which instance types can be started or run via CI:

```yaml
- Sid: AllowEc2RunInstancesInstanceType
    Effect: Allow
    Action:
      - ec2:RunInstances
      - ec2:StartInstances
    Resource:
      - arn:aws:ec2:us-east-1:{{ aws_account_id }}:instance/*
    Condition:
      StringEquals:
        ec2:InstanceType:
          - t2.nano
          - t2.micro
          - t3.nano
          - t3.micro
          - m1.large  # lowest cost instance type with EBS optimization supported
```

The `aws/terminator/` directory contains the terminator application, which we deploy to AWS
Lambda.  This acts as a cleanup service in the event that any CI job
fails to remove resources that it creates.  Information about writing a
new terminator class can be found in the terminator's
[README](https://github.com/mattclay/aws-terminator/blob/master/aws/README.md).

The `hacking/` directory contains a playbook and two sets of policies that are intended for
contributors to use with their own AWS accounts.  The `aws_config/setup-iam.yml`
playbook creates IAM policies and associates them with two iam_groups.
These groups can then be associated with your own appropriate user:

-   *ansible-integration-ci*: This group mirrors the permissions used by
    the the AWS collections CI
-   *ansible-integration-unsupported*: The group assigns additional
    permissions on top of the 'CI' permissions required to run the
    'unsupported' tests

Usage information to deploy these groups and policies to your AWS user
is documented in the [setup-iam.yml](https://github.com/mattclay/aws-terminator/blob/master/hacking/aws_config/setup-iam.yml)
playbook.

## Testing Locally

You've now written your code and your test cases, but you'd like to run
your tests locally before pushing to GitHub and sending the change
through CI.  Great!  You'll need credentials for an AWS account and a
few setup steps. 

Ansible includes a CLI utility to run integration tests.  You can either
set up a [boto profile](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/configuration.html)
in your environment or use a credentials config file to authenticate to
AWS.  A [sample config](https://github.com/ansible/ansible/blob/devel/test/lib/ansible_test/config/cloud-config-aws.ini.template)
file is provided by the ansible-test application included with Ansible. 
Copy this file to `tests/integration/cloud-config-aws.ini` in your local checkout of
the collection repository and fill in your AWS account details for
`@ACCESS_KEY`, `@SECRET_KEY`, `@SECURITY_TOKEN`, `@REGIO`N.

**NOTE:** Both AWS Collection repositories have a
`tests/.gitignore` file that will ignore this file path when checking in code, but you should
always be vigilant when storing AWS credentials to disk or in a
repository directory.

If you already have Ansible installed  on your local machine,
`ansible-test` should already be in your PATH.  If not, you can run it from a local checkout
of the Ansible project.

```bash
git clone https://github.com/ansible/ansible.git
cd ansible/
source ansible/hacking/env-setup
```

You will also need to ensure that any Collection dependencies are
installed and accessible in your
[COLLECTIONS_PATHS](https://docs.ansible.com/ansible/devel/reference_appendices/config.html#collections-paths). 
Collection dependencies are listed in the
`tests/requirements.yml` file in the Collection and can be installed with the
`ansible-galaxy collection install` command.

You can now run integration tests from the Collection repository:

```bash
cd ~/src/collections/ansible_collections/amazon/aws
ansible-test integration ec2_group
```

Tests that are unstable or unsupported will not be executed by default. 
To run these types of tests, there are additional flags you can pass to
`ansible-test`:

```bash
ansible-test integration ec2_group --allow-unstable  --allow-unsupported
```

If you prefer to run the tests in a container, there is a default test
image that `ansible-test`
can automatically retrieve and run that contains the necessary Python
libraries for AWS tests.  This can be pulled and run by providing the
`--docker` flag.  (Docker must already be installed and configured on your local system.)

```bash
ansible-test integration ec2_group --allow-unstable  --allow-unsupported --docker
```

The test container image ships with all Ansible-supported versions of
Python.  To specify a particular Python version, such as 3.7, test with:

```bash
ansible-test integration ec2_group --allow-unstable  --allow-unsupported --docker --python 3.7
```

**NOTE:** Integration tests will create real resources in the specified
AWS account subject to AWS pricing for the resource and region. 
Existing tests should make every effort to remove resources at the end
of the test run, but make sure to check that all created resources are
successfully deleted after executing a test suite to prevent billing
surprises.  This is especially recommended when developing new test
suites or adding new resources not already covered by the test's always
cleanup block.  

**NOTE:** Be cautious when working with IAM, security groups, and other
access controls that have the potential to expose AWS account access or
resources.

## Submitting a Change

When your change is ready to submit, open a [pull request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/proposing-changes-to-your-work-with-pull-requests)
(PR) in the GitHub repository for the [appropriate AWS Collection](https://docs.ansible.com/ansible/devel/community/contributing_maintained_collections.html). 
Shippable CI will automatically run tests and report the results back to
the PR.  If your change is for a new module or tests new AWS resources
or actions, you may see permissions failures in the test.  In that case,
you will also need to open a PR in the [mattclay/aws-terminator repository](https://github.com/mattclay/aws-terminator/)
to add IAM permissions and possibly a [Terminator class](https://github.com/mattclay/aws-terminator/blob/master/aws/README.md)
to support testing the new functionality, as described in the
**CI Policies and Terminator Lambda** section of
this post.  Members of the Ansible AWS community will triage and review
your contribution, and provide any feedback they have on the
submission.  

## Next Steps and Resources

Contributing to open source projects can be daunting at first, but
hopefully this blog post provides a good technical resource on how to
contribute to the AWS Ansible Collections. If you need assistance with
your contribution along the way, you can find the Ansible AWS community
on [Freenode](https://freenode.net/) IRC in channel #ansible-aws.

Congratulations and welcome, you are now a contributor to the Ansible
project!
