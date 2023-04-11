---
title: "Bullhorn #27"
date: 2021-05-27 23:00 UTC
tags: news
category: bullhorn
type: text
---

![Ansible Bullhorn banner](/images/bullhorn-banner-mango.png)

## The Bullhorn

*A Newsletter for the Ansible Developer Community*
*Issue #27, 2021-05-27 ([Past Issues](https://us19.campaign-archive.com/home/?u=56d874e027110e35dea0e03c1&id=d6635f5420))*

Welcome to the Bullhorn, our newsletter for the Ansible developer community. If you have any questions or content you’d like to share, please reach out to us at the-bullhorn@redhat.com, or comment on this [GitHub issue](https://github.com/ansible/community/issues/546).

<!-- TEASER_END -->

**KEY DATES**

* 2021-06-02: [community IRC meeting](https://github.com/ansible/community/issues/539), 18:00 UTC (propose topics [here](https://github.com/ansible-community/community-topics/issues))
* 2021-06-08: [Ansible Contributor Summit 2021.06](https://www.eventbrite.com/e/ansible-contributor-summit-202106-registration-152686374055?aff=bullhorn), 07:00 UTC
* 2021-06-08: [ETA for Ansible 4.1.0 release](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_4.html)
* 2021-06-08: [Bullhorn #28 content deadline](https://github.com/ansible/community/issues/546)
* 2021-06-09: Hackathon/PR Day (plus possible [community IRC meeting](https://github.com/ansible/community/issues/539))
* 2021-06-10: [D&I working group meeting](https://github.com/ansible/community/issues/577), 19:00 UTC
* 2021-06-15/16: [Red Hat Summit 2021 Virtual Experience Part 2](https://www.redhat.com/en/summit)
* 2021-06-21: ETA for Ansible-Core 2.11.2 and Ansible-Base 2.10.11 release
* [Ansible-core 2.12 Roadmap now available](https://docs.ansible.com/ansible-core/devel/roadmap/ROADMAP_2_12.html)

**ANSIBLE 4.0.0 NOW GENERALLY AVAILABLE**

Ansible 4.0.0 has been released on May 18th. 🎉

The Ansible Community team announced the general availability of Ansible 4.0.0 on May 18th, 2021. This is the first Ansible release to make use of Ansible-core-2.11. There may be changes to the playbook language or other backwards incompatibilities. Please see the [porting guide](https://docs.ansible.com/ansible/devel/porting_guides/porting_guide_4.html) for details.

This release of Ansible 4.0.0 marks the end of updates to Ansible 3. Future updates of the Ansible package will be bugfixes and backwards compatible feature enhancements to the Ansible 4 package. For what's new in this release and how to get it, please see [Toshio Kuratomi’s email to the ansible-announce list](https://groups.google.com/g/ansible-announce/c/H7LvB-uYMWg). 

Ansible 5 development begins now. Ansible 5 will be released in approximately six months, bringing in the Ansible-core-2.12 release.

**ANSIBLE-CORE 2.11.1, ANSIBLE-BASE 2.10.10, AND ANSIBLE 2.9.22 RELEASED**

The Ansible Core team announced the maintenance releases of Ansible-Core 2.11.1, Ansible-Base 2.10.10, and Ansible 2.9.22 on May 24th. Follow [this link](https://groups.google.com/g/ansible-devel/c/bu64VgA_Qc0) for Rick Elrod’s email to the ansible-devel mailing list, to obtain details on what’s new, installation instructions, and schedule for future releases.

**COMMUNICATION: IRC NETWORK CHANGE**

Ansible Community has made the [decision](https://github.com/ansible-community/community-topics/issues/19) to move to [Libera.Chat](https://libera.chat/) IRC network. We are using the same channel names as we did on the Freenode network. Documentation will be updated shortly, and we will share them when ready. From now on, discussions and meetings will take place on [Libera.Chat](https://libera.chat/) instead of Freenode.

**NEW/UPDATED COMMUNITY COLLECTIONS**

Community General Collection - [community.general](https://galaxy.ansible.com/community/general) 3.1.0 has been released. This was not included in Ansible 4.0.0, which was in feature freeze.

**LOOKING FOR NETBOX COLLECTION MAINTAINER**

There's a call for a maintainer to take over the ownership of the Netbox collection. Please see the details [here](https://github.com/netbox-community/ansible_modules/discussions/526) and reach out if you are interested!

**INTRODUCING SPHINX-ANSIBLE**

[Sphinx-Ansible](https://github.com/ansible-community/sphinx-ansible) is a new extension for [Sphinx](https://www.sphinx-doc.org/en/master/index.html), the documentation generator.

Sphinx uses a plaintext markup language called RestructuredText. This extension allows you to write some regular Ansible tasks directly within the documentation. When you generate the final document, the extension will call Ansible to run these tasks. The output will be integrated in the end result. It's helpful if you want to ensure the accuracy of your documentation. You can for instance run the generation in a CI pipeline.

**FEEDBACK WANTED!**

* With [inventory plugins for ESXi host](https://github.com/ansible-collections/community.vmware/pull/674), you can gather information about VMware ESXi in your vCenter using the plugin. Please feel free to try and share your review.
* For Vyos network devices, we are requesting feedback on the model for [Vyos logging_global resource module](https://github.com/ansible-network/resource_module_models/pull/132), which manages the logging attributes.
* If you are using role argument specs in collections, or are trying them out, please provide feedback for the following PRs:
    - [Generate role documentation](https://github.com/ansible-community/antsibull/pull/272) - this PR creates role documentation from role argument specs for the docsite, similarly to plugin and module documentation.
    - [Support roles with argument spec](https://github.com/ansible-community/antsibull-changelog/pull/55) - this PR allows antsibull-changelog to auto-detect new roles (it only considers the `main` entrypoint) in collections.
* There's a feature request for the Cisco ASA collection to have a [dynamic_filter](https://github.com/ansible-collections/cisco.asa/issues/115) ASA module which can enable Botnet filtering via Cisco dynamic/static DB. Feedback is welcome from the community as to how often you've used the Cisco ASA botnet filtering feature, and if you want the process to be automated via Ansible Cisco ASA module.
* We're updating galaxy.ansible.com to use GalaxyNG, the code that powers Ansible Automation Hub, because it is well maintained and efficient. Help us make sure your use cases are addressed in this transition! Please take a look at this [post on Reddit](https://www.reddit.com/r/ansible/comments/na4end/ansible_community_galaxy_next_steps_help_needed/) for the details, and ways you can help and provide feedback.
* In ansible-core 2.12, collections will be able to define new groups to use with `module_defaults`. [Here](https://gist.github.com/s-hertel/725ecc719b5301e76c571aca58d39bd3) is a summary of the evolution of the feature. [Feedback](https://github.com/ansible/ansible/pull/74039) is welcome!
* We are currently in the testing phase of our new GitHub Action PPA process. This testing includes Ansible `2.8.20` and `2.9.22` for Ubuntu `18.04`, as well as Ansible `2.10.7`, `3.4.0`, and `4.0.0` for Ubuntu `18.04`, `20.04`, `20.10`, and `21.04`. If you are interested in testing or checking out the new process please see [this GitHub issue](https://github.com/ansible-community/ppa/issues/1) for more details.

**ANSIBLE CONTRIBUTOR SUMMIT 2021.06**

The next Ansible Contributor Summit will be held on Tuesday, June 8, 2021. That's in less than 2 weeks! Please see the details and register on [Eventbrite](https://www.eventbrite.com/e/ansible-contributor-summit-202106-registration-152686374055?aff=bullhorn) if you haven't already, and propose/vote on topics you’d like to discuss in this [HackMD note](https://hackmd.io/@ansible-community/contrib-summit-202106).

**CONTENT FROM THE ANSIBLE COMMUNITY**

Follow the adventurous tale of [Ansible role argument specification](https://steampunk.si/blog/ansible-role-argument-specification/) (one of the new features of Ansible Core 2.11) by [Tadej Borovšak](https://github.com/tadeboro), where CI saves the day!

**THE ANSIBLE TEAM IS HIRING**

Red Hat is hiring several roles to work on Ansible. Please check the job descriptions in the links and apply!

* [DevOps Automation Engineer - Red Hat Ansible](https://global-redhat.icims.com/jobs/82487/devops-automation-engineer---red-hat-ansible/job)
* [Senior Field Product Manager - Technical](https://us-redhat.icims.com/jobs/82489/senior-product-manager---technical/job)
* [Senior Product Manager - Ansible](https://us-redhat.icims.com/jobs/82490/senior-product-manager---technical/job)
* [Principal Product Manager - Ansible](https://us-redhat.icims.com/jobs/86158/principal-product-manager---technical/job)

**FEEDBACK**

Have any questions you’d like to ask, or issues you’d like to see covered? Please send us an email at the-bullhorn@redhat.com.
