---
title: "Bullhorn #82"
date: 2022-11-25 01:00 UTC
tags: news
category: bullhorn
type: text
---

![Ansible Bullhorn banner](/images/bullhorn-banner-mango.png)

*A Newsletter for the Ansible Developer Community*
*Issue #82, 2022-11-24 ([Past Issues](https://us19.campaign-archive.com/home/?u=56d874e027110e35dea0e03c1&id=d6635f5420))*

Welcome to [The Bullhorn](https://github.com/ansible/community/wiki/News#the-bullhorn), our newsletter for the Ansible developer community. If you have any questions or content you’d like to share, you're welcome to chat with us in the [Ansible Social room on Matrix](https://matrix.to/#/#social:ansible.com), and mention [`newsbot`](https://matrix.to/#/@newsbot:ansible.im) to have your news item tagged for review for the next weekly issue!

<!-- TEASER_END -->

## KEY DATES ⏱️

[cybette](https://matrix.to/#/@cybette:ansible.im) shared

> * 2022-11-29: [DaWGs meeting](https://github.com/ansible/community/issues/643), 16:00 UTC
> * 2022-11-30: [Community WG meeting](https://github.com/ansible/community/issues/645), 19:00 UTC (propose topics [here](https://github.com/ansible-community/community-topics/issues))
> * 2022-12-01: [Bullhorn #83 content deadline](https://github.com/ansible/community/wiki/News#the-bullhorn), 18:00 UTC
> * 2022-12-05: ETA for Ansible-Core 2.14.1 and 2.13.7 releases
> * 2022-12-06: [ETA for Ansible 7.1.0 release](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_7.html)

## GENERAL NEWS UPDATES 🔈️

[Sean Sullivan](https://matrix.to/#/@ssulliva:matrix.org) contributed

> New Matrix room [#aap_config_as_code:ansible.com](https://matrix.to/#/#aap_config_as_code:ansible.com): AAP Configuration as Code Working Group for collections that configure Controller, AWX, Hub, Galaxy and much more.

[samccann](https://matrix.to/#/@samccann:ansible.im) said

> As part of our effort to improve Ansible search results,  the Ansible 2.4 documentation is now archived at https://docs.ansible.com/archive/ansible/2.4/. Please update any bookmarks as we will redirect traffic from the old URL soon to go to `/latest/`.

## MAJOR NEW RELEASES 🏆️

### Ansible [↗](https://github.com/ansible-collections) 📦️

The `Ansible` package includes `ansible-core` and is a batteries-included package that provides a curated set of Ansible collections. See the [Ansible roadmaps](https://docs.ansible.com/ansible/devel/roadmap/ansible_roadmap_index.html) for future release plans.

[chadams](https://matrix.to/#/@chadams:ansible.im) said

> Ansible 7.0.0 is out! ❤️
> 🔗[https://groups.google.com/g/ansible-announce/c/ATu1rGVAz_E](https://groups.google.com/g/ansible-announce/c/ATu1rGVAz_E)
> 
> 💽You can install it by running the following command or download the release tarball directly from [pypi](https://pypi.python.org/packages/source/a/ansible/ansible-7.0.0.tar.gz):
> 
> ```
> pip install ansible==7.0.0 --user
> ```
> 
> ➡️ Check [Release Notes📦️🗒️](https://github.com/ansible-community/ansible-build-data/blob/main/7/CHANGELOG-v7.rst) and [Ansible 7 Porting Guide](https://docs.ansible.com/ansible/devel/porting_guides/porting_guide_7.html) for more details!

### AWX Project [↗](https://github.com/ansible/awx) 

AWX provides a web-based user interface, REST API, and task engine built on top of Ansible.

[Lila Yasin](https://matrix.to/#/@lyasin:matrix.org) contributed

> We're happy to announce that the next release of AWX, version 21.9.0 is now available!
> 
> Some notable features include:
> * Refactor test_get_cleanup_task_kwargs_active_jobs and add new test
> * Enable feature branch api-schema test
> * Add node_type to instance info and capacity metrics
> * Update awx collection workflow module schema with new options
> 
> In addition, AWX Operator version 1.1.0 has also been released!
> 
> Some notable features include:
> * Backup and restore receptor tls secret with expected generated name
> 
> Please see the releases pages for more details:
> 
> AWX: [https://github.com/ansible/awx/releases/tag/21.9.0](https://github.com/ansible/awx/releases/tag/21.9.0)
> Operator: [https://github.com/ansible/awx-operator/releases/tag/1.1.0](https://github.com/ansible/awx-operator/releases/tag/1.1.0)

## COLLECTION UPDATES 🪄

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) shared

> community.routeros 2.4.0 ([changelog](https://github.com/ansible-collections/community.routeros/blob/main/CHANGELOG.rst#v2-4-0)) with many improvements of the API modules.

[sshnaidm](https://matrix.to/#/@sshnaidm:matrix.org) contributed

> New version [1.10.0](https://github.com/containers/ansible-podman-collections/blob/master/CHANGELOG.rst#v1-10-0) of Ansible Podman collection was released. We have a lot of bugfixes and improvements, a new become plugin - [podman_unshare](https://github.com/containers/ansible-podman-collections/blob/master/plugins/become/podman_unshare.py) which allows user to execute commands in its container user namespace, and a new module - [podman_generate_systemd](https://github.com/containers/ansible-podman-collections/blob/master/plugins/modules/podman_generate_systemd.py) for Systemd unit files generation for containers and pods.

[Sean Sullivan](https://matrix.to/#/@ssulliva:matrix.org) said

> The redhat_cop collections are changing namespaces to infra. The collection will continue to publish all collections to redhat_cop for another 6 months.
> 
> All of the collections in this group have recently released changes. This includes:
> * infra.controller_configuration 2.1.9 released to be compatible with recently added AWX changes. Changelog [here](https://github.com/redhat-cop/controller_configuration/blob/devel/changelogs/changelog.yaml).
> * infra.ah_configuration 0.9.2 Automation hub and galaxy_ng configuration. Fixed various major errors, including a major publishing error. Changelog [here](https://github.com/redhat-cop/ah_configuration/blob/devel/changelogs/changelog.yaml).
> * infra.ee_utilities 2.0.1 Updated to add several use cases to Execution Environment Creation.
> * infra.aap_utilities 2.2.2 Update to OCP installer to allow individual components.

## HELP WANTED 🙏

[andersson007_](https://matrix.to/#/@andersson007_:matrix.org) shared

> The following collection inclusion requests are waiting for your review:
> 
> * [dellemc.unity](https://github.com/ansible-collections/ansible-inclusion/discussions/32)
> 
> See the [process description](https://github.com/ansible-collections/ansible-inclusion#review-process) to learn how to do it.
> 
> If you have any questions, just ping `andersson007` on [Matrix](https://docs.ansible.com/ansible/devel/community/communication.html#ansible-community-on-matrix) in the [#community:ansible.com](https://matrix.to/#/#community:ansible.com) room or on [Libera.Chat IRC](https://docs.ansible.com/ansible/devel/community/communication.html#ansible-community-on-irc) in the `#ansible-community` channel or directly.
> 
> Please help the community extend the Ansible package!

## COMMUNITY UPDATES 👂️

[cybette](https://matrix.to/#/@cybette:ansible.im) shared

> ### Ansible Contributor Survey
> 
> Feedback is really important to us so we can keep on improving the Contributor Experience for our wonderful Ansible Community. Please take a few minutes to fill in the [Contributor Survey](https://www.surveymonkey.co.uk/r/7PK28F8) that we have put together!

[steampunks](https://matrix.to/#/@xlab_steampunk:matrix.org) contributed

> We were going to present our tool for Ansible Playbook developers at the Ansible Contributor Summit last month, but unfortunately our flight was delayed, and we missed the session. Now, we have recorded a demo where you can see Steampunk Spotter in action: https://www.youtube.com/watch?v=YG0h_fYn-TY

## COMMUNITY EVENTS AND MEETUPS 📅

[cybette](https://matrix.to/#/@cybette:ansible.im) said

> [**Ansible Zürich**](https://www.meetup.com/ansible-zurich/) will be having their [11th Ansible Meetup](https://www.meetup.com/ansible-zurich/events/288952760/) on November 29 (Tuesday). There are 3 topics planned: "Infrastructure deployment and infrastructure as code in Microsoft Azure", "Ansible LFOps - Managing RHEL-based datacenter influenced by DebOps", and "Simple Ansible hacks". Check out the [details and RSVP](https://www.meetup.com/ansible-zurich/events/288952760/).
> 
> [**Ansible London** meetup on 14th December](https://www.meetup.com/ansible-london/events/289470467/) has been cancelled due to rail strike.

[cybette](https://matrix.to/#/@cybette:ansible.im) shared

> ### Cfgmgmtcamp 2023 and Ansible Contributor Summit
> 
> [CfgMgmtCamp](https://cfgmgmtcamp.eu/ghent2023/) will return to Ghent in 2023! Mark your calendars for Feb 6-8. Check out the [CFP](https://cfp.cfgmgmtcamp.org/2023/cfp) looking for presentations, workshops, and fringes (deadline: Sunday, Dec 4).
> 
> Our next Ansible Contributor Summit will be in Europe as a fringe event of Cfgmgmtcamp! It will be held on Wednesday Feb 8, 2023. More details to come, stay tuned!

## THE ANSIBLE TEAM IS HIRING 💰️

[Don Naro](https://matrix.to/#/@orandon:ansible.im) said

> We're hiring! The Ansible team at Red Hat is looking for an **Automation Engineer** who loves automating repetitive tasks, diving deep into source code and systems to perform root-cause analysis of issues. Apply to the **Software Quality team** at [this link](https://global-redhat.icims.com/jobs/96532/automation-engineer---ansible-software-quality/job?hub=7) or share with someone you know.

[Don Naro](https://matrix.to/#/@orandon:ansible.im) contributed

> Another exciting opportunity to join the Ansible team at Red Hat. We're looking for someone who constantly looks for ways to break things and rebuild them better. Come and join the **Quality Engineering team** as a developer who designs and automates creative ways to break software and uncover problems. Apply to the role at [this link](https://us-redhat.icims.com/jobs/97074/senior-software-quality-engineer-ansible-quality-engineering/job?hub=7) or share with someone you know.

## THAT'S ALL FOR NOW!

Have any questions you’d like to ask, or issues you’d like to see covered? Please ask in [#social:ansible.com](https://matrix.to/#/#social:ansible.com)! See you next time!
