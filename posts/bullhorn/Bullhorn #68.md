---
title: "Bullhorn #68"
date: 2022-07-22 08:00 UTC
tags: news
category: bullhorn
type: text
---

![Ansible Bullhorn banner](/images/bullhorn-banner-mango.png)

*A Newsletter for the Ansible Developer Community*
*Issue #68, 2022-07-22 ([Past Issues](https://us19.campaign-archive.com/home/?u=56d874e027110e35dea0e03c1&id=d6635f5420))*

Welcome to [The Bullhorn](https://github.com/ansible/community/wiki/News#the-bullhorn), our newsletter for the Ansible developer community. If you have any questions or content you’d like to share, you're welcome to chat with us in the [Ansible Social room on Matrix](https://matrix.to/#/#social:ansible.com), and mention [`newsbot`](https://matrix.to/#/@newsbot:ansible.im) to have your news item tagged for review for the next weekly issue!

<!-- TEASER_END -->

## KEY DATES ⏱️

[cybette](https://matrix.to/#/@cybette:ansible.im) said

> * 2022-07-26: [DaWGs meeting](https://github.com/ansible/community/issues/643), 15:00 UTC
> * 2022-07-27: [Community WG meeting](https://github.com/ansible/community/issues/645), 18:00 UTC (propose topics [here](https://github.com/ansible-community/community-topics/issues))
> * 2022-08-02: [ETA for Ansible 6.2.0 release](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_6.html)
> * 2022-08-02: [DaWGs meeting](https://github.com/ansible/community/issues/643), 15:00 UTC
> * 2022-08-03: [Community WG meeting](https://github.com/ansible/community/issues/645), 18:00 UTC (propose topics [here](https://github.com/ansible-community/community-topics/issues))
> * 2022-08-04: [Bullhorn #69 content deadline](https://github.com/ansible/community/wiki/News#the-bullhorn), 18:00 UTC
> * 2022-08-15: ETA for Ansible-Core 2.13.3 release
> * 2022-10-17: [Ansible Contributor Summit 2022.10](https://ansiblecs202210.eventbrite.com/?aff=hackmd)
> * 2022-10-18/19: [AnsibleFest 2022](https://www.ansible.com/ansiblefest?sc_cid=7013a000002i5g3AAA)

## GENERAL NEWS UPDATES 🔈️

[ssbarnea](https://matrix.to/#/@ssbarnea:matrix.org) shared

> Ansible DevTools team introduces an [open-source mentoring program](https://github.com/ansible/devtools/wiki/mentoring). If you like some of our tools and want to learn how to improve your open-source contributing skills, this might interest you.

### Ansible-Core [↗](https://github.com/ansible/ansible) ⚡️

The `ansible-core` package contains the base engine and a small subset of modules and plugins. To see what's planned for the next release, look at the [`ansible-core` roadmaps](https://docs.ansible.com/ansible-core/devel/roadmap/ansible_core_roadmap_index.html).

[samccann](https://matrix.to/#/@samccann:ansible.im) contributed

> Ansible Core 2.13 Documentation is now available in Japanese - https://docs.ansible.com/core-translated-ja.html

## MAJOR NEW RELEASES 🏆️

[cybette](https://matrix.to/#/@cybette:ansible.im) said

> [ansible-core 2.13.2](https://groups.google.com/g/ansible-devel/c/TneSb28Qmvk) has been released. This is a maintenance release, with a minor change improving the error message when the download of a pip bootstrap script fails, plus numerous bugfixes.

## COLLECTION UPDATES 🪄

[briantist](https://matrix.to/#/@briantist:libera.chat) contributed

> `community.hashi_vault` has released [version 3.1.0](https://github.com/ansible-collections/community.hashi_vault/releases/tag/3.1.0), announcing a change to a default value that will take place in `4.0.0`.

## PROPOSALS - DISCUSS AND VOTE! 🗳️

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) said

> There is a new community / steering committee vote on whether there should be stronger rules for inter-collection dependencies for collections included in the Ansible package: https://github.com/ansible-community/community-topics/discussions/119

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) contributed

> There is a new community / steering committee vote on whether / how boolean values in documentation and other sources should be normalized: https://github.com/ansible-community/community-topics/discussions/120

[mariolenz](https://matrix.to/#/@mariolenz:matrix.org) shared

> As mentioned in [The Bullhorn #63](https://mailchi.mp/redhat/the-bullhorn-63), we consider `google.cloud` an effectively unmaintained collection. Therefore, we've opened a community / steering committee [vote](https://github.com/ansible-community/community-topics/discussions/121) on removing it from the Ansible 8 community package.

## COMMUNITY UPDATES 👂️

[cybette](https://matrix.to/#/@cybette:ansible.im) contributed

> "Ansible: Up and Running, 3rd Edition" by [Bas Meijer](https://github.com/bbaassssiiee), [Lorin Hochstein](https://github.com/lorin), and [René Moser](https://github.com/resmo) has been released! Check out what's new and reserve your copy [here](https://www.ansiblebook.com/). Code examples are available on [GitHub](https://github.com/ansiblebook).

[steampunks](https://matrix.to/#/@xlab_steampunk:matrix.org) said

> Based on our experience writing countless Ansible Playbooks and Ansible Collections, we’ve created a guide for high-quality Ansible playbooks to achieve safe, reliable, and secure automation: https://steampunk.si/blog/ultimate-guide-for-high-quality-ansible-playbooks/ 

## COMMUNITY EVENTS AND MEETUPS 📅

[cybette](https://matrix.to/#/@cybette:ansible.im) shared

> ### Ansible Contributor Summit
> 
> The [Ansible Contributor Summit](https://github.com/ansible/community/wiki/Contributor-Summit) will be held the day before [AnsibleFest 2022](https://www.ansible.com/ansiblefest?sc_cid=7013a000002i5g3AAA) on **October 17, 2022**, where participants will be able to join both in-person (in Chicago, IL, USA) and online. Please check out the details [on Eventbrite](https://ansiblecs202210.eventbrite.com/?aff=hackmd) and **pre-register for the event as early as possible**!
> 
> Take a look at the [potential topics](https://hackmd.io/@ansible-community/cs202210-planning) and propose your own!

[cybette](https://matrix.to/#/@cybette:ansible.im) contributed

> ### Ansible Atlanta Meetup
> 
> [Ansible Atlanta](https://www.meetup.com/ansible-atlanta/) is restarting their monthly meetups on [August 4](https://www.meetup.com/ansible-atlanta/events/286490353/). Catch up with them to hear updates about what is happening in the Ansble community and how some of the changes are reflected in Red Hat's Ansible Automation Platform.

## THAT'S ALL FOR NOW!

Have any questions you’d like to ask, or issues you’d like to see covered? Please ask in [#social:ansible.com](https://matrix.to/#/#social:ansible.com)! The Bullhorn editor will be taking a mid-year break, and will return in 2 weeks time. See you in August!
