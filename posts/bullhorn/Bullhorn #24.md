---
title: "Bullhorn #24"
date: 2021-04-15 23:00 UTC
tags: news
category: bullhorn
type: text
---

![Ansible Bullhorn banner](/images/bullhorn-banner-mango.png)

## The Bullhorn

*A Newsletter for the Ansible Developer Community*
*Issue #24, 2021-04-15 ([Past Issues](https://us19.campaign-archive.com/home/?u=56d874e027110e35dea0e03c1&id=d6635f5420))*

Welcome to the Bullhorn, our newsletter for the Ansible developer community. If you have any questions or content you’d like to share, please reach out to us at the-bullhorn@redhat.com, or comment on this [GitHub issue](https://github.com/ansible/community/issues/546).

<!-- TEASER_END -->

**KEY DATES**

* 2021-04-20: mini Docs PR day, 14:00 UTC (details below)
* 2021-04-20: [ETA for Ansible 3.3.0 release](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_3_0.html)
* 2021-04-21: [community IRC meeting](https://github.com/ansible/community/issues/539), 18:00 UTC
* 2021-04-26: Deadline for approval of new collections in Ansible 4
* 2021-04-26: [ETA for ansible-core 2.11 release](https://docs.ansible.com/ansible-core/devel/roadmap/ROADMAP_2_11.html)
* 2021-04-27: [Bullhorn #25 content deadline](https://github.com/ansible/community/issues/546)
* 2021-04-27/28: [Red Hat Summit 2021 Virtual Experience](https://www.redhat.com/en/summit) (free registration)
* 2021-04-28: [community IRC meeting](https://github.com/ansible/community/issues/539), 18:00 UTC
* 2021-04-29: [D&I working group meeting](https://github.com/ansible/community/issues/577), 19:00 UTC
* 2021-05-18: [ETA for Ansible 4.0.0 release](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_4.html)
* [Ansible-core 2.12 Roadmap now available](https://docs.ansible.com/ansible-core/devel/roadmap/ROADMAP_2_12.html)

**ANSIBLE-BASE 2.10.8, ANSIBLE 2.9.20 AND 2.8.20 RELEASED**

The Ansible Core team announced the maintenance releases of Ansible-Base 2.10.8, Ansible 2.9.20, and Ansible 2.8.20 on April 13th.

* Ansible 2.9.20 is the last in the 2.9 series to receive bug fixes. All future releases will be for security fixes only.
* Ansible 2.8 will go EOL (End Of Life) with the release of Ansible 2.8.20 (final release in the 2.8 series).
* The ansible-base package consists of only the Ansible execution engine, related tools (e.g. ansible-galaxy, ansible-test), and a very small set of built-in plugins, and is also bundled with the larger Ansible distribution.

Follow [this link](https://groups.google.com/g/ansible-devel/c/sXx569SuWEY) for Rick Elrod’s email to the ansible-devel mailing list, to obtain details on what’s new, installation instructions, and schedule for future releases.

**ANSIBLE 4.0.0 ALPHA4 RELEASED**

The Ansible Community team announced the fourth alpha release of Ansible 4.0.0 on April 15th. This update is based on the ansible-core-2.11.x package which is a major update from the Ansible 3.x package (which is based on ansible-base-2.10.x). There may be backwards incompatibilities in the core playbook language. Please see the [porting guide](https://docs.ansible.com/ansible/devel/porting_guides/porting_guide_4.html) for details.

The last day for new collections to have been reviewed and approved for Ansible 4.0.0 is April 26th. We have limited volunteers to review the collections so please do not wait until the last minute to respond to any feedback on your submissions!

This is an alpha release. Therefore, there may be more backwards incompatible changes and new features added before Ansible 4.0.0 final is released. For what is included in this release, and how to get it for testing, please see [Toshio Kuratomi’s email to the ansible-devel list](https://groups.google.com/g/ansible-devel/c/jv0_r3kEcWQ).

Ansible 4.0.0 beta1 is scheduled for April 27th.

**MAINTENANCE LIFECYCLE FOR THE ANSIBLE COMMUNITY PACKAGE**

The ``ansible`` package published to PyPI aggregates a selected list of over 85 Ansible collections and pulls in ``ansible-core`` (previously ``ansible-base``) as a dependency.

At the two previous #ansible-community meetings, we have discussed how we might maintain past major releases of the package (such as 3.x once 4.x has shipped) and we have settled on revisiting this later for the time being.

There are benefits to a longer maintenance cycle and while we are open to the idea, it is a non-negligible amount of work without even considering the implications of patching collections that do not backport bug and security fixes.

Maintaining a single major version of the ansible package for six months while providing the ability to install and update collections out-of-band leveraging `ansible-core` and `ansible-galaxy` is likely a good middle ground until the need for a longer maintenance cycle is voiced by the wider community.

Please refer to this [GitHub issue](https://github.com/ansible-community/community-topics/issues/1) if you would like to read more about this or would like to help and get involved.

**NEW/UPDATED COMMUNITY COLLECTIONS**

* Ansible Community VMware Collection - [community.vmware](https://galaxy.ansible.com/community/vmware) 1.9 has been released with security fixes. Please upgrade to the latest version.
* Ansible Collection for ServiceNow ITSM - [servicenow.itsm](https://galaxy.ansible.com/servicenow/itsm) 1.0.0 is a new collection to automate ServiceNow IT Service Management [ITSM](https://www.servicenow.com/products/itsm.html). You can install the new collection with `ansible-galaxy collection install servicenow.itsm`. Please feel free to use and provide feedback.
* Docker Community Collection - [community.docker](https://galaxy.ansible.com/community/docker) 1.5.0 has been released
* Ansible Community Crypto Collection - [community.crypto](https://galaxy.ansible.com/community/crypto) 1.6.1 has been released
* Community General Collection - [community.general](https://galaxy.ansible.com/community/general) 2.5.1 has been released
* MySQL collection for Ansible - [community.mysql](https://galaxy.ansible.com/community/mysql) 2.0.0 has been released
* Community Network Collection - [community.network](https://galaxy.ansible.com/community/network) 2.1.1 has been released

**CHANGES IMPACTING COLLECTION OWNERS**

The [ansible-core repository](https://github.com/ansible/ansible) now includes the `stable-2.11` branch, and the version of the `devel` branch has been bumped to `2.12.0.dev0` ([announcement](https://github.com/ansible-collections/overview/issues/45#issuecomment-813821100)). For collection maintainers, this means that if you have an `tests/sanity/ignore-2.11.txt` file in your collection, it needs to be copied to `tests/sanity/ignore-2.12.txt` to avoid CI crashes. See [this pull request](https://github.com/ansible-collections/cisco.nxos/pull/275) as an example.

In addition, if the collection is included in Ansible, please make sure that CI also tests against the new `stable-2.11` branch. Ansible 4.0.0 will be based on ansible-core 2.11 and thus, according to the [inclusion criteria](https://github.com/ansible-collections/overview/blob/main/collection_requirements.rst), your collection must work with stable-2.11.

See the examples of related pull requests for [GitHub Actions](https://github.com/ansible-collections/community.hrobot/pull/12) and [Azure Pipelines](https://github.com/ansible-collections/community.crypto/pull/214).

We still recommend testing against the `devel` branch as well to be informed early about breaking changes (see the GitHub action workflow [example](https://github.com/ansible-collections/collection_template/blob/main/.github/workflows/ansible-test.yml)).

**UPDATE: ANSIBLE COMMUNITY IRC MEETING**

Previously, all the agenda topics that needed to be discussed in the weekly Ansible Community IRC meetings were added to [this GitHub issue](https://github.com/ansible/community/issues/539). To track and categorize each topic separately, we've created a new ["community-topics" GitHub repository](https://github.com/ansible-community/community-topics/). If you want to discuss an idea, suggest improvements, or submit new policy/proposals and New Collection Inclusion Requests, please create a [new issue](https://github.com/ansible-community/community-topics/issues) in the [repo](https://github.com/ansible-community/community-topics/) as a topic, and it’ll be discussed publicly in the weekly IRC meeting. After every meeting, the meeting minutes/summaries and meeting logs will be posted to the [original issue](https://github.com/ansible/community/issues/539).

**MINI DOCUMENTATION PR DAY**

The Ansible Documentation Working Group (aka DaWGs) will host a mini docs PR day on Tuesday, April 20th at 10am ET/14:00 UTC, lasting four hours. We will review and merge docs PRs for ansible/ansible and any collection-based docs PRs that attendees bring! So come on over to #ansible-docs on Freenode IRC.

**THE ANSIBLE TEAM IS HIRING**

Red Hat is hiring several roles to work on Ansible. Please check the job descriptions in the links and apply!

* [Senior Principal Software Engineer - Ansible Content Architect](https://us-redhat.icims.com/jobs/85283/senior-principal-software-engineer---ansible-content-architect/job)
* [Senior Field Product Manager - Technical](https://us-redhat.icims.com/jobs/82489/senior-product-manager---technical/job)
* [Senior Product Manager - Technical](https://us-redhat.icims.com/jobs/82490/senior-product-manager---technical/job)
* [Principal Product Manager - Technical](https://us-redhat.icims.com/jobs/86158/principal-product-manager---technical/job)
* [Technical Marketing Manager - Red Hat Ansible Automation Platform](https://global-redhat.icims.com/jobs/82487/technical-marketing-manager---red-hat-ansible-automation-platform/job)
* [Technical Marketing Manager](https://us-redhat.icims.com/jobs/82006/technical-marketing-manager/job)

**CONTENT FROM THE ANSIBLE COMMUNITY**

[Daniel](https://github.com/daniel-wtd/) published a [blog post](https://blog.while-true-do.io/ansible-overview/) giving an overview of Ansible including tools and development in the broader ecosystem.

[ara](https://ara.recordsansible.org/) 1.5.6 has been released and features a refresh of the playbook reporting interface included with the API server. [David](https://twitter.com/dmsimard) has written a [blog post](https://ara.recordsansible.org/blog/2021/04/15/announcing-the-release-of-ara-1.5.6/) about it to provide some highlights. 

**ANSIBLE CONTRIBUTOR SUMMIT 2021.06**

The next Ansible Contributor Summit will be held on June 8, 2021. Registration info will be shared shortly, and in the meantime, please propose topics you’d like to discuss in this [HackMD note](https://hackmd.io/@ansible-community/contrib-summit-202106).

**ANSIBLE VIRTUAL MEETUPS**

The following virtual meetup(s) are being held in the Ansible community over the next month:

* Wed, Apr 21 · 6:00 PM GMT+2 - [Ansible in DevOps Torun-Bydgoszcz](https://www.meetup.com/Ansible-in-DevOps-Torun-Bydgoszcz/events/276022444/) - AiDO Meetup #15 Ansible collections

**FEEDBACK**

Have any questions you’d like to ask, or issues you’d like to see covered? Please send us an email at the-bullhorn@redhat.com.
