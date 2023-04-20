---
title: "Bullhorn #83"
date: 2022-12-03 03:00 UTC
tags: news
category: bullhorn
type: text
---

![Ansible Bullhorn banner](/images/bullhorn-banner-mango.png)

*A Newsletter for the Ansible Developer Community*
*Issue #83, 2022-12-02 ([Past Issues](https://us19.campaign-archive.com/home/?u=56d874e027110e35dea0e03c1&id=d6635f5420))*

Welcome to [The Bullhorn](https://github.com/ansible/community/wiki/News#the-bullhorn), our newsletter for the Ansible developer community. If you have any questions or content you’d like to share, you're welcome to chat with us in the [Ansible Social room on Matrix](https://matrix.to/#/#social:ansible.com), and mention [`newsbot`](https://matrix.to/#/@newsbot:ansible.im) to have your news item tagged for review for the next weekly issue!

<!-- TEASER_END -->

## KEY DATES ⏱️

[cybette](https://matrix.to/#/@cybette:ansible.im) said

> * 2022-12-05: [ETA for Ansible-Core 2.14.1 and 2.13.7 releases](https://groups.google.com/g/ansible-devel/c/IQ7VPnw9yS8)
> * 2022-12-06: [ETA for Ansible 6.7.0 release](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_6.html), the final Ansible 6.x release
> * 2022-12-06: [ETA for Ansible 7.1.0 release](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_7.html)
> * 2022-12-06: [DaWGs meeting](https://github.com/ansible/community/issues/643), 16:00 UTC
> * 2022-12-07: [Community WG meeting](https://github.com/ansible/community/issues/645), 19:00 UTC (propose topics [here](https://github.com/ansible-community/community-topics/issues))
> * 2022-12-08: [Bullhorn #84 content deadline](https://github.com/ansible/community/wiki/News#the-bullhorn), 18:00 UTC

## GENERAL NEWS UPDATES 🔈️

[samccann](https://matrix.to/#/@samccann:ansible.im) shared

> Ansible EOL docs for version 2.5 have been archived [here](https://docs.ansible.com/archive/ansible/2.5/). Update any bookmarks you have. We will redirect all traffic from the old 2.5 site to `/latest/` starting next week.

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) contributed

> If you are using GHA to run tests on collections, you might have noticed strange failures when using ansible-test's `--docker` option when using `ubuntu-latest`. Read more about this and how to fix this in this [issue](https://github.com/ansible-collections/news-for-maintainers/issues/28).

[cybette](https://matrix.to/#/@cybette:ansible.im) contributed

> [Ansible-Core holiday release schedule](https://groups.google.com/g/ansible-devel/c/IQ7VPnw9yS8) - due the the holiday season, the Dec 26/Jan 2 ansible-core release window will be skipped. Ansible-core 2.13.7 and 2.14.1 will be released on December 5, and the next releases will be at the end of January 2023.

## MAJOR NEW RELEASES 🏆️

### Ansible [↗](https://github.com/ansible-collections) 📦️

The `Ansible` package includes `ansible-core` and is a batteries-included package that provides a curated set of Ansible collections. See the [Ansible roadmaps](https://docs.ansible.com/ansible/devel/roadmap/ansible_roadmap_index.html) for future release plans.

[ompragash](https://matrix.to/#/@ompragash:ansible.im) said

> Ansible 7 PPA package is available for the Ubuntu jammy (22.04LTS) & kinetic (22.10) releases!🎉
> 
> Contributors are welcome to test the package and provide us feedback!❤️
> 
> Follow the instructions to install and test Ansible 7 on ubuntu:jammy docker container 🚀
> 
> ```
> # docker run --name=test-ansible7 -td ubuntu:jammy bash
> # docker exec -it test-ansible7 bash
> 
> root@ed6c0c4e2adc:/# TZ=America/New_York && ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
> root@ed6c0c4e2adc:/# apt-get update && apt -y install software-properties-common
> root@ed6c0c4e2adc:/# add-apt-repository ppa:ansible/testing-ansible-7 -y && apt-get update
> root@ed6c0c4e2adc:/# apt install ansible -y
> ```
> 
> ☕️ If you run into installation issues or technical errors, kindly report it on the ansible-community/ppa repo [here](https://github.com/ansible-community/ppa/issues/new).

### AWX Project [↗](https://github.com/ansible/awx)

AWX provides a web-based user interface, REST API, and task engine built on top of Ansible.

[Lila Yasin](https://matrix.to/#/@lyasin:matrix.org) shared

> We're happy to announce that the next release of AWX, version 21.10.0 is now available!
> Some notable features include:
> * Add multiple asset export for awx cli
> * Allow setting max forks and max concurrent jobs per container/instance group
> 
> In addition, AWX Operator version 1.1.1 has also been released!
> 
> Please see the releases pages for more details:
> * AWX: [https://github.com/ansible/awx/releases/tag/21.10.0](https://github.com/ansible/awx/releases/tag/21.10.0)
> * Operator: [https://github.com/ansible/awx-operator/releases/tag/1.1.1](https://github.com/ansible/awx-operator/releases/tag/1.1.1)

## PROJECT UPDATES 🛠️

[dmsimard](https://matrix.to/#/@dmsimard:matrix.org) contributed

> The long overdue release of ara 1.6.0 should come out next week!
> 
> There will be a blog post about the highlights but in the meantime, you can find the full changelog for the latest release candidate on [GitHub](https://github.com/ansible-community/ara/releases/tag/1.6.0rc2).
> 
> If you'd like to test it out ahead of the release: check out the [live demo](https://demo.recordsansible.org) or read the upgrade notes in the changelog, find the [getting started guide](https://github.com/ansible-community/ara#getting-started) and use `pip install --pre ara[server]` when installing from PyPI or the tag `centos9-source-latest` instead of `latest` when using container images.

[Sean Cavanaugh](https://matrix.to/#/@ipvsean:matrix.org) contributed

> [New blog post](https://www.ansible.com/blog/walking-on-clouds-with-ansible) out on ansible.com for the new fully certified collection cloud.terraform, thanks to Nuno Martins for writing this one up.

[John Hardy](https://matrix.to/#/@jonnyfiveiq:matrix.org) shared

> [NEW blog post](https://www.ansible.com/blog/importing/exporting-collections-in-automation-hubs) - How to import/export collections in Automation Hub from CLI, API or UI for Connected or Disconnected environments.

## COLLECTION UPDATES 🪄

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) shared

> community.sops 1.5.0 ([changelog](https://github.com/ansible-collections/community.sops/blob/main/CHANGELOG.rst#v1-5-0)) has been released with a role for installing sops, and two playbooks for installing sops on localhost and remote targets. This makes it easier to use community.sops in Execution Environments.

[Simon Dodsley](https://matrix.to/#/@sdodsley:matrix.org) shared

> purestorage.fusion 1.2.0 ([changelog](https://github.com/Pure-Storage-Ansible/Fusion-Collection/blob/master/CHANGELOG.rst#v1-2-0)) has been released.

[adhawkins](https://matrix.to/#/@adhawkins:libera.chat) contributed

> adhawkins.borgbase 1.0.1 ([release info](https://github.com/adhawkins/ansible-borgbase/releases/tag/v1.0.1)) has been released with a couple of fixes - one which prevented creating new repos.

[Ashwini Mhatre](https://matrix.to/#/@amhatre:matrix.org) said

> We're happy to announce the following networking collection updates:
> * [ansible.utils 2.8.0](https://github.com/ansible-collections/ansible.utils/releases/tag/2.8.0) has been released with new features ([changelog](https://github.com/ansible-collections/ansible.utils/blob/2.8.0/CHANGELOG.rst))
> * [cisco.iosxr 4.0.3](https://github.com/ansible-collections/cisco.iosxr/releases/tag/4.0.3) has been released with bugfixes ([changelog](https://github.com/ansible-collections/cisco.iosxr/blob/4.0.3/CHANGELOG.rst))
> * [cisco.nxos 4.0.1](https://github.com/ansible-collections/cisco.nxos/releases/tag/4.0.1) has been released with bugfixes ([changelog](https://github.com/ansible-collections/cisco.nxos/blob/4.0.1/CHANGELOG.rst))
> * [junipernetworks.junos 4.1.0](https://github.com/ansible-collections/junipernetworks.junos/releases/tag/4.1.0) has been released with new features ([changelog](https://github.com/ansible-collections/junipernetworks.junos/blob/4.1.0/CHANGELOG.rst))

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) contributed

> community.crypto 2.9.0 ([changelog](https://github.com/ansible-collections/community.crypto/blob/main/CHANGELOG.rst#v2-9-0)) has been released with a new feature for `community.crypto.x509_certificate_info`.

[andersson007_](https://matrix.to/#/@andersson007_:matrix.org) said

> The community.postgresql collection version 2.3.1 has been released ([changelog](https://github.com/ansible-collections/community.postgresql/blob/main/CHANGELOG.rst)). Thanks to [vonschultz](https://github.com/vonschultz) and [hunleyd](https://github.com/hunleyd)!

### Collection Removal

[mariolenz](https://matrix.to/#/@mariolenz:matrix.org) said

> It looks like the [community.google](https://github.com/ansible-collections/community.google) collection is effectively unmaintained. According to the current [community guidelines for collections](https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst#unmaintained-collections), we consider removing it in a future version of the Ansible community package. Please see [Unmaintained collection: community.google](https://github.com/ansible-community/community-topics/issues/160) for more information or to announce that you’re interested in taking over the maintenance of `community.google`.
> 
> At least one month after this announcement appears here and in the [collection’s issue tracker](https://github.com/ansible-collections/community.google/issues/21), the Ansible Community Steering Committee will vote on whether this collection is considered unmaintained and will be removed, or whether it will be kept. If it will be removed, this will happen earliest in Ansible 9.0.0. Please note that you can still manually install the collection with `ansible-galaxy collection install community.google` even when it has been removed from Ansible.

[mariolenz](https://matrix.to/#/@mariolenz:matrix.org) said

> It looks like the [community.fortios](https://github.com/ansible-collections/community.fortios) collection is effectively unmaintained. According to the current [community guidelines for collections](https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst#unmaintained-collections), we consider removing it in a future version of the Ansible community package. Please see [Unmaintained collection: community.fortios](https://github.com/ansible-community/community-topics/issues/162) for more information or to announce that you’re interested in taking over the maintenance of (a fork of) `community.fortios`.
> 
> At least one month after this announcement appears here and in the [collection’s issue tracker](https://github.com/ansible-collections/community.fortios/issues/19), the Ansible Community Steering Committee will vote on whether this collection is considered unmaintained and will be removed, or whether it will be kept. If it will be removed, this will happen earliest in Ansible 9.0.0. Please note that you can still manually install the collection with `ansible-galaxy collection install community.fortios` even when it has been removed from Ansible.

[gotmax (He/Him)](https://matrix.to/#/@gotmax:matrix.org) shared

> cyberark.pas is subject to removal from version 9 of the Ansible community package due to unresolved [Collection Requirements](https://github.com/ansible-collections/overview/blob/main/collection_requirements.rst) violations. Please see [community-topics#168](https://github.com/ansible-community/community-topics/issues/168) for more information.

## FEEDBACK WANTED

[mwester](https://matrix.to/#/@mwester:matrix.org) shared

> ### Ansible Modules for configuring SentinelOne Management Consoles
> 
> Hey Ansible Community! Colleagues and I developed some Ansible Modules for configuring SentinelOne Management Consoles and we bundled them into an Ansible collection sva.sentinelone. We would like to have some community feedback and maybe some of you have SentinelOne in use and would like to manage your environment with our collection. You can find the collection on [Ansible Galaxy](https://galaxy.ansible.com/sva/sentinelone) or [Github](https://github.com/svalabs/ansible-collection-sva.sentinelone).

## PROPOSALS - DISCUSS AND VOTE! 🗳️

[mariolenz](https://matrix.to/#/@mariolenz:matrix.org) contributed

> As mentioned in [The Bullhorn #79](https://mailchi.mp/redhat/the-bullhorn-79), we consider `cisco.nso` an effectively unmaintained collection. Therefore, we've opened a community / steering committee [vote](https://github.com/ansible-community/community-topics/discussions/165) on removing it from the Ansible 9 community package.

## COMMUNITY UPDATES 👂️

[cybette](https://matrix.to/#/@cybette:ansible.im) shared

> ### Ansible Contributor Survey
> 
> Feedback is really important to us so we can keep on improving the Contributor Experience for our wonderful Ansible Community. Please take a few minutes to fill in the [Contributor Survey](https://www.surveymonkey.co.uk/r/7PK28F8) that we have put together, and thanks to those who've already done so!

[cybette](https://matrix.to/#/@cybette:ansible.im) contributed

> The Ansible Community Team has a presence on Mastodon as [@ansible@fosstodon.org](https://fosstodon.org/@ansible) - we look forward to sharing news and engaging with the community in the fediverse!

## COMMUNITY EVENTS AND MEETUPS 📅

[cybette](https://matrix.to/#/@cybette:ansible.im) said

> ### Cfgmgmtcamp 2023 and Ansible Contributor Summit
> 
> Join us Feb 6-8, 2023 in Ghent for [CfgMgmtCamp](https://cfgmgmtcamp.eu/ghent2023/). Check out the [CFP](https://cfp.cfgmgmtcamp.org/2023/cfp) looking for presentations, workshops, and fringes. The Dec 6 deadline is fast approaching!
> 
> We will have Ansible Contributor Summit as part of Cfgmgmtcamp on Feb 8, 2023. More details to follow!

## THAT'S ALL FOR NOW!

Have any questions you’d like to ask, or issues you’d like to see covered? Please ask in [#social:ansible.com](https://matrix.to/#/#social:ansible.com)! See you next time!
