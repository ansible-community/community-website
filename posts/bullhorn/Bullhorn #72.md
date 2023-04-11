---
title: "Bullhorn #72"
date: 2022-09-02 15:30 UTC
tags: news
category: bullhorn
type: text
---

![Ansible Bullhorn banner](/images/bullhorn-banner-mango.png)

*A Newsletter for the Ansible Developer Community*
*Issue #72, 2022-09-02 ([Past Issues](https://us19.campaign-archive.com/home/?u=56d874e027110e35dea0e03c1&id=d6635f5420))*

Welcome to [The Bullhorn](https://github.com/ansible/community/wiki/News#the-bullhorn), our newsletter for the Ansible developer community. If you have any questions or content you’d like to share, you're welcome to chat with us in the [Ansible Social room on Matrix](https://matrix.to/#/#social:ansible.com), and mention [`newsbot`](https://matrix.to/#/@newsbot:ansible.im) to have your news item tagged for review for the next weekly issue!

<!-- TEASER_END -->

## KEY DATES ⏱️

[cybette](https://matrix.to/#/@cybette:ansible.im) shared

> * 2022-09-06: [DaWGs meeting](https://github.com/ansible/community/issues/643), 15:00 UTC
> * 2022-09-07: [Community WG meeting](https://github.com/ansible/community/issues/645), 18:00 UTC (propose topics [here](https://github.com/ansible-community/community-topics/issues))
> * 2022-09-08: [Bullhorn #73 content deadline](https://github.com/ansible/community/wiki/News#the-bullhorn), 18:00 UTC
> * 2022-09-12: ETA for Ansible-Core 2.13.4 and Ansible-Core 2.12.9 releases (if those releases have updates)
> * 2022-09-13: [ETA for Ansible 6.4.0 release](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_6.html)
> * 2022-09-19: [ansible-core feature freeze, stable-2.14 branch created](https://docs.ansible.com/ansible-core/devel/roadmap/ROADMAP_2_14.html) (related to upcoming [Ansible 7](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_7.html))
> * **2022-10-17: [Ansible Contributor Summit 2022.10](https://ansiblecs202210.eventbrite.com/?aff=hackmd)**
> * **2022-10-18/19: [AnsibleFest 2022](https://www.ansible.com/ansiblefest?sc_cid=7013a000002i5g3AAA)**

## GENERAL NEWS UPDATES 🔈️

[samccann](https://matrix.to/#/@samccann:ansible.im) contributed

> We are archiving old EOL Ansible doc sets to a new archive site. This will remove search results that point to older docs. Select the `Visit the archive` button from https://docs.ansible.com/ansible_community.html
> 
> We will redirect the older URLs for these doc sets to `latest` so be sure to bookmark this if you are using an EOL version of Ansible. Today's archive has Ansible 2.3. We will announce others as they are archived.

## COLLECTION UPDATES 🪄

[sshnaidm](https://matrix.to/#/@sshnaidm:matrix.org) contributed

> [Openstack Ansible collections](https://opendev.org/openstack/ansible-collections-openstack/src/branch/stable/1.0.0) released stable [version 1.9.0](https://opendev.org/openstack/ansible-collections-openstack/src/branch/stable/1.0.0/CHANGELOG.rst#v1.9.0), it includes about 30 bugfixes and improvements. Also it restricts OpenstackSDK version to be less than 0.99.0, since the 0.99.0 release breaks backward compatibility and a new major collection version will be released for OpenstackSDK > 0.99.0. See more details in [README](https://opendev.org/openstack/ansible-collections-openstack/src/branch/master/README.md#breaking-backward-compatibility-warning).

[mariolenz](https://matrix.to/#/@mariolenz:matrix.org) said

> The [inspur.ispim](https://galaxy.ansible.com/inspur/ispim) collection has been included in the ansible package.

[Simon Dodsley](https://matrix.to/#/@sdodsley:matrix.org) said

> purestorage.fusion 1.1.0 ([changelog](https://github.com/Pure-Storage-Ansible/Fusion-Collection/blob/master/CHANGELOG.rst#v110)) has been released with new features and bugfixes.

[mariolenz](https://matrix.to/#/@mariolenz:matrix.org) contributed

> It looks like the [mellanox.onyx](https://github.com/ansible-collections/mellanox.onyx) collection is effectively unmaintained. According to the current [community guidelines for collections](https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst#unmaintained-collections), we consider removing it in a future version of the Ansible community package. Please see [Unmaintained collection: mellanox.onyx](https://github.com/ansible-community/community-topics/issues/136) for more information or to announce that you’re interested in taking over the maintenance of (a fork of) mellanox.onyx.
> 
> At least one month after this announcement appears here and in the [collection’s issue tracker](https://github.com/ansible-collections/mellanox.onyx/issues/25), the Ansible Community Steering Committee will vote on whether this collection is considered unmaintained and will be removed, or whether it will be kept. If it will be removed, this will happen earliest in Ansible 8.0.0. Please note that you can still manually install the collection with `ansible-galaxy collection install mellanox.onyx` even when it has been removed from Ansible.
 
## HELP WANTED 🙏

[andersson007_](https://matrix.to/#/@andersson007_:matrix.org) shared

> The following collection inclusion requests are waiting for your review:
> 
> * [dellemc.unity](https://github.com/ansible-collections/ansible-inclusion/discussions/32)
> * [lowlydba.sqlserver](https://github.com/ansible-collections/ansible-inclusion/discussions/51)
> * [grafana.grafana](https://github.com/ansible-collections/ansible-inclusion/discussions/52)
> 
> See the [process description](https://github.com/ansible-collections/ansible-inclusion#review-process) to learn how to do it.
> 
> If you have any questions, just ping `andersson007_` on [Matrix](https://docs.ansible.com/ansible/devel/community/communication.html#ansible-community-on-matrix) in the [#community:ansible.com](https://matrix.to/#/#community:ansible.com) room or on [Libera.Chat IRC](https://docs.ansible.com/ansible/devel/community/communication.html#ansible-community-on-irc) in the `#ansible-community` channel or directly.
> 
> Please help the community extend the Ansible package!

## PROPOSALS - DISCUSS AND VOTE! 🗳️

[mariolenz](https://matrix.to/#/@mariolenz:matrix.org) shared

> Please share your opinion on [removing collections that announce themselves as being unmaintained or deprecated](https://github.com/ansible-community/community-topics/issues/130).

## COMMUNITY UPDATES 👂️

[sshnaidm](https://matrix.to/#/@sshnaidm:matrix.org) said

> Let me share with you ["Transible"](https://github.com/sshnaidm/transible) - the tool which converts your cloud to Ansible playbooks, with Openstack and Amazon AWS EC2 & VPC currently supported. Try it and generate Ansible playbooks from your cloud infrastructure. More details in this [Medium article](https://medium.com/@einarum/transible-your-way-to-infrastructure-as-code-with-ansible-eca0774fbea1) and the repository is: https://github.com/sshnaidm/transible

## COMMUNITY EVENTS AND MEETUPS 📅

[cybette](https://matrix.to/#/@cybette:ansible.im) contributed

> ### Ansible Contributor Summit 2022.10
> 
> The Ansible Contributor Summit will be held the day before AnsibleFest 2022 on **October 17, 2022**, where participants will be able to join both in-person (in Chicago, IL, USA) and online.
> 
>  We have put together a [preliminary agenda](https://hackmd.io/@ansible-community/cs202210-agenda), subject to change based on comments and feedback - and here's where we need your input! Please use the [comment feature on hackmd](https://hackmd.io/s/how-to-use-comments) to comment on the [draft agenda](https://hackmd.io/@ansible-community/cs202210-agenda), or propose additional topics in the [planning hackmd](https://hackmd.io/@ansible-community/cs202210-planning). Alternatively you can ping me on matrix/irc with your comments and suggestions. Thanks!
> 
> ### Ansible Atlanta Meetup
> 
> Join [Ansible Atlanta](https://www.meetup.com/ansible-atlanta/) in their next meetup on September 8 to [Learn about Ansible Navigator](https://www.meetup.com/ansible-atlanta/events/287638006/). Check out the details in the links and RSVP.

## THE ANSIBLE TEAM IS HIRING 💰️

[cybette](https://matrix.to/#/@cybette:ansible.im) said

> The Ansible Community team is looking for a **Principal Software Community Engineer** to join us!
> 
> In this role, you will work as part of a team focused on flourishing our amazing upstream community. The Ansible ecosystem is always growing and expanding. We want you to be part of the team that engages and keeps this community vibrant.
> 
> To find out more and apply, check out the [job description](https://global-redhat.icims.com/jobs/96529/principal-software-community-engineer/job?hub=7). Note that this is a flexible Remote - global position, available in any country/state where Red Hat has a corporate presence.

## THAT'S ALL FOR NOW!

Have any questions you’d like to ask, or issues you’d like to see covered? Please ask in [#social:ansible.com](https://matrix.to/#/#social:ansible.com)! See you next time!
