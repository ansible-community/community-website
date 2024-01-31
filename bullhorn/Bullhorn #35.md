---
title: "Bullhorn #35"
date: 2021-10-08 21:00 UTC
tags: news
category: bullhorn
type: text
---

![Ansible Bullhorn banner](/images/bullhorn-banner-mango.png)

## The Bullhorn

*A Newsletter for the Ansible Developer Community*
*Issue #35, 2021-10-08 ([Past Issues](https://us19.campaign-archive.com/home/?u=56d874e027110e35dea0e03c1&id=d6635f5420))*

Welcome to the Bullhorn, our newsletter for the Ansible developer community. If you have any questions or content you’d like to share, please reach out to us at the-bullhorn@redhat.com, or comment on this [GitHub issue](https://github.com/ansible/community/issues/546).

<!-- TEASER_END -->

### KEY DATES

* 2021-10-11: ETA for Ansible-Core 2.11.6 and Ansible-Base 2.10.15 releases
* 2021-10-12: [ETA for Ansible 4.7.0 release](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_4.html)
* 2021-10-13: [community IRC meeting](https://github.com/ansible/community/issues/539), 18:00 UTC (propose topics [here](https://github.com/ansible-community/community-topics/issues))
* 2021-10-14: [D&I working group meeting](https://github.com/ansible/community/issues/577), 19:00 UTC
* 2021-10-19: [Bullhorn #36 content deadline](https://github.com/ansible/community/issues/546)
* 2021-10-20: [community IRC meeting](https://github.com/ansible/community/issues/539), 18:00 UTC (propose topics [here](https://github.com/ansible-community/community-topics/issues))
* 2021-11-30: [ETA for Ansible 5.0.0 GA release](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_5.html)

### CONTRIBUTOR SUMMIT & ANSIBLEFEST - THANK YOU!

We are collating all the notes, slides, and recordings from last week's Ansible Contributor Summit and parts of AnsibleFest, and will share them soon in a write-up. In the meantime, THANK YOU to all those who participated in one way or other throughout the week (on top of your continued contributions all year round)! YOU are what makes the Ansible Community so amazing!

### ANSIBLE 4.6.0 RELEASED

The Ansible Community team announced the availability of Ansible 4.6.0 on September 21st. This update contains bugfixes and new, backwards compatible features in the contained collections. The release makes use of Ansible-core-2.11.5.

For what's new in this release and installation instructions, please see [Toshio Kuratomi’s email to the ansible-announce list](https://groups.google.com/g/ansible-announce/c/-78_q5ZY9fI).

### ANSIBLE 5.0.0 ALPHA1 RELEASED

The Ansible Community team announced the first alpha release of Ansible 5.0.0 on October 5th. This update is based on the ansible-core-2.12.x package which is a major update from the  one used by Ansible 4. Ansible 4 was based on Ansible Core 2.11.x. There may be backwards incompatibilities in the core playbook language. Please see the [porting guide](https://docs.ansible.com/ansible/devel/porting_guides/porting_guide_5.html) for details.

* Collection maintainers please test that your collections work with this.
* Users please test your playbooks and workflows.
* Report bugs upstream (ansible-core bugs [here](https://github.com/ansible/ansible) and bugs in collections to the relevant collection issue trackers).
* Ansible 5.0.0 final is currently scheduled for 2021-11-30. 

This is an alpha release. Therefore, there may be more backwards incompatible changes and new features added before Ansible 5.0.0 final is released. For what is included in this release, and how to get it for testing, please see [Toshio Kuratomi’s email to the ansible-devel list](https://groups.google.com/g/ansible-devel/c/w94QsScCHoA).

### ANSIBLE-CORE 2.12.0 BETA1 RELEASED

The Ansible Core team announced the first beta release of Ansible-Core 2.12.0 on September 27th. Follow [this link](https://groups.google.com/g/ansible-devel/c/TVacGbKsyx8) for Matt Martz’s email to the ansible-devel mailing list, to obtain details on what’s new, how to get it, and schedule for future releases.

### NEW/UPDATED COMMUNITY COLLECTIONS

* Ansible Podman Collection - [containers.podman](https://galaxy.ansible.com/containers/podman) [1.8.0](https://github.com/containers/ansible-podman-collections/blob/master/CHANGELOG.rst#v1-8-0) has been released with 4 new modules: [podman_save](https://github.com/containers/ansible-podman-collections/blob/master/plugins/modules/podman_save.py) and [podman_load](https://github.com/containers/ansible-podman-collections/blob/master/plugins/modules/podman_load.py) for saving and loading images from files, [podman_export](https://github.com/containers/ansible-podman-collections/blob/master/plugins/modules/podman_export.py) and [podman_import](https://github.com/containers/ansible-podman-collections/blob/master/plugins/modules/podman_import.py) for exporting and importing containers from files. Also added systemd unit file generation for containers and pods.
* Community General Collection - [community.general](https://galaxy.ansible.com/community/general) 2.5.6 and 3.7.0 have been released.
* Community DNS Collection - [community.dns](https://galaxy.ansible.com/community/dns) 2.0.0 has been released.
* MySQL collection for Ansible - [community.mysql](https://galaxy.ansible.com/community/mysql) 2.2.0, 2.3.0, and 1.4.3 have been released.
* Community AWS Collection - [community.aws](https://galaxy.ansible.com/community/aws) 2.0.0 has been released with several major changes. Please see the [changelog](https://github.com/ansible-collections/community.aws/blob/main/CHANGELOG.rst) for more info.
* PostgreSQL collection for Ansible - [community.postgresql](https://galaxy.ansible.com/community/postgresql) 1.5.0 has been released.
* ProxySQL collection for Ansible - [community.proxysql](https://galaxy.ansible.com/community/proxysql) 1.3.0 has been released.
* Docker Community Collection - [community.docker](https://galaxy.ansible.com/community/docker) 1.10.0 has been released.
* Ansible Community Crypto Collection - [community.crypto](https://galaxy.ansible.com/community/crypto) 1.9.5 has been released, fixing compatibility with cryptography 35.0.0.

You can now keep track of the releases of Ansible community projects and collections via the [Ansible community RSS feeds](https://rss.community.eng.ansible.com/).

### ANNOUNCING NEW COLLECTION MAINTAINERS

We are happy to announce that the [community.rabbitmq](https://github.com/ansible-collections/community.rabbitmq) collection has found a new maintainer: [John Imison](https://github.com/Im0).

On behalf of the Ansible Community and the Community Team, we’d like to congratulate him on getting commit in the collection's repository and say THANK YOU!

### CHANGES IMPACTING COLLECTION OWNERS

* [Removal of Python 2.6 Support](https://github.com/ansible-collections/overview/issues/45#issuecomment-931612845) - collection maintainers may need to make the following changes:
    * If you have any sanity test ignores for Python 2.6 in your `ignore-2.13.txt` file, you will need to remove them.
    * If you have Python 2.6 or CentOS 6 in your CI test matrix, you will need to remove them.
* [Updated base and default containers](https://github.com/ansible-collections/overview/issues/45#issuecomment-938372701) - the `base` and `default` containers used by `ansible-test` in the `devel` branch have been updated.
* For more details of each of the above, and to stay on top of these changes, please subscribe to the [issue on GitHub](https://github.com/ansible-collections/overview/issues/45).

### ANSIBLE AUTOMATION WORKSHOPS FOR AAP2 

[Ansible Automation Workshops](https://github.com/ansible/workshops) for Ansible Automation Platform 2 (AAP2) have been released!
- docs are rendered using Github Pages on [this website](https://aap2.demoredhat.com)
- available in RHPDS for Red Hat partners and employees; for community users directions are provided for provisioning onto your own AWS environment 
- all content including prescriptive walkthrough exercises, slide decks, etc. is 100% open source
- showcases: execution environments, ansible-navigator, Automation controller (downstream of AWX) and much more
- please open issues / concerns on [GitHub](https://github.com/ansible/workshops/issues)

### CONTENT FROM THE ANSIBLE COMMUNITY

A team of the VMware {code} Connect Hackathon 2021 created an [Ansible based Toolkit](https://github.com/DaftPyPosh/vSphereSCG) to apply the VMware vSphere Security Configuration Guide to an existing ESXi deployment. The [community.vmware](https://github.com/ansible-collections/community.vmware) collection and some REST Calls are used so far. Work in Progess! Check out this [example video](https://www.youtube.com/watch?v=LEyDyiuihMg).

### ANSIBLE MEETUPS & COMMUNITY EVENTS

The following meetups are being held in the Ansible community over the next month:

* Wed, Oct 13 · 6:00 PM EEST - [Ansible Paris](https://www.meetup.com/Ansible-Paris/events/281202630/) - Meetup #21 @RED HAT
* Thu, Oct 14 · 4:00 PM EDT - [Ansible Toronto](https://www.meetup.com/Ansible-Toronto/events/280620210/) - Ansible Toronto October 2021 (Hybrid)

### THE ANSIBLE TEAM IS HIRING

Red Hat is hiring several roles to work on Ansible. Please check the job descriptions in the links and apply!

* [Software Engineer - Part time (Returnship)](https://global-redhat.icims.com/jobs/88865/software-engineer---part-time-%28returnship%29/job), CZ-Brno
* [Principal Product Marketing Manager, Ansible Cloud Services](https://us-redhat.icims.com/jobs/88957/principal-product-marketing-manager%2c-ansible-cloud-services/job), US-Remote
* [Senior Product Marketing Manager, Ansible Cloud Services](https://us-redhat.icims.com/jobs/89158/senior-product-marketing-manager%2c-ansible-cloud-services/job), US-Remote

### FEEDBACK

Have any questions you’d like to ask, or issues you’d like to see covered? Please send us an email at the-bullhorn@redhat.com.
