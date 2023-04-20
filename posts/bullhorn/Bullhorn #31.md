---
title: "Bullhorn #31"
date: 2021-07-29 20:00 UTC
tags: news
category: bullhorn
type: text
---

![Ansible Bullhorn banner](/images/bullhorn-banner-mango.png)

## The Bullhorn

*A Newsletter for the Ansible Developer Community*
*Issue #31, 2021-07-29 ([Past Issues](https://us19.campaign-archive.com/home/?u=56d874e027110e35dea0e03c1&id=d6635f5420))*

Welcome to the Bullhorn, our newsletter for the Ansible developer community. If you have any questions or content you’d like to share, please reach out to us at the-bullhorn@redhat.com, or comment on this [GitHub issue](https://github.com/ansible/community/issues/546).

<!-- TEASER_END -->

**KEY DATES**

* 2021-08-03: [Ansible & Matrix Video Q&A](https://youtu.be/9R31zq_7R6c), 14:00 UTC
* 2021-08-04: [community IRC meeting](https://github.com/ansible/community/issues/539), 18:00 UTC (propose topics [here](https://github.com/ansible-community/community-topics/issues))
* 2021-08-05: [D&I working group meeting](https://github.com/ansible/community/issues/577), 19:00 UTC
* 2021-08-10: [ETA for Ansible 4.4.0 release](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_4.html)
* 2021-08-11: [community IRC meeting](https://github.com/ansible/community/issues/539), 18:00 UTC (propose topics [here](https://github.com/ansible-community/community-topics/issues))
* 2021-08-16: ETA for Ansible-Core 2.11.4 and Ansible-Base 2.10.13 release
* 2021-08-17: [Bullhorn #32 content deadline](https://github.com/ansible/community/issues/546)
* 2021-09-28: [Contributor Summit 2021.09](https://hackmd.io/@ansible-community/contrib-summit-202109) - Day 1 💾📅
* 2021-09-29/30: [AnsibleFest 2021](https://www.ansible.com/ansiblefest) 💾📅
* 2021-10-01: [Contributor Summit 2021.09](https://hackmd.io/@ansible-community/contrib-summit-202109) - Day 2 💾📅

**ANSIBLE 4.3.0 RELEASED**

The Ansible Community team announced the availability of Ansible 4.3.0 on July 20th. This update contains bugfixes and new, backwards compatible features in the contained collections. The release makes use of Ansible-core-2.11.

For what's new in this release and how to get it, please see [Toshio Kuratomi’s email to the ansible-announce list](https://groups.google.com/g/ansible-announce/c/ssbMIqs4qNM).

**ANSIBLE-CORE 2.11.3, ANSIBLE-BASE 2.10.12, AND ANSIBLE 2.9.24 RELEASED**

The Ansible Core team announced the maintenance releases of Ansible-Core 2.11.3, Ansible-Base 2.10.12, and Ansible 2.9.24 on July 19th. Follow [this link](https://groups.google.com/g/ansible-devel/c/KLqQiqgdEuA) for Rick Elrod’s email to the ansible-devel mailing list, to obtain details on what’s new, installation instructions, and schedule for future releases.

**ANSIBLE-CORE 2.12 RELEASE SCHEDULE**

The Ansible Core team has updated the [ansible-core roadmap](https://docs.ansible.com/ansible-core/devel/roadmap/ROADMAP_2_12.html) that will delay the release of 2.12 from 2021-10-25 to 2021-11-08.

The Ansible 5.0 community package [roadmap](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_5.html) will have to be updated as well in order to take into account the planned changes. We will provide more information on the new plan soon.

**NEW/UPDATED COMMUNITY COLLECTIONS**

* Community General Collection - [community.general](https://galaxy.ansible.com/community/general) 3.4.0 has been released with new features and bugfixes.
* Community HashiVault Collection - [community.hashi_vault](https://galaxy.ansible.com/community/hashi_vault) [1.3.2](https://github.com/ansible-collections/community.hashi_vault/releases/tag/1.3.2) has been released.
* Community libvirt Collection - [community.libvirt](https://galaxy.ansible.com/community/libvirt) 1.0.2 has been released.
* ProxySQL collection for Ansible - [community.proxysql](https://galaxy.ansible.com/community/proxysql) 1.1.0 has been released.
* Community RabbitMQ Collection - [community.rabbitmq](https://galaxy.ansible.com/community/rabbitmq) 1.1.0 has been released.

**ANNOUNCING NEW COLLECTION MAINTAINERS**

We are happy to announce that the [community.proxysql](https://github.com/ansible-collections/community.proxysql) collection has found a new maintainer: [Markus Bergholz](https://github.com/markuman) (markuman on GitHub / IRC).

He has done an excellent job as a code contributor in different repositories under the `ansible` and `ansible-collections` organizations, as well as being a reviewer and an active community member.

On behalf of the Ansible Community and the Community Team, we’d like to congratulate him on getting commit access, and say THANK YOU!

**LOOKING FOR COLLECTION MAINTAINERS/CONTRIBUTORS**

- The [community.rabbitmq](https://github.com/ansible-collections/community.rabbitmq) collection is urgently looking for new maintainers. If you're interested, please respond in the [pinned issue](https://github.com/ansible-collections/community.rabbitmq/issues/81).
- The [community.libvirt](https://github.com/ansible-collections/community.libvirt) collection is urgently looking for new maintainers. If you're interested, please respond in the [pinned issue](https://github.com/ansible-collections/community.libvirt/issues/78).

**ANSIBLE COMMUNITY AND MATRIX**

[Greg Sutcliffe](https://matrix.to/#/@gwmngilfen:ansible.im/) will be hosting a [Matrix Q&A](https://youtu.be/9R31zq_7R6c), next Tuesday August 3rd at [14:00 UTC](https://www.timeanddate.com/worldclock/fixedtime.html?msg=Proposal%3A+Ansible+Community+to+accept+Matrix+as+an+equal+partner+to+IRC&iso=20210803T15&p1=136), as a way to test out a new method to run our conferences. The video stream will be on [YouTube](https://youtu.be/9R31zq_7R6c), and chat will be held directly in our [IRC/Matrix room](https://matrix.to/#/#community:ansible.im), so folks will be able to play back both video and chat later if they wish.

**ANSIBLE GALAXY IMPORT CHANGES**

Please be aware that there's a change made in Ansible Galaxy to require mandatory `requires_ansible` in the `meta/runtime.yml` file for uploading a collection ([#122](https://github.com/ansible/galaxy-importer/pull/122), [#124](https://github.com/ansible/galaxy-importer/pull/124)). After you've added the collection, you will probably hit `ansible-test` failure in sanity checks if you use it with the `--venv` option, since it is unable to check this field due to the [failing requirement](https://github.com/ansible/ansible/issues/75353). You will need to have the `meta/runtime.yml` file now for your collection to be uploaded.

**COLLECTION INCLUSION CANDIDATES FOR ANSIBLE 5.0**

We are working towards adding new collections into Ansible 5.0.0, and you can track the progress of the various collections in this [GitHub issue](https://github.com/ansible-community/community-topics/issues/32).

**ANSIBLE CONTRIBUTOR SUMMIT AND SURVEY** 

Thanks to those who have taken the time to fill in the [Contributor Survey](https://www.surveymonkey.co.uk/r/3YBYKTS)! If you haven't done so, please take a few moments for [the survey](https://www.surveymonkey.co.uk/r/3YBYKTS), we'd greatly appreciate it!

The [next Contributor Summit](https://hackmd.io/@ansible-community/contrib-summit-202109) will be on September 28th and October 1st, alongside [AnsibleFest](https://www.ansible.com/ansiblefest). The first day (Tuesday, 28/9) is aimed at new contributors and people who want to understand what is involved in contributing. Day two (Friday, 1/10) will contain the usual interactive discussions with more technical details. If you'd like to help with the planning (especially with the content for day 1), please see this [issue](https://github.com/ansible-community/community-topics/issues/30).

**THE ANSIBLE TEAM IS HIRING**

We're looking for Senior Software Engineers to join us as we take the Ansible Automation Platform to the next level and help the world automate solutions for anything and everything you might imagine. Please check the job descriptions in the links and apply!

* [Senior Software Engineer - Ansible](https://global-redhat.icims.com/jobs/88229/senior-software-engineer---ansible/job) - Remote IT
* [Senior Software Engineer - Ansible](https://global-redhat.icims.com/jobs/88230/senior-software-engineer---ansible/job) - Remote ES
* [Senior Software Engineer - Ansible Controller API](https://us-redhat.icims.com/jobs/86519/senior-software-engineer---ansible-controller-api/job) - Remote US NC
* [Senior Software Engineer - Ansible](https://global-redhat.icims.com/jobs/86822/senior-software-engineer--ansible/job) - Remote CZ

In addition, we're also looking for a [Technical Marketing Manager, Ansible Automation](https://us-redhat.icims.com/jobs/88164/senior-product-marketing-manager/job) - worldwide, remote. In this role, you will have significant technical sales enablement responsibilities, including the development of technical content for presentations, demonstrations, videos, e-books, conference talks, and sales tools that will be used by thousands of solutions architects, consultants, and partner presales associates.

**FEEDBACK**

Have any questions you’d like to ask, or issues you’d like to see covered? Please send us an email at the-bullhorn@redhat.com.

