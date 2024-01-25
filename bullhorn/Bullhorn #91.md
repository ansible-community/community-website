---
title: "Bullhorn #91"
date: 2023-02-20 09:00 UTC
tags: news
category: bullhorn
type: text
---

![Ansible Bullhorn banner](/images/bullhorn-banner-mango.png)

*A Newsletter for the Ansible Developer Community*
*Issue #91, 2023-02-20 ([Past Issues](https://us19.campaign-archive.com/home/?u=56d874e027110e35dea0e03c1&id=d6635f5420))*

Welcome to [The Bullhorn](https://github.com/ansible/community/wiki/News#the-bullhorn), our newsletter for the Ansible developer community. If you have any questions or content you’d like to share, you're welcome to chat with us in the [Ansible Social room on Matrix](https://matrix.to/#/#social:ansible.com), and mention [`newsbot`](https://matrix.to/#/@newsbot:ansible.im) to have your news item tagged for review for the next weekly issue!

<!-- TEASER_END -->

## KEY DATES ⏱️

[cybette](https://matrix.to/#/@cybette:ansible.im) shared

> * 2023-02-21: [DaWGs meeting](https://github.com/ansible/community/issues/678), 16:00 UTC
> * 2023-02-22: [Community WG meeting](https://github.com/ansible/community/issues/679), 19:00 UTC (propose topics [here](https://github.com/ansible-community/community-topics/issues))
> * 2023-02-23: [Bullhorn #92 content deadline](https://github.com/ansible/community/wiki/News#the-bullhorn), 18:00 UTC
> * 2023-02-27: ETA for Ansible-Core 2.14.3
> * 2023-02-28: [ETA for Ansible 7.3.0 release](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_7.html)

## GENERAL NEWS UPDATES 🔈️

[Gwmngilfen](https://matrix.to/#/@gwmngilfen:ansible.im) said

> FOSDEM *and* CfgMgmtCamp *and* Contributor Summit happened earlier this month!
> 
> We're not quite ready to share the videos with you yet, but we promise that will be in a near-future Bullhorn for you. Huge thanks to @cybette, Kris & Tosh, the FOSDEM team, and Mark our video guy!
> 
> I'll also be doing an event write-up as soon as I possibly can, so look out for that. In the meantime, put this in your calendar for next year!

## MAJOR NEW RELEASES 🏆️

### AWX Project [↗](https://github.com/ansible/awx)

AWX provides a web-based user interface, REST API, and task engine built on top of Ansible.

[john-westcott-iv](https://matrix.to/#/@john-westcott-iv:ansible.im) said

> We're happy to announce that the next release of AWX, version 21.12.0 is now available!
> Some notable features include:
> * Update clustering.md to be more current
> * Enable support for injecting complex extra vars
> * Adding new management command to allow failsafe enabling of local auth
> * SAML enhancements
> * Add `--order_by` option to awx CLI
> * Re-add workflow approval bulk actions to workflow approvals list
> * Attempt to consolidate CI logic with github_ci_runner target
> 
> In addition AWX Operator version 1.2.0 has also been released!
> Some notable features include:
> * [fix] Backup role use k8s_cp module to write large files
> * Add `additional_labels` parameter
> * Auto-assign NodePort port by default rather than hardcoding a default
> 
> Please see the releases pages for more details: [AWX](https://github.com/ansible/awx/releases/tag/21.12.0), [Operator](https://github.com/ansible/awx-operator/releases/tag/1.2.0).

## COLLECTION UPDATES 🪄

[markuman](https://matrix.to/#/@markuman:matrix.org) contributed

> community.mysql [1.5.0](https://github.com/ansible-collections/community.mysql/releases/tag/1.5.0), [2.4.0](https://github.com/ansible-collections/community.mysql/releases/tag/2.4.0) and [3.6.0](https://github.com/ansible-collections/community.mysql/releases/tag/3.6.0) have been released.

[mariolenz](https://matrix.to/#/@mariolenz:matrix.org) contributed

> As mentioned in [The Bullhorn #90](https://mailchi.mp/redhat/the-bullhorn-90), people stepped up and started to maintain `google.cloud` again. Therefor, we [had a vote on cancelling the removal process](https://github.com/ansible-community/community-topics/issues/105#issuecomment-1412001896) - which was accepted. So this collection will stay in the community package!
> 
> Thanks [toumorokoshi](https://github.com/toumorokoshi) for reaching out to us and resurrecting the collection!

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) contributed

> community.docker 1.10.15 ([changelog](https://github.com/ansible-collections/community.docker/blob/stable-1/CHANGELOG.rst#v1-10-15)) has been released. This is the final release of the 1.x.y release stream; the `stable-1` branch is now End of Life. If you are still using it, please upgrade to community.docker 2.x.y or (better) 3.x.y. If you are still using Ansible 2.9 or ansible-base 2.10, you will have to use 2.x.y, as 3.x.y no longer supports these versions.

## HELP WANTED 🙏

[Don Naro](https://matrix.to/#/@orandon:ansible.im) shared

> Are you interested in helping improve the navigation and layout of "docs.ansible.com"? Do you think you can help connect users with information in the docs more efficiently? If so, the Ansible community team invites you to contribute to [this](https://github.com/ansible/jinja-docsite) repository. We plan to use this repository to overhaul the landing pages for Ansible community documentation and create a more intuitive and modern user experience. See you in the PR queue!

[andersson007_](https://matrix.to/#/@andersson007_:matrix.org) contributed

> The [new collection inclusion requests](https://github.com/ansible-collections/ansible-inclusion/discussions/categories/new-collection-reviews) are waiting for your [reviews](https://github.com/ansible-collections/ansible-inclusion#review-process). Please help the community extend the package!

[samccann](https://matrix.to/#/@samccann:ansible.im) said

> Looking to help out in Ansible but not sure where to start? Take a look at some easyfix or good first issues:
> * across multiple [collections](https://github.com/search?q=user%3Aansible-collections+label%3Aeasyfix%2C%22good+first+issue%22+state%3Aopen&type=Issues )
> * for all [other](https://github.com/search?q=user%3Aansible+user%3Aansible-community+label%3Aeasyfix%2C%22good+first+issue%22+state%3Aopen&type=Issues) Ansible projects

## PROPOSALS - DISCUSS AND VOTE! 🗳️

[andersson007_](https://matrix.to/#/@andersson007_:matrix.org) shared

> The Community will be happy to get your ideas on the `Role or playbook-focused collections: include in the Ansible package or not?` community [topic](https://github.com/ansible-community/community-topics/issues/197)!

[andersson007_](https://matrix.to/#/@andersson007_:matrix.org) contributed

> As the concerns about future of the Ansible package continue to show up, the [Community Certification instead of collection inclusion?](https://github.com/ansible-community/community-topics/issues/198) community topic has been created. Let's discuss it!

[jillr](https://matrix.to/#/@jillr:libera.chat) shared

> The Ansible Cloud team is proposing a new way to **manage cloud resources in a more declarative fashion**. We're looking for community feedback on the project [here](https://github.com/ansible-collections/pravic/pull/12).

## COMMUNITY EVENTS AND MEETUPS 📅

[ompragash](https://matrix.to/#/@ompragash:ansible.im) shared

> 📣 We are excited to announce the upcoming **Ansible Community Day** in India!
> 
> Join us in-person for a day of presentations, workshops, and networking with other Ansible enthusiasts. Learn about the latest developments in Ansible and how it can help you automate your IT infrastructure. Don't miss out on this opportunity to connect with the Ansible community and take your skills to the next level.
> 
> Register now on [meetup.com](https://www.meetup.com/ansible-pune/events/290492160/). If you have an interesting Ansible use case or experience you would like to share, submit your talk proposal [here](https://forms.gle/DjTewB8GsgZdzJkc7).
> 
> 🗓 SAT, FEB 25, 2023, 9:30 AM IST
> 📍 Red Hat India Private Limited, Magarpatta Inner Circle · Pune, Maharashtra

[cybette](https://matrix.to/#/@cybette:ansible.im) said

> There are several community meetups coming up! 
> * [Ansible Atlanta](https://www.meetup.com/ansible-atlanta/events/291211206/) on Feb 23 @ 7:00 PM EST
> * [Ansible Zürich](https://www.meetup.com/ansible-zurich/events/290204496/) on Feb 28 @ 5:00 PM CET
> * [Ansible München](https://www.meetup.com/ansible-munchen/events/289768549/) also on Feb 28 @ 6:00PM CET
> 
> Check out the respective event pages for details and RSVP!

[cmrussell99](https://matrix.to/#/@cmrussell99:matrix.org) shared

> Join the next office hours call on **Event-Driven Ansible**!  We share tips and techniques and most importantly answer your questions as you try Event-Driven Ansible. Next call is on March 2, 2023 at 11AM ET. Register [here](https://www.redhat.com/en/events/webinar/event-driven-ansible-office-hours-march).

## THAT'S ALL FOR NOW!

Have any questions you’d like to ask, or issues you’d like to see covered? Please ask in [#social:ansible.com](https://matrix.to/#/#social:ansible.com)! See you next time!
