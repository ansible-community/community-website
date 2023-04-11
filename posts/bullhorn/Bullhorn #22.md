---
title: "Bullhorn #22"
date: 2021-03-18 21:00 UTC
tags: news
category: bullhorn
type: text
---

![Ansible Bullhorn banner](/images/bullhorn-banner-mango.png)

## The Bullhorn

*A Newsletter for the Ansible Developer Community*
*Issue #22, 2021-03-18 ([Past Issues](https://us19.campaign-archive.com/home/?u=56d874e027110e35dea0e03c1&id=d6635f5420))*

Welcome to the Bullhorn, our newsletter for the Ansible developer community. If you have any questions or content you’d like to share, please reach out to us at the-bullhorn@redhat.com, or comment on this [GitHub issue](https://github.com/ansible/community/issues/546).

<!-- TEASER_END -->

**KEY DATES**

* 2021-03-24: [Collection Inclusion review day](https://github.com/ansible-collections/ansible-inclusion/discussions), 13:00 UTC
* 2021-03-24: [community IRC meeting](https://github.com/ansible/community/issues/539), 19:00 UTC
* 2021-03-30: [ETA for Ansible 3.2.0 release](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_3_0.html)
* 2021-03-30: [Bullhorn #23 content deadline](https://github.com/ansible/community/issues/546)
* 2021-03-31: [community IRC meeting](https://github.com/ansible/community/issues/539), 19:00 UTC
* 2021-04-01: [D&I working group meeting](https://github.com/ansible/community/issues/577), 19:00 UTC
* 2021-04-13: Last day for new collections to be [submitted for inclusion in Ansible 4](https://github.com/ansible-collections/ansible-inclusion/discussions/). Note that collections MUST be reviewed and approved before being included.
* 2021-04-26: [ETA for ansible-core 2.11 release](https://github.com/ansible/ansible/blob/devel/docs/docsite/rst/roadmap/ROADMAP_2_11.rst)
* 2021-05-18: [ETA for Ansible 4.0.0 release](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_4.html)

**ANSIBLE 3.1.0 RELEASED**

The Ansible Community team announced the general availability of Ansible 3.1.0 on March 11th. This update contains bugfixes and new, backwards compatible features in the contained collections. If you would like to learn about how and why we got to version 3.0.0, we invite you to visit our blog for the [background](https://www.ansible.com/blog/announcing-the-community-ansible-3.0.0-package) as well as a [Q&A](https://www.ansible.com/blog/ansible-3.0.0-qa). For what's new in the release and how to install it, please see [Toshio Kuratomi's email to the ansible-announce list](https://groups.google.com/g/ansible-announce/c/cU4WVtab80o).

**ANSIBLE 4.0.0 ALPHA1 RELEASED**

The Ansible Community team announced the first alpha release of Ansible 4.0.0 on March 16th. This update is based on the ansible-core-2.11.x package which is a major update from the Ansible 3.x package (which is based on ansible-base-2.10.x). There may be backwards incompatibilities in the core playbook language. Please see the [porting guide](https://docs.ansible.com/ansible/devel/porting_guides/porting_guide_4.html) for details.

This is an alpha release. Therefore, there may be more backwards incompatible changes and new features added before Ansible 4.0.0 final is released. For what is included in this release, and how to get it for testing, please see [Toshio Kuratomi's email to the ansible-devel list](https://groups.google.com/g/ansible-devel/c/rtwXoKrIQG0).

**UPCOMING ANSIBLE 2.8, ANSIBLE 2.9, ANSIBLE-BASE, ANSIBLE-CORE SCHEDULE**

The Ansible Core team shared the plan for Ansible releases prior to 2.10, and the next few ansible-base and ansible-core releases.

On 26 April 2021, several things are slated to happen:
* ansible-core 2.11.0 will see a general availability release
* ansible 2.8.z will be considered End Of Life and will no longer see updates
* ansible 2.9.z will drop to security-only releases

For more detailed dates of specific releases, please take a look at [Rick Elrod's email to the ansible-devel mailing list](https://groups.google.com/g/ansible-devel/c/udlVP0236zw).

**NEW/UPDATED COMMUNITY COLLECTIONS**

* Kubernetes Collection for Ansible - [kubernetes.core](https://galaxy.ansible.com/kubernetes/core) 1.2.0 is now out. This release introduces a `helm_template` module, dependent deletions and more reliable idempotency checks in addition to logic to handle the breaking changes in the Kubernetes client version 12 library and other incremental fixes and improvements.
* Ansible Community Crypto Collection - [community.crypto](https://galaxy.ansible.com/community/crypto) 1.5.0 has been released (new features and bugfixes).
* Docker Community Collection - [community.docker](https://galaxy.ansible.com/community/docker) 1.4.0 has been released (new features, modules, and bugfixes).
* Community Sops Collection - [community.sops](https://galaxy.ansible.com/community/sops) 1.0.5 has been released (bugfixes).
* Ansible POSIX Collection - [ansible.posix](https://galaxy.ansible.com/ansible/posix) 1.2.0 has been released (minor changes and bugfixes).
* MySQL collection for Ansible - [community.mysql](https://galaxy.ansible.com/community/mysql) 1.3.0 has been released (minor changes, important deprecation announcements, and bugfixes).
* Icinga Director Collection for Ansible - [t_systems_mms.icinga_director](https://galaxy.ansible.com/t_systems_mms/icinga_director) 1.16.0 has been released with a new module (usergroup) and various other improvements.

**INTRODUCING ANSIBLE COMMUNITY STEERING COMMITTEE**

* Last week, at the Ansible Contributor Summit, we [introduced the Ansible Community Steering Committee](https://groups.google.com/g/ansible-devel/c/FRbn4qT3Jf0).
* From next week's [Ansible Community meeting](https://github.com/ansible/community/issues/539) (2021-03-24), we will officially kick start the Steering Committee.
* For further information about the Steering Committee, see ["Ansible Community Steering Committee"](https://hackmd.io/@ansible-community/steering-committee).

**ANSIBLE CONTRIBUTOR SUMMIT 2021.03 RECAP AND SURVEY**

[Ansible Contributor Summit 2021.03](https://hackmd.io/@ansible-community/contrib-summit-202103) was held last Tuesday (March 9, 2021). Here is a [Contributor Survey](https://www.surveymonkey.co.uk/r/SGNJZHV) that we have put together. If you missed the event or want to recap parts from it, the logs, presentations, and recordings are available in the [Ansible Community wiki](https://github.com/ansible/community/wiki/Contributor-Summit).

Please take a couple of minutes to fill in the [survey](https://www.surveymonkey.co.uk/r/SGNJZHV), whether you have attended all/part/none of the event. Feedback is really important to us so we can keep on improving the Contributor Experience for our wonderful Ansible Community.

[Daniel Schier](https://twitter.com/daniel_wtd) from the community did a [great write-up](https://blog.while-true-do.io/ansible-contributor-summit-2021/) of the event. Thanks!

**ANSIBLE DOCSITE SPLIT COMPLETED**

With the release of Ansible 3, we had a need to track two different releases, Ansible and ansible-core. To achieve this, we now have:

* [Ansible Documentation](https://docs.ansible.com/ansible/latest/index.html) - This docsite now tracks Ansible (the package).
* [Ansible Core Documentation](https://docs.ansible.com/ansible-core/devel/) - This docsite now tracks ansible-core (and ansible-base).
 
To clarify, **Ansible Documentation** includes everything, with the exception of core porting guides (which are included in the [Ansible core porting guides](https://docs.ansible.com/ansible-core/devel/porting_guides/core_porting_guides.html)) and core roadmaps.
 
The **Ansible Core Documentation** includes only core features. Scenario guides, network guides, and Ansible porting guides/roadmaps are not on ansible-core.

**THE ANSIBLE TEAM IS HIRING**

Red Hat is hiring several roles to work on Ansible. Please check the job descriptions in the links and apply!
* [Manager, Ansible Cloud Engineering](https://us-redhat.icims.com/jobs/82347/manager%2c-ansible-cloud-engineering/job)
* [Technical Marketing Manager - Red Hat Ansible Automation Platform](https://global-redhat.icims.com/jobs/82487/technical-marketing-manager---red-hat-ansible-automation-platform/job)

**CONNECT WITH THE ANSIBLE COMMUNITY**

The Ansible community is growing and there are new ways for you to stay in touch, the [Ansible Discord server](https://discord.gg/DRmN7ubwud) is a passionate community of Ansible users ready to help you troubleshoot your Ansible projects via text, voice or screen-sharing. 

Come join us on the [Ansible Discord server](https://discord.gg/DRmN7ubwud).

**ANSIBLE VIRTUAL MEETUPS**

The following virtual meetup(s) are being held in the Ansible community over the next month:

* Thu, Mar 25 · 4:00 PM EDT - [Ansible NOVA](https://www.meetup.com/Ansible-NOVA/events/276995149/) - From Ansible to Anchore: With Ansible founder, Saïd Ziouani

**FEEDBACK**

Have any questions you’d like to ask, or issues you’d like to see covered? Please send us an email at the-bullhorn@redhat.com.
