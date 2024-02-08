---
title: "Bullhorn #70"
date: 2022-08-19 05:15 UTC
tags: news
category: bullhorn
type: text
---

![Ansible Bullhorn banner](/images/bullhorn-banner-mango.png)

*A Newsletter for the Ansible Developer Community*
*Issue #70, 2022-08-18 ([Past Issues](https://us19.campaign-archive.com/home/?u=56d874e027110e35dea0e03c1&id=d6635f5420))*

Welcome to [The Bullhorn](https://github.com/ansible/community/wiki/News#the-bullhorn), our newsletter for the Ansible developer community. If you have any questions or content you’d like to share, you're welcome to chat with us in the [Ansible Social room on Matrix](https://matrix.to/#/#social:ansible.com), and mention [`newsbot`](https://matrix.to/#/@newsbot:ansible.im) to have your news item tagged for review for the next weekly issue!

<!-- TEASER_END -->

## KEY DATES ⏱️

[cybette](https://matrix.to/#/@cybette:ansible.im) said

> * 2022-08-23: [ETA for Ansible 6.3.0 release](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_6.html)
> * 2022-08-23: [DaWGs meeting](https://github.com/ansible/community/issues/643), 15:00 UTC
> * 2022-08-24: [Community WG meeting](https://github.com/ansible/community/issues/645), 18:00 UTC (propose topics [here](https://github.com/ansible-community/community-topics/issues))
> * 2022-08-25: [Bullhorn #71 content deadline](https://github.com/ansible/community/wiki/News#the-bullhorn), 18:00 UTC
> * 2022-09-12: ETA for Ansible-Core 2.13.4 and Ansible-Core 2.12.9 releases (if those releases have updates)
> * 2022-10-17: [Ansible Contributor Summit 2022.10](https://ansiblecs202210.eventbrite.com/?aff=hackmd)
> * 2022-10-18/19: [AnsibleFest 2022](https://www.ansible.com/ansiblefest?sc_cid=7013a000002i5g3AAA)

## GENERAL NEWS UPDATES 🔈️

[andersson007_](https://matrix.to/#/@andersson007_:matrix.org) contributed

> Hi everyone!
> We are happy to announce the first collection inclusion requests review day!
> 
> **We will be sorting out the requests in the following categories:**
> * [second review needed](https://github.com/ansible-collections/ansible-inclusion/discussions/categories/second-review-needed)
> * [new collection reviews](https://github.com/ansible-collections/ansible-inclusion/discussions/categories/new-collection-reviews)
> 
> **What it'll give you and what you'll give back:**
> * Gain experience in understanding the collection requirements which can be helpful for you as a collection maintainer or future collection author.
> * Help the Community extend the Ansible package. It is necessary for a collection to receive two reviews and approvals, otherwise it can't be included.
> 
> **What will it look like:**
> * See the [inclusion review process description](https://github.com/ansible-collections/ansible-inclusion#review-process).
> * Inclusion reviews will happen in the [inclusion requests](https://github.com/ansible-collections/ansible-inclusion/discussions) themselves.
> * We will be discussing our challenges on Matrix/IRC and in the discussions along the way.
> 
> **When:** Tuesday, 23 August, 06:00 UTC - 14:00 UTC. If the day/time doesn't work for you, feel free to contact `andersson007_` in the channels mentioned below. You can drop by anytime during the session, and complete the review any day later.
> 
> **Where:**  In the [#community:ansible.com](https://matrix.to/#/#community:ansible.com) channel on [Matrix](https://docs.ansible.com/ansible/devel/community/communication.html#ansible-community-on-matrix) or the bridged `#ansible-community` channel on [Libera.Chat](https://docs.ansible.com/ansible/devel/community/communication.html#ansible-community-on-irc) IRC.
> 
> **How to join:** Just ping `andersson007_` on Matrix/IRC.
> 
> We'll be happy to see everyone and help!

## MAJOR NEW RELEASES 🏆️

### Antsibull [↗](https://github.com/ansible-community/antsibull) 🐂

Tooling for building the `Ansible` package and collection documentation.

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) contributed

> antsibull-docs 1.3.0 ([changelog](https://github.com/ansible-community/antsibull-docs/blob/main/CHANGELOG.rst#v1-3-0)) has been released with several new features for the docs build! The most important changes are that now booleans are rendered as `true` and `false` instead of `yes` and `no` (https://github.com/ansible-community/community-topics/issues/116), and that a proper parser is used for Ansible markup, which properly escapes for example backticks instead of simply inserting them into the RST files (https://github.com/ansible-community/antsibull-docs/issues/21).

### Ansible-Core [↗](https://github.com/ansible/ansible) ⚡️

The `ansible-core` package contains the base engine and a small subset of modules and plugins. To see what's planned for the next release, look at the [`ansible-core` roadmaps](https://docs.ansible.com/ansible-core/devel/roadmap/ansible_core_roadmap_index.html).

[cybette](https://matrix.to/#/@cybette:ansible.im) shared

> [ansible-core 2.13.3 and ansible-core 2.12.8](https://groups.google.com/g/ansible-devel/c/px0IRJodpKY) have been released. These are maintenance releases containing numerous bugfixes.

## COLLECTION UPDATES 🪄

[Felix Fontein](https://matrix.to/#/@felixfontein:matrix.org) shared

> We are pleased to announce that community.docker 3.0.0 ([changelog](https://github.com/ansible-collections/community.docker/blob/main/CHANGELOG.rst#v3-0-0)) has finally been released! 🎉 Many of the modules that used to depend on the Docker SDK for Python now directly use requests to talk to the Docker Daemon. Only the Docker Swarm management modules still use the Docker SDK for Python. Also the `community.docker.docker_container` module has been completely rewritten.
> There are also new maintenance releases of the older release branches, 1.10.11 ([changelog](https://github.com/ansible-collections/community.docker/blob/stable-1/CHANGELOG.rst#v1-10-11)) and 2.7.1 ([changelog](https://github.com/ansible-collections/community.docker/blob/stable-2/CHANGELOG.rst#v2-7-1)), which contain bugfixes and documentation improvements.

## HELP WANTED 🙏

[andersson007_](https://matrix.to/#/@andersson007_:matrix.org) shared

> The following collection inclusion requests are waiting for your review:
> * [dellemc.powerflex](https://github.com/ansible-collections/ansible-inclusion/discussions/33)
> * [dellemc.unity](https://github.com/ansible-collections/ansible-inclusion/discussions/32)
> * [inspur.ispim](https://github.com/ansible-collections/ansible-inclusion/discussions/47)
> * [lowlydba.sqlserver](https://github.com/ansible-collections/ansible-inclusion/discussions/51)
> 
> See the [process description](https://github.com/ansible-collections/ansible-inclusion#review-process) to learn how to do it.
> 
> Please help the community extend the Ansible package!

## PROPOSALS - DISCUSS AND VOTE! 🗳️

[mariolenz](https://matrix.to/#/@mariolenz:matrix.org) contributed

> There is a new community / steering committee vote on whether `servicenow.servicenow` should be removed from Ansible 7: https://github.com/ansible-community/community-topics/discussions/127

## COMMUNITY UPDATES 👂️

[cybette](https://matrix.to/#/@cybette:ansible.im) shared

> Here's a convenient and useful [Ansible reference sheet](https://jpmens.net/2022/07/24/an-ansible-reference-sheet/) created by [JP Mens](https://twitter.com/jpmens), a longtime member of the Ansible community and someone who actually has [Ten years of Ansible](https://jpmens.net/2022/06/06/ten-years-of-ansible/) experience. Thanks for sharing your knowledge with the community, JP!

## COMMUNITY EVENTS AND MEETUPS 📅

[cybette](https://matrix.to/#/@cybette:ansible.im) said

> ### Ansible India Meetup
> 
> Ansible India is organizing an online meetup, [NetOps and SecOps with Ansible](https://www.meetup.com/ansible-pune/events/287852503/), on August 25 at 3PM IST. There will be 3 talks: "Develop network modules using Networking Templates, Not Resource Modules", "Detect config drift and fix configuration using Resource Module", and "Getting started with Ansible security automation".
> 
> ### Ansible Singapore Meetup
> 
> Hear about "Ansible Loves VSCode" and "Ansible and Python" in the first in-person meetup in 3 years with [Ansible Singapore](https://www.meetup.com/ansible-singapore/)! Check out the details of this [August 29 meetup @ Red Hat SG Office](https://www.meetup.com/ansible-singapore/events/287781210/) and RSVP.
> 
> ### Ansible Atlanta Meetup
> 
> Join [Ansible Atlanta](https://www.meetup.com/ansible-atlanta/) in their next meetup on September 8 to [Learn about Ansible Navigator](https://www.meetup.com/ansible-atlanta/events/287638006/). Check out the details in the links and RSVP.

## THAT'S ALL FOR NOW!

Have any questions you’d like to ask, or issues you’d like to see covered? Please ask in [#social:ansible.com](https://matrix.to/#/#social:ansible.com)! See you next time!
