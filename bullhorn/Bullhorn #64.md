---
title: "Bullhorn #64"
date: 2022-06-24 11:10 UTC
tags: news
category: bullhorn
type: text
---

![Ansible Bullhorn banner](/images/bullhorn-banner-mango.png)

*A Newsletter for the Ansible Developer Community*
*Issue #64, 2022-06-24 ([Past Issues](https://us19.campaign-archive.com/home/?u=56d874e027110e35dea0e03c1&id=d6635f5420))*

Welcome to [The Bullhorn](https://github.com/ansible/community/wiki/News#the-bullhorn), our newsletter for the Ansible developer community. If you have any questions or content you’d like to share, you're welcome to chat with us in the [Ansible Social room on Matrix](https://matrix.to/#/#social:ansible.com), and mention [`newsbot`](https://matrix.to/#/@newsbot:ansible.im) to have your news item tagged for review for the next weekly issue!

<!-- TEASER_END -->

## KEY DATES ⏱️

[cybette](https://matrix.to/#/@cybette:ansible.im) contributed

> * 2022-06-28: [ETA for Ansible 5.10.0, the final Ansible 5.x release](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_5.html)
> * 2022-06-28: [DaWGs meeting](https://github.com/ansible/community/issues/643), 15:00 UTC
> * 2022-06-29: [Community WG meeting](https://github.com/ansible/community/issues/645), 18:00 UTC (propose topics [here](https://github.com/ansible-community/community-topics/issues))
> * 2022-06-30: [Bullhorn #65 content deadline](https://github.com/ansible/community/wiki/News#the-bullhorn), 18:00 UTC
> * 2022-07-12: [ETA for Ansible 6.1.0 release](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_6.html)
> * 2022-07-15: Deadline for [CFP submission](https://reg.experiences.redhat.com/flow/redhat/rhaf22/cfp/login) for [AnsibleFest 2022](https://www.ansible.com/ansiblefest)
> * 2022-07-18: ETA for Ansible-Core 2.13.2 and Ansible-Core 2.12.8 releases

## MAJOR NEW RELEASES 🏆️

[John Westcott](https://matrix.to/#/@john-westcotti-iv:matrix.org) contributed

> We're happy to announce that [AWX version 21.2.0](https://github.com/ansible/awx/releases/tag/21.2.0) is now available!
> We're happy to announce that [AWX Operator version 0.22.0](https://github.com/ansible/awx-operator/releases/tag/0.22.0) is now available!

### Ansible-Core [↗](https://github.com/ansible/ansible) ⚡️

The `ansible-core` package contains the base engine and a small subset of modules and plugins. To see what's planned for the next release, look at the [`ansible-core` roadmaps](https://docs.ansible.com/ansible-core/devel/roadmap/ansible_core_roadmap_index.html).

[cybette](https://matrix.to/#/@cybette:ansible.im) shared

> [ansible-core 2.13.1 and ansible-core 2.12.7](https://groups.google.com/g/ansible-announce/c/SN2sp15icy8) have been released. These are maintenance releases containing numerous bugfixes.

### Antsibull [↗](https://github.com/ansible-community/antsibull) 🐂

Tooling for building the `Ansible` package and collection documentation.

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) contributed

> antsibull 0.48.0 ([changelog](https://github.com/ansible-community/antsibull/blob/main/CHANGELOG.rst#v0-48-0)) has been released with a bugfix for the release preparation command, and some improvements and breaking changes in the release role.

### Ansible [↗](https://github.com/ansible-collections) 📦️

The `Ansible` package includes `ansible-core` and is a batteries-included package that provides a curated set of Ansible collections. See the [Ansible roadmaps](https://docs.ansible.com/ansible/devel/roadmap/ansible_roadmap_index.html) for future release plans.

[ompragash](https://matrix.to/#/@ompragash:ansible.im) contributed

> **📢We are super excited to announce the major release of Ansible 6.0.0!🎉**
> [🔗https://groups.google.com/g/ansible-announce/c/yprrt94l22w](https://groups.google.com/g/ansible-announce/c/yprrt94l22w)
> 
> 💽 You can install it by running the following command or download it directly from [pypi](https://pypi.python.org/packages/source/a/ansible/ansible-6.0.0.tar.gz):
> 
> ```
> pip install ansible==6.0.0 --user
> ```
> 
> 🔆 Some of the key highlights to celebrate as part of this release are:
> 
> ➡️ Addition of four new Collections:
> * cisco.dnac (version 6.4.0)
> * community.sap (version 1.0.0)
> * community.sap_libs (version 1.1.0)
> * vmware.vmware_rest (version 2.1.5)
> 
> ➡️ New command-line utility `ansible-community` that prints the version of the Ansible Community package:
> 
> ~~~
> $ ansible-community --version
> Ansible community version 6.0.0
> ~~~
> 
> Check  [Release Notes📦️🗒️](https://github.com/ansible-community/ansible-build-data/blob/main/6/CHANGELOG-v6.rst) and [Ansible 6 Porting Guide](https://docs.ansible.com/ansible/devel/porting_guides/porting_guide_6.html) for more details on changes, improvements, new and deprecated features!!

## COLLECTION UPDATES 🪄

[abuzachis](https://matrix.to/#/@aevelina:ansible.im) shared

> [amazon.aws 3.3.1](https://github.com/ansible-collections/amazon.aws/tree/3.3.1) has been released with some utility features ([see changelog for details](https://github.com/ansible-collections/amazon.aws/blob/3.3.1/CHANGELOG.rst)).
> 
> [amazon.aws 4.0.0](https://github.com/ansible-collections/amazon.aws) has been released with some new features, bugfixes, breaking changes and deprecated features. The amazon.aws collection has also dropped support for `botocore<1.20.0` and `boto3<1.17.0` ([see changelog for details](https://github.com/ansible-collections/amazon.aws/blob/4.0.0/CHANGELOG.rst)).

[jatorcasso](https://matrix.to/#/@jatorcasso:ansible.im) said

> [community.aws 3.4.0](https://github.com/ansible-collections/community.aws/tree/3.4.0) has been released with some new features, bugfixes, and deprecated features ([see changelog for details](https://github.com/ansible-collections/community.aws/blob/3.4.0/CHANGELOG.rst)).

[tremble](https://matrix.to/#/@mchappell:matrix.org) contributed

> [community.aws 4.0.0](https://github.com/ansible-collections/community.aws/tree/4.0.0) has been released with new modules, features, bugfixes and deprecated features ([see changelog for details](https://github.com/ansible-collections/community.aws/blob/4.0.0/CHANGELOG.rst)).

## HELP WANTED 🙏

[andersson007_](https://matrix.to/#/@andersson007_:matrix.org) contributed

> The following collection inclusion requests are waiting for your review:
> * [vultr.cloud](https://github.com/ansible-collections/ansible-inclusion/discussions/44)
> * [check_point.gaia](https://github.com/ansible-collections/ansible-inclusion/discussions/34)
> * [inspur.ispim](https://github.com/ansible-collections/ansible-inclusion/discussions/47)
> * [purestorage.fusion](https://github.com/ansible-collections/ansible-inclusion/discussions/48)
> 
> See the [process description](https://github.com/ansible-collections/ansible-inclusion#review-process) to learn how to do it.
> 
> Please help the community extend the Ansible package!

## COMMUNITY UPDATES 👂️

[briantist](https://matrix.to/#/@briantist:libera.chat) shared

> [galactory](https://github.com/briantist/galactory) is a thin Ansible Galaxy front-end that uses Artifactory for its backend storage. It also supports transparently proxying to upstream Galaxy, storing those artifacts in Artifactory as well. It supports reading, discovering, and publishing collections (no role support).

## COMMUNITY EVENTS AND MEETUPS 📅

[cybette](https://matrix.to/#/@cybette:ansible.im) contributed

> [Ansible Singapore](https://www.meetup.com/Ansible-Singapore/) is meeting on Thursday, June 30, for an opinionated approach in setting up a Golden Image pipeline to build a hardened Base Image for Windows Server 2019. Check out the details of their [Ansible Virtual Meet Up - June 2022](https://www.meetup.com/ansible-singapore/events/286680970/) and RSVP.

[cybette](https://matrix.to/#/@cybette:ansible.im) said

> ### AnsibleFest and Ansible Contributor Summit
> 
> [AnsibleFest 2022](https://www.ansible.com/ansiblefest) will be in Chicago, IL (USA) this year, on **October 18 & 19**. [The call for proposals](https://reg.experiences.redhat.com/flow/redhat/rhaf22/cfp/login) is now open until **July 15, 2022**.
> 
> Content topics can include:
> * Getting Started
> * Automating Red Hat products
> * Use Case / Domain-focused (e.g. Network, Security, Cloud)
> * Audience-focused (e.g. Developers, Operations)
> * Thought Leadership
> * Community and Culture
> 
> There will be an **Ansible Contributor Summit** the day before AnsibleFest on **October 17, 2022**, where participants will be able to join both in-person (in Chicago) and online. More details about this event will be shared as we confirm them!

## THAT'S ALL FOR NOW!

Have any questions you’d like to ask, or issues you’d like to see covered? Please ask in [#social:ansible.com](https://matrix.to/#/#social:ansible.com)! See you next time!
