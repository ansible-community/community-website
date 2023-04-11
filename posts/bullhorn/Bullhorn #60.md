---
title: "Bullhorn #60"
date: 2022-05-27 19:00 UTC
tags: news
category: bullhorn
type: text
---

![Ansible Bullhorn banner](/images/bullhorn-banner-mango.png)

*A Newsletter for the Ansible Developer Community*
*Issue #60, 2022-05-27 ([Past Issues](https://us19.campaign-archive.com/home/?u=56d874e027110e35dea0e03c1&id=d6635f5420))*

Welcome to [The Bullhorn](https://github.com/ansible/community/wiki/News#the-bullhorn), our newsletter for the Ansible developer community. If you have any questions or content you’d like to share, you're welcome to chat with us in the [Ansible Social room on Matrix](https://matrix.to/#/#social:ansible.com), and mention [`newsbot`](https://matrix.to/#/@newsbot:ansible.im) to have your news item tagged for review for the next weekly issue!

<!-- TEASER_END -->

## KEY DATES ⏱️

[cybette](https://matrix.to/#/@cybette:ansible.im) contributed

> * 2022-05-31: [DaWGs meeting](https://github.com/ansible/community/issues/643), 15:00 UTC
> * 2022-06-01: [Community WG meeting](https://github.com/ansible/community/issues/645), 18:00 UTC (propose topics [here](https://github.com/ansible-community/community-topics/issues))
> * 2022-06-02: [Bullhorn #61 content deadline](https://github.com/ansible/community/wiki/News#the-bullhorn), 18:00 UTC
> * 2022-06-07: [ETA for Ansible 5.9.0 release](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_5.html)
> * 2022-06-20: ETA for Ansible-Core 2.12.7 and Ansible-Core 2.11.13 releases (if those releases have updates)
> * 2022-06-21: [ETA for Ansible 6.0.0 GA](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_6.html)

## GENERAL NEWS UPDATES 🔈️

[cybette](https://matrix.to/#/@cybette:ansible.im) shared

> [AnsibleFest 2022](https://www.ansible.com/ansiblefest) will be in Chicago, IL (USA) this year, on October 18 & 19. [CFP for AnsibleFest](https://reg.experiences.redhat.com/flow/redhat/rhaf22/cfp/login) is open until July 15, 2022.
> 
> There will be an Ansible Contributor Summit the day before AnsibleFest on October 17, 2022. More details about the event will be shared as we confirm them!

[sivel](https://github.com/sivel) shared

> As of May 23, 2022, upstream Ansible 2.9 and Ansible-base 2.10 are officially end of life. Please review the [original announcement](https://groups.google.com/g/ansible-announce/c/kegIH5_okmg/) for more information.

## MAJOR NEW RELEASES 🏆️

### Ansible-Core [↗](https://github.com/ansible/ansible) ⚡️

The `ansible-core` package contains the base engine and a small subset of modules and plugins. To see what's planned for the next release, look at the [`ansible-core` roadmaps](https://docs.ansible.com/ansible-core/devel/roadmap/ansible_core_roadmap_index.html).

[sivel](https://github.com/sivel) said

> [ansible-core 2.12.6 and ansible-core 2.11.12](https://groups.google.com/g/ansible-devel/c/qJLT-ekilPY) have been released. These are maintenance releases containing numerous bugfixes.

### Ansible [↗](https://github.com/ansible-collections) 📦️

The `Ansible` package includes `ansible-core` and is a batteries-included package that provides a curated set of Ansible collections. See the [Ansible roadmaps](https://docs.ansible.com/ansible/devel/roadmap/ansible_roadmap_index.html) for future release plans.

[dmsimard](https://matrix.to/#/@dmsimard:matrix.org) said

> Ansible 6.0.0b1 (including ansible-core 2.13.0) is now available for testing! It features, amongst other things, significantly improved installation performance on top of the latest updates from the included Ansible collections. This is a good opportunity to test the upcoming releases of both ansible and ansible-core and report feedback ahead of the stable release expected around 2022-06-21.
> 
> You can find the release announcement on [ansible-announce](https://groups.google.com/g/ansible-announce/c/r8JuHKaFZxw) and the changelog on [GitHub](https://github.com/ansible-community/ansible-build-data/blob/main/6/CHANGELOG-v6.rst).
> 
> Happy automating!

## COLLECTION UPDATES 🪄

[ompragash](https://matrix.to/#/@ompragash:ansible.im) shared

> Community Network Collection 4.0.0 has been released and is available to download!  See [changelog](https://github.com/ansible-collections/community.network/blob/stable-4/CHANGELOG.rst) for details regarding the major changes and deprecated features!🎉

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) contributed

> community.docker 2.6.0 ([changelog](https://github.com/ansible-collections/community.docker/blob/main/CHANGELOG.rst#v2-6-0)) and 1.10.10 ([changelog](https://github.com/ansible-collections/community.docker/blob/stable-1/CHANGELOG.rst#v1-10-10)) have been released.

[Hideki Saito](https://matrix.to/#/@saito-hideki:matrix.org) contributed

> ansible.posix 1.4.0 ([changelog](https://github.com/ansible-collections/ansible.posix/blob/1.4.0/CHANGELOG.rst#v1-4-0)) has been released.

[markuman](https://matrix.to/#/@markuman:matrix.org) contributed

> community.proxysql [1.4.0](https://github.com/ansible-collections/community.proxysql/releases/tag/1.4.0) has been released.

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) said

> community.routeros 2.1.0 ([changelog](https://github.com/ansible-collections/community.routeros/blob/main/CHANGELOG.rst#v2-1-0)) has been released with new modules, new features, and some bugfixes!

[andersson007_](https://matrix.to/#/@andersson007_:matrix.org) contributed

> The [cisco.dnac](https://galaxy.ansible.com/cisco/dnac) collection has been included in Ansible 5 and 6.

[briantist](https://matrix.to/#/@briantist:libera.chat) contributed

> [`community.hashi_vault` version `3.0.0`](https://github.com/ansible-collections/community.hashi_vault/releases/tag/3.0.0) has been released, dropping support for Ansible 2.9 and ansible-base 2.10, as well as removing some deprecated features.

## PROPOSALS - DISCUSS AND VOTE! 🗳️

[mariolenz](https://matrix.to/#/@mariolenz:matrix.org) contributed

> For people using the Ansible community package, there is no generic way to find out the version they are running. `ansible --version` just gives the ansible-core version, so they have to rely on their specific package manager (pip, dpkg, rpm...). If you think there should be a generic way, please add your views to the [CLI program which prints the Ansible package's version](https://github.com/ansible-community/community-topics/issues/89) discussion.

[hunleyd](https://matrix.to/#/@hunleyd:matrix.org) said

> The `community.postgresql` maintainers need your feedback! A proposal for formalizing the supported PG versions has been filed [here](https://github.com/ansible-collections/community.postgresql/issues/276) and needs your input. If adopted, the collection will issue major releases yearly and each major release will officially support the five major version of PG supported at that time. We think this will ultimately improve the collection and improve the end user's experience but *we need your input*. We look forward to hearing from everyone!

[dmsimard](https://matrix.to/#/@dmsimard:matrix.org) said

> If you happen to be using the ansible package from EPEL, we would appreciate your feedback on updating from 2.9 to the latest release of ansible 5. Please find [this thread](https://lists.fedoraproject.org/archives/list/epel-devel@lists.fedoraproject.org/thread/7RATG567ZHEY2TPJILDUNEKC23P25CZB/) for more information. Thank you!

## COMMUNITY EVENTS AND MEETUPS 📅

[cybette](https://matrix.to/#/@cybette:ansible.im) shared

> [Ansible München](https://www.meetup.com/Ansible-Munchen/) group is organizing an [Ansible SpringFest!](https://www.meetup.com/Ansible-Munchen/events/284695940/) It is happening soon on Tuesday, May 31st, starting from 18:00 CEST at Einstein Kultur. There will be 2 talks, “Ansible Automation for SAP - Deployment, Operations and Modernization” and “Ansible and Kubernetes - an alternative to Helm”. See [here](https://www.meetup.com/Ansible-Munchen/events/284695940/) for more details and RSVP.

## THAT'S ALL FOR NOW!

Have any questions you’d like to ask, or issues you’d like to see covered? Please ask in [#social:ansible.com](https://matrix.to/#/#social:ansible.com)! See you next time!
