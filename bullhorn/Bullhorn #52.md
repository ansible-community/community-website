---
title: "Bullhorn #52"
date: 2022-03-31 22:00 UTC
tags: news
category: bullhorn
type: text
---

![Ansible Bullhorn banner](/images/bullhorn-banner-mango.png)

*A Newsletter for the Ansible Developer Community*
*Issue #52, 2022-03-31 ([Past Issues](https://us19.campaign-archive.com/home/?u=56d874e027110e35dea0e03c1&id=d6635f5420))*

Welcome to [The Bullhorn](https://github.com/ansible/community/wiki/News#the-bullhorn), our newsletter for the Ansible developer community. If you have any questions or content you’d like to share, you're welcome to chat with us in the [Ansible Social room on Matrix](https://matrix.to/#/#social:ansible.com), and mention [`newsbot`](https://matrix.to/#/@newsbot:ansible.im) to have your news item tagged for review for the next weekly issue!

<!-- TEASER_END -->

## KEY DATES ⏱️

[cybette](https://matrix.to/#/@cybette:ansible.im) said

> * 2022-04-05: [ETA for Ansible 5.6.0 release](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_5.html)
> * 2022-04-05: [DaWGs meeting](https://github.com/ansible/community/issues/643), 15:00 UTC
> * 2022-04-06: [Community WG meeting](https://github.com/ansible/community/issues/645), 18:00 UTC (propose topics [here](https://github.com/ansible-community/community-topics/issues))
> * 2022-04-07: [Bullhorn #53 content deadline](https://github.com/ansible/community/wiki/News#the-bullhorn), 18:00 UTC
> * **2022-04-12: [Contributor Summit 2022.04](https://hackmd.io/@ansible-community/contrib-summit-202204)**
> * 2022-04-25: ETA for Ansible-Core 2.12.5 and Ansible-Core 2.11.11 releases (if those releases have updates)
> * 2022-05-23: [ETA for Ansible-Core 2.13 GA](https://docs.ansible.com/ansible-core/devel/roadmap/ROADMAP_2_13.html)
> * 2022-05-23: [End-of-life for upstream Ansible 2.9 and Ansible-base 2.10](https://groups.google.com/g/ansible-announce/c/kegIH5_okmg/)

## GENERAL NEWS UPDATES 🔈️

[cybette](https://matrix.to/#/@cybette:ansible.im) contributed

> **Ansible Contributor Summit 2022.04** is happening in less than 2 weeks! We have an amazing [list of topics](https://hackmd.io/@ansible-community/contrib-summit-202204/%2FzxOZe_FzR7a9-pw6r6_Ypg) and will be scheduling them soon. Check out the [event page](https://hackmd.io/@ansible-community/contrib-summit-202204) and join us on **[April 12, 2022 (Tuesday)](https://raw.githubusercontent.com/ansible/community/main/meetings/ical/contribsummit202204.ics)** from 12:00 UTC.

### Ansible-Core [↗](https://github.com/ansible/ansible) ⚡️

The `ansible-core` package contains the base engine and a small subset of modules and plugins. To see what's planned for the next release, look at the [`ansible-core` roadmaps](https://docs.ansible.com/ansible-core/devel/roadmap/ansible_core_roadmap_index.html).

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) shared

> In ansible/ansible, the `stable-2.13` branch has been created ([more infos](https://github.com/ansible-collections/news-for-maintainers/issues/14)), and the version of the `devel` branch has been bumped to 2.14.0.dev0 ([more infos](https://github.com/ansible-collections/news-for-maintainers/issues/13)).

## MAJOR NEW RELEASES 🏆️

### Ansible-Core [↗](https://github.com/ansible/ansible) ⚡️

The `ansible-core` package contains the base engine and a small subset of modules and plugins. To see what's planned for the next release, look at the [`ansible-core` roadmaps](https://docs.ansible.com/ansible-core/devel/roadmap/ansible_core_roadmap_index.html).

[cybette](https://matrix.to/#/@cybette:ansible.im) shared

> [ansible-core 2.12.4 and ansible-core 2.11.10](https://groups.google.com/g/ansible-devel/c/PWA8uP_suwg) have been released.

### Antsibull [↗](https://github.com/ansible-community/antsibull) 🐂

Tooling for building the `Ansible` package and collection documentation.

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) shared

> antsibull 0.42.0 has (finally) been released! It contains several new docs related features, most importantly support for collection links files, improvements for the attributes table, and a more stable docs parsing backend for ansible-core 2.13+. It also contains some improvements for building Ansible 6. ([Changelog](https://github.com/ansible-community/antsibull/blob/main/CHANGELOG.rst#v0-42-0))

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) contributed

> antsibull 0.43.0 has been released ([changelog](https://github.com/ansible-community/antsibull/blob/main/CHANGELOG.rst#v0-43-0)). Collection extra docs linting capability has been added to antsibull-docs, as antsibull-lint will be deprecated in the next minor release.

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) said

> antsibull-changelog 0.15.0 has been released ([changelog](https://github.com/ansible-community/antsibull-changelog/blob/main/CHANGELOG.rst#v0-15-0)). The changelogs/changelog.yaml file format linting capability from antsibull-lint was added to antsibull-changelog, as antsibull-lint will be deprecated soon.

## COLLECTION UPDATES 🪄

[markuman](https://matrix.to/#/@markuman:matrix.org) contributed

> [community.aws 2.4.0](https://github.com/ansible-collections/community.aws/releases/tag/2.4.0) has just been released.

[LowlyDBA](https://matrix.to/#/@LowlyDBA:libera.chat) said

> New collection for SQL Server management available on Galaxy. The first release of [lowlydba.sqlserver](https://github.com/lowlydba/lowlydba.sqlserver) is now live!

[Mandar Kulkarni](https://matrix.to/#/@mandkulk:matrix.org) said

> [amazon.aws 2.2.0](https://github.com/ansible-collections/amazon.aws/tree/2.2.0) has been released with  bug-fixes (see [changelog](https://github.com/ansible-collections/amazon.aws/blob/2.2.0/CHANGELOG.rst) for details).

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) contributed

> [community.docker 2.3.0](https://github.com/ansible-collections/community.docker/blob/main/CHANGELOG.rst#v2-3-0) and [community.docker 1.10.7](https://github.com/ansible-collections/community.docker/blob/stable-1/CHANGELOG.rst#v1-10-7) have been released with new features and bugfixes for the connection plugins. This mostly affects ansible-core 2.13 compatibility.

[briantist](https://matrix.to/#/@briantist:libera.chat) shared

> [`community.hashi_vault` version `2.4.0`](https://github.com/ansible-collections/community.hashi_vault/releases/tag/2.4.0) has been released.

## COMMUNITY UPDATES 👂️

[dmsimard](https://matrix.to/#/@dmsimard:matrix.org) shared

> ara records ansible 1.5.8 has been released! This new version brings fixes as well as general maintenance work to address python and dependency deprecations while adding a few features. Check out the [highlights on the blog](https://ara.recordsansible.org/blog/2022/03/31/announcing-the-release-of-ara-1.5.8/) or find the full changelog on GitHub: https://github.com/ansible-community/ara/releases/tag/1.5.8

## COMMUNITY EVENTS AND MEETUPS 📅

[cybette](https://matrix.to/#/@cybette:ansible.im) said

> Join [London virtual meetup on 19th April 2022](https://www.meetup.com/Ansible-London/events/284846000/) and hear about ansible-lint's future, deploying an OpenStack infrastructure with Ansible, and migration from Puppet to Ansible.

[dmsimard](https://matrix.to/#/@dmsimard:matrix.org) contributed

> We'll have our first Ansible Montreal meetup in person since the beginning of the pandemic! Presentations will be in French and available in streaming if you can't make it. Sign up here for the April 21 meetup: https://www.meetup.com/Ansible-Montreal/events/284804996/

## THAT'S ALL FOR NOW!

Have any questions you’d like to ask, or issues you’d like to see covered? Please ask in [#social:ansible.com](https://matrix.to/#/#social:ansible.com)! See you next time!
