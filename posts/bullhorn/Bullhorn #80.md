---
title: "Bullhorn #80"
date: 2022-11-04 21:00 UTC
tags: news
category: bullhorn
type: text
---

![Ansible Bullhorn banner](/images/bullhorn-banner-mango.png)

*A Newsletter for the Ansible Developer Community*
*Issue #80, 2022-11-04 ([Past Issues](https://us19.campaign-archive.com/home/?u=56d874e027110e35dea0e03c1&id=d6635f5420))*

Welcome to [The Bullhorn](https://github.com/ansible/community/wiki/News#the-bullhorn), our newsletter for the Ansible developer community. If you have any questions or content you’d like to share, you're welcome to chat with us in the [Ansible Social room on Matrix](https://matrix.to/#/#social:ansible.com), and mention [`newsbot`](https://matrix.to/#/@newsbot:ansible.im) to have your news item tagged for review for the next weekly issue!

<!-- TEASER_END -->

## KEY DATES ⏱️

[cybette](https://matrix.to/#/@cybette:ansible.im) shared

> * 2022-11-07: ETA for Ansible-Core 2.13.6 release
> * 2022-11-07: [Ansible-Core 2.14 GA](https://docs.ansible.com/ansible-core/devel/roadmap/ROADMAP_2_14.html)
> * 2022-11-07: [Last day for collections to make backwards incompatible releases that will be accepted into Ansible-7](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_7.html)
> * 2022-11-08: [Ansible 7.0.0 beta1 – feature freeze](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_7.html)
> * 2022-11-08: [DaWGs meeting](https://github.com/ansible/community/issues/643), 15:00 UTC
> * 2022-11-09: [Community WG meeting](https://github.com/ansible/community/issues/645), 19:00 UTC (propose topics [here](https://github.com/ansible-community/community-topics/issues))
> * 2022-11-10: [Bullhorn #81 content deadline](https://github.com/ansible/community/wiki/News#the-bullhorn), 18:00 UTC

## GENERAL NEWS UPDATES 🔈️

[gotmax (He/Him)](https://matrix.to/#/@gotmax:matrix.org) contributed

> The weekly community meeting has moved from Wednesdays at 18:00 UTC to Wednesdays at 19:00 UTC so it stays at 2:00 p.m. EST / 8:00 p.m. CET now that DST / summer time is ending. The meeting location -- #ansible-community on IRC and [#community:ansible.com](https://matrix.to/#/#community:ansible.com) on Matrix -- remains the same. As always, all interested community members are welcome!

[samccann](https://matrix.to/#/@samccann:ansible.im) said

> Ansible 2.3 docs have moved to the archive site at https://docs.ansible.com/archive/ansible/2.3/. Update any bookmarks you have as old bookmarks will now redirect to /latest/ documentation.

## MAJOR NEW RELEASES 🏆️

[john-westcott-iv](https://matrix.to/#/@john-westcott-iv:ansible.im) shared

> We're happy to announce that the next release of AWX, version 21.8.0 is now available!
> Some notable features include:
> * Adding ppc64le support parameters
> * Shortcut Instance.objects.me when possible
> * Hostname validation in InstanceSerializer
> * Update UI to support pending health checks.
> * Sending field_name in AttributeError
> * Allows job output to calculate elapsed time
> * Make job lifecycle Cyan again
> * Add arm64 architecture mapping to image_architecture for m1mac
> * Allows health checks on only execution nodes
> 
> In addition AWX Operator version 1.0.0 has also been released!
> Some notable features include:
> * Change no_log type to boolean
> * Enable configuration of route and ingress api versions
> 
> Please see the release pages for more details:
> AWX: [https://github.com/ansible/awx/releases/tag/21.8.0](https://github.com/ansible/awx/releases/tag/21.8.0)
> Operator: [https://github.com/ansible/awx-operator/releases/tag/1.0.0](https://github.com/ansible/awx-operator/releases/tag/1.0.0)
> 
> Known Issues:
> * In AWX Operator the no_log property has changed from a string to a boolean.

## COLLECTION UPDATES 🪄

[briantist](https://matrix.to/#/@briantist:libera.chat) contributed

> `community.hashi_vault` [version `3.4.0`](https://github.com/ansible-collections/community.hashi_vault/releases/tag/3.4.0) has been released with a new module and bugfix. This is the last expected `3.x.y` release before `4.0.0`.

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) contributed

> community.docker 3.2.0 ([changelog](https://github.com/ansible-collections/community.docker/blob/main/CHANGELOG.rst#v3-2-0)) has been released with a new feature and two deprecations in docker_container.

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) said

> community.general 6.0.0-a1 ([changelog](https://github.com/ansible-collections/community.general/blob/main/CHANGELOG.rst#v6-0-0-a1)) has been released. This is a pre-release for the upcoming 6.0.0 major release. The main objective of this pre-release is to make it possible to test the large stuctural changes by flattening the directory structure. See the corresponding entry in the changelog for details.

[andersson007_](https://matrix.to/#/@andersson007_:matrix.org) said

> community.network collection 5.0.0 has been released! See the [changelog](https://github.com/ansible-collections/community.network/blob/stable-5/CHANGELOG.rst) for details. Special thanks to [felixfontein](https://github.com/felixfontein) for removing flat-mapping and other improvements!

[Im0](https://matrix.to/#/@Im0:libera.chat) contributed

> collection.rabbitmq has released version 1.2.3 which is available on github and galaxy.  More details are available within the [changelog](https://github.com/ansible-collections/community.rabbitmq/blob/main/CHANGELOG.rst).

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) shared

> community.crypto 2.8.0 ([changelog](https://github.com/ansible-collections/community.crypto/blob/main/CHANGELOG.rst#v2-8-0)) has been released with some new features. The `openssl_pkcs12` module allows to select an encryption level with recent enough cryptography libraries, and there have been further improvements for the ACME modules with regard to error handling.

[hunleyd](https://matrix.to/#/@hunleyd:matrix.org) said

> The `community.postgresql` team has released [1.7.6](https://github.com/ansible-collections/community.postgresql/blob/stable-1/CHANGELOG.rst) as a bugfix release.

[hunleyd](https://matrix.to/#/@hunleyd:matrix.org) shared

> The `community.postgresql` team has released the [2.3.0](https://github.com/ansible-collections/community.postgresql/blob/main/CHANGELOG.rst) minor release. Thanks to all those involved!

## HELP WANTED 🙏

[andersson007_](https://matrix.to/#/@andersson007_:matrix.org) shared

> The following collection inclusion requests are waiting for your review:
> 
> * [dellemc.unity](https://github.com/ansible-collections/ansible-inclusion/discussions/32)
> 
> See the [process description](https://github.com/ansible-collections/ansible-inclusion#review-process) to learn how to do it.
> 
> If you have any questions, just ping `andersson007` on [Matrix](https://docs.ansible.com/ansible/devel/community/communication.html#ansible-community-on-matrix) in the [#community:ansible.com](https://matrix.to/#/#community:ansible.com) room or on [Libera.Chat IRC](https://docs.ansible.com/ansible/devel/community/communication.html#ansible-community-on-irc) in the `#ansible-community` channel or directly.
> 
> Please help the community extend the Ansible package!

## PROPOSALS - DISCUSS AND VOTE! 🗳️

[gotmax (He/Him)](https://matrix.to/#/@gotmax:matrix.org) said

> The community steering committee has started [a vote](https://github.com/ansible-community/community-topics/discussions/158) on whether we should amend the [Ansible community package removal process](https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst) to consider collections with unresolved [Collection Requirements](https://github.com/ansible-collections/overview/blob/main/collection_requirements.rst) violations unmaintained and thus subject to removal. Please see [the PR](https://github.com/ansible-collections/overview/pull/217) that amends the policy and [the community-topics ticket](https://github.com/ansible-community/community-topics/issues/150) for more information.

## COMMUNITY UPDATES 👂️

[Gwmngilfen](https://matrix.to/#/@gwmngilfen:ansible.im) contributed

> ![](https://i.imgur.com/nHomERE.png)
> 
> Summit review time! Speaking as the data person for the Ansible Community Team, Contributor Summit (and AnsibleFest overall) looks to have been quite popular!
> 
> Typically we might see ~20-25 unique accounts / day in our [Social room](https://matrix.to/#/#social:ansible.com) (and the Summit room is obviously very quiet outside of events). However, we saw *over 100* people in those two rooms during Contributor Summit, and sustained over 50 during the Fest keynotes as well. In total we saw *well over 200 unique accounts* during the week.
> 
> We also saw almost 100 new folks join the Social room over the course of the keynotes (and the rest of the week), for which thanks again to maxamillion and cybette for the keynote and interview shoutouts. We hope you're enjoying it!
> 
> As usual, I'll have the survey out shortly, which is open to all the community (whether you attended Summit or not). I look forward to making *even more plots* for your comsumption 🙂

[steampunks](https://matrix.to/#/@xlab_steampunk:matrix.org) contributed

> [Steampunk Spotter](https://steampunk.si/spotter/) version 1.1 has been released! The new version of this tool that analyzes Ansible Playbooks brings new checks for simplified Ansible upgrades, GitLab integration, and quick reference to Ansible module documentation for the entire Ansible Galaxy.

## COMMUNITY EVENTS AND MEETUPS 📅

[gundalow](https://matrix.to/#/@gundalow:ansible.im) shared

> The Ansible London in-person Meetup returns!
> 
> After a long break, the London Meetup resumes on Wednesday 14th December.
> 
> We will have talks on
> 
> * chocolatey - The Package Manager for Windows
> * Adopting systems compliance using CIS - Remediation and Audit
> 
> [RSVP](https://www.meetup.com/ansible-london/events/289470467/) to reserve your seat.

[gundalow](https://matrix.to/#/@gundalow:ansible.im) contributed

> ### New Meeting: AWX Office Hours
> 
> One of the many benefits of open source projects is the ability to form – and collaborate with – a community of users and contributors. This mutually benefits the project and the community at large: it helps the project stay pertinent to its users (who can first-hand voice their opinions and concerns) and it helps users to gain insight into the overall direction of the project which makes it easier to know what to expect in the future. All the while, contributors are able to implement features, enhancements, and documentation that they themselves consider important.
> 
> This kind of feedback loop is vital to the success of AWX and the AWX team wants to make it as easy as possible for you - our community - to get involved. To that end, we have several things in the works, and would like to begin by announcing our new **AWX Office Hours meeting**.
> 
> Our first meeting will be held on **Tuesday, November 8, 2022** at [1500 UTC](https://dateful.com/time-zone-converter?t=15:00&tz=UTC) on [Google Meet](https://github.com/ansible/awx/issues/13155).
> 
> Add the topics you are interested to [AWX Office Hours Agenda](https://github.com/ansible/awx/issues/13155).

## THE ANSIBLE TEAM IS HIRING 💰️

[Don Naro](https://matrix.to/#/@orandon:ansible.im) said

> We're hiring! The Ansible team at Red Hat is looking for an **Automation Engineer** who loves automating repetitive tasks, diving deep into source code and systems to perform root-cause analysis of issues. Apply to the **Software Quality team** at [this link](https://global-redhat.icims.com/jobs/96532/automation-engineer---ansible-software-quality/job?hub=7) or share with someone you know.

[Don Naro](https://matrix.to/#/@orandon:ansible.im) contributed

> Another exciting opportunity to join the Ansible team at Red Hat. We're looking for someone who constantly looks for ways to break things and rebuild them better. Come and join the **Quality Engineering team** as a developer who designs and automates creative ways to break software and uncover problems. Apply to the role at [this link](https://us-redhat.icims.com/jobs/97074/senior-software-quality-engineer-ansible-quality-engineering/job?hub=7) or share with someone you know.

## THAT'S ALL FOR NOW!

Have any questions you’d like to ask, or issues you’d like to see covered? Please ask in [#social:ansible.com](https://matrix.to/#/#social:ansible.com)! See you next time!
