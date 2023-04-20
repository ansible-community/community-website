---
title: "Bullhorn #29"
date: 2021-07-01 20:30 UTC
tags: news
category: bullhorn
type: text
---

![Ansible Bullhorn banner](/images/bullhorn-banner-mango.png)

## The Bullhorn

*A Newsletter for the Ansible Developer Community*
*Issue #29, 2021-07-01 ([Past Issues](https://us19.campaign-archive.com/home/?u=56d874e027110e35dea0e03c1&id=d6635f5420))*

Welcome to the Bullhorn, our newsletter for the Ansible developer community. If you have any questions or content you’d like to share, please reach out to us at the-bullhorn@redhat.com, or comment on this [GitHub issue](https://github.com/ansible/community/issues/546).

<!-- TEASER_END -->

**KEY DATES**

* 2021-07-07: [community IRC meeting](https://github.com/ansible/community/issues/539), 18:00 UTC (propose topics [here](https://github.com/ansible-community/community-topics/issues))
* 2021-07-08: [D&I working group meeting](https://github.com/ansible/community/issues/577), 19:00 UTC
* 2021-07-13: [Bullhorn #30 content deadline](https://github.com/ansible/community/issues/546)
* 2021-07-14: [community IRC meeting](https://github.com/ansible/community/issues/539), 18:00 UTC (propose topics [here](https://github.com/ansible-community/community-topics/issues))
* 2021-07-19: ETA for Ansible-Core 2.11.3 and Ansible-Base 2.10.12 release
* 2021-07-20: [ETA for Ansible 4.3.0 release](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_4.html)

**ANSIBLE 4.2.0 RELEASED**

The Ansible Community team announced the availability of Ansible 4.2.0 on June 30th. This update contains bugfixes and new, backwards compatible features in the contained collections. The release makes use of Ansible-core-2.11. There may be changes to the playbook language or other backwards incompatibilities. Please see the [porting guide](https://docs.ansible.com/ansible/devel/porting_guides/porting_guide_4.html) for details.

For what's new in this release and how to get it, please see [Toshio Kuratomi’s email to the ansible-announce list](https://groups.google.com/g/ansible-announce/c/LzSCGkYpdOU). 

We're planning to release Ansible 5.0.0 in November 2021, bringing in the Ansible-core-2.12 release.

**ANSIBLE-CORE 2.11.2, ANSIBLE-BASE 2.10.11, AND ANSIBLE 2.9.23 RELEASED**

The Ansible Core team announced the maintenance releases of Ansible-Core 2.11.2, Ansible-Base 2.10.11, and Ansible 2.9.23 on June 22nd. These releases fix a templating security issue, CVE-2021-3583, in addition to several other bugs. Follow [this link](https://groups.google.com/g/ansible-devel/c/nPmBIXpGrPk) for Rick Elrod’s email to the ansible-devel mailing list, to obtain details on what’s new, installation instructions, and schedule for future releases.

**ANTSIBULL-CHANGELOG AND ANSIBLE-PYGMENTS**

The changelog generator [antsibull-changelog](https://github.com/ansible-community/antsibull-changelog) 0.11.0 has been released, with support for detecting new roles in collections.

[ansible-pygments](https://github.com/ansible-community/ansible-pygments/) 0.1.0 has been released. This package provides a Pygments lexer `ansible-output` for highlighting `ansible-playbook` output, and the Pygments color scheme used for the Ansible docsite.

**NEW/UPDATED COMMUNITY COLLECTIONS**

* Foreman Ansible Collection - [theforeman.foreman](https://galaxy.ansible.com/theforeman/foreman) [2.1.0 and 2.1.1](https://theforeman.github.io/foreman-ansible-modules/v2.1.1/CHANGELOG.html#v2-1-1) were released. Most notable changes include:
  * more `*_info` modules: content_view_info, content_view_version_info, domain_info, host_errata_info, repository_set_info, setting_info, subnet_info, and subscription_info
  * new roles: content_rhel, hostgroups, content_views, organizations, and content_credentials
  * `compute_resource` module can now better manage Azure compute resources
  * important bugfix in 2.1.1: host, hostgroup - don’t override already set parameters when passing an activation key only (and vice versa).
* Ansible Collection for ServiceNow ITSM - [servicenow.itsm](https://galaxy.ansible.com/servicenow/itsm) [1.1.0](https://github.com/ansible-collections/servicenow.itsm/blob/1.1.0/CHANGELOG.rst) released. Most Notable changes include:
  * support for `refresh_token` in the login mechanism
  * support for specifying queries in the `*_info` modules.
* Openstack Ansible Collection - [openstack.cloud](https://galaxy.ansible.com/openstack/cloud) [1.5.0](https://github.com/openstack/ansible-collections-openstack/blob/master/CHANGELOG.rst#v1-5-0) was released with a lot of bugfixes, improvements, and 3 new modules: [address_scope](https://github.com/openstack/ansible-collections-openstack/blob/master/plugins/modules/address_scope.py), [dns_zone_info](https://github.com/openstack/ansible-collections-openstack/blob/master/plugins/modules/dns_zone_info.py), and [floating_ip_info](https://github.com/openstack/ansible-collections-openstack/blob/master/plugins/modules/floating_ip_info.py).
* Podman Ansible Collection - [containers.podman](https://galaxy.ansible.com/containers/podman) [1.6.0](https://github.com/containers/ansible-podman-collections/blob/master/CHANGELOG.rst#v1-6-0) and [1.6.1](https://github.com/containers/ansible-podman-collections/blob/master/CHANGELOG.rst#v1-6-1) were released. New module [podman_play](https://github.com/containers/ansible-podman-collections/blob/master/plugins/modules/podman_play.py) was introduced for playing Kubernetes YAML files as Podman Pods.
* Ansible VMware vSphere Collection - [vmware.vmware_rest](https://galaxy.ansible.com/vmware/vmware_rest) 2.0.0 released (new major version). Notable changes:
  * a new set of modules to manage the vCenter appliances (VCSA)
  * modules to manage Library, including snapshoting and booting VM through an OVF.
* TrendMicro DeepSecurity Ansible Collection - [trendmicro.deepsec](https://galaxy.ansible.com/trendmicro/deepsec) [1.1.0](https://github.com/ansible-collections/trendmicro.deepsec/blob/main/changelogs/CHANGELOG.rst#v110) released. Two new modules are introduced in this release:
  * deepsec_apikey - Create new and manage API Keys
  * deepsec_system_settings - Modify the system settings for TrendMicro Deep Security.
* Docker Community Collection - [community.docker](https://galaxy.ansible.com/community/docker) 1.8.0 has been released with bugfixes and new features.
* Community HashiVault Collection - [community.hashi_vault](https://galaxy.ansible.com/community/hashi_vault) [1.2.0](https://github.com/ansible-collections/community.hashi_vault/releases/tag/1.2.0) and [1.3.0](https://github.com/ansible-collections/community.hashi_vault/releases/tag/1.3.0) have been released. A new [User Guide](https://docs.ansible.com/ansible/devel/collections/community/hashi_vault/docsite/user_guide.html) has also been published providing some detailed information about certain options.
* Community General Collection - [community.general](https://galaxy.ansible.com/community/general) 1.3.11, 2.5.4, and 3.3.0 (plus 3.3.1) have been released. The former two with bugfixes, and the latter with new features and bugfixes.
* Community Sops Collection - [community.sops](https://galaxy.ansible.com/community/sops) [1.1.0](https://github.com/ansible-collections/community.sops/releases/tag/1.1.0) has been released, with a minor change to use public API from Ansible, and the addition of the `decrypt` filter.
* Community RouterOS Collection - [community.routeros](https://galaxy.ansible.com/community/routeros) 1.2.0 has been released.

**ANSIBLE DOCUMENTATION UPDATE**

The [Ansible devel docsite](https://docs.ansible.com/ansible/devel/collections/index.html) will now always include the latest release version (the latest version that's not a prerelease according to semantic versioning) of all collections that will appear in the next Ansible release, instead of using exactly the same versions as the latest Ansible release. This means that `devel` for example includes community.hashi_vault 1.3.0, while the latest Ansible release available at time of writing (ansible-4.1.0) only contains community.hashi_vault 1.1.3. Also if community.hashi_vault 2.0.0 would have been released, it would be used for the `devel` docs, even if future Ansible 4.x.0 releases will only contain 1.y.z releases.

This allows collection developers and users to read documentation for the latest collection release, instead of just having docs for the latest release that's included in some Ansible version.

You can also see that the collection releases mentioned above - theforeman.foreman 2.1.1, community.routeros 1.2.0, and openstack.cloud 1.5.0 - are already documented on [`/devel/`](https://docs.ansible.com/ansible/devel/collections/index.html), while [`/latest/`](https://docs.ansible.com/ansible/latest/collections/index.html) contains older versions of these collections.

**LOOKING FOR COLLECTION MAINTAINERS/CONTRIBUTORS**

The following collections - [community.mysql](https://github.com/ansible-collections/community.mysql/issues/180), [community.postgresql](https://github.com/ansible-collections/community.postgresql/issues/102), and [community.proxysql](https://github.com/ansible-collections/community.proxysql/issues/39) - are looking for new maintainers and contributors! If you are interested, please refer to the corresponding pinned issues linked via the collection names.

**REVIEWS AND FEEDBACK WANTED!**

* Requesting review on [gRPC connection plugin](https://github.com/ansible-collections/ansible.netcommon/pull/279). This PR will add a new connection plugin for gRPC based communication with network hosts.
* Requesting review on [Platform agnostics network resource manager role](https://github.com/ansible-collections/ansible.network/issues/13) for [ansible.network](https://github.com/ansible-collections/ansible.network) collection.
* Ansible has a new open source, data-centric, container-first, developer-friendly interface called [ansible-navigator](https://github.com/ansible/ansible-navigator) which will be included in the next Red Hat Ansible Automation Platform release. We are looking forward to your feedback, issues, and PRs in the [repo](https://github.com/ansible/ansible-navigator). Please help us make this great!

**CONTENT FROM THE ANSIBLE COMMUNITY**

[Sebastian Gumprich](https://github.com/rndmh3ro) wrote a blog post in German on how to convert roles into collections: [Von einer Ansible-Rolle zur Collection – der weg ist das ziel](https://blog.t-systems-mms.com/tech-insights/von-einer-ansible-rolle-zur-collection-der-weg-ist-das-ziel).

**THE ANSIBLE TEAM IS HIRING**

Red Hat is hiring several roles to work on Ansible. Please check the job descriptions in the links and apply!

* [Principal Software Engineer- Ansible](https://global-redhat.icims.com/jobs/86822/principal-software-engineer--ansible/job)
* [DevOps Automation Engineer - Red Hat Ansible](https://global-redhat.icims.com/jobs/82487/devops-automation-engineer---red-hat-ansible/job)

**ANSIBLE CONTRIBUTOR SUMMIT AND SURVEY** 

Thanks to everyone who participated in the [Ansible Contributor Summit 2021.06](https://hackmd.io/@ansible-community/contrib-summit-202106) on June 8, 2021! We are slightly delayed with the editing of the recordings, and will have the videos and logs available in the [Ansible Community wiki](https://github.com/ansible/community/wiki/Contributor-Summit) soon. In the meantime, please take a few minutes to fill in the [Contributor Survey](https://www.surveymonkey.co.uk/r/3YBYKTS) that we have put together.

The next Contributor Summit will take place alongside AnsibleFest. The dates are not confirmed yet, but it will be in the week of September 27, 2021. Details to follow!

**FEEDBACK**

Have any questions you’d like to ask, or issues you’d like to see covered? Please send us an email at the-bullhorn@redhat.com.



