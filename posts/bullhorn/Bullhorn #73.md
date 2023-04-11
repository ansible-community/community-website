---
title: "Bullhorn #73"
date: 2022-09-09 08:15 UTC
tags: news
category: bullhorn
type: text
---

![Ansible Bullhorn banner](/images/bullhorn-banner-mango.png)

*A Newsletter for the Ansible Developer Community*
*Issue #73, 2022-09-09 ([Past Issues](https://us19.campaign-archive.com/home/?u=56d874e027110e35dea0e03c1&id=d6635f5420))*

Welcome to [The Bullhorn](https://github.com/ansible/community/wiki/News#the-bullhorn), our newsletter for the Ansible developer community. If you have any questions or content you’d like to share, you're welcome to chat with us in the [Ansible Social room on Matrix](https://matrix.to/#/#social:ansible.com), and mention [`newsbot`](https://matrix.to/#/@newsbot:ansible.im) to have your news item tagged for review for the next weekly issue!

<!-- TEASER_END -->

## KEY DATES ⏱️

[cybette](https://matrix.to/#/@cybette:ansible.im) said

> * 2022-09-12: ETA for Ansible-Core 2.13.4 and Ansible-Core 2.12.9 releases (if those releases have updates)
> * 2022-09-13: [ETA for Ansible 6.4.0 release](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_6.html)
> * 2022-09-13: [DaWGs meeting](https://github.com/ansible/community/issues/643), 15:00 UTC
> * 2022-09-14: [Community WG meeting](https://github.com/ansible/community/issues/645), 18:00 UTC (propose topics [here](https://github.com/ansible-community/community-topics/issues))
> * 2022-09-15: [Bullhorn #74 content deadline](https://github.com/ansible/community/wiki/News#the-bullhorn), 18:00 UTC
> * 2022-09-19: [ansible-core feature freeze, stable-2.14 branch created](https://docs.ansible.com/ansible-core/devel/roadmap/ROADMAP_2_14.html) (related to upcoming [Ansible 7](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_7.html))
> * **2022-10-17: [Ansible Contributor Summit 2022.10](https://ansiblecs202210.eventbrite.com/?aff=hackmd)**
> * **2022-10-18/19: [AnsibleFest 2022](https://www.ansible.com/ansiblefest?sc_cid=7013a000002i5g3AAA)**

## MAJOR NEW RELEASES 🏆️

### Antsibull [↗](https://github.com/ansible-community/antsibull) 🐂

Tooling for building the `Ansible` package and collection documentation.

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) shared

> antsibull-docs 1.4.0 ([changelog](https://github.com/ansible-community/antsibull-docs/blob/main/CHANGELOG.rst#v1-4-0)) has been released with new features and a bugfix. Installation instructions and collection links can now be customized, and error pages try to link to the collection's issue tracker instead of the collection's URL if possible.

## COLLECTION UPDATES 🪄

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) said

> community.docker 3.1.0 ([changelog](https://github.com/ansible-collections/community.docker/blob/main/CHANGELOG.rst#v3-1-0)) has been released with a new feature for `community.docker.docker_swarm` and some documentation improvements. The collection now also fully conforms to the REUSE specifications (except for the changelog fragments).

[andersson007_](https://matrix.to/#/@andersson007_:matrix.org) said

> The [community.mysql](https://github.com/ansible-collections/community.mysql) collection version [3.5.0](https://github.com/ansible-collections/community.mysql/blob/main/CHANGELOG.rst#v3-5-0) has been released! Special thanks to [rsicart](https://github.com/rsicart), [betanummeric](https://github.com/betanummeric), [laurent-indermuehle](https://github.com/laurent-indermuehle) and [aneustroev](https://github.com/aneustroev)!

## HELP WANTED 🙏

[andersson007_](https://matrix.to/#/@andersson007_:matrix.org) shared

> The following collection inclusion requests are waiting for your review:
> 
> * [dellemc.unity](https://github.com/ansible-collections/ansible-inclusion/discussions/32)
> * [grafana.grafana](https://github.com/ansible-collections/ansible-inclusion/discussions/52)
> 
> See the [process description](https://github.com/ansible-collections/ansible-inclusion#review-process) to learn how to do it.
> 
> If you have any questions, just ping `andersson007_` on [Matrix](https://docs.ansible.com/ansible/devel/community/communication.html#ansible-community-on-matrix) in the [#community:ansible.com](https://matrix.to/#/#community:ansible.com) room or on [Libera.Chat IRC](https://docs.ansible.com/ansible/devel/community/communication.html#ansible-community-on-irc) in the `#ansible-community` channel or directly.
> 
> Please help the community extend the Ansible package!

## COMMUNITY UPDATES 👂️

[briantist](https://matrix.to/#/@briantist:libera.chat) contributed

> ### galactory
> 
> [`galactory` (an Ansible Galaxy proxy for Artifactory)](https://github.com/briantist/galactory) has released [version `0.4.0`](https://github.com/briantist/galactory/releases/tag/v0.4.0) with new support for configuration via config files and environment variables. [Docker releases](https://github.com/briantist/galactory/pkgs/container/galactory) now include `linux/arm64` arch images.

[briantist](https://matrix.to/#/@briantist:libera.chat) shared

> [`galactory` version `0.5.0`](https://github.com/briantist/galactory/releases/tag/v0.5.0) has been released with new options for controlling the upstream proxy cache. With `--cache-write=false` it's now possible to proxy to an upstream without any writes to Artifactory, removing the need for an API key in some configurations.

[steampunks](https://matrix.to/#/@xlab_steampunk:matrix.org) contributed

> ### Steampunk Spotter
> 
> Hey, our team has developed Steampunk Spotter, a tool that analyzes Ansible Playbooks and offers recommendations: https://steampunk.si/spotter/.  You can try it out via CLI for free. 

## COMMUNITY EVENTS AND MEETUPS 📅

[cybette](https://matrix.to/#/@cybette:ansible.im) contributed

> ### Ansible Contributor Summit 2022.10
> 
> The Ansible Contributor Summit will be held the day before AnsibleFest 2022 on **October 17, 2022**, where participants will be able to join both in-person (in Chicago, IL, USA) and online.
> 
>  We have put together a [preliminary agenda](https://hackmd.io/@ansible-community/cs202210-agenda), subject to change based on comments and feedback - and here's where we need your input! Please use the [comment feature on hackmd](https://hackmd.io/s/how-to-use-comments) to comment on the [draft agenda](https://hackmd.io/@ansible-community/cs202210-agenda), or propose additional topics in the [planning hackmd](https://hackmd.io/@ansible-community/cs202210-planning). Alternatively you can ping me on matrix/irc with your comments and suggestions. Thanks!
> 
## THE ANSIBLE TEAM IS HIRING 💰️

[gundalow](https://matrix.to/#/@gundalow:ansible.im) said

> ### Join the Ansible Controller Team
> 
> The Red Hat Ansible Controller Engineering team (which you may know as its upstream name, [AWX](https://github.com/ansible/awx), or old name of Ansible Tower) is looking for a **Python Software Engineer** to join us. In this role, you will add new functionality to and maintain released versions of automation controller by contributing to the design of new features, implementing features from designs, identifying root causes and fixing complex issues, assisting technical support with customer escalations, identifying and resolving gaps in the Continuous Integration (CI) pipeline, and developing needed enhancements. To succeed in this role, you’ll need to be friendly, curious, be willing to learn and teach, be sensitive to the perspectives of others, and care about creating a positive and inclusive environment.
> Successful applicants must reside in a state where Red Hat is registered to do business.
> 
> What you will do
> 
> * Contribute to the design and perform the implementation of new features in automation controller
> * Troubleshoot customer-reported issues, guide in-house issue reproduction, determine root causes, describe issues in detail to fellow engineers and customers, and develop software code changes to resolve issues
> * Regularly communicate and interact with open source communities to provide guidance and understand issues; review community pull requests (PRs)
> * Work closely with technical support, documentation, and quality assurance (QA) teams to identify and deliver improvements to test automation, documentation, and knowledge base for automation controller
> * Develop and deliver customer-focused enhancements in maintenance releases
> * Investigate and recommend strategic improvements for tools and processes to advance and expand efficiency and throughput
> 
> Interested in helping us make Ansible Controller better? [Apply now](https://us-redhat.icims.com/jobs/95831/software-engineer/job?hub=7)

[cybette](https://matrix.to/#/@cybette:ansible.im) shared

> ### Join the Ansible Community Team
> 
> The Red Hat Ansible Community team is looking for a **Senior Software Community Engineer** to join us!
> 
> In this role, you will work as part of a team focused on flourishing our amazing upstream community. The Ansible ecosystem is always growing and expanding. We want you to be part of the team that engages and keeps this community vibrant.
> 
> To find out more and apply, check out the [job description](https://global-redhat.icims.com/jobs/96607/senior-software-community-engineer/job). Note that this is a flexible Remote - global position, available in any country/state where Red Hat has a corporate presence.

## THAT'S ALL FOR NOW!

Have any questions you’d like to ask, or issues you’d like to see covered? Please ask in [#social:ansible.com](https://matrix.to/#/#social:ansible.com)! See you next time!
