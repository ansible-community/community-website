---
title: "Bullhorn #79"
date: 2022-10-28 22:10 UTC
tags: news
category: bullhorn
type: text
---

![Ansible Bullhorn banner](/images/bullhorn-banner-mango.png)

*A Newsletter for the Ansible Developer Community*
*Issue #79, 2022-10-28 ([Past Issues](https://us19.campaign-archive.com/home/?u=56d874e027110e35dea0e03c1&id=d6635f5420))*

Welcome to [The Bullhorn](https://github.com/ansible/community/wiki/News#the-bullhorn), our newsletter for the Ansible developer community. If you have any questions or content you’d like to share, you're welcome to chat with us in the [Ansible Social room on Matrix](https://matrix.to/#/#social:ansible.com), and mention [`newsbot`](https://matrix.to/#/@newsbot:ansible.im) to have your news item tagged for review for the next weekly issue!

<!-- TEASER_END -->

## KEY DATES ⏱️

[cybette](https://matrix.to/#/@cybette:ansible.im) shared

> * 2022-11-01: [DaWGs meeting](https://github.com/ansible/community/issues/643), 15:00 UTC
> * 2022-11-02: [Community WG meeting](https://github.com/ansible/community/issues/645), 18:00 UTC (propose topics [here](https://github.com/ansible-community/community-topics/issues))
> * 2022-11-03: [Bullhorn #80 content deadline](https://github.com/ansible/community/wiki/News#the-bullhorn), 18:00 UTC
> * 2022-11-07: ETA for Ansible-Core 2.13.6 and Ansible-Core 2.12.11 releases (if those releases have updates)
> * 2022-11-07: [Ansible-core 2.14 GA](https://docs.ansible.com/ansible-core/devel/roadmap/ROADMAP_2_14.html)
> * 2022-11-07: [Last day for collections to make backwards incompatible releases that will be accepted into Ansible-7](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_7.html)
> * 2022-11-08: [Ansible 7.0.0 beta1 – feature freeze](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_7.html)

## GENERAL NEWS UPDATES 🔈️

[gotmax (He/Him)](https://matrix.to/#/@gotmax:matrix.org) said

> The Ansible Community Steering Committee [has approved](https://github.com/ansible-community/community-topics/discussions/153) [a change](https://github.com/ansible-collections/overview/commit/6dbb5037c09dce9324cb39e322be2f42e068f117) to the [Collection Requirements](https://github.com/ansible-collections/overview/blob/main/collection_requirements.rst) re. SCM and release requirements. Collections were always required to tag releases, but we have clarified what `tagging` actually means. We have also explicitly stated that "collection artifacts released to Galaxy MUST be built from the sources that are tagged in the collection's git repository as that release." Please see the [full change](https://github.com/ansible-collections/overview/commit/6dbb5037c09dce9324cb39e322be2f42e068f117) for more information.

[samccann](https://matrix.to/#/@samccann:ansible.im) contributed

> Ansible 2.3 documentation will redirect to /latest/ docs in a week. If you need 2.3 documentation, use the archive site at https://docs.ansible.com/ansible-prior-versions.html to access these docs.

## MAJOR NEW RELEASES 🏆️

### Ansible [↗](https://github.com/ansible-collections) 📦️

The `Ansible` package includes `ansible-core` and is a batteries-included package that provides a curated set of Ansible collections. See the [Ansible roadmaps](https://docs.ansible.com/ansible/devel/roadmap/ansible_roadmap_index.html) for future release plans.

[chadams](https://matrix.to/#/@chadams:ansible.im) contributed

> Ansible 7.0.0a2 is out! ❤️
> 🔗[https://groups.google.com/g/ansible-announce/c/EI8cOKdBAxQ](https://groups.google.com/g/ansible-announce/c/EI8cOKdBAxQ)
> 💽You can install it by running the following command or download the release tarball directly from [pypi](https://pypi.python.org/packages/source/a/ansible/ansible-7.0.0a2.tar.gz):
> 
> ```
> pip install ansible==7.0.0a2 --user
> ```
> 
> ```
> $ ansible-community --version
> Ansible community version 7.0.0a2
> ```
> 
> ➡️ Check [Release Notes📦️🗒️](https://github.com/ansible-community/ansible-build-data/blob/main/7/CHANGELOG-v7.rst) and [Ansible 7 Porting Guide](https://docs.ansible.com/ansible/devel/porting_guides/porting_guide_7.html) for more details!

### Ansible-Core [↗](https://github.com/ansible/ansible) ⚡️

The `ansible-core` package contains the base engine and a small subset of modules and plugins. To see what's planned for the next release, look at the [`ansible-core` roadmaps](https://docs.ansible.com/ansible-core/devel/roadmap/ansible_core_roadmap_index.html).

[sivel](https://github.com/sivel) shared

> [New release candidates: ansible-core 2.14.0rc1 - C'mon Everybody](https://groups.google.com/g/ansible-devel/c/3zntv1e7OGQ) - this release candidate will become general availability release on 7 November 2022.

## COLLECTION UPDATES 🪄

[andersson007_](https://matrix.to/#/@andersson007_:matrix.org) said

> The [lowlydba.sqlserver](https://galaxy.ansible.com/lowlydba/sqlserver) collection has passed the [Collection inclusion procedure](https://github.com/ansible-collections/ansible-inclusion/blob/main/README.md) and will be included in the next minor release of Ansible. Thanks to [lowlydba](https://github.com/lowlydba) and [briantist](https://github.com/briantist) for the contribution!

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) shared

> community.general 5.8.0 ([changelog](https://github.com/ansible-collections/community.general/blob/stable-5/CHANGELOG.rst#v5-8-0)) has been released with new features and bugfixes. This is the last 5.x.0 minor release, from now on there will only be bugfix releases 5.8.x. The next minor/major release of the collection will be version 6.0.0 on November 7th.

[itsbryantp](https://matrix.to/#/@itsbryantp:matrix.org) shared

> The [ibm.ds8000 v1.1.0 collection](https://galaxy.ansible.com/ibm/ds8000) is now available on Ansible Galaxy! This release adds new support to handle more mainframe oriented use cases such as managing LSS volumes and CKD alias volumes. Check out the following [blog](https://community.ibm.com/community/user/storage/blogs/randy-blea1/2022/09/30/automate-your-mainframe-with-ansible-using-ibmds80) for more information.

[itsbryantp](https://matrix.to/#/@itsbryantp:matrix.org) said

> The first release of the [ibm.csm v1.0.0 collection](https://galaxy.ansible.com/ibm/csm) is now available on Ansible Galaxy! The IBM Copy Services Manager collection provides modules for managing your CSM servers and sessions. Learn more in the following [blog](https://community.ibm.com/community/user/storage/blogs/randy-blea1/2022/09/30/automate-your-mainframe-with-ansible-using-ibmds80).

[itsbryantp](https://matrix.to/#/@itsbryantp:matrix.org) shared

> The ibm_zos_core collection 1.3.6 is available on [Ansible Galaxy](https://galaxy.ansible.com/ibm/ibm_zos_core) and Automation Hub! This release includes several bug fixes and support for `ansible-core` 2.11. See the [release notes](https://ibm.github.io/z_ansible_collections_doc/ibm_zos_core/docs/source/release_notes.html#version-1-3-6) for the full list of updates.

[itsbryantp](https://matrix.to/#/@itsbryantp:matrix.org) shared

> The [ibm_zos_core 1.4.0-beta.2 collection](https://galaxy.ansible.com/ibm/ibm_zos_core) is now available on Ansible Galaxy! This release includes several bug fixes, support for `ansible-core` 2.11, and significant architecture changes to the `zos_copy` module. See the [release notes](https://ibm.github.io/z_ansible_collections_doc/ibm_zos_core/docs/source/release_notes.html#version-1-4-0-beta-2) for more details.

[Sagar Paul](https://matrix.to/#/@sagpaul:matrix.org) said

> We had a major release for the following network collections
> 
> * ansible.netcommon     4.0.0
> 
>     - Modules deprecated
> 
>         - napalm
>         - net\_banner
>         - net\_interface
>         - net\_l2\_interface
>         - net\_l3\_interface
>         - net\_linkagg
>         - net\_lldp
>         - net\_lldp\_interface
>         - net\_logging
>         - net\_static\_route
>         - net\_system
>         - net\_user
>         - net\_vlan
>         - net\_vrf
> 
> * cisco.iosxr           4.0.0
> 
>     - Modules deprecated -
> 
>         - iosxr\_interface
> 
> * arista.eos            6.0.0
> 
>     - Modules deprecated -
> 
>         - eos\_interface
>         - eos\_l2\_interface
>         - eos\_l3\_interface
>         - eos\_linkagg
>         - eos\_static\_route
>         - eos\_vlan
> 
> * cisco.nxos            4.0.0
> 
>     - Modules deprecated -
> 
>         - nxos\_acl
>         - nxos\_acl\_interface
>         - nxos\_interface
>         - nxos\_interface\_ospf
>         - nxos\_l2\_interface
>         - nxos\_l3\_interface
>         - nxos\_linkagg
>         - nxos\_lldp
>         - nxos\_ospf
>         - nxos\_ospf\_vrf
>         - nxos\_smu
>         - nxos\_static\_route
>         - nxos\_vlan
> 
> * cisco.ios             4.0.0
> 
>     - Modules deprecated -
> 
>         - ios\_interface
>         - ios\_l2\_interface
>         - ios\_l3\_interface
>         - ios\_static\_route
>         - ios\_vlan
> 
> * cisco.asa             4.0.0
> 
>     - Modules deprecated -
> 
>         - asa\_acl
>         - asa\_og
> 
> * vyos.vyos             4.0.0
> 
>     - Modules deprecated -
> 
>         - vyos\_interface
>         - vyos\_l3\_interface
>         - vyos\_linkagg
>         - vyos\_lldp
>         - vyos\_lldp\_interface
>         - vyos\_static\_route
> 
> * junipernetworks.junos 4.0.0
> 
>     - Modules deprecated -
> 
>         - junos\_interface
>         - junos\_l2\_interface
>         - junos\_l3\_interface
>         - junos\_linkagg
>         - junos\_lldp
>         - junos\_lldp\_interface
>         - junos\_static\_route
>         - junos\_vlan 
> 
> * This release also drops support for `connection: local` and provider dictionary.

[abuzachis](https://matrix.to/#/@aevelina:ansible.im) contributed

> [amazon.aws 5.1.0](https://github.com/ansible-collections/amazon.aws/blob/stable-5/CHANGELOG.rst#v5-1-0) has been released with some minor changes, bugfixes, security fixes and deprecated features.

[mariolenz](https://matrix.to/#/@mariolenz:matrix.org) contributed

> It looks like the [cisco.nso](https://github.com/CiscoDevNet/ansible-nso) collection is effectively unmaintained. According to the current [community guidelines for collections](https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst#unmaintained-collections), we consider removing it in a future version of the Ansible community package. Please see [Unmaintained collection: cisco.nso](https://github.com/ansible-community/community-topics/issues/155) for more information or to announce that you’re interested in taking over the maintenance of (a fork of) `cisco.nso`.
> 
> At least one month after this announcement appears here and in the [collection’s issue tracker](https://github.com/CiscoDevNet/ansible-nso/issues/10), the Ansible Community Steering Committee will vote on whether this collection is considered unmaintained and will be removed, or whether it will be kept. If it will be removed, this will happen earliest in Ansible 9.0.0. Please note that you can still manually install the collection with `ansible-galaxy collection install cisco.nso` even when it has been removed from Ansible.

## HELP WANTED 🙏

[Don Naro](https://matrix.to/#/@orandon:ansible.im) contributed

> We're looking to start a DaWGs Open Hour in EMEA to discuss all aspects of Ansible community documentation. Contributors and interested parties can fill in this short survey to indicate their time preference and submit discussion topics: https://www.surveymonkey.com/r/NKTKV6W

[andersson007_](https://matrix.to/#/@andersson007_:matrix.org) said

> The following collection inclusion requests are waiting for your review:
> 
> * [dellemc.unity](https://github.com/ansible-collections/ansible-inclusion/discussions/32)
> 
> See the [process description](https://github.com/ansible-collections/ansible-inclusion#review-process) to learn how to do it.
> 
> If you have any questions, just ping `andersson007` on [Matrix](https://docs.ansible.com/ansible/devel/community/communication.html#ansible-community-on-matrix) in the [#community:ansible.com](https://matrix.to/#/#community:ansible.com) room or on [Libera.Chat IRC](https://docs.ansible.com/ansible/devel/community/communication.html#ansible-community-on-irc) in the `#ansible-community` channel or directly.
> 
> Please help the community extend the Ansible package!

## PROPOSALS - DISCUSS AND VOTE! 🗳️

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) said

> There is a [discussion](https://github.com/ansible-community/community-topics/issues/151) and [a community vote](https://github.com/ansible-community/community-topics/discussions/157) on a concrete proposal to adjust the release cadence of Ansible 7 to couple it more closely to ansible-core releases. The basic idea is to release Ansible 1-2 days after ansible-core is released. For Ansible 7.0.0, the idea is to release it two weeks after ansible-core 2.14.0 if no major issue is found, so we have time for one beta release (directly after 2.14.0) and one release candidate (one week after 2.14.0). See the discussion and [the summary in the vote](https://github.com/ansible-community/community-topics/discussions/157#discussion-4512394) for details.

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) shared

> There is a [discussion in community-topics](https://github.com/ansible-community/community-topics/issues/154) on how to mark private plugins in a collection. One proposal is to use a leading underscore in the plugin name to indicate private (outside ansible.builtin, there it means deprecated). One potential problem is that this notation was used by some tools as a deprecation mark before, though this use was very inconsistent. If you have any ideas, are involved in projects that would be affected by this, or just interested in the topic in general, please take a look and participate in the discussion!

## COMMUNITY UPDATES 👂️

[maxamillion](https://matrix.to/#/@maxamillion:one.ems.host) said

> ### Ansible Edge Working Group
> 
> This is a brand new working group focusing on bringing Ansible Automation to Edge Computing!
> 
> We had the good fortune of initially launching during Ansible Contributor Summit, and we were represented in the Day 2 Keynote on the AnsibleFest main-stage.
> 
> Please come learn a little about the [Edge Working Group](https://github.com/ansible/community/wiki/Edge-Automation) and join us in our [#edge:ansible.com](https://matrix.to/#/#edge:ansible.com) Matrix room (bridged to `#ansible-edge` on irc.libera.chat).

[Gwmngilfen](https://matrix.to/#/@gwmngilfen:ansible.im) contributed

> During the fun of AnsibleFest, cybette and maxamillion had a chance to sit with theCUBE and do an interview on the Ansible community, Contributor Summit, Matrix, Hacktoberfest and more. [Give it a watch!](https://www.thecube.net/events/red-hat/ansiblefest-2022/content/Videos/0e8cec23-d195-4692-8a98-c9a8e2dee7b4)

[gotmax (He/Him)](https://matrix.to/#/@gotmax:matrix.org) contributed

> Join us in #ansible-packaging (Libera.chat) / [#packaging:ansible.com](https://matrix.to/#/#packaging:ansible.com) (Matrix) to discuss packaging of projects in the Ansible ecosystem, whether it's ansible-core, collections, or ARA. Linux distribution package maintainers and anyone else interested in Ansible packaging is welcome. Currently, we have packagers from Void Linux, CentOS, Fedora, and EPEL, and we'd love to have more!

[gotmax (He/Him)](https://matrix.to/#/@gotmax:matrix.org) said

> In addition to the ansible community package and ansible-core, we have packaged almost 20 standalone collections in Fedora, many of which are also packaged for EPEL! We already have a good number of packaged collections, so I figured it was time to write up some formal guidelines. I have submitted [draft Ansible Collection Guidelines](https://pagure.io/packaging-committee/pull-request/1201) to the Fedora Packaging Committee for inclusion in the official [Fedora Packaging Guidelines site](https://docs.fedoraproject.org/en-US/packaging-guidelines/). These guidelines outline the best practices for packaging Ansible Collections in Fedora and how to use the ansible-packaging RPM macros. There's already a few people involved, but we'd love to have others. Anyone interested in how they can get involved or who have any other questions, comments, or feedback should join #ansible-packaging (Libera.chat) / [#packaging:ansible.com](https://matrix.to/#/#packaging:ansible.com) (Matrix).

## COMMUNITY EVENTS AND MEETUPS 📅

If you've missed out on some of the AnsibleFest action last week, fear not! You can view the keynotes from [day 1](https://www.youtube.com/watch?v=J7YRaPzKw4A) and [day 2](https://www.youtube.com/watch?v=0tHRrMjBxIM), as well as access a wealth of on-demand sessions in the [AnsibleFest Content Hub](https://www.redhat.com/en/blog/check-out-ansiblefest-content-hub-now). In addition, check out the [Best of Fest 2022](https://www.ansible.com/blog/best-of-fest-2022) along with [AnsibleFest 2022 Newsroom](https://www.redhat.com/en/about/ansiblefest-newsroom) for more updates.

We will also share a recap of the Ansible Contributor Summit, along with the Contributor Survey, in the next issue of The Bullhorn. Stay tuned!

In the meantime, there are some local Ansible meetup events happening! [Ansible Toronto](https://www.meetup.com/ansible-toronto/) will be doing an [AnsibleFest Recap](https://www.meetup.com/ansible-toronto/events/289072255/), while [Ansible Atlanta](https://www.meetup.com/ansible-atlanta/) will be talking about [Execution Environments, from dev to prod](https://www.meetup.com/ansible-atlanta/events/289115928/). Check out the details in the links and RSVP!

## THAT'S ALL FOR NOW!

Have any questions you’d like to ask, or issues you’d like to see covered? Please ask in [#social:ansible.com](https://matrix.to/#/#social:ansible.com)! See you next time!
