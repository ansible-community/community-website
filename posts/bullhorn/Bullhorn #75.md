---
title: "Bullhorn #75"
date: 2022-09-26 12:00 UTC
tags: news
category: bullhorn
type: text
---

![Ansible Bullhorn banner](/images/bullhorn-banner-mango.png)

*A Newsletter for the Ansible Developer Community*
*Issue #75, 2022-09-23 ([Past Issues](https://us19.campaign-archive.com/home/?u=56d874e027110e35dea0e03c1&id=d6635f5420))*

Welcome to [The Bullhorn](https://github.com/ansible/community/wiki/News#the-bullhorn), our newsletter for the Ansible developer community. If you have any questions or content you’d like to share, you're welcome to chat with us in the [Ansible Social room on Matrix](https://matrix.to/#/#social:ansible.com), and mention [`newsbot`](https://matrix.to/#/@newsbot:ansible.im) to have your news item tagged for review for the next weekly issue!

<!-- TEASER_END -->

## KEY DATES ⏱️

[cybette](https://matrix.to/#/@cybette:ansible.im) shared

> * 2022-09-26: [Start of ansible-core 2.14 betas](https://docs.ansible.com/ansible-core/devel/roadmap/ROADMAP_2_14.html)
> * 2022-09-27: [Ansible-7.0.0 alpha1](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_7.html)
> * 2022-09-27: [DaWGs meeting](https://github.com/ansible/community/issues/643), 15:00 UTC
> * 2022-09-28: [Community WG meeting](https://github.com/ansible/community/issues/645), 18:00 UTC (propose topics [here](https://github.com/ansible-community/community-topics/issues))
> * 2022-09-29: [Bullhorn #76 content deadline](https://github.com/ansible/community/wiki/News#the-bullhorn), 18:00 UTC
> * 2022-10-04: [ETA for Ansible 6.5.0 release](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_6.html)
> * 2022-10-10: ETA for Ansible-Core 2.13.5 and Ansible-Core 2.12.10 releases (if those releases have updates)
> * 2022-10-12: [Community topic: List any backwards incompatible collection releases that beta1 should try to accommodate](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_7.html)
> * **2022-10-17: [Ansible Contributor Summit 2022.10](https://ansiblecs202210.eventbrite.com/?aff=hackmd)**
> * **2022-10-18/19: [AnsibleFest 2022](https://www.ansible.com/ansiblefest?sc_cid=7013a000002i5g3AAA)**

## GENERAL NEWS UPDATES 🔈️

[Gwmngilfen](https://matrix.to/#/@gwmngilfen:ansible.im) said

> ### Room visibility changes on Matrix - rollout complete
> 
> Back in [Issue 63](https://mailchi.mp/redhat/the-bullhorn-63) (in June!) we shared the result of the debate on the visibility changes that had been [voted in by the community](https://github.com/ansible-community/community-topics/issues/43), and that we would start a process of rolling that change out to all rooms gradually. I'm glad to say that this is now complete, and all rooms have been updated. So for IRC folks, **the rooms are now public** and ChanServ entrymsgs will direct you to a copy of the history.
> 
> We went with a slow rollout of a few rooms per week to allow for feedback. In fact we received very little, mostly in the form of positive reactions to the announcements prior to the change in each room (big thanks to those who gave a 👍️). We did also get a few useful comments on the changes, so thanks also to those people for their input (which we acted on).
> 
> Thanks to everyone who participated in the discussion at various points (both in the debate, and during the rollout) - it's been a long process, but I'm glad it was done the way it was 🙏

[samccann](https://matrix.to/#/@samccann:ansible.im) contributed

> ### Hacktoberfest
> 
> Hacktoberfest is coming! Consider adding the topic to your repository to get some community help with your easier issues for this month-long hackfest. See the maintainers section at https://hacktoberfest.com/participation/ for details.

## MAJOR NEW RELEASES 🏆️

### Antsibull [↗](https://github.com/ansible-community/antsibull) 🐂

Tooling for building the `Ansible` package and collection documentation.

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) shared

> antsibull-docs 1.6.0 ([changelog](https://github.com/ansible-community/antsibull-docs/blob/main/CHANGELOG.rst#v1-6-0)) has been released with new features and bugfixes.

### Ansible-Core [↗](https://github.com/ansible/ansible) ⚡️

The `ansible-core` package contains the base engine and a small subset of modules and plugins. To see what's planned for the next release, look at the [`ansible-core` roadmaps](https://docs.ansible.com/ansible-core/devel/roadmap/ansible_core_roadmap_index.html).

[cybette](https://matrix.to/#/@cybette:ansible.im) contributed

> [ansible-core 2.13.4 and ansible-core 2.12.9](https://groups.google.com/g/ansible-devel/c/mBAQY9EMbos) have been released. These are maintenance releases containing numerous bugfixes.

## COLLECTION UPDATES 🪄

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) said

> community.crypto 2.6.0 ([changelog](https://github.com/ansible-collections/community.crypto/blob/main/CHANGELOG.rst#v2-6-0)) has been released. The openssh_keypair module can now export into specific formats when the `cryptography` backend is used, and the acme modules support the HTTP 429 Too Many Requests status code.

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) contributed

> community.crypto 2.7.0 ([changelog](https://github.com/ansible-collections/community.crypto/blob/main/CHANGELOG.rst#v2-7-0)) has been released with another improvement for the ACME modules and improved compatibility for future ansible-core releases.

[Simon Dodsley](https://matrix.to/#/@sdodsley:matrix.org) shared

> purestorage.flasharray 1.14.0 ([changelog](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/blob/master/CHANGELOG.rst#v1-14-0)) has been released with new features and bugfixes.

[briantist](https://matrix.to/#/@briantist:libera.chat) shared

> [`community.hashi_vault` version `3.3.0`](https://github.com/ansible-collections/community.hashi_vault/releases/tag/3.3.0) [[changelog](https://ansible-collections.github.io/community.hashi_vault/tag/3.3.0/collections/community/hashi_vault/docsite/CHANGELOG.html#v3-3-0)] has been released. `vault_token_create`'s support for orphan tokens has been updated for `hvac>=1.0.0`.

[Simon Dodsley](https://matrix.to/#/@sdodsley:matrix.org) said

> purestorage.fusion 1.1.1 ([changelog](https://github.com/Pure-Storage-Ansible/Fusion-Collection/blob/1.1.1/CHANGELOG.rst#v1-1-1)) has been released with a critical bug fix.

[Simon Dodsley](https://matrix.to/#/@sdodsley:matrix.org) contributed

> purestorage.flashblade 1.10.0 ([changelog](https://github.com/Pure-Storage-Ansible/FlashBlade-Collection/blob/master/CHANGELOG.rst#v1-10-0)) has been released with new features and bugfixes.

## HELP WANTED 🙏

[andersson007_](https://matrix.to/#/@andersson007_:matrix.org) shared

> The following collection inclusion requests are waiting for your review:
> 
> * [dellemc.unity](https://github.com/ansible-collections/ansible-inclusion/discussions/32)
> * [grafana.grafana](https://github.com/ansible-collections/ansible-inclusion/discussions/52)
> 
> See the [process description](https://github.com/ansible-collections/ansible-inclusion#review-process) to learn how to do it.
> 
> If you have any questions, just ping `andersson007` on [Matrix](https://docs.ansible.com/ansible/devel/community/communication.html#ansible-community-on-matrix) in the [#community:ansible.com](https://matrix.to/#/#community:ansible.com) room or on [Libera.Chat IRC](https://docs.ansible.com/ansible/devel/community/communication.html#ansible-community-on-irc) in the `#ansible-community` channel or directly.
> 
> Please help the community extend the Ansible package!

## COMMUNITY EVENTS AND MEETUPS 📅

[cybette](https://matrix.to/#/@cybette:ansible.im) said

> [Ansible New Zealand](https://www.meetup.com/ansible-new-zealand/) is having an online meetup on October 6, 2022 at 11:00 NZST. There'll be 2 talks: AAP2 (Ansible Automation Platform) by Ashor Benjamin and Execution Environments (EE) through Ansible Builder by Feliz Karnadi. Check out the details and RSVP [here](https://www.meetup.com/ansible-new-zealand/events/288591399/).

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

## THAT'S ALL FOR NOW!

Have any questions you’d like to ask, or issues you’d like to see covered? Please ask in [#social:ansible.com](https://matrix.to/#/#social:ansible.com)! See you next time!
