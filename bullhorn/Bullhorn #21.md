---
title: "Bullhorn #21"
date: 2021-03-05 17:15 UTC
tags: news
category: bullhorn
type: text
---

![Ansible Bullhorn banner](/images/bullhorn-banner-mango.png)

## The Bullhorn

*A Newsletter for the Ansible Developer Community*
*Issue #21, 2021-03-05 ([Past Issues](https://us19.campaign-archive.com/home/?u=56d874e027110e35dea0e03c1&id=d6635f5420))*

Welcome to the Bullhorn, our newsletter for the Ansible developer community. If you have any questions or content you’d like to share, please reach out to us at the-bullhorn@redhat.com, or comment on this [GitHub issue](https://github.com/ansible/community/issues/546).

<!-- TEASER_END -->

**KEY DATES**

* 2021-03-09: [Ansible Contributor Summit 2021.03](https://www.eventbrite.com/e/ansible-contributor-summit-202103-registration-141735886853?aff=bullhorn), 12:00 UTC (more info below)
* 2021-03-09: [ETA for Ansible 3.1.0 release](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_3_0.html)
* 2021-03-10: Hackathon/PR Day in #ansible-community, 12:00 UTC
* 2021-03-16: [Bullhorn #22 content deadline](https://github.com/ansible/community/issues/546)
* 2021-03-17: [community IRC meeting](https://github.com/ansible/community/issues/539), 19:00 UTC
* 2021-03-18: [D&I working group meeting](https://github.com/ansible/community/issues/577), 19:00 UTC
* 2021-03-29: [ETA for ansible-core 2.11 release candidate](https://github.com/ansible/ansible/blob/devel/docs/docsite/rst/roadmap/ROADMAP_2_11.rst)
* 2021-05-18: ETA for Ansible 4.0.0 general release (more info below)

**ANSIBLE 4.0.0 ROADMAP AND DATES**

* 2021-04-13: Last day for new collections to be [submitted for inclusion in Ansible 4](https://github.com/ansible-collections/ansible-inclusion/discussions/). Note that collections MUST be reviewed and approved before being included. There is no guarantee that we will review every collection. The earlier your collection is submitted, the more likely it will be that your collection will be reviewed and the necessary feedback can be addressed in time for inclusion.
* 2021-04-26: Last day for collections to make backwards incompatible releases that will be accepted into Ansible 4.
* 2021-04-27: Ansible-4.0.0 beta1 – feature freeze 1 (weekly beta releases. Collection owners and interested users should test for bugs).
* 2021-05-18: Ansible-4.0.0 general release.

For the full Ansible 4.0.0 schedule please see the [Ansible 4.0.0 roadmap](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_4.html).

**ANSIBLE-BASE 2.10.6 NOW GENERALLY AVAILABLE**

The Ansible Core team announced the general release of Ansible-Base 2.10.6 on February 19th. This ansible-base package consists of only the Ansible execution engine, related tools (e.g. ansible-galaxy, ansible-test), and a very small set of built-in plugins, and is also bundled with the larger Ansible distribution. For more information on what's new, how to download, and report issues, read [Rick Elrod’s announcement to the ansible-devel mailing list](https://groups.google.com/g/ansible-devel/c/QzKCxTIWbYQ).

**ANSIBLE 2.9.18 AND 2.8.19 RELEASED**

The Ansible Core team announced the availability of Ansible 2.9.18 and Ansible 2.8.19 on February 19th, both of which are maintenance releases. Follow [this link](https://groups.google.com/g/ansible-devel/c/BjUj4PB8C_s) for Rick Elrod’s email to the ansible-devel mailing list, to obtain details on what’s new, installation instructions, and links to the full changelogs.

**CHANGES IMPACTING COLLECTION OWNERS**

**Breaking change:** Vendored `ipaddress` in `ansible.netcommon` 2.0.0 has been removed. In case your collection uses the vendored `ipaddress` module from ansible.netcommon, either directly (`import ansible_collections.ansible.netcommon.plugins.module_utils.compat.ipaddress`) or indirectly (`import ansible.module_utils.compat.ipaddress`, see [ansible-core's module_utils routing](https://github.com/ansible/ansible/blob/78d3810fdf7c579be5d9be8412844ae79d3f313b/lib/ansible/config/ansible_builtin_runtime.yml#L7618-L7619)): it has been **removed** from ansible.netcommon 2.0.0 (released 3 days ago) and these imports will no longer work! Check out [how to update your code](https://github.com/ansible-collections/overview/issues/45#issuecomment-791194436).

In your `galaxy.yml` we strongly suggest you pin to major versions to avoid accidentally bringing in breaking changes, i.e.:
```yaml=
dependencies:
  "ansible.netcommon": ">=2.0.0,<3.0.0"
```

`ansible.netcommon` 2.0.0 also removes deprecated connection arguments from netconf_config. See the [changelog](https://github.com/ansible-collections/ansible.netcommon/blob/main/changelogs/CHANGELOG.rst#v2-0-0).

As always, please subscribe to [Changes impacting collection owners](https://github.com/ansible-collections/overview/issues/45) to be informed about changes as soon as they happen.

**NEW/UPDATED COMMUNITY COLLECTIONS**

The [Community HashiVault Collection](https://galaxy.ansible.com/community/hashi_vault) [community.hashi_vault](https://github.com/ansible-collections/community.hashi_vault) 1.1.1 was released on 2021-02-24 ([changelog](https://github.com/ansible-collections/community.hashi_vault/blob/main/CHANGELOG.rst#v1-1-1)).

The [Foreman Ansible Collection](https://galaxy.ansible.com/theforeman/foreman) v2.0.0 was released ([full changelog](https://theforeman.github.io/foreman-ansible-modules/v2.0.0/CHANGELOG.html#v2-0-0)). Most notable changes include:
- new modules: [host_info](https://theforeman.github.io/foreman-ansible-modules/v2.0.0/plugins/host_info_module.html#ansible-collections-theforeman-foreman-host-info-module), [repository_info](https://theforeman.github.io/foreman-ansible-modules/v2.0.0/plugins/repository_info_module.html#ansible-collections-theforeman-foreman-repository-info-module) and [puppetclasses_import](https://theforeman.github.io/foreman-ansible-modules/v2.0.0/plugins/puppetclasses_import_module.html#ansible-collections-theforeman-foreman-puppetclasses-import-module)
- new roles: activation_keys, lifecycle_environments, repositories, sync_plans
- host module can now look up the correct network id for a network given as part of interfaces_attributes

Breaking changes:
- All role variables are now prefixed with `foreman_` to avoid clashes with similarly named variables from roles outside this collection.

**REQUEST FOR FEEDBACK - ANSIBLE NETWORKING**

The Ansible Networking team would like to gather feedback from the network community on how to improve the behaviour of network config module warning messages. Please add your comments in this [discussion on GitHub](https://github.com/ansible/network/discussions/48).

**DIVERSITY AND INCLUSION WG SEEKING EXPERIENCE IN ACCESSIBLE DESIGN**

The Ansible [Diversity and Inclusion](https://github.com/ansible/community/wiki/Diversity) Working Group is seeking members of the community with experience in accessible design or use of assistive technologies to help identify areas for improvement and implement changes to our online media (documentation, GitHub templates and forms, etc). Please reach out to the group on [Freenode IRC in channel #ansible-diversity](https://webchat.freenode.net/#ansible-diversity) if you would like to participate.

**CONTENT FROM THE ANSIBLE COMMUNITY**

* At [FOSDEM 2021](https://fosdem.org/2021/), [Evgeni Golov](https://twitter.com/zhenech) gave a talk titled "your management layer should be cattle too". [Video, slides and further links are available on the FOSDEM talk page](https://fosdem.org/2021/schedule/event/yourmanagementlayershouldbecattletoo/).
* [Ansible: Assign Tag to object in vCenter](https://medium.com/@AbhijeetKasurde/ansible-assign-tag-to-object-in-vcenter-b23382371cf8) by [Abhijeet Kasurde](https://github.com/Akasurde)
* [Ansible - Release 3.0.0](https://blog.while-true-do.io/ansible-release-3-0-0/) by [Daniel Schier](https://github.com/daniel-wtd)
* [Ansible: Using ‘virtualbox’ inventory plugin](https://medium.com/@AbhijeetKasurde/ansible-using-virtualbox-inventory-plugin-222cc0becfc6) by [Abhijeet Kasurde](https://github.com/Akasurde)

**ANSIBLE CONTRIBUTOR SUMMIT 2021.03**

The next Ansible Contributor Summit will be held on **Tuesday, March 9, from [12:00-20:00 UTC](https://www.timeanddate.com/worldclock/fixedtime.html?msg=Ansible+Contributor+Summit+2021.03&iso=20210309T12)**. Please see the details and register on [Eventbrite](https://www.eventbrite.com/e/ansible-contributor-summit-202103-registration-141735886853?aff=bullhorn), and check out the agenda and participation links in this [HackMD note](https://hackmd.io/@ansible-community/contrib-summit-202103).

We will follow up on Wednesday, March 10, with a Hackathon/PR day from 12:00 UTC. This will take place on [Freenode IRC in channel #ansible-community](https://webchat.freenode.net/#ansible-community).

**ANSIBLE VIRTUAL MEETUPS**

The following virtual meetups are being held in the Ansible community over the next month:

* Wed, Mar 17 · 6:00 PM GMT+1 - [Ansible Meetup Dresden](https://www.meetup.com/Ansible-Meetup-Dresden/events/276690420/) - Meetup 03.2021
* Thu, Mar 18 · 3:00 PM EDT - [Ansible Québec](https://www.meetup.com/Ansible-Quebec/events/276567692/) and [Ansible Montréal](https://www.meetup.com/Ansible-Montreal/events/276525794/) - Rencontre Mars 2021

**FEEDBACK**

Have any questions you’d like to ask, or issues you’d like to see covered? Please send us an email at the-bullhorn@redhat.com.
