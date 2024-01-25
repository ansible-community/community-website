---
title: "Bullhorn #76"
date: 2022-09-30 17:45 UTC
tags: news
category: bullhorn
type: text
---

![Ansible Bullhorn banner](/images/bullhorn-banner-mango.png)

*A Newsletter for the Ansible Developer Community*
*Issue #76, 2022-09-30 ([Past Issues](https://us19.campaign-archive.com/home/?u=56d874e027110e35dea0e03c1&id=d6635f5420))*

Welcome to [The Bullhorn](https://github.com/ansible/community/wiki/News#the-bullhorn), our newsletter for the Ansible developer community. If you have any questions or content you’d like to share, you're welcome to chat with us in the [Ansible Social room on Matrix](https://matrix.to/#/#social:ansible.com), and mention [`newsbot`](https://matrix.to/#/@newsbot:ansible.im) to have your news item tagged for review for the next weekly issue!

<!-- TEASER_END -->

## KEY DATES ⏱️

[cybette](https://matrix.to/#/@cybette:ansible.im) said

> * 2022-10-04: [ETA for Ansible 6.5.0 release](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_6.html)
> * 2022-10-04: [DaWGs meeting](https://github.com/ansible/community/issues/643), 15:00 UTC
> * 2022-10-05: [Community WG meeting](https://github.com/ansible/community/issues/645), 18:00 UTC (propose topics [here](https://github.com/ansible-community/community-topics/issues))
> * 2022-10-06: [Bullhorn #77 content deadline](https://github.com/ansible/community/wiki/News#the-bullhorn), 18:00 UTC
> * 2022-10-10: ETA for Ansible-Core 2.13.5 and Ansible-Core 2.12.10 releases (if those releases have updates)
> * 2022-10-12: [Community topic: List any backwards incompatible collection releases that beta1 should try to accommodate](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_7.html)
> * **2022-10-17: [Ansible Contributor Summit 2022.10](https://hackmd.io/@ansible-community/cs202210-agenda)**
> * 2022-10-17: [ansible-core 2.14 release candidate 1](https://docs.ansible.com/ansible-core/devel/roadmap/ROADMAP_2_14.html)
> * 2022-10-18: [Ansible-7.0.0 alpha2](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_7.html)
> * **2022-10-18/19: [AnsibleFest 2022](https://www.ansible.com/ansiblefest?sc_cid=7013a000002i5g3AAA)**

## GENERAL NEWS UPDATES 🔈️

### Ansible [↗](https://github.com/ansible-collections) 📦️

The `Ansible` package includes `ansible-core` and is a batteries-included package that provides a curated set of Ansible collections. See the [Ansible roadmaps](https://docs.ansible.com/ansible/devel/roadmap/ansible_roadmap_index.html) for future release plans.

[chadams](https://matrix.to/#/@chadams:ansible.im) contributed

> Ansible 7.0.0a1 (first alpha release) is out! ❤️
> 🔗[https://groups.google.com/g/ansible-devel/c/iXPDK5udh7Y](https://groups.google.com/g/ansible-devel/c/iXPDK5udh7Y)
> 
> 💽You can install it by running the following command or download the release tarball directly from [pypi](https://pypi.python.org/packages/source/a/ansible/ansible-7.0.0a1.tar.gz):
> 
> ```
> pip install ansible==7.0.0a1 --user
> ```
> 
> 🔆 Note: Ansible 7 requires Python 3.9 on the controller, same as ansible-core 2.14.
> 
> ➡️ Check [Release Notes📦️🗒️](https://github.com/ansible-community/ansible-build-data/blob/main/7/CHANGELOG-v7.rst) and [Ansible 7 Porting Guide](https://docs.ansible.com/ansible/devel/porting_guides/porting_guide_7.html) for more details!

[samccann](https://matrix.to/#/@samccann:ansible.im) shared

> ### Hacktoberfest
> 
> Hacktoberfest is coming! Consider adding the topic to your repository to get some community help with your easier issues for this month-long hackfest. See the maintainers section at https://hacktoberfest.com/participation/ for details.

## MAJOR NEW RELEASES 🏆️

### Antsibull [↗](https://github.com/ansible-community/antsibull) 🐂

Tooling for building the `Ansible` package and collection documentation.

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) contributed

> antsibull 0.50.0 ([changelog](https://github.com/ansible-community/antsibull/blob/main/CHANGELOG.rst#v0-50-0)) was released with new features and bugfixes for Ansible 6.x.0 and Ansible 7.x.0.

### Ansible-Core [↗](https://github.com/ansible/ansible) ⚡️

The `ansible-core` package contains the base engine and a small subset of modules and plugins. To see what's planned for the next release, look at the [`ansible-core` roadmaps](https://docs.ansible.com/ansible-core/devel/roadmap/ansible_core_roadmap_index.html).

[cybette](https://matrix.to/#/@cybette:ansible.im) shared

> The first beta release of ansible-core 2.14.0b1 is now available! This is a major release. Find out how to get it and check out the full changelog: https://groups.google.com/g/ansible-devel/c/gCZ44HW1zAc

## PROPOSALS - DISCUSS AND VOTE! 🗳️

[mariolenz](https://matrix.to/#/@mariolenz:matrix.org) shared

> As mentioned in [The Bullhorn #71](https://mailchi.mp/redhat/the-bullhorn-71), we consider `dellemc.os6` an effectively unmaintained collection. Therefore, we’ve opened a community / steering committee [vote](https://github.com/ansible-community/community-topics/discussions/139) on removing it from the Ansible 8 community package.

[mariolenz](https://matrix.to/#/@mariolenz:matrix.org) said

> As mentioned in [The Bullhorn #71](https://mailchi.mp/redhat/the-bullhorn-71), we consider `dellemc.os10` an effectively unmaintained collection. Therefore, we’ve opened a community / steering committee [vote](https://github.com/ansible-community/community-topics/discussions/141) on removing it from the Ansible 8 community package.

[mariolenz](https://matrix.to/#/@mariolenz:matrix.org) contributed

> As mentioned in [The Bullhorn #71](https://mailchi.mp/redhat/the-bullhorn-71), we consider `dellemc.os9` an effectively unmaintained collection. Therefore, we’ve opened a community / steering committee [vote](https://github.com/ansible-community/community-topics/discussions/140) on removing it from the Ansible 8 community package.

## COMMUNITY EVENTS AND MEETUPS 📅

[cybette](https://matrix.to/#/@cybette:ansible.im) said

> [Ansible New Zealand](https://www.meetup.com/ansible-new-zealand/) is having an online meetup on October 6, 2022 at 11:00 NZST. There'll be 2 talks: AAP2 (Ansible Automation Platform) by Ashor Benjamin and Execution Environments (EE) through Ansible Builder by Feliz Karnadi. Check out the details and RSVP [here](https://www.meetup.com/ansible-new-zealand/events/288591399/).

## THAT'S ALL FOR NOW!

Have any questions you’d like to ask, or issues you’d like to see covered? Please ask in [#social:ansible.com](https://matrix.to/#/#social:ansible.com)! See you next time!
