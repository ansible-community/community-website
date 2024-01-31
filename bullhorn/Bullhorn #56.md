---
title: "Bullhorn #56"
date: 2022-04-29 12:30 UTC
tags: news
category: bullhorn
type: text
---

![Ansible Bullhorn banner](/images/bullhorn-banner-mango.png)

*A Newsletter for the Ansible Developer Community*
*Issue #56, 2022-04-29 ([Past Issues](https://us19.campaign-archive.com/home/?u=56d874e027110e35dea0e03c1&id=d6635f5420))*

Welcome to [The Bullhorn](https://github.com/ansible/community/wiki/News#the-bullhorn), our newsletter for the Ansible developer community. If you have any questions or content you’d like to share, you're welcome to chat with us in the [Ansible Social room on Matrix](https://matrix.to/#/#social:ansible.com), and mention [`newsbot`](https://matrix.to/#/@newsbot:ansible.im) to have your news item tagged for review for the next weekly issue!

<!-- TEASER_END -->

## KEY DATES ⏱️

[cybette](https://matrix.to/#/@cybette:ansible.im) said

> * 2022-05-03: [DaWGs meeting](https://github.com/ansible/community/issues/643), 15:00 UTC
> * 2022-05-04: [Community WG meeting](https://github.com/ansible/community/issues/645), 18:00 UTC (propose topics [here](https://github.com/ansible-community/community-topics/issues))
> * 2022-05-05: [Bullhorn #57 content deadline](https://github.com/ansible/community/wiki/News#the-bullhorn), 18:00 UTC
> * 2022-05-17: [ETA for Ansible 5.8.0 release](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_5.html)
> * 2022-05-23: ETA for Ansible-Core 2.12.6 and Ansible-Core 2.11.12 releases (if those releases have updates)
> * 2022-05-23: [ETA for Ansible-Core 2.13 GA](https://docs.ansible.com/ansible-core/devel/roadmap/ROADMAP_2_13.html)
> * 2022-05-23: [End-of-life for upstream Ansible 2.9 and Ansible-base 2.10](https://groups.google.com/g/ansible-announce/c/kegIH5_okmg/)
> * 2022-06-21: [ETA for Ansible 6.0.0 GA](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_6.html)

## GENERAL NEWS UPDATES 🔈️

[andersson007_](https://matrix.to/#/@andersson007_:matrix.org) contributed

> We are happy to announce that Mario Lenz ([mariolenz](https://github.com/mariolenz)) and Alexei Znamensky ([russoz](https://github.com/russoz)) have joined the [Ansible Community Steering Committee](https://docs.ansible.com/ansible/devel/community/steering/community_steering_committee.html) -  welcome aboard, folks! Thank you for joining us and your great long-term contribution!

[gundalow](https://matrix.to/#/@gundalow:ansible.im) contributed

> ### Process for removing collections from the Ansible Package
> 
> Sometimes the Ansible Community may need to remove a collection from the `ansible` package for stability, legal, or security reasons.
> 
> We've recently signed off on that process, which you can review [here](https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst).

## MAJOR NEW RELEASES 🏆️

### Ansible [↗](https://github.com/ansible-collections) 📦️

The `Ansible` package includes `ansible-core` and is a batteries-included package that provides a curated set of Ansible collections. See the [Ansible roadmaps](https://docs.ansible.com/ansible/devel/roadmap/ansible_roadmap_index.html) for future release plans.

[dmsimard](https://matrix.to/#/@dmsimard:matrix.org) said

> Ansible 5.7.0 has been released with updates to 19 of the included Ansible collections! Read the [announcement](https://groups.google.com/g/ansible-announce/c/-HctLPdjWaM) or check out the [update changelog](https://github.com/ansible-community/ansible-build-data/blob/main/5/CHANGELOG-v5.rst) to learn more about this new version.

### Ansible-Core [↗](https://github.com/ansible/ansible) ⚡️

The `ansible-core` package contains the base engine and a small subset of modules and plugins. To see what's planned for the next release, look at the [`ansible-core` roadmaps](https://docs.ansible.com/ansible-core/devel/roadmap/ansible_core_roadmap_index.html).

[cybette](https://matrix.to/#/@cybette:ansible.im) shared

> [ansible-core 2.12.5 and ansible-core 2.11.11](https://groups.google.com/g/ansible-devel/c/KkFAN1dwVOQ) have been released. These are maintenance releases containing numerous bugfixes.

## COLLECTION UPDATES 🪄

[Sean Sullivan](https://matrix.to/#/@seansulliv:matrix.org) said

> redhat_cop.ah_configuration [0.7.0](https://galaxy.ansible.com/redhat_cop/ah_configuration) has been released.
> Included in this update is addition of management of EE repositories in modules and roles.
> Also an update to simplify updating and uploading collections.

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) contributed

> community.dns 2.1.0 has been released ([changelog](https://github.com/ansible-collections/community.dns/blob/main/CHANGELOG.rst#v2-1-0)). The release includes Execution Environment support next to an updated Public Suffix List.

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) shared

> community.docker [1.10.8](https://github.com/ansible-collections/community.docker/blob/stable-1/CHANGELOG.rst#v1-10-8) and [2.4.0](https://github.com/ansible-collections/community.docker/blob/main/CHANGELOG.rst#v2-4-0) have been released with bugfixes and new features. The 2.4.0 release declares dependencies for Execution Environments for most of its content.

[hunleyd](https://matrix.to/#/@hunleyd:matrix.org) contributed

> The `community.postgresql` collection has released [1.7.3](https://github.com/ansible-collections/community.postgresql/releases/tag/1.7.3) and [2.1.4](https://github.com/ansible-collections/community.postgresql/releases/tag/2.1.4) to fully deprecate Ansible 2.9/2.10. Thanks to our newest contributor [jchancojr](https://github.com/jchancojr) and everyone else involved!

[Gomathi Selvi](https://matrix.to/#/@gomathiselvi:matrix.org) contributed

> The following network collections (major releases) got released earlier today. 
> 
> [ansible.netcommon 3.0.0](https://galaxy.ansible.com/ansible/netcommon)
> [ansible.utils 2.6.1](https://galaxy.ansible.com/ansible/utils)
> [arista.eos 5.0.0](https://galaxy.ansible.com/arista/eos)
> [vyos.vyos 3.0.0](https://galaxy.ansible.com/vyos/vyos)
> [cisco.ios 3.0.0](https://galaxy.ansible.com/cisco/ios)

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) shared

> community.general 4.8.0 has been released ([changelog](https://github.com/ansible-collections/community.general/blob/stable-4/CHANGELOG.rst#v4-8-0)). This is the last 4.x.0 minor release, from now on there will only be bugfix releases (4.8.x) for major version 4. Version 5.0.0 is scheduled for May 17th, with probably an alpha release being made this week.

[rsicart](https://matrix.to/#/@rsicart:matrix.org) shared

> community.mysql [3.1.3](https://github.com/ansible-collections/community.mysql/releases/tag/3.1.3) has been released.

## HELP WANTED 🙏

[samccann](https://matrix.to/#/@samccann:ansible.im) said

> ### Revamping the Ansible Getting Started Guide
> 
> We will be rewriting this guide in the coming months and are looking for your feedback on where the stumbling blocks are for new users to Ansible. Add your comments/ideas/feedback to https://github.com/ansible/ansible/issues/77681 and thanks for your help!

## PROPOSALS - DISCUSS AND VOTE! 🗳️

[gundalow](https://matrix.to/#/@gundalow:ansible.im) shared

> ### Removal of broken collection community.kubevirt from Ansible 6
> 
> `community.kubevirt` depends on `community.kubernetes < 2.0.0`. Since Ansible 5, `community.kubernetes 2.x.y` is included, which effectively breaks the community.kubevirt collection. There has been some initial work ([here](https://github.com/ansible-collections/community.kubevirt/pull/25) and [here](https://github.com/ansible-collections/community.kubevirt/pull/34)) on making `community.kubevirt` work with `community.kubernetes >= 2.0.0` resp. kubernetes.core >= 2.0.0 work, but that work was never completed.
> 
> As it stands we will be moving `community.kubevirt` from Ansible 6.
> 
> Feedback welcome via [community-topics#92](https://github.com/ansible-community/community-topics/issues/92)

[gundalow](https://matrix.to/#/@gundalow:ansible.im) contributed

> ### Schedule community.kubernetes for removal in Ansible 6 or Ansible 7 
> 
> `community.kubernetes 2.0.0` is mostly empty, it contains deprecated redirects to `kubernetes.core`. We announced in Ansible 4.2 ([changelog fragment](https://github.com/ansible-community/ansible-build-data/pull/68/files)) that `community.kubernetes` will be removed eventually from Ansible, but we did not provide an explicit version cut-off. (See [ansible-community/community-topics#22](https://github.com/ansible-community/community-topics/issues/22) for the general discussion.)
> 
> We have three possible ways forward which we need your feedback on:
> 
> 1) Remove `community.kubernetes` from Ansible 6.
> 2) Announce removal of `community.kubernetes` from Ansible 7 in Ansible 6.0.0.
> 3) Do not remove, or announce removal, of community.kubernetes from `ansible` for now. (ie, no change.)
> 
> Please provide your feedback via [community-topics#93](https://github.com/ansible-community/community-topics/issues/93)

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

[gundalow](https://matrix.to/#/@gundalow:ansible.im) contributed

> ### Challenges with reviewing collections to be included in the Ansible Package
> 
> Before new collections can be included in the `ansible` package they have to go through a detailed review via the [Collection checklist](https://github.com/ansible-collections/overview/blob/main/collection_checklist.md) that reflects the [Community collection requirements](https://github.com/ansible-collections/overview/blob/main/collection_requirements.rst). This exists to ensure we maintain a high bar of quality.
> 
> We currently have two major challenges:
> 
> * Lack of reviews, therefore, the submitted collection can't get into the package.
> * A large, and ever growing inclusion [backlog](https://github.com/ansible-collections/ansible-inclusion/discussions/categories/new-collection-reviews): incoming rate is faster than reviews take place.
> 
> We are collecting ideas via [community-topics#97](https://github.com/ansible-community/community-topics/issues/97)

## COMMUNITY UPDATES 👂️

[cybette](https://matrix.to/#/@cybette:ansible.im) shared

> ### Ansible Contributor Survey
> 
> Feedback is really important to us so we can keep on improving the Contributor Experience for our wonderful Ansible Community. Please take a few minutes to fill in the [Contributor Survey](https://www.surveymonkey.co.uk/r/TDB8YQK) that we have put together!

### Maintainers [↗](https://github.com/ansible-community) 🪜

Maintainers help to run the community!

[samccann](https://matrix.to/#/@samccann:ansible.im) contributed

> Collection owners - Edit on GitHub is back! Add `docs/docsite/links.yml` to your collection to enable it. See https://github.com/ansible-collections/collection_template/blob/main/docs/docsite/links.yml for structure and details.

## THAT'S ALL FOR NOW!

Have any questions you’d like to ask, or issues you’d like to see covered? Please ask in [#social:ansible.com](https://matrix.to/#/#social:ansible.com)! See you next time!
