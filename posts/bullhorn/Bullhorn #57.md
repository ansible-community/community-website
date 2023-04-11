---
title: "Bullhorn #57"
date: 2022-05-06 12:40 UTC
tags: news
category: bullhorn
type: text
---

![Ansible Bullhorn banner](/images/bullhorn-banner-mango.png)

*A Newsletter for the Ansible Developer Community*
*Issue #57, 2022-05-06 ([Past Issues](https://us19.campaign-archive.com/home/?u=56d874e027110e35dea0e03c1&id=d6635f5420))*

Welcome to [The Bullhorn](https://github.com/ansible/community/wiki/News#the-bullhorn), our newsletter for the Ansible developer community. If you have any questions or content you’d like to share, you're welcome to chat with us in the [Ansible Social room on Matrix](https://matrix.to/#/#social:ansible.com), and mention [`newsbot`](https://matrix.to/#/@newsbot:ansible.im) to have your news item tagged for review for the next weekly issue!

<!-- TEASER_END -->

## KEY DATES ⏱️

[cybette](https://matrix.to/#/@cybette:ansible.im) shared

> * 2022-05-10: [DaWGs meeting](https://github.com/ansible/community/issues/643), 15:00 UTC
> * 2022-05-11: [Community WG meeting](https://github.com/ansible/community/issues/645), 18:00 UTC (propose topics [here](https://github.com/ansible-community/community-topics/issues))
> * 2022-05-12: [Bullhorn #58 content deadline](https://github.com/ansible/community/wiki/News#the-bullhorn), 18:00 UTC
> * 2022-05-17: [ETA for Ansible 5.8.0 release](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_5.html)
> * 2022-05-23: ETA for Ansible-Core 2.12.6 and Ansible-Core 2.11.12 releases (if those releases have updates)
> * 2022-05-23: [ETA for Ansible-Core 2.13 GA](https://docs.ansible.com/ansible-core/devel/roadmap/ROADMAP_2_13.html)
> * 2022-05-23: [End-of-life for upstream Ansible 2.9 and Ansible-base 2.10](https://groups.google.com/g/ansible-announce/c/kegIH5_okmg/)
> * 2022-06-21: [ETA for Ansible 6.0.0 GA](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_6.html)

## GENERAL NEWS UPDATES 🔈️

[dmsimard](https://matrix.to/#/@dmsimard:matrix.org) shared

> Ansible 6.0.0a2 (including ansible-core 2.13.0rc1) is now available for testing! This is a good opportunity to test the upcoming releases of both ansible and ansible-core and report feedback ahead of their releases. See the release announcement for more information: https://groups.google.com/g/ansible-announce/c/GSFkoR0MWpU

[dmsimard](https://matrix.to/#/@dmsimard:matrix.org) said

> Hi o/
> 
> We're working on implementing regular testing of ansible-test's sanity checks across every collection included in the Ansible community package and found that many are failing sanity tests. It would be great to fix as many as we can before the release of Ansible 6 around 2022-06-21.
> 
> Most failures are not critical and there's a lot of low-hanging fruits that could contribute to improving the quality of the modules and plugins that are released. It's OK to ignore rules that are not relevant but these should be specified in versioned files such as `tests/sanity/ignore-2.12.txt` in order to avoid warnings and errors.
> 
> There's documentation on sanity tests here: https://docs.ansible.com/ansible/latest/dev_guide/testing_sanity.html
> If you are the maintainer of an included collection or would like to help, you can learn more about the effort and the logs from the sanity tests in this issue: https://github.com/ansible-community/community-topics/issues/96
> 
> If you'd like to chat about Ansible packaging in general, find us in:
> - #ansible-community and #ansible-packaging on libera.chat, or
> - [#community:ansible.com](https://matrix.to/#/#community:ansible.com) and [#packaging:ansible.com](https://matrix.to/#/#packaging:ansible.com) on matrix

## MAJOR NEW RELEASES 🏆️

### Antsibull [↗](https://github.com/ansible-community/antsibull) 🐂

Tooling for building the `Ansible` package and collection documentation.

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) contributed

> antsibull-docs 1.1.0 ([changelog](https://github.com/ansible-community/antsibull-docs/blob/main/CHANGELOG.rst#v1-1-0)) has been released. It improves presentation of lookup plugins, and supports ansible-core 2.14's sidecar docs feature for test and filter plugins.

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) shared

> antsibull 0.45.0 ([changelog](https://github.com/ansible-community/antsibull/blob/main/CHANGELOG.rst#v0-45-0)) has been released. It has some improvements for building Ansible.

### Ansible [↗](https://github.com/ansible-collections) 📦️

The `Ansible` package includes `ansible-core` and is a batteries-included package that provides a curated set of Ansible collections. See the [Ansible roadmaps](https://docs.ansible.com/ansible/devel/roadmap/ansible_roadmap_index.html) for future release plans.

[dmsimard](https://matrix.to/#/@dmsimard:matrix.org) contributed

> ansible 5.7.1 has been released to address a syntax error that landed in a new version of fortinet.fortios shipped in 5.7.0. We've rolled back the version of the collection to the previous version, 2.1.4. The release announcement is available here: https://groups.google.com/g/ansible-announce/c/GmOhXTtmj_w

## COLLECTION UPDATES 🪄

[itsbryantp](https://matrix.to/#/@itsbryantp:matrix.org) shared

> The ibm.ibm_zos_core collection has released [version 1.3.3](https://galaxy.ansible.com/ibm/ibm_zos_core) to Ansible Galaxy and Automation Hub! It addresses a couple of zos_copy and zos_job_query module bugs. See the [release notes](https://ibm.github.io/z_ansible_collections_doc/ibm_zos_core/docs/source/release_notes.html#version-1-3-3) for more details.

## HELP WANTED 🙏

[samccann](https://matrix.to/#/@samccann:ansible.im) said

> ### Revamping the Ansible Getting Started Guide
> 
> We will be rewriting this guide in the coming months and are looking for your feedback on where the stumbling blocks are for new users to Ansible. Add your comments/ideas/feedback to https://github.com/ansible/ansible/issues/77681 and thanks for your help!

## COMMUNITY UPDATES 👂️

[hunleyd](https://matrix.to/#/@hunleyd:matrix.org) said

> The `community.postgresql` collection maintainers are pleased to announce the immediate availability of a new Matrix room (https://matrix.to/#/#postgresql:ansible.com) for all users interested in the collection! If you're a current user of the collection seeking help (or wanting to help others), a new user interested in finding out about the collection, or just curious about PostgreSQL and how to use it in your Ansible plays, please feel free to join us and have a chat.

[gundalow](https://matrix.to/#/@gundalow:ansible.im) contributed

> [Pinakes](https://github.com/ansible/pinakes) is the upstream community project for Red Hat's Automation Services Catalog product. You can join the discussion in [#pinakes:ansible.com](https://matrix.to/#/#pinakes:ansible.com)  (`#ansible-pinakes` on Libera.chat)

[cybette](https://matrix.to/#/@cybette:ansible.im) shared

> ### Ansible Contributor Survey
> 
> Feedback is really important to us so we can keep on improving the Contributor Experience for our wonderful Ansible Community. Please take a few minutes to fill in the [Contributor Survey](https://www.surveymonkey.co.uk/r/TDB8YQK) that we have put together!

## PROPOSALS - DISCUSS AND VOTE! 🗳️

[andersson007_](https://matrix.to/#/@andersson007_:matrix.org) contributed

> The Community and Steering committee will be grateful for any feedback on the ["What to do with a lack of collection inclusion reviews"](https://github.com/ansible-community/community-topics/issues/97) community topic. The backlog of [submitted collections](https://github.com/ansible-collections/ansible-inclusion/discussions/) is growing. How can we fix the situation? See the topic for details.

[gundalow](https://matrix.to/#/@gundalow:ansible.im) said

> ### Generic sanity check for all collections
> 
> As https://github.com/ansible-community/ansible-build-data/issues/114 showed we should really check the existing collections included in the Ansible package. Some ideas:
> 
> 1. Set up some nightly CI that runs some basic sanity checks (like `ansible-test sanity --docker -v`) on all collections. Let's specify one or two of the stable branches for that.
> 2. Give all collections that fail this some time to fix it. If they don't, say, in two months, let's deprecate them with planned removal from Ansible 7. (Doing this for Ansible 6 is too close IMO.)
> 3. From then on, warn in advance once new stable branches are added to this CI (and remove old ones so that at most 1-2 of them are active at the same time), with the same rules: if a collection fails CI and doesn't fix it in a certain amount of time (with a new release), they will be deprecated and removed in the next major version of Ansible.
> 
> What do you think?
> 
> Let us know via [community-topics#96](https://github.com/ansible-community/community-topics/issues/96)

## COMMUNITY EVENTS AND MEETUPS 📅

[cybette](https://matrix.to/#/@cybette:ansible.im) contributed

> [Ansible München](https://www.meetup.com/Ansible-Munchen/) group is organizing an [Ansible SpringFest!](https://www.meetup.com/Ansible-Munchen/events/284695940/) It will be on Tuesday, May 31st, starting from 18:00 CEST at Einstein Kultur. There will be 2 talks, "Ansible Automation for SAP - Deployment, Operations and Modernization" and "Ansible and Kubernetes - an alternative to Helm". See [here](https://www.meetup.com/Ansible-Munchen/events/284695940/) for more details and RSVP.

## THAT'S ALL FOR NOW!

Have any questions you’d like to ask, or issues you’d like to see covered? Please ask in [#social:ansible.com](https://matrix.to/#/#social:ansible.com)! See you next time!
