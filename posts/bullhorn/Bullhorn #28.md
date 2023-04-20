---
title: "Bullhorn #28"
date: 2021-06-11 18:00 UTC
tags: news
category: bullhorn
type: text
---

![Ansible Bullhorn banner](/images/bullhorn-banner-mango.png)

## The Bullhorn

*A Newsletter for the Ansible Developer Community*
*Issue #28, 2021-06-11 ([Past Issues](https://us19.campaign-archive.com/home/?u=56d874e027110e35dea0e03c1&id=d6635f5420))*

Welcome to the Bullhorn, our newsletter for the Ansible developer community. If you have any questions or content you’d like to share, please reach out to us at the-bullhorn@redhat.com, or comment on this [GitHub issue](https://github.com/ansible/community/issues/546).

<!-- TEASER_END -->

**KEY DATES**

* 2021-06-15/16: [Red Hat Summit 2021 Virtual Experience Part 2](https://www.redhat.com/en/summit)
* 2021-06-16: [community IRC meeting](https://github.com/ansible/community/issues/539), 18:00 UTC (propose topics [here](https://github.com/ansible-community/community-topics/issues))
* 2021-06-21: ETA for Ansible-Core 2.11.2 and Ansible-Base 2.10.11 release
* 2021-06-22: [Bullhorn #29 content deadline](https://github.com/ansible/community/issues/546)
* 2021-06-23: [community IRC meeting](https://github.com/ansible/community/issues/539), 18:00 UTC (propose topics [here](https://github.com/ansible-community/community-topics/issues))
* 2021-06-24: [D&I working group meeting](https://github.com/ansible/community/issues/577), 19:00 UTC
* 2021-06-29: [ETA for Ansible 4.2.0 release](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_4.html)

**ANSIBLE 4.1.0 RELEASED**

The Ansible Community team announced the general availability of Ansible 4.1.0 on June 10th. This update contains bugfixes and new, backwards compatible features in the contained collections. The release makes use of Ansible-core-2.11. There may be changes to the playbook language or other backwards incompatibilities. Please see the [porting guide](https://docs.ansible.com/ansible/devel/porting_guides/porting_guide_4.html) for details.

For what's new in this release and how to get it, please see [Toshio Kuratomi’s email to the ansible-announce list](https://groups.google.com/g/ansible-announce/c/Zz3z_jV2-e8). 

Ansible 5 development begins now. We're tentatively planning to release Ansible 5.0.0 in November 2021, bringing in the Ansible-core-2.12 release.

**COMMUNICATION: LIBERA.CHAT IRC NETWORK**

Ansible Community has made the [decision](https://github.com/ansible-community/community-topics/issues/19) to move to [Libera.Chat](https://libera.chat/) IRC network. We are using the same channel names as we did on the Freenode network. Documentation will be updated shortly, and we will share them when ready. From now on, discussions and meetings will take place on [Libera.Chat](https://libera.chat/) instead of Freenode.

**NEW/UPDATED COMMUNITY COLLECTIONS**

* OKD Collection for Ansible - the [community.okd](https://galaxy.ansible.com/community/okd) collection repository has been moved to [its new home](https://github.com/openshift/community.okd) under the `openshift` GitHub organization. All links to its previous home under `ansible-collections` should automatically redirect.
* Ansible Community Crypto Collection - [community.crypto](https://galaxy.ansible.com/community/crypto) 1.7.0 has been released, with a bunch of new features and bugfixes.
* Ansible VMware vSphere Collection - [vmware.vmware_rest](https://galaxy.ansible.com/vmware/vmware_rest) 2.0.0rc1 has been released. This new branch only support vSphere 7.0.2+ and comes with a new set of modules to manage the vSphere appliances. 
* The Amazon AWS Collection - [amazon.aws](https://galaxy.ansible.com/amazon/aws)  and Community AWS Collection - [community.aws](https://galaxy.ansible.com/community/aws) are now only tested on Python 3.6+.  Changes that use Python 3 syntax can be made to both collections.
    * The inventory script included in community.aws has been moved to a [separate repository](https://github.com/ansible-community/contrib-scripts). It will no longer be included in community.aws 3.0.0, and will be removed from the community.aws `main` branch during the 3.0 development cycle.
* Community General Collection - [community.general](https://galaxy.ansible.com/community/general) 2.5.3 and 3.2.0 have been released.
    * All inventory and vault scripts included in community.general have been moved to a [separate repository](https://github.com/ansible-community/contrib-scripts). They will no longer be included in community.general 4.0.0, and will be removed from community.general's `main` branch soon.
* Docker Community Collection - [community.docker](https://galaxy.ansible.com/community/docker) 1.7.0 has been released.
* Kubernetes Collection for Ansible - [kubernetes.core](https://galaxy.ansible.com/kubernetes/core) 2.0.0 has been released. This release includes:
    * The migration to `kubernetes.core` from `community.kubernetes` including the move to [its new repo](https://github.com/ansible-collections/kubernetes.core)
    * The openshift client dependency -- the collection now relies solely on the official kubernetes community client library
    * Python2 support has been dropped
    * Several performance improvements including...
      * Introduction of turbo mode to reuse connections to the K8s API service
      * You can now apply multiple templates in one task rather than one task per loop item
    * Improved the resource patch handling including...
      * Only patch existing objects
      * The introduction of `k8s_json_patch` to better handle JSON patches
    * Many more bugs fixes and small incremental improvements -- see the [project CHANGELOG](https://github.com/ansible-collections/kubernetes.core/blob/main/CHANGELOG.rst) for a complete list.

**ANNOUNCING NEW COLLECTION MAINTAINERS**

We are happy to announce that, since the [Contributor Summit in March 2021](https://hackmd.io/@ansible-community/contrib-summit-202103), the project has found new maintainers, among others:
* Amin Vakil (@aminvakil) and Alexey Znamensky (@russoz) in `community.general`, and
* Jorge Rodriguez (@Jorge-Rodriguez) in `community.mysql`.

With their participation, each of the above collections now has 3 active maintainers.

They have done an excellent job with hundreds of merged pull requests and a great history of reviews in different repositories. Their contributions are influencing the whole project as they have helped and are helping to shape very important general documents which live in the [community-docs](https://github.com/ansible/community-docs) repository. These include the quick-start guide, contributing file template, review checklist, maintainer guidelines, and other docs that will help many contributors improve Ansible.

On behalf of the Ansible Community and the Community Team, we'd like to congratulate them on getting `commit` access, and say THANK YOU!

**LOOKING FOR COLLECTION MAINTAINERS/CONTRIBUTORS**

The following collections - [community.mysql](https://github.com/ansible-collections/community.mysql/issues/180), [community.postgresql](https://github.com/ansible-collections/community.postgresql/issues/102), and [community.proxysql](https://github.com/ansible-collections/community.proxysql/issues/39) - are looking for new maintainers and contributors! If you are interested, please refer to the corresponding pinned issues linked via the collection names.

**REVIEWS AND FEEDBACK WANTED!**

* Requesting review on [gRPC connection plugin](https://github.com/ansible-collections/ansible.netcommon/pull/279). This PR will add a new connection plugin for gRPC based communication with network hosts.
* Requesting review on [Platform agnostics network resource manager role](https://github.com/ansible-collections/ansible.network/issues/13) for [ansible.network](https://github.com/ansible-collections/ansible.network) collection.
* Ansible has a new open source, data-centric, container-first, developer-friendly interface called [ansible-navigator](https://github.com/ansible/ansible-navigator) which will be included in the next Red Hat Ansible Automation Platform release. If you don't mind the bleeding edge, try out the [alpha-1 release](https://pypi.org/project/ansible-navigator/1.0.0a1/) that was released to PyPI on June 1st. We are looking forward to your feedback, issues, and PRs in the [repo](https://github.com/ansible/ansible-navigator). Please help us make this great!
* If you are using role argument specs in collections, or are trying them out, please provide feedback for the following PRs:
    - [Generate role documentation](https://github.com/ansible-community/antsibull/pull/272) - this PR creates role documentation from role argument specs for the docsite, similarly to plugin and module documentation.
    - [Support roles with argument spec](https://github.com/ansible-community/antsibull-changelog/pull/55) - this PR allows antsibull-changelog to auto-detect new roles (it only considers the `main` entrypoint) in collections.
* There's a feature request for the Cisco ASA collection to have a [dynamic_filter](https://github.com/ansible-collections/cisco.asa/issues/115) ASA module which can enable Botnet filtering via Cisco dynamic/static DB. Feedback is welcome from the community as to how often you've used the Cisco ASA botnet filtering feature, and if you want the process to be automated via Ansible Cisco ASA module.

**COMMUNITY DOCUMENTATION UPDATE**

The collection maintainer guidelines have been merged to the work-in-progress [community docs](https://github.com/ansible/community-docs/). Along with them are other documents that can be used across the collections, such as the review checklist, releasing guidelines, contributing.rst, and quick-start guide. Thanks to everyone who helped out! Feel free to open PRs and share your ideas, as well as refer to the documents from your READMEs, CONTRIBUTING.mds, and so on. When the community docs have settled in a permanent location, we will find and correct all the references in the repositories under the ansible-collections GitHub organization.

**CONTENT FROM THE ANSIBLE COMMUNITY**

The XLAB [Steampunk team](https://steampunk.si/) has made part of their internal QA tool available to the general public. You can test it out [here](https://scanner.steampunk.si/).

**THE ANSIBLE TEAM IS HIRING**

Red Hat is hiring several roles to work on Ansible. Please check the job descriptions in the links and apply!

* [Principal Software Engineer- Ansible](https://global-redhat.icims.com/jobs/86822/principal-software-engineer--ansible/job)
* [DevOps Automation Engineer - Red Hat Ansible](https://global-redhat.icims.com/jobs/82487/devops-automation-engineer---red-hat-ansible/job)
* [Senior Field Product Manager - Technical](https://us-redhat.icims.com/jobs/82489/senior-product-manager---technical/job)
* [Senior Product Manager - Ansible](https://us-redhat.icims.com/jobs/82490/senior-product-manager---technical/job)

**ANSIBLEFEST 2021 CFP**

This year's AnsibleFest will be a virtual event, happening on September 29–30, 2021. The call for presentations is now open! Add your voice to the conversation by telling us your automation story - check out the details and submit your proposal [here](https://www.ansible.com/ansiblefest).

**ANSIBLE CONTRIBUTOR SUMMIT 2021.06** 

Thanks to everyone who participated in the [Ansible Contributor Summit 2021.06](https://hackmd.io/@ansible-community/contrib-summit-202106) on June 8, 2021! We are editing the recordings, and will gather the logs/presentations/videos and share them in the [Ansible Community wiki](https://github.com/ansible/community/wiki/Contributor-Summit) shortly.  Look out for the Contributor Survey in the coming weeks!

The next Contributor Summit will take place alongside AnsibleFest. The dates are not confirmed yet, but it will be in the week of September 27, 2021. Details to follow!

**FEEDBACK**

Have any questions you’d like to ask, or issues you’d like to see covered? Please send us an email at the-bullhorn@redhat.com.
