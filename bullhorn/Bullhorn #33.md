---
title: "Bullhorn #33"
date: 2021-09-03 01:00 UTC
tags: news
category: bullhorn
type: text
---

![Ansible Bullhorn banner](/images/bullhorn-banner-mango.png)

## The Bullhorn

*A Newsletter for the Ansible Developer Community*
*Issue #33, 2021-09-02 ([Past Issues](https://us19.campaign-archive.com/home/?u=56d874e027110e35dea0e03c1&id=d6635f5420))*

Welcome to the Bullhorn, our newsletter for the Ansible developer community. If you have any questions or content you’d like to share, please reach out to us at the-bullhorn@redhat.com, or comment on this [GitHub issue](https://github.com/ansible/community/issues/546).

<!-- TEASER_END -->

**KEY DATES**

* 2021-09-08: [community IRC meeting](https://github.com/ansible/community/issues/539), 18:00 UTC (propose topics [here](https://github.com/ansible-community/community-topics/issues))
* 2021-09-13: ETA for Ansible-Core 2.11.5 and Ansible-Base 2.10.14 release
* 2021-09-14: [Bullhorn #34 content deadline](https://github.com/ansible/community/issues/546)
* 2021-09-15: [community IRC meeting](https://github.com/ansible/community/issues/539), 18:00 UTC (propose topics [here](https://github.com/ansible-community/community-topics/issues))
* 2021-09-16: [D&I working group meeting](https://github.com/ansible/community/issues/577), 19:00 UTC
* 2021-09-21: [ETA for Ansible 4.6.0 release](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_4.html)
* 2021-09-28: [Contributor Summit 2021.09](https://ansiblecs202109.eventbrite.com/?aff=bullhorn) - Day 1 💾📅
* 2021-09-29/30: [AnsibleFest 2021](https://www.ansible.com/ansiblefest) 💾📅
* 2021-10-01: [Contributor Summit 2021.09](https://hackmd.io/@ansible-community/contrib-summit-202109) - Day 2 💾📅

**ANSIBLE 4.5.0 RELEASED**

The Ansible Community team announced the availability of Ansible 4.5.0 on August 31st. This update contains bugfixes and new, backwards compatible features in the contained collections. The release makes use of Ansible-core-2.11.4.

For what's new in this release and how to get it, please see [Toshio Kuratomi’s email to the ansible-announce list](https://groups.google.com/g/ansible-announce/c/sYr9CYEieus).

**CONTRIBUTOR SUMMIT & ANSIBLEFEST** 

The next [Ansible Contributor Summit](https://hackmd.io/@ansible-community/contrib-summit-202109) will be on September 28th and October 1st, alongside [AnsibleFest 2021](https://www.ansible.com/ansiblefest). Registration is open! Please register on [Eventbrite](https://ansiblecs202109.eventbrite.com/?aff=bullhorn) to stay informed of updates to the event. Note that the AnsibleFest registration is separate from the Contributor Summit.

The [first day (Tuesday, 28/9)](https://hackmd.io/@ansible-community/contrib-summit-202109#Day-1-Tuesday-September-28-2021) is aimed at new contributors and people who want to understand what is involved in contributing. [Day two (Friday, 1/10)](https://hackmd.io/@ansible-community/contrib-summit-202109#Day-2-Friday-October-1-2021) will contain the usual interactive discussions with more technical details.

In addition, we will be running a [Hackathon](https://hackmd.io/@ansible-community/contrib-summit-202109#Hackathon) in parallel throughout the week (Tuesday to Friday). This is for anyone with an interest in contributing to Ansible (with a focus on Collections), including those who have never contributed and are unsure of how to get started, existing contributors and maintainers, etc. all are welcome! Resources (people, labs, docs, etc.) will be available to help people through the entire process.

During AnsibleFest, we will have a Community Live Q&A with members of the Ansible Community Team (exact date and time TBD). If you have pressing questions that you'd like us to answer/discuss, please suggest them in this [GitHub issue](https://github.com/ansible/community/issues/629).

**NEW/UPDATED COMMUNITY COLLECTIONS**

* Docker Community Collection - [community.docker](https://galaxy.ansible.com/community/docker) 1.9.1 has been released.
* Ansible Community Crypto Collection - [community.crypto](https://galaxy.ansible.com/community/crypto) 1.9.0 has been released.
* Community General Collection - [community.general](https://galaxy.ansible.com/community/general) 1.3.12 and 3.6.0 have been released.
* Sensu Go Ansible Collection - [sensu.sensu_go](https://galaxy.ansible.com/sensu/sensu_go) 1.12.0 has been released.
* Openstack Ansible Collection - [openstack.cloud](https://galaxy.ansible.com/openstack/cloud) [1.5.1](https://opendev.org/openstack/ansible-collections-openstack/src/branch/master/CHANGELOG.rst#v1.5.1) has been released which contains some new features and bugfixes, mostly networking related.

**ANNOUNCING NEW COLLECTION MAINTAINER**

We are happy to announce that the [community.rabbitmq](https://galaxy.ansible.com/community/rabbitmq) collection has found a new maintainer: [Jacob Floyd](https://github.com/cognifloyd).

He has done an excellent job as a code contributor and reviewer in several repositories within the `ansible` and `ansible-collections` organizations. He is also a maintainer of the [community.mongodb](https://galaxy.ansible.com/community/mongodb) collection.

On behalf of the Ansible Community and the Community Team, we’d like to congratulate him on getting commit access, and say THANK YOU!

**ANSIBLE GALAXY UPDATE**

We updated the backend infrastructure of [Ansible Galaxy](https://galaxy.ansible.com/) on August 24th. It is now running off the latest major version of OpenShift, and this allows us to keep up to date with performance and security patches.

We realize that we didn't do the best job in informing people about the downtime in advance. We will work on improving such communication, including notification banners on [galaxy.ansible.com](https://galaxy.ansible.com/).

**ANSIBLE MOLECULE UPDATE**

* [Ansible Molecule](https://molecule.readthedocs.io/) [3.4.0](https://github.com/ansible-community/molecule/discussions/3203) was released which now allows plugins to require presence of various collections needed by them. Its most popular plugins were also updated to expose their required collections.
* The [Molecule container](https://github.com/ansible-community/molecule/discussions/3206) was removed from [quay.io](https://quay.io/) after almost one year of deprecation.

**NEW TOOL: RELEASE RSS FEEDS AGGREGATOR**

A [new tool](https://rss.community.eng.ansible.com/) to help keep track of project releases is now available for the community. It provides a blog-like interface that aggregates the release RSS feeds of relevant Ansible community projects, in addition to every Ansible collection included in the Ansible community package on PyPI. It also provides a meta Atom feed that aggregates the last one hundred events, available [here](https://rss.community.eng.ansible.com/atom.xml). 

Feel free to open an issue or pull request in [rss-feed-aggregator](https://github.com/ansible-community/rss-feed-aggregator) to improve it or add missing projects.

**NEW TOOL: CODESEARCH**

A [new Codesearch tool](https://codesearch.community.eng.ansible.com/) is now available to help quickly search across the 350+ git repositories that make up the `ansible`, `ansible-community` and `ansible-collections` organizations on GitHub, as well as collections included in the Ansible community package.

It is deployed with the help of Ansible. While it is rough around the edges, feel free to [take a look here](https://github.com/dmsimard/hound-localrepos) if you are curious about how it works, or perhaps even how you might be able to deploy it for yourself.

**CONTENT FROM THE ANSIBLE COMMUNITY**

[Gonéri Le Bouder](https://github.com/goneri) wrote about how to [Audit your VMware vCenter Server using Ansible](https://www.ansible.com/blog/audit-your-vmware-vcenter-server-using-ansible).

**ANSIBLE MEETUPS & COMMUNITY EVENTS**

The following meetups/events are being held in the Ansible community over the next month:

* Wed, Sep 22 · 5:30 PM CEST - [Ansible in DevOps Torun-Bydgoszcz](https://www.meetup.com/Ansible-in-DevOps-Torun-Bydgoszcz/events/280507922/) - AiDO Meetup #18 Debaty IT/DevOps
* Fri, Sep 24 - [Ansible Meetup Dresden](https://www.meetup.com/de-DE/Ansible-Meetup-Dresden/) will be participating at [DecompileD](https://decompiled.de/) (you can use promo code "ANSIBLE" to get a discount on the ticket!)
* Tue, Sep 28 · 5:00 PM CEST - [Ansible Zürich](https://www.meetup.com/Ansible-Zurich/events/280443227/) - 10th Ansible Meetup

**THE ANSIBLE TEAM IS HIRING**

Red Hat is hiring several roles to work on Ansible. Please check the job descriptions in the links and apply!

* [Agile Project Manager](https://us-redhat.icims.com/jobs/82356/agile-project-manager/job), US-Raleigh
* [Senior Software Engineer - Ansible Controller API](https://us-redhat.icims.com/jobs/86519/senior-software-engineer---ansible-controller-api/job), US-NC-Remote
* [Senior Quality Engineer](https://global-redhat.icims.com/jobs/87033/senior-quality-engineer/job), BR-Remote
* [Senior Software Engineer - Python](https://us-redhat.icims.com/jobs/82352/senior-software-engineer---python/job), US-Remote
* [Software Engineer - Part time (Returnship)](https://global-redhat.icims.com/jobs/88865/software-engineer---part-time-%28returnship%29/job), CZ-Brno
* [Senior Software Engineer - Front End Development](https://us-redhat.icims.com/jobs/89147/senior-software-engineer---front-end-development/job), US-Remote
* [Senior Software Engineer](https://us-redhat.icims.com/jobs/88838/senior-software-engineer/job), US-Remote
* [Principal Software Engineer](https://us-redhat.icims.com/jobs/88830/principal-software-engineer/job), US-Remote
* [Principal Product Marketing Manager, Ansible Cloud Services](https://us-redhat.icims.com/jobs/88957/principal-product-marketing-manager%2c-ansible-cloud-services/job), US-Remote
* [Senior Product Marketing Manager, Ansible Cloud Services](https://us-redhat.icims.com/jobs/89158/senior-product-marketing-manager%2c-ansible-cloud-services/job), US-Remote
* [Principal Product Manager Ansible Cloud Services](https://us-redhat.icims.com/jobs/88967/principal-product-manager-ansible-cloud-services/job), US-Remote

**FEEDBACK**

Have any questions you’d like to ask, or issues you’d like to see covered? Please send us an email at the-bullhorn@redhat.com.
