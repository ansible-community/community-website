---
title: "Bullhorn #46"
date: 2022-02-17 21:00 UTC
tags: news
category: bullhorn
type: text
---

![Ansible Bullhorn banner](/images/bullhorn-banner-mango.png)

*A Newsletter for the Ansible Developer Community*
*Issue #46, 2022-02-17 ([Past Issues](https://us19.campaign-archive.com/home/?u=56d874e027110e35dea0e03c1&id=d6635f5420))*

Welcome to [The Bullhorn](https://github.com/ansible/community/wiki/News#the-bullhorn), our newsletter for the Ansible developer community. If you have any questions or content you’d like to share, you're welcome to chat with us in the [Ansible Social room on Matrix](https://matrix.to/#/#social:ansible.com), and mention [`newsbot`](https://matrix.to/#/@newsbot:ansible.im) to have your news item tagged for review for the next weekly issue!

<!-- TEASER_END -->

## KEY DATES

[cybette](https://matrix.to/#/@cybette:ansible.im) shared

> * 2022-02-22: [ETA for Ansible 5.4.0 release](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_5.html)
> * 2022-02-22: [DaWGs meeting](https://github.com/ansible/community/issues/643), 16:00 UTC
> * 2022-02-23: [Community WG meeting](https://github.com/ansible/community/issues/645), 18:00 UTC (propose topics [here](https://github.com/ansible-community/community-topics/issues))
> * 2022-02-24: [Bullhorn #47 content deadline](https://github.com/ansible/community/wiki/News#the-bullhorn), 18:00 UTC
> * 2022-02-28: ETA for Ansible-Core 2.12.3, Ansible-Core 2.11.9, and Ansible-Base 2.10.18 releases (if those releases have updates)

## GENERAL NEWS UPDATES

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) contributed

> We have [updated the Ansible collection inclusion process](https://github.com/ansible-community/community-topics/issues/63). So far, completely new collections were only allowed in new major releases. With this change, new collections can be included in any minor release. We hope that this will simplify the process by removing a huge review pressure near the major releases.

[andersson007_](https://matrix.to/#/@andersson007_:matrix.org) contributed

> The [Ansible Community Package Collection Requirements](https://github.com/ansible-collections/overview/blob/main/collection_requirements.rst) were [updated](https://github.com/ansible-collections/overview/pull/196/files) by the [decision](https://github.com/ansible-community/community-topics/issues/67) of the [Steering Committee](https://github.com/ansible/community-docs/blob/main/ansible_community_steering_committee.rst).

### DevTools [↗](https://github.com/ansible/vscode-ansible)

Projects to make it easier to write and test Ansible Content. Includes [VScode extension](https://github.com/ansible/vscode-ansible), [language server](https://github.com/ansible/ansible-language-server), [ansible-lint](https://github.com/ansible-community/ansible-lint), [molecule](https://github.com/ansible-community/molecule), [ansible-navigator](https://github.com/ansible/ansible-navigator) and potentially other development goodies. To see what's planned, and how you can help checkout the [foundation-devtools project board](https://github.com/orgs/ansible/projects/86/views/4)

[Tomasz Maciążek](https://matrix.to/#/@tomaciazek:matrix.org) shared

> The [tomaciazek.ansible](https://marketplace.visualstudio.com/items?itemName=tomaciazek.ansible) VS Code extension is now officially deprecated in favor of [redhat.ansible](https://marketplace.visualstudio.com/items?itemName=redhat.ansible). The migration guide can be found either on the old extension marketplace page or [here](https://github.com/tomaciazek/vscode-ansible).

### Ansible-Core [↗](https://github.com/ansible/ansible)

The `ansible-core` package contains the base engine and a small subset of modules and plugins. To see what's planned for the next release, look at the [`ansible-core` roadmaps](https://docs.ansible.com/ansible-core/devel/roadmap/ansible_core_roadmap_index.html).

[gundalow](https://matrix.to/#/@gundalow:ansible.im) said

> The Ansible Core Team has just begun Phase 3 development for `ansible-core 2.13`, which started on 14th Feb. This means that the [ansible/ansible milestone](https://github.com/ansible/ansible/tree/milestone) branch has been advanced to the last commit of Feb 11, 2022 corresponding to [ansible/ansible@c9d3518](https://github.com/ansible/ansible/commit/c9d3518).
> 
> For a given ansible-core release, development is typically split into three phases of decreasing duration, with larger and more invasive changes targeted to be merged to `devel` in earlier phases. The `milestone` branch is updated to the contents of `devel` at the end of each development phase. This allows testing of semi-stable unreleased features on a predictable schedule without the exposure to the potential instability of the daily commit "fire hose" from `devel`.
> 
> See the [2.13](https://docs.ansible.com/ansible-core/devel/roadmap/ROADMAP_2_13.html#development-phase) roadmap for the current development milestone and release dates.

## COLLECTION UPDATES

[andersson007_](https://matrix.to/#/@andersson007_:matrix.org) shared

> [community.postgresql](https://github.com/ansible-collections/community.postgresql) [2.1.0](https://github.com/ansible-collections/community.postgresql/blob/main/CHANGELOG.rst) has been released.

[andersson007_](https://matrix.to/#/@andersson007_:matrix.org) shared

> [community.mysql](https://github.com/ansible-collections/community.mysql) [2.3.4](https://github.com/ansible-collections/community.mysql/blob/stable-2/changelogs/CHANGELOG.rst) and [3.1.1](https://github.com/ansible-collections/community.mysql/blob/main/changelogs/CHANGELOG.rst) have been released.

[jm1](https://matrix.to/#/@jm1:libera.chat) contributed

> [openstack.cloud](https://opendev.org/openstack/ansible-collections-openstack) [1.7.0](https://opendev.org/openstack/ansible-collections-openstack/src/tag/1.7.0/CHANGELOG.rst) has been released. It features three new modules baremetal_node_info, baremetal_port and baremetal_port_info which help with managing OpenStack Ironic nodes and ports.

[briantist](https://matrix.to/#/@briantist:libera.chat) contributed

> [`community.hashi_vault` version `2.3.0` has been released](https://github.com/ansible-collections/community.hashi_vault/releases/tag/2.3.0).

[markuman](https://matrix.to/#/@markuman:matrix.org) said

> [community.aws](https://github.com/ansible-collections/community.aws) 3.1.0 and 2.3.0 have been released.

[abuzachis](https://matrix.to/#/@aevelina:ansible.im) said

> [amazon.aws 3.1.1](https://github.com/ansible-collections/amazon.aws) has been released with some new features, bugfixes and a deprecation ([see changelog for details](https://github.com/ansible-collections/amazon.aws/blob/3.1.1/CHANGELOG.rst)). 3.1.0 failed to publish on Galaxy, hence, we had to bump the release version.

## HELP WANTED

[Markus @RealRockaut](https://matrix.to/#/@rockaut:matrix.org) contributed

> for [community.zabbix](https://github.com/ansible-collections/community.zabbix): With the release of Zabbix 6.0 LTS we would love to get some help on blocking issues like [with the integration of a new scripts module](https://github.com/ansible-collections/community.zabbix/issues/634). Thank you for your attention!

## PROPOSALS - DISCUSS AND VOTE!

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) contributed

> We started a discussion on which files/directories of the Ansible community package should be present on installation. Currently the package contains everything that the collection tarballs on Ansible Galaxy contain, which includes things like tests, extra documentation, CI configuration, editor and .gitignore config files, etc. All these files will (for now) still be available in the Ansible source distribution (on PyPi), but when installing with pip we want to trim it down to what users actually need and want. Combined with that we want to ship wheels for Ansible 6, which will make installing Ansible a lot faster and reduce the installation size. Please see [the discussion issue](https://github.com/ansible-community/community-topics/issues/65) for details. If you have ideas, wishes or comments, please add them!

## COMMUNITY UPDATES

[cybette](https://matrix.to/#/@cybette:ansible.im) said

> The recording and slides from my FOSDEM talk, "Lessons from 6 Virtual Ansible Contributor Summits", are now available [on the FOSDEM site](https://fosdem.org/2022/schedule/event/conference_ansible_lessons/). Speaking of Contributor Summits, we are planning the details for the next one which will probably be in April. More details to come, stay tuned! (And please reach out to me if you have any suggestions/questions on the topic!)

### Maintainers [↗](https://github.com/ansible-community)

Maintainers help to run the community!

[andersson007_](https://matrix.to/#/@andersson007_:matrix.org) contributed

> We are happy to announce that the [community.postgresql](https://github.com/ansible-collections/community.postgresql) collection has found a new maintainer - Douglas J Hunley ([hunleyd](https://github.com/hunleyd) on GitHub). Our congratulations, Douglas, and thank you for your great contribution!

## COMMUNITY EVENTS AND MEETUPS

[cybette](https://matrix.to/#/@cybette:ansible.im) said

> Join [Ansible Singapore](https://www.meetup.com/Ansible-Singapore/) group in "Ansible Virtual Meet Up - February 2022" on Thursday, Feb 24. Check the details and RSVP [here](https://www.meetup.com/Ansible-Singapore/events/284073479/).

## THAT'S ALL FOR NOW!

Have any questions you’d like to ask, or issues you’d like to see covered? Please ask in [#social:ansible.com](https://matrix.to/#/#social:ansible.com)! See you next time!
