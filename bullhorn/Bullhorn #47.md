---
title: "Bullhorn #47"
date: 2022-02-24 23:00 UTC
tags: news
category: bullhorn
type: text
---

![Ansible Bullhorn banner](/images/bullhorn-banner-mango.png)

*A Newsletter for the Ansible Developer Community*
*Issue #47, 2022-02-24 ([Past Issues](https://us19.campaign-archive.com/home/?u=56d874e027110e35dea0e03c1&id=d6635f5420))*

Welcome to [The Bullhorn](https://github.com/ansible/community/wiki/News#the-bullhorn), our newsletter for the Ansible developer community. If you have any questions or content you’d like to share, you're welcome to chat with us in the [Ansible Social room on Matrix](https://matrix.to/#/#social:ansible.com), and mention [`newsbot`](https://matrix.to/#/@newsbot:ansible.im) to have your news item tagged for review for the next weekly issue!

<!-- TEASER_END -->

## KEY DATES

[cybette](https://matrix.to/#/@cybette:ansible.im) shared

> * 2022-02-28: ETA for Ansible-Core 2.12.3 and Ansible-Core 2.11.9 releases
> * 2022-03-01: [DaWGs meeting](https://github.com/ansible/community/issues/643), 16:00 UTC
> * 2022-03-02: [Community WG meeting](https://github.com/ansible/community/issues/645), 18:00 UTC (propose topics [here](https://github.com/ansible-community/community-topics/issues))
> * 2022-03-03: [Bullhorn #48 content deadline](https://github.com/ansible/community/wiki/News#the-bullhorn), 18:00 UTC
> * 2022-03-15: [ETA for Ansible 5.5.0 release](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_5.html)

## GENERAL NEWS UPDATES

[cybette](https://matrix.to/#/@cybette:ansible.im) contributed

> Ansible [turns 10](https://github.com/ansible/ansible/commits/f31421576b00f0b167cdbe61217c31c21a41ac02)! We appreciate all of you, contributors and users in the community, for the amazing growth and adoption of Ansible over the past decade. Happy Birthday to Ansible, and let's continue automating and innovating with Ansible for the next 10 years and beyond!

## MAJOR NEW RELEASES

### Ansible [↗](https://github.com/ansible-collections)

The `Ansible` package includes `ansible-core` and is a batteries-included package that provides a curated set of Ansible collections. See the [Ansible roadmaps](https://docs.ansible.com/ansible/devel/roadmap/ansible_roadmap_index.html) for future release plans.

[dmsimard](https://matrix.to/#/@dmsimard:matrix.org) shared

> ansible 5.4.0 has been released and includes minor updates from 24 Ansible collections! Read more about it in the [announcement](https://groups.google.com/g/ansible-announce/c/razQPdsJXCs), the [changelog](https://github.com/ansible-community/ansible-build-data/blob/main/5/CHANGELOG-v5.rst) or the [porting guide](https://docs.ansible.com/ansible/devel/porting_guides/porting_guide_5.html).

## COLLECTION UPDATES

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) contributed

> community.docker 2.2.0 has been released [with new features and bugfixes](https://github.com/ansible-collections/community.docker/blob/main/CHANGELOG.rst#v2-2-0). Version 1.10.5 has been released [with bugfixes](https://github.com/ansible-collections/community.docker/blob/stable-1/CHANGELOG.rst#v1-10-5).

[rrey](https://matrix.to/#/@rrey:matrix.org) said

> community.grafana 1.3.2 has been released ([changelog](https://github.com/ansible-collections/community.grafana/blob/1.3.2/CHANGELOG.rst#v1-3-2)).

[rainerleber](https://matrix.to/#/@rainerleber:matrix.org) said

> community.sap 1.0.0 has been released ([changelog](https://github.com/ansible-collections/community.sap/blob/main/CHANGELOG.rst)).

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) shared

> community.crypto 2.2.2 has been released [with some bugfixes](https://github.com/ansible-collections/community.crypto/blob/main/CHANGELOG.rst#v2-2-2), and community.crypto 1.9.12 has been released [with backports of these fixes and some known issues, as some of these issues could not be fixed in some cases](https://github.com/ansible-collections/community.crypto/blob/stable-1/CHANGELOG.rst#v1-9-12).

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) contributed

> community.general 4.5.0 ([changelog](https://github.com/ansible-collections/community.general/blob/stable-4/CHANGELOG.rst#v4-5-0)) and 3.8.5 ([changelog](https://github.com/ansible-collections/community.general/blob/stable-3/CHANGELOG.rst#v3-8-5)) have been released with new features (only 4.5.0) and bugfixes.

## HELP WANTED

[Rémi Rey](https://matrix.to/#/@rrey:matrix.org) contributed

> The [community.grafana](https://github.com/ansible-collections/community.grafana) collection is looking for help. There are major changes in Grafana 8 that requires adaptations in the modules. We are also looking for [good souls to join the maintainers](https://github.com/ansible-collections/community.grafana/issues/217) <3

## PROPOSALS - FEEDBACK APPRECIATED!

[Gwmngilfen](https://matrix.to/#/@gwmngilfen:ansible.im) said

> ### Chatrooms Feedback
> 
> It is coming up on 6 months since the vote to adopt Matrix alongside IRC. At that time, I said we should treat this as an ongoing process, and I meant it! I am preparing a blogpost covering the adoption so far, data to show, nice wins, pain points, and so on.
> 
> I would love to hear from the community about how the last few months have felt for you! Are you a long-term community member, or perhaps someone who just joined? Are the rooms discoverable enough? Are some things causing issues? Good, bad, or just interesting, I'd like to hear it. Note that nothing I hear will be made public without consent - but I hope I can publish some comments, and gain an idea of the sentiment.
> 
> If you are comfortable having a direct chat, then message me (`@gwmngilfen:ansible.im` or `gwmngilfen-work` on Libera), otherwise please feel free to leave anonymous comments [on this form](https://www.surveymonkey.co.uk/r/ZDYBFB5). The feedback window will be open for about 2-3 weeks, as I plan to write the blogpost in mid-March. Thanks!

[gundalow](https://matrix.to/#/@gundalow:ansible.im) shared

> ### Improving Ansible documentation by unversioning some guides
> 
> Today, we have multiple files that we only maintain in `/devel/`. Historically, we had problems keeping these files up to date in other branches (`latest` and older). The docs team chose to publish the following pages only to `devel` and put a stub page up in `latest` and earlier releases to point to `devel`:
> 
> * [Porting guides](https://docs.ansible.com/ansible/latest/porting_guides/porting_guides.html)
> * [Release and Maintenance](https://docs.ansible.com/ansible/latest/reference_appendices/release_and_maintenance.html)
> 
> While this has worked well to keep the relevant docs current, it can be a cause of confusion. One recent reader was confused that we were pointing them to a devel page which has the banner that says this is not a guaranteed stable branch.
> 
> We have another set of guides (the community and contributor guides) that are getting a significant overhaul in devel. These guides are not specific to any release (core or Ansible package), but because we publish only to versioned urls, we force these guides to be 'versioned'.
> 
> We'd really welcome feedback from users, contributors and folks that have helped with the documentation via [ansible-community/community-topics#68](https://github.com/ansible-community/community-topics/issues/68).

[gundalow](https://matrix.to/#/@gundalow:ansible.im) contributed

> ### Revamping the community and contributor documentation
> 
> We have docs in three places today for contributors:
> *  ansible/ansible in the [community folder](https://github.com/ansible/ansible/tree/devel/docs/docsite/rst/community)
> *  [ansible/community-docs](https://github.com/ansible/community-docs) - more collection focused
> *  [ansible-collections/overview](https://github.com/ansible-collections/overview) - has deeper collection contribution details
> 
> Since only the first one is published to docs.ansible.com, we need to find a way to publish the details from the other two repositories.
> 
> This is a complex issue, and will shape how we structure the wide range of Ansible Documentation in the future. We'd really like to get your thoughts, and to hear your ideas via [community-topics#60](https://github.com/ansible-community/community-topics/issues/60).

### Ansible-Core [↗](https://github.com/ansible/ansible)

The `ansible-core` package contains the base engine and a small subset of modules and plugins. To see what's planned for the next release, look at the [`ansible-core` roadmaps](https://docs.ansible.com/ansible-core/devel/roadmap/ansible_core_roadmap_index.html).

[gundalow](https://matrix.to/#/@gundalow:ansible.im) contributed

> ### `ansible-core` is proposing adding Type Annotations
> 
> Since the ansible-core controller fully dropped support for older versions of Python, starting in ansible-core 2.12, new Python language features like inline type annotations have become available to us. Before we open the floodgates to type annotations being splattered across the ansible-core codebase, it's necessary to define some policy around how type annotations will be used, and especially how they will be validated.
> 
> If you have experience with Python's type annotations we'd like to hear how you think this could help, let us know your thoughts via [ansible/proposals#202](https://github.com/ansible/proposals/issues/202).

## COMMUNITY EVENTS AND MEETUPS

[cybette](https://matrix.to/#/@cybette:ansible.im) contributed

> Join [Ansible NOVA](https://www.meetup.com/Ansible-NOVA/) group in “Ansible NOVA March Spring Soiree!” on Thursday, March 24 at 16:30 EDT / 20:30 UTC. It'll be a virtual meetup and they are looking for speakers/content. Check the details and RSVP [here](https://www.meetup.com/Ansible-NOVA/events/284181915/).

## THAT'S ALL FOR NOW!

Have any questions you’d like to ask, or issues you’d like to see covered? Please ask in [#social:ansible.com](https://matrix.to/#/#social:ansible.com)! See you next time!
