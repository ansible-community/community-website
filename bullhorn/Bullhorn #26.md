---
title: "Bullhorn #26"
date: 2021-05-13 21:00 UTC
tags: news
category: bullhorn
type: text
---

![Ansible Bullhorn banner](/images/bullhorn-banner-mango.png)

## The Bullhorn

*A Newsletter for the Ansible Developer Community*
*Issue #26, 2021-05-13 ([Past Issues](https://us19.campaign-archive.com/home/?u=56d874e027110e35dea0e03c1&id=d6635f5420))*

Welcome to the Bullhorn, our newsletter for the Ansible developer community. If you have any questions or content you’d like to share, please reach out to us at the-bullhorn@redhat.com, or comment on this [GitHub issue](https://github.com/ansible/community/issues/546).

<!-- TEASER_END -->

**KEY DATES**

* 2021-05-18: [ETA for Ansible 4.0.0 release](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_4.html)
* 2021-05-19: [community IRC meeting](https://github.com/ansible/community/issues/539), 18:00 UTC (propose topics [here](https://github.com/ansible-community/community-topics/issues))
* 2021-05-24: ETA for Ansible-Core 2.11.1 release
* 2021-05-25: [Bullhorn #27 content deadline](https://github.com/ansible/community/issues/546)
* 2021-05-26: [community IRC meeting](https://github.com/ansible/community/issues/539), 18:00 UTC (propose topics [here](https://github.com/ansible-community/community-topics/issues))
* 2021-05-27: [D&I working group meeting](https://github.com/ansible/community/issues/577), 19:00 UTC
* 2021-06-08: [Ansible Contributor Summit 2021.06](https://www.eventbrite.com/e/ansible-contributor-summit-202106-registration-152686374055?aff=bullhorn)
* [Ansible-core 2.12 Roadmap now available](https://docs.ansible.com/ansible-core/devel/roadmap/ROADMAP_2_12.html)

**ANSIBLE 4.0.0 RELEASE CANDIDATE 1**

The Ansible Community team announced the first release candidate of Ansible 4.0.0 on May 11th. This update is based on the Ansible-core-2.11.x package which is a major update from the Ansible 3 package (Ansible 3 was based on Ansible-base-2.10.x). There may be backwards incompatibilities in the core playbook language. Please see the [porting guide](https://docs.ansible.com/ansible/devel/porting_guides/porting_guide_4.html) for details. For what is included in this release, and how to get it for testing, please see [Toshio Kuratomi’s email to the ansible-devel list](https://groups.google.com/g/ansible-devel/c/LnqAU5m4ioU). Unless a blocker bug is found, Ansible 4.0.0 final is scheduled for May 18, 2021.

**ANSIBLE 3.4.0 RELEASED**

The Ansible Community team announced the general availability of Ansible 3.4.0 on May 11th. This update contains bugfixes and new, backwards compatible features in the contained collections. If you would like to learn about how and why we got to version 3.0.0, we invite you to visit our blog for the [background](https://www.ansible.com/blog/announcing-the-community-ansible-3.0.0-package) as well as a [Q&A](https://www.ansible.com/blog/ansible-3.0.0-qa). For what's new in the release and how to install it, please see [Toshio Kuratomi's email to the ansible-announce list](https://groups.google.com/g/ansible-announce/c/UfVpNNkpRuA). Barring unforeseen issues, this will be the last Ansible 3 release.

**ANSIBLE-BASE 2.10.9 AND ANSIBLE 2.9.21 RELEASED**

The Ansible Core team announced the maintenance releases of Ansible-Base 2.10.9 and Ansible 2.9.21 on May 3rd. Follow [this link](https://groups.google.com/g/ansible-devel/c/6xlHakDA9Gs) for Rick Elrod’s email to the ansible-devel mailing list, to obtain details on what’s new, installation instructions, and schedule for future releases.

**NEW/UPDATED COMMUNITY COLLECTIONS**

* IBM Z System Automation collection - [ibm.ibm_zos_sysauto](https://galaxy.ansible.com/ibm/ibm_zos_sysauto) 1.0.0 has been released.
* PostgreSQL collection for Ansible - [community.postgresql](https://galaxy.ansible.com/community/postgresql) 1.3.0 has been released.
* Ansible Community VMware Collection - [community.vmware](https://galaxy.ansible.com/community/vmware) [1.10.0](https://github.com/ansible-collections/community.vmware/pull/830) has been released. Please update for new features and bug fixes.
* Community DNS Collection - [community.dns](https://galaxy.ansible.com/community/dns) 1.0.0 has been released. The collection provides some DNS-related filter plugins and modules.
* TrendMicro DeepSecurity Ansible Collection - [trendmicro.deepsec](https://galaxy.ansible.com/trendmicro/deepsec) [1.0.0](https://github.com/ansible-collections/trendmicro.deepsec/pull/15) has been released. This collection includes a variety of Ansible content to help automate the management of TrendMicro DeepSecurity Endpoint Security solutions. Please check out the collection and update for new feature and bug fixes.
* Community General Collection - [community.general](https://galaxy.ansible.com/community/general) 2.5.2 has been released for inclusion in Ansible 3.4.0.
* Community General Collection - [community.general](https://galaxy.ansible.com/community/general) 3.0.2 has been released for inclusion in Ansible 4.0.0 RC1.
* Docker Community Collection - [community.docker](https://galaxy.ansible.com/community/docker) 1.6.0 has been released.

**CHANGES IMPACTING COLLECTION OWNERS**

* Ansible Changelog Tool - [antsibull-changelog](https://github.com/ansible-community/antsibull-changelog/) [0.10.0](https://github.com/ansible-community/antsibull-changelog/blob/main/CHANGELOG.rst#v0-10-0) has been released.
* [Update testing to use Fedora 34](https://github.com/ansible-collections/overview/issues/45#issuecomment-830220740) - Fedora 34 has been added to `ansible-test` on the `devel` branch.
* [Testing with Python 3.10](https://github.com/ansible-collections/overview/issues/45#issuecomment-836847770) - Python 3.10 is now supported by the `devel` branch version of `ansible-test`.
* For more details of each of the above, and to stay on top of these changes, please subscribe to the [issue on GitHub](https://github.com/ansible-collections/overview/issues/45).

**PROPOSAL: ANSIBLE COMMUNITY GALAXY NEXT STEPS**

We're updating galaxy.ansible.com to use GalaxyNG, the code that powers Ansible Automation Hub, because it is well maintained and efficient. Help us make sure your use cases are addressed in this transition! Please take a look at this [post on Reddit](https://www.reddit.com/r/ansible/comments/na4end/ansible_community_galaxy_next_steps_help_needed/) for the details, and ways you can help and provide feedback.

**FEEDBACK: ADD ACTION_GROUPS SUPPORT TO COLLECTIONS**

In ansible-core 2.12, collections will be able to define new groups to use with `module_defaults`. [Here](https://gist.github.com/s-hertel/725ecc719b5301e76c571aca58d39bd3) is a summary of the evolution of the feature. [Feedback](https://github.com/ansible/ansible/pull/74039) is welcome!

**FEEDBACK: UBUNTU PPA**

We are currently in the testing phase of our new GitHub Action PPA process. This testing includes Ansible `2.8.20` and `2.9.21` for Ubuntu `18.04`, as well as Ansible `2.10.7`, `3.4.0`, and `4.0.0rc1` for Ubuntu `18.04`, `20.04`, `20.10`, and `21.04`. If you are interested in testing or checking out the new process please see [this GitHub issue](https://github.com/ansible-community/ppa/issues/1) for more details.

**ANSIBLE CONTRIBUTOR SUMMIT 2021.06**

The next Ansible Contributor Summit will be held on Tuesday, June 8, 2021. Please see the details and register on [Eventbrite](https://www.eventbrite.com/e/ansible-contributor-summit-202106-registration-152686374055?aff=bullhorn), and propose topics you’d like to discuss in this [HackMD note](https://hackmd.io/@ansible-community/contrib-summit-202106).

**PYCON US 2021**

A few of us from the Ansible team will be at [PyCon US 2021](https://us.pycon.org/2021/). Come chat with us this Friday, May 14th 12-5:30pm EDT at the Red Hat booth. Talent scouts from Red Hat will be at the PyCon Job Fair on Sunday, May 16th 1-3pm EDT.

**CONTENT FROM THE ANSIBLE COMMUNITY**

Find out how the Ansible project is working to eliminate racism and other harmful prejudices from the project's code and community with this [great post](https://opensource.com/article/21/5/inclusive-language-ansible) by [Jill Rouleau](https://github.com/jillr).

**ANSIBLE VIRTUAL MEETUPS**

The following virtual meetup(s) are being held in the Ansible community over the next month:

* Fri, May 14 · 16:00 UTC - [CentOS Dojo](https://wiki.centos.org/Events/Dojo/May2021) - "Keeping track of CentOS infrastructure deployments with Ansible and ARA" by [David Moreau-Simard](https://twitter.com/dmsimard) and [Fabian Arrotin](https://twitter.com/Arrfab)
* Tue, May 18 · 11:00 AM GMT+2 - [Ansible Anwendertreffen](https://www.ansible-anwender.de/post/2021/04/register/) (in German)
* Tue, May 25 · 6:00 PM GMT+1 - [Ansible London](https://www.meetup.com/Ansible-London/events/278093392/) - Virtual meetup 25th May 2021

**THE ANSIBLE TEAM IS HIRING**

Red Hat is hiring several roles to work on Ansible. Please check the job descriptions in the links and apply!

* [DevOps Automation Engineer - Red Hat Ansible](https://global-redhat.icims.com/jobs/82487/devops-automation-engineer---red-hat-ansible/job)
* [Senior Field Product Manager - Technical](https://us-redhat.icims.com/jobs/82489/senior-product-manager---technical/job)
* [Senior Product Manager - Technical](https://us-redhat.icims.com/jobs/82490/senior-product-manager---technical/job)
* [Principal Product Manager - Technical](https://us-redhat.icims.com/jobs/86158/principal-product-manager---technical/job)

**FEEDBACK**

Have any questions you’d like to ask, or issues you’d like to see covered? Please send us an email at the-bullhorn@redhat.com.
