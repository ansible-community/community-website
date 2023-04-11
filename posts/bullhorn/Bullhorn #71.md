---
title: "Bullhorn #71"
date: 2022-08-26 14:00 UTC
tags: news
category: bullhorn
type: text
---

![Ansible Bullhorn banner](/images/bullhorn-banner-mango.png)

*A Newsletter for the Ansible Developer Community*
*Issue #71, 2022-08-26 ([Past Issues](https://us19.campaign-archive.com/home/?u=56d874e027110e35dea0e03c1&id=d6635f5420))*

Welcome to [The Bullhorn](https://github.com/ansible/community/wiki/News#the-bullhorn), our newsletter for the Ansible developer community. If you have any questions or content you’d like to share, you're welcome to chat with us in the [Ansible Social room on Matrix](https://matrix.to/#/#social:ansible.com), and mention [`newsbot`](https://matrix.to/#/@newsbot:ansible.im) to have your news item tagged for review for the next weekly issue!

<!-- TEASER_END -->

## KEY DATES ⏱️

[cybette](https://matrix.to/#/@cybette:ansible.im) shared

> * 2022-08-30: [DaWGs meeting](https://github.com/ansible/community/issues/643), 15:00 UTC
> * 2022-08-31: [Community WG meeting](https://github.com/ansible/community/issues/645), 18:00 UTC (propose topics [here](https://github.com/ansible-community/community-topics/issues))
> * 2022-09-01: [Bullhorn #72 content deadline](https://github.com/ansible/community/wiki/News#the-bullhorn), 18:00 UTC
> * 2022-09-12: ETA for Ansible-Core 2.13.4 and Ansible-Core 2.12.9 releases (if those releases have updates)
> * 2022-09-13: [ETA for Ansible 6.4.0 release](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_6.html)
> * 2022-10-17: [Ansible Contributor Summit 2022.10](https://ansiblecs202210.eventbrite.com/?aff=hackmd)
> * 2022-10-18/19: [AnsibleFest 2022](https://www.ansible.com/ansiblefest?sc_cid=7013a000002i5g3AAA)

## GENERAL NEWS UPDATES 🔈️

[andersson007_](https://matrix.to/#/@andersson007_:matrix.org) said

> Hello everyone!
> The first collection inclusion request review day announced in [Bullhorn #70](https://mailchi.mp/redhat/the-bullhorn-70) and which happened on 23 August, 2022, was successful: we reviewed 5 collections!
> 
> Special thanks to [mariolenz](https://github.com/mariolenz), [briantist](https://github.com/briantist) and [Don Naro](https://github.com/oraNod) for the great job they did!
> See you all in the next event;)

## MAJOR NEW RELEASES 🏆️

[john-westcott-iv](https://matrix.to/#/@john-westcott-iv:ansible.im) contributed

> We're happy to announce that the next release of AWX, version [21.5.0](https://github.com/ansible/awx/releases/tag/21.5.0) is now available!
> Some notable features include:
> 
> * Add a graph to show database connections being used
> * Refactors and redesigns workflow approval to improve UX
> * Add Help Text with documentation link to Notification Templates page
> * Allow for passing multiple items for values and roles when configuring SAML auth
> * Task manager refactor
> * Easier review workflow output
> * Wait 60 seconds before scaling down a worker
> * Further resiliency changes, specifically focused on case of database going offline
> * Complex schedules UI
> * Add metric for task manager on\_commit calls
> * Add more graphs for task manager refactor
> * Altering events relationship to hosts to increase performance
> * add help command to make
> * feature\_request\_form\_update
> * Added more context to subscription details and rearrange the order of some of the fields
> * Modifying AWX collection to allow connection to IPv6 hosts.
> * Implement Generic OIDC Provider
> 
> In addition AWX Operator version [0.27.0](https://github.com/ansible/awx-operator/releases/tag/0.27.0) has also been released!
> Some notable features include:
> 
> * configure callback receiver workers based on CPU
> * Upgrade to Operator SDK v1.22.2
> 
> Please see the releases pages for more details:
> AWX: https://github.com/ansible/awx/releases/tag/21.5.0
> Operator: https://github.com/ansible/awx-operator/releases/tag/0.27.0

### Ansible [↗](https://github.com/ansible-collections) 📦️

The `Ansible` package includes `ansible-core` and is a batteries-included package that provides a curated set of Ansible collections. See the [Ansible roadmaps](https://docs.ansible.com/ansible/devel/roadmap/ansible_roadmap_index.html) for future release plans.

[Christian Adams](https://matrix.to/#/@rooftopcellist:matrix.org) contributed

> Ansible 6.3.0 is out!❤️
> 🔗https://groups.google.com/g/ansible-announce/c/PSbAe3qmQ0s
> 
> 💽You can install it by running the following command or download the release tarball directly from [pypi](https://pypi.python.org/packages/source/a/ansible/ansible-6.3.0.tar.gz):
> 
> ```
> pip install ansible==6.3.0 --user
> ```
> 
> 🔆Try the all new `ansible-community` command-line utility added in Ansible 6 that allows to print the version of the Ansible Community package:
> 
> ```
> $ ansible-community --version
> Ansible community version 6.3.0
> ```
> 
> ➡️Check [Release Notes📦️🗒️](https://github.com/ansible-community/ansible-build-data/blob/main/6/CHANGELOG-v6.rst) and [Ansible 6 Porting Guide](https://docs.ansible.com/ansible/devel/porting_guides/porting_guide_6.html) for more details!

## COLLECTION UPDATES 🪄

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) shared

> community.general 5.5.0 ([changelog](https://github.com/ansible-collections/community.general/blob/stable-5/CHANGELOG.rst#v5-5-0)) has been released with new features and bugfixes.

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) said

> community.sops 1.3.0 ([changelog](https://github.com/ansible-collections/community.sops/blob/main/CHANGELOG.rst#v1-3-0)) has been released with a new feature to work around an awx information leak when using the community.sops.sops vars plugin.

[briantist](https://matrix.to/#/@briantist:libera.chat) shared

> [`community.hashi_vault` version `3.2.0`](https://github.com/ansible-collections/community.hashi_vault/releases/tag/3.2.0) has been released with [support for the `azure` auth method](https://github.com/ansible-collections/community.hashi_vault/pull/293), thanks to new contributor [@jchenship](https://github.com/jchenship). This release also includes retries on HTTP 412 and a bugfix affecting `requests>=2.28.0`.

[mariolenz](https://matrix.to/#/@mariolenz:matrix.org) said

> The servicenow.servicenow collection has been deprecated by its maintainers and [will be removed from Ansible 7](https://github.com/ansible-community/community-topics/issues/124). It can still be installed manually, but it is suggested to swich to [servicenow.itsm](https://galaxy.ansible.com/servicenow/itsm) instead.

### Unmaintained Collections

[mariolenz](https://matrix.to/#/@mariolenz:matrix.org) contributed

> It looks like the [dellemc.os6](https://github.com/ansible-collections/dellemc.os6) collection is effectively unmaintained. According to the current [community guidelines for collections](https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst#unmaintained-collections), we consider removing it in a future version of the Ansible community package. Please see [Unmaintained collection: dellemc.os6](https://github.com/ansible-community/community-topics/issues/132) for more information or to announce that you're interested in taking over the maintenance of (a fork of) `dellemc.os6`.
> 
> At least one month after this announcement appears here and in the [collection's issue tracker](https://github.com/ansible-collections/dellemc.os6/issues/54), the Ansible Community Steering Committee will vote on whether this collection is considered unmaintained and will be removed, or whether it will be kept. If it will be removed, this will happen earliest in Ansible 8.0.0. Please note that you can still manually install the collection with `ansible-galaxy collection install dellemc.os6` even when it has been removed from Ansible.

[mariolenz](https://matrix.to/#/@mariolenz:matrix.org) contributed

> It looks like the [dellemc.os9](https://github.com/ansible-collections/dellemc.os9) collection is effectively unmaintained. According to the current [community guidelines for collections](https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst#unmaintained-collections), we consider removing it in a future version of the Ansible community package. Please see [Unmaintained collection: dellemc.os9](https://github.com/ansible-community/community-topics/issues/133) for more information or to announce that you're interested in taking over the maintenance of (a fork of) `dellemc.os9`.
> 
> At least one month after this announcement appears here and in the [collection's issue tracker](https://github.com/ansible-collections/dellemc.os9/issues/33), the Ansible Community Steering Committee will vote on whether this collection is considered unmaintained and will be removed, or whether it will be kept. If it will be removed, this will happen earliest in Ansible 8.0.0. Please note that you can still manually install the collection with `ansible-galaxy collection install dellemc.os9` even when it has been removed from Ansible.

[mariolenz](https://matrix.to/#/@mariolenz:matrix.org) shared

> It looks like the [dellemc.os10](https://github.com/ansible-collections/dellemc.os10) collection is effectively unmaintained. According to the current [community guidelines for collections](https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst#unmaintained-collections), we consider removing it in a future version of the Ansible community package. Please see [Unmaintained collection: dellemc.os10](https://github.com/ansible-community/community-topics/issues/134) for more information or to announce that you're interested in taking over the maintenance of (a fork of) `dellemc.os10`.
> 
> At least one month after this announcement appears here and in the [collection's issue tracker](https://github.com/ansible-collections/dellemc.os10/issues/136), the Ansible Community Steering Committee will vote on whether this collection is considered unmaintained and will be removed, or whether it will be kept. If it will be removed, this will happen earliest in Ansible 8.0.0. Please note that you can still manually install the collection with `ansible-galaxy collection install dellemc.os10` even when it has been removed from Ansible.

## PROPOSALS - DISCUSS AND VOTE! 🗳️

[mariolenz](https://matrix.to/#/@mariolenz:matrix.org) shared

> Please share your opinion on [removing collections that announce themselves as being unmaintained or deprecated](https://github.com/ansible-community/community-topics/issues/130).

## COMMUNITY EVENTS AND MEETUPS 📅

[cybette](https://matrix.to/#/@cybette:ansible.im) said

> ### Ansible Singapore Meetup
> 
> Hear about "Ansible Loves VSCode" and "Ansible and Python" in the first in-person meetup in 3 years with [Ansible Singapore](https://www.meetup.com/ansible-singapore/)! Check out the details of this [August 29 meetup @ Red Hat SG Office](https://www.meetup.com/ansible-singapore/events/287781210/) and RSVP.
> 
> ### Ansible Atlanta Meetup
> 
> Join [Ansible Atlanta](https://www.meetup.com/ansible-atlanta/) in their next meetup on September 8 to [Learn about Ansible Navigator](https://www.meetup.com/ansible-atlanta/events/287638006/). Check out the details in the links and RSVP.

## THAT'S ALL FOR NOW!

Have any questions you’d like to ask, or issues you’d like to see covered? Please ask in [#social:ansible.com](https://matrix.to/#/#social:ansible.com)! See you next time!
