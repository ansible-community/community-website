---
title: "Bullhorn #78"
date: 2022-10-14 00:11 UTC
tags: news
category: bullhorn
type: text
---

![Ansible Bullhorn banner](/images/bullhorn-banner-mango.png)

*A Newsletter for the Ansible Developer Community*
*Issue #78, 2022-10-13 ([Past Issues](https://us19.campaign-archive.com/home/?u=56d874e027110e35dea0e03c1&id=d6635f5420))*

Welcome to [The Bullhorn](https://github.com/ansible/community/wiki/News#the-bullhorn), our newsletter for the Ansible developer community. If you have any questions or content you’d like to share, you're welcome to chat with us in the [Ansible Social room on Matrix](https://matrix.to/#/#social:ansible.com), and mention [`newsbot`](https://matrix.to/#/@newsbot:ansible.im) to have your news item tagged for review for the next weekly issue!

<!-- TEASER_END -->

## KEY DATES ⏱️

[cybette](https://matrix.to/#/@cybette:ansible.im) contributed

> * **2022-10-17: [Ansible Contributor Summit 2022.10](https://hackmd.io/@ansible-community/contrib-summit-202210)**
> * 2022-10-17: [Ansible-core 2.14 release candidate 1](https://docs.ansible.com/ansible-core/devel/roadmap/ROADMAP_2_14.html)
> * **2022-10-18/19: [AnsibleFest 2022](https://www.ansible.com/ansiblefest?sc_cid=7013a000002i5g3AAA)**
> * 2022-10-18: [DaWGs meeting](https://github.com/ansible/community/issues/643), 15:00 UTC
> * 2022-10-19: [Community WG meeting](https://github.com/ansible/community/issues/645), 18:00 UTC (propose topics [here](https://github.com/ansible-community/community-topics/issues))
> * 2022-10-25: [ETA for Ansible 6.6.0 release](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_6.html)
> * 2022-10-26: [Community WG meeting](https://github.com/ansible/community/issues/645), 18:00 UTC ([topic: Decide what contingencies to activate for any blockers that do not meet the deadline](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_7.html))
> * 2022-10-27: [Bullhorn #79 content deadline](https://github.com/ansible/community/wiki/News#the-bullhorn), 18:00 UTC
> * 2022-11-07: ETA for Ansible-Core 2.13.6 and Ansible-Core 2.12.11 releases (if those releases have updates)
> * 2022-11-07: [Ansible-core 2.14 GA](https://docs.ansible.com/ansible-core/devel/roadmap/ROADMAP_2_14.html)
> * 2022-11-07: [Last day for collections to make backwards incompatible releases that will be accepted into Ansible-7](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_7.html)

## ANSIBLEFEST AND CONTRIBUTOR SUMMIT!!

> It's almost time for the automation experience of the year - **AnsibleFest 2022** and **Ansible Contributor Summit 2022.10** are happening next week in Chicago!
> 
> On October 17, we start off the week with the Contributor Summit. For those attending (both online and in-person), please bookmark the main [Contributor Summit HackMD](https://hackmd.io/@ansible-community/contrib-summit-202210) so you can have the latest event info and updates at your fingertips. Check out the [agenda](https://hackmd.io/@ansible-community/contrib-summit-202210/%2FIJ2KL2KQQv-cR5fGSOwiVg) and details about [each session](https://hackmd.io/@ansible-community/contrib-summit-202210/%2FIJ2KL2KQQv-cR5fGSOwiVg%23Session-Notes) beforehand so you come prepared to participate and engage in these sessions!
> 
> On October 18 & 19, join us at [AnsibleFest](https://www.ansible.com/ansiblefest?sc_cid=7013a000002i5g3AAA) and immerse yourself in the movement that has made Ansible an industry-leading automation technology. Find out [what the two days have to offer](https://www.ansible.com/blog/the-automation-experience-ansiblefest-2022), and have a look at some things to [know before you go](https://www.redhat.com/en/blog/ansiblefest-2022-know-you-go).
> 
> *(The Bullhorn will also pause its release for a week and return in two weeks!)*

## GENERAL NEWS UPDATES 🔈️

[ompragash](https://matrix.to/#/@ompragash:ansible.im) shared

> _**AWX Operator**_ found a new home in [OperatorHub.io](https://operatorhub.io/operator/awx-operator)!❤️🎉
> 
> 💽Starting from AWX Operator v0.30.0, it’s easier to install AWX on your cluster directly from OperatorHub.io with the below command:
> 
> ```
> kubectl create -f https://operatorhub.io/install/awx-operator.yaml
> ```
> 
> 🔆 Check [How to install an Operator from OperatorHub.io](https://operatorhub.io/how-to-install-an-operator) for more details!
> 
> 🕵️ If you run into installation issues or technical errors, kindly report it on the ansible/awx-operator repo [here](https://github.com/ansible/awx-operator/issues/new/choose) or reach out to us on Matrix: [#awx:ansible.com](https://docs.ansible.com/ansible/latest/community/communication.html#ansible-community-on-matrix) | IRC: [#ansible-awx](https://docs.ansible.com/ansible/latest/community/communication.html#ansible-community-on-irc)

[andersson007_](https://matrix.to/#/@andersson007_:matrix.org) shared

> We are happy to announce that Maxwell G (aka [gotmax23](https://github.com/gotmax23) on GitHub, gotmax on Matrix) has joined the [Steering Committee](https://docs.ansible.com/ansible/devel/community/steering/community_steering_committee.html).
> 
> Thank you, Maxwell, for your contributions to the Community and the Project! It's a great honor for us to have you on board!

## MAJOR NEW RELEASES 🏆️

### Ansible [↗](https://github.com/ansible-collections) 📦️

The `Ansible` package includes `ansible-core` and is a batteries-included package that provides a curated set of Ansible collections. See the [Ansible roadmaps](https://docs.ansible.com/ansible/devel/roadmap/ansible_roadmap_index.html) for future release plans.

[chadams](https://matrix.to/#/@chadams:ansible.im) contributed

> Ansible 6.5.0 is out! ❤️
> 🔗[https://groups.google.com/g/ansible-announce/c/awqMFstEArk](https://groups.google.com/g/ansible-announce/c/awqMFstEArk)
> 
> 💽You can install it by running the following command or download the release tarball directly from [pypi](https://pypi.python.org/packages/source/a/ansible/ansible-6.5.0.tar.gz):
> 
> ```
> pip install ansible==6.5.0 --user
> ```
> 
> 🔆Try the all new `ansible-community` command-line utility added in Ansible 6 that allows to print the version of the Ansible Community package:
> 
> ```
> $ ansible-community --version
> Ansible community version 6.5.0
> ```
> 
> ➡️ Check [Release Notes📦️🗒️](https://github.com/ansible-community/ansible-build-data/blob/main/6/CHANGELOG-v6.rst) and [Ansible 6 Porting Guide](https://docs.ansible.com/ansible/devel/porting_guides/porting_guide_6.html) for more details!

### Ansible-Core [↗](https://github.com/ansible/ansible) ⚡️

The `ansible-core` package contains the base engine and a small subset of modules and plugins. To see what's planned for the next release, look at the [`ansible-core` roadmaps](https://docs.ansible.com/ansible-core/devel/roadmap/ansible_core_roadmap_index.html).

[cybette](https://matrix.to/#/@cybette:ansible.im) shared

> [ansible-core 2.14.0b3 (3rd beta)](https://groups.google.com/g/ansible-devel/c/s2EwCSbS_hM) has been released. Subject to the need for additional beta releases, the first release candidate is scheduled for 2022-10-17.
> 
> [ansible-core 2.13.5 and ansible-core 2.12.10](https://groups.google.com/g/ansible-devel/c/k6FX5XNH9ww) have been released. These are maintenance releases containing numerous bugfixes.

## COLLECTION UPDATES 🪄

[mariolenz](https://matrix.to/#/@mariolenz:matrix.org) contributed

> The `mellanox.onyx` collection [is considered unmaintained](https://github.com/ansible-community/community-topics/issues/136) and will be removed from Ansible 8 if no one starts maintaining it again before Ansible 8. See [the removal process for details on how this works](https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst#cancelling-removal-of-an-unmaintained-collection).

## HELP WANTED 🙏

[andersson007_](https://matrix.to/#/@andersson007_:matrix.org) shared

> The following collection inclusion requests are waiting for your review:
> 
> * [dellemc.unity](https://github.com/ansible-collections/ansible-inclusion/discussions/32)
> * [grafana.grafana](https://github.com/ansible-collections/ansible-inclusion/discussions/52)
> 
> See the [process description](https://github.com/ansible-collections/ansible-inclusion#review-process) to learn how to do it.
> 
> If you have any questions, just ping `andersson007` on [Matrix](https://docs.ansible.com/ansible/devel/community/communication.html#ansible-community-on-matrix) in the [#community:ansible.com](https://matrix.to/#/#community:ansible.com) room or on [Libera.Chat IRC](https://docs.ansible.com/ansible/devel/community/communication.html#ansible-community-on-irc) in the `#ansible-community` channel or directly.
> 
> Please help the community extend the Ansible package!

## PROPOSALS - DISCUSS AND VOTE! 🗳️

[rrey](https://matrix.to/#/@rrey:matrix.org) said

> The [Ansible Collection Grafana](https://github.com/ansible-collections/community.grafana) has started a [discussion on Github](https://github.com/ansible-collections/community.grafana/discussions/278) around the possibility to merge with the recently created [collection for Grafana Cloud](https://github.com/grafana/grafana-ansible-collection) (by Grafana Labs).
> 
> If you are using the collection, we would like to have your feedback!

## COMMUNITY UPDATES 👂️

[briantist](https://matrix.to/#/@briantist:libera.chat) shared

> `galactory` (the Ansible Galaxy proxy for Artifactory) has [released version `0.6.0`](https://github.com/briantist/galactory/releases/tag/v0.6.0) [[changelog](https://github.com/briantist/galactory/blob/main/CHANGELOG.rst#v0-6-0)] adding the ability to prevent anonymous collection uploads while retaining upstream proxy caching.

[briantist](https://matrix.to/#/@briantist:libera.chat) shared

> `galactory` has [released version `0.7.0`](https://github.com/briantist/galactory/releases/tag/v0.7.0) [[changelog](https://github.com/briantist/galactory/blob/main/CHANGELOG.rst#v0-7-0)] with a potentially breaking change to how properties are set. Some incorrectly configured reverse proxies break with the new method. A new option is available to fall back to the previous method, which requires a Pro license.

## THAT'S ALL FOR NOW!

Have any questions you’d like to ask, or issues you’d like to see covered? Please ask in [#social:ansible.com](https://matrix.to/#/#social:ansible.com)! See you next time!
