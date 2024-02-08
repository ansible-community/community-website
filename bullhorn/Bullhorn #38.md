---
title: "Bullhorn #38"
date: 2021-11-18 22:30 UTC
tags: news
category: bullhorn
type: text
---

![Ansible Bullhorn banner](/images/bullhorn-banner-mango.png)

*A Newsletter for the Ansible Developer Community*
*Issue #38, 2021-11-18 ([Past Issues](https://us19.campaign-archive.com/home/?u=56d874e027110e35dea0e03c1&id=d6635f5420))*

Welcome to the Bullhorn, our newsletter for the Ansible developer community. If you have any questions or content you’d like to share, please reach out to us at the-bullhorn@redhat.com, or chat with us in the [Ansible Social room on Matrix](https://matrix.to/#/#social:ansible.com).

<!-- TEASER_END -->

## KEY DATES

[cybette](https://matrix.to/#/@cybette:ansible.im) said

> * 2021-11-23: [ETA for Ansible 4.9.0 release](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_4.html)
> * 2021-11-24: [community IRC meeting](https://github.com/ansible/community/issues/539), 18:00 UTC (propose topics [here](https://github.com/ansible-community/community-topics/issues))
> * 2021-11-30: [ETA for Ansible 5.0.0 GA release](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_5.html)
> * 2021-12-01: [community IRC meeting](https://github.com/ansible/community/issues/539), 18:00 UTC (propose topics [here](https://github.com/ansible-community/community-topics/issues))
> * 2021-12-01: [Bullhorn #39 content deadline](https://github.com/ansible/community/issues/546)
> * 2021-12-06: ETA for Ansible-Core 2.12.1 release

## GENERAL NEWS UPDATES

[samccann](https://matrix.to/#/@smccann:matrix.org) contributed

> We are proposing the addition of semantic markup for module documentation to separate what the module has (options, values, etc.) from how we display it (bold, italic, monospace, etc.). See https://github.com/ansible-community/community-topics/issues/53 for details and to add your thoughts.

[samccann](https://matrix.to/#/@smccann:matrix.org) said

> We are experimenting with changing the module documentation tables that appear on docs.ansible.com to make them more compatible with smaller screen sizes. This also impacts how it appears on wider screens so please take a look at https://github.com/ansible-community/antsibull/pull/335 and post your comments!
> 
> Before example:
> 
> https://docs.ansible.com/ansible/devel/collections/community/crypto/acme_account_module.html#parameters
> 
> ![](https://i.imgur.com/ZJDVDko.png)
> 
> After example:
> 
> https://ansible.fontein.de/collections/community/crypto/acme_account_module.html#parameters
> 
> ![](https://i.imgur.com/NjHVJF4.png)
> 
> (More examples in the [pull request](https://github.com/ansible-community/antsibull/pull/335).)

### Ansible-Core [↗](https://github.com/ansible/ansible)

**Ansible Core** is minimal package containing the base engine, modules, and plugins

[gundalow](https://matrix.to/#/@gundalow:ansible.im) said

> We are happy to announce that `ansible-core-2.12` is available on CentOS Stream - [Ansible on Koji Hub](https://kojihub.stream.centos.org/koji/buildinfo?buildID=15195)

## MAJOR NEW RELEASES

### Ansible [↗](https://github.com/ansible-collections)

**Ansible** is the full-fat package containing Ansible Core & the Community Collections

[dmsimard](https://matrix.to/#/@dmsimard:libera.chat) contributed

> Ansible 5.0.0b2 (including ansible-core 2.12.0) is now available for testing: https://groups.google.com/g/ansible-announce/c/_Z4JE5X-gZg

### Ansible-Core [↗](https://github.com/ansible/ansible)

**Ansible Core** is minimal package containing the base engine, modules, and plugins

[Gwmngilfen (work)](https://matrix.to/#/@gwmngilfen:ansible.im) said

> Update from @sivel: New major release: ansible-core 2.12.0 https://groups.google.com/g/ansible-announce/c/Q3Gp8O8sJak

### Antsibull [↗](https://github.com/ansible-community/antsibull)

Tooling for building various things related to ansible

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) contributed

> antsibull 0.39.2 has been released

## COLLECTION UPDATES

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) said

> community.docker 1.10.1 and 2.0.1 have been released with docs fixes

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) said

> community.hrobot 1.2.1 has been released

[briantist](https://github.com/briantist) contributed

> [`community.hashi_vault` version `1.5.0` has been released with a new action group and `mount_point` vars for plugins](https://github.com/ansible-collections/community.hashi_vault/releases/tag/1.5.0). This is expected to be the final `1.x` release of the collection.

[briantist](https://github.com/briantist) shared

> [`community.hashi_vault` version `2.0.0` has been released](https://github.com/ansible-collections/community.hashi_vault/releases/tag/2.0.0). Some deprecated features have been removed and support for Python 2 and Python 3.5 has been dropped.

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) shared

> community.dns 2.0.2 has been released with updates to the Public Suffix List

[resmo](https://github.com/resmo) contributed

> `ngine_io.vultr` has started the conversion to the Vultr API v2, which will be completed with the collection release of 2.0.0. Progress can be followed at https://github.com/ngine-io/ansible-collection-vultr/pull/22.

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) said

> community.general 2.5.7 has been released. This is the last regular 2.5.x release, from now on there will only be releases for major bugfixes or security fixes.

[andersson007_](https://matrix.to/#/@andersson007_:matrix.org) said

> community.cockroachdb 0.2.0 has been released

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) contributed

> community.general 4.0.2 has been released

[evgeni](https://github.com/evgeni) shared

> The [Foreman Ansible Collection](https://galaxy.ansible.com/theforeman/foreman) v3.0.0 was released.
> Most notable changes include:
> - drop of Ansible 2.8 support (breaking change)
> - switch inventory plugin to the new Reports API (breaking change as this might change returned results)
> - convert2rhel role to ease setup of environments to convert CentOS and Oracle Linux installations to RHEL
> 
> [full changelog](https://theforeman.github.io/foreman-ansible-modules/v3.0.0/CHANGELOG.html#v3-0-0)

[tremble](https://github.com/tremble) contributed

> amazon.aws 2.1.0 has been released
> community.aws 2.1.0 has been released

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) said

> community.internal_test_tools 0.5.0 has been released with some tool improvements

[endorama](https://github.com/endorama) shared

> community.sops 1.2.0 has been released

## COMMUNITY UPDATES

[Gwmngilfen (work)](https://matrix.to/#/@gwmngilfen:ansible.im) contributed

> ### Contributor Summit on Matrix Live
> 
> I got the chance to join [Thib](https://matrix.to/#/@thib:ergaster.org) from Element on the latest episode of Matrix Live! We spent a very pleasant time discussing how running events on Matrix felt, what the architecture was, where we think it did well, and how to improve it in the future. You can watch it [on YouTube](https://www.youtube.com/watch?v=3dqrqMglXNY) or on the [This Week in Matrix blog](https://matrix.org/blog/2021/11/12/this-week-in-matrix-2021-11-12/).
> 
> ![](https://i.imgur.com/m3dokr3.png)

[cybette](https://matrix.to/#/@cybette:ansible.im) said

> Thanks to those who have already filled in the [Contributor Survey](https://www.surveymonkey.co.uk/r/GSMSG7K)! If you haven't had the chance to do so, please spare a few minutes to take [the survey](https://www.surveymonkey.co.uk/r/GSMSG7K). We truly appreciate your feedback!

### Maintainers [↗](https://github.com/ansible-community)

Maintainers help to run the community!

[andersson007_](https://matrix.to/#/@andersson007_:matrix.org) said

> The [community.libvirt](https://github.com/ansible-collections/community.libvirt) collection is looking for new maintainers. If you're interested, please let us know in [this](https://github.com/ansible-collections/community.libvirt/issues/78) issue. Thank you!

## COMMUNITY EVENTS/MEETUPS

[cybette](https://matrix.to/#/@cybette:ansible.im) contributed

> * Thu, Nov 18 @ 6:30PM CST - [Ansible Minneapolis](https://www.meetup.com/Ansible-Minneapolis/events/lndxqsyccpbxb/) - Ansible Meetup at Indeed Brewing
> * Thu, Nov 25 @ 11:00AM SGT - [Ansible Singapore](https://www.meetup.com/Ansible-Singapore/events/281992436/) - Ansible Virtual Meet Up - November 2021

[tima](https://github.com/tima) shared

> An Ansible Working Group meeting has been started under the [Operator Framework](https://github.com/operator-framework/operator-sdk) project community. Meetings will be held monthly, ever third Monday at 5PM UTC. Topics will include not only the Ansible Operator SDK, but also the [kubernetes.core](https://github.com/ansible-collections/kubernetes.core) collection and other Ansible + cloud native discussion. For more information [see the Operator Framework community repo](https://github.com/operator-framework/community#ansible-working-group). The first meeting was held November 15. [A recording of the call is available here](https://youtu.be/bxkpITK5qfc). The WG has also setup [a new mailing list](https://groups.google.com/g/ansible-k8s-operator/about) for discussion between the meetings. Please subscribe and join in the conversation.

## THAT'S ALL FOR NOW!

Have any questions you’d like to ask, or issues you’d like to see covered? Please ask in [#social:ansible.com](https://matrix.to/#/#social:ansible.com)! See you next time!
