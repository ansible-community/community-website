---
title: "Bullhorn #17"
date: 2021-01-06 17:00 UTC
tags: news
category: bullhorn
type: text
---

![Ansible Bullhorn banner](/images/bullhorn-banner-mango.png)

## The Bullhorn

*A Newsletter for the Ansible Developer Community*
*Issue #17, 2021-01-06 ([Past Issues](https://us19.campaign-archive.com/home/?u=56d874e027110e35dea0e03c1&id=d6635f5420))*

Welcome to the Bullhorn, our newsletter for the Ansible developer community. If you have any questions or content you’d like to share, please reach out to us at the-bullhorn@redhat.com, or comment on this [GitHub issue](https://github.com/ansible/community/issues/546).

<!-- TEASER_END -->

**KEY DATES**

* 2021-01-06: [community IRC meeting](https://github.com/ansible/community/issues/539), 19:00 UTC
* 2021-01-07: [D&I working group meeting](https://github.com/ansible/community/issues/577), 19:00 UTC
* 2021-01-13: [community IRC meeting](https://github.com/ansible/community/issues/539), 19:00 UTC
* 2021-01-18: [Bullhorn #18 content deadline](https://github.com/ansible/community/issues/546)
* 2021-01-18: ETA for Ansible-base 2.10.5 release
* 2021-01-26: ETA for Ansible 2.10.6 release
* 2021-01-27: New collections to be included in Ansible 3.0.0 must be **reviewed and approved** by this date.
    * Please submit your new collections for review as early as possible because we have limited reviewers. Submissions made close to the deadline may not have time to be reviewed and approved in time for inclusion.
* 2021-02-16: [ETA for Ansible 3.0.0 release](https://github.com/ansible/ansible/blob/devel/docs/docsite/rst/roadmap/COLLECTIONS_3_0.rst)

**ACCEPTING NEW COLLECTIONS FOR ANSIBLE 3.0.0**

The [criteria for accepting new collections for Ansible 3.0.0](https://github.com/ansible-collections/overview/blob/main/collection_requirements.rst) (scheduled for release in February) have been approved.

If you would like your collection to be included in ansible-3.0.0, please try to make your collection conform to [the requirements](https://github.com/ansible-collections/overview/blob/main/collection_requirements.rst) and then [submit it as a discussion](https://github.com/ansible-collections/ansible-inclusion/discussions/new).

- When you start the discussion, please include a link to the collection on galaxy, a link to the source code repository, a link to the issue tracker, and the GitHub IDs of collection owners that we should contact if there's a problem with the collection later.
- We will review the new collection requests that have been submitted on a first-come, first-served basis. The earlier you submit your collection, the more likely you are to get it into 3.0.0.
- The review may turn up things that need to be fixed which would delay acceptance.
- 2021-01-27 is the date by which new collections **must be reviewed and accepted**, so get your collection in as early as possible, i.e. **NOW**! Submitting it close to the deadline may mean that there is not enough time for us to review and approve it resulting in it not being accepted.

The procedure for getting new collections in is **highly likely** to change for the Ansible 4.0.0 release (including who reviews, whether it remains first-come first-served, and so forth).

**ANSIBLE 2.10.5 NOW GENERALLY AVAILABLE**

The Ansible Community team announced the general availability of Ansible 2.10.5 on January 5th. This update contains bug fixes and new, backwards compatible features in the contained collections. For more information on what’s new, how to get it, plus schedule for upcoming releases, read [Deric Crago’s announcement to the ansible-devel mailing list](https://groups.google.com/g/ansible-devel/c/QXx1SXJk05c).

**NEW/UPDATED COMMUNITY COLLECTIONS**

- The [MySQL collection for Ansible 1.1.2](https://galaxy.ansible.com/community/mysql) has been released.
- [Ansible Podman collections](https://galaxy.ansible.com/containers/podman) has a big [update](https://github.com/containers/ansible-podman-collections/blob/master/CHANGELOG.rst) to 1.4.0 and 1.4.1 releases. There are new modules for login management - [podman_logout](https://github.com/containers/ansible-podman-collections/blob/master/plugins/modules/podman_logout.py) and [podman_login_info](https://github.com/containers/ansible-podman-collections/blob/master/plugins/modules/podman_login_info.py). A new module [podman_containers](https://github.com/containers/ansible-podman-collections/blob/master/plugins/modules/podman_containers.py) allows you to run multiple Podman containers at once, which saves time and performs faster if you need to run multiple containers in a row. We have also added a few network related features like IPv6, MAC addresses, MTU and VLAN configs, etc.
- The [community.hashi_vault Collection](https://galaxy.ansible.com/community/hashi_vault) [1.0.0](https://github.com/ansible-collections/community.hashi_vault/releases/tag/1.0.0) has been released on 2020-12-30. The hashi_vault lookup plugin will be [removed/redirected](https://github.com/ansible-collections/community.general/pull/1566) from community.general 2.0.0, i.e. for Ansible 3.0.0.
- [Docker Community Collection 1.1.0](https://galaxy.ansible.com/community/docker) has been released with a few new plugins and modules and other new features.
- The [Ansible Openstack collection](https://galaxy.ansible.com/openstack/cloud) released [1.2.1](https://github.com/openstack/ansible-collections-openstack/blob/master/CHANGELOG.rst#v1-2-1) version, with a lot of bug fixes and improvements.
- The [community.vmware collection 1.6.0](https://galaxy.ansible.com/community/vmware) has been released with a lot of improvements, fixes, and a new module.
- The [KubeVirt Collection for Ansible 1.0.0](https://galaxy.ansible.com/community/kubevirt) has been released and will be contained in [Ansible 2.10.5](https://groups.google.com/g/ansible-devel/c/QXx1SXJk05c) (next to the new collections [cisco.nso](https://galaxy.ansible.com/cisco/nso), [community.google](https://galaxy.ansible.com/community/google), and [community.hashi_vault](https://galaxy.ansible.com/community/hashi_vault)). Note that cisco.nso contains modules that will be removed from [community.network](https://galaxy.ansible.com/community/network) 2.0.0, while the other mentioned collections (community.kubevirt, community.google, community.hashi_vault) contain modules and plugins that will be removed from [community.general](https://galaxy.ansible.com/community/general) 2.0.0.

**PROPOSAL FOR ANSIBLE NETWORKING**

The Ansible Network Engineering Team is cordially welcoming comments from the Ansible Network community for the following proposal: [BGP Global and AF Context Resource Model](https://github.com/ansible/community/issues/582). The enablement of BGP as network resource modules for supported platforms has long been requested, and is now being scoped and planned for implementing this year. Please provide feedback in the next few weeks!

**ANSIBLE COMMUNITY STATS UPDATE**

For the last bit of fun in 2020, [Greg re-did](https://twitter.com/Gwmngilfen/status/1341417009968537600) the [2019 bubble plot](https://emeraldreverie.org/2019/12/19/visualising-the-community-contributions-to-ansible-modules/) for the new world of Collections. As before, it shows the amount of contribution to the various collections, coloured by the amount of contribution from staff vs community.

![](https://pbs.twimg.com/media/Ep2rX4HXcAAboMf?format=jpg&name=4096x4096)

**DIVERSITY & INCLUSION WORKING GROUP MEETING**

The first Diversity WG meetings will be this week on January 7th at 19:00 UTC in IRC channel `#ansible-diversity`, and take place every other week. Submit agenda items in this [GitHub issue](https://github.com/ansible/community/issues/577).

**CONTENT FROM THE ANSIBLE COMMUNITY**

ara 1.5.4 has been released:
- See the [changelog](https://ara.readthedocs.io/en/latest/changelog-release-notes.html)
- The new version is already available on: [PyPi](https://pypi.org/project/ara/), [DockerHub](https://hub.docker.com/r/recordsansible/ara-api), and [Quay](https://quay.io/repository/recordsansible/ara-api) as well as Fedora

**ANSIBLE VIRTUAL MEETUPS**

The following virtual meetups are being held in the Ansible community over the next month:

* Tue, Jan 19 · 6:00 PM GMT+1 - [Ansible Meetup Dresden](https://www.meetup.com/Ansible-Meetup-Dresden/events/275316369/) - Meetup 01.2021

**FEEDBACK**

Have any questions you’d like to ask, or issues you’d like to see covered? Please send us an email at the-bullhorn@redhat.com.
