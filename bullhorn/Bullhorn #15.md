---
title: "Bullhorn #15"
date: 2020-12-02 18:00 UTC
tags: news
category: bullhorn
type: text
---

![Ansible Bullhorn banner](/images/bullhorn-banner-mango.png)

**The Bullhorn**
**Issue #15, 2020-12-02**

Welcome to the Bullhorn, our newsletter for the Ansible developer community. If you have any questions or content you’d like to share, please reach out to us at the-bullhorn@redhat.com, or comment on this [GitHub issue](https://github.com/ansible/community/issues/546).

<!-- TEASER_END -->

**KEY DATES**

* 2020-12-02: [community IRC meeting](https://github.com/ansible/community/issues/539), 19:00 UTC
* 2020-12-14: ETA for ansible-base 2.10.4 release
* 2020-12-14: [Bullhorn #16 content deadline](https://github.com/ansible/community/issues/546)
* 2020-12-16: [community IRC meeting](https://github.com/ansible/community/issues/539), 19:00 UTC
* 2020-12-17: [PR Review day](https://github.com/ansible/community/issues/407), 15:00 UTC
* 2021-01-05: ETA for ansible 2.10.5 release
* 2021-02: [proposed release schedule for Ansible 3.0](https://www.reddit.com/r/ansible/comments/jwzwwf/ansible300_schedule_and_preview_of_400_schedule/)

**ANSIBLE 2.10.4 NOW GENERALLY AVAILABLE**

The Ansible Community team announced the general availability of Ansible 2.10.4 on December 1st. This update of the ansible-2.10 package should be a drop-in replacement for Ansible 2.9; the roles and playbooks that you currently use should work out of the box with ansible-2.10.4. For more information on what’s new, how to get it, plus schedule for upcoming releases, read [David Moreau Simard’s announcement to the ansible-devel mailing list](https://groups.google.com/g/ansible-devel/c/CHgsLbNCcK0).

**ANSIBLE-BASE 2.10.4 RELEASE POSTPONED ONE WEEK**

The release schedule for ansible-base 2.10.4, along with Ansible 2.8.18 and 2.9.16, has been pushed back by a week. The new release date will be December 14 instead of December 7. Please see [Rick Elrod's email](https://groups.google.com/g/ansible-devel/c/gpQYwDg9Irg) for more details.

**NEW/UPDATED COMMUNITY COLLECTIONS**

- The OKD Collection for Ansible, [community.okd](https://galaxy.ansible.com/community/okd) 1.0 is now available. It includes a variety of Ansible content to help automate the management of applications in OKD and OpenShift clusters, as well as the provisioning and maintenance of the clusters themselves. It is included in the Ansible 2.10.4 release.

- The Community Hetzner Robot Collection, [community.hrobot](https://galaxy.ansible.com/community/hrobot) 1.0.0 has been released and is now included in the Ansible 2.10.4 release. It contains the `hetzner_*` modules from [community.general](https://galaxy.ansible.com/community/general).

- The Community Crypto Collection, [community.crypto](https://galaxy.ansible.com/community/crypto) 1.3.0 has been released. It has new modules for operating on private keys, CSRs and X.509 certificates without having to operate on files.

- The Community General Collection, [community.general](https://galaxy.ansible.com/community/general) 1.3.0 has been released. This is the last 1.x.0 minor release, the next releases will be patch releases (if needed). Version 2.0.0 will be released at the end of January 2021 for inclusion in Ansible 3.0.0.

- The Community Network Collection, [community.network](https://galaxy.ansible.com/community/network) 1.3.0 has been released. This is the last 1.x.0 minor release, the next releases will be patch releases (if needed). Version 2.0.0 will be released at the end of January 2021 for inclusion in Ansible 3.0.0.

**REQUEST FOR COMMENTS**

We'd appreciate your feedback on two important topics. Please see the following issues for details and reply in the respective issues with your comments.

* [Bumping the required version of python for the Ansible controller to Python 3.8](https://github.com/ansible/ansible/issues/72668)
* [Formalizing requirements for including new collections in the Ansible package](https://github.com/ansible-collections/overview/issues/131)

**ANSIBLE DOCUMENTATION SURVEY**

We have created a [one-page survey](https://www.surveymonkey.co.uk/r/B7PDVSB) about the Ansible documentation. If you use [docs.ansible.com](https://docs.ansible.com/), we’d love to hear your views! We’re hoping to learn whether different types of users need different types of documentation. We’re also interested in what the most common pain points are for documentation. The survey will be open through the end of December, 2020. Please [fill out the survey](https://www.surveymonkey.co.uk/r/B7PDVSB) and pass the word!

**CONTENT FROM THE ANSIBLE COMMUNITY**

* [Veeam Backup & Replication RestAPI Ansible Collection](https://mycloudrevolution.com/en/2020/11/11/veeam-backup-replication-restapi-ansible-collection/) by [Markus Kraus](https://github.com/vMarkusK)
* [Why and how of the NGINX Unit Ansible Collection](https://steampunk.si/blog/why-and-how-of-the-nginx-unit-ansible-collection/) by [Tadej Borovšak](https://github.com/tadeboro)
* [Ansible: Create a Tag Category in vCenter](https://medium.com/@AbhijeetKasurde/ansible-create-a-tag-category-in-vcenter-416a2bc8ca5) by [Abhijeet Kasurde](https://github.com/Akasurde)
* [Ansible: Performance Impact of the Python version](https://goneri.lebouder.net/2020/11/26/ansible-performance-impact-of-the-python-version/) by [Gonéri Le Bouder](https://github.com/goneri)

**COMMUNITY.GENERAL IGNORE LINES CLEANUP STATS**

Cleanup work has been done on the ignore lines for sanity tests in the [community.general](https://github.com/ansible-collections/community.general) repository, going from 3608 ignored failures in 1.2.0 down to 1952 ignored lines in 1.3.0, and currently 1547 in `main`. The top 5 ignored validations being:

```
   309 validate-modules:parameter-type-not-in-doc
   289 validate-modules:doc-missing-type
   258 validate-modules:parameter-list-no-elements
   161 validate-modules:undocumented-parameter
    90 validate-modules:doc-default-does-not-match-spec
```

while the top 5 offenders (2-level breakdown) being from:

```
   238 net_tools/nios
   180 cloud/ovirt
   104 remote_management/oneview
    60 cloud/scaleway
    52 cloud/google
```

**ANSIBLE VIRTUAL MEETUPS**

The following virtual meetups are being held in the Ansible community over the next month:

* Tue, Dec 8 · 5:00 PM GMT+11 - [Sydney Ansible User Group](https://www.meetup.com/Ansible-Sydney/events/274801128/) - SPECIAL EVENT: Top Secret People Skills (Know Others by Knowing Yourself)
* Wed, Dec 9 · 5:00 PM GMT+1 - [Ansible in DevOps Torun-Bydgoszcz](https://www.meetup.com/Ansible-in-DevOps-Torun-Bydgoszcz/events/274669461/) - Torun GitLab Day 2020

**FEEDBACK**

Have any questions you’d like to ask, or issues you’d like to see covered? Please send us an email at the-bullhorn@redhat.com.
