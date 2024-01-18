---
author: Abhijeet Kasurde
date: 2020-11-04 00:00 UTC
description: We recently released the kubernetes.core 1.1, our first Red
  Hat Certified Content Collection release, for general use. A big part
  of the new content that has been introduced is support for automating
  Helm operations.
lang: en-us
title: Automating Helm using Ansible
---

# Automating Helm using Ansible

Increasing business demands are driving the need for increased
automation to support rapid, yet stable, and reliable deployments of
applications and supporting infrastructure. Kubernetes and cloud-native
technologies are no different. For the Kubernetes platform, Helm is the
standard means of packaging, configuring and deploying applications and
services onto any cluster.

We recently released the kubernetes.core 1.1, our first Red Hat
Certified Content Collection release, for general use. A big part of the
new content that has been introduced is support for automating Helm
operations. In this blog post, I will show you some common scenarios for
its use in your automation.

Please note that prior to the release of kubernetes.core 1.1, its
contents were released as community.kubernetes. With this content
becoming Red Hat support and certified content, a name change was in
order. We are in
[the process of making that transition](https://github.com/ansible-collections/community.kubernetes/issues/221). 

# A Quick Introduction to Helm

Helm is an open source tool used for packaging and deploying
applications on Kubernetes. It is often called Kubernetes Package
Manager. It is widely adopted by the Kubernetes community and the Cloud
Native Computing Foundation (CNCF) graduate project.

Helm simplifies deployment of the applications by abstracting many of
the complexities. This enables easier adoption and allows teams to be
more productive.

Helm is designed as a Package Manager specifically for Kubernetes. It
supports operations like install, remove, upgrade, rollback and
downgrade for Kubernetes applications. As you may know, Kubernetes
applications can be defined using declarative resource files for
different Kubernetes objects like Deployment, Services, ConfigMaps,
PersistentVolumeClaims and so on. Distributing and managing Kubernetes
applications is difficult. Helm packages all Kubernetes resource files
into a format called "Charts". Chart can be considered as the Kubernetes
Package. This packaging format contains information about resource
files, dependencies information and metadata.

# Automating Helm using Ansible

You can automate your Kubernetes infrastructure using Ansible. All
Kubernetes modules are now located in the Kubernetes Collection called
kubernetes.core. This Collection also contains modules to automate Helm
and its related functionalities.

The following is the list of Helm related modules included in the
kubernetes.core Collection -

1.  **helm** - Manages K8S packages with the Helm binary
2.  **helm_info** - Gather information on Helm packages deployed inside
    the cluster
3.  **helm_plugin** - Manage Helm plugins
4.  **helm_plugin_info** - Gather information about Helm plugins
5.  **helm_repository** - Manage Helm repositories

Helm modules take advantage of the Helm binary installed on Ansible
controllers. This makes helm modules work out of the box and readily
available for the users. Unlike the previous helm module, these are 
independent of any third party Python libraries. A special thanks to
[LucasBoisserie](https://github.com/LucasBoisserie) for his
contributions.

Let us take a look at these modules used in some common scenarios.

## Scenario 1 - Adding new Helm Repository

In order to install the Helm Package, you need to have the Helm
repository added in your Kubernetes cluster. 

Let us now add a Helm Repository using helm_repository module:

```
---
- hosts: localhost
  vars:
     helm_chart_url: "https://charts.bitnami.com/bitnami"
  tasks:
      - name: Add helm repo
        kubernetes.core.helm_repository:
            name: bitnami
            repo_url: "{{ helm_chart_url }}"
```

Here, we are installing a new Helm Chart Repository by specifying URL
and name. After running this playbook, you will have Bitnami Chart
Repository installed in your environment.

```
# helm repo list
NAME     URL
stable     https://kubernetes-charts.storage.googleapis.com/
bitnami    https://charts.bitnami.com/bitnami
```

## Scenario 2 - Installing a Helm Chart

Now, we have the Helm repository configured. Let us now install nginx charts
from the Bitnami repository.

```
---
- hosts: localhost
  tasks:
     - name: Install Nginx Chart
       kubernetes.core.helm:
           name: nginx-server
           namespace: testing
           chart_ref: bitnami/nginx
```

After running this playbook, you can see nginx-server deployment running
in your *testing* environment.

```
# kubectl -n testing get deploy
NAME            READY   UP-TO-DATE   AVAILABLE   AGE
nginx-server      1/1     1            1           48s
```

## Scenario 3 - Gather information about Helm Chart installed

Gathering information about the Helm Chart is also easy using the
helm_info module.

```
---
- hosts: localhost
  tasks:
     - name: Gather information about nginx-server
       kubernetes.core.helm_info:
            name: nginx-server
            release_namespace: testing
```

Running this playbook will provide valuable information about the
installed chart such as app version, chart version, revision, status and
updated date time about the given chart.

## Scenario 4 - Install Helm Plugin

Helm allows you to enhance its functionality by providing pluggable
architecture. That means users can write plugins to enhance Helm
functionality. There is a large number of Helm plugins available. Users
can install those plugins depending on their use case and requirements.

Let us now try to install the Helm plugin called
[helm env](https://github.com/adamreese/helm-env). This helm plugin allows
users to view the environment variables available to a helm plugin.

```
---
- hosts: localhost
  tasks:
     - name: Install Helm Plugin
       kubernetes.core.helm_plugin:
           plugin_path: https://github.com/adamreese/helm-env
           state: present
           release_namespace: testing
```

## Scenario 5 - Gather information about Helm plugins

Users can gather information about installed Helm plugins from the given
Kubernetes cluster.

```
---
- hosts: localhost
  tasks:
  - name: Gather Helm plugin info
    kubernetes.core.helm_plugin_info:
        release_namespace: testing
    register: r

  - name: Print plugin version
    debug:
    msg: "{{ ( r.plugin_list | selectattr('name', 'equalto', plugin_name) | list )[0].version }}"
    vars:
    plugin_name: "env"
```

This will output all the information related to plugins from the given
namespace. Users can specify a particular plugin name to gather its
information.

# Conclusion & Next Steps

There you have it. With the Helm modules in kubernetes.core, you can
easily automate the management of Kubernetes applications in a
repeatable and reliable way. We hope you try it and let us know what you
think. Please stop by at the Ansible Kubernetes IRC channel 
#ansible-kubernetes on [Freenode](https://webchat.freenode.net/) to
provide your valuable feedback or if you need assistance with
**kubernetes.core** Collection.

In a future post, we'll cover the rest of what's new in
kubernetes.core and introduce the
[community.okd (OpenShift) Collection](https://github.com/ansible-collections/community.okd)
we are currently developing.
