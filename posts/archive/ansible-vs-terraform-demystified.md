---
author: Sean Cavanaugh
date: 2022-09-13 00:00 UTC
description: Comparing and contrasting Red Hat Ansible Automation
  Platform and Hashicorp Terraform
lang: en-us
title: Ansible versus Terraform Demystified
---

# Ansible versus Terraform Demystified

> Consider also checking out the article [Ansible vs. Terraform](https://www.redhat.com/en/topics/automation/ansible-vs-terraform), clarified on RedHat.com

Ansible and Terraform are two very powerful but unique open source IT
tools that are often compared in competitive discussions.  We often see
comparisons of the two tools - but many times, these comparisons are
done purely from a "spec sheet" comparison. This type of comparison,
while an interesting read, doesn't take into account using the products
at scale or if the comparison is realistic as a binary all-or-nothing
approach. We at Red Hat have been helping enterprises for over 20 years
and have a good idea how most IT administrators are using these two
tools in production. Although both tools *can* generally do most things,
we typically see that they are each leveraged by means of their biggest
strengths as opposed to having to choose one or the other.

Spoiler:  The two tools are better together and can work in harmony to
create a better experience for developers and operations teams.

Both Ansible and Terraform are open source tools with huge user bases,
which often leads to cult followings because of the classical "hammer"
approach.  That is, if my only tool is a hammer, every problem will
start resembling a nail. This ends up trying to solve new problems the
only way I know how, rather than trying another tool that might be more
effective.  It is never a great idea to only understand one tool and its
approach and philosophy. Instead, you should open your mind to
understanding why different tools and platforms exist, and why
successful organizations may be using both.  In this blog we will go
over the differences and similarities between Ansible and Terraform, the
open source projects and their downstream enterprise products.  Keep in
mind that this is a blog and to check the date for relevancy as products
and projects are constantly changing and evolving.

## Terraform

Terraform is an open source project that is sponsored by the company
HashiCorp. Terraform is one of several open source projects that have
been productized by HashiCorp; other projects include Vagrant, Packer,
Consul and Vault.  HashiCorp specifically has a design philosophy called
the [Tao of HashiCorp](https://www.hashicorp.com/tao-of-hashicorp) where
they want their projects and products to be simple, modular, and
composable. In this case, each project and product pairing has well
defined scopes and for larger workflows you would combine multiple
projects and products.  They define Terraform with the following
purpose:

Terraform is the infrastructure as code offering from HashiCorp. It is
a tool for building, changing, and managing infrastructure in a safe,
repeatable way. Operators and Infrastructure teams can use Terraform to
manage environments with a configuration language called the HashiCorp
Configuration Language (HCL) for human-readable, automated
deployments. [source](https://learn.hashicorp.com/tutorials/terraform/infrastructure-as-code)

Terraform is mainly command-line only, but is well integrated with a set
of popular public clouds. Terraform is great at provisioning fixed sets
of cloud infrastructure and tearing them down afterwards.  HashiCorp
provides two productization methods of Terraform for customers, they can
either self-manage their custom deployment with Terraform Enterprise or
they can use their managed service [Terraform Cloud](https://www.hashicorp.com/products/terraform/pricing).
Their
business tier provides drift detection, SSO Audit logs, self-hosted
agents and customized concurrency.

## Ansible

Ansible is an IT automation tool. It can configure systems, deploy
software, and orchestrate more advanced IT tasks such as continuous
deployments or zero downtime rolling updates.  Most people are familiar
with community Ansible, which is the command-line tool for running
Ansible Playbooks.  Like Terraform, Ansible focuses on simplicity and
ease-of-use.  Ansible uses [YAML syntax](https://docs.ansible.com/ansible/latest/reference_appendices/YAMLSyntax.html) for
Ansible playbooks.  We use YAML because it is easier for humans to read
and write than other common data formats like XML or JSON.

Red Hat Ansible Automation Platform is the product that is offered to
customers.  It is built on the foundations of Ansible with numerous
enterprise features, combining more than a dozen upstream projects into
an integrated, streamlined product. Each product component also has a
specific purpose with a well defined scope similar to HashiCorp's design
philosophy.  For example, the automation controller is the Web UI and
API for Ansible automation, which is based on the upstream project AWX.
 This component is bundled into the platform to manage automation.
Ansible Automation Platform is available to be [run on-premises](https://www.redhat.com/en/technologies/management/ansible/trial?extIdCarryOver=true&sc_cid=701f2000000txokAAA) and
charged by node (rather than by user) or you can use the
[managed service offering on Microsoft Azure](https://www.redhat.com/en/technologies/management/ansible/azure).

To summarize, both Ansible and Terraform have open source command-line
only versions.  They both have products available with enterprise
features such as a Web UI or SSO.  The primary difference for their
community versions is that Ansible is an multi-purpose automation tool,
whereas Terraform is an infrastructure as code tool.  The confusion
starts occurring because there are numerous use cases that could
potentially be solved by either tool, and both Ansible and Terraform
have plugins to call each other.  For example, many Ansible experts
simply provision AWS resources with an Ansible Playbook and might not
understand why others use an entirely different tool. Similarly,
Terraform experts might create and destroy entire instances for even the
smallest configuration change (see next section about immutability).

## Immutable Infrastructure: The Killer App?

Terraform takes an immutable approach to infrastructure.  If you are
unfamiliar with immutable infrastructure, it is defined as instances
that do not change over time or are unable to be changed. To greatly
simplify, an IT operator can create a declarative file (a Terraform HCL
file) that represents in structured data what they want their end-state
cloud footprint to look like and deploy this with Terraform.  One of the
advantages of this approach is that it creates a single source of truth
(that HCL file) that can be deployed over and over again without having
to understand how it gets to the end-state.  This approach can be simple
and elegant for individuals getting started quickly but depending on the
size of infrastructure can become [complex and hard to manage](https://www.youtube.com/watch?v=wRgQxfrFJYU).
Another advantage
of an immutable approach is that it is just as easy to tear down
(de-provision) your cloud resources. This allows developers to quickly
spin up resources, test something, then tear them down.

Ansible, by design, takes an imperative approach to automation.  You
simply have a task list that iterates through each resource.  You would
tell it to provision this VPC, this subnet, then this VM.  The advantage
of this approach is it is very simple to understand, there is no hidden
magic, which helps it become easy to troubleshoot.  The disadvantage is
usually it is more cumbersome to do teardowns and de-provision without
knowing the correct order.  I have to delete the instance, then the
security group, and so on and so forth. However, Ansible has support for
calling both AWS CloudFormation (another immutable and declarative
approach for AWS), and Terraform.  In fact, Ansible Automation Platform
does this for all major public clouds, and encourages people to use
their preference for provisioning and de-provisioning.  This is a great
example of how Terraform and Ansible are better together.

**Important:** Although Ansible is not universally immutable, depending
on how you implement your individual tasks, some Ansible tasks can be
immutable.

Here's an example: You can have an Ansible Playbook that provisions a
Linux virtual machine into a public cloud using a CloudFormation
Template, and then subsequently installs an application via the
[dnf Ansible module](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/dnf_module.html).
This activity would be entirely immutable by Ansible.  Most Ansible
modules are designed to be
[idempotent](https://docs.ansible.com/ansible/latest/reference_appendices/glossary.html#term-Idempotency) so
that they only make changes when they need to.  Ansible is extremely
flexible, and it's easy to just automate shell commands which are not
idempotent and change every time the playbook is run.  This showcases
how Ansible shines as a multi-purpose automation tool versus a discrete
infrastructure as code tool.  

## Use Cases Compared

If you read all the articles about Terraform, you will find they are
public-cloud focused. This is where immutable infrastructure works well
and Terraform is great at provisioning cloud resources and applications
for AWS, Azure, Docker, GCP, and OCI.  However, there is more to IT
operations than automated infrastructure provisioning and this is why
Ansible is extremely popular as well.  This is not a knock on Terraform,
it is a specific tool with a specific purpose and ethos designed
purposely to do infrastructure as code.  However, this infrastructure as
code wholly depends on how you define your infrastructure.  Is my
critical Cisco IOS network switch not infrastructure?  IT Infrastructure
can mean a lot of different things to different IT administrators
depending on if they are a network engineer, cloud operations engineer,
system administrator or have another title or role.

Ansible focuses on automation with a variety of use cases that are
typically divided up into domains, due to their legacy silos:

-   Infrastructure automation - includes automation of Linux and
    Microsoft Windows, as well as storage vendors like NetApp,
    PureStorage, and HPE.
-   Network automation - includes physical switches, routers, load
    balancers, and SDN controllers from popular vendors such as Arista,
    Cisco, F5 and Juniper.
-   Security automation - integrates SIEM, IDPS, and firewalls from
    vendors like IBM, Checkpoint, and ITSM tools like ServiceNow.  
-   Edge and hybrid cloud footprints.

## Moving to an Event-Driven IT Strategy

As opposed to Terraform, Ansible is more focused on the entire IT
workflow. For example, consider the following workflow:

1.  Deploy a Web Application to AWS.
2.  Update your ServiceNow ITSM with Web Application Information.
3.  Run a schedule to check every hour that the Web Application is
    responding on the correct ports *or* use event streams to monitor
    ports and the application for further automation.
4.  Update/Create a ServiceNow ticket if the Web Application stops
    responding and attempts automation for remediation.

In the above example, it is not enough to simply provision a web
application into a public cloud.  There are other steps that need to
take place in this automation workflow.  We need the automation to sync
with the customer\'s ITSM tool, and include event-driven checks for the
web application to ensure it is operating correctly (we call this
continuous IT compliance).  Stateful automation can even guarantee this
service is kept running while human operators make changes out of band
from your automation.

## Better: Ansible Orchestrating Terraform

Terraform is an excellent cloud provisioning and de-provisioning tool
for infrastructure as code.  Ansible is a great all-purpose,
cross-domain automation solution.  Both have an amazing open source
communities and well supported downstream paid products.  What we see
with the community, customers and even our own IT workflows is that you
can combine these tools and solutions to create even more amazing IT
workflows.  If you are already invested with Terraform, Ansible simply
allows you to wrap those HCL templates into more holistic automation
workflows. Ansible further extends your automation allowing you to add
tasks like configuration management and application deployment to the
Terraform IaC deployment.

## How are people using Ansible?

We've noticed that many IT administrators refer to the specific "cloud
deployment and retirement" use case rather than looking at other cloud
operations use cases, such as Day 2 operations.  To help spark some
ideas, let's highlight some Ansible cloud automation use cases today
outside of just provisioning and de-provisioning cloud resources.

-   **Infrastructure visibility -** This is simply using Ansible to
    retrieve information from your public clouds to understand your
    cloud footprint.  This is very helpful for brownfield environments
    where there are numerous IT administrators configuring resources
    out-of-band from each other.  When there isn't a forced IT process,
    it is a great starter use case because it is read-only and requires
    no production changes.
-   **Compliance -** We need to not only treat cloud infrastructure as
    code, but also the cloud as code.  For example, we can enforce IAM
    policies and make sure there is a common experience across public
    clouds.  Another example would be to force a tag policy across your
    instances for billing and auditing and shutting down instances out
    of compliance.  What's great about Ansible is that it can operate
    and enforce these policies on mutable and immutable infrastructure.
-   **Business continuity -** Ansible can help keep the lights on.  Move
    and copy resources off cloud, create and manage policies for backups
    and build automation to manage disruptions and failures.
-   **Cloud operations -** Ansible can automate Day 2 activities.  This
    includes application deployments and CI/CD pipelines, lifecycle
    management and enforcement as well as OS patching and maintenance.
-   **Cloud migration -** Ansible can help move workloads to where you
    need them.  For example, adopting automation for your on-premises
    infrastructure can help operators adopt public cloud.  Making sure
    your source of truth is automation versus the on-box configurations
    is the first step for cloud migration.  Ansible automation can also
    reduce friction for migration to cloud native, allowing developers
    to migrate off legacy infrastructure.  By using Ansible automation,
    an IT group can help unify automation architecture across legacy and
    cloud-native.
-   **Infrastructure optimization -** Adopting clouds can help IT
    operators save time and money, but initially it\'s hard to predict
    costs and understand how your billing requirements change.  Having
    an automation strategy can help you keep costs under control by
    turning off unused resources, rightsizing cloud resources and
    combining with use cases like infrastructure visibility, you can
    easily recover orphaned resources and make sure there are no
    surprise costs.
-   **Infrastructure orchestration -** We talked about this previously,
    but how are you integrating everything that's not in your public
    cloud? Orchestration is simply how we break down silos and integrate
    with infrastructure outside the cloud.  This allows IT operators to
    orchestrate business outcomes versus tech silos and apply consistent
    compliance across all infrastructure.
-   **Automated troubleshooting -** As your IT team gains confidence
    with automation, we can move towards an event-driven architecture.
     This allows IT teams to respond faster to incidents, speed up
    meantime to resolution and integrate with an organization's ITSM
    solution.

## Are people succeeding?

The quick answer? Yes! Even automating Terraform with Ansible! But
holistic automation goes beyond doing one thing well in the cloud.
Ansible can automate and orchestrate physical, virtual and cloud
resources. It can automate the provisioning, configuration management,
and manage Day 2 operations of network devices, Windows servers, storage
and of course Linux. But regardless of what people decide to use to
solve a problem, we've found that the real issues aren't with "what" or
"how" a problem is solved from a technology perspective, but more about
standardizing across technology domains while growing up and out to
scale across the entire IT organization.

One of the most impressive and recent success stories using Ansible
Automation Platform in the cloud was by Asian Development Bank. The
published [case study](https://www.redhat.com/en/resources/asian-development-bank-case-study)
details how they modernized their infrastructure while at the same time
modernizing their workforce, allowing them more time to focus on more
important things, like innovative projects and new service offerings.
They standardized on Terraform for Day 0 while standardizing on Ansible
Automation Platform for Day 1 and Day 2 operations. Check out their
story in the embedded
[video](https://www.redhat.com/en/resources/asian-development-bank-case-study)!

## Final Thoughts

The confusion between Ansible and Terraform has existed for some time,
either through inaccurate (or outdated) source material or through
inexperience in using either/both technologies. This blog post (while
somewhat biased) should help to at least start the conversation around
the deeper connections between Ansible and Terraform. Every situation,
use case, and person implementing the solution can be different, but
because of these factors we believe Ansible is the best solution for
automation.
