---
title: "Bullhorn #44"
date: 2022-02-03 22:30 UTC
tags: news
category: bullhorn
type: text
---

![Ansible Bullhorn banner](/images/bullhorn-banner-mango.png)

*A Newsletter for the Ansible Developer Community*
*Issue #44, 2022-02-03 ([Past Issues](https://us19.campaign-archive.com/home/?u=56d874e027110e35dea0e03c1&id=d6635f5420))*

Welcome to [The Bullhorn](https://github.com/ansible/community/wiki/News#the-bullhorn), our newsletter for the Ansible developer community. If you have any questions or content you’d like to share, you're welcome to chat with us in the [Ansible Social room on Matrix](https://matrix.to/#/#social:ansible.com), and mention [`newsbot`](https://matrix.to/#/@newsbot:ansible.im) to have your news item tagged for review for the next weekly issue!

<!-- TEASER_END -->

## KEY DATES

[cybette](https://matrix.to/#/@cybette:ansible.im) shared

> * 2022-02-05/06: [FOSDEM 2022](https://fosdem.org/2022/) featuring a number of [Ansible sessions](https://fosdem.org/2022/search/?q=ansible)
> * 2022-02-08: [DaWGs meeting](https://github.com/ansible/community/issues/643), 16:00 UTC
> * 2022-02-09: [Community WG meeting](https://github.com/ansible/community/issues/645), 18:00 UTC (propose topics [here](https://github.com/ansible-community/community-topics/issues))
> * 2022-02-10: [Bullhorn #45 content deadline](https://github.com/ansible/community/wiki/News#the-bullhorn), 18:00 UTC
> * 2022-02-22: [ETA for Ansible 5.4.0 release](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_5.html)
> * 2022-02-28: ETA for Ansible-Core 2.12.3, Ansible-Core 2.11.9, and Ansible-Base 2.10.18 releases (if those releases have updates)

## GENERAL NEWS UPDATES

[cybette](https://matrix.to/#/@cybette:ansible.im) contributed

> We published the first issue of [The Bullhorn](https://github.com/ansible/community/wiki/News#the-bullhorn) - our newsletter for the Ansible developer community - in April 2020. Since then, it has gained momentum and is now one of the main places people go to for Ansible community news, thanks to all of you! We've been releasing them approximately every 2 weeks so far, but with [newsbot](https://matrix.to/#/@newsbot:ansible.im) streamlining the process and many of you contributing frequently, we are now officially making The Bullhorn a weekly newsletter!
> 
> The deadline for submitting news items will be every Thursday at 18:00 UTC. Please send your updates to [newsbot](https://matrix.to/#/@newsbot:ansible.im) in the [Ansible Social room on Matrix](https://matrix.to/#/#social:ansible.com). If you're on IRC, you can join the `#ansible-social` channel on Libera.Chat and mention `newsbot[m]` with your update, which will achieve the same.

[gundalow](https://matrix.to/#/@gundalow:ansible.im) contributed

> Now that CentOS 8 [has been fully discontinued](https://lists.centos.org/pipermail/centos-announce/2020-December/048208.html), most package mirrors have begun culling CentOS 8 content, which breaks all `ansible-test` CentOS 8 containers configured on discontinued production package mirrors. Rather than rebuilding all versions of the affected containers to use the `vault.centos.org` package mirrors or moving to a clone distro, we're just discontinuing test container support for CentOS 8. This decision is based largely on the fact that RHEL 8 test VM support via ansible-core-ci is available on all branches to provide nearly identical test coverage.
> 
> We recommend that projects immediately remove any `centos8/` ansible-test container entries in their CI matrices, as they will likely fail on tasks that require access to a package mirror. Projects running their CI under Ansible's Azure Pipelines subscription can replace those CentOS 8 matrix entries with `rhel8.2/` - `rhel8.5/` (depending on which version of ansible-test is in use) to get nearly identical coverage under a RHEL 8 VM, provided and paid for by Ansible.
> 
> If you want to discuss this, we welcome feedback in [ansible-collections/news-for-maintainers/discussions/4](https://github.com/ansible-collections/news-for-maintainers/discussions/4).

[deric.crago](https://matrix.to/#/@deric.crago:ansible.im) shared

> Ansible Ubuntu PPA News: Ubuntu 21.04 (hirsute) has been removed from the https://launchpad.net/~ansible/+archive/ubuntu/ansible PPA and Ubuntu 22.04 (jammy) has been added to the https://launchpad.net/~ansible/+archive/ubuntu/testing-ansible PPA

[andersson007_](https://matrix.to/#/@andersson007_:matrix.org) said

> We are happy to announce a new Steering Committee member! Markus Bergholz ([markuman](https://github.com/markuman)) has been a very active community member for several years. He has contributed to the Ansible project as a developer, reviewer, collection maintainer, and a person who helps other contributors and users on IRC/Matrix and GitHub.
> 
> We are happy to get him on board! Our congratulations, Markus, and thank you for your great long-term contribution!
> 
> We have also updated the Steering Committee policies and procedures. To learn more, see the following documents:
> * [Ansible Community Steering Committee](https://github.com/ansible/community-docs/blob/main/ansible_community_steering_committee.rst)
> * [Ansible Community Steering Committee Membership Guidelines](https://github.com/ansible/community-docs/blob/main/steering_committee_membership_guidelines.rst)

## MAJOR NEW RELEASES

### Ansible [↗](https://github.com/ansible-collections)

The `Ansible` package includes `ansible-core` and is a batteries-included package that provides a curated set of Ansible collections. See the [Ansible roadmaps](https://docs.ansible.com/ansible/devel/roadmap/ansible_roadmap_index.html) for future release plans.

[dmsimard](https://matrix.to/#/@dmsimard:matrix.org) contributed

> Ansible 5.3.0 has been released and is available on PyPI !
> Find more information about it in the release [announcement](https://groups.google.com/g/ansible-announce/c/gU0uW0CNwJM) or in the [changelog](https://github.com/ansible-community/ansible-build-data/blob/main/5/CHANGELOG-v5.rst#release-summary).

### Ansible-Core [↗](https://github.com/ansible/ansible)

The `ansible-core` package contains the base engine and a small subset of modules and plugins. To see what's planned for the next release, look at the [`ansible-core` roadmaps](https://docs.ansible.com/ansible-core/devel/roadmap/ansible_core_roadmap_index.html).

[dmsimard](https://matrix.to/#/@dmsimard:matrix.org) contributed

> ansible-core 2.12.2 and 2.11.8 as well as ansible-base 2.10.17 have been released: https://groups.google.com/g/ansible-announce/c/VEdKtbHRDAI

### Antsibull [↗](https://github.com/ansible-community/antsibull)

Tooling for building the `Ansible` package and collection documentation.

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) shared

> antsibull 0.41.0 has been released ([changelog](https://github.com/ansible-community/antsibull/blob/main/CHANGELOG.rst#v0-41-0)) with some new features and bugfixes. The docsite build will now support the new `keyword` field in ansible-core plugin documentation, will strip email addresses from author entries, and mention the plugin type more prominently in the documentation.

## COLLECTION UPDATES

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) shared

> community.crypto 2.2.0 and 1.9.10 have been released with a new feature (2.2.0) and a bugfix. See the [2.2.0 changelog](https://github.com/ansible-collections/community.crypto/blob/main/CHANGELOG.rst#v2-2-0) and the [1.9.10 changelog](https://github.com/ansible-collections/community.crypto/blob/stable-1/CHANGELOG.rst#v1-9-10) for details.

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) shared

> community.general 4.4.0 has been released ([changelog](https://github.com/ansible-collections/community.general/blob/stable-4/CHANGELOG.rst#v4-4-0)).

[gundalow](https://matrix.to/#/@gundalow:ansible.im) contributed

> We've got two new blog posts from Ashwini Mhatre on `Getting Started with Ansible.utils Collection for Playbook Creators`. The Ansible `ansible.utils` collection includes a variety of plugins that aid in the management, manipulation and visibility of data for the Ansible playbook developer. The most common use case for this collection is when you want to work with the complex data structures present in an Ansible playbook, inventory, or returned from modules.
> 
> Plugins are code which will augment ansible-core functionality. This code executes on control node and gives options and extensions for the core features of Red Hat Ansible Automation Platform. This `ansible.utils` plugin collection includes:
> 
> * Filter plugins
> * Lookup plugins
> * Test plugins
> * Modules
> 
> We hope you'll enjoy [part1](https://www.ansible.com/blog/getting-started-with-ansible.utils-collection-for-playbook-creators-part-1) and [part2](https://www.ansible.com/blog/getting-started-with-ansible.utils-collection-for-playbook-creators-part-2), and take a look at the [collection](https://galaxy.ansible.com/ansible/utils) and [source repo](https://github.com/ansible-collections/ansible.utils) where we'd love to hear your suggestions on how to improve the collection.

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) shared

> The community.general 1.x.y and 2.x.y release streams will be End of Life latest on 2022-05-23. This coincides with the feature freeze for Ansible 6; by this date community.general 5.0.0 will have been released as well. This is announced in the latest 1.3.13 and 2.5.8 releases, which contain no user-visible changes.

[jillr](https://matrix.to/#/@jillr:libera.chat) contributed

> The AWS community has begun planning for the 4.0.0 releases of [amazon.aws](https://github.com/ansible-collections/amazon.aws/issues/645) and [community.aws](https://github.com/ansible-collections/community.aws/issues/895).  Please see the linked issues for more details or to get involved.

## HELP WANTED

[samccann](https://matrix.to/#/@samccann:ansible.im) contributed

> Looking for a way to contribute to Ansible? How about starting with one of these easyfix issues? https://github.com/ansible/ansible/issues?q=is%3Aopen+is%3Aissue+label%3Aeasyfix

## PROPOSALS - DISCUSS AND VOTE!

[gundalow](https://matrix.to/#/@gundalow:ansible.im) shared

> *Changelogs* are an important way to let users know about new features, and more importantly potentially backwards incompatible changes which might require you to update how you use a certain Collection. Based on feedback, we've realised that these aren't always written consistently. We are looking for your feedback (especially from end users and maintainers) on how we can give a better experience. We'd love your thoughts via [community-topics#64](https://github.com/ansible-community/community-topics/issues/64).

[samccann](https://matrix.to/#/@samccann:ansible.im) contributed

> We're working on better community and contributor guidlines for Ansible. Please comment at https://github.com/ansible-community/community-topics/issues/60 with your ideas!

## COMMUNITY EVENTS AND MEETUPS

[cybette](https://matrix.to/#/@cybette:ansible.im) contributed

> Check out [FOSDEM 2022](https://fosdem.org/2022/) this weekend (Feb 5-6), with several [Ansible](https://fosdem.org/2022/search/?q=ansible) related talks, including [Simple (but useful) Ansible reporting with ara](https://fosdem.org/2022/schedule/event/ansible_reporting_ara/), [Ansible + Matrix: Through The Looking Glass](https://fosdem.org/2022/schedule/event/matrix_ansible/), and [Lessons from 6 Virtual Ansible Contributor Summits](https://fosdem.org/2022/schedule/event/conference_ansible_lessons/).

[cybette](https://matrix.to/#/@cybette:ansible.im) shared

> Join [Ansible Bangalore](https://www.meetup.com/Ansible-Bangalore/) group in an online meetup about Ansible & AWX on Saturday, Feb 5. Check the details and RSVP [here](https://www.meetup.com/Ansible-Bangalore/events/283638490/).

## THAT'S ALL FOR NOW!

Have any questions you’d like to ask, or issues you’d like to see covered? Please ask in [#social:ansible.com](https://matrix.to/#/#social:ansible.com)! See you next time!
