---
title: "Bullhorn #25"
date: 2021-04-30 17:00 UTC
tags: news
category: bullhorn
type: text
---

![Ansible Bullhorn banner](/images/bullhorn-banner-mango.png)

## The Bullhorn

*A Newsletter for the Ansible Developer Community*
*Issue #25, 2021-04-30 ([Past Issues](https://us19.campaign-archive.com/home/?u=56d874e027110e35dea0e03c1&id=d6635f5420))*

Welcome to the Bullhorn, our newsletter for the Ansible developer community. If you have any questions or content you’d like to share, please reach out to us at the-bullhorn@redhat.com, or comment on this [GitHub issue](https://github.com/ansible/community/issues/546).

<!-- TEASER_END -->

**KEY DATES**

* 2021-05-05: [community IRC meeting](https://github.com/ansible/community/issues/539), 18:00 UTC
* 2021-05-11: [ETA for Ansible 3.4.0 release](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_3_0.html)
* 2021-05-11: [Bullhorn #26 content deadline](https://github.com/ansible/community/issues/546)
* 2021-05-12: [community IRC meeting](https://github.com/ansible/community/issues/539), 18:00 UTC
* 2021-05-13: [D&I working group meeting](https://github.com/ansible/community/issues/577), 19:00 UTC
* 2021-05-18: [ETA for Ansible 4.0.0 release](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_4.html)
* 2021-06-08: [Ansible Contributor Summit 2021.06](https://www.eventbrite.com/e/ansible-contributor-summit-202106-registration-152686374055?aff=bullhorn)
* [Ansible-core 2.12 Roadmap now available](https://docs.ansible.com/ansible-core/devel/roadmap/ROADMAP_2_12.html)

**ANSIBLE 3.3.0 RELEASED**

The Ansible Community team announced the general availability of Ansible 3.3.0 on April 22nd. This update contains bugfixes and new, backwards compatible features in the contained collections. If you would like to learn about how and why we got to version 3.0.0, we invite you to visit our blog for the [background](https://www.ansible.com/blog/announcing-the-community-ansible-3.0.0-package) as well as a [Q&A](https://www.ansible.com/blog/ansible-3.0.0-qa). For what's new in the release and how to install it, please see [Toshio Kuratomi's email to the ansible-announce list](https://groups.google.com/g/ansible-announce/c/WS77GFbqitk).

**ANSIBLE-CORE 2.11.0 RELEASED**

The Ansible Core team announced the general availability of Ansible-Core 2.11.0 on April 26th. Ansible-core 2.11 is a rename of ansible-base. As with ansible-base, it includes only a minimal, vetted set of modules and plugins, and is extensible through the use of Ansible Collections. Follow [this link](https://groups.google.com/g/ansible-devel/c/vgzZj3e624g) for Rick Elrod’s email to the ansible-devel mailing list, to obtain details on what’s new, installation instructions, and schedule for future releases.

**ANSIBLE 4.0.0 BETA1 RELEASED**

The Ansible Community team announced the first beta release of Ansible 4.0.0 on April 29th. This update is based on the ansible-core-2.11.x package which is a major update from the Ansible 3.x package (which is based on ansible-base-2.10.x). There may be backwards incompatibilities in the core playbook language. Please see the [porting guide](https://docs.ansible.com/ansible/devel/porting_guides/porting_guide_4.html) for details. For what is included in this release, and how to get it for testing, please see [Toshio Kuratomi’s email to the ansible-devel list](https://groups.google.com/g/ansible-devel/c/v4ObPeDkdDg). Unless a blocker bug is found, Ansible 4.0.0 final is scheduled for May 18, 2021.

**NEW/UPDATED COMMUNITY COLLECTIONS**

* Openstack Cloud Collection - [openstack.cloud](https://galaxy.ansible.com/openstack/cloud) [1.4.0](https://github.com/openstack/ansible-collections-openstack/blob/master/CHANGELOG.rst#v1-4-0) has been released, with a few bugfixes including IPv6 functionality, and a new [object_container](https://github.com/openstack/ansible-collections-openstack/blob/master/plugins/modules/object_container.py) module for the management of Swift containers.
* Ansible Podman Collection - [containers.podman](https://galaxy.ansible.com/containers/podman) [1.5.0](https://github.com/containers/ansible-podman-collections/blob/master/CHANGELOG.rst#v1-5-0) has been released, with a lot of bugfixes since the 1.4.0 version, including full support of recent Podman v3 release, Podman networking and new [podman_login](https://github.com/containers/ansible-podman-collections/blob/master/plugins/modules/podman_login.py) module for login to container registries using Podman.
* Internal Test Tools Collection - [community.internal_test_tools](https://galaxy.ansible.com/community/internal_test_tools) 0.4.0 has been released with more features, some bugfixes and refactorings for the `open_url`/`fetch_url` test frameworks.
* MySQL collection for Ansible - [community.mysql](https://galaxy.ansible.com/community/mysql) 2.1.0 and 1.4.1 have been released.
* Community General Collection - [community.general](https://galaxy.ansible.com/community/general) 3.0.0 and 1.3.10 have been released. 1.3.10 is the last regular bugfix release from the stable-1 branch.
* Amazon AWS Collection - [amazon.aws](https://galaxy.ansible.com/amazon/aws) [1.5.0](https://github.com/ansible-collections/amazon.aws/blob/stable-1.5/CHANGELOG.rst) and Community AWS Collection - [community.aws](https://galaxy.ansible.com/community/aws) [1.5.0](https://github.com/ansible-collections/community.aws/blob/stable-1.5/CHANGELOG.rst) have been released, and stable-1.5 have been branched for both collections.
  * The next releases of these  collections, 2.0, will drop support for Python 2.7 in advance of AWS' [end of Python2 support](https://aws.amazon.com/blogs/developer/announcing-end-of-support-for-python-2-7-in-aws-sdk-for-python-and-aws-cli-v1/) on July 15, 2021.

**CHANGES IMPACTING COLLECTION OWNERS**

* Ansible Changelog Tool - [antsibull-changelog](https://github.com/ansible-community/antsibull-changelog/) [0.10.0](https://github.com/ansible-community/antsibull-changelog/blob/main/CHANGELOG.rst#v0-10-0) has been released
* [FreeBSD 13.0 now available for testing on `devel` branch](https://github.com/ansible-collections/overview/issues/45#issuecomment-824337164)
* [ansible-test Sanity Tests Require Python 3.8+](https://github.com/ansible-collections/overview/issues/45#issuecomment-825453639)
* [ansible-test Collection Configuration](https://github.com/ansible-collections/overview/issues/45#issuecomment-827853900)
* [Codecov bash uploader now hosted in S3](https://github.com/ansible-collections/overview/issues/45#issuecomment-829350163)
* For more details of each of the above, and to stay on top of these changes, please subscribe to the [issue on GitHub](https://github.com/ansible-collections/overview/issues/45)

**THE ANSIBLE TEAM IS HIRING**

Red Hat is hiring several roles to work on Ansible. Please check the job descriptions in the links and apply!

* [DevOps Automation Engineer - Red Hat Ansible](https://global-redhat.icims.com/jobs/82487/devops-automation-engineer---red-hat-ansible/job)
* [Senior Principal Software Engineer - Ansible Content Architect](https://us-redhat.icims.com/jobs/85283/senior-principal-software-engineer---ansible-content-architect/job)
* [Senior Field Product Manager - Technical](https://us-redhat.icims.com/jobs/82489/senior-product-manager---technical/job)
* [Senior Product Manager - Technical](https://us-redhat.icims.com/jobs/82490/senior-product-manager---technical/job)
* [Principal Product Manager - Technical](https://us-redhat.icims.com/jobs/86158/principal-product-manager---technical/job)
* [Technical Marketing Manager](https://us-redhat.icims.com/jobs/82006/technical-marketing-manager/job)

**CONTENT FROM THE ANSIBLE COMMUNITY**

* [Jacobo Nájera](https://twitter.com/jacobonajera) wrote an [article about Ansible collections](https://www.jacobo.org/colecciones-de-ansible/) (in Spanish).
* [William Clark](https://github.com/wbclark) has been working on an Ansible role for automating the synchronization and serving of RHEL content in Foreman/Katello. Here's a [blog post](https://theforeman.org/2021/04/configuring-katello-via-ansible-to-synchronize-and-serve-rhel-content.html) where you can read more about it and watch the demo.

**ANSIBLE CONTRIBUTOR SUMMIT 2021.06**

The next Ansible Contributor Summit will be held on Tuesday, June 8, 2021. Please see the details and register on [Eventbrite](https://www.eventbrite.com/e/ansible-contributor-summit-202106-registration-152686374055?aff=bullhorn), and propose topics you’d like to discuss in this [HackMD note](https://hackmd.io/@ansible-community/contrib-summit-202106).

**ANSIBLE VIRTUAL MEETUPS**

The following virtual meetup(s) are being held in the Ansible community over the next month:

* Tue, May 11 · 6:30 PM GMT+2 - [Linux-Stammtisch München](https://www.meetup.com/Linux-Stammtisch-Munchen/events/277897862/) - Online Linux-Stammtisch: All eyes on Ansible
* Fri, May 14 · 16:00 UTC - [CentOS Dojo](https://wiki.centos.org/Events/Dojo/May2021) - "Keeping track of CentOS infrastructure deployments with Ansible and ARA" by [David Moreau-Simard](https://twitter.com/dmsimard) and [Fabian Arrotin](https://twitter.com/Arrfab)
* Tue, May 18 · 11:00 AM GMT+2 - [Ansible Anwendertreffen](https://www.ansible-anwender.de/post/2021/04/register/) (in German)

**FEEDBACK**

Have any questions you’d like to ask, or issues you’d like to see covered? Please send us an email at the-bullhorn@redhat.com.
