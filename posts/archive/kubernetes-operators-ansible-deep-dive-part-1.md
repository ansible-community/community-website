---
author: James Cammarata
date: 2019-07-25 00:00 UTC
description: Part one of this series Senior Principal Software Engineer
  at Ansible, James Cammarata walks through Kubernetes Operators and
  writing Operators in Ansible
lang: en-us
title: Kubernetes Operators with Ansible Deep Dive, Part 1
---

# Kubernetes Operators with Ansible Deep Dive, Part 1

This deep dive series assumes the reader has access to a Kubernetes test
environment. A tool like minikube is an acceptable platform for the
purposes of this article. If you are an existing Red Hat customer,
another option is spinning up an OpenShift cluster
through [[cloud.redhat.com](https://cloud.redhat.com/){.c8}]{.c9}[. This
SaaS portal makes trying OpenShift a turnkey operation.]{.c6}

In this part[ of this deep dive series, we\'ll:]{.c6}

1.  [Take a look at operators overall, and what they do in
    OpenShift/Kubernetes.]{style="background-color: transparent;"}
2.  [Take a quick look at the Operator SDK, and why you\'d want to use
    an Ansible operator rather than other kinds of operators provided by
    the SDK.]{style="background-color: transparent;"}
3.  [And finally, how Ansible Operators are structured and the relevant
    files created by the Operator
    SDK.]{style="background-color: transparent;"}

## What Are Operators?

For those who may not be very familiar with Kubernetes, it is, in its
most simplistic description - a resource manager. Users specify how much
of a given resource they want and Kubernetes manages those resources to
achieve the state the user specified. These resources can be pods (which
contain one or more containers), persistent volumes, or even custom
resources defined by users.

This makes Kubernetes useful for managing resources that don\'t contain
any state (like pods of web servers or load balancing resources).
However, Kubernetes doesn\'t provide any built-in logic for managing
resources like databases or caches which are stateful and sensitive to
restarts. Operators were created to bridge this gap by providing a way
for users to specify a piece of code (traditionally written in Golang)
tied to [[custom resource
definitions](https://docs.openshift.com/container-platform/4.1/applications/crds/crd-extending-api-with-crds.html){.c8}
in Kubernetes.]{.c9}

[Operators were so named because they allow you to embed your
operational logic of an application into an automated manager running on
Kubernetes/OpenShift.]{.c6}

## The Operator SDK, and a quick overview of Ansible Operators

[Red Hat created the [[Operator
Framework](https://blog.openshift.com/introducing-the-operator-framework/%26sa=D%26ust=1563546779219000){.c8}]{.c9} to
make the job of creating and managing operators easier across their full
lifetime. As part of the framework, the Operator SDK is tasked with
creating and building operators in an automated manner for users. Over
time it has grown to add several operator types. In 2018, we began work
on adding the Ansible Operator type to the SDK. We want to make it
easier to build operators in Kubernetes environments based on
Ansible.]{.c16}

### Why use Ansible for Operators?

[At first, operators were written in Golang. This immediately sets the
bar somewhat high for anyone who wants to write an operator --- someone
has to know a relatively low-level programming language to get started.
On top of this, you must also be familiar with Kubernetes internals,
such as the API and how events are generated for resources.]{.c6}

The Ansible Operator was created to address this short-coming. The
Ansible Operator consists of two main pieces:

1.  [A small chunk of Golang code, which handles the interface between
    Kubernetes/OpenShift and the operator.]{.c6}
2.  A container, which receives events from the above code and runs
    Ansible Playbooks as required.

[That\'s it! The Ansible and Operator SDK abstract away all of the
difficult parts of writing an operator and allows you to focus on what
matters --- managing your applications. If you already have a large base
of Ansible knowledge in your organization, you can immediately begin
managing applications using Ansible Operator. A further added bonus of
using Ansible for your operators is that you immediately have access to
any module that Ansible can run. This allows folks to incorporate
off-cluster management tasks related to your application. For
example:]{.c6}

1.  Creating DNS entries for your newly deployed applications
2.  Spinning up resources external to your cluster, such as storage or
    networking
3.  More easily do off-site backups to external cloud services
4.  Manage external load balancing based on custom metrics

[There are a number of possibilities that Kubernetes Operators written
with Ansible can provide a potential solution for.]{.c6}

## Creating a Kubernetes Operator with Ansible from scratch

First, [[install the Operator
SDK](https://github.com/operator-framework/operator-sdk/blob/master/doc/user/install-operator-sdk.md){.c8}]{.c9}[ following
their instructions. Once the install is complete, we can create a new
operator with the following command:]{.c6}

    $ operator-sdk new test-operator \
        --api-version=test.ansible-operator.com/v1 \
        --kind=Test \
        --type=ansible

    INFO[0000] Creating new Ansible operator 'test-operator'.
    ...
    INFO[0000] Project creation complete.

    $ cd test-operator/

## Kubernetes Operator with Ansible structure and files

[Now that we have our Operator skeleton, let\'s take a look at some of
the main files used when deploying Operators in general, as well as what
the Ansible Operator type generated specifically. These are:]{.c19}

1.  [The watches.yaml file]{.c19}
2.  [The build directory]{.c19}
3.  [The deploy directory]{.c19}
4.  [The roles directory]{.c19}[\
    ]{.c19}

One other directory is present here as well: the molecule directory,
which contains files to automate testing your roles/playbooks
using [[Molecule](https://molecule.readthedocs.io/en/stable/%26sa=D%26ust=1563546779225000){.c8}]{.c9}.
We will not be covering the use of Molecule here it's noted for the sake
of being complete[.]{.c6}

If you run [ls -l]{.c7 style="font-family: 'courier new', courier;"} in
the above [test-operator]{.c7
style="font-family: 'courier new', courier;"}[[ ]{style="font-family: 'courier new', courier;"}directory,
you see these files/directories there after creating the new operator
skeleton.]{.c6}

### The watches.yaml file

[This file is used by the Ansible Operator to tell Kubernetes/OpenShift
which custom resources (based on the Group/Version/Kind fields) the
operator is responsible in handling. It is the glue that ties our custom
code to the Kubernetes API:]{.c6}

    $ cat watches.yaml
    ---
    - version: v1
      group: test.ansible-operator.com
      kind: Test
      role: /opt/ansible/roles/test

specifying any other playbook boilerplate. However if you are running
more than one role in your operator you can change that line to be:

    playbook: /opt/ansible/playbook.yaml

Also, you\'ll need to tweak the [build/Dockerfile]{.c7
style="font-family: 'courier new', courier;"}[ (more on this below) to
copy the playbook into the container so add this line:]{.c6}

    COPY playbook.yaml ${HOME}/playbook.yaml

[You would then create the specified playbook in the same directory as
the [watches.yaml]{style="font-family: 'courier new', courier;"}
file.]{.c6}

### The build directory

This directory contains a few files related to building the operator
artifact. Because operators are just another application to
OpenShift/Kubernetes, this artifact is a container built using
a [Dockerfile]{.c7 style="font-family: 'courier new', courier;"}[. The
other files here are related to testing via Molecule, which we are not
going to cover in this blog series.]{.c6}

The [Dockerfile]{style="font-family: 'courier new', courier;"} is very
simple, so we won\'t delve into it much other than to say it is based on
the ansible-operator image
from [[quay.io](https://quay.io/%26sa=D%26ust=1563546779229000){.c8
rel=" noopener"}]{.c9}[, and copies the roles and watches.yml file into
the container image.]{.c6}

### The deploy directory

This directory contains YAML files for deploying the operator into
OpenShift/K8s using the [oc]{.c7
style="font-family: 'courier new', courier;"} or [kubectl]{.c7
style="font-family: 'courier new', courier;"}[ CLI commands.]{.c6}

The CustomResourceDefinition (CRD) and CustomResource (CR) are defined
in the [deploy/crds/]{.c7
style="font-family: 'courier new', courier;"} directory. The CRD is what
the [watches.yaml]{.c7
style="font-family: 'courier new', courier;"}[ file references, meaning
all instances (CRs) of this definition will be controlled by our
operator.]{.c6}

The CRD is defined in [deploy/crds/test_v1_test_crd.yaml]{.c7
style="font-family: 'courier new', courier;"}[ and is mostly boilerplate
for OpenShift/Kubernetes:]{.c6}

    $ cat deploy/crds/test_v1_test_crd.yaml
    apiVersion: apiextensions.k8s.io/v1beta1
    kind: CustomResourceDefinition
    metadata:
      name: tests.test.ansible-operator.com
    spec:
      ...

You can see the operator-sdk command above filled in most of these
fields with the values we specified. By themselves, CRDs are not very
useful, you need actual instances of what they define --- this is what
CustomResources do. Our CustomResource (CR) is defined
in [deploy/crds/test_v1_test_cr.yaml]{.c7
style="font-family: 'courier new', courier;"}[, and is relatively short
(compared to the other YAML files, anyway):]{.c6}

    $ cat deploy/crds/test_v1_test_cr.yaml 
    apiVersion: test.ansible-operator.com/v1
    kind: Test
    metadata:
      name: example-test
    spec:
      size: 3

Each of the values set under the spec entry become variables passed into
Ansible as extra variables. Using these, we can customize the behavior
of our operator. The default example creates an entry named size, which
we can use in our roles to dynamically scale the application our
operator is managing.

The [deploy/role.yaml]{style="font-family: 'courier new', courier;"} and
[deploy/role_binding.yaml]{style="font-family: 'courier new', courier;"}
(not shown), define some RBAC controls which give your login access to
manage the custom resources defined above. Role Based Access Control
(RBAC) is not covered in this post, so again we\'re just mentioning them
for completeness.

Finally, the
[deploy/operator.yaml]{style="font-family: 'courier new', courier;"}:

    $ cat deploy/operator.yaml 
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: test-operator
    spec:
      ...

[This file is quite long, but mainly it creates a new Deployment
resource in OpenShift/Kubernetes, which helps ensure that our operator
stays up and running.]{.c6}

### The roles directory

[This is the directory where you place any roles you wish to include
with your operator, and should be familiar to experienced Ansible users.
As noted above, this directory is copied completely into the Ansible
Operator container, and roles here can be referenced in the watches.yaml
file or other playbooks you include.]{.c6}

Roles commonly use the [k8s]{.c7 .c14
style="font-family: 'courier new', courier;"}[ module (included in Red
Hat Ansible Automation since the 2.6 release) to manage resources on the
cluster. If you are familiar with Kubernetes resource files, this module
will be very intuitive (the YAML from a resource file can be copy/pasted
directly as the input to this module). To learn more, you can read the
documentation for the k8s module here:]{.c6}

[[https://docs.ansible.com/ansible/latest/modules/k8s_module.html](https://docs.ansible.com/ansible/latest/modules/k8s_module.html%26sa=D%26ust=1563546779234000){.c8
rel=" noopener"}]{.c9}

## Summary

This concludes our deep dive into operators, Operator SDK, and Ansible
Operator creation and structure. Operators written using Ansible give
you the power of operators in general, while allowing you to leverage
preexisting Ansible expertise to quickly get up to speed on deploying
applications on OpenShift or Kubernetes.
