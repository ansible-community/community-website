---
title: "Bullhorn #23"
date: 2021-04-01 20:30 UTC
tags: news
category: bullhorn
type: text
---

![Ansible Bullhorn banner](/images/bullhorn-banner-mango.png)

## The Bullhorn

*A Newsletter for the Ansible Developer Community*
*Issue #23, 2021-04-01 ([Past Issues](https://us19.campaign-archive.com/home/?u=56d874e027110e35dea0e03c1&id=d6635f5420))*

Welcome to the Bullhorn, our newsletter for the Ansible developer community. If you have any questions or content you’d like to share, please reach out to us at the-bullhorn@redhat.com, or comment on this [GitHub issue](https://github.com/ansible/community/issues/546).

<!-- TEASER_END -->

**KEY DATES**

* 2021-04-07: [community IRC meeting](https://github.com/ansible/community/issues/539), 18:00 UTC
* 2021-04-13: Last day for new collections to be [submitted for inclusion in Ansible 4](https://github.com/ansible-collections/ansible-inclusion/discussions/). Note that collections MUST be reviewed and approved before being included.
* 2021-04-13: [Bullhorn #24 content deadline](https://github.com/ansible/community/issues/546)
* 2021-04-14: [community IRC meeting](https://github.com/ansible/community/issues/539), 18:00 UTC
* 2021-04-15: [D&I working group meeting](https://github.com/ansible/community/issues/577), 19:00 UTC
* 2021-04-20: [ETA for Ansible 3.3.0 release](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_3_0.html)
* 2021-04-26: [ETA for ansible-core 2.11 release](https://github.com/ansible/ansible/blob/devel/docs/docsite/rst/roadmap/ROADMAP_2_11.rst)
* 2021-05-18: [ETA for Ansible 4.0.0 release](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_4.html)

**ANSIBLE 3.2.0 RELEASED**

The Ansible Community team announced the general availability of Ansible 3.2.0 on March 30th. This update contains bugfixes and new, backwards compatible features in the contained collections. If you would like to learn about how and why we got to version 3.0.0, we invite you to visit our blog for the [background](https://www.ansible.com/blog/announcing-the-community-ansible-3.0.0-package) as well as a [Q&A](https://www.ansible.com/blog/ansible-3.0.0-qa). For what's new in the release and how to install it, please see [Toshio Kuratomi's email to the ansible-announce list](https://groups.google.com/g/ansible-announce/c/GfcyHboqprA).

**ANSIBLE 4.0.0 ALPHA3 RELEASED**

The Ansible Community team announced the third alpha release of Ansible 4.0.0 on March 30th. This update is based on the ansible-core-2.11.x package which is a major update from the Ansible 3.x package (which is based on ansible-base-2.10.x). There may be backwards incompatibilities in the core playbook language. Please see the [porting guide](https://docs.ansible.com/ansible/devel/porting_guides/porting_guide_4.html) for details.

This is an alpha release. Therefore, there may be more backwards incompatible changes and new features added before Ansible 4.0.0 final is released. For what is included in this release, and how to get it for testing, please see [Toshio Kuratomi's email to the ansible-devel list](https://groups.google.com/g/ansible-devel/c/-kcCaQ9Yrgs).

**UPCOMING ANSIBLE 2.8, ANSIBLE 2.9, ANSIBLE-BASE, ANSIBLE-CORE SCHEDULE**

The Ansible Core team shared the plan for Ansible releases prior to 2.10, and the next few ansible-base and ansible-core releases.

On 26 April 2021, several things are slated to happen:
* ansible-core 2.11.0 will see a general availability release
* ansible 2.8.z will be considered End Of Life and will no longer see updates
* ansible 2.9.z will drop to security-only releases

For more detailed dates of specific releases, please take a look at [Rick Elrod's email to the ansible-devel mailing list](https://groups.google.com/g/ansible-devel/c/udlVP0236zw).

**NEW/UPDATED COMMUNITY COLLECTIONS**


* Community HashiVault Collection - [community.hashi_vault](https://galaxy.ansible.com/community/hashi_vault) [1.1.3](https://github.com/ansible-collections/community.hashi_vault/releases/tag/1.1.3) has been released, with a bugfix for `userpass` authentication.
* [community.sops](https://galaxy.ansible.com/community/sops) 1.0.6, [community.crypto](https://galaxy.ansible.com/community/crypto) 1.6.0, and [community.general](https://galaxy.ansible.com/community/general) 1.3.9 and 2.3.0 have been released to fix compatibility issues with the latest ansible-core 2.11 beta. (The versions included in Ansible 4.0.0 alpha 2 and 3 contain these fixes.)
* PostgreSQL collection for Ansible - [community.postgresql](https://galaxy.ansible.com/community/postgresql) 1.2.0 has been released with new features.
* Community General Collection - [community.general](https://galaxy.ansible.com/community/general) 2.4.0 has been released (new plugins, modules, features, bugfixes).

**KUBERNETES COLLECTION MIGRATION**

On Monday April 5th the Ansible Kubernetes collection will be migrating it's working repository from [`community.kubernetes`](https://github.com/ansible-collections/community.kubernetes) to its new [`kubernetes.core`](https://github.com/ansible-collections/kubernetes.core) repo home. This is one of the final steps in the transition of this content to a project led by Red Hat Ansible that we started last year. This is just a development activity move to a different repository at this time. The `community.kubernetes` repo will remain, but will be locked once things have been moved. 

We recommend that you upgrade to the latest stable release (1.2) and start using the `kubernetes.core` namespace in your projects if you haven't already. We are already releasing this content as both `community.kubernetes` and `kubernetes.core` currently, but will be phasing out the former in the future. For more info, please see [this blog post](https://www.ansible.com/blog/whats-new-and-whats-changed-in-the-ansible-content-collection-for-kubernetes). 

We appreciate your patience as we try to work through this with the least amount of disruption possible. 

**THE ANSIBLE TEAM IS HIRING**

Red Hat is hiring several roles to work on Ansible. Please check the job descriptions in the links and apply!
* [Manager, Ansible Cloud Engineering](https://us-redhat.icims.com/jobs/82347/manager%2c-ansible-cloud-engineering/job)
* [Technical Marketing Manager - Red Hat Ansible Automation Platform](https://global-redhat.icims.com/jobs/82487/technical-marketing-manager---red-hat-ansible-automation-platform/job)
* [Technical Marketing Manager](https://us-redhat.icims.com/jobs/82006/technical-marketing-manager/job)
* [Senior Technical Marketing Manager](https://us-redhat.icims.com/jobs/82005/senior-technical-marketing-manager/job)

**CONTENT FROM THE ANSIBLE COMMUNITY**

[Werner Dijkerman](https://github.com/dj-wasabi) published 3 blog posts that make use of Ansible and the Zabbix Community collection to get a Zabbix environment running:

* Part 1: [Installing the Zabbix Server with Ansible](https://blog.zabbix.com/installing-the-zabbix-server-with-ansible/13317/)
* Part 2: [Installing and configuring the Zabbix Proxy](https://blog.zabbix.com/installing-and-configuring-the-zabbix-proxy/13319/)
* Part 3: [Finalizing the installation of Zabbix Agent with Ansible](https://blog.zabbix.com/finalizing-the-installation-of-zabbix-agent-with-ansible/13321/)

**ANSIBLE VIRTUAL MEETUPS**

The following virtual meetup(s) are being held in the Ansible community over the next month:

* Mon, Apr 5 · 12:00 PM GMT+8 - [Ansible Singapore](https://www.meetup.com/Ansible-Singapore/events/277147045/) - Ansible Virtual Meet Up - Apr 2021
* Wed, Apr 21 · 5:30 PM GMT+2 - [Ansible in DevOps Torun-Bydgoszcz](https://www.meetup.com/Ansible-in-DevOps-Torun-Bydgoszcz/events/276022444/) - AiDO Meetup #15 Back to normal

**FEEDBACK**

Have any questions you’d like to ask, or issues you’d like to see covered? Please send us an email at the-bullhorn@redhat.com.
