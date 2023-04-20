---
title: "Bullhorn #62"
date: 2022-06-10 14:45 UTC
tags: news
category: bullhorn
type: text
---

![Ansible Bullhorn banner](/images/bullhorn-banner-mango.png)

*A Newsletter for the Ansible Developer Community*
*Issue #62, 2022-06-10 ([Past Issues](https://us19.campaign-archive.com/home/?u=56d874e027110e35dea0e03c1&id=d6635f5420))*

Welcome to [The Bullhorn](https://github.com/ansible/community/wiki/News#the-bullhorn), our newsletter for the Ansible developer community. If you have any questions or content you’d like to share, you're welcome to chat with us in the [Ansible Social room on Matrix](https://matrix.to/#/#social:ansible.com), and mention [`newsbot`](https://matrix.to/#/@newsbot:ansible.im) to have your news item tagged for review for the next weekly issue!

<!-- TEASER_END -->

## KEY DATES ⏱️

[cybette](https://matrix.to/#/@cybette:ansible.im) said

> * 2022-06-14: [DaWGs meeting](https://github.com/ansible/community/issues/643), 15:00 UTC
> * 2022-06-15: [Community WG meeting](https://github.com/ansible/community/issues/645), 18:00 UTC (propose topics [here](https://github.com/ansible-community/community-topics/issues))
> * 2022-06-16: [Bullhorn #63 content deadline](https://github.com/ansible/community/wiki/News#the-bullhorn), 18:00 UTC
> * 2022-06-20: ETA for Ansible-Core 2.12.7 and Ansible-Core 2.11.13 releases (if those releases have updates)
> * 2022-06-21: [ETA for Ansible 6.0.0 GA](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_6.html)
> * 2022-06-28: [ETA for Ansible 5.10.0, the final Ansible 5.x release](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_5.html)
> * 2022-07-15: Deadline for [CFP submission](https://reg.experiences.redhat.com/flow/redhat/rhaf22/cfp/login) for [AnsibleFest 2022](https://www.ansible.com/ansiblefest)

## GENERAL NEWS UPDATES 🔈️

[andersson007_](https://matrix.to/#/@andersson007_:matrix.org) contributed

> We are happy to announce that the [Collection inclusion policy](https://docs.ansible.com/ansible/devel/community/steering/community_steering_committee.html#collection-inclusion-requests-workflow) has been recently relaxed by the [Ansible Community Steering Committee](https://docs.ansible.com/ansible/devel/community/steering/community_steering_committee.html)!
> 
> Before the change, for a collection to get included in the `ansible` community package, it required reviews and approvals made by two Steering Committee members.
> 
> Now, one Steering Committee member and one Community (non-Steering Committee) member review and approval will be enough!
> 
> This change:
> * Should speed up the `ansible` community package enhancement by involving the broader Community.
> * Opens a great contribution opportunity for non-Steering Committee persons.
> * Allows community members (especially collection developers & maintainers) to learn a lot by checking together with the Steering Committee members if other's collections satisfy the Collection requirements.
> 
> Regular community reviewers will be offered to join the Steering Committee.
> 
> Inclusion requests to review:
> * [ibm.spectrum_virtualize](https://github.com/ansible-collections/ansible-inclusion/discussions/35)
> * [purestorage.fusion](https://github.com/ansible-collections/ansible-inclusion/discussions/48)
> * [vultr.cloud](https://github.com/ansible-collections/ansible-inclusion/discussions/44)
> * [check_point.gaia](https://github.com/ansible-collections/ansible-inclusion/discussions/34)
> * [inspur.ispim](https://github.com/ansible-collections/ansible-inclusion/discussions/47)
> 
> How? Copy the [Review checklist](https://github.com/ansible-collections/overview/blob/main/collection_checklist.md) into a discussion and go through it. See the [complete](https://github.com/ansible-collections/ansible-inclusion/discussions/24#discussioncomment-1485070) example.
> 
> They are waiting for your reviews!
> 
> Thank you!

[samccann](https://matrix.to/#/@samccann:ansible.im) contributed

> Need help writing or editing your collection docs? We have community writers ready to help review docs PRs and provide basic help using the Edit on GitHub feature. These writers can provide grammar and readability advice for your collection docs or other Ansible community project docs. Ping us in the #docs [matrix](https://matrix.to/#/#docs:ansible.com)/[irc](https://web.libera.chat/#ansible-docs) channels to get details on how we can help, and see the project tracking board [here](https://github.com/orgs/ansible-community/projects/3/views/1).

## MAJOR NEW RELEASES 🏆️

### Antsibull [↗](https://github.com/ansible-community/antsibull) 🐂

Tooling for building the `Ansible` package and collection documentation.

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) shared

> antsibull 0.47.0 has been released with a feature that adds a CLI program `ansible-community --version` that allows to print the Ansible version to Ansible 6.0.0rc1 and later releases.

### Ansible [↗](https://github.com/ansible-collections) 📦️

The `Ansible` package includes `ansible-core` and is a batteries-included package that provides a curated set of Ansible collections. See the [Ansible roadmaps](https://docs.ansible.com/ansible/devel/roadmap/ansible_roadmap_index.html) for future release plans.

[ompragash](https://matrix.to/#/@ompragash:ansible.im) said

> 🚨 Ansible 5.9.0 which includes ansible-core 2.12.6 has been released and is available to download from [pypi](https://pypi.python.org/packages/source/a/ansible/ansible-5.9.0.tar.gz)🎉. https://groups.google.com/g/ansible-devel/c/Xb6n9irkar0

[ompragash](https://matrix.to/#/@ompragash:ansible.im) contributed

> We are excited to announce the release of Ansible 6.0.0rc1 (First Release Candidate)!🎉
> 🔗 https://groups.google.com/g/ansible-announce/c/cn2lofbqaGY
> 
> You can install it by running the following command or download it directly from [pypi](https://pypi.python.org/packages/source/a/ansible/ansible-6.0.0rc1.tar.gz):
> 
> ```
> pip install ansible==6.0.0rc1 --user
> ```
> 
> Oh and don't miss out on the all new `ansible-community` command-line utility added in Ansible 6 that prints the version of the Ansible Community package:
> 
> ```
> $ ansible-community --version
> Ansible community version 6.0.0rc1
> ```

## COLLECTION UPDATES 🪄

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) shared

> community.dns 2.2.0 ([changelog](https://github.com/ansible-collections/community.dns/blob/2.2.0/CHANGELOG.rst#v2-2-0)) has been released with new features and an updated Public Suffix List.

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) shared

> community.general 5.1.0 ([changelog](https://github.com/ansible-collections/community.general/blob/stable-5/CHANGELOG.rst#v5-1-0)) has been released with several new features and a new module.

[Qalthos](https://matrix.to/#/@qalthos:ansible.im) shared

> Two more networking collection announcements:
> * [cisco.iosxr 3.1.0](https://github.com/ansible-collections/cisco.iosxr/tree/3.1.0) has been released with new features ([changelog](https://github.com/ansible-collections/cisco.iosxr/blob/3.1.0/CHANGELOG.rst))
> * [junipernetworks.junos 3.0.1](https://github.com/ansible-collections/junipernetworks.junos/tree/3.0.1) has been released with bugfixes ([changelog](https://github.com/ansible-collections/junipernetworks.junos/blob/3.0.1/CHANGELOG.rst))

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) contributed

> community.hrobot 1.4.0 ([changelog](https://github.com/ansible-collections/community.hrobot/blob/main/CHANGELOG.rst#v1-4-0)) has been released with a new feature.

## COMMUNITY UPDATES 👂️

[Gwmngilfen](https://matrix.to/#/@gwmngilfen:ansible.im) said

> I've just published a [blog post](https://emeraldreverie.org/2022/06/07/matrix-adoption-so-far) detailing the data we have on the usage of IRC & Matrix over the last 6 months. The TL;DR is that in terms of users-per-day IRC is flat, and Matrix is growing - check out the post for all the juicy plots!

> ![](https://i.imgur.com/lwI8ltE.png)

## THE ANSIBLE TEAM IS HIRING 💰️

[gundalow](https://matrix.to/#/@gundalow:ansible.im) said

> **Principal Software Engineer (Controller)**
> 
> We are looking for a Principal Software Engineer to work on [Controller](https://www.ansible.com/products/controller), which is the downstream of [AWX](https://github.com/ansible/awx). This is the main component of what was previously called Ansible Tower.
> 
> In this role, you’ll be part of the Controller team whose work powers the Red Hat Ansible Automation Platform and enables customers to centralize and control their IT infrastructure with a visual dashboard, role-based access control, and more. As a Principal Software Engineer, you’ll be working with engineers at a variety of experience levels, developing each other’s skills, trusting in each other’s strengths, and supporting one another as you deliver on team commitments. 
> 
> 
> * Write and maintain high quality code as a member of a team, leading best practice usage by example
> * Lead engineers in building implementations of new designs
> * Develop and mature habits in following engineering best practices
> * Work closely with lead architects and product managers to ensure features and fixes meet desired use-cases
> * Write unit and integration tests as well as understand debugging software 
> * Actively participate in code reviews with the team
> * Work with the Quality Engineering (QE) team to ensure that builds are tested correctly
> * Submit patches for bug fixes to the Red Hat Ansible Automation Platform as well as the open source community; review patches from other community members
> * Mentor other engineers; lead them in delivering quality software
> 
> If this sounds like you, please apply via [jobs.redhat.com](https://us-redhat.icims.com/jobs/93825/principal-software-engineer-%28controller%29/job?hub=7).

## THAT'S ALL FOR NOW!

Have any questions you’d like to ask, or issues you’d like to see covered? Please ask in [#social:ansible.com](https://matrix.to/#/#social:ansible.com)! See you next time!
