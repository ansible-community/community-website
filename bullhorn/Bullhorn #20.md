---
title: "Bullhorn #20"
date: 2021-02-18 21:00 UTC
tags: news
category: bullhorn
type: text
---

![Ansible Bullhorn banner](/images/bullhorn-banner-mango.png)

## The Bullhorn

*A Newsletter for the Ansible Developer Community*
*Issue #20, 2021-02-18 ([Past Issues](https://us19.campaign-archive.com/home/?u=56d874e027110e35dea0e03c1&id=d6635f5420))*

Welcome to the Bullhorn, our newsletter for the Ansible developer community. If you have any questions or content you’d like to share, please reach out to us at the-bullhorn@redhat.com, or comment on this [GitHub issue](https://github.com/ansible/community/issues/546).

<!-- TEASER_END -->

**KEY DATES**

* 2021-02-24: [community IRC meeting](https://github.com/ansible/community/issues/539), 19:00 UTC
* 2021-03-02: [Bullhorn #21 content deadline](https://github.com/ansible/community/issues/546)
* 2021-03-03: [community IRC meeting](https://github.com/ansible/community/issues/539), 19:00 UTC
* 2021-03-04: [D&I working group meeting](https://github.com/ansible/community/issues/577), 19:00 UTC
* 2021-03-09: [Ansible Contributor Summit 2021.03](https://www.eventbrite.com/e/ansible-contributor-summit-202103-registration-141735886853?aff=bullhorn) (more info below)
* 2021-03-09: [ETA for Ansible 3.1.0 release](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_3_0.html)
* 2021-05-18: ETA for Ansible 4.0.0 general release (more info below)

**ANSIBLE 4.0.0 ROADMAP AND DATES**

* 2021-03-03: Ansible-4.0.0 alpha1 (biweekly ansible alphas. These are timed to coincide with the start of the ansible-core-2.11 pre-releases).
* 2021-04-13: Last day for new collections to be [submitted for inclusion in Ansible 4](https://github.com/ansible-collections/ansible-inclusion/discussions/). Note that collections MUST be reviewed and approved before being included. There is no guarantee that we will review every collection. The earlier your collection is submitted, the more likely it will be that your collection will be reviewed and the necessary feedback can be addressed in time for inclusion.
* 2021-04-26: Last day for collections to make backwards incompatible releases that will be accepted into Ansible 4.
* 2021-04-27: Ansible-4.0.0 beta1 – feature freeze 1 (weekly beta releases. Collection owners and interested users should test for bugs).
* 2021-05-18: Ansible-4.0.0 general release.

For the full Ansible 4.0.0 schedule please see the [Ansible 4.0.0 roadmap](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_4.html).

**ANSIBLE 3.0.0 NOW GENERALLY AVAILABLE**

Ansible 3.0.0 has been released on February 18th. 🎉

This version of the Ansible community package marks the end of the restructuring of the Ansible ecosystem. This work culminates what began in 2019 to [restructure the Ansible project](https://www.ansible.com/blog/thoughts-on-restructuring-the-ansible-project) and shape [how Ansible content was delivered](https://www.ansible.com/blog/the-future-of-ansible-content-delivery).

To learn more about how and why we got to 3.0.0, we invite you to visit our blog for the background as well as a Q&A:
* [Announcing the Community Ansible 3.0.0 Package](https://www.ansible.com/blog/announcing-the-community-ansible-3.0.0-package)
* [Ansible 3.0.0 Q&A](https://www.ansible.com/blog/ansible-3.0.0-qa)

This Ansible 3.0.0 release is based on the ansible-base-2.10.x package just like ansible-2.10 was, so the changes shouldn’t be too large. However, it does contain new major versions of many collections which means that there will be some backwards incompatible changes in the modules and plugins. The version number has been bumped to 3.0.0 because we have moved to semantic versioning. See the [release announcement by Toshio Kuratomi](https://groups.google.com/g/ansible-announce/c/vdcujxt2pk8) for more information on how we're using semantic versioning, and the other changes in Ansible-3.0.0.

**ANSIBLE 2.10.7 RELEASED**

The Ansible Community Team released Ansible 2.10.7 containing several important bugfixes. For full details, see the [release announcement by Toshio Kuratomi](https://groups.google.com/g/ansible-devel/c/V4oCyU1OQ_c). This is the last planned release of ansible-2.10.x. Further updates will be made to ansible-3.x.

**CHANGES IMPACTING COLLECTION OWNERS**

* If your collection is tested with `ansible-test` using the `--docker` option and you test against `devel` or the `stable-2.11` branch, the following containers will be removed `fedora30`, `fedora31`, `ubuntu1604` on **March 1st**. See [this note](https://github.com/ansible-collections/overview/issues/45#issuecomment-776930466) for futher details.
* Collection repositories that were previously using Shippable for CI testing are moving to Azure Pipelines as Shippable is approaching End of Life. For repositories using GitHub Actions for CI there is no change. You can track the progress [here](https://github.com/ansible-collections/overview/issues/124).
* Security: avoid information leaks (that are easily avoidable) in your modules by using `no_log=True`. Now detected by CI in ansible-core devel, [details](https://github.com/ansible-collections/overview/issues/45#issuecomment-774472384).
* The import sanity test has been extended to cover plugins. Previously it only covered modules ([details](https://github.com/ansible-collections/overview/issues/45#issuecomment-778498813)).
* Updated pylint Sanity Test ([details](https://github.com/ansible-collections/overview/issues/45#issuecomment-777121861)).

To be aware of changes as soon as they happen, we suggest that you subscribe to [Changes impacting Collection Contributors and Maintainers](https://github.com/ansible-collections/overview/issues/45). The "Subscribe" button is on the right below GitHub Labels.

**NEW/UPDATED COMMUNITY COLLECTIONS**

* [Squeezer, an Ansible collection modules for Pulp](https://galaxy.ansible.com/pulp/squeezer) has released 0.0.7. If you're looking for a better way to manage and distribute Debian and Ubuntu content, Pulp can help. If you want to automate your Ubuntu and Debian content management workflows using Ansible, you can now do that with the [latest release of Pulp Squeezer](https://pulpproject.org/2021/02/08/pulp-squeezer-0.0.7/)! 
* The [PostgreSQL collection for Ansible](https://galaxy.ansible.com/community/postgresql) [community.postgresql](https://github.com/ansible-collections/community.postgresql) 1.1.1 has been released ([changelog](https://github.com/ansible-collections/community.postgresql/blob/main/CHANGELOG.rst#v1-1-1)).
* The [Community HashiVault Collection](https://galaxy.ansible.com/community/hashi_vault) [community.hashi_vault](https://github.com/ansible-collections/community.hashi_vault) 1.1.0 was released on 2021-02-08 ([changelog](https://github.com/ansible-collections/community.hashi_vault/blob/main/CHANGELOG.rst#v1-1-0)).
* The [Community General Collection](https://galaxy.ansible.com/community/general) [community.general](https://github.com/ansible-collections/community.general) 2.1.1 has been released, with new features and bugfixes. Please note that this version will not be included in Ansible 3.0.0, and there will be another release (2.2.0) for Ansible 3.1.0.
* The [Ansible Openstack Collection](https://galaxy.ansible.com/openstack/cloud) [openstack.cloud](https://opendev.org/openstack/ansible-collections-openstack) was released recently to 1.3.0 version. It includes a lot of bugfixes, plus five new modules: [identity_role_info](https://opendev.org/openstack/ansible-collections-openstack/src/branch/master/plugins/modules/identity_role_info.py), [keypair_info](https://opendev.org/openstack/ansible-collections-openstack/src/branch/master/plugins/modules/keypair_info.py), [security_group_info](https://opendev.org/openstack/ansible-collections-openstack/src/branch/master/plugins/modules/security_group_info.py), [security_group_rule_info](https://opendev.org/openstack/ansible-collections-openstack/src/branch/master/plugins/modules/security_group_rule_info.py), and [stack_info](https://opendev.org/openstack/ansible-collections-openstack/src/branch/master/plugins/modules/stack_info.py).
* The [Ansible Podman Collection](https://galaxy.ansible.com/containers/podman) [containers.podman](https://github.com/containers/ansible-podman-collections) has released version 1.4.3, which contains a lot of bugfixes and modules compatible with the latest version 3 of Podman. In addition, its [documentation on GitHub](https://containers.github.io/ansible-podman-collections) is now up to date reflecting the latest changes.

**REQUEST FOR FEEDBACK - ANSIBLE NETWORKING**

The Ansible Networking team would like to gather feedback from the network community on how to improve the behaviour of network config module warning messages. Please add your comments in this [discussion on GitHub](https://github.com/ansible/network/discussions/48).

**ANSIBLE-LINT 5.0.0 RELEASED**

A [major v5 new release](https://github.com/ansible-community/ansible-lint/releases) of ansible-lint was made, one that addresses lots of user requests and bugs. Among the most notable changes we should mention:

* Execution of both `ansible-playbook --syntax-check` and `yamllint` (optional) is included, so you no longer need to run them separately.
* New ansible file-type detection logic based on glob patterns.
* Support for collections and installation of requirements.yml inside isolated environments. Those that do not want to install requirements can use offline mode and mock missing collections, roles, modules or extra vars.
* All internal rules now have text based tag names, as they are more human-friendly.
* Rules API changed and custom rules must be updated in order to use with the version.
* Installation instructions were updated and you must make sure to mention which version of Ansible you want to use it with.

Read the [upgrade guidelines](https://github.com/ansible-community/ansible-lint/discussions/1150) on the forum before upgrading. Please use the same thread for feedback and feel free to make pull-requests with fixes if needed.

**BRAND NEW COLLECTION DEPENDENCY RESOLVER IN `ansible-galaxy` CLI**

If you install any Ansible Collections from Galaxy, it'll mean the world to us if you could try out our new and refined `ansible-galaxy collection [download|install|list|verify]` subcommands introduced by [ansible-core PR #72591](https://github.com/ansible/ansible/pull/72591). As a part of the ansible-core 2.11 effort to improve and refine the UX of the `ansible-galaxy` CLI related to managing third-party collection installs, this pull request introduced a new runtime dependency — [resolvelib](https://github.com/sarugaku/resolvelib). This library implements an agnostic dependency resolver with the support for backtracking that has recently been incorporated by [pip](https://pip.pypa.io) (Python package installer), by default. Doing so allowed us to substantially simplify the codebase in [ansible-core](https://github.com/ansible/ansible) and helped us implement new features that made the behavior of `ansible-galaxy collection` subcommands closer to how [pip](https://pip.pypa.io) works.

If you want to learn more about the internals, check out [this post](https://webknjaz.me/prose/ansible-galaxy-reuses-pips-resolvelib/).

Among new features, this change allows upgrading pre-installed collections to newer versions without requiring `--force` or `--force-with-deps` options when the existing installation does not satisfy the user request or any transitive requirements discovered during the process of dependency resolution.

Another feature is the new `--upgrade` (or `-U`) option that allows you to explicitly request updating the installed collections.

This change has already been accepted, so doing `pip install https://github.com/ansible/ansible/tarball/devel` should be enough to get a version that contains the refactoring. Another option would be to install a pre-release (like a release candidate) of [ansible-core](https://github.com/ansible/ansible) from PyPI, but it's not yet published at the time of writing.

Please try out these updates — we'd love to hear what you think!

**NEW COMMUNITY STATISTICS MAP**

There has been a map for community data (Meetup locations, PR counts) for a while, but it was a bit buried and hard to find. [Greg](https://twitter.com/Gwmngilfen) has just released the first version of a new map stats app, which you will find on the [stats server](https://stats.eng.ansible.com/) or via the [direct link](https://stats.eng.ansible.com/app/map_app). Suggestions for more things to map or other ways to display the data are welcome by raising issues [on GitHub](https://github.com/ansible-community/stats-map).

**DIVERSITY AND INCLUSION WG SEEKING EXPERIENCE IN ACCESSIBLE DESIGN**

The Ansible [Diversity and Inclusion](https://github.com/ansible/community/wiki/Diversity) Working Group is seeking members of the community with experience in accessible design or use of assistive technologies to help identify areas for improvement and implement changes to our online media (documentation, Github templates and forms, etc). Please reach out to the group on [Freenode IRC in channel #ansible-diversity](https://webchat.freenode.net/#ansible-diversity) if you would like to participate.

**CONTENT FROM THE ANSIBLE COMMUNITY**

* At [FOSDEM 2021](https://fosdem.org/2021/), [Brian Bouterse](https://github.com/bmbouter) gave a talk titled [Host your own on-premise Ansible Galaxy](https://fosdem.org/2021/schedule/event/hostyourownansiblegalaxy/). Here are the [notes from the talk](https://hackmd.io/@pulp/ansible-containers#/) as well as the [recording](https://video.fosdem.org/2021/D.infra/hostyourownansiblegalaxy.webm).
* A blog post by [Jeff Geerling](https://github.com/geerlingguy) - [Fast vs Easy: Benchmarking Ansible Operators for Kubernetes](https://www.ansible.com/blog/fast-vs-easy-benchmarking-ansible-operators-for-kubernetes).
* Read about [David](https://github.com/dmsimard)'s plan to move code review from Gerrit to GitHub for the health and sustainability of the [ara project](https://ara.recordsansible.org/), and add your thoughts on [Would you contribute to ara if pull requests on GitHub were possible?](https://github.com/ansible-community/ara/issues/205)
* [Abhijeet Kasurde](https://github.com/Akasurde) wrote a blog post about [Creating Tags in vCenter using Ansible](https://medium.com/@AbhijeetKasurde/ansible-create-a-tag-in-vcenter-dd9cb1b2186b).

**ANSIBLE CONTRIBUTOR SUMMIT 2021.03**

The next Ansible Contributor Summit will be held on **Tuesday, March 9, from [12:00-20:00 UTC](https://www.timeanddate.com/worldclock/fixedtime.html?msg=Ansible+Contributor+Summit+2021.03&iso=20210309T12)**. Please see the details and register on [Eventbrite](https://www.eventbrite.com/e/ansible-contributor-summit-202103-registration-141735886853?aff=bullhorn), and propose topics you’d like to discuss in this [HackMD note](https://hackmd.io/uZDSLOOdS1Kx0xfZVIATmQ).

**ANSIBLE VIRTUAL MEETUPS**

We're happy to introduce a new meetup group: [Ansible Iraq](https://www.meetup.com/ansible-iraq/)! They have planned their first meetup for Sun, Feb 28 · 8:00 PM GMT+3. More details and RSVP on the [event page](https://www.meetup.com/ansible-iraq/events/276327264/). 

**FEEDBACK**

Have any questions you’d like to ask, or issues you’d like to see covered? Please send us an email at the-bullhorn@redhat.com.
