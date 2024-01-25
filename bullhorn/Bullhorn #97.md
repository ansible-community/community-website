---
title: "Bullhorn #97"
date: 2023-04-06 06:00 UTC
tags: news
category: bullhorn
type: text
---

![Ansible Bullhorn banner](/images/bullhorn-banner-mango.png)

*A Newsletter for the Ansible Developer Community*
*Issue #97, 2023-04-04 ([Past Issues](https://us19.campaign-archive.com/home/?u=56d874e027110e35dea0e03c1&id=d6635f5420))*

Welcome to [The Bullhorn](https://github.com/ansible/community/wiki/News#the-bullhorn), our newsletter for the Ansible developer community. If you have any questions or content you’d like to share, you're welcome to chat with us in the [Ansible Social room on Matrix](https://matrix.to/#/#social:ansible.com), and mention [`newsbot`](https://matrix.to/#/@newsbot:ansible.im) to have your news item tagged for review for the next weekly issue!

<!-- TEASER_END -->

## KEY DATES ⏱️

[cybette](https://matrix.to/#/@cybette:ansible.im) said

> * 2023-04-11: [DaWGs meeting](https://github.com/ansible/community/issues/678), 15:00 UTC
> * 2023-04-12: [Community WG meeting](https://github.com/ansible/community/issues/679), 18:00 UTC (propose topics [here](https://github.com/ansible-community/community-topics/issues))
> * 2023-04-13: [Bullhorn #98 content deadline](https://github.com/ansible/community/wiki/News#the-bullhorn), 18:00 UTC
> * 2023-04-24: ETA for Ansible-Core 2.14.5 and 2.15.0rc1
> * 2023-04-25: [ETA for Ansible 7.5.0 release](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_7.html)

## GENERAL NEWS UPDATES 🔈️

[Gwmngilfen](https://matrix.to/#/@gwmngilfen:ansible.im) said

> ### Contributor Summit & Community survey results for Feb
> 
> After CfgMgmtCamp and Ansible Contributor Summit, we ran our usual post-event survey, which also asks more general questions about the state of the community.
> 
> I've now closed the forms and done the analysis, and you can find the results [here](https://connect.eng.ansible.com/content/9b71c2c7-6e08-4383-8c35-df149d4891ab). In general it's fairly consistent with previous surveys (which you can find [here](https://connect.eng.ansible.com/community_surveys/)).
> 
> Overall we're seeing more of the themes we've already discussed in the [community strategy](https://emeraldreverie.org/2023/02/24/ansible_state_2023/) so I hope the plans for the year ahead will positively impact that. Check it out, and let me know your thoughts!
> 
> ![](https://i.imgur.com/puIUHWs.png)

[cybette](https://matrix.to/#/@cybette:ansible.im) shared

> ### Website Working Group
> 
> We welcome you to review the new [Ansible Community website concept](https://hackmd.io/@ansible-community/new-website-concept) and give us some feedback! You can comment in the HackMD note, or drop by the [Website WG Matrix room](https://matrix.to/#/#website:ansible.com) and chat with us. Look forward to hearing from you!

## MAJOR NEW RELEASES 🏆️

### Ansible [↗](https://github.com/ansible-collections) 📦️

The `Ansible` package includes `ansible-core` and is a batteries-included package that provides a curated set of Ansible collections. See the [Ansible roadmaps](https://docs.ansible.com/ansible/devel/roadmap/ansible_roadmap_index.html) for future release plans.

[anwesha](https://matrix.to/#/@anwesha:ansible.im) contributed

> [Ansible 7.4.0](https://groups.google.com/g/ansible-announce/c/NuXPFzdT1i0) is out! ❤️
> 
> 💽You can install it by running the following command or download the release tarball directly from [pypi](https://pypi.python.org/packages/source/a/ansible/ansible-7.4.0.tar.gz):
> 
> ```
> pip install ansible==7.4.0 --user
> ```
> 
> ➡️ Check [Release Notes📦️🗒️](https://github.com/ansible-community/ansible-build-data/blob/main/7/CHANGELOG-v7.rst) and [Ansible 7 Porting Guide](https://docs.ansible.com/ansible/devel/porting_guides/porting_guide_7.html) for more details!

### DevTools [↗](https://github.com/ansible/ansible-navigator) ⛏️

Projects to make it easier to write and test Ansible Content. Includes [VScode extension](https://github.com/ansible/vscode-ansible), [language server](https://github.com/ansible/ansible-language-server), [ansible-lint](https://github.com/ansible-community/ansible-lint), [molecule](https://github.com/ansible-community/molecule), [ansible-navigator](https://github.com/ansible/ansible-navigator) and potentially other development goodies. To see what's planned, and how you can help checkout the [foundation-devtools project board](https://github.com/orgs/ansible/projects/86/views/4)

[Shatakshi](https://matrix.to/#/@shatakshiiii:matrix.org) contributed

> Ansible-Navigator version 3.0.0 is out! Dropping support for Python 3.8, couple of new features, and a long list of bug fixes.
> 
> Some of the notable changes are:
> 
> 1. Adding json output support for images and collections subcommand.
> 2. Adapting PEP 621 packaging.
> 3. Easier prompt support with a new CLI parameter `enable_prompts` for run subcommand.
> 4. Removing towncrier, related files and navigator's share directory.
> 5. Adapting latest creator-ee updates.
> 6. Adding more volume mount options.
> ... and much more :)
> 
> Please do check out the [release notes](https://github.com/ansible/ansible-navigator/releases/tag/v3.0.0) for all the updates.

### Antsibull [↗](https://github.com/ansible-community/antsibull) 🐂

Tooling for building the `Ansible` package and collection documentation.

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) said

> [antsibull-docs-parser 0.2.0](https://github.com/ansible-community/antsibull-docs-parser/blob/main/CHANGELOG.rst#v0-2-0) and [antsibull-docs-ts 0.2.0](https://github.com/ansible-community/antsibull-docs-ts/blob/main/CHANGELOG.rst#v0-2-0) are out. These are dependency-less Python respectively TypeScript libraries that allow to process Ansible markup, including the new semantic markup.

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) shared

> antsibull-changelog 0.20.0 ([changelog](https://github.com/ansible-community/antsibull-changelog/blob/0.20.0/CHANGELOG.rst#v0-20-0)) has been released. The main news is that we switched the build system from poetry-core to hatchling. This should not have any visible effect to users of antsibull-changelog.

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) contributed

> antsibull-docs 1.11.0 ([changelog](https://github.com/ansible-community/antsibull-docs/blob/main/CHANGELOG.rst#v1-11-0)) has been released. It contains two new important features, first semantic markup support for roles (which was missing so far), and second a markup validator which validates classic and semantic Ansible markup. 

### AWX Project [↗](https://github.com/ansible/awx)

AWX provides a web-based user interface, REST API, and task engine built on top of Ansible.

[john-westcott-iv](https://matrix.to/#/@john-westcott-iv:ansible.im) contributed

> We're happy to announce that the next release of AWX, version 21.14.0 is now available!
> Some notable features include:
> * Use ansible-runner change to get periodic keep-alive messages in K8S
> * Automatically build image for feature branch
> * Add scm_branch to inventory source and inventory update
> * [New Feature] Add Bulk add host and bulk job launch
> * Add instance groups roles
> * Adds support for a pseudolocalization and lang query params
> * Turn off auto completion on the login form
> * Don't use githubusercontent for containers.conf and podman-contianers.conf
> * [New Feature] Introducing tech preview of the new AWX UI
> * Expose execution node var for playbook
> * Expose SOCIAL_AUTH_USERNAME_IS_FULL_EMAIL
> 
> In addition AWX Operator version 1.4.0 has also been released!
> Some notable features include:
> * Use sha1 instead of md5 to make the installer work in FIPS
> * Add loadbalancerip to spec file
> * Revert to using k8s_cp module to read backup files
> 
> Please see the releases pages for more details: [AWX](https://github.com/ansible/awx/releases/tag/21.14.0), [Operator](https://github.com/ansible/awx-operator/releases/tag/1.4.0).

[TheRealHaoLiu](https://matrix.to/#/@therealhaoliu:matrix.org) said

> We're happy to announce that the next release of AWX, version 22.0.0 is now available!
> Some notable features include:
> * Allow soft deletion of HostMetrics and add usage collection utility
> * Allow TLS 1.2 for Receptor connections
> * Allow for using Ansible's `constructed` inventory plugin to dynamically group hosts from AWX inventories
> * Allow web and task container to be deployed in separate deployment on Kubernetes
> 
> In addition AWX Operator version 2.0.0 has also been released!
> Some notable features include:
> * Allow TLS 1.2 for Receptor connections
> * Deploy web and task component in independent deployment
> 
> Please see the releases pages for more details: [AWX](https://github.com/ansible/awx/releases/tag/22.0.0), [Operator](https://github.com/ansible/awx-operator/releases/tag/2.0.0).

## PROJECT UPDATES 🛠️

### AWX Project [↗](https://github.com/ansible/awx)

AWX provides a web-based user interface, REST API, and task engine built on top of Ansible.

[Lila Yasin](https://matrix.to/#/@lyasin:matrix.org) said

> Announcing AWX Web/Task Split Deployments for Kubernetes:
> * In the v22 release of AWX, the web/API backend and the task backend now live in separate Kubernetes deployments.
> * With the split deployments, we can now scale replicas separately or together.
> * To utilize this feature, you can edit your awx-operator spec to indicate the number of replicas you would like. 
> * You can scale replicas up or down for each deployment by using the `web_replicas` or `task_replicas` respectively. You can scale all pods across both deployments by using `replicas` as well. 
>   - If you specify the `replicas` field, the key passed will scale both the `web` and `task` replicas to the same number. 
>   - If `web_replicas` or `task_replicas` is ever passed, it will override the existing `replicas` field on the specific deployment with the new key value.
> * This enhancement not only allows for independent web and task scaling and replicas, it also paves the way for automatic scaling down the line.
> * We want your feedback! Do you find this feature helpful? Let us know [on Matrix](https://red.ht/join-ansible)!
> * Find an issue?  Please report those [on GitHub](https://github.com/ansible/awx/blob/devel/ISSUES.md).

[alancoding](https://matrix.to/#/@alancoding:matrix.org) said

> We have merged the [constructed inventory feature](https://github.com/ansible/awx/pull/13448) into AWX and it will go out in the next release. This is an alternative to smart inventory and addresses the key pain points like lack of groups, filtering on hostvars, and using general Ansible jinja2 templates for the user criteria.

### DevTools [↗](https://github.com/ansible/vscode-ansible) ⛏️

Projects to make it easier to write and test Ansible Content. Includes [VScode extension](https://github.com/ansible/vscode-ansible), [language server](https://github.com/ansible/ansible-language-server), [ansible-lint](https://github.com/ansible-community/ansible-lint), [molecule](https://github.com/ansible-community/molecule), [ansible-navigator](https://github.com/ansible/ansible-navigator) and potentially other development goodies. To see what's planned, and how you can help checkout the [foundation-devtools project board](https://github.com/orgs/ansible/projects/86/views/4)

[cidrblock](https://matrix.to/#/@cidrblock:matrix.org) said

> On behalf of the ansible devtools team: ansible-navigator verion v3.0.0 was just released. Included are a long list of bug fixes and the removal of python3.8 support. Have a look [here](https://pypi.org/project/ansible-navigator/).
> 
> Thank you to all the devtools project contributors, including a first time contributor @eamigo.

## COLLECTION UPDATES 🪄

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) shared

> community.general 6.5.0 ([changelog](https://github.com/ansible-collections/community.general/blob/stable-6/CHANGELOG.rst)) has been released with new features, bugfixes, and new plugins. Note that the next minor 6.x.y release will be 6.6.0 on April 24th, and after that the next minor/major release will be 7.0.0 on May 8th. That is one week before May 15th, the feature freeze date for [Ansible 8](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_8.html#release-schedule).

[briantist](https://matrix.to/#/@briantist:libera.chat) contributed

> `community.hashi_vault` [version `4.2.0`](https://github.com/ansible-collections/community.hashi_vault/releases/tag/4.2.0) [[changelog](https://ansible-collections.github.io/community.hashi_vault/tag/4.2.0/collections/community/hashi_vault/docsite/CHANGELOG.html#v4-2-0)] has been released with a new KVv2 write module and a warning/deprecation for duplicated term string option use in the `hashi_vault` lookup.

[tremble](https://matrix.to/#/@mchappell:matrix.org) said

> [amazon.aws 5.4.0](https://github.com/ansible-collections/amazon.aws/tree/5.4.0) has been released with bugfixes for the ec2_metadata_facts, ec2_vol, rds_instance and route53_info modules, as well as feature enhancements for the ec2_spot_instance and route53_health_check modules - [see changelog for details](https://github.com/ansible-collections/amazon.aws/blob/5.4.0/CHANGELOG.rst).
> 
> [community.aws 5.4.0](https://github.com/ansible-collections/community.aws/tree/5.4.0) has been released with feature enhancements for the ecs_service and sns modules - [see changelog for details](https://github.com/ansible-collections/community.aws/blob/5.4.0/CHANGELOG.rst).

## HELP WANTED 🙏

[andersson007_](https://matrix.to/#/@andersson007_:matrix.org) contributed

> The [new collection inclusion requests](https://github.com/ansible-collections/ansible-inclusion/discussions/categories/new-collection-reviews) are waiting for your [reviews](https://github.com/ansible-collections/ansible-inclusion#review-process). Please help the community extend the package!

## COMMUNITY EVENTS AND MEETUPS 📅

[anwesha](https://matrix.to/#/@anwesha:ansible.im) shared

> **Ansible Kolkata** Meetup group is rebooting its journey on **8th April 2023** at Indus Net Technologies, Kolkata, West Bengal. Learn about the Ansible Ecosystem and Automation with AWX from our Ansible Upstream. Book your slot now [here](https://www.meetup.com/ansible-kolkata/events/292239211/).

[cybette](https://matrix.to/#/@cybette:ansible.im) shared

> [**Ansible Dresden**](https://www.meetup.com/ansible-meetup-dresden/) meetup group is having a session on [Dynamic Inventories or How to handle AWS, Azure and more](https://www.meetup.com/ansible-meetup-dresden/events/291692249/), Thursday **April 13** at 5:30 PM CEST. Check out the meetup page for details and RSVP!

[cybette](https://matrix.to/#/@cybette:ansible.im) shared

> [**Ansible Atlanta**](https://www.meetup.com/ansible-atlanta/) meetup group is having a session on [Enterprise level Ansible Automation Overview](https://www.meetup.com/ansible-atlanta/events/292553848), Thursday **April 20** at 7:00 PM EDT. Check out the meetup page for details and RSVP!

[resmo](https://matrix.to/#/@resmo:libera.chat) contributed

> The 13th **Ansible Zürich** in person meetup is happening on **May 31 2023**, [details and RSVP](https://www.meetup.com/ansible-zurich/events/291951930/).

## THAT'S ALL FOR NOW!

Have any questions you’d like to ask, or issues you’d like to see covered? Please ask in [#social:ansible.com](https://matrix.to/#/#social:ansible.com)! See you next time!
