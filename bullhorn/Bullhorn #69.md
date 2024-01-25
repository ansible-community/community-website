---
title: "Bullhorn #69"
date: 2022-08-09 14:45 UTC
tags: news
category: bullhorn
type: text
---

![Ansible Bullhorn banner](/images/bullhorn-banner-mango.png)

*A Newsletter for the Ansible Developer Community*
*Issue #69, 2022-08-08 ([Past Issues](https://us19.campaign-archive.com/home/?u=56d874e027110e35dea0e03c1&id=d6635f5420))*

Welcome to [The Bullhorn](https://github.com/ansible/community/wiki/News#the-bullhorn), our newsletter for the Ansible developer community. If you have any questions or content you’d like to share, you're welcome to chat with us in the [Ansible Social room on Matrix](https://matrix.to/#/#social:ansible.com), and mention [`newsbot`](https://matrix.to/#/@newsbot:ansible.im) to have your news item tagged for review for the next weekly issue!

<!-- TEASER_END -->

## KEY DATES ⏱️

[cybette](https://matrix.to/#/@cybette:ansible.im) said

> * 2022-08-09: [DaWGs meeting](https://github.com/ansible/community/issues/643), 15:00 UTC
> * 2022-08-10: [Community WG meeting](https://github.com/ansible/community/issues/645), 18:00 UTC (propose topics [here](https://github.com/ansible-community/community-topics/issues))
> * 2022-08-11: [Bullhorn #70 content deadline](https://github.com/ansible/community/wiki/News#the-bullhorn), 18:00 UTC
> * 2022-08-15: ETA for Ansible-Core 2.13.3 and Ansible-Core 2.12.8 releases
> * 2022-08-23: [ETA for Ansible 6.3.0 release](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_6.html)
> * 2022-10-17: [Ansible Contributor Summit 2022.10](https://ansiblecs202210.eventbrite.com/?aff=hackmd)
> * 2022-10-18/19: [AnsibleFest 2022](https://www.ansible.com/ansiblefest?sc_cid=7013a000002i5g3AAA)

## MAJOR NEW RELEASES 🏆️

[john-westcott-iv](https://matrix.to/#/@john-westcott-iv:ansible.im) contributed

> We're happy to announce that the next release of AWX, version 21.4.0 is now available!
> Some notable features include:
> * Bump Receptorctl to 1.2.3
> * Added forks to unified jobs table
> * Remove update_on_project_update
> * Adding fields to job_metadata for workflows and approval nodes
> * Adding subscriptions module and adding pool_id to license module
> * Adding remove_superuser and remove_system_auditors to the SAML user attribute map
> 
> In addition AWX Operator version 0.26.0 has also been released!
> Some notable features include:
> * Fix undefined limit key in installation config
> * Restore not managed external postgresql
> * Bump dependencies
> * Use new postgres pod label when migrating from old instance
> 
> Please see the releases pages for more details:
> AWX: [https://github.com/ansible/awx/releases/tag/21.4.0](https://github.com/ansible/awx/releases/tag/21.4.0)
> Operator: [https://github.com/ansible/awx-operator/releases/tag/0.26.0](https://github.com/ansible/awx-operator/releases/tag/0.26.0)
> 
> *Known Issues*:
> There is a known issue that the helm charts were not properly updated for Operator 0.26.0. See [https://github.com/ansible/awx-operator/issues/1011](https://github.com/ansible/awx-operator/issues/1011). Help wanted. Once this is resolved we will be making a new release of AWX Operator.

[ssbarnea](https://matrix.to/#/@ssbarnea:matrix.org) contributed

> ansible-lint 6.4.0 was released with lots of bugfixes and a new feature called "profiles", one that allow you to easily pick which set of rules you want to follow. https://github.com/ansible/ansible-lint/discussions/2254

### Antsibull [↗](https://github.com/ansible-community/antsibull) 🐂

Tooling for building the `Ansible` package and collection documentation.

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) shared

> antsibull 0.49.0 has been released ([changelog](https://github.com/ansible-community/antsibull/blob/0.49.0/CHANGELOG.rst#v0-49-0)). This bugfix and feature release contains a breaking change in the release role, and the repository now follows the [REUSE specification](https://reuse.software/spec/).

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) contributed

> antsibull-changelog 0.16.0 ([changelog](https://github.com/ansible-community/antsibull-changelog/blob/0.16.0/CHANGELOG.rst#v0-16-0)) has been released with improved support for standalone projects and support for newer rstcheck versions. It also mostly follows the [REUSE specification](https://reuse.software/spec/).

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) said

> antsibull-docs 1.2.0 ([changelog](https://github.com/ansible-community/antsibull-docs/blob/main/CHANGELOG.rst#v1-2-0)) has been released with some new features and bugfixes. Main news affect easier to use `seealso` support for plugins, and a way to check generated collection docs with rstcheck as part of the `lint-collection-docs` subcommand.

### Ansible [↗](https://github.com/ansible-collections) 📦️

The `Ansible` package includes `ansible-core` and is a batteries-included package that provides a curated set of Ansible collections. See the [Ansible roadmaps](https://docs.ansible.com/ansible/devel/roadmap/ansible_roadmap_index.html) for future release plans.

[ompragash](https://matrix.to/#/@ompragash:ansible.im) shared

> Ansible 6.2.0 is out!❤️
> 🔗https://groups.google.com/g/ansible-announce/c/gSJBtyyHLrk
> 
> 💽You can install it by running the following command or download the release tarball directly from [pypi](https://pypi.python.org/packages/source/a/ansible/ansible-6.2.0.tar.gz):
> 
> ```
> pip install ansible==6.2.0 --user
> ```
> 
> 🔆Try the all new `ansible-community` command-line utility added in Ansible 6 that prints the version of the Ansible Community package:
> 
> ```
> $ ansible-community --version
> Ansible community version 6.2.0
> ```
> 
> ➡️Check [Release Notes📦️🗒️](https://github.com/ansible-community/ansible-build-data/blob/main/6/CHANGELOG-v6.rst) and [Ansible 6 Porting Guide](https://docs.ansible.com/ansible/devel/porting_guides/porting_guide_6.html) for more details!

## COLLECTION UPDATES 🪄

### Collection Releases

[tremble](https://matrix.to/#/@mchappell:matrix.org) said

> [amazon.aws 4.1.0](https://github.com/ansible-collections/amazon.aws/tree/4.1.0) has been released with some new features, bugfixes, and deprecated features, [see changelog for details](https://github.com/ansible-collections/amazon.aws/blob/4.1.0/CHANGELOG.rst).
> 
> [amazon.aws 3.4.0](https://github.com/ansible-collections/amazon.aws/tree/3.4.0) has been released with some new bugfixes, [see changelog for details](https://github.com/ansible-collections/amazon.aws/blob/3.4.0/CHANGELOG.rst).

[csmart](https://matrix.to/#/@csmart:matrix.org) contributed

> community.libvirt collection version 1.2.0 has been released, containing some bug fixes and expanded dynamic inventory which returns more guest information.

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) shared

> community.general 5.4.0 ([changelog](https://github.com/ansible-collections/community.general/blob/stable-5/CHANGELOG.rst#v5-4-0)) has been released with new plugins, modules, features, and bugfixes.

[Qalthos](https://matrix.to/#/@qalthos:ansible.im) contributed

> There have been a few networking releases this week:
> * [ansible.netcommon 3.1.0](https://github.com/ansible-collections/ansible.netcommon/tree/3.1.0) has been released with new features ([changelog](https://github.com/ansible-collections/ansible.netcommon/blob/3.1.0/CHANGELOG.rst))
> * [cisco.ios 3.3.0](https://github.com/ansible-collections/cisco.ios/tree/3.3.0) has been released with new features ([changelog](https://github.com/ansible-collections/cisco.ios/blob/3.3.0/CHANGELOG.rst))
> * [cisco.iosxr 3.3.0](https://github.com/ansible-collections/cisco.iosxr/tree/3.3.0) has been released with new features ([changelog](https://github.com/ansible-collections/cisco.iosxr/blob/3.3.0/CHANGELOG.rst))

[tremble](https://matrix.to/#/@mchappell:matrix.org) shared

> [community.aws 3.5.0](https://github.com/ansible-collections/community.aws/tree/3.5.0) has been released with various bugfixes, [see changelog for details](https://github.com/ansible-collections/community.aws/blob/3.5.0/CHANGELOG.rst).
> 
> [community.aws 4.1.1](https://github.com/ansible-collections/community.aws/tree/4.1.1) has been released with some new features, bugfixes, and deprecated features, [see changelog for details](https://github.com/ansible-collections/community.aws/blob/4.1.1/CHANGELOG.rst).

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) contributed

> community.docker 3.0.0-rc1 ([changelog](https://github.com/ansible-collections/community.docker/blob/main/CHANGELOG.rst#v3-0-0-rc1)) has been released. If no further bugs are reported, the final 3.0.0 release will appear in around two weeks. This release features a complete rewrite of docker_container, and most modules and plugins no longer need the Docker SDK for Python (except the ones for managing Docker Swarm).

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) said

> community.routeros 2.2.0 ([changelog](https://github.com/ansible-collections/community.routeros/blob/main/CHANGELOG.rst#v220)) has been released. It contains two new modules, `community.routeros.api_info` and `community.routeros.api_modify`, which allow to modify certain paths in a more Ansible-like fashion using the RouterOS API.

[laurent-indermuehle](https://matrix.to/#/@laurent-indermuehle:matrix.org) said

> The community.mysql collection versions [1.4.8](https://github.com/ansible-collections/community.mysql/blob/stable-1/CHANGELOG.rst), [2.3.9](https://github.com/ansible-collections/community.mysql/blob/stable-2/CHANGELOG.rst) and [3.4.0](https://github.com/ansible-collections/community.mysql/blob/main/CHANGELOG.rst) have been released.

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) shared

> community.azure 2.0.0 has been released. It is an empty shell containing tombstones for all modules contained in the previous versions. If you are still using community.azure, please migrate to azure.azcollection.

[betanummeric](https://matrix.to/#/@betanummeric:matrix.org) contributed

> The [community.postgresql](https://github.com/ansible-collections/community.postgresql) collection versions [1.7.5](https://github.com/ansible-collections/community.postgresql/blob/stable-1/CHANGELOG.rst) and [2.2.0](https://github.com/ansible-collections/community.postgresql/blob/main/CHANGELOG.rst) have been released.

### Collection Inclusion

[andersson007_](https://matrix.to/#/@andersson007_:matrix.org) said

> We are happy to announce that the [ibm.spectrum_virtualize](https://galaxy.ansible.com/ibm/spectrum_virtualize) collection has been included in the ansible community package. Thanks to everyone who helped review the collection and thanks to the maintainers for submitting the collection and making it satisfy the [Collection requirements](https://github.com/ansible-collections/overview/blob/main/collection_checklist.md)!

### Collection Removal

[mariolenz](https://matrix.to/#/@mariolenz:matrix.org) shared

> The google.cloud collection [is considered unmaintained](https://github.com/ansible-community/community-topics/issues/105) and will be removed from Ansible 8 if no one starts maintaining it again before Ansible 8. See [the removal process for details on how this works](https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst#cancelling-removal-of-an-unmaintained-collection).

## HELP WANTED 🙏

[andersson007_](https://matrix.to/#/@andersson007_:matrix.org) shared

> The following collection inclusion requests are waiting for your review:
> 
> * [inspur.ispim](https://github.com/ansible-collections/ansible-inclusion/discussions/47)
> * [lowlydba.sqlserver](https://github.com/ansible-collections/ansible-inclusion/discussions/51)
> 
> See the [process description](https://github.com/ansible-collections/ansible-inclusion#review-process) to learn how to do it.
> 
> Please help the community extend the Ansible package!

## COMMUNITY UPDATES 👂️

### Maintainers [↗](https://github.com/ansible-community) 🪜

Maintainers help to run the community!

[andersson007_](https://matrix.to/#/@andersson007_:matrix.org) contributed

> We are happy to announce a new maintainer of the [community.zabbix](https://github.com/ansible-collections/community.zabbix) collection - Michal Hybner ([mu1f407](https://github.com/mu1f407) on GitHub)! Thank you, Michal, for your great contribution and desire to help with the collection!

[andersson007_](https://matrix.to/#/@andersson007_:matrix.org) said

> We are happy to welcome several new maintainers in the [community.zabbix](https://github.com/ansible-collections/community.zabbix) collection: [pyrodie18](https://github.com/pyrodie18), [BGmot](https://github.com/BGmot) and [lzadjsf](https://github.com/lzadjsf). Thank you, folks, for your interest and desire to help! Many thanks to [D3DeFi](https://github.com/D3DeFi), one of the current collection maintainers, for promoting them!

[andersson007_](https://matrix.to/#/@andersson007_:matrix.org) shared

> We are also happy to announce a new maintainer of the [community.postgresql](https://github.com/ansible-collections/community.postgresql) collection - Felix Hamme ([betanummeric](https://github.com/betanummeric) on GitHub)! Our congratulations, Felix, and thank you for your great contribution in many collections and desire to help!

[andersson007_](https://matrix.to/#/@andersson007_:matrix.org) said

> We are happy to announce that the [community.mysql](https://github.com/ansible-collections/community.mysql) collection has found a new maintainer - Laurent Indermühle ([laurent-indermuehle](https://github.com/laurent-indermuehle) on GitHub). Our congratulations, Laurent, and thank you for your great contribution!

Thanks and congratulations to all! 👏🎉

## THAT'S ALL FOR NOW!

Have any questions you’d like to ask, or issues you’d like to see covered? Please ask in [#social:ansible.com](https://matrix.to/#/#social:ansible.com)! See you next time!
