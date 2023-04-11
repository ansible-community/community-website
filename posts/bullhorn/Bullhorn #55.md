---
title: "Bullhorn #55"
date: 2022-04-22 13:00 UTC
tags: news
category: bullhorn
type: text
---

![Ansible Bullhorn banner](/images/bullhorn-banner-mango.png)

*A Newsletter for the Ansible Developer Community*
*Issue #55, 2022-04-21 ([Past Issues](https://us19.campaign-archive.com/home/?u=56d874e027110e35dea0e03c1&id=d6635f5420))*

Welcome to [The Bullhorn](https://github.com/ansible/community/wiki/News#the-bullhorn), our newsletter for the Ansible developer community. If you have any questions or content you’d like to share, you're welcome to chat with us in the [Ansible Social room on Matrix](https://matrix.to/#/#social:ansible.com), and mention [`newsbot`](https://matrix.to/#/@newsbot:ansible.im) to have your news item tagged for review for the next weekly issue!

<!-- TEASER_END -->

## KEY DATES ⏱️

[cybette](https://matrix.to/#/@cybette:ansible.im) said

> * 2022-04-25: ETA for Ansible-Core 2.12.5 and Ansible-Core 2.11.11 releases
> * 2022-04-26: [ETA for Ansible 5.7.0 release](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_5.html)
> * 2022-04-26: [DaWGs meeting](https://github.com/ansible/community/issues/643), 15:00 UTC
> * 2022-04-27: [Community WG meeting](https://github.com/ansible/community/issues/645) topic: [List any backwards incompatible collection releases that Ansible 6.0.0b1 should try to accommodate](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_6.html), 18:00 UTC
> * 2022-04-28: [Amazon Web Services WG meeting](https://github.com/ansible/community/issues/654), 17:30 UTC
> * 2022-04-28: [Bullhorn #56 content deadline](https://github.com/ansible/community/wiki/News#the-bullhorn), 18:00 UTC
> * 2022-05-23: [ETA for Ansible-Core 2.13 GA](https://docs.ansible.com/ansible-core/devel/roadmap/ROADMAP_2_13.html)
> * 2022-05-23: [End-of-life for upstream Ansible 2.9 and Ansible-base 2.10](https://groups.google.com/g/ansible-announce/c/kegIH5_okmg/)
> * 2022-06-21: [ETA for Ansible 6.0.0 GA](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_6.html)

## GENERAL NEWS UPDATES 🔈️

[abuzachis](https://matrix.to/#/@aevelina:ansible.im) shared

> The Amazon Web Services Working group is holding a monthly community meeting in #ansible-aws IRC channel at 17:30 UTC every fourth Thursday of the month. The next community meeting is scheduled on April 28th at 17:30 UTC. If you have something to discuss (e.g. a PR that needs help), add your request to the [meeting agenda](https://github.com/ansible/community/issues?q=is:open+label:meeting_agenda+label:aws) and join the IRC #ansible-aws channel / [#aws:ansible.com](https://matrix.to/#/#aws:ansible.com) room on Matrix.

[cybette](https://matrix.to/#/@cybette:ansible.im) contributed

> The [live video stream](https://www.youtube.com/watch?v=mili3ax3V4o) from **Ansible Contributor Summit 2022.04** is available for playback! Thanks to [ziegenberg](https://matrix.to/#/@ziegenberg:matrix.org), we now have timestamps for the individual sessions as chapters in the video, so you can go directly to the presentations you're interested in, or might have missed. We will be sharing the rest of the info (talk details, slides, etc.) as well as the Contributor Survey next week. Thanks again to everyone for your participation and making it an amazing experience for all!

## COLLECTION UPDATES 🪄

[markuman](https://matrix.to/#/@markuman:matrix.org) shared

> community.proxysql [1.3.2](https://github.com/ansible-collections/community.proxysql/releases/tag/1.3.2) has been released.

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) shared

> community.hrobot 1.3.0 has been released ([changelog](https://github.com/ansible-collections/community.hrobot/releases/tag/1.3.0)).

[markuman](https://matrix.to/#/@markuman:matrix.org) said

> [community.aws](https://github.com/ansible-collections/community.aws) [3.2.1](https://github.com/ansible-collections/community.aws/releases/tag/3.2.1) has been released.  
> The new parameter `purge_tags` in `ec2_asg` module, that was introduced in [community.aws](https://github.com/ansible-collections/community.aws) [3.2.0](https://github.com/ansible-collections/community.aws/releases/tag/3.2.0) with its default value `true`, possibly breaks existing playbooks for users if they don't update their playbooks and specify purge_tags: false. However, this release restores the previous behaviour.

## HELP WANTED 🙏

[samccann](https://matrix.to/#/@samccann:ansible.im) contributed

> Looking for a way to contribute to Ansible? How about starting with one of these [easyfix issues](https://github.com/ansible/ansible/issues?q=is%3Aopen+is%3Aissue+label%3Aeasyfix)?

## PROPOSALS - DISCUSS AND VOTE! 🗳️

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) contributed

> If you are interested in using community.crypto in an Execution Environment, you might be interested in the discussion which cryptography library (quite old system libraries with FIPS enabled, or latest PyPi versions without FIPS) should the collection depend on: https://github.com/ansible-collections/community.crypto/pull/440#issuecomment-1100605304 If you have opinions on this, please comment!

[cybette](https://matrix.to/#/@cybette:ansible.im) said

> Your votes needed! Proposal: merge and adopt the procedures defined in [Describe how collections can be removed from the Ansible package](https://github.com/ansible-collections/overview/pull/201). Please vote [in this issue](https://github.com/ansible-community/community-topics/issues/90) (and not in the PR). The vote will close on 2022-04-27.

[samccann](https://matrix.to/#/@samccann:ansible.im) said

> [Ansible community documentation priorities](https://github.com/ansible-community/community-topics/issues/81) - this topic lists the priorities that we'll focus on for community Ansible documentation. We welcome your feedback on this to ensure we are focusing efforts where needed.

## COMMUNITY EVENTS AND MEETUPS 📅

[cybette](https://matrix.to/#/@cybette:ansible.im) shared

> Join [Ansible Singapore](https://www.meetup.com/Ansible-Singapore/) group in “Ansible Virtual Meet Up - April 2022” talking about Automation Mesh on Thursday, April 28 at 09:00 SGT / 01:00 UTC. Check the details of this virtual meetup and RSVP [here](https://www.meetup.com/Ansible-Singapore/events/285368952/).
> 
> Join [Ansible New Zealand](https://www.meetup.com/Ansible-New-Zealand/) as they reconnect with fellow Ansibulls with Bank of New Zealand sharing on how they enabled others through the power of Ansible Automation. The online event will be on April 28, at 12:00 NZST. More details and RSVP [here](https://www.meetup.com/Ansible-New-Zealand/events/285222245/).
> 
> [Ansible Minneapolis](https://www.meetup.com/Ansible-Minneapolis/) is having their [April Meetup at Bad Weather Brewing](https://www.meetup.com/Ansible-Minneapolis/events/284338270/). Join them on April 28 at 18:30 CDT and help them define the next steps for the meetup.

## THAT'S ALL FOR NOW!

Have any questions you’d like to ask, or issues you’d like to see covered? Please ask in [#social:ansible.com](https://matrix.to/#/#social:ansible.com)! See you next time!
