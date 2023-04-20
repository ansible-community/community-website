---
title: "Bullhorn #89"
date: 2023-01-28 08:15 UTC
tags: news
category: bullhorn
type: text
---

![Ansible Bullhorn banner](/images/bullhorn-banner-mango.png)

*A Newsletter for the Ansible Developer Community*
*Issue #89, 2023-01-28 ([Past Issues](https://us19.campaign-archive.com/home/?u=56d874e027110e35dea0e03c1&id=d6635f5420))*

Welcome to [The Bullhorn](https://github.com/ansible/community/wiki/News#the-bullhorn), our newsletter for the Ansible developer community. If you have any questions or content you’d like to share, you're welcome to chat with us in the [Ansible Social room on Matrix](https://matrix.to/#/#social:ansible.com), and mention [`newsbot`](https://matrix.to/#/@newsbot:ansible.im) to have your news item tagged for review for the next weekly issue!

<!-- TEASER_END -->

## KEY DATES ⏱️

[cybette](https://matrix.to/#/@cybette:ansible.im) shared

> * 2023-01-30: [ETA for Ansible-Core 2.14.2 and 2.13.8 releases](https://groups.google.com/g/ansible-devel/c/IQ7VPnw9yS8)
> * 2023-01-31: [ETA for Ansible 7.2.0 release](https://groups.google.com/g/ansible-devel/c/htFjU7jZVYA)
> * 2023-01-31: [DaWGs meeting](https://github.com/ansible/community/issues/678), 16:00 UTC
> * 2023-02-01: [Community WG meeting](https://github.com/ansible/community/issues/679), 19:00 UTC (propose topics [here](https://github.com/ansible-community/community-topics/issues))
> * 2023-02-02: [Bullhorn #90 content deadline](https://github.com/ansible/community/wiki/News#the-bullhorn), 18:00 UTC
> * **2023-02-08: [Ansible Contributor Summit 2023.02](https://hackmd.io/@ansible-community/cs202302-planning)**

## GENERAL NEWS UPDATES 🔈️

**[Ansible Contributor Summit 2023.02](https://hackmd.io/@ansible-community/cs202302-planning)** is in less than 2 weeks! If you are planning to attend in person, please include Workshop/Fringe day when you [register for CfgMgmtCamp](https://cfgmgmtcamp.eu/ghent2023/registration/) and select "Ansible Contributor Summit" as the add-on. For those planning to join virtually, watch this space next week for info on how to participate.

## MAJOR NEW RELEASES 🏆

### AWX Project [↗](https://github.com/ansible/awx)

AWX provides a web-based user interface, REST API, and task engine built on top of Ansible.

[sfoster](https://matrix.to/#/@sfoster:matrix.org) contributed

> We're happy to announce that [AWX version 21.11.0](https://github.com/ansible/awx/releases/tag/21.11.0) is now available! We're happy to announce that [AWX Operator version 1.1.4](https://github.com/ansible/awx-operator/releases/tag/1.1.4) is now available!

## PROJECT UPDATES 🛠️

### AWX Project [↗](https://github.com/ansible/awx)

AWX provides a web-based user interface, REST API, and task engine built on top of Ansible.

[relrod](https://matrix.to/#/@relrod:matrix.org) said

> `awx-ee` images are now being tagged with their respective AWX releases (e.g. there is now a `quay.io/ansible/awx-ee:21.11.0` for the current AWX release). You can of course continue using `latest` if you prefer, but these version tags are meant to provide a stable image version which represents the current state of `awx-ee` at the time of an AWX release. Please try it out and let us know in the [Ansible AWX Matrix channel](https://matrix.to/#/#awx:ansible.com) if you have any feedback or questions!

[relrod](https://matrix.to/#/@relrod:matrix.org) said

> We are looking to upgrade our default `awx-ee` image to CentOS Stream 9 in the near future. We have an image built with that as a base, pushed to quay at `quay.io/ansible/awx-ee:stream9-pre` - Please test it out! We welcome any feedback in the [Ansible AWX Matrix channel](https://matrix.to/#/#awx:ansible.com) or as an issue on the `ansible/awx-ee` [repository](https://github.com/ansible/awx-ee).

## COLLECTION UPDATES 🪄

[Simon Dodsley](https://matrix.to/#/@sdodsley:matrix.org) said

> purestorage.pure1 1.1.0 ([changelog](https://github.com/Pure-Storage-Ansible/Pure1-Collection/releases/tag/1.1.0)) has been released.

[markuman](https://matrix.to/#/@markuman:matrix.org) said

> community.aws [5.2.0](https://github.com/ansible-collections/community.aws/releases/tag/5.2.0) and [4.5.0](https://github.com/ansible-collections/community.aws/releases/tag/4.5.0) has been released.

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) contributed

> community.hrobot 1.7.0 ([changelog](https://github.com/ansible-collections/community.hrobot/blob/main/CHANGELOG.rst#v1-7-0)) has been released with a new module for managing a vSwitch.

[Sean Sullivan](https://matrix.to/#/@ssulliva:matrix.org) contributed

> The infra collections have had recent updates:
> * [infra.ah_configuration 1.1.0](https://github.com/redhat-cop/ah_configuration/releases/tag/1.1.0) Automation hub and galaxy_ng configuration. Majorly improved testing and as a result of fixes all modules and roles work on the last 3 versions of galaxy_ng and Automation Hub.
> * [infra.controller_configuration 2.2.5](https://github.com/redhat-cop/controller_configuration/releases/tag/2.2.5) Various fixes and additions and improvements to collection, including methods to export configuration files from controller to be used by the collection.
> * [infra.ee_utilities 2.0.6](https://github.com/redhat-cop/ee_utilities/releases/tag/2.0.6) Updated several bugs and add ability to use types in collection requirements for building execution environments

[resmo](https://matrix.to/#/@resmo:libera.chat) contributed

> vultr.cloud 1.7.0 ([changelog](https://github.com/vultr/ansible-collection-vultr/blob/v1.7.0/CHANGELOG.rst)) has been released introducing snapshot support.

[mariolenz](https://matrix.to/#/@mariolenz:matrix.org) contributed

> The `community.google` collection [is considered unmaintained](https://github.com/ansible-community/community-topics/issues/160) and will be removed from Ansible 9 if no one starts maintaining it again before Ansible 9. See [the removal process for details on how this works](https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst#cancelling-removal-of-an-unmaintained-collection).
> 
> Please note that you can still manually install the collection with `ansible-galaxy collection install community.google` even when it has been removed from Ansible.

[mariolenz](https://matrix.to/#/@mariolenz:matrix.org) said

> The `community.skydive` collection [is considered unmaintained](https://github.com/ansible-community/community-topics/issues/171) and will be removed from Ansible 9 if no one starts maintaining it again before Ansible 9. See [the removal process for details on how this works](https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst#cancelling-removal-of-an-unmaintained-collection).
> 
> Please note that you can still manually install the collection with `ansible-galaxy collection install community.skydive` even when it has been removed from Ansible.

## HELP WANTED 🙏

[samccann](https://matrix.to/#/@samccann:ansible.im) contributed

> Looking to help out in Ansible but not sure where to start? Take a look at some easyfix or good first issues:
> * across multiple [collections](https://github.com/search?q=user%3Aansible-collections+label%3Aeasyfix%2C%22good+first+issue%22+state%3Aopen&type=Issues )
> * for all [other](https://github.com/search?q=user%3Aansible+user%3Aansible-community+label%3Aeasyfix%2C%22good+first+issue%22+state%3Aopen&type=Issues) Ansible projects

[andersson007_](https://matrix.to/#/@andersson007_:matrix.org) contributed

> Here are a couple of ideas for our contributors on how to get involved in project/package support and governance:
> * Become a [project maintainer](https://docs.ansible.com/ansible/devel/community/contributor_path.html#become-a-collection-maintainer) (collection oriented).
> * Become a [Steering Committee](https://docs.ansible.com/ansible/devel/community/steering/community_steering_committee.html) member (it's not limited by any number).

[andersson007_](https://matrix.to/#/@andersson007_:matrix.org) contributed

> The following collection inclusion requests are waiting for your review:
> 
> * [quantumsheep.scaleway](https://github.com/ansible-collections/ansible-inclusion/discussions/54)
> * [infra/aap_utilities](https://github.com/ansible-collections/ansible-inclusion/discussions/58)
> * [infra/ee_utilities](https://github.com/ansible-collections/ansible-inclusion/discussions/57)
> * [infra/ah_configuration](https://github.com/ansible-collections/ansible-inclusion/discussions/56)
> * [infra/controller_configuration](https://github.com/ansible-collections/ansible-inclusion/discussions/55)
> 
> See the [process description](https://github.com/ansible-collections/ansible-inclusion#review-process) to learn how to do it.
> 
> If you have any questions, just ping `andersson007` on [Matrix](https://docs.ansible.com/ansible/devel/community/communication.html#ansible-community-on-matrix) in the [#community:ansible.com](https://matrix.to/#/#community:ansible.com) room or on [Libera.Chat IRC](https://docs.ansible.com/ansible/devel/community/communication.html#ansible-community-on-irc) in the `#ansible-community` channel or directly.
> 
> Please help the community extend the Ansible package!

## PROPOSALS - DISCUSS AND VOTE! 🗳️

[Don Naro](https://matrix.to/#/@orandon:ansible.im) shared

> As a next step on the path to a new and improved Ansible docsite we want to hear from the community! We've narrowed down a set of key personas that we plan to use to create better entry points to Ansible documentation. The goal is to help community users find docs in a way that fully supports their automation journey. Please add your thoughts in this [community topic](https://github.com/ansible-community/community-topics/issues/175) or comment directly on the personas [here](https://hackmd.io/pZb5w5JFRQW3RJ73n23tlw).

## COMMUNITY UPDATES 👂️

[steampunks](https://matrix.to/#/@xlab_steampunk:matrix.org) said

> Our team did [an experiment](https://steampunk.si/blog/how-to-upgrade-ansible-playbook-in-20-minutes/) to find out how much time you can actually save if you use Steampunk Spotter for Ansible upgrade compared to doing it manually.

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
> * [Ansible Singapore](https://www.meetup.com/ansible-singapore/events/290957740/) on Jan 31 @ 6:30 PM SST
> * [Ansible NOVA](https://www.meetup.com/ansible-nova/events/291072493/) on Feb 9 @ 6:00 PM EST
> * [Ansible Zürich](https://www.meetup.com/ansible-zurich/events/290204496/) on Feb 28 @ 5:00 PM CET
> * [Ansible München](https://www.meetup.com/ansible-munchen/events/289768549/) also on Feb 28 @ 6:00PM CET
> 
> Check out the respective event pages for details and RSVP!

## THAT'S ALL FOR NOW!

Have any questions you’d like to ask, or issues you’d like to see covered? Please ask in [#social:ansible.com](https://matrix.to/#/#social:ansible.com)! See you next time!
