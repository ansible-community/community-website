---
author: Jeff Geerling
date: 2020-01-14 00:00 UTC
description: A closer look at Ansible in a Cloud-Native Kubernetes
  Environment.
lang: en-us
title: How useful is Ansible in a Cloud-Native Kubernetes Environment?
---

# How useful is Ansible in a Cloud-Native Kubernetes Environment?

A question I've been hearing a lot lately is "why are you still using
Ansible in your Kubernetes projects?" Followed often by "what's the
point of writing your book [Ansible for
Kubernetes](https://www.ansibleforkubernetes.com/) when Ansible isn't
really necessary once you start using Kubernetes?"

I spent a little time thinking about these questions, and the motivation
behind them, and wanted to write a blog post addressing them, because it
seems a lot of people may be confused about what Kubernetes does, what
Ansible does, and why both are necessary technologies in a modern
business migrating to a cloud-native technology stack (or even a fully
cloud-native business).

One important caveat to mention upfront, and I quote directly from my
book:

*While Ansible can do almost everything for you, it may not be the right
tool for every aspect of your infrastructure automation. Sometimes there
are other tools which may more cleanly integrate with your application
developers' workflows, or have better support from app vendors.*

We should always guard against the [golden hammer
fallacy](https://en.wikipedia.org/wiki/Law_of_the_instrument). No single
infrastructure tool---not even the best Kubernetes-as-a-service
platform---can fill the needs of an entire business's IT operation. If
anything, we have seen an explosion of specialist tools as is evidenced
by the [CNCF landscape](https://landscape.cncf.io/).

Ansible fits into multiple areas of cloud-native infrastructure
management, but I would like to specifically highlight three areas in
this post:

![Ansible_cloud-native-venn-diagram](/images/posts/archive/Ansible_cloud-native-venn-diagram.png)

Namely, how Ansible fits into the processes for Container Builds,
Cluster Management, and Application Lifecycles.

I'd especially caution against teams diving into Kubernetes head first
without a broader automation strategy. Kubernetes can't manage your
entire application lifecycle, nor can it bootstrap itself; you should
not settle for automating the inside of a Kubernetes cluster while using
manual processes to build and manage your cluster; this becomes
especially dangerous if you manage more than one cluster, as is best
practice for most environments (at least having a staging and production
cluster, or a private internal cluster and a public facing cluster).

## Container Build

In the past decade, server management and application deployment became
more and more automated. Usually, automation became more intuitive and
maintainable, especially after the introduction of configuration
management and orchestration tools like CFEngine, Puppet, Chef, and
Ansible.

There's no great solution for all application deployments, though, even
with modern automation tools. Java has WAR files and the VM. Python has
virtual environments. PHP has scripts and multiple execution engines.
Ruby has ruby environments. Running operations teams who can efficiently
manage servers and deployments for five, ten, or more development stacks
(and sometimes multiple versions of each, like Java 7, Java 8, and Java
11) is a failing proposition.

Luckily, containerization started to solve that issue. Instead of
developers handing off source code and expecting operations to be able
to handle the intricacies of multiple environments, developers hand off
containers, which can be run by a compatible container runtime on almost
any modern server environment.

But in some ways, things have stagnated in the container build realm;
the Dockerfile, which was nothing more than a shell script with some
Docker-specific DSL and hacky inline commands to solve image layer size
issues, is still used in many places as the *de facto* app build script.

![Geerling Blog 3](/images/posts/archive/geerling-blog-three.png)

How many times have you encountered an indecipherable Dockerfile like
this?

We can do better. Ansible can build and manage containers using
Dockerfiles, sure, but Ansible is also very good at building container
images directly---and nowadays, you don't even need to install Docker!
There are lighter-weight open source build tools like
[Buildah](https://buildah.io/) that integrate with an Ansible container
build tool
[ansible-bender](https://github.com/ansible-community/ansible-bender) to
build containers using more expressive and maintainable Ansible
Playbooks.

There are other ways to build containers, too. But I lament the fact
that many developers and sysadmins have settled on the lowest common
denominator, the Dockerfile, to build their critical infrastructure
components, when there are more expressive, maintainable, and universal
tools like Ansible which produce the same end result.

## Cluster Management

Kubernetes Clusters don't appear out of thin air. Depending on the type
of clusters you're using, they require management for upgrades and
integrations. Cluster management can become crippling, especially if,
like most organizations, you're managing multiple clusters (multiple
production clusters, staging and QA clusters, etc.).

If you're running inside a private cloud, or on bare metal servers, you
will need a way to install Kubernetes and manage individual servers in
the cluster. Ansible has a proven track record of being able to
orchestrate multi-server applications, and Kubernetes itself is a
multi-server application---which happens to manage one or thousands of
other multi-server applications through containerization.

Projects like [Kubespray](https://kubespray.io/) have used Ansible for
custom Kubernetes cluster builds and are compatible with dozens of
different infrastructure arrangements.

Even if you use a managed Kubernetes offering, like AKS, EKS, or GKE,
Ansible has modules like
[azure_rm_aks](https://docs.ansible.com/ansible/latest/modules/azure_rm_aks_module.html),
[aws_eks_cluster](https://docs.ansible.com/ansible/latest/modules/aws_eks_cluster_module.html),
and
[gcp_container_cluster](https://docs.ansible.com/ansible/latest/modules/gcp_container_cluster_module.html),
which manage clusters, along with thousands of other modules which
simplify and somewhat standardize cluster management among different
cloud providers.

Even if you don't need multi-cloud capabilities, Ansible offers useful
abstractions like managing CloudFormation template deployments on AWS
with the
[cloudformation](https://docs.ansible.com/ansible/latest/modules/cloudformation_module.html)
module, or Terraform deployments with the
[terraform](https://docs.ansible.com/ansible/latest/modules/terraform_module.html)
module.

It's extremely rare to have an application which can live entirely
within Kubernetes and not need to be coordinated with any external
resource (e.g. networking device, storage, external database service,
etc.). If you're lucky, there may be a Kubernetes Operator to help you
integrate your applications with external services, but more often
there's not. Here, too, Ansible helps by managing a Kubernetes
application along with external integrations, all in one playbook
written in cloud-native's *lingua franca*, YAML.

I'll repeat what I said earlier: you should not settle for automating
the inside of a Kubernetes cluster while using manual processes to build
and manage your cluster---especially if you have more than one cluster!

## Application Lifecycle

The final area where Ansible shows great promise is in managing
applications inside of Kubernetes. Using Ansible to build operators with
the [Operator SDK](https://github.com/operator-framework/operator-sdk),
you can encode all your application's lifecycle management (deployment,
upgrades, backups, etc.) inside of a [Kubernetes
operator](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/)
to be placed in any Kubernetes cluster---even if you don't use Ansible
to manage anything else in that cluster.

Rather than forcing developers and ops teams to learn Go or another
specialized language to maintain an operator, you can build it with YAML
and Ansible.

There is a lot of promise here, though there are scenarios---at least,
in the current state of the Operator SDK---where you might need to drop
back to Go for more advanced use cases. The power comes in the ability
to rely on Ansible's thousands of modules from within your running
Application operator in the cluster, and in the ease of adoption for any
kind of development team.

For teams who already use Ansible, it's a no-brainer to migrate their
existing Ansible knowledge, roles, modules, and playbooks into
Kubernetes management playbooks and Ansible-based operators. For teams
new to Ansible, its flexibility for all things related to IT automation
(Networking, Windows, Linux, Security, etc.) and ease of use make it an
ideal companion for cloud-native orchestration.
