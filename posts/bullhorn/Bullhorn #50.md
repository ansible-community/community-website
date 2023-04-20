---
title: "Bullhorn #50"
date: 2022-03-18 04:30 UTC
tags: news
category: bullhorn
type: text
---

![Ansible Bullhorn banner](/images/bullhorn-banner-mango.png)

*A Newsletter for the Ansible Developer Community*
*Issue #50, 2022-03-17 ([Past Issues](https://us19.campaign-archive.com/home/?u=56d874e027110e35dea0e03c1&id=d6635f5420))*

Welcome to [The Bullhorn](https://github.com/ansible/community/wiki/News#the-bullhorn), our newsletter for the Ansible developer community. If you have any questions or content you’d like to share, you're welcome to chat with us in the [Ansible Social room on Matrix](https://matrix.to/#/#social:ansible.com), and mention [`newsbot`](https://matrix.to/#/@newsbot:ansible.im) to have your news item tagged for review for the next weekly issue!

<!-- TEASER_END -->

## KEY DATES

[cybette](https://matrix.to/#/@cybette:ansible.im) contributed

> * 2022-03-22: [DaWGs meeting](https://github.com/ansible/community/issues/643), 16:00 UTC
> * 2022-03-23: [Community WG meeting](https://github.com/ansible/community/issues/645), 18:00 UTC (propose topics [here](https://github.com/ansible-community/community-topics/issues))
> * 2022-03-24: [Bullhorn #51 content deadline](https://github.com/ansible/community/wiki/News#the-bullhorn), 18:00 UTC
> * 2022-03-28: ETA for Ansible-Core 2.12.4 and Ansible-Core 2.11.10 releases (if those releases have updates)
> * 2022-04-05: [ETA for Ansible 5.6.0 release](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_5.html)
> * 2022-04-12: [Contributor Summit 2022.04](https://hackmd.io/@ansible-community/contrib-summit-202204) 💾📅
> * 2022-05-23: [ETA for Ansible-core 2.13 GA](https://docs.ansible.com/ansible-core/devel/roadmap/ROADMAP_2_13.html)
> * 2022-05-23: [End-of-life for upstream Ansible 2.9 and Ansible-base 2.10](https://groups.google.com/g/ansible-announce/c/kegIH5_okmg/)

## GENERAL NEWS UPDATES

[cybette](https://matrix.to/#/@cybette:ansible.im) shared

> Planning to attend the next **Ansible Contributor Summit**? Mark your calendars for **[April 12, 2022 (Tuesday)](https://raw.githubusercontent.com/ansible/community/main/meetings/ical/contribsummit202204.ics)** and check out the [HackMD note](https://hackmd.io/@ansible-community/contrib-summit-202204) - [add your names](https://hackmd.io/@ansible-community/contrib-summit-202204/%2F-JfWR98UTgOEKL7IDIXbKQ) & [propose/vote on topics](https://hackmd.io/@ansible-community/contrib-summit-202204/%2FzxOZe_FzR7a9-pw6r6_Ypg).

## MAJOR NEW RELEASES

### Ansible [↗](https://github.com/ansible-collections)

The `Ansible` package includes `ansible-core` and is a batteries-included package that provides a curated set of Ansible collections. See the [Ansible roadmaps](https://docs.ansible.com/ansible/devel/roadmap/ansible_roadmap_index.html) for future release plans.

[dmsimard](https://matrix.to/#/@dmsimard:matrix.org) shared

> Ansible 5.5.0 has been released with updates to 19 collections! You can find more information about this new release in the [announcement](https://groups.google.com/g/ansible-announce/c/4sbFT7aVklY) and the [changelog](https://github.com/ansible-community/ansible-build-data/blob/main/5/CHANGELOG-v5.rst).

## COLLECTION UPDATES

[andersson007_](https://matrix.to/#/@andersson007_:matrix.org) shared

> [community.mysql](https://github.com/ansible-collections/community.mysql) versions [2.3.5](https://github.com/ansible-collections/community.mysql/blob/stable-2/changelogs/CHANGELOG.rst) and [3.1.2](https://github.com/ansible-collections/community.mysql/blob/main/changelogs/CHANGELOG.rst) have been released.

[ashwini](https://matrix.to/#/@ashwini:libera.chat) shared

> The `ipaddr` filters are broken in `ansible.netcommon` 2.6.0 release as we have recently migrated `ipaddr` filters from `ansible.netcommon` to `ansible.utils`. We have released utils 2.5.2 and netcommon 2.6.1 which fixed these two issues ([ansible.netcommon#375](https://github.com/ansible-collections/ansible.netcommon/issues/375), [ansible.utils#148](https://github.com/ansible-collections/ansible.utils/issues/148)). For the [FQDN issue](https://github.com/ansible/ansible/issues/77192), the ansible-core team has already merged [the fix](https://github.com/ansible/ansible/pull/77210). This fix will be available in the March 28th release, which means that users of non fqdn ipaddr filters can use the old netcommon collection version 2.5.1 as a workaround until the next ansible-core release (March 28th) by the core-team. For fqdn ipaddr filters, users can use the latest versions of any of ansible.netcommon (2.6.1) or ansible.utils (2.5.2).

[Sean Sullivan](https://matrix.to/#/@seansulliv:matrix.org) contributed

> Controller Configuration collection just released a new update 2.1.2 including a way to do object differentials to clean up Tower and Controller Instances https://galaxy.ansible.com/redhat_cop/controller_configuration

[hunleyd](https://matrix.to/#/@hunleyd:matrix.org) said

> `community.postgresql` 2.1.2 has been released with a new deprecation. ([changelog](https://github.com/ansible-collections/community.postgresql/blob/2.1.2/CHANGELOG.rst#v2-1-2))

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) shared

> community.general 4.6.0 has been released with new features and bugfixes ([changelog](https://github.com/ansible-collections/community.general/blob/stable-4/CHANGELOG.rst#v4-6-0)).

## PROPOSALS - DISCUSS AND VOTE!

[samccann](https://matrix.to/#/@samccann:ansible.im) contributed

> Ansible docs is proposing to archive older (EOL) releases (aka move them to a new archive site) - If you use an ansible release < 2.8, consider adding comments and voting on this topic at https://github.com/ansible-community/community-topics/issues/78

[samccann](https://matrix.to/#/@samccann:ansible.im) shared

> Ansible community is adding a formatted yaml file to the collection structure to facilitate adding more links to each collection docs page on docs.ansible.com (including Edit on GitHub), see https://github.com/ansible-community/community-topics/issues/80 to comment and vote on  this yaml file format.

[hunleyd](https://matrix.to/#/@hunleyd:matrix.org) contributed

> If you use the `community.postgresql` collection, we'd love to hear your thoughts on this proposed change: https://github.com/ansible-collections/community.postgresql/issues/212

[briantist](https://matrix.to/#/@briantist:libera.chat) said

> The `community.hashi_vault` collection is looking for feedback about some upcoming content. This is dedicated content for reading from the KV secret backend (the most commonly used one). If you use HashiCorp Vault with Ansible your input is appreciated! https://github.com/ansible-collections/community.hashi_vault/discussions/229

## COMMUNITY EVENTS AND MEETUPS

[cybette](https://matrix.to/#/@cybette:ansible.im) said

> Join [Ansible NOVA](https://www.meetup.com/Ansible-NOVA/) group in “Ansible NOVA March Spring Soiree!” on Thursday, March 24 at 16:30 EDT / 20:30 UTC. Check the details of this virtual meetup and RSVP [here](https://www.meetup.com/Ansible-NOVA/events/284181915/).

## THAT'S ALL FOR NOW!

Have any questions you’d like to ask, or issues you’d like to see covered? Please ask in [#social:ansible.com](https://matrix.to/#/#social:ansible.com)! See you next time!
