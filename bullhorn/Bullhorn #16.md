---
title: "Bullhorn #16"
date: 2020-12-16 17:00 UTC
tags: news
category: bullhorn
type: text
---

![Ansible Bullhorn banner](/images/bullhorn-banner-mango.png)

## The Bullhorn

*A Newsletter for the Ansible Developer Community*
*Issue #16, 2020-12-16 ([Past Issues](https://us19.campaign-archive.com/home/?u=56d874e027110e35dea0e03c1&id=d6635f5420))*

Welcome to the Bullhorn, our newsletter for the Ansible developer community. If you have any questions or content you’d like to share, please reach out to us at the-bullhorn@redhat.com, or comment on this [GitHub issue](https://github.com/ansible/community/issues/546).

<!-- TEASER_END -->

**KEY DATES**

* 2020-12-16: [community IRC meeting](https://github.com/ansible/community/issues/539), 19:00 UTC
* 2020-12-17: [PR Review day](https://github.com/ansible/community/issues/407), 15:00 UTC
* 2021-01-04: [Bullhorn #17 content deadline](https://github.com/ansible/community/issues/546)
* 2021-01-05: ETA for ansible 2.10.5 release
* 2021-01-06: [community IRC meeting](https://github.com/ansible/community/issues/539), 19:00 UTC
* 2021-01-07: [D&I working group meeting](https://github.com/ansible/community/issues/577), 19:00 UTC
* 2021-01-18: ETA for ansible-base 2.10.5 release
* 2021-01-27: New collections to be included in Ansible 3.0.0 must be **reviewed and approved** by this date.
    * Please submit your new collections for review as early as possible because we have limited reviewers. Submissions made close to the deadline may not have time to be reviewed and approved in time for inclusion.
* 2021-02: [release schedule for Ansible 3.0.0](https://github.com/ansible/ansible/blob/devel/docs/docsite/rst/roadmap/COLLECTIONS_3_0.rst)

**ACCEPTING NEW COLLECTIONS FOR ANSIBLE 3.0.0**

The [criteria for accepting new collections for Ansible 3.0.0](https://github.com/ansible-collections/overview/blob/main/collection_requirements.rst) (releasing in February) have been approved.

If you would like your collection to be included in ansible-3.0.0, please try to make your collection conform to [the requirements](https://github.com/ansible-collections/overview/blob/main/collection_requirements.rst) and then [submit it as a discussion](https://github.com/ansible-collections/ansible-inclusion/discussions/new).

- When you start the discussion, please include a link to the collection on galaxy, a link to the source code repository, a link to the issue tracker, and the GitHub IDs of collection owners that we should contact if there's a problem with the collection later.
- We will review the new collection requests that have been submitted on a first-come, first-served basis. The earlier you submit your collection, the more likely you are to get it into 3.0.0.
- The review may turn up things that need to be fixed which would delay acceptance.
- 2021-01-27 is the date by which new collections **must be reviewed and accepted**, so get your collection in as early as possible! Submitting it close to the deadline may mean that there is not enough time for us to review and approve it resulting in it not being accepted.

The procedure for getting new collections in is **highly likely** to change for the Ansible 4.0.0 release (including who reviews, whether it remains first-come first-served, and so forth).

**ANSIBLE-BASE 2.10.4 NOW GENERALLY AVAILABLE**

The Ansible Core team announced the general release of Ansible-Base 2.10.4 on December 14th. This ansible-base package consists of only the Ansible execution engine, related tools (e.g. ansible-galaxy, ansible-test), and a very small set of built-in plugins, and is also bundled with the larger Ansible distribution. For more information on how to download, test, and report issues, read [Rick Elrod’s announcement to the ansible-devel mailing list](https://groups.google.com/g/ansible-devel/c/FLUKcVQY-NI).

**ANSIBLE 2.9.16 AND 2.8.18 RELEASED**

The Ansible Core team announced the availability of Ansible 2.9.16 and Ansible 2.8.18 on December 14th, both of which are maintenance releases. Follow [this link](https://groups.google.com/g/ansible-devel/c/os1npQgJgVc) for Rick Elrod’s email to the ansible-devel mailing list, to obtain details on what’s new, installation instructions, and links to the full changelogs.

**NEW/UPDATED COMMUNITY COLLECTIONS**

- The [Foreman Ansible Collection 1.5.0](https://theforeman.org/2020/12/foreman-ansible-modules-v150-released.html) was released on December 3rd, followed by a minor update to [theforeman.foreman 1.5.1](https://galaxy.ansible.com/theforeman/foreman), fixing a bug that got introduced in 1.5.0.
- The Community Hetzner Robot Collection, [community.hrobot 1.1.0](https://galaxy.ansible.com/community/hrobot) has been released with an inventory plugin.
- The Sensu Go Ansible Collection, [sensu.sensu_go 1.7.0](https://galaxy.ansible.com/sensu/sensu_go) has just been released for your monitoring needs on Amazon Linux and Windows hosts.

**ANSIBLE CONTIRBUTOR SURVEY DATA**

[Greg](https://twitter.com/gwmngilfen) has started some deep dives into the data from the first 3 Contributor Summit surveys we ran during 2020. He's written up [three](https://emeraldreverie.org/2020/12/16/community_survey_data_p1/) [whole](https://emeraldreverie.org/2020/12/16/community_survey_data_p2/) [posts](https://emeraldreverie.org/2020/12/16/community_survey_data_p3/) on how the survey is designed, and what it has to say about burnout and contribution blockers in Ansible. Here's a teaser:

![Screenshot](https://emeraldreverie.org/post/2020-12-16-community-survey-data-burnout-and-blockers/time_coeffs.png)

**DIVERSITY & INCLUSION WORKING GROUP MEETING**

The Diversity WG meetings will begin next year on January 7th at 19:00 UTC in IRC channel `#ansible-diversity`, and take place every other week. Submit agenda items in this [GitHub issue](https://github.com/ansible/community/issues/577).

**ANSIBLE DOCUMENTATION SURVEY**

We have created a [one-page survey](https://www.surveymonkey.co.uk/r/B7PDVSB) about the Ansible documentation. If you use [docs.ansible.com](https://docs.ansible.com/), we’d love to hear your views! We’re hoping to learn whether different types of users need different types of documentation. We’re also interested in what the most common pain points are for documentation. The survey will be open until December 31st, 2020. Please [fill out the survey](https://www.surveymonkey.co.uk/r/B7PDVSB) and pass the word!

**CONTENT FROM THE ANSIBLE COMMUNITY**

Following up on his previous article about [CI of the Ansible modules for VMware](https://goneri.lebouder.net/2020/08/21/vmware-ci-of-ansible-modules-a-retrospective/), [Gonéri Le Bouder](https://github.com/goneri) explains [how to prepare the vSphere instances for the VMware CI](https://goneri.lebouder.net/2020/12/14/ansible-how-we-prepare-the-vsphere-instance-for-the-vmware-ci/).

**SEASON'S GREETINGS**

This will be the last issue of The Bullhorn for 2020. Thanks for all your support and contributions. Warm greetings from the Ansible Community Team, and see you in 2021!

![](https://i.imgur.com/Af0De4D.png)

**FEEDBACK**

Have any questions you’d like to ask, or issues you’d like to see covered? Please send us an email at the-bullhorn@redhat.com.
