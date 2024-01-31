---
title: "Bullhorn #67"
date: 2022-07-15 16:30 UTC
tags: news
category: bullhorn
type: text
---

![Ansible Bullhorn banner](/images/bullhorn-banner-mango.png)

*A Newsletter for the Ansible Developer Community*
*Issue #67, 2022-07-15 ([Past Issues](https://us19.campaign-archive.com/home/?u=56d874e027110e35dea0e03c1&id=d6635f5420))*

Welcome to [The Bullhorn](https://github.com/ansible/community/wiki/News#the-bullhorn), our newsletter for the Ansible developer community. If you have any questions or content you’d like to share, you're welcome to chat with us in the [Ansible Social room on Matrix](https://matrix.to/#/#social:ansible.com), and mention [`newsbot`](https://matrix.to/#/@newsbot:ansible.im) to have your news item tagged for review for the next weekly issue!

<!-- TEASER_END -->

## KEY DATES ⏱️

[cybette](https://matrix.to/#/@cybette:ansible.im) contributed

> * 2022-07-18: ETA for Ansible-Core 2.13.2 release
> * 2022-07-19: [DaWGs meeting](https://github.com/ansible/community/issues/643), 15:00 UTC
> * 2022-07-20: [Community WG meeting](https://github.com/ansible/community/issues/645), 18:00 UTC (propose topics [here](https://github.com/ansible-community/community-topics/issues))
> * 2022-07-21: [Bullhorn #68 content deadline](https://github.com/ansible/community/wiki/News#the-bullhorn), 18:00 UTC
> * 2022-08-02: [ETA for Ansible 6.2.0 release](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_6.html)

## MAJOR NEW RELEASES 🏆️

[john-westcott-iv](https://matrix.to/#/@john-westcott-iv:ansible.im) said

> We're happy to announce that [AWX version 21.3.0](https://github.com/ansible/awx/releases/tag/21.3.0) is now available along with [AWX Operator version 0.24.0](https://github.com/ansible/awx-operator/releases/tag/0.24.0)!
> * Adds import export to awx cli for schedules as a top level object
> * Add state to awx license module
> * Import/export error codes when something bad happens
> * [New] Bubble up an error code when something goes wrong with import/export
> * Pass combined artifacts from nested workflows into downstream nodes
> * Remove deprecated field update_on_project_update
> * Add database connection to the metrics endpoint
> * Add Help Text with documentation link to Schedules page

### Ansible [↗](https://github.com/ansible-collections) 📦️

The `Ansible` package includes `ansible-core` and is a batteries-included package that provides a curated set of Ansible collections. See the [Ansible roadmaps](https://docs.ansible.com/ansible/devel/roadmap/ansible_roadmap_index.html) for future release plans.

[ompragash](https://matrix.to/#/@ompragash:ansible.im) shared

> Ansible 6.1.0 is out!❤️
> 🔗https://groups.google.com/g/ansible-devel/c/KxogBHF70Fo
> 
> 💽You can install it by running the following command or download the release tarball directly from [pypi](https://pypi.python.org/packages/source/a/ansible/ansible-6.1.0.tar.gz):
> ```
> pip install ansible==6.1.0 --user
> ```
> 
> 🔆Oh and don't miss out on the all new `ansible-community` command-line utility added in Ansible 6 that prints the version of the Ansible Community package:
> ```
> $ ansible-community --version
> Ansible community version 6.1.0
> ```
> 
> ➡️Check [Release Notes📦️🗒️](https://github.com/ansible-community/ansible-build-data/blob/main/6/CHANGELOG-v6.rst) and [Ansible 6 Porting Guide](https://docs.ansible.com/ansible/devel/porting_guides/porting_guide_6.html) for more details!

## COLLECTION UPDATES 🪄

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) said

> community.crypto 1.9.18 ([changelog](https://github.com/ansible-collections/community.crypto/blob/stable-1/CHANGELOG.rst#v1-9-18)) and 2.4.0 ([changelog](https://github.com/ansible-collections/community.crypto/blob/main/CHANGELOG.rst#v2-4-0)) have been released with a bugfix. The 2.4.0 release also deprecates Ansible 2.9 and ansible-base 2.10 support that will be removed in the next major release.

[csmart](https://matrix.to/#/@csmart:matrix.org) said

> community.rabbitmq 1.2.2 ([changelog](https://github.com/ansible-collections/community.rabbitmq/blob/main/CHANGELOG.rst#v1-2-2)) has been released with a small bug fix to disable check mode for the user module.

## COMMUNITY EVENTS AND MEETUPS 📅

[cybette](https://matrix.to/#/@cybette:ansible.im) contributed

> ### Ansible India Meetup
> 
> Join Ansible India in their [July 2022 online meetup](https://www.meetup.com/ansible-pune/events/287002963/) on July 21 with 2 talks: "Ansible Navigator - A text-based user interface (TUI) Tool Deep Dive", and "AWX Backup and Restore on Kubernetes".
> 
> ### Ansible Minneapolis Meetup
> 
> [Ansible Minneapolis](https://www.meetup.com/ansible-minneapolis/) is planning a [social hour on July 21](https://www.meetup.com/ansible-minneapolis/events/286654794/), and if you have a topic you'd like to discuss, join the meetup group and let the organizer know!
> 
> ### Ansible Atlanta Meetup
> 
> [Ansible Atlanta](https://www.meetup.com/ansible-atlanta/) is restarting their monthly meetups on [August 4](https://www.meetup.com/ansible-atlanta/events/286490353/). Catch up with them to hear updates about what is happening in the Ansble community and how some of the changes are reflected in Red Hat's Ansible Automation Platform.

[cybette](https://matrix.to/#/@cybette:ansible.im) said

> ### Ansible Contributor Summit
> 
> The **Ansible Contributor Summit** will be held the day before [AnsibleFest 2022](https://www.ansible.com/ansiblefest) on **October 17, 2022**, where participants will be able to join both in-person (in Chicago, IL, USA) and online. Please check out the details [on Eventbrite](https://ansiblecs202210.eventbrite.com/?aff=hackmd) and **pre-register for the event as early as possible**!

## THE ANSIBLE TEAM IS HIRING 💰️

[gundalow](https://matrix.to/#/@gundalow:ansible.im) shared

> Ansible is looking for an *Agile Practitioner* to support the Red Hat Ansible Platform (Remote USA).
> 
> In this role, you will work closely with creative and experienced engineers to create innovative technology for the next generation of offerings. You will primarily focus on a strategic part of the Ansible organization centered around infrastructure and support for the Ansible development teams. An important part of this role is as coach and champion of agile principles throughout the organization to facilitate the transition to a continuous improvement mindset. You should love helping engineering succeed, and have a passion for concepts surrounding automation, DevOps, site reliability engineering (SRE), and other modern software development techniques.
> 
> To find out more and apply, check out the [job description](https://us-redhat.icims.com/jobs/95776/agile-practitioner---ansible-platform/job?hub=7).

## THAT'S ALL FOR NOW!

Have any questions you’d like to ask, or issues you’d like to see covered? Please ask in [#social:ansible.com](https://matrix.to/#/#social:ansible.com)! See you next time!
