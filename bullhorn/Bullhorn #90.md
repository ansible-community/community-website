---
title: "Bullhorn #90"
date: 2023-02-03 18:15 UTC
tags: news
category: bullhorn
type: text
---

![Ansible Bullhorn banner](/images/bullhorn-banner-mango.png)

*A Newsletter for the Ansible Developer Community*
*Issue #90, 2023-02-03 ([Past Issues](https://us19.campaign-archive.com/home/?u=56d874e027110e35dea0e03c1&id=d6635f5420))*

Welcome to [The Bullhorn](https://github.com/ansible/community/wiki/News#the-bullhorn), our newsletter for the Ansible developer community. If you have any questions or content you’d like to share, you're welcome to chat with us in the [Ansible Social room on Matrix](https://matrix.to/#/#social:ansible.com), and mention [`newsbot`](https://matrix.to/#/@newsbot:ansible.im) to have your news item tagged for review for the next weekly issue!

<!-- TEASER_END -->

## KEY DATES ⏱️

[cybette](https://matrix.to/#/@cybette:ansible.im) shared

> * **2023-02-04: [FOSDEM 2023](https://fosdem.org/2023/)**
> * **2023-02-06: [Cfgmgmtcamp 2023](https://cfgmgmtcamp.eu/ghent2023/)**
> * 2023-02-07: [DaWGs meeting](https://github.com/ansible/community/issues/678), 16:00 UTC
> * **2023-02-08: [Ansible Contributor Summit 2023.02](https://hackmd.io/@ansible-community/cs202302-planning)**
> * 2023-02-14: [DaWGs meeting](https://github.com/ansible/community/issues/678), 16:00 UTC
> * 2023-02-15: [Community WG meeting](https://github.com/ansible/community/issues/679), 19:00 UTC (propose topics [here](https://github.com/ansible-community/community-topics/issues))
> * 2023-02-16: [Bullhorn #91 content deadline](https://github.com/ansible/community/wiki/News#the-bullhorn), 18:00 UTC
> * 2023-02-27: ETA for Ansible-Core 2.14.3
> * 2023-02-28: [ETA for Ansible 7.3.0 release](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_7.html)

## GENERAL NEWS UPDATES 🔈️

[cybette](https://matrix.to/#/@cybette:ansible.im) contributed

> ### FOSDEM and CfgMgmtCamp
> 
> If you are attending [FOSDEM (Feb 4-5)](https://fosdem.org/2023/) or [CfgMgmtCamp (Feb 6-8)](https://cfgmgmtcamp.eu/ghent2023/), we will have an Ansible stand at both events! For FOSDEM, we'll be in [building K level 1](https://fosdem.org/2023/stands/). Come by and chat with members of the Ansible team and community!

[cybette](https://matrix.to/#/@cybette:ansible.im) contributed

> ### Ansible Contributor Summit 2023.02
> 
> The schedule for Ansible Contributor Summit on Feb 8 is [available](https://hackmd.io/@ansible-community/cs202302-planning#Tentative-Schedule-time-in-CET)! In addition, we're thinking of having an Ansible Community Social on Feb 7 in Ghent (as part of CfgMgmtCamp/Contributor Summit), please indidate your interest [here](https://hackmd.io/@ansible-community/cs202302-planning#Ansible-Social-Tuesday-Feb-7) by Feb 4 so we can find a location to accommodate us.
> 
> Live stream and online chat will be available as well. Check (and bookmark) the [event HackMD note](https://hackmd.io/@ansible-community/cs202302-planning) for details and updates!

[samccann](https://matrix.to/#/@samccann:ansible.im) said

> We are archiving Ansible 2.6 documentation. If you are using these docs, update bookmarks to point [here](https://docs.ansible.com/archive/ansible/2.6/). We will redirect the old link to `/latest/` docs starting next week.

## MAJOR NEW RELEASES 🏆️

### Ansible-Core [↗](https://github.com/ansible/ansible) ⚡️

The `ansible-core` package contains the base engine and a small subset of modules and plugins. To see what's planned for the next release, look at the [`ansible-core` roadmaps](https://docs.ansible.com/ansible-core/devel/roadmap/ansible_core_roadmap_index.html).

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) said

> ansible-core 2.14.2 ([changelog](https://github.com/ansible/ansible/blob/v2.14.2/changelogs/CHANGELOG-v2.14.rst#v2-14-2)) has been [released](https://groups.google.com/g/ansible-devel/c/PEBRhje74oM). For users, one important fix is that deprecations for module parameters and deprecated aliases are now shown again. This has been accidentally disabled since ansible-core 2.11. For developers, ansible-test obtained a large set of fixes and improvements, mostly regarding container handling (`--docker` argument); see the list of major changes in the changelog for some more information on this.

### Antsibull [↗](https://github.com/ansible-community/antsibull) 🐂

Tooling for building the `Ansible` package and collection documentation.

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) shared

> antsibull 0.53.0 ([changelog](https://github.com/ansible-community/antsibull/blob/main/CHANGELOG.rst#v0-53-0)) has been released with new features and bugfixes.

### Ansible [↗](https://github.com/ansible-collections) 📦️

The `Ansible` package includes `ansible-core` and is a batteries-included package that provides a curated set of Ansible collections. See the [Ansible roadmaps](https://docs.ansible.com/ansible/devel/roadmap/ansible_roadmap_index.html) for future release plans.

[chadams](https://matrix.to/#/@chadams:ansible.im) contributed

> [Ansible 7.2.0 is out!](https://groups.google.com/g/ansible-announce/c/AHhjZOU1xBg) ❤️
> 
> 💽You can install it by running the following command or download the release tarball directly from [pypi](https://pypi.python.org/packages/source/a/ansible/ansible-7.2.0.tar.gz):
> 
> ```
> pip install ansible==7.2.0 --user
> ```
> 
> ➡️ Check [Release Notes📦️🗒️](https://github.com/ansible-community/ansible-build-data/blob/main/7/CHANGELOG-v7.rst) and [Ansible 7 Porting Guide](https://docs.ansible.com/ansible/devel/porting_guides/porting_guide_7.html) for more details!

## COLLECTION UPDATES 🪄

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) said

> community.dns 2.5.0 ([changelog](https://github.com/ansible-collections/community.dns/blob/main/CHANGELOG.rst#v2-5-0)) has been released with new features, bugfixes, and an updated Public Suffix List.

[Timothy Appnel](https://matrix.to/#/@tappnel:matrix.org) contributed

> servicenow.itsm 2.1.0 has been released. Details [here](https://github.com/ansible-collections/servicenow.itsm/blob/main/CHANGELOG.rst#v2-1-0).

[jm1](https://matrix.to/#/@jakobmeng:fedora.im) shared

> A new major [release 2.0.0 of the Ansible collection for OpenStack clouds aka openstack.cloud](
> https://lists.openstack.org/pipermail/openstack-discuss/2023-February/031975.html) has been published: Massively refactored, openstacksdk 1.0 compatible, fully documented, extensively tested and new modules!

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) said

> community.general 5.8.5 ([5.8.5 changelog](https://github.com/ansible-collections/community.general/blob/stable-5/CHANGELOG.rst#v5-8-5)) and 6.3.0 ([6.3.0 changelog](https://github.com/ansible-collections/community.general/blob/stable-6/CHANGELOG.rst#v6-3-0)) have been released with new bugfixes, features, and two new modules for managing Out-Of-Band controllers with OCAPI.

[mariolenz](https://matrix.to/#/@mariolenz:matrix.org) said

> As mentioned in [The Bullhorn #84](https://mailchi.mp/redhat/the-bullhorn-84), we voted on removing `cyberark.pas` from Ansible 9. We never announced the result (which was positive) because when we were counting the votes someone from Cyberark reached out to us and promised that they will work on the collection.
> 
> Long story short, it looks like they did! So we had another [discussion and vote](https://github.com/ansible-community/community-topics/issues/180) about the collection and decided to keep it since the collection requirements are met and the collection itself looks maintained again.

[Timothy Appnel](https://matrix.to/#/@tappnel:matrix.org) shared

> I am happy to announce kubernetes.core 2.4.0 has been released with dozens of minor enhancements and fixes. Details are [here](https://github.com/ansible-collections/kubernetes.core/blob/main/CHANGELOG.rst#v2-4-0).

## HELP WANTED 🙏

[andersson007_](https://matrix.to/#/@andersson007_:matrix.org) contributed

> The [new collection inclusion requests](https://github.com/ansible-collections/ansible-inclusion/discussions/categories/new-collection-reviews) are waiting for your [reviews](https://github.com/ansible-collections/ansible-inclusion#review-process). Please help the community extend the `ansible` package!

[samccann](https://matrix.to/#/@samccann:ansible.im) shared

> Looking to help out in Ansible but not sure where to start? Take a look at some easyfix or good first issues:
> * across multiple [collections](https://github.com/search?q=user%3Aansible-collections+label%3Aeasyfix%2C%22good+first+issue%22+state%3Aopen&type=Issues )
> * for all [other](https://github.com/search?q=user%3Aansible+user%3Aansible-community+label%3Aeasyfix%2C%22good+first+issue%22+state%3Aopen&type=Issues) Ansible projects

## PROPOSALS - DISCUSS AND VOTE! 🗳️

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) said

> There is a [new community vote](https://github.com/ansible-community/community-topics/discussions/194) on the proposed [Roadmap for Ansible 8](https://github.com/ansible/ansible/pull/79598), to end on Feburary 9th, 2023.

[mariolenz](https://matrix.to/#/@mariolenz:matrix.org) said

> As mentioned in [The Bullhorn #69](https://mailchi.mp/redhat/the-bullhorn-69), we decided to remove `google.cloud` from Ansible 8 because we considered it unmaintained. Afterwards, someone from Google [announced a plan to refactor and maintain the collection again](https://github.com/ansible-community/community-topics/issues/105#issuecomment-1242367646).
> 
> Since then, there has been work on the collection and also some new releases. Therefore, we started a [vote on cancelling the removal of google.cloud from Ansible 8](https://github.com/ansible-community/community-topics/discussions/195).

## COMMUNITY UPDATES 👂️

[steampunks](https://matrix.to/#/@xlab_steampunk:matrix.org) said

> [We tested ChatGPT](https://steampunk.si/blog/chat-GPT-ansible-playbooks/) and here’s our conclusion: Although the current state of AI systems is not capable of generating production-ready Ansible Playbooks without manual writing, AI is still very useful - you just have to know how to use it.

## COMMUNITY EVENTS AND MEETUPS 📅

[Sean Sullivan](https://matrix.to/#/@ssulliva:matrix.org) contributed

> The infra config as Code collection group will have a community meeting Feb 15th. Details [here](https://github.com/redhat-cop/controller_configuration/issues/475).

[ompragash](https://matrix.to/#/@ompragash:ansible.im) shared

> 📣 We are excited to announce the upcoming **Ansible Community Day** in India!
> 
> Join us in-person for a day of presentations, workshops, and networking with other Ansible enthusiasts. Learn about the latest developments in Ansible and how it can help you automate your IT infrastructure. Don't miss out on this opportunity to connect with the Ansible community and take your skills to the next level.
> 
> Register now on [meetup.com](https://www.meetup.com/ansible-pune/events/290492160/). If you have an interesting Ansible use case or experience you would like to share, submit your talk proposal [here](https://forms.gle/DjTewB8GsgZdzJkc7).
> 
> 🗓 SAT, FEB 25, 2023, 9:30 AM IST
> 📍 Red Hat India Private Limited, Magarpatta Inner Circle · Pune, Maharashtra

[cybette](https://matrix.to/#/@cybette:ansible.im) shared

> There are several community meetups coming up! 
> * [Ansible NOVA](https://www.meetup.com/ansible-nova/events/291072493/) on Feb 9 @ 6:00 PM EST
> * [Ansible Atlanta](https://www.meetup.com/ansible-atlanta/events/291211206/) on Feb 23 @ 7:00 PM EST
> * [Ansible Zürich](https://www.meetup.com/ansible-zurich/events/290204496/) on Feb 28 @ 5:00 PM CET
> * [Ansible München](https://www.meetup.com/ansible-munchen/events/289768549/) also on Feb 28 @ 6:00PM CET
> 
> Check out the respective event pages for details and RSVP!

## THAT'S ALL FOR NOW!

Have any questions you’d like to ask, or issues you’d like to see covered? Please ask in [#social:ansible.com](https://matrix.to/#/#social:ansible.com)! See you next time!
