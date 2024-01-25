---
title: "Bullhorn #54"
date: 2022-04-14 21:30 UTC
tags: news
category: bullhorn
type: text
---

![Ansible Bullhorn banner](/images/bullhorn-banner-mango.png)

*A Newsletter for the Ansible Developer Community*
*Issue #54, 2022-04-14 ([Past Issues](https://us19.campaign-archive.com/home/?u=56d874e027110e35dea0e03c1&id=d6635f5420))*

Welcome to [The Bullhorn](https://github.com/ansible/community/wiki/News#the-bullhorn), our newsletter for the Ansible developer community. If you have any questions or content you’d like to share, you're welcome to chat with us in the [Ansible Social room on Matrix](https://matrix.to/#/#social:ansible.com), and mention [`newsbot`](https://matrix.to/#/@newsbot:ansible.im) to have your news item tagged for review for the next weekly issue!

<!-- TEASER_END -->

## KEY DATES ⏱️

[cybette](https://matrix.to/#/@cybette:ansible.im) contributed

> * 2022-04-19: [DaWGs meeting](https://github.com/ansible/community/issues/643), 15:00 UTC
> * 2022-04-20: [Community WG meeting](https://github.com/ansible/community/issues/645), 18:00 UTC (propose topics [here](https://github.com/ansible-community/community-topics/issues))
> * 2022-04-21: [Bullhorn #55 content deadline](https://github.com/ansible/community/wiki/News#the-bullhorn), 18:00 UTC
> * 2022-04-25: ETA for Ansible-Core 2.12.5 and Ansible-Core 2.11.11 releases (if those releases have updates)
> * 2022-04-26: [ETA for Ansible 5.7.0 release](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_5.html)
> * 2022-04-27: [Community WG meeting](https://github.com/ansible/community/issues/645) topic: [List any backwards incompatible collection releases that Ansible 6.0.0 beta1 should try to accommodate.](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_6.html)
> * 2022-05-23: [ETA for Ansible-Core 2.13 GA](https://docs.ansible.com/ansible-core/devel/roadmap/ROADMAP_2_13.html)
> * 2022-05-23: [End-of-life for upstream Ansible 2.9 and Ansible-base 2.10](https://groups.google.com/g/ansible-announce/c/kegIH5_okmg/)
> * 2022-06-21: [ETA for Ansible 6.0.0 GA](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_6.html)

## GENERAL NEWS UPDATES 🔈️

[cybette](https://matrix.to/#/@cybette:ansible.im) said

> The [live video stream](https://www.youtube.com/watch?v=mili3ax3V4o) from **Ansible Contributor Summit 2022.04** is available for playback! Thanks to [ziegenberg](https://matrix.to/#/@ziegenberg:matrix.org), we now have timestamps for the individual sessions as chapters in the video, so you can go directly to the presentations you're interested in, or might have missed. We will be sharing the rest of the info (talk details, slides, etc.) as well as the Contributor Survey next week. Thanks again to everyone for your participation and making it an amazing experience for all!

### Ansible [↗](https://github.com/ansible-collections) 📦️

The `Ansible` package includes `ansible-core` and is a batteries-included package that provides a curated set of Ansible collections. See the [Ansible roadmaps](https://docs.ansible.com/ansible/devel/roadmap/ansible_roadmap_index.html) for future release plans.

[dmsimard](https://matrix.to/#/@dmsimard:matrix.org) shared

> Ansible 6.0.0 alpha1 (including [ansible-core 2.13.0b0](https://groups.google.com/g/ansible-devel/c/QTRq_6btIKE)) is now available for testing: https://groups.google.com/g/ansible-announce/c/qWfZJ8FoeCI. It includes the newest major releases of included Ansible collections and ships python wheels resulting in significantly improved installation performance. Please give it a try and let us know if you encounter any issues!

## MAJOR NEW RELEASES 🏆️

### Antsibull [↗](https://github.com/ansible-community/antsibull) 🐂

Tooling for building the `Ansible` package and collection documentation.

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) said

> [antsibull 0.44.0 (changelog)](https://github.com/ansible-community/antsibull/blob/main/CHANGELOG.rst#v0-44-0) has been released. Note that upgrading from < 0.44.0 to >= 0.44.0 is complicated by the fact that the package has been split up into three packages: antsibull-core, antsibull-docs, and antsibull. The way `pip` works will probably remove the `antsibull-docs` CLI command since it moved to the dependent package `antsibull-docs`. To work around this, either first uninstall `antsibull` before installing 0.44.0, or re-install `antsibull-docs` afterwards.

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) contributed

> If you are using the `antsibull-docs` or `antsibull-lint collection-docs` CLI command from the `antsibull` package, consider switching to using the new [antsibull-docs 1.0.0 package](https://github.com/ansible-community/antsibull-docs/) instead! It is more stable and comes with less potential baggage to carry around.

## COLLECTION UPDATES 🪄

[hunleyd](https://matrix.to/#/@hunleyd:matrix.org) shared

> `community.postgresql` has released both [1.7.2](https://github.com/ansible-collections/community.postgresql/blob/stable-1/CHANGELOG.rst) and [2.1.3](https://github.com/ansible-collections/community.postgresql/blob/main/CHANGELOG.rst) today with minor fixes and an important deprecation.

[ompragash](https://matrix.to/#/@ompragash:ansible.im) contributed

> [community.network](https://github.com/ansible-collections/community.network) [1.3.7](https://github.com/ansible-collections/community.network/tree/1.3.7) & [2.2.2](https://github.com/ansible-collections/community.network/tree/2.2.2) & [3.2.0](https://github.com/ansible-collections/community.network/tree/3.2.0) have been released with some improvements and bug fixes (see changelogs [1.3.7](https://github.com/ansible-collections/community.network/blob/1.3.7/CHANGELOG.rst#v1-3-7), [2.2.2](https://github.com/ansible-collections/community.network/blob/2.2.2/CHANGELOG.rst#v2-2-2), [3.2.0](https://github.com/ansible-collections/community.network/blob/3.2.0/CHANGELOG.rst#v3-2-0) for more details)🎉

[itsbryantp](https://matrix.to/#/@itsbryantp:matrix.org) shared

> The [ibm.ds8000 1.0.0](https://galaxy.ansible.com/ibm/ds8000) collection has had its first release to Ansible Galaxy! The IBM DS8000 collection provides modules and plugins for interacting with the IBM DS8000 family storage products, starting with host and volume management capabilities. Check out the following [blog](https://lnkd.in/ewAvny6p) to learn more along with the [changelog](https://github.com/ansible-collections/ibm.ds8000/releases/tag/v1.0.0) for more details.

[itsbryantp](https://matrix.to/#/@itsbryantp:matrix.org) said

> The [ibm.ibm_zhmc 1.0.2](https://github.com/zhmcclient/zhmc-ansible-modules) is now certified and available on Ansible Automation Hub! See the [release notes](https://zhmcclient.github.io/zhmc-ansible-modules/1.0.2/release_notes.html) for details.

[jillr](https://matrix.to/#/@jillr:libera.chat) shared

> The Ansible Cloud Team has released the 0.1.0 alpha version of a new collection for AWS using the new Amazon Cloud Control API https://galaxy.ansible.com/amazon/cloud

## COMMUNITY UPDATES 👂️

[gundalow](https://matrix.to/#/@gundalow:ansible.im) said

> **Awesome Ansible** ![Awesome Ansible](https://awesome.re/badge.svg)
> 
> Thanks to the great work by [KeyboardInterrupt](https://github.com/KeyboardInterrupt) we now have [awesome-ansible](https://github.com/ansible-community/awesome-ansible) which has a curated list of cool Ansible projects.
> 
> A lot of time and effort has been put into this list to ensure the resources and projects listed are high-quality, only awesome items. Awesome lists are curations of the best, not everything.
> 
> * Take a look at the [existing list](https://github.com/ansible-community/awesome-ansible/blob/main/README.md), to find something new
> * If you know of something missing, [edit the list](https://github.com/ansible-community/awesome-ansible/edit/main/README.md)
> * Ideas on bigger changes, such as new sections (groups of tools, non-English resources), [raise an issue](https://github.com/ansible-community/awesome-ansible/issues)

## COMMUNITY EVENTS AND MEETUPS 📅

[gundalow](https://matrix.to/#/@gundalow:ansible.im) contributed

> The next Ansible London Virtual Meetup will be on Tuesday 19th April at 18:30 BST (17:30 UTC), all are welcome.
> 
> 1. **ansible-lint future and its fixing new feature** by Sorin Sbarnea
> 2. **Deploying an OpenStack infrastructure on a single server with Ansible** by James Freeman
> 3. **How I migrated from Puppet to Ansible** by Dennis McCarthy
> 
> * Event page: [meetup](https://www.meetup.com/Ansible-London/events/284846000/)
> * YouTube: [live steam](https://youtu.be/F6krXtJ4xSc)
> * Matrix Chat: [#europe:ansible.com](https://matrix.to/#/#europe:ansible.com) (preferred)
> * IRC Chat: `#ansible-eu` on Libera.chat

[dmsimard](https://matrix.to/#/@dmsimard:matrix.org) said

> We'll have our first Ansible Montreal meetup in person since the beginning of the pandemic! Presentations will be in French and available in streaming if you can't make it. Sign up here for the April 21 meetup: https://www.meetup.com/Ansible-Montreal/events/284804996/

## THAT'S ALL FOR NOW!

Have any questions you’d like to ask, or issues you’d like to see covered? Please ask in [#social:ansible.com](https://matrix.to/#/#social:ansible.com)! See you next time!
