---
title: "Bullhorn #19"
date: 2021-02-04 21:00 UTC
tags: news
category: bullhorn
type: text
---

![Ansible Bullhorn banner](/images/bullhorn-banner-mango.png)

## The Bullhorn

*A Newsletter for the Ansible Developer Community*
*Issue #19, 2021-02-04 ([Past Issues](https://us19.campaign-archive.com/home/?u=56d874e027110e35dea0e03c1&id=d6635f5420))*

Welcome to the Bullhorn, our newsletter for the Ansible developer community. If you have any questions or content you’d like to share, please reach out to us at the-bullhorn@redhat.com, or comment on this [GitHub issue](https://github.com/ansible/community/issues/546).

<!-- TEASER_END -->

**KEY DATES**

* 2021-02-09: ETA for Ansible 3.0.0 release candidate
* 2021-02-10: [community IRC meeting](https://github.com/ansible/community/issues/539), 19:00 UTC
* 2021-02-15: ETA for Ansible-base 2.10.6 release
* 2021-02-16: [ETA for Ansible 3.0.0 general release](https://github.com/ansible/ansible/blob/devel/docs/docsite/rst/roadmap/COLLECTIONS_3_0.rst)
* 2021-02-16: [Bullhorn #20 content deadline](https://github.com/ansible/community/issues/546)
* 2021-02-17: [community IRC meeting](https://github.com/ansible/community/issues/539), 19:00 UTC
* 2021-02-18: [D&I working group meeting](https://github.com/ansible/community/issues/577), 19:00 UTC

**ANSIBLE 2.10.6 NOW GENERALLY AVAILABLE**

The Ansible Community team announced the general availability of Ansible 2.10.6 on January 26th. This update contains bug fixes and new, backwards compatible features in the contained collections. Important notes:

* This release fixes CVE-2021-20178 and CVE-2021-20180 in the `community.general.bitbucket_pipeline_variable` and `community.general.snmp_facts` modules.
* There will be one more 2.10 release, ansible-2.10.7, on February 9, 2021.  Ansible-3.0.0, is planned for February 16, 2021.

For the full release announcement including what’s new, how to get it, plus schedule for upcoming releases, read [Toshio Kuratomi’s email to the ansible-devel mailing list](https://groups.google.com/g/ansible-devel/c/H_YEoNo3zv8).

**ANSIBLE 3.0.0 BETA1 RELEASED**

The Ansible Community team announced the first beta release of Ansible 3.0.0 on February 2nd, now available for testing. You can get it via pip: `pip install --user ansible==3.0.0b1`

* The Ansible package has moved to semantic versioning

Unless blockers are discovered, Ansible 3.0.0 final will be out on February 16th. For the full announcement including changelogs, please see [Toshio Kuratomi’s email to the ansible-devel mailing list](https://groups.google.com/g/ansible-devel/c/CURhozF2nj0) or [David Moreau Simard's Reddit post and discussion](https://www.reddit.com/r/ansible/comments/lbbdab/ansible300_beta1_released/).

**NEW COLLECTION CRITERIA**

A new collection criteria has been added: Collections are only allowed to use specific directories in the `plugins/` directory which correspond to [recognized plugin types](https://github.com/ansible-collections/overview/blob/main/collection_requirements.rst#modules-plugins).

**NEW/UPDATED COMMUNITY COLLECTIONS**

* The [Community General Collection](https://galaxy.ansible.com/community/general) community.general 1.3.5 and 2.0.0 have been released. [Changelog for 2.0.0 (with all changes since 1.0.0)](https://github.com/ansible-collections/community.general/blob/stable-2/CHANGELOG.rst).
* The [Community Network Collection](https://galaxy.ansible.com/community/network) community.network 1.3.1 and 2.0.0 have been released. [Changelog for 2.0.0 (with all changes since 1.0.0)](https://github.com/ansible-collections/community.network/blob/stable-2/CHANGELOG.rst).
* The [Docker Community Collection](https://galaxy.ansible.com/community/docker) community.docker 1.2.1 has been released with some improvements and fixes for `docker_container`, `docker_image` and the `docker` connection plugin.
* The [Community Crypto Collection](https://galaxy.ansible.com/community/crypto) community.crypto 1.4.0 has been released with some improvements for the `luks_device`, `openssl_csr*` and `openssl_pkcs12` modules.
* The [Sensu Go Ansible Collection](https://galaxy.ansible.com/sensu/sensu_go) sensu.sensu_go was updated to 1.8.0. For more information about its releases, head over to [release notes](https://sensu.github.io/sensu-go-ansible/release_notes.html).
* The [Internal Test Tools Collection](https://galaxy.ansible.com/community/internal_test_tools) community.internal_test_tools 0.3.0 has been released ([changelog](https://github.com/ansible-collections/community.internal_test_tools/blob/main/CHANGELOG.rst)). This collection is not for end-users, but for collection maintainers. It contains frameworks for testing `open_url` and `fetch_url` based modules and plugins, modules for testing files and directories for changes (useful for integration tests), and some tools for running extra sanity tests and for helping with `meta/runtime.yml` redirects, in particular for collections using flatmapping.

**MODULE COMPAT FOR PYTHON 3.8+ CONTROLLER**

If you use Ansible's selinux support in any of the core file modules, or the yum/dnf/apt package managers, we'd love for you to try out [module compat for py3.8+ controller](https://github.com/ansible/ansible/pull/73423). As part of the ansible-core 2.11 project to bump controller Python requirements to 3.8+, this pull request provides a couple of new module compatibility APIs, and changes to the core modules that need those APIs to continue functioning under Python 3.8+.

You can pip install the PR to a Python 3.8+ environment from source via `pip install https://github.com/nitzmahone/ansible/tarball/module_respawn`, or clone the PR locally and run directly from the source in the usual way (assuming you've already got an environment set up to run Ansible from source).

Try out the package management and file module(s) with selinux that you use under `localhost` with Ansible installed on Python 3.8/3.9, or by forcing `ansible_python_interpreter` to any target-side supported Python version (2.6-3.9). The modules should now work transparently with no manual installation of dependencies required (including the oft-dreaded `libselinux-python`!).

**REQUEST FOR COMMENTS - KUBERNETES COLLECTION**

The Kubernetes inventory plugin is being [refactored](https://github.com/ansible-collections/community.kubernetes/pull/217) to improve overall operation. We would like your comments on how this plugin is being used. Does the refactoring make sense? What is the impact, if any, of the changes? Are there other improvements to be made to help users? Please add your feedback to this [GitHub issue](https://github.com/ansible-collections/community.kubernetes/issues/226).

**THE ANSIBLE TEAM IS HIRING**

The Ansible Product Marketing team has 3 jobs available as Technical Marketing Managers (individual contributors, managing content, not people) that will focus on Red Hat Ansible Automation Platform:

* [Technical Marketing Manager](https://us-redhat.icims.com/jobs/82006/technical-marketing-manager/job)
* [Senior Technical Marketing Manager](https://us-redhat.icims.com/jobs/82005/senior-technical-marketing-manager/job)
* [Principal Technical Marketing Manager](https://us-redhat.icims.com/jobs/82004/principal-technical-marketing-manager/job)

In addition, we're looking for a [Manager of Technical Marketing](https://us-redhat.icims.com/jobs/82003/manager%2c-technical-marketing/job) to manage the technical marketing strategy and team, as well as [2 Product](https://us-redhat.icims.com/jobs/82007/product-marketing-manager/job) [Marketing Managers](https://us-redhat.icims.com/jobs/82009/product-marketing-manager/job). Please check the job descriptions in the links and apply!

**CONTENT FROM THE ANSIBLE COMMUNITY**

[David Moreau Simard](https://github.com/dmsimard) wrote a blog post on ["Benchmarking Ansible and python versions for fun and science"](https://ara.recordsansible.org/blog/2021/01/30/benchmarking-ansible-and-python-versions-for-fun-and-science/).

**ANSIBLE CONTRIBUTOR SUMMIT 2021.03**

The next Ansible Contributor Summit will be held on March 9, 2021. Registration info will be shared shortly, and in the meantime, please propose topics you'd like to discuss in [this HackMD note](https://hackmd.io/uZDSLOOdS1Kx0xfZVIATmQ).

**ANSIBLE VIRTUAL MEETUPS**

The following virtual meetups are being held in the Ansible community over the next month:

* Wed, Feb 17 · 5:00 PM GMT+1 - [Ansible in DevOps Torun-Bydgoszcz](https://www.meetup.com/Ansible-in-DevOps-Torun-Bydgoszcz/events/276002537/) - AiDO Meetup #13 Rekrutacja w IT + Ulga IP BOX
* Thu, Feb 18 · 6:00 PM GMT+1 - [Ansible Meetup Dresden](https://www.meetup.com/Ansible-Meetup-Dresden/events/275843917/) - Meetup 02.2021

**FEEDBACK**

Have any questions you’d like to ask, or issues you’d like to see covered? Please send us an email at the-bullhorn@redhat.com.
