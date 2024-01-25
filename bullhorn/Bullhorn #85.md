---
title: "Bullhorn #85"
date: 2022-12-16 00:35 UTC
tags: news
category: bullhorn
type: text
---

![Ansible Bullhorn banner](/images/bullhorn-banner-mango.png)

*A Newsletter for the Ansible Developer Community*
*Issue #85, 2022-12-15 ([Past Issues](https://us19.campaign-archive.com/home/?u=56d874e027110e35dea0e03c1&id=d6635f5420))*

Welcome to [The Bullhorn](https://github.com/ansible/community/wiki/News#the-bullhorn), our newsletter for the Ansible developer community. If you have any questions or content you’d like to share, you're welcome to chat with us in the [Ansible Social room on Matrix](https://matrix.to/#/#social:ansible.com), and mention [`newsbot`](https://matrix.to/#/@newsbot:ansible.im) to have your news item tagged for review for the next weekly issue!

<!-- TEASER_END -->

## KEY DATES ⏱️

[cybette](https://matrix.to/#/@cybette:ansible.im) said

> * 2022-12-21: [Community WG meeting](https://github.com/ansible/community/issues/645), 19:00 UTC (propose topics [here](https://github.com/ansible-community/community-topics/issues))
> * 2022-12-22: [Bullhorn #86 content deadline](https://github.com/ansible/community/wiki/News#the-bullhorn), 18:00 UTC (last issue for 2022!)
> * 2023-01-03: [DaWGs meeting](https://github.com/ansible/community/issues/643), 16:00 UTC
> * 2023-01-30: [ETA for Ansible-Core 2.14.2 and 2.13.8 releases](https://groups.google.com/g/ansible-devel/c/IQ7VPnw9yS8)
> * 2023-01-31: [ETA for Ansible 7.2.0 release](https://groups.google.com/g/ansible-devel/c/htFjU7jZVYA)

## GENERAL NEWS UPDATES 🔈️

[mariolenz](https://matrix.to/#/@mariolenz:matrix.org) said

> Due to the upcoming holiday season, we [will skip the next Ansible release window](https://groups.google.com/g/ansible-announce/c/r2MvrvOIcpQ). We will wait for the ansible-core 2.14.2 release, which should happen at the end of January 2023, and will release Ansible 7.2.0 one or two days after that.

[cybette](https://matrix.to/#/@cybette:ansible.im) shared

> [ansible-core 2.15.0 Schedule Change](https://groups.google.com/g/ansible-devel/c/KtGFm6fCB7U) - due to a scheduling conflict, ansible-core 2.15.0 will be released 1 week early on 2023-05-15 instead of 2023-05-22. The updated schedule can be found [here](https://github.com/ansible/ansible/blob/devel/docs/docsite/rst/roadmap/ROADMAP_2_15.rst).

[Gwmngilfen](https://matrix.to/#/@gwmngilfen:ansible.im) shared

> ### Contacting the Community Team in chat
> 
> The community has changed a lot in the last year - we've said goodbye to some sorely-missed faces, welcomed new faces, and also done some restructuring as well. However, that's left things unclear as to who to reach out to when we're needed. We've had people DM us individually to help with an issue, which we don't mind (it's our job!) but if that person is away, the wider community is left hanging.
> 
> To help with this, the Community Team has agreed to add **@mods** to our highlighted words in chat. In [any room we're in](https://docs.ansible.com/ansible/devel/community/communication.html#real-time-chat) (which across the team should be all of them, I think), you can use **@mods**  to get the team's attention, and someone should answer!

## MAJOR NEW RELEASES 🏆️

### AWX Project [↗](https://github.com/ansible/awx)

AWX provides a web-based user interface, REST API, and task engine built on top of Ansible.

[Lila Yasin](https://matrix.to/#/@lyasin:matrix.org) contributed

> We're happy to announce that the next release of AWX, version 21.10.1 is now available!
> Some notable features include:
> * Add inventory host list related groups column
> * update task manager docs after refactoring
> 
> In addition, AWX Operator version 1.1.2 has also been released!
> Some notable features include:
> * Bump Ansible Operator SDK version to v1.25.3
> 
> Please see the releases pages for more details: [AWX](https://github.com/ansible/awx/releases/tag/21.10.1), [Operator](https://github.com/ansible/awx-operator/releases/tag/1.1.2).

## COLLECTION UPDATES 🪄

[markuman](https://matrix.to/#/@markuman:matrix.org) shared

> [community.aws](https://galaxy.ansible.com/community/aws) 5.1.0 and 4.4.0 have been released.

[chadmf](https://matrix.to/#/@chadmf:ansible.im) shared

> ### Ansible Edge Collections Update 
> At AnsibleFest we announced the work we have been doing for Edge and we wanted to update everyone in The Bullhorn that version 1.0 of [infra.osbuild](https://github.com/redhat-cop/infra.osbuild), [community.cip](https://github.com/ansible-collections/community.cip) and [community.fdo](https://github.com/ansible-collections/community.fdo) collections are available for everyone to start using.
> 
> The [infra.osbuild](https://github.com/redhat-cop/infra.osbuild) collection is designed to set up a builder server to build and host rpm-ostree images so that you have a central repository of your image and updates. Please put in any issues you run into, any and all feedback is greatly appreciated and everyone that worked on this collection can be reached in [the Ansible Edge matrix room](https://matrix.to/#/#edge:ansible.com).
> 
> The [community.cip](https://github.com/ansible-collections/community.cip) collection was created in collaboration with Rockwell Automation to configure and audit tags (parameters on the controller that represent inputs and outputs to a device) on programmable logic controllers (PLC) for industrial controls. This enables a manufacturing facility to audit and configure tags on multiple PLCs at scale instead of sending a person with a cable around the factory floor to configure them.
> 
> The [community.fdo](https://github.com/ansible-collections/community.fdo) collection was created by our good friends over at XLAB and was pushed into ansible-collections last Friday by [@maxamillion](https://github.com/maxamillion). This hopefully will make our lives easier when setting up FDO servers and should be used in tandem with infra.osbuild. Please reach out in [the Ansible Edge matrix room](https://matrix.to/#/#edge:ansible.com) with any questions.

## PROPOSALS - FEEDBACK WANTED! 🗳️

[elijahd](https://matrix.to/#/@elijahd:ansible.im) shared

> [@kdelee on github](https://github.com/kdelee) is seeking feedback on a proof of concept for a Bulk Job Launch feature that would enable launching batches of jobs via the API with a single request. Checkout [the PR](https://github.com/ansible/awx/pull/13331) to try the feature and/or leave comments about if this feature would be useful to you or to provide any technical review.

## COMMUNITY EVENTS AND MEETUPS 📅

[anwesha](https://matrix.to/#/@anwesha:ansible.im) shared

> We are reviving the Stockholm Ansible Meetup group from the new year, 2023 💖 We are having our in-person meetup on 12th January 2023.
> 
> The plan is to know and talk about the state and the working of the Ansible community. We are also holding a lightning talks session where you can share your Ansible story and your overall automation journey.
> 
> Register your talk for the lightning talks session, check out the detailed plan and RSVP at our [event page](https://www.meetup.com/ansible-stockholm/events/290310440/). 
> 
> See you all folks there.🙂

[cybette](https://matrix.to/#/@cybette:ansible.im) contributed

> Our request for a stand at [FOSDEM 2023](https://fosdem.org/2023/) has been [accepted](https://fosdem.org/2023/news/2022-12-08-accepted-stands-fosdem-2023/), so there'll be an Ansible Community stand at FOSDEM, Feb 4-5. See you in Brussels! 

## DOCUMENTATION UPDATES 📑

[Don Naro](https://matrix.to/#/@orandon:ansible.im) contributed

> The `ansible/docsite` repo is now public, giving the Ansible community full access to all the html and navigation assets that go into `docs.ansible.com`. Fork [the repo](https://github.com/ansible/docsite) and start hacking.

[Don Naro](https://matrix.to/#/@orandon:ansible.im) said

> We've updated the landing pages for `docs.ansible.com` to include an Ansible ecosystem page that organizes links to different projects. We've also refreshed some of the navigation and other pages to improve findability. Go visit https://docs.ansible.com/ and have a look. And remember the `ansible/docsite` repo is now public so you can send a PR with any improvements.

## THAT'S ALL FOR NOW!

Have any questions you’d like to ask, or issues you’d like to see covered? Please ask in [#social:ansible.com](https://matrix.to/#/#social:ansible.com)! See you next time!
