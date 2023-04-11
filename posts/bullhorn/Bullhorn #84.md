---
title: "Bullhorn #84"
date: 2022-12-12 08:00 UTC
tags: news
category: bullhorn
type: text
---

![Ansible Bullhorn banner](/images/bullhorn-banner-mango.png)

*A Newsletter for the Ansible Developer Community*
*Issue #84, 2022-12-09 ([Past Issues](https://us19.campaign-archive.com/home/?u=56d874e027110e35dea0e03c1&id=d6635f5420))*

Welcome to [The Bullhorn](https://github.com/ansible/community/wiki/News#the-bullhorn), our newsletter for the Ansible developer community. If you have any questions or content you’d like to share, you're welcome to chat with us in the [Ansible Social room on Matrix](https://matrix.to/#/#social:ansible.com), and mention [`newsbot`](https://matrix.to/#/@newsbot:ansible.im) to have your news item tagged for review for the next weekly issue!

<!-- TEASER_END -->

## KEY DATES ⏱️

[cybette](https://matrix.to/#/@cybette:ansible.im) shared

> * 2022-12-13: [AWX Community Office Hours](https://github.com/ansible/awx/issues/13240), 15:00 UTC
> * 2022-12-13: [DaWGs meeting](https://github.com/ansible/community/issues/643), 16:00 UTC
> * 2022-12-14: [Event-Driven Ansible Office Hours](https://www.redhat.com/en/events/webinar/event-driven-ansible-office-hours-december?extIdCarryOver=true&sc_cid=701f2000001OH6uAAG), 16:00 UTC
> * 2022-12-14: [Community WG meeting](https://github.com/ansible/community/issues/645), 19:00 UTC (propose topics [here](https://github.com/ansible-community/community-topics/issues))
> * 2022-12-15: [Bullhorn #85 content deadline](https://github.com/ansible/community/wiki/News#the-bullhorn), 18:00 UTC
> * 2023-01-30: [ETA for Ansible-Core 2.14.2 and 2.13.8 releases](https://groups.google.com/g/ansible-devel/c/IQ7VPnw9yS8)

## MAJOR NEW RELEASES 🏆️

### Ansible [↗](https://github.com/ansible-collections) 📦️

The `Ansible` package includes `ansible-core` and is a batteries-included package that provides a curated set of Ansible collections. See the [Ansible roadmaps](https://docs.ansible.com/ansible/devel/roadmap/ansible_roadmap_index.html) for future release plans.

[anwesha](https://matrix.to/#/@anwesha:ansible.im) contributed

> Ansible 6.7.0 is out! ❤️ (🔗 [announcement](https://groups.google.com/g/ansible-project/c/ZJ0MZ1SjBhg))
> 
> 💽You can install it by running the following command or download the release tarball directly from [pypi](https://pypi.python.org/packages/source/a/ansible/ansible-6.7.0.tar.gz):
> 
> ```
> python3 -m pip install ansible==6.7.0 --user
> ```
> 
> 🔆Try the `ansible-community` command-line utility added in Ansible 6 that prints the version of the Ansible Community package:
> 
> ```
> $ ansible-community --version
> Ansible community version 6.7.0
> ```
> 
> ➡️ Check [Release Notes📦️🗒️](https://github.com/ansible-community/ansible-build-data/blob/main/6/CHANGELOG-v6.rst) and [Ansible 6 Porting Guide](https://docs.ansible.com/ansible/devel/porting_guides/porting_guide_6.html) for more details!

[anwesha](https://matrix.to/#/@anwesha:ansible.im) shared

> Ansible 7.1.0 is out! ❤️ (🔗 [announcement](https://groups.google.com/g/ansible-announce/c/n_DC6V-4gwI))
> 
> 💽You can install it by running the following command or download the release tarball directly from [pypi](https://pypi.python.org/packages/source/a/ansible/ansible-7.1.0.tar.gz):
> 
> ```
> pip install ansible==7.1.0 --user
> ```
> 
> ➡️ Check [Release Notes📦️🗒️](https://github.com/ansible-community/ansible-build-data/blob/main/7/CHANGELOG-v7.rst) and [Ansible 7 Porting Guide](https://docs.ansible.com/ansible/devel/porting_guides/porting_guide_7.html) for more details!

### Antsibull [↗](https://github.com/ansible-community/antsibull) 🐂

Tooling for building the `Ansible` package and collection documentation.

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) contributed

> antsibull 0.52.0 ([changelog](https://github.com/ansible-community/antsibull/blob/main/CHANGELOG.rst#v0-52-0)) has been released with some breaking changes. Some long deprecated features have been removed, and there is now a `validate-tags` subcommand to ensure that collection versions in an Ansible release are tagged in collections' respective git repositories.

[gotmax (He/Him)](https://matrix.to/#/@gotmax:matrix.org) contributed

> [antsibull-core 2.0.0a1](https://pypi.org/project/antsibull-core/2.0.0a1/) has been released. This major release drops support for Python 3.6, 3.7, and 3.8 and deprecates some compatability code ([full changelog](https://github.com/ansible-community/antsibull-core/blob/2.0.0a1/CHANGELOG.rst#v2-0-0a1)). It also includes a new feature needed by `antsibull-build`. antsibull-core houses shared code used by [`antsibull-build`](https://github.com/ansible-community/antsibull) and [`antsibull-docs`](https://github.com/ansible-community/antsibull-docs). If you use either of these tools, please help us test this new release. It can be installed with `pip install -U antsibull-core==2.0.0a1`. Note that you'll need the latest version of antsibull and antsibull-docs to use antsibull-core 2.0.0a1.

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) shared

> antsibull-docs 1.8.0 ([changelog](https://github.com/ansible-community/antsibull-docs/blob/1.8.0/CHANGELOG.rst#v1-8-0)) has been released with several new features both for the Ansible docsite and for collection docsites.

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) said

> antsibull-core 1.5.0 ([changelog](https://github.com/ansible-community/antsibull-core/blob/stable-1/CHANGELOG.rst#v1-5-0)) has been released with a new feature for antsibull. (This new feature is also available in 2.0.0a1.)

### Ansible-Core [↗](https://github.com/ansible/ansible) ⚡️

The `ansible-core` package contains the base engine and a small subset of modules and plugins. To see what's planned for the next release, look at the [`ansible-core` roadmaps](https://docs.ansible.com/ansible-core/devel/roadmap/ansible_core_roadmap_index.html).

[cybette](https://matrix.to/#/@cybette:ansible.im) shared

> [ansible-core 2.14.1](https://groups.google.com/g/ansible-devel/c/AGqD9SR1D5I) and [2.13.7](https://groups.google.com/g/ansible-devel/c/hGR4LnAkeCw) have been relased. These are maintenance releases containing numerous bugfixes.

## DOCUMENTATION UPDATES 🔈️

[Don Naro](https://matrix.to/#/@orandon:ansible.im) contributed

> The `ansible/docsite` repo is now public, giving the Ansible community full access to all the html and navigation assets that go into `docs.ansible.com`. Fork [the repo](https://github.com/ansible/docsite) and start hacking.

[Don Naro](https://matrix.to/#/@orandon:ansible.im) shared

> We've updated the landing pages for `docs.ansible.com` to include an Ansible ecosystem page that organizes links to different projects. We've also refreshed some of the navigation and other pages to improve findability. Go visit https://docs.ansible.com/ and have a look. And remember the `ansible/docsite` repo is now public so you can send a PR with any improvements.

## COLLECTION UPDATES 🪄

[Yusuke Tsutsumi](https://matrix.to/#/@tsutsumiyusuke:matrix.org) shared

> The 1.1.0-beta of the [google.cloud collection](https://galaxy.ansible.com/google/cloud) is live on Ansible Galaxy! This is the first release to the google.cloud collection in over a year, and focuses primarily on compatibility fixes for ansible-core 2.13. Please give it a try and file any issues [on GitHub](https://github.com/ansible-collections/google.cloud).

[andersson007_](https://matrix.to/#/@andersson007_:matrix.org) shared

> The [grafana.grafana](https://galaxy.ansible.com/grafana/grafana) collection has been included in Ansible 7! Thanks to [mbialon](https://github.com/mbialon), [acozine](https://github.com/acozine), [felixfontein](https://github.com/felixfontein) for reviewing the inclusion request and collection maintainers for fast feedback!

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) said

> community.docker 3.3.0 ([changelog](https://github.com/ansible-collections/community.docker/blob/main/CHANGELOG.rst#v3-3-0)) has been released with new features and bugfixes. The docker_image module is now idempotent when archiving images, and current_container_facts works better with newer Docker versions and also tries to detect podman containers.

[rainerleber](https://matrix.to/#/@rainerleber:matrix.org) said

> community.sap_libs 1.4.0 ([changelog](https://github.com/sap-linuxlab/community.sap_libs/blob/main/CHANGELOG.rst)) has been released with new features and bugfixes. Note that the sap modules from community.general will be replaced by redirects to community.sap_libs in the next major release.

[itsbryantp](https://matrix.to/#/@itsbryantp:matrix.org) said

> The [ibm_zos_core 1.4.0 collection](https://ibm.github.io/z_ansible_collections_doc/ibm_zos_core/docs/source/release_notes.html#version-1-4-0) is now available on Ansible Galaxy and Automation Hub! This release contains many updates including a new zos_mount module, major enhancements to the zos_copy module, along with enhancements to several other modules. Check out [this blog](https://community.ibm.com/community/user/ibmz-and-linuxone/blogs/demetrios-dimatos1/2022/12/01/ibm-ansible-core-140-has-released?CommunityKey=ce54fe94-0145-4832-a0ef-4ea81d6062cc) for more details.

[betanummeric](https://matrix.to/#/@betanummeric:matrix.org) contributed

> The [community.postgresql](https://github.com/ansible-collections/community.postgresql) collection versions [1.7.7](https://github.com/ansible-collections/community.postgresql/blob/stable-1/CHANGELOG.rst) and [2.3.2](https://github.com/ansible-collections/community.postgresql/blob/main/CHANGELOG.rst) have been released.

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) shared

> community.routeros 2.5.0 ([changelog](https://github.com/ansible-collections/community.routeros/blob/main/CHANGELOG.rst#v2-5-0)) has been released with new features and a bugfix for the API modules.

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) said

> community.general 6.1.0 ([changelog](https://github.com/ansible-collections/community.general/blob/stable-6/CHANGELOG.rst#v6-1-0)) has been released with new features, bugfixes, and new modules. Note that the sap modules will be replaced by redirects to community.sap_libs in the next major release.

### Collection Removal

[mariolenz](https://matrix.to/#/@mariolenz:matrix.org) contributed

> The `cisco.nso` collection [is considered unmaintained](https://github.com/ansible-community/community-topics/issues/155) and will be removed from Ansible 9 if no one starts maintaining it again before Ansible 9. See [the removal process for details on how this works](https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst#cancelling-removal-of-an-unmaintained-collection).
> 
> Please note that you can still manually install the collection with `ansible-galaxy collection install cisco.nso` even when it has been removed from Ansible.

[mariolenz](https://matrix.to/#/@mariolenz:matrix.org) said

> It looks like the [community.skydive](https://github.com/ansible-collections/skydive) collection is effectively unmaintained. According to the current [community guidelines for collections](https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst#unmaintained-collections), we consider removing it in a future version of the Ansible community package. Please see [Unmaintained collection: community.skydive](https://github.com/ansible-community/community-topics/issues/171) for more information or to announce that you're interested in taking over the maintenance of (a fork of) `community.skydive`.
> 
> At least one month after this announcement appears here and in the [collection's issue tracker](https://github.com/ansible-collections/skydive/issues/24), the Ansible Community Steering Committee will vote on whether this collection is considered unmaintained and will be removed, or whether it will be kept. If it will be removed, this will happen earliest in Ansible 9.0.0. Please note that you can still manually install the collection with `ansible-galaxy collection install community.skydive` even when it has been removed from Ansible.

## PROJECT UPDATES 🛠️

[relrod](https://matrix.to/#/@relrod:matrix.org) said

> A [retry mechanism](https://github.com/ansible/receptor/pull/683) has been added to **Receptor**, to handle intermittent connection issues with Kubernetes logging stream. This fixes an issue where AWX jobs lasting longer than 4 hours would fail. Go try it out and let us know how it works!

[relrod](https://matrix.to/#/@relrod:matrix.org) contributed

> Want to learn more about **AWX** or share what you know with everyone else? We're looking for ideas for our [AWX Community YouTube channel](https://www.youtube.com/@ansible-awx), and help creating content! See [this issue](https://github.com/ansible/awx/issues/13242) for more!

[dmsimard](https://matrix.to/#/@dmsimard:matrix.org) said

> **ARA Records Ansible** 1.6.0 has been released and includes a bunch of improvements and new features to make playbooks easier to understand and troubleshoot! You can find the highlights from this release on [the blog](https://ara.recordsansible.org/blog/2022/12/05/announcing-the-release-of-ara-1.6.0/) and the full changelog is available on [GitHub](https://github.com/ansible-community/ara/releases/tag/1.6.0).
> 
> In the meantime, I am also taking this opportunity to mention that the project is moving its Twitter presence to Mastodon. You can follow [@ara@fosstodon.org](https://fosstodon.org/@ara) for updates and there's even an [RSS feed](https://fosstodon.org/@ara.rss)!

[Lila Yasin](https://matrix.to/#/@lyasin:matrix.org) contributed

> I am very excited to present my first blog post! **Project signing** is a new feature developed for Red Hat Ansible Automation Platform that came out in the latest 2.3 release. It enables users to sign project-based content (think playbooks, workflows, inventories, etc.) and verify whether or not that content has remained secure. It also features a new CLI tool, [ansible-sign](https://github.com/ansible/ansible-sign). This blog post will explain how it works, illustrate how to implement it, and highlight a few scenarios.  Check it out 👉️ [here](https://www.ansible.com/blog/project-signing-and-verification).

## PROJECT OFFICE HOURS 📅

[relrod](https://matrix.to/#/@relrod:matrix.org) shared

> Next **Ansible AWX Community Office Hours** meeting will be on **13 December, at 15UTC**! Join us to discuss and help shape the future of AWX! Agenda (and meeting link) is [here](https://github.com/ansible/awx/issues/13240).

[cmrussell99](https://matrix.to/#/@cmrussell99:matrix.org) contributed

> Greetings All! We are doing some Office Hours for **Event-Driven Ansible**. They are approximately monthly, and designed to answer your questions and get your thoughts and ideas. We share some tips and other useful information around the Event-Driven Ansible developer preview.  
> 
> The next one is **Wednesday, December 14th at 11AM ET**. You can sign up [here](https://www.redhat.com/en/events/webinar/event-driven-ansible-office-hours-december?extIdCarryOver=true&sc\_cid=701f2000001OH6uAAG) for December if you are interested in attending. 
> 
> In January, the Office Hours is planned for January 18th, with registration [here](https://www.redhat.com/en/events/webinar/event-driven-ansible-office-hours-january?extIdCarryOver=true&sc_cid=701f2000001OH6uAAG).
> 
> There is also a [replay of the November Office Hours](https://www.ansible.com/resources/webinars-training/event-driven-ansible-office-hours) which focused on Getting Started content, and you can listen at your convenience.

## PROPOSALS - DISCUSS AND VOTE! 🗳️

[mariolenz](https://matrix.to/#/@mariolenz:matrix.org) contributed

> Since the ansible-core team announced they will [skip the Dec 26/Jan 2 window](https://groups.google.com/g/ansible-devel/c/IQ7VPnw9yS8) due to the holiday season, it's a bit unclear what to do with the community package. There is an open [vote](https://github.com/ansible-community/community-topics/discussions/169) when to release 7.2.0 (**vote ends 2022-12-12**).

[gotmax (He/Him)](https://matrix.to/#/@gotmax:matrix.org) said

> As mentioned in [last week's Bullhorn issue](https://mailchi.mp/redhat/the-bullhorn-83), cyberark.pas is subject to removal from version 9 of the Ansible community package due to unresolved [Collection Requirements](https://github.com/ansible-collections/overview/blob/main/collection_requirements.rst) violations. A week has passed since the [community-topics issue](https://github.com/ansible-community/community-topics/issues/168) was filed and other SC members confirmed the violation, so a [vote](https://github.com/ansible-community/community-topics/discussions/172) has been started (**vote ends on 2022-12-16**).

## THAT'S ALL FOR NOW!

Have any questions you’d like to ask, or issues you’d like to see covered? Please ask in [#social:ansible.com](https://matrix.to/#/#social:ansible.com)! See you next time!
