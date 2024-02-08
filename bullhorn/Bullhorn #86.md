---
title: "Bullhorn #86"
date: 2022-12-24 00:45 UTC
tags: news
category: bullhorn
type: text
---

![Ansible Bullhorn banner](/images/bullhorn-banner-mango.png)

*A Newsletter for the Ansible Developer Community*
*Issue #86, 2022-12-23 ([Past Issues](https://us19.campaign-archive.com/home/?u=56d874e027110e35dea0e03c1&id=d6635f5420))*

Welcome to [The Bullhorn](https://github.com/ansible/community/wiki/News#the-bullhorn), our newsletter for the Ansible developer community. If you have any questions or content you’d like to share, you're welcome to chat with us in the [Ansible Social room on Matrix](https://matrix.to/#/#social:ansible.com), and mention [`newsbot`](https://matrix.to/#/@newsbot:ansible.im) to have your news item tagged for review for the next issue!

<!-- TEASER_END -->

## KEY DATES ⏱️

[cybette](https://matrix.to/#/@cybette:ansible.im) contributed

> * 2023-01-03: [DaWGs meeting](https://github.com/ansible/community/issues/643#issuecomment-1349579652), 16:00 UTC
> * 2023-01-04: [Community WG meeting](https://github.com/ansible/community/issues/645), 19:00 UTC (propose topics [here](https://github.com/ansible-community/community-topics/issues))
> * 2023-01-05: [Bullhorn #87 content deadline](https://github.com/ansible/community/wiki/News#the-bullhorn), 18:00 UTC
> * 2023-01-30: [ETA for Ansible-Core 2.14.2 and 2.13.8 releases](https://groups.google.com/g/ansible-devel/c/IQ7VPnw9yS8)
> * 2023-01-31: [ETA for Ansible 7.2.0 release](https://groups.google.com/g/ansible-devel/c/htFjU7jZVYA)
> * 2023-02-08: [Ansible Contributor Summit 2023.02](https://hackmd.io/@ansible-community/cs202302-planning)

## GENERAL NEWS UPDATES 🔈️

This will be the last issue for 2022. A big THANKS to every one of you for all of your contributions and readership! Happy holidays and see you in 2023 🎉

[cybette](https://matrix.to/#/@cybette:ansible.im) said

> ### Ansible Contributor Summit
> 
> Ansible Contributor Summit 2023.02 will be held on the third day of [CfgMgmtCamp 2023](https://cfgmgmtcamp.eu/ghent2023/) on **February 8, 2023**, where participants will be able to join both in-person (in Ghent, Belgium) and online. Please take a look at the initial details [here](https://hackmd.io/@ansible-community/cs202302-planning) and propose your topics!

## MAJOR NEW RELEASES 🏆️

### Antsibull [↗](https://github.com/ansible-community/antsibull) 🐂

Tooling for building the `Ansible` package and collection documentation.

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) contributed

> antsibull-changelog 0.18.0 ([changelog](https://github.com/ansible-community/antsibull-changelog/blob/main/CHANGELOG.rst#v0-18-0)) has been released. This is a maintainence release that drops support for Python versions 3.6, 3.7, and 3.8. There are no functional changes; if this is causing problems in CI, please either make sure a newer Python version is used, or restrict the antsibull-changelog version to < 0.18.0.

### AWX Project [↗](https://github.com/ansible/awx) 

AWX provides a web-based user interface, REST API, and task engine built on top of Ansible.

[relrod](https://matrix.to/#/@relrod:matrix.org) said

> We're happy to announce that [AWX version 21.10.2](https://github.com/ansible/awx/releases/tag/21.10.2) is now available! We're happy to announce that [AWX Operator version 1.1.3](https://github.com/ansible/awx-operator/releases/tag/1.1.3) is now available! This AWX version downgrades a dependency which was causing tracebacks to appear often in the logs of some deployments.

## COLLECTION UPDATES 🪄

[Simon Dodsley](https://matrix.to/#/@sdodsley:matrix.org) said

> purestorage-fusion 1.3.0 ([changelog](https://github.com/Pure-Storage-Ansible/Fusion-Collection/blob/master/CHANGELOG.rst#v1-3-0)) has been released.

[Yusuke Tsutsumi](https://matrix.to/#/@tsutsumiyusuke:matrix.org) shared

> The google.cloud 1.1.0 collection is now available! [This version](https://galaxy.ansible.com/google/cloud) includes multiple bugfixes and has been tested with ansible-core up to 2.13. Please give it a shot, and file any bugs or PRs [on GitHub](https://github.com/ansible-collections/google.cloud).

[resmo](https://matrix.to/#/@resmo:libera.chat) shared

> The [vultr.cloud collection](https://galaxy.ansible.com/vultr/cloud) team is pleased to announce version 1.5.0. In this version, VPC support for the instance module has been added as well as a new module instance_info.

## PROJECT UPDATES 🛠️

### AWX Project [↗](https://github.com/ansible/awx) 

AWX provides a web-based user interface, REST API, and task engine built on top of Ansible.

[relrod](https://matrix.to/#/@relrod:matrix.org) contributed

> Our AWX Community Office Hours for December was a huge success! Thank you to all who attended! Missed it? Catch it [on YouTube](https://www.youtube.com/watch?v=xG58czmXPxY&list=PLp4Ci0fwnVC2XIA0xstmjQKvAan-oQqhl&index=2). We have an agenda started for January! Have something you want to bring up? Throw it on the agenda [here](https://github.com/ansible/awx/issues/13325) and we'll see you there!

[relrod](https://matrix.to/#/@relrod:matrix.org) shared

> There's a super cool [AWX community YouTube channel](https://www.youtube.com/@ansible-awx) now. This is a place where we -- the AWX community -- can show off some cool ways to use AWX or share information that the rest of the community might find useful. If you're of the creative type and wish to volunteer to make a video, let's work together and make something cool! Check out [this GitHub issue](https://github.com/ansible/awx/issues/13242) for information. Make a cool video and get a limited-time angry potato plush!

[relrod](https://matrix.to/#/@relrod:matrix.org) contributed

> By popular demand, awx-ee images will soon start having version tags, created when an AWX release happens as a snapshot of the current `awx-ee:latest` at that point. No more relying on daily builds and a single `latest` tag! It will be possible to specify a specific, stable image and update to a newer one on your own time! Coming soon!

[relrod](https://matrix.to/#/@relrod:matrix.org) said

> AWX is working towards moving its Kubernetes deployment from a single deployment to two deployments: one for Task pods and one for Web/API pods. The goal here is to be able to scale these pods independently of each other, which means we need to decouple some service dependencies that we've accumulated over time in the single deployment world. The work here is making steady progress. If anyone is interested in helping out with this or if this will be useful for you, let's chat in the [AWX Matrix channel](https://matrix.to/#/#awx:ansible.com)!

## COMMUNITY UPDATES 👂️

[lucab_it](https://matrix.to/#/@lucab_it:matrix.org) shared

> **"Ansible For VMware By Examples"** by [Luca Berton, aka "Ansible Pilot"](https://www.ansiblepilot.com/) has been released! Exclusive 20% off for the Ansible community using the `ANSIBLEPILOT` discount code during the first month via [Apress](https://link.springer.com/book/10.1007/978-1-4842-8879-5). Code examples are available on [GitHub](https://github.com/Apress/Ansible-For-VMware-by-Examples_Luca-Berton).

## COMMUNITY EVENTS AND MEETUPS 📅

[anwesha](https://matrix.to/#/@anwesha:ansible.im) said

> We are reviving the Stockholm Ansible Meetup group from the new year, 2023 💖 We are having our in-person meetup on 12th January 2023.
> 
> The plan is to know and talk about the state and the working of the Ansible community. We are also holding a lightning talks session where you can share your Ansible story and your overall automation journey.
> 
> Register your talk for the lightning talks session, check out the detailed plan and RSVP at our [event page](https://www.meetup.com/ansible-stockholm/events/290310440/). 
> 
> See you all folks there.🙂

## THAT'S ALL FOR NOW!

Have any questions you’d like to ask, or issues you’d like to see covered? Please ask in [#social:ansible.com](https://matrix.to/#/#social:ansible.com)! See you next time!
