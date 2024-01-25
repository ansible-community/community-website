---
title: "Bullhorn #32"
date: 2021-08-19 22:30 UTC
tags: news
category: bullhorn
type: text
---

![Ansible Bullhorn banner](/images/bullhorn-banner-mango.png)

## The Bullhorn

*A Newsletter for the Ansible Developer Community*
*Issue #32, 2021-08-19 ([Past Issues](https://us19.campaign-archive.com/home/?u=56d874e027110e35dea0e03c1&id=d6635f5420))*

Welcome to the Bullhorn, our newsletter for the Ansible developer community. If you have any questions or content you’d like to share, please reach out to us at the-bullhorn@redhat.com, or comment on this [GitHub issue](https://github.com/ansible/community/issues/546).

<!-- TEASER_END -->

**KEY DATES**

* 2021-08-25: [community IRC meeting](https://github.com/ansible/community/issues/539), 18:00 UTC (propose topics [here](https://github.com/ansible-community/community-topics/issues))
* 2021-08-31: [ETA for Ansible 4.5.0 release](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_4.html)
* 2021-08-31: [Bullhorn #33 content deadline](https://github.com/ansible/community/issues/546)
* 2021-09-01: [community IRC meeting](https://github.com/ansible/community/issues/539), 18:00 UTC (propose topics [here](https://github.com/ansible-community/community-topics/issues))
* 2021-09-02: [D&I working group meeting](https://github.com/ansible/community/issues/577), 19:00 UTC
* 2021-09-13: ETA for Ansible-Core 2.11.5 and Ansible-Base 2.10.14 release
* 2021-09-28: [Contributor Summit 2021.09](https://ansiblecs202109.eventbrite.com/?aff=bullhorn) - Day 1 💾📅
* 2021-09-29/30: [AnsibleFest 2021](https://www.ansible.com/ansiblefest) 💾📅
* 2021-10-01: [Contributor Summit 2021.09](https://hackmd.io/@ansible-community/contrib-summit-202109) - Day 2 💾📅

**ANSIBLE 4.4.0 RELEASED**

The Ansible Community team announced the availability of Ansible 4.4.0 on August 10th. This update contains bugfixes and new, backwards compatible features in the contained collections. The release makes use of Ansible-core-2.11.

For what's new in this release and how to get it, please see [Toshio Kuratomi’s email to the ansible-announce list](https://groups.google.com/g/ansible-announce/c/C6NgzAIHgG4).

**ANSIBLE-CORE 2.11.4, ANSIBLE-BASE 2.10.13, AND ANSIBLE 2.9.25 RELEASED**

The Ansible Core team announced the maintenance releases of Ansible-Core 2.11.4, Ansible-Base 2.10.13, and Ansible 2.9.25 on August 18th. Follow [this link](https://groups.google.com/g/ansible-devel/c/vaI6IeusQDQ) for Rick Elrod’s email to the ansible-devel mailing list, to obtain details on what’s new, installation instructions, and schedule for future releases.

**ANSIBLE CONTRIBUTOR SUMMIT** 

The [next Contributor Summit](https://hackmd.io/@ansible-community/contrib-summit-202109) will be on September 28th and October 1st, alongside [AnsibleFest](https://www.ansible.com/ansiblefest). Registration is open! Please register on [Eventbrite](https://ansiblecs202109.eventbrite.com/?aff=bullhorn) to stay informed of updates to the event. Note that the AnsibleFest registration is separate from the Contributor Summit.

The first day (Tuesday, 28/9) is aimed at new contributors and people who want to understand what is involved in contributing. Day two (Friday, 1/10) will contain the usual interactive discussions with more technical details. If you'd like to help with the planning (especially with the content for day 1), please see this [issue](https://github.com/ansible-community/community-topics/issues/30).

**NEW/UPDATED COMMUNITY COLLECTIONS**

* Community RouterOS Collection - [community.routeros](https://galaxy.ansible.com/community/routeros) 2.0.0-a1 has been released; there's a breaking change in the behavior of the `community.routeros.api` module with respect to error handling. If you are using this collection / module, please check out the prerelease to ensure you will not be surprised by the 2.0.0 release.
* Docker Community Collection - [community.docker](https://galaxy.ansible.com/community/docker) 1.9.0 has been released with a new connection plugin (`community.docker.nsenter`), new features, and bugfixes.
* Ansible Community Crypto Collection - [community.crypto](https://galaxy.ansible.com/community/crypto) 1.8.0 has been released.
* Community General Collection - [community.general](https://galaxy.ansible.com/community/general) 2.5.5 and 3.5.0 have been released.
* MySQL collection for Ansible - [community.mysql](https://galaxy.ansible.com/community/mysql) 1.4.2, 2.1.1, and 2.2.0-a1 have been released.
* Ansible POSIX Collection - [ansible.posix](https://galaxy.ansible.com/ansible/posix) [1.3.0](https://github.com/ansible-collections/ansible.posix/blob/main/CHANGELOG.rst#v1-3-0) has been released.
* ProxySQL collection for Ansible - [community.proxysql](https://galaxy.ansible.com/community/proxysql) [1.2.0](https://github.com/ansible-collections/community.proxysql/blob/main/CHANGELOG.rst#v1-2-0) has been released.
* Ansible Podman Collection - [containers.podman](https://galaxy.ansible.com/containers/podman) [1.7.0](https://github.com/containers/ansible-podman-collections/blob/master/CHANGELOG.rst#v1-7-0) has been released, with new module [podman_secret](https://github.com/containers/ansible-podman-collections/blob/master/plugins/modules/podman_secret.py) for management of Podman secrets. (More info can be found [here](https://www.redhat.com/sysadmin/new-podman-secrets-command).)

**ANSIBLE COMMUNITY AND MATRIX**

The [Ansible community](https://docs.ansible.com/ansible/latest/community/index.html) has [adopted Matrix](https://github.com/ansible-community/community-topics/issues/36#issuecomment-892890140) as an official place to chat (bridged to IRC). Documentation has been [merged to devel](https://docs.ansible.com/ansible/devel/community/communication.html#ansible-community-on-matrix), and all our rooms have aliases already - you can join [#community:ansible.im](https://matrix.to/#/#community:ansible.im), or add "ansible.im" to your directory search for the whole list (or join [#space:ansible.im](https://matrix.to/#/#space:ansible.im) if you're in the [Matrix Space beta](https://matrix.org/blog/2021/05/17/the-matrix-space-beta)). See you there!

**ANSIBLE GALAXY MAINTENANCE**

There is a planned maintenance for Ansible Galaxy on August 24th at 11:00 UTC, with up to 3 hours of downtime to move galaxy.ansible.com to a new and improved cluster.

**COLLECTION INCLUSION CANDIDATES FOR ANSIBLE 5.0**

We are working towards adding new collections into Ansible 5.0.0, and you can track the progress of the various collections in this [GitHub issue](https://github.com/ansible-community/community-topics/issues/32).

**CONTENT FROM THE ANSIBLE COMMUNITY**

* [Sebastian Gumprich](https://github.com/rndmh3ro) created a first version of [antsichaut](https://github.com/rndmh3ro/antsichaut), a tool that tries to automate the creation of collection changelogs by filling `changelog.yaml` (used by antsibull-changelog) with data from GitHub Pull Requests.
* ara 1.5.7 has been released, and [David Moreau Simard](https://twitter.com/dmsimard) wrote a [blog post](https://ara.recordsansible.org/blog/2021/08/02/announcing-the-release-of-ara-1.5.7/) with the highlights.

**THE ANSIBLE TEAM IS HIRING**

We're looking for Senior Software Engineers to join us as we take the Ansible Automation Platform to the next level and help the world automate solutions for anything and everything you might imagine. Please check the job descriptions in the links and apply!

* [Senior Software Engineer - Ansible](https://global-redhat.icims.com/jobs/86822/senior-software-engineer--ansible/job) - Remote CZ
* [Senior Software Engineer - Ansible](https://global-redhat.icims.com/jobs/88229/senior-software-engineer---ansible/job) - Remote IT
* [Senior Software Engineer - Ansible](https://global-redhat.icims.com/jobs/88230/senior-software-engineer---ansible/job) - Remote ES
* [Senior Software Engineer - Ansible Controller API](https://us-redhat.icims.com/jobs/86519/senior-software-engineer---ansible-controller-api/job) - Remote US NC

In addition, we're also looking for a [Technical Marketing Manager, Ansible Automation](https://us-redhat.icims.com/jobs/88164/senior-product-marketing-manager/job) - worldwide, remote. In this role, you will have significant technical sales enablement responsibilities, including the development of technical content for presentations, demonstrations, videos, e-books, conference talks, and sales tools that will be used by thousands of solutions architects, consultants, and partner presales associates.

**ANSIBLE VIRTUAL MEETUPS**

The following virtual meetup(s) are being held in the Ansible community over the next month:

* Wed, Aug 25 · 10:00 AM SST - [Ansible Singapore](https://www.meetup.com/Ansible-Singapore/events/280143374/) - Red Hat Ansible Automates Virtual Event 2021
* Tue, Aug 31 · 5:30 PM EEST - [Ansible Ireland](https://www.meetup.com/ansible-ireland/events/279464896/) - Ansible Ireland meetup #2

**FEEDBACK**

Have any questions you’d like to ask, or issues you’d like to see covered? Please send us an email at the-bullhorn@redhat.com.

