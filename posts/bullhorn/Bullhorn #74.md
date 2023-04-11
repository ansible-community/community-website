---
title: "Bullhorn #74"
date: 2022-09-16 23:00 UTC
tags: news
category: bullhorn
type: text
---

![Ansible Bullhorn banner](/images/bullhorn-banner-mango.png)

*A Newsletter for the Ansible Developer Community*
*Issue #74, 2022-09-16 ([Past Issues](https://us19.campaign-archive.com/home/?u=56d874e027110e35dea0e03c1&id=d6635f5420))*

Welcome to [The Bullhorn](https://github.com/ansible/community/wiki/News#the-bullhorn), our newsletter for the Ansible developer community. If you have any questions or content you’d like to share, you're welcome to chat with us in the [Ansible Social room on Matrix](https://matrix.to/#/#social:ansible.com), and mention [`newsbot`](https://matrix.to/#/@newsbot:ansible.im) to have your news item tagged for review for the next weekly issue!

<!-- TEASER_END -->

## KEY DATES ⏱️

[cybette](https://matrix.to/#/@cybette:ansible.im) said

> * 2022-09-19: [ansible-core feature freeze, stable-2.14 branch created](https://docs.ansible.com/ansible-core/devel/roadmap/ROADMAP_2_14.html) (related to upcoming [Ansible 7](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_7.html))
> * 2022-09-20: [DaWGs meeting](https://github.com/ansible/community/issues/643), 15:00 UTC
> * 2022-09-21: [Community WG meeting](https://github.com/ansible/community/issues/645), 18:00 UTC (propose topics [here](https://github.com/ansible-community/community-topics/issues))
> * 2022-09-22: [Bullhorn #75 content deadline](https://github.com/ansible/community/wiki/News#the-bullhorn), 18:00 UTC
> * 2022-09-26: [Start of ansible-core 2.14 betas](https://docs.ansible.com/ansible-core/devel/roadmap/ROADMAP_2_14.html)
> * 2022-09-27: [Ansible-7.0.0 alpha1](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_7.html)
> * 2022-10-04: [ETA for Ansible 6.5.0 release](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_6.html)
> * **2022-10-17: [Ansible Contributor Summit 2022.10](https://ansiblecs202210.eventbrite.com/?aff=hackmd)**
> * **2022-10-18/19: [AnsibleFest 2022](https://www.ansible.com/ansiblefest?sc_cid=7013a000002i5g3AAA)**

## MAJOR NEW RELEASES 🏆️

[john-westcott-iv](https://matrix.to/#/@john-westcott-iv:ansible.im) contributed

> We're happy to announce that the next release of AWX, version 21.6.0 is now available!
> Some notable features include:
> * Allow for projects to be GPG-verified against unexpected changes
> * Add documentation for running development environment in kind
> * Add exception options to the schedule form in the UI
> * Add make target for building personal awx kube image
> * Close database connections while processing job output
> * Fix awx-manage list_instances command to show last seen heartbeat
> * Implement generic OIDC provider for Authentication
> 
> In addition AWX Operator version 0.29.0 has also been released!
> Some notable features include:
> * Allow runtime modification of receptor config without updating configmap
> * Upgrade operator-sdk version from 1.22.2 to 1.23.0
> 
> Please see the releases pages for more details:
> AWX: [https://github.com/ansible/awx/releases/tag/21.6.0](https://github.com/ansible/awx/releases/tag/21.6.0)
> Operator: [https://github.com/ansible/awx-operator/releases/tag/0.29.0](https://github.com/ansible/awx-operator/releases/tag/0.29.0)

### Antsibull [↗](https://github.com/ansible-community/antsibull) 🐂

Tooling for building the `Ansible` package and collection documentation.

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) said

> antsibull-docs 1.5.0 ([changelog](https://github.com/ansible-community/antsibull-docs/blob/main/CHANGELOG.rst#v1-5-0)) has been released with new features and bugfixes. The latest version prevents duplicate filter/test docs, and improves 'version added' formatting.

### Ansible [↗](https://github.com/ansible-collections) 📦️

The `Ansible` package includes `ansible-core` and is a batteries-included package that provides a curated set of Ansible collections. See the [Ansible roadmaps](https://docs.ansible.com/ansible/devel/roadmap/ansible_roadmap_index.html) for future release plans.

[ompragash](https://matrix.to/#/@ompragash:ansible.im) said

> Ansible 6.4.0 is out!❤️
> 🔗https://groups.google.com/g/ansible-devel/c/AtEKw1UGKyY
> 
> 💽You can install it by running the following command or download the release tarball directly from [pypi](https://pypi.python.org/packages/source/a/ansible/ansible-6.4.0.tar.gz):
> 
> ```
> pip install ansible==6.4.0 --user
> ```
> 
> 🚨 New Collections Included Alert:
> 
> * inspur.ispim (version 1.0.1)
> * vultr.cloud (version 1.1.0)
> 
> 🔆Oh and don't miss out the all new `ansible-community` command-line utility added in Ansible 6 that prints the version of the Ansible Community package:
> 
> ```
> $ ansible-community --version
> Ansible community version 6.4.0
> ```
> 
> ➡️Check [Release Notes📦️🗒️](https://github.com/ansible-community/ansible-build-data/blob/main/6/CHANGELOG-v6.rst) and [Ansible 6 Porting Guide](https://docs.ansible.com/ansible/devel/porting_guides/porting_guide_6.html) for more details!

## COLLECTION UPDATES 🪄

[rsicart](https://matrix.to/#/@rsicart:matrix.org) contributed

> The community.mysql collection version [3.5.1](https://github.com/ansible-collections/community.mysql/blob/main/CHANGELOG.rst#v3-5-1) has been released! Special thanks to [andersson007](https://github.com/Andersson007), [laurent-indermuehle](https://github.com/laurent-indermuehle) and [betanummeric](https://github.com/betanummeric)!

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) shared

> community.general 5.6.0 ([changelog](https://github.com/ansible-collections/community.general/blob/stable-5/CHANGELOG.rst#v5-6-0)) has been released with new features and bugfixes.

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) shared

> community.sops 1.4.0 ([changelog](https://github.com/ansible-collections/community.sops/blob/main/CHANGELOG.rst#v1-4-0)) has been released with age support.

[andersson007_](https://matrix.to/#/@andersson007_:matrix.org) shared

> The [vultr.cloud](https://galaxy.ansible.com/vultr/cloud) colletion has passed the [Colletion inclusion procedure](https://github.com/ansible-collections/ansible-inclusion/blob/main/README.md) and will be included in the next minor release of Ansible 6.

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) contributed

> community.routeros 2.3.0 ([changelog](https://github.com/ansible-collections/community.routeros/blob/main/CHANGELOG.rst#v2-3-0)) has been released with new features and bugfixes for the API modules.

## THE ANSIBLE TEAM IS HIRING 💰️

[gundalow](https://matrix.to/#/@gundalow:ansible.im) said

> ### Join the Ansible Controller Team
> 
> The Red Hat Ansible Controller Engineering team (which you may know as its upstream name, [AWX](https://github.com/ansible/awx), or old name of Ansible Tower) is looking for a **Python Software Engineer** to join us. In this role, you will add new functionality to and maintain released versions of automation controller by contributing to the design of new features, implementing features from designs, identifying root causes and fixing complex issues, assisting technical support with customer escalations, identifying and resolving gaps in the Continuous Integration (CI) pipeline, and developing needed enhancements. To succeed in this role, you’ll need to be friendly, curious, be willing to learn and teach, be sensitive to the perspectives of others, and care about creating a positive and inclusive environment.
> Successful applicants must reside in a state where Red Hat is registered to do business.
> 
> What you will do
> 
> * Contribute to the design and perform the implementation of new features in automation controller
> * Troubleshoot customer-reported issues, guide in-house issue reproduction, determine root causes, describe issues in detail to fellow engineers and customers, and develop software code changes to resolve issues
> * Regularly communicate and interact with open source communities to provide guidance and understand issues; review community pull requests (PRs)
> * Work closely with technical support, documentation, and quality assurance (QA) teams to identify and deliver improvements to test automation, documentation, and knowledge base for automation controller
> * Develop and deliver customer-focused enhancements in maintenance releases
> * Investigate and recommend strategic improvements for tools and processes to advance and expand efficiency and throughput
> 
> Interested in helping us make Ansible Controller better? [Apply now](https://us-redhat.icims.com/jobs/95831/software-engineer/job?hub=7)

[cybette](https://matrix.to/#/@cybette:ansible.im) shared

> ### Join the Ansible Community Team
> 
> The Red Hat Ansible Community team is looking for a **Senior Software Community Engineer** to join us!
> 
> In this role, you will work as part of a team focused on flourishing our amazing upstream community. The Ansible ecosystem is always growing and expanding. We want you to be part of the team that engages and keeps this community vibrant.
> 
> To find out more and apply, check out the [job description](https://global-redhat.icims.com/jobs/96607/senior-software-community-engineer/job). Note that this is a flexible Remote - global position, available in any country/state where Red Hat has a corporate presence.

## THAT'S ALL FOR NOW!

Have any questions you’d like to ask, or issues you’d like to see covered? Please ask in [#social:ansible.com](https://matrix.to/#/#social:ansible.com)! See you next time!
