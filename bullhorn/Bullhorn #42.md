---
title: "Bullhorn #42"
date: 2022-01-14 10:30 UTC
tags: news
category: bullhorn
type: text
---

![Ansible Bullhorn banner](/images/bullhorn-banner-mango.png)

*A Newsletter for the Ansible Developer Community*
*Issue #42, 2022-01-14 ([Past Issues](https://us19.campaign-archive.com/home/?u=56d874e027110e35dea0e03c1&id=d6635f5420))*

Welcome to the Bullhorn, our newsletter for the Ansible developer community. If you have any questions or content you’d like to share, please reach out to us at the-bullhorn@redhat.com, or chat with us in the [Ansible Social room on Matrix](https://matrix.to/#/#social:ansible.com) - mention [`newsbot`](https://matrix.to/#/@newsbot:ansible.im) to have your news item tagged for review for the next issue!

<!-- TEASER_END -->

## KEY DATES

[cybette](https://matrix.to/#/@cybette:ansible.im) shared

> * 2022-01-18: [DaWGs meeting](https://github.com/ansible/community/issues/643), 16:00 UTC
> * 2022-01-19: [Community WG meeting](https://github.com/ansible/community/issues/645), 18:00 UTC (propose topics [here](https://github.com/ansible-community/community-topics/issues))
> * 2022-01-25: [DaWGs meeting](https://github.com/ansible/community/issues/643), 16:00 UTC
> * 2022-01-26: [Community WG meeting](https://github.com/ansible/community/issues/645), 18:00 UTC (propose topics [here](https://github.com/ansible-community/community-topics/issues))
> * 2022-01-26: [Bullhorn #43 content deadline](https://github.com/ansible/community/issues/546)
> * 2022-01-31: ETA for Ansible-Core 2.12.2, Ansible-Core 2.11.8, and Ansible-Base 2.10.17 releases (if those releases have updates)
> * 2022-02-01: [ETA for Ansible 5.3.0 release](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_5.html)

## GENERAL NEWS UPDATES

[dmsimard](https://matrix.to/#/@dmsimard:matrix.org) contributed

> We are opening a call for proposals to the wider community for a monthly Ansible community meetup we would like to run on Matrix, IRC and Jitsi to fill in the gap between editions of AnsibleFest and Ansible Contributor Summits.
> While you can expect updates from the Ansible community and engineering teams, we would love to hear about your Ansible tips, projects and stories whether you are a user, a contributor or a developer.
> 
> If you are interested to do a proposal or would like to suggest an idea or topic for someone to talk about, please head to the GitHub repository we have prepared for the occasion: https://github.com/ansible-community/meetup
> 
> Thank you and we are looking forward to your proposals and ideas!

### Ansible [↗](https://github.com/ansible-collections)

The `Ansible` package includes `ansible-core` and is a batteries-included package that provides a curated set of Ansible collections. See the [Ansible roadmaps](https://docs.ansible.com/ansible/devel/roadmap/ansible_roadmap_index.html) for future release plans.

[samccann](https://matrix.to/#/@smccann:matrix.org) said

> We have updated the module/plugin tables in Ansible documentation so they work better on smaller screens and include links when a module name is mentioned. This is only available on devel docs so far. See examples - https://docs.ansible.com/ansible/devel/collections/community/crypto/acme_certificate_module.html#parameters and https://docs.ansible.com/ansible/devel/collections/community/hashi_vault/hashi_vault_lookup.html#parameters. Feedback welcome!

## MAJOR NEW RELEASES

### Ansible [↗](https://github.com/ansible-collections)

The `Ansible` package includes `ansible-core` and is a batteries-included package that provides a curated set of Ansible collections. See the [Ansible roadmaps](https://docs.ansible.com/ansible/devel/roadmap/ansible_roadmap_index.html) for future release plans.

[dmsimard](https://matrix.to/#/@dmsimard:matrix.org) shared

> ansible 5.2.0 has been released: https://groups.google.com/g/ansible-announce/c/iEXVScuWHfI -- it includes updates from cisco.meraki, community.crypto, community.dns, community.docker, community.general, community.hashi_vault, community.hrobot, community.proxysql, dellemc.openmanage, netbox.netbox, purestorage.flasharray and t_systems_mms.icinga_director.

## COLLECTION UPDATES

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) said

> community.crypto 2.1.0 has been released with some new modules and bugfixes ([changelog](https://github.com/ansible-collections/community.crypto/blob/main/CHANGELOG.rst)).

[sshnaidm](https://matrix.to/#/@sshnaidm:matrix.org) said

> [openstack.cloud](https://galaxy.ansible.com/openstack/cloud) collection released 1.6.0 version, we've got new RBAC modules for neutron - [neutron_rbac_policy](https://opendev.org/openstack/ansible-collections-openstack/src/branch/master/plugins/modules/neutron_rbac_policy.py), [neutron_rbac_policies_info](https://opendev.org/openstack/ansible-collections-openstack/src/branch/master/plugins/modules/neutron_rbac_policies_info.py) and new module for discovering Nova services - [compute_service_info](https://opendev.org/openstack/ansible-collections-openstack/src/branch/master/plugins/modules/compute_service_info.py), and a few bugfixes of course.

[sshnaidm](https://matrix.to/#/@sshnaidm:matrix.org) said

> [containers.podman](https://github.com/containers/ansible-podman-collections) collection released new 1.9.1 version, since last update we have new podman_tag module, also updated module podman_secret which manages secrets for Pods and options for newest Podman Pod versions.

[markuman](https://matrix.to/#/@markuman:libera.chat) contributed

> community.aws 3.0.0 has just been released.

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) shared

> community.general 4.3.0 has been released with new features and bugfixes ([changelog](https://github.com/ansible-collections/community.general/blob/stable-4/CHANGELOG.rst)).

## HELP WANTED

[samccann](https://matrix.to/#/@smccann:matrix.org) contributed

> Looking for a way to contribute to Ansible? How about starting with one of these easyfix issues? https://github.com/ansible/ansible/issues?q=is%3Aopen+is%3Aissue+label%3Aeasyfix

## PROPOSALS - DISCUSS AND VOTE!

[gundalow](https://matrix.to/#/@gundalow:ansible.im) said

> We are looking at improving the consistency of Ansible plugin documentation by requiring FQCN (Fully Qualified Collection Names) for all plugins, including `builtin` (i.e. those plugins included in `ansible-core`). This allows examples to be copied and pasted without you updating your `collections:` keyword. Full details of the proposal and the ability to record your vote can be done in [community-topics#58](https://github.com/ansible-community/community-topics/issues/58).

[gundalow](https://matrix.to/#/@gundalow:ansible.im) shared

> We are looking at mentioning the plugin type more prominently on docs.ansible.com. This is due to [feedback](https://github.com/ansible-community/community-topics/issues/57) that it's confusing when there are two plugins with the same name, i.e. `file` (lookup or module). Full details of the proposal, and the ability to record your vote can be done via [community-topic#61](https://github.com/ansible-community/community-topics/issues/61).

[gundalow](https://matrix.to/#/@gundalow:ansible.im) shared

> We are looking at reducing the maintenance for old stable branches for [community.general](https://github.com/ansible-collections/community.general/) and [community.network](https://github.com/ansible-collections/community.network/) collection repositories. We'd welcome your feedback, in particular if you think you may be negatively impacted by the change. Full details of the proposal, and the ability to record your vote can be done via [community-topic#55](https://github.com/ansible-community/community-topics/issues/55).

## COMMUNITY UPDATES

[cybette](https://matrix.to/#/@cybette:ansible.im) contributed

> Looking for a great way to hone your automation skills? Check out the early release of [“Ansible: Up and Running, 3rd Edition”](https://www.oreilly.com/library/view/ansible-up-and/9781098109141/) by [Bas Meijer](https://github.com/bbaassssiiee) et al. on O’Reilly and get up & running in no time!

## COMMUNITY EVENTS AND MEETUPS

[Gwmngilfen](https://matrix.to/#/@gwmngilfen:ansible.im) said

> ### FOSDEM 2022 - Ansible & Matrix, 6(ish) months on
> 
> As part of the [FOSDEM Matrix devroom](https://fosdem.org/2022/schedule/event/matrix_ansible/), I'll be taking a look at our journey so far with Matrix - where we came from, how we got to here, what's gone well (or not), and what I hope we'll achieve in the next chunk of time. Me being me, there will be graphs as well ;)
> 
> I'm also looking for feedback on how _you_ have found the journey so far, whether as an existing user of either Matrix or IRC, or as someone who has moved over. You'll have to be quick though, as I need to record the final version by Friday 21st!

[cybette](https://matrix.to/#/@cybette:ansible.im) contributed

> Join [Ansible Singapore](https://www.meetup.com/ansible-singapore/) group in [Ansible Virtual Meet Up - January 2022](https://www.meetup.com/Ansible-Singapore/events/283214898/) on Thursday, Jan 20. Check the details and RSVP [here](https://www.meetup.com/Ansible-Singapore/events/283214898/).

[cybette](https://matrix.to/#/@cybette:ansible.im) shared

> I'll be sharing [Lessons from 6 Virtual Ansible Contributor Summits](https://fosdem.org/2022/schedule/event/conference_ansible_lessons/) in [FOSDEM 2022](https://fosdem.org/2022/)'s [Conference Organisation devroom](https://fosdem.org/2022/schedule/track/conference_organisation/) on Saturday, Feb 5, 2022. Check out other [Ansible-related happenings](https://fosdem.org/2022/search/?q=ansible) at FOSDEM!

## THAT'S ALL FOR NOW!

Have any questions you’d like to ask, or issues you’d like to see covered? Please ask in [#social:ansible.com](https://matrix.to/#/#social:ansible.com)! See you next time!
