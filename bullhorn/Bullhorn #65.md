---
title: "Bullhorn #65"
date: 2022-07-01 19:15 UTC
tags: news
category: bullhorn
type: text
---

![Ansible Bullhorn banner](/images/bullhorn-banner-mango.png)

*A Newsletter for the Ansible Developer Community*
*Issue #65, 2022-07-01 ([Past Issues](https://us19.campaign-archive.com/home/?u=56d874e027110e35dea0e03c1&id=d6635f5420))*

Welcome to [The Bullhorn](https://github.com/ansible/community/wiki/News#the-bullhorn), our newsletter for the Ansible developer community. If you have any questions or content you’d like to share, you're welcome to chat with us in the [Ansible Social room on Matrix](https://matrix.to/#/#social:ansible.com), and mention [`newsbot`](https://matrix.to/#/@newsbot:ansible.im) to have your news item tagged for review for the next weekly issue!

<!-- TEASER_END -->

## KEY DATES ⏱️

[cybette](https://matrix.to/#/@cybette:ansible.im) contributed

> * 2022-07-05: [DaWGs meeting](https://github.com/ansible/community/issues/643), 15:00 UTC
> * 2022-07-06: [Community WG meeting](https://github.com/ansible/community/issues/645), 18:00 UTC (propose topics [here](https://github.com/ansible-community/community-topics/issues))
> * 2022-07-07: [Bullhorn #66 content deadline](https://github.com/ansible/community/wiki/News#the-bullhorn), 18:00 UTC
> * 2022-07-12: [ETA for Ansible 6.1.0 release](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_6.html)
> * 2022-07-15: Deadline for [CFP submission](https://reg.experiences.redhat.com/flow/redhat/rhaf22/cfp/login) for [AnsibleFest 2022](https://www.ansible.com/ansiblefest)
> * 2022-07-18: ETA for Ansible-Core 2.13.2 and Ansible-Core 2.12.8 releases

## GENERAL NEWS UPDATES 🔈️

[Don Naro](https://matrix.to/#/@orandon:ansible.im) shared

> Work continues on improving Ansible documentation for retrievability and general organization.
> In this update we're pleased to announce several changes to the User Guide:
> 
> * [Basic concepts](https://docs.ansible.com/ansible/devel/getting_started/basic_concepts.html) has moved to the _Getting started with Ansible_ section.
> * All the content for Microsoft Windows users has been separated from the _User Guide_ to a dedicated [Using Ansible on Windows](https://docs.ansible.com/ansible/devel/win_guide/index.html) guide.
> * [Ansible tips and tricks](https://docs.ansible.com/ansible/devel/tips_tricks/index.html) is also separated from the _User Guide_.
> 
> We hope these changes help you navigate the Ansible documentation more easily and find the content you're looking for.
> More changes to the _User Guide_ are in plan and next up we're aiming to consolidate some of the Playbook content in the User Guide.
> You can find out more about this effort, and join in the conversation, in [GitHub issue 78082](https://github.com/ansible/ansible/issues/78082).

[gundalow](https://matrix.to/#/@gundalow:ansible.im) said

> The Ansible Core team has recently begun Phase 2 development for ansible-core 2.14 as of June 27, which means that the `milestone` branch has been advanced to the last commit of Jun 24, 2022 corresponding to [ansible/ansible@4594c0c](https://github.com/ansible/ansible/commit/4594c0c6094fcf801caeef27a5170d39d2207b08). 
> 
> See the ansible-core 2.14 [roadmap](https://docs.ansible.com/ansible-core/devel/roadmap/ROADMAP_2_14.html#development-phase) for more information.

## MAJOR NEW RELEASES 🏆️

### Ansible [↗](https://github.com/ansible-collections) 📦️

The `Ansible` package includes `ansible-core` and is a batteries-included package that provides a curated set of Ansible collections. See the [Ansible roadmaps](https://docs.ansible.com/ansible/devel/roadmap/ansible_roadmap_index.html) for future release plans.

[ompragash](https://matrix.to/#/@ompragash:ansible.im) shared

> 📢Ansible 5.10.0 has been released and available in [PyPI](https://pypi.org/project/ansible/5.10.0/)!🎉
> 🔗 https://groups.google.com/g/ansible-announce/c/7rnkSYhdjSY
> 
> 💽 You can install it by running the following command or download the tar.gz directly from [pypi](https://pypi.python.org/packages/source/a/ansible/ansible-5.10.0.tar.gz):
> 
> ```
> pip install ansible==5.10.0 --user
> ```
> 
> 🔆Note:🔆 This is the last release of Ansible 5.x
> 
> Check  [Release Notes📦️🗒️](https://github.com/ansible-community/ansible-build-data/blob/main/5/CHANGELOG-v5.rst) and [Ansible 5 Porting Guide](https://docs.ansible.com/ansible/devel/porting_guides/porting_guide_5.html) for more details!

## HELP WANTED 🙏

[andersson007_](https://matrix.to/#/@andersson007_:matrix.org) said

> The following collection inclusion requests are waiting for your review:
> * [vultr.cloud](https://github.com/ansible-collections/ansible-inclusion/discussions/44)
> * [inspur.ispim](https://github.com/ansible-collections/ansible-inclusion/discussions/47)
> 
> See the [process description](https://github.com/ansible-collections/ansible-inclusion#review-process) to learn how to do it.
> 
> Please help the community extend the Ansible package!

## PROPOSALS - DISCUSS AND VOTE! 🗳️

[Gwmngilfen](https://matrix.to/#/@gwmngilfen:ansible.im) said

> ### Matrix Room Shields for repo READMEs?
> 
> I've opened an [example PR](https://github.com/ansible-community/community-topics/pull/114) for displaying a Shields.io shield for a Matrix room inside the README of a repository. This is the same kind of thing as you often see for test coverage, code coverage, Python versions, etc.
> 
> ![](https://i.imgur.com/vFQ7VB7.png)
> 
> I think this is an useful extra way for maintainers to direct users to the right place to get help, and has the nice side-effect of demonstrating the large vibrant community we have. I'm looking to get feedback on whether this should go in the template repo, so that people know it's an option - what are your thoughts? Please [comment on the PR](https://github.com/ansible-community/community-topics/pull/114)!

[briantist](https://matrix.to/#/@briantist:libera.chat) contributed

> ### Python version support for hvac library
> 
> The `community.hashi_vault` collection is looking for feedback about support for end-of-life Python versions going forward. [Join the discussion](https://github.com/ansible-collections/community.hashi_vault/discussions/277).

## COMMUNITY EVENTS AND MEETUPS 📅

[cybette](https://matrix.to/#/@cybette:ansible.im) shared

> [Ansible Minneapolis](https://www.meetup.com/ansible-minneapolis/) is planning a [social hour on July 21](https://www.meetup.com/ansible-minneapolis/events/286654794/), and if you have a topic you'd like to discuss, join the meetup group and let the organizer know!

[cybette](https://matrix.to/#/@cybette:ansible.im) contributed

> [Ansible Atlanta](https://www.meetup.com/ansible-atlanta/) is restarting their monthly meetups on [August 4](https://www.meetup.com/ansible-atlanta/events/286490353/). Catch up with them to hear updates about what is happening in the Ansble community and how some of the changes are reflected in Red Hat's Ansible Automation Platform.

[cybette](https://matrix.to/#/@cybette:ansible.im) said

> ### AnsibleFest and Ansible Contributor Summit
> 
> [AnsibleFest 2022](https://www.ansible.com/ansiblefest) will be in Chicago, IL (USA) this year, on **October 18 & 19**. [The call for proposals](https://reg.experiences.redhat.com/flow/redhat/rhaf22/cfp/login) is now open until **July 15, 2022**.
> 
> Content topics can include:
> * Getting Started
> * Automating Red Hat products
> * Use Case / Domain-focused (e.g. Network, Security, Cloud)
> * Audience-focused (e.g. Developers, Operations)
> * Thought Leadership
> * Community and Culture
> 
> There will be an **Ansible Contributor Summit** the day before AnsibleFest on **October 17, 2022**, where participants will be able to join both in-person (in Chicago) and online. We have started **pre-registration** for this event. Please check out the details [on Eventbrite](https://ansiblecs202210.eventbrite.com/?aff=hackmd)!

## THE ANSIBLE TEAM IS HIRING 💰️

[gundalow](https://matrix.to/#/@gundalow:ansible.im) shared

> Ansible is looking for an *Agile Practitioner* to support the Red Hat Ansible Platform (Remote USA).
> 
> In this role, you will work closely with creative and experienced engineers to create innovative technology for the next generation of offerings. You will primarily focus on a strategic part of the Ansible organization centered around infrastructure and support for the Ansible development teams. An important part of this role is as coach and champion of agile principles throughout the organization to facilitate the transition to a continuous improvement mindset. You should love helping engineering succeed, and have a passion for concepts surrounding automation, DevOps, site reliability engineering (SRE), and other modern software development techniques.
> 
> To find out more and apply, check out the [job description](https://us-redhat.icims.com/jobs/95776/agile-practitioner---ansible-platform/job?hub=7).

## THAT'S ALL FOR NOW!

Have any questions you’d like to ask, or issues you’d like to see covered? Please ask in [#social:ansible.com](https://matrix.to/#/#social:ansible.com)! See you next time!
