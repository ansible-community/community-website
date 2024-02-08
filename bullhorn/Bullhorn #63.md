---
title: "Bullhorn #63"
date: 2022-06-17 11:50 UTC
tags: news
category: bullhorn
type: text
---

![Ansible Bullhorn banner](/images/bullhorn-banner-mango.png)

*A Newsletter for the Ansible Developer Community*
*Issue #63, 2022-06-17 ([Past Issues](https://us19.campaign-archive.com/home/?u=56d874e027110e35dea0e03c1&id=d6635f5420))*

Welcome to [The Bullhorn](https://github.com/ansible/community/wiki/News#the-bullhorn), our newsletter for the Ansible developer community. If you have any questions or content you’d like to share, you're welcome to chat with us in the [Ansible Social room on Matrix](https://matrix.to/#/#social:ansible.com), and mention [`newsbot`](https://matrix.to/#/@newsbot:ansible.im) to have your news item tagged for review for the next weekly issue!

<!-- TEASER_END -->

## KEY DATES ⏱️

[cybette](https://matrix.to/#/@cybette:ansible.im) contributed

> * 2022-06-20: ETA for Ansible-Core 2.13.1 and Ansible-Core 2.12.7 releases
> * 2022-06-21: [ETA for Ansible 6.0.0 GA](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_6.html)
> * 2022-06-21: [DaWGs meeting](https://github.com/ansible/community/issues/643), 15:00 UTC
> * 2022-06-22: [Community WG meeting](https://github.com/ansible/community/issues/645), 18:00 UTC (propose topics [here](https://github.com/ansible-community/community-topics/issues))
> * 2022-06-23: [Bullhorn #64 content deadline](https://github.com/ansible/community/wiki/News#the-bullhorn), 18:00 UTC
> * 2022-06-28: [ETA for Ansible 5.10.0, the final Ansible 5.x release](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_5.html)
> * 2022-07-15: Deadline for [CFP submission](https://reg.experiences.redhat.com/flow/redhat/rhaf22/cfp/login) for [AnsibleFest 2022](https://www.ansible.com/ansiblefest)

## GENERAL NEWS UPDATES 🔈️

[Don Naro](https://matrix.to/#/@orandon:ansible.im) shared

> ### New Ansible Getting Started guide
> 
> We've made the first iteration of the new [Ansible Getting Started](https://docs.ansible.com/ansible/devel/getting_started/index.html) guide available.
> 
> The goal of this content is reducing the barrier to entry for new Ansible users and simplifying the journey for anyone who wants to ramp up on the basics, start writing playbooks, and gain a solid foundation to build Ansible skills.
> 
> The Getting Started guide incorporates a lot of great suggestions from the Ansible community via PRs, chat messages, and Reddit.
> 
> We hope you find it useful and look forward to getting more feedback to improve the content.

[Gwmngilfen](https://matrix.to/#/@gwmngilfen:ansible.im) said

> ### Room visibility changes on Matrix
> 
> As our [adoption of Matrix continues](https://emeraldreverie.org/2022/06/07/matrix-adoption-so-far/), we've been taking a look at the expectations of Matrix users. It's common on modern chat platforms to be able to see the history when you join a room (or even _before_ you join a room), which helps make sure you have the right room, set your expectations, understand the usage patterns, posting frequency, and so on. Today, that's not the case for most of our rooms, as they inherited the IRC-bridged-default of hiding room history from new joiners.
> 
> So, following a [long discussion](https://github.com/ansible-community/community-topics/issues/43) (6 months!) we're happy to announce that the Community and the Steering Committee have approved changing the history visibility on our Matrix rooms to match those expectations. This is a minor, but positive, change for the experience of our Matrix users - but it is also a change in expectations for our IRC users (although in reality, IRC is logged in many places already), so we will be adding ChanServ notices to our rooms to flag this to our IRC folks. Of course, we will be staging this rollout slowly - all rooms will get a ChanServ notice for joining, we'll notify the room manually a few days before the change, and we will only do a few rooms per week. Thanks!

## COLLECTION UPDATES 🪄

[andersson007_](https://matrix.to/#/@andersson007_:matrix.org) said

> ### Collection Inclusion Requests
> 
> The following collection inclusion requests are waiting for your review:
> * [vultr.cloud](https://github.com/ansible-collections/ansible-inclusion/discussions/44)
> * [check_point.gaia](https://github.com/ansible-collections/ansible-inclusion/discussions/34)
> * [purestorage.fusion](https://github.com/ansible-collections/ansible-inclusion/discussions/48)
> 
> See the [review process description](https://github.com/ansible-collections/ansible-inclusion#review-process) to learn how to do it.
> 
> Please help the community extend the package!

[mariolenz](https://matrix.to/#/@mariolenz:matrix.org) contributed

> ### Collection removal
> 
> It looks like the [google.cloud](https://github.com/ansible-collections/google.cloud) collection is effectively unmaintained. According to the current [community guidelines for collections](https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst#unmaintained-collections), we consider removing it in a future version of the Ansible community package. Please see [Unmaintained collection: google.cloud](https://github.com/ansible-community/community-topics/issues/105) for more information or to announce that you're interested in taking over the maintenance of (a fork of) `google.cloud`.
> 
> At least one month after this announcement appears here and in the [collection's issue tracker](https://github.com/ansible-collections/google.cloud/issues/485), the Ansible Community Steering Committee will vote on whether this collection is considered unmaintained and will be removed, or whether it will be kept. If it will be removed, this will happen earliest in Ansible 8.0.0. Please note that you can still manually install the collection with `ansible-galaxy collection install google.cloud` even when it has been removed from Ansible.

## COMMUNITY UPDATES 👂️

[gotmax (He/Him)](https://matrix.to/#/@gotmax:matrix.org) shared

> ### Ansible packages in Fedora Copr
> 
> There is now a COPR repo, [gotmax23/ansible-6](https://copr.fedorainfracloud.org/coprs/gotmax23/ansible-6/), available for Fedora that provides RPM packages for the latest version of ansible (currently 6.0.0rc1) and ansible-core (currently 2.13.0), as well as the latest versions of our packaged standalone collections for the Fedora releases where they are outdated. This enables ansible early adopters to utilize the newest ansible packages that cannot be published in the default repos for stable versions due to major version bumps being prohibited.
> 
> This also allows the maintainers to test our ansible packaging before we publish it in the default repos. Fedora Rawhide will update to Ansible 6 after the 6.0.0 final release, but I plan to continue publishing the latest versions in this COPR for the currently supported stable releases (35 and 36). Feel free to leave feedback in the [COPR's associated Fedora Discussion post](https://discussion.fedoraproject.org/t/gotmax23-ansible-6/39299) or join us in [#packaging:ansible.com](https://matrix.to/#/#packaging:ansible.com) (#ansible-packaging on libera.chat)!

## EVENTS AND MEETUPS 📅

[cybette](https://matrix.to/#/@cybette:ansible.im) shared

> ### AnsibleFest and Ansible Contributor Summit
> 
> [AnsibleFest 2022](https://www.ansible.com/ansiblefest) will be in Chicago, IL (USA) this year, on **October 18 & 19**. [The call for proposals](https://reg.experiences.redhat.com/flow/redhat/rhaf22/cfp/login) is now open until **July 15, 2022**.
> 
> Content topics can include:
> * Getting Started
> * Automating Red Hat products
> * Use Case / Domain-focused (e.g. Network, Security, Cloud)
> * Audience-focused (e.g. Developers, Operations)
> * Thought Leadership
> * Community and Culture
> 
> There will be an **Ansible Contributor Summit** the day before AnsibleFest on **October 17, 2022**, where participants will be able to join both in-person (in Chicago) and online. More details about this event will be shared as we confirm them!

## THE ANSIBLE TEAM IS HIRING 💰️

[gundalow](https://matrix.to/#/@gundalow:ansible.im) said

> ### Principal Software Engineer (Controller)
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
