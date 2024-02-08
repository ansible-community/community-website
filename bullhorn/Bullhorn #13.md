---
title: "Bullhorn #13"
date: 2020-11-04 15:00 UTC
tags: news
category: bullhorn
type: text
---

![Ansible Bullhorn banner](/images/bullhorn-banner-mango.png)

**The Bullhorn**
**Issue #13, 2020-11-04**

Welcome to the Bullhorn, our newsletter for the Ansible developer community. If you have any questions or content you’d like to share, please reach out to us at the-bullhorn@redhat.com, or comment on this [GitHub issue](https://github.com/ansible/community/issues/546).

<!-- TEASER_END -->

**KEY DATES**

* 2020-11-04: [community IRC meeting](https://github.com/ansible/community/issues/539)
* 2020-11-11: [community IRC meeting](https://github.com/ansible/community/issues/539)
* 2020-11-13: [Bullhorn #14 content deadline](https://github.com/ansible/community/issues/546)
* 2020-12-01: ETA for ansible 2.10.3 release
* 2020-12-07: ETA for ansible-base 2.10.4 release
* 2021-02: [tentative schedule for ansible 2.11 release](https://github.com/ansible/ansible/blob/devel/docs/docsite/rst/roadmap/COLLECTIONS_2_11.rst) (subject to change)

**ANSIBLE 2.10.2 NOW GENERALLY AVAILABLE**

The Ansible Community team announced the general availability of Ansible 2.10.2 on November 3rd. This update of the ansible-2.10 package should be a drop-in replacement for Ansible 2.9; the roles and playbooks that you currently use should work out of the box with ansible-2.10.2. For more information on what’s new, how to get it, plus schedule for upcoming releases, read [Toshio Kuratomi’s announcement to the ansible-devel mailing list](https://groups.google.com/forum/#!topic/ansible-devel/SwqsSASkvos).

**ANSIBLE-BASE 2.10.3 NOW GENERALLY AVAILABLE**

The Ansible Base team announced the general release of Ansible 2.10.3 on November 2nd. This ansible-base package consists of only the Ansible execution engine, related tools (e.g. ansible-galaxy, ansible-test), and a very small set of built-in plugins, and is also bundled with the larger Ansible distribution. For more information on how to download, test, and report issues, read [Rick Elrod’s announcement to the ansible-devel mailing list](https://groups.google.com/forum/#!topic/ansible-devel/n8h-Eoh59ds).

**ANSIBLE 2.9.15 AND 2.8.17 RELEASED**

The Ansible Core team announced the availability of Ansible 2.9.15 and Ansible 2.8.17 on November 2nd, both of which are maintenance releases. Follow [this link](https://groups.google.com/forum/#!topic/ansible-devel/N3Mr-PIGaq8) for Rick Elrod’s email to the ansible-devel mailing list, to obtain details on what’s new, installation instructions, and links to the full changelogs.

**NEW/UPDATED COMMUNITY COLLECTIONS**

The [Foreman Ansible Collection](https://galaxy.ansible.com/theforeman/foreman) v1.4.0 was released. Most notable changes include: (1) new modules: [job_invocation](https://theforeman.github.io/foreman-ansible-modules/v1.4.0/plugins/job_invocation_module.html) and [smart_proxy](https://theforeman.github.io/foreman-ansible-modules/v1.4.0/plugins/smart_proxy_module.html), (2) apypie is now vendored, makes installation on EL distributions easier, and (3) [redhat_manifest](https://theforeman.github.io/foreman-ansible-modules/v1.4.0/plugins/redhat_manifest_module.html) supports Simple Content Access. For more details, take a look at this [blog post](https://theforeman.org/2020/10/foreman-ansible-modules-v140-released.html) and the [full changelog](https://theforeman.github.io/foreman-ansible-modules/v1.4.0/CHANGELOG.html#v1-4-0).

The [Community Sops Collection](https://galaxy.ansible.com/community/sops) 0.1.0 has been released. It helps decrpyting and encrypting data with [Mozilla sops](https://github.com/mozilla/sops), which allows the encryption of YAML values (and not keys), and allows the use of multiple keys at once and keys from different sources. If you find ansible-vault too restrictive for your use-case, this might be better suited for you. However, it is a bit harder to use in Ansible, since there are no vault plugins.

The [Ansible Utilities Collection](https://galaxy.ansible.com/ansible/utils) includes a variety of plugins that aid in the management, manipulation and visibility of data for the Ansible playbook developer. It is *currently under active development* and the 1.0.0 version will be released in the first week of December 2020. Contributions to the [collection with PRs and issues](https://github.com/ansible-collections/ansible.utils) are welcomed!

Some content will get moved out of [community.general](https://galaxy.ansible.com/community/general) and [community.network](https://galaxy.ansible.com/community/network) for versions 2.0.0, which will be included in Ansible 2.11. Some of these moves have already been done and initial versions of the new collections have been released. After some testing and once they reach versions 1.0.0, they will be included in Ansible 2.10.

1. [community.postgresql](https://galaxy.ansible.com/community/postgresql) 0.1.0: contains the postgres_* modules from community.general
2. [community.routeros](https://galaxy.ansible.com/community/routeros) 0.1.0: contains the routeros* plugins and modules from community.network
3. [community.docker](https://galaxy.ansible.com/community/docker) 0.1.0: contains the docker* plugins and modules from community.general. Please note that all deprecations planned for removal in community.general 2.0.0 have already been applied. See the [changelog](https://github.com/ansible-collections/community.docker/blob/main/CHANGELOG.rst) for details.

See [here](https://github.com/ansible-collections/overview/discussions/117#discussioncomment-108048) for a detailed description of the content move.

**ANSIBLE CONTRIBUTOR SURVEY**

Last month, on October 12th and 15th, we had Ansible Contributor Summit as part of AnsibleFest 2020. Here is a [Contributor Survey](https://www.surveymonkey.co.uk/r/5DG9VJX) that we have put together. Please take a couple of minutes to fill this in, whether you have attended all/part/none of the event. (Thanks to those who've already done so!)

Feedback is really important to us so we can keep on improving the Contributor Experience for our wonderful Ansible Community.

If you missed the event or want to recap parts from it, the logs, notes and recordings are available in the [Ansible community wiki](https://github.com/ansible/community/wiki/Contributor-Summit#ansible-contributor-summit-10---part-of-ansiblefest-2020-virtual-experience-october-12--15-2020).

**CONTENT FROM THE ANSIBLE COMMUNITY**

ARA [1.5.2](https://github.com/ansible-community/ara/releases/tag/1.5.2) as well as [1.5.3](https://github.com/ansible-community/ara/releases/tag/1.5.3) were released and users are encouraged to update to benefit from significant performance improvements.

[David Moreau-Simard](https://twitter.com/dmsimard) shared data about these improvements in a blog post: [Benchmarking ansible and ara for fun and science](https://ara.recordsansible.org/blog/2020/11/01/benchmarking-ansible-and-ara-for-fun-and-science/).

**ANSIBLE VIRTUAL MEETUPS**

The following virtual meetups are being held in the Ansible community over the next month:

* Wed, Nov 4 · 12:30 PM EST - [Ansible Toronto](https://www.meetup.com/Ansible-Toronto/events/274080932/) - AnsibleFest Recap and Ansible’s new Kubernetes and OpenShift content with Jeff Geerling
* Wed, Nov 4 · 4:00 PM EST - [Ansible NOVA](https://www.meetup.com/Ansible-NOVA/events/273934763/) - Pumpkin Spiced Ansible and...AnsibleFest Recap!
* Tue, Nov 10 · 6:00 PM EST - [Ansible NYC](https://www.meetup.com/Ansible-NYC/events/274372991/) - AnsibleFest Round Up and QA with Tim Appnel
* Fri, Nov 13 · 12:00 PM GMT+13 - [Ansible New Zealand](https://www.meetup.com/Ansible-New-Zealand/events/274246880/) - ANZ Bank Ansible Network Automation: From Lunch Hobby to Production Ready
* Wed, Nov 18 · 5:00 PM GMT+1 - [Ansible in DevOps Torun-Bydgoszcz](https://www.meetup.com/Ansible-in-DevOps-Torun-Bydgoszcz/events/274276840/) - #10 Meeting AiDO Wprowadzenie do Kubernetes -> warsztat

***Note**: For these virtual meetups, the links to participate will be visible once you RSVP to attend. If you’re interested in the topics presented, you can join from anywhere in the world as long as the time zone and language works for you!*

**FEEDBACK**

Have any questions you’d like to ask, or issues you’d like to see covered? Please send us an email at the-bullhorn@redhat.com.
