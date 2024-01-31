---
title: "Bullhorn #59"
date: 2022-05-20 06:15 UTC
tags: news
category: bullhorn
type: text
---

![Ansible Bullhorn banner](/images/bullhorn-banner-mango.png)

*A Newsletter for the Ansible Developer Community*
*Issue #59, 2022-05-20 ([Past Issues](https://us19.campaign-archive.com/home/?u=56d874e027110e35dea0e03c1&id=d6635f5420))*

Welcome to [The Bullhorn](https://github.com/ansible/community/wiki/News#the-bullhorn), our newsletter for the Ansible developer community. If you have any questions or content you’d like to share, you're welcome to chat with us in the [Ansible Social room on Matrix](https://matrix.to/#/#social:ansible.com), and mention [`newsbot`](https://matrix.to/#/@newsbot:ansible.im) to have your news item tagged for review for the next weekly issue!

<!-- TEASER_END -->

## KEY DATES ⏱️

[cybette](https://matrix.to/#/@cybette:ansible.im) said

> * 2022-05-23: [End-of-life for upstream Ansible 2.9 and Ansible-base 2.10](https://groups.google.com/g/ansible-announce/c/kegIH5_okmg/)
> * 2022-05-23: ETA for Ansible-Core 2.12.6 and Ansible-Core 2.11.12 releases
> * 2022-05-24: [DaWGs meeting](https://github.com/ansible/community/issues/643), 15:00 UTC
> * 2022-05-25: [Community WG meeting](https://github.com/ansible/community/issues/645), 18:00 UTC (propose topics [here](https://github.com/ansible-community/community-topics/issues))
> * 2022-05-26: [Bullhorn #60 content deadline](https://github.com/ansible/community/wiki/News#the-bullhorn), 18:00 UTC
> * 2022-06-07: [ETA for Ansible 5.9.0 release](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_5.html)
> * 2022-06-21: [ETA for Ansible 6.0.0 GA](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_6.html)

## GENERAL NEWS UPDATES 🔈️

[dmsimard](https://matrix.to/#/@dmsimard:matrix.org) said

> Ansible 6.0.0a3 (including ansible-core 2.13.0) is now available for testing! It features, amongst other things, significantly improved installation performance on top of the latest updates from the included Ansible collections.
> This is a good opportunity to test the upcoming releases of both ansible and ansible-core and report feedback ahead of their releases.
> 
> You can find the release announcement on [ansible-announce](https://groups.google.com/g/ansible-announce/c/x51luOaarOk) and the changelog on [GitHub](https://github.com/ansible-community/ansible-build-data/blob/main/6/CHANGELOG-v6.rst).
> Happy automating!

## MAJOR NEW RELEASES 🏆️

### Ansible-Core [↗](https://github.com/ansible/ansible) ⚡️

The `ansible-core` package contains the base engine and a small subset of modules and plugins. To see what's planned for the next release, look at the [`ansible-core` roadmaps](https://docs.ansible.com/ansible-core/devel/roadmap/ansible_core_roadmap_index.html).

[cybette](https://matrix.to/#/@cybette:ansible.im) shared

> The general release of [ansible-core 2.13.0](https://groups.google.com/g/ansible-devel/c/ZebrihfEGZY) is now available! This release is a major release. Check out the [full changelog](https://github.com/ansible/ansible/blob/v2.13.0/changelogs/CHANGELOG-v2.13.rst) for more details.

### Ansible [↗](https://github.com/ansible-collections) 📦️

The `Ansible` package includes `ansible-core` and is a batteries-included package that provides a curated set of Ansible collections. See the [Ansible roadmaps](https://docs.ansible.com/ansible/devel/roadmap/ansible_roadmap_index.html) for future release plans.

[dmsimard](https://matrix.to/#/@dmsimard:matrix.org) shared

> Ansible 5.8.0 has been released with updates to 25 included Ansible collections 🎉
> You can find the release announcement on [ansible-announce](https://groups.google.com/g/ansible-announce/c/pT_VuSf9uS4) and the changelog on [GitHub](https://github.com/ansible-community/ansible-build-data/blob/main/5/CHANGELOG-v5.rst).
> Happy automating!

## COLLECTION UPDATES 🪄

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) contributed

> community.general 5.0.0 ([changelog](https://github.com/ansible-collections/community.general/blob/stable-5/CHANGELOG.rst#v5-0-0)) has been released. The 5.0.0 release is the first one to drop support for Ansible 2.9 and ansible-base 2.10, which allows the collection to stop shipping a large number of symlinks and use meta/runtime.yml for routing instead.

[andersson007_](https://matrix.to/#/@andersson007_:matrix.org) shared

> The [community.mysql](https://galaxy.ansible.com/community/mysql) collection versions [1.4.6](https://github.com/ansible-collections/community.mysql/blob/stable-1/CHANGELOG.rst), [2.3.7](https://github.com/ansible-collections/community.mysql/blob/stable-2/CHANGELOG.rst) and [3.2.1](https://github.com/ansible-collections/community.mysql/blob/main/CHANGELOG.rst) have been released! Thanks to [felixfontein](https://github.com/felixfontein)!

[csmart](https://matrix.to/#/@csmart:matrix.org) said

> The community.rabbitmq collection 1.2.0 version has been released!

[csmart](https://matrix.to/#/@csmart:matrix.org) contributed

> The community.rabbitmq collection 1.2.1 version has been released, the only change from 1.2.0 is to include a missing Python Software Foundation License file.

[csmart](https://matrix.to/#/@csmart:matrix.org) contributed

> The community.libvirt collection 1.1.0 version has been released!

[ompragash](https://matrix.to/#/@ompragash:ansible.im) contributed

> The [community.network](https://github.com/ansible-collections/community.network) minor releases [2.3.0](https://github.com/ansible-collections/community.network/releases/tag/2.3.0) & [3.3.0](https://github.com/ansible-collections/community.network/releases/tag/3.3.0) have been released!🎉
> Thanks to all the awesome people who contributed to them!❤️

[hunleyd](https://matrix.to/#/@hunleyd:matrix.org) shared

> `community.postgresql` has released both [1.7.4](https://github.com/ansible-collections/community.postgresql/blob/stable-1/CHANGELOG.rst) and [2.1.5](https://github.com/ansible-collections/community.postgresql/blob/main/CHANGELOG.rst) today with minor fixes. Many thanks to everyone involved!

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) contributed

> community.general 1.3.14 and 2.5.9 have been released, which are the final releases for the 1.x.y and 2.x.y release streams. Both release streams are now End of Life. Thanks to everyone who contributed to them!

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) shared

> community.docker 2.5.0 ([changelog](https://github.com/ansible-collections/community.docker/blob/main/CHANGELOG.rst#v2-5-0)) has been released with two new Docker Swarm features.

## PROPOSALS - DISCUSS AND VOTE! 🗳️

[hunleyd](https://matrix.to/#/@hunleyd:matrix.org) said

> The `community.postgresql` maintainers need your feedback! A proposal for formalizing the supported PG versions has been filed [here](https://github.com/ansible-collections/community.postgresql/issues/276) and needs your input. If adopted, the collection will issue major releases yearly and each major release will officially support the five major version of PG supported at that time. We think this will ultimately improve the collection and improve the end user's experience but *we need your input*. We look forward to hearing from everyone!

[dmsimard](https://matrix.to/#/@dmsimard:matrix.org) said

> If you happen to be using the ansible package from EPEL, we would appreciate your feedback on updating from 2.9 to the latest release of ansible 5. Please find [this thread](https://lists.fedoraproject.org/archives/list/epel-devel@lists.fedoraproject.org/thread/7RATG567ZHEY2TPJILDUNEKC23P25CZB/) for more information. Thank you!

## COMMUNITY UPDATES 👂️

[dmsimard](https://matrix.to/#/@dmsimard:matrix.org) said

> ara provides simple Ansible reporting and @dmsimard seeks your feedback, pondering on what ara 2.0 might look like in [this blog post](https://ara.recordsansible.org/blog/2022/05/19/what-might-ara-2.0-look-like/).
> Please have a look! It would be much appreciated to have feedback from users. Thank you!

## THAT'S ALL FOR NOW!

Have any questions you’d like to ask, or issues you’d like to see covered? Please ask in [#social:ansible.com](https://matrix.to/#/#social:ansible.com)! See you next time!
