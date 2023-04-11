---
title: "Bullhorn #87"
date: 2023-01-12 00:45 UTC
tags: news
category: bullhorn
type: text
---

![Ansible Bullhorn banner](/images/bullhorn-banner-mango.png)

*A Newsletter for the Ansible Developer Community*
*Issue #87, 2023-01-11 ([Past Issues](https://us19.campaign-archive.com/home/?u=56d874e027110e35dea0e03c1&id=d6635f5420))*

Welcome to [The Bullhorn](https://github.com/ansible/community/wiki/News#the-bullhorn), our newsletter for the Ansible developer community. If you have any questions or content you’d like to share, you're welcome to chat with us in the [Ansible Social room on Matrix](https://matrix.to/#/#social:ansible.com), and mention [`newsbot`](https://matrix.to/#/@newsbot:ansible.im) to have your news item tagged for review for the next weekly issue!

<!-- TEASER_END -->

## KEY DATES ⏱️

[cybette](https://matrix.to/#/@cybette:ansible.im) contributed

> * 2023-01-17: [DaWGs meeting](https://github.com/ansible/community/issues/678), 16:00 UTC
> * 2023-01-18: [Community WG meeting](https://github.com/ansible/community/issues/679), 19:00 UTC (propose topics [here](https://github.com/ansible-community/community-topics/issues))
> * 2023-01-19: [Bullhorn #88 content deadline](https://github.com/ansible/community/wiki/News#the-bullhorn), 18:00 UTC
> * 2023-01-30: [ETA for Ansible-Core 2.14.2 and 2.13.8 releases](https://groups.google.com/g/ansible-devel/c/IQ7VPnw9yS8)
> * 2023-01-31: [ETA for Ansible 7.2.0 release](https://groups.google.com/g/ansible-devel/c/htFjU7jZVYA)
> * 2023-02-08: [Ansible Contributor Summit 2023.02](https://hackmd.io/@ansible-community/cs202302-planning)

## GENERAL NEWS UPDATES 🔈️

Happy New Year! Welcome to the first issue of The Bullhorn in 2023. We look forward to more exciting collaborations with the Ansible Community this year!

[cybette](https://matrix.to/#/@cybette:ansible.im) said

> ### Ansible Contributor Summit
> 
> Ansible Contributor Summit 2023.02 will be held on the third day of [CfgMgmtCamp 2023](https://cfgmgmtcamp.eu/ghent2023/) on **February 8, 2023**, where participants will be able to join both in-person (in Ghent, Belgium) and online. Please take a look at the initial details [here](https://hackmd.io/@ansible-community/cs202302-planning) and propose your topics!

## COLLECTION UPDATES 🪄

[russoz](https://matrix.to/#/@russoz:matrix.org) contributed

> The modules `community.general.rax_*` are being marked for deprecation, as they all rely on the Python package `pyrax` that has been deprecated in 2017. If you are interested in keeping these modules in the collection, please volunteer to maintain them and hopefully move them away from the deprecated library. See more in [this issue](https://github.com/ansible-collections/community.general/issues/5648).

[mariolenz](https://matrix.to/#/@mariolenz:matrix.org) shared

> The [dellemc.unity](https://galaxy.ansible.com/dellemc/unity) collection has passed the [Collection inclusion procedure](https://github.com/ansible-collections/ansible-inclusion#readme) and will be included in the next minor release of Ansible. Thanks to [rajendraindukuri](https://github.com/rajendraindukuri), [anupamaloke](https://github.com/anupamaloke) and [Jennifer-John](https://github.com/Jennifer-John) for the contribution!

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) said

> community.sops 1.6.0 ([changelog](https://github.com/ansible-collections/community.sops/blob/main/CHANGELOG.rst#v1-6-0)) has been released with improvements for the `community.sops.install` role.

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) contributed

> community.general 6.2.0 ([changelog](https://github.com/ansible-collections/community.general/blob/stable-6/CHANGELOG.rst#v6-2-0)) has been released. Please note that the Rackspace modules might get deprecated in version 7.0.0 and removed in version 9.0.0, since the Python library they are based on (`pyrax`) has been deprecated for a long time. If you are interested in maintaining and improving (potentially partially rewriting?) the modules to avoid removal, please [look at the GitHub issue discussing this](https://github.com/ansible-collections/community.general/issues/5648).

[resmo](https://matrix.to/#/@resmo:libera.chat) shared

> vultr.cloud released v1.5.1, a bug fix release. See [changelog](https://github.com/vultr/ansible-collection-vultr/blob/main/CHANGELOG.rst#v1-5-1) for details.

[markuman](https://matrix.to/#/@markuman:matrix.org) said

> community.proxysql [1.5.0](https://github.com/ansible-collections/community.proxysql/releases/tag/1.5.0) and [1.5.1](https://github.com/ansible-collections/community.proxysql/releases/tag/1.5.1) have been released.

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) shared

> community.crypto 2.10.0 ([changelog](https://github.com/ansible-collections/community.crypto/blob/main/CHANGELOG.rst#v2-10-0)) has been released with bugfixes and a bunch of new filter plugins which make it easier to obtain information from keys, certificates, and other objects.

[Simon Dodsley](https://matrix.to/#/@sdodsley:matrix.org) shared

> purestorage.flasharray 1.16.0 ([changelog](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/blob/master/CHANGELOG.rst#v1-16-0)) has been released with bugfixes and a new module to support the array SNMP Agent.

[abuzachis](https://matrix.to/#/@aevelina:ansible.im) said

> [amazon.aws 3.5.1](https://github.com/ansible-collections/amazon.aws/tree/3.5.1) has been released with a security fix (see [changelog](https://github.com/ansible-collections/amazon.aws/blob/3.5.1/CHANGELOG.rst#v3-5-1) for details).
> 
> [amazon.aws 4.4.0](https://github.com/ansible-collections/amazon.aws/tree/4.4.0) has been released with a number of security and minor bug fixes (see [changelog](https://github.com/ansible-collections/amazon.aws/blob/4.4.0/CHANGELOG.rst#v4-4-0) for details).

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) contributed

> community.routeros 2.6.0 ([changelog](https://github.com/ansible-collections/community.routeros/blob/main/CHANGELOG.rst#v2-6-0)) has been released with new features and bugfixes for the `community.routeros.api_modify` and `community.routeros.api_info` modules.

## PROPOSALS - DISCUSS AND VOTE! 🗳️

[mariolenz](https://matrix.to/#/@mariolenz:matrix.org) said

> As mentioned in [The Bullhorn #83](https://mailchi.mp/redhat/the-bullhorn-83), we consider `community.fortios` an effectively unmaintained collection. Therefore, we've opened a community / steering committee [vote](https://github.com/ansible-community/community-topics/discussions/179) on removing it from the Ansible 9 community package.

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) said

> If you are still using the community.docker 1.x.y releases, you might be interested in the [discussion whether these should be declared End of Life or not](https://github.com/ansible-collections/community.docker/issues/543).

## COMMUNITY UPDATES 👂️

[briantist](https://matrix.to/#/@briantist:libera.chat) shared

> [Galactory](https://github.com/briantist/galactory) has released several new versions. `v0.8.0` released with several features and bugfixes, and our first external contribution. Shortly after patch releases `v0.8.1` and [`v0.8.2`](https://github.com/briantist/galactory/blob/main/CHANGELOG.rst#v0-8-2) released to fix some bugs introduced in `v0.8.0`.

[briantist](https://matrix.to/#/@briantist:libera.chat) shared

> [Galactory](https://github.com/briantist/galactory) has also released [`v0.9.0`](https://github.com/briantist/galactory/blob/main/CHANGELOG.rst#v0-9-0), adding basic support for `ProxyFix` for use with reverse proxies and load balancers.

## COMMUNITY EVENTS AND MEETUPS 📅

[anwesha](https://matrix.to/#/@anwesha:ansible.im) contributed

> The first Ansible Meetup for 2023 is happening tomorrow (January 12) in Stockholm! Check out the details and RSVP at our [event page](https://www.meetup.com/ansible-stockholm/events/290310440/). See you there! 🙂

## THE ANSIBLE TEAM IS HIRING 💰️

[samccann](https://matrix.to/#/@samccann:ansible.im) shared

> Ansible product documentation (AAP) have a few senior technical writing reqs open. See the following for details:
> * [Senior Technical Writer (US-MA-Westford)](https://us-redhat.icims.com/jobs/98391/senior-technical-writer/job?hub=7)
> * [Senior Technical Writer (US-NC-Raleigh)](https://us-redhat.icims.com/jobs/98388/senior-technical-writer/job?hub=7)
> * [Senior Technical Writer (IE-Remote)](https://us-redhat.icims.com/jobs/97562/senior-technical-writer---ansible-automation-platform/job?hub=7)

[samccann](https://matrix.to/#/@samccann:ansible.im) said

> Ansible product documentation (AAP) is looking for a senior content strategist!  See [Senior Content Strategist (US-Remote)](https://us-redhat.icims.com/jobs/98398/senior-content-strategist/job?hub=7) for details!

## THAT'S ALL FOR NOW!

Have any questions you’d like to ask, or issues you’d like to see covered? Please ask in [#social:ansible.com](https://matrix.to/#/#social:ansible.com)! See you next time!
