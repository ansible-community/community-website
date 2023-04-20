---
title: "Bullhorn #36"
date: 2021-10-24 20:30 UTC
tags: news
category: bullhorn
type: text
---

![Ansible Bullhorn banner](/images/bullhorn-banner-mango.png)

## The Bullhorn

*A Newsletter for the Ansible Developer Community*
*Issue #36, 2021-10-22 ([Past Issues](https://us19.campaign-archive.com/home/?u=56d874e027110e35dea0e03c1&id=d6635f5420))*

Welcome to the Bullhorn, our newsletter for the Ansible developer community. If you have any questions or content you’d like to share, please reach out to us at the-bullhorn@redhat.com, or comment on this [GitHub issue](https://github.com/ansible/community/issues/546).

<!-- TEASER_END -->

### KEY DATES

* 2021-10-27: [community IRC meeting](https://github.com/ansible/community/issues/539), 18:00 UTC (propose topics [here](https://github.com/ansible-community/community-topics/issues))
* 2021-10-28: [D&I working group meeting](https://github.com/ansible/community/issues/577), 19:00 UTC
* 2021-11-02: [ETA for Ansible 4.8.0 release](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_4.html)
* 2021-11-02: [Bullhorn #37 content deadline](https://github.com/ansible/community/issues/546)
* 2021-11-03: [community IRC meeting](https://github.com/ansible/community/issues/539), 18:00 UTC (check possible new time [here](https://github.com/ansible-community/community-topics/issues/48))
* 2021-11-08: ETA for Ansible-Core 2.11.7 and Ansible-Base 2.10.16 releases
* 2021-11-08: [ETA for Ansible-Core 2.12.0 GA release](https://docs.ansible.com/ansible-core/devel/roadmap/ROADMAP_2_12.html)
* 2021-11-30: [ETA for Ansible 5.0.0 GA release](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_5.html)

### ANSIBLE 4.7.0 RELEASED

The Ansible Community team announced the availability of Ansible 4.7.0 on October 13th. This update contains bugfixes and new, backwards compatible features in the contained collections. The release makes use of Ansible-core-2.11.6.

For what's new in this release and installation instructions, please see [David Moreau Simard’s email to the ansible-announce list](https://groups.google.com/g/ansible-announce/c/Nl-5dEB5mZU).

### ANSIBLE 5.0.0 ALPHA2 AVAILABLE FOR TESTING

The Ansible Community team announced the second alpha release of Ansible 5.0.0 on October 19th. This version is based on ansible-core 2.12.0rc1 which is a major update from ansible-core 2.11.x used in Ansible 4. There may be backwards incompatibilities in the core playbook language. Please see the [porting guide](https://docs.ansible.com/ansible/devel/porting_guides/porting_guide_5.html) for details.

This is an alpha release. Therefore, there may be more backwards incompatible changes and new features added before Ansible 5.0.0 final is released. For what is included in this release, and how to get it for testing, please see [David Moreau Simard’s email to the ansible-devel list](https://groups.google.com/g/ansible-devel/c/cighpvRQQdg). There is also a [testing-ansible-5 PPA](https://launchpad.net/~ansible/+archive/ubuntu/testing-ansible-5) available for Ubuntu.

### ANSIBLE-CORE 2.11.6, ANSIBLE-BASE 2.10.15, AND ANSIBLE 2.9.27 RELEASED

The Ansible Core team announced the maintenance releases of Ansible-Core 2.11.6, Ansible-Base 2.10.15, and Ansible 2.9.27 on October 14th. Follow [this link](https://groups.google.com/g/ansible-announce/c/xwhboaCpjm4) for Matt Martz’s email to the ansible-announce mailing list, to obtain details on what’s new, installation instructions, and schedule for future releases.

### ANSIBLE-CORE 2.12.0 RC1 RELEASED

The Ansible Core team announced the first release candidate of Ansible-Core 2.12.0 on October 18th. Check out [this link](https://groups.google.com/g/ansible-devel/c/UiO35a_OjjI) for Matt Martz’s email to the ansible-devel mailing list, to obtain details on what’s new, how to get it, and schedule for future releases.

### NEW/UPDATED COMMUNITY COLLECTIONS

New Collections:

* Healthchecks.io Community Collection - [community.healthchecksio](https://github.com/ansible-collections/community.healthchecksio) is a new collection containing modules for assisting in the automation of the [Healthchecks.io](https://healthchecks.io/) monitoring service. If you are interested in helping, please visit its [issue tracker](https://github.com/ansible-collections/community.healthchecksio/issues) or reach out to [Mark Mercado](https://github.com/mamercad), the collection's author and maintainer.
* LBRY Community Collection - [community.lbry](https://github.com/ansible-collections/community.lbry) is a new collection (work in progress) focusing on modules working with the [LBRY Platform](https://lbry.tech/).

Updated Collections:

* Community General Collection - [community.general](https://galaxy.ansible.com/community/general) 3.8.0 has been released. This will be the last 3.x.0 minor release, with community.general 4.0.0 planned for November 2nd.
* Community RouterOS Collection - [community.routeros](https://galaxy.ansible.com/community/routeros) 2.0.0-a2 has been released with some more breaking changes and some new filter plugins. If you use the collection, please make sure to try this out and provide feedback in case something does not work as expected.
* MySQL collection for Ansible - [community.mysql](https://galaxy.ansible.com/community/mysql) 2.3.1 has been released.
* Community Hetzner Robot Collection - [community.hrobot](https://galaxy.ansible.com/community/hrobot) 1.2.0 has been released with several new modules.
* Docker Community Collection - [community.docker](https://galaxy.ansible.com/community/docker) 2.0.0 has been released.

You can now keep track of the releases of Ansible community projects and collections via the [Ansible community RSS feeds](https://rss.community.eng.ansible.com/).

### CHANGES IMPACTING COLLECTION OWNERS

* [Deprecation of centos8 in ansible-test](https://github.com/ansible-collections/overview/issues/45#issuecomment-944657318) - support for the `centos8` test container in `ansible-test` is now deprecated since CentOS 8 will reach end-of-life on December 31st. Support for the test container will be removed from the devel branch in mid-November.
* For more details of the above, and to stay on top of these changes, please subscribe to the [issue on GitHub](https://github.com/ansible-collections/overview/issues/45).

### CONTENT FROM THE ANSIBLE COMMUNITY

If you are interested in speeding up your Ansible execution time, have a look at [ansible-trace](https://github.com/mhansen/ansible-trace) by [Mark Hansen](https://github.com/mhansen), a plugin for visualising execution time across playbooks, tasks, and hosts. Join in the discussions on the [mailing list](https://groups.google.com/g/ansible-project/c/AZJfDONBZjo) or on [reddit](https://www.reddit.com/r/ansible/comments/q49h2d/ansibletrace_visualise_execution_time_of_ansible/).

[Sergey Pechenko](https://github.com/tnt4brain) has implemented a callback plugin ["log2db"](https://github.com/tnt4brain/ansible-logging-to-db) that acts like a stdout plugin, but also writes almost everything into an external PostgreSQL database, which can be useful for audits, etc. The plugin can be configured via standard `ansible.cfg` mechanics: it supports its own section with a set of keys. The plugin has "batteries included", i.e. no external PostgreSQL driver like psycopg2 should be installed to any box: Ansible-friendly version of pg8000 is included and starts up upon the loading of the plugin. For more info, check out the [plugin repo](https://github.com/tnt4brain/ansible-logging-to-db) and the [modified pg8000 driver](https://github.com/tnt4brain/ansible-pg8k), and Sergey will be glad to get feedback from you!

### ANSIBLE MEETUPS & COMMUNITY EVENTS

The following meetup(s) are being held in the Ansible community over the next month:

* Fri, Oct 29 · 1:00 PM SGT - [Ansible Singapore](https://www.meetup.com/Ansible-Singapore/events/281546171) - Ansible Virtual Meet Up - October 2021

### THE ANSIBLE TEAM IS HIRING

Red Hat is hiring several roles to work on Ansible. Please check the job descriptions in the links and apply!

* [Principal Product Marketing Manager, Ansible Cloud Services](https://us-redhat.icims.com/jobs/88957/principal-product-marketing-manager%2c-ansible-cloud-services/job), US-Remote
* [Senior Product Marketing Manager, Ansible Cloud Services](https://us-redhat.icims.com/jobs/89158/senior-product-marketing-manager%2c-ansible-cloud-services/job), US-Remote
* [Software Engineer - Part time (Returnship)](https://global-redhat.icims.com/jobs/88865/software-engineer---part-time-%28returnship%29/job), CZ-Brno

### FEEDBACK

Have any questions you’d like to ask, or issues you’d like to see covered? Please send us an email at the-bullhorn@redhat.com.
