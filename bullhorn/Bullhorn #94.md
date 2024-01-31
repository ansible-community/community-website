---
title: "Bullhorn #94"
date: 2023-03-11 06:15 UTC
tags: news
category: bullhorn
type: text
---

![Ansible Bullhorn banner](/images/bullhorn-banner-mango.png)

*A Newsletter for the Ansible Developer Community*
*Issue #94, 2023-03-10 ([Past Issues](https://us19.campaign-archive.com/home/?u=56d874e027110e35dea0e03c1&id=d6635f5420))*

Welcome to [The Bullhorn](https://github.com/ansible/community/wiki/News#the-bullhorn), our newsletter for the Ansible developer community. If you have any questions or content you’d like to share, you're welcome to chat with us in the [Ansible Social room on Matrix](https://matrix.to/#/#social:ansible.com), and mention [`newsbot`](https://matrix.to/#/@newsbot:ansible.im) to have your news item tagged for review for the next weekly issue!

<!-- TEASER_END -->

## KEY DATES ⏱️

[cybette](https://matrix.to/#/@cybette:ansible.im) said

> * 2023-03-14: [DaWGs meeting](https://github.com/ansible/community/issues/678), 16:00 UTC
> * 2023-03-15: [Community WG meeting](https://github.com/ansible/community/issues/679), 19:00 UTC (propose topics [here](https://github.com/ansible-community/community-topics/issues))
> * 2023-03-16: [Bullhorn #95 content deadline](https://github.com/ansible/community/wiki/News#the-bullhorn), 18:00 UTC
> * 2023-03-27: ETA for Ansible-Core 2.14.4 and 2.13.9
> * 2023-03-28: [ETA for Ansible 7.4.0 release](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_7.html)

## GENERAL NEWS UPDATES 🔈️

[cybette](https://matrix.to/#/@cybette:ansible.im) contributed

> We have added a notice on [Ansible Galaxy](https://galaxy.ansible.com/) as follows:
> 
> "Red Hat is working on exciting new Ansible content development capabilities within the context of [Project Wisdom](https://www.redhat.com/en/engage/project-wisdom) to help other automators build Ansible content. Your roles and collections may be used as training data for a machine learning model that provides Ansible automation content recommendations. If you have concerns, please contact the Ansible team at ansible-content-ai@redhat.com."

[cybette](https://matrix.to/#/@cybette:ansible.im) shared

> ### CfgMgmtCamp & Contributor Summit recordings
> 
> For those who missed the events, or if you were there but missed some of the talks, or if you want to rewatch some of them (because they're great!) - here are the playlists:
> * [Ansible Contributor Summit 2023.02 (Feb 8, 2023)](https://www.youtube.com/playlist?list=PL0FmYCf7ocrY-uMXYlnbCI2jZz8rDM8zP)
> * [Ansible track @ Cfgmgmtcamp 2023](https://www.youtube.com/playlist?list=PL0FmYCf7ocrZkU2-l-dxveX9woxZUe1ic)
> 
> Thanks to [Mark](https://matrix.to/#/@sig-io:matrix.org) for recording the talks!

[Gwmngilfen](https://matrix.to/#/@gwmngilfen:ansible.im) said

> ### Contributor Summit & Community Survey
> 
> As usual after a Contributor Summit event, I've put together a survey to help us learn for next time. It also covers more general questions about how the community feels to you at the moment, so even if you couldn't make it to the Contributor event, or CfgMgmtCamp, it's still worth a look. [It should take just a few minutes](https://www.surveymonkey.co.uk/r/W9SWQ9Q)!
> 
> (And on the topic, if you didn't see the post about feedback on the Community Strategy for 2023, [check that out too](https://ansible.github.io/community/posts/state_of_the_community_2023.html)!)

## MAJOR NEW RELEASES 🏆️

### AWX Project [↗](https://github.com/ansible/awx)

AWX provides a web-based user interface, REST API, and task engine built on top of Ansible.

[john-westcott-iv](https://matrix.to/#/@john-westcott-iv:ansible.im) contributed

> We're happy to announce that the next release of AWX, version 21.13.0 is now available!
> Some notable features include:
> * Make docker-compose command configurable in Makefile
> * Add `disable_instance` management command
> * Switch from head to tail in project update playbook when clearing project dir
> 
> In addition AWX Operator version 1.3.0 has also been released!
> Some notable features include:
> * AWX: Add `termination_grace_period_seconds`
> * Restore postgres database if external db
> * Add nodeport_port to instantiate playbook
> * Bump ansible operator SDK version to v1.26.0
> 
> Please see the releases pages for more details: [AWX](https://github.com/ansible/awx/releases/tag/21.13.0), [Operator](https://github.com/ansible/awx-operator/releases/tag/1.3.0).

### Antsibull [↗](https://github.com/ansible-community/antsibull) 🐂

Tooling for building the `Ansible` package and collection documentation.

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) shared

> antsibull-changelog 0.19.0 ([changelog](https://github.com/ansible-community/antsibull-changelog/blob/main/CHANGELOG.rst#v0-19-0)) has been released with new features. It can now extract the current version also from Python PEP 621 projects and JavaScript/TypeScript `package.json` based projects, and it uses the standard library tomllib on Python 3.11+ instead of needing toml or tomli to be available.

### Ansible-Core [↗](https://github.com/ansible/ansible) ⚡️

The `ansible-core` package contains the base engine and a small subset of modules and plugins. To see what's planned for the next release, look at the [`ansible-core` roadmaps](https://docs.ansible.com/ansible-core/devel/roadmap/ansible_core_roadmap_index.html).

[cybette](https://matrix.to/#/@cybette:ansible.im) said

> [ansible-core 2.14.3 and ansible-core 2.13.8](https://groups.google.com/g/ansible-devel/c/iF081u9jyws) were released last week. These are maintenance releases containing numerous bugfixes.

### DevTools [↗](https://github.com/ansible/vscode-ansible) ⛏️

Projects to make it easier to write and test Ansible Content. Includes [VScode extension](https://github.com/ansible/vscode-ansible), [language server](https://github.com/ansible/ansible-language-server), [ansible-lint](https://github.com/ansible-community/ansible-lint), [molecule](https://github.com/ansible-community/molecule), [ansible-navigator](https://github.com/ansible/ansible-navigator) and potentially other development goodies. To see what's planned, and how you can help checkout the [foundation-devtools project board](https://github.com/orgs/ansible/projects/86/views/4)

[Priyam Sahoo](https://matrix.to/#/@priyams:matrix.org) contributed

> The Devtools team has released `ansible-lint version 6.14.0`, which includes 23 bugfixes and 3 minor changes. Please refer to the changelog [here](https://github.com/ansible/ansible-lint/releases/tag/v6.14.0) for more information.

## HELP WANTED 🙏

[andersson007_](https://matrix.to/#/@andersson007_:matrix.org) contributed

> The [new collection inclusion requests](https://github.com/ansible-collections/ansible-inclusion/discussions/categories/new-collection-reviews) are waiting for your [reviews](https://github.com/ansible-collections/ansible-inclusion#review-process). Please help the community extend the package!

[Don Naro](https://matrix.to/#/@orandon:ansible.im) shared

> Come join us and help build a new docsite! The community team has been working to update the Ansible documentation landing page based on a set of [user journeys](https://github.com/ansible/docsite/blob/personas/user-journeys/ansible-user-journey-maps.md ). Right now we're working on a [prototype docsite ](https://github.com/ansible/jinja-docsite) to improve the navigation and user experience.

[samccann](https://matrix.to/#/@samccann:ansible.im) said

> Looking to help out in Ansible but not sure where to start? Take a look at some easyfix or good first issues:
> * across multiple [collections](https://github.com/search?q=user%3Aansible-collections+label%3Aeasyfix%2C%22good+first+issue%22+state%3Aopen&type=Issues )
> * for all [other](https://github.com/search?q=user%3Aansible+user%3Aansible-community+label%3Aeasyfix%2C%22good+first+issue%22+state%3Aopen&type=Issues) Ansible projects

## PROPOSALS - DISCUSS AND VOTE! 🗳️

[Don Naro](https://matrix.to/#/@orandon:ansible.im) contributed

> We want to hear from you! The Ansible community team is gathering feedback on a static site generator to build a new documentation landing page and community site, should the community be in favour of those efforts.
> 
> So, if you have opinions or insights on which static site generator we should use, please let us know. Visit our [static site generator community topic](https://github.com/ansible-community/community-topics/issues/210) and let us know what you think.

## COMMUNITY EVENTS AND MEETUPS 📅

[Ashutosh Bhakare](https://matrix.to/#/@ashutoshbhakare:matrix.org) said

> We are glad to announce our upcoming hands-on Workshop on Ansible 101. This workshop will provide good entry-level knowledge about Ansible.
> 
> Hurry up and register using [this link](https://www.meetup.com/ansible-aurangabad/events/291861534/).
> 
> Date: Saturday, March 11 2023 AT 11 AM
> Location: Unnati Development and Training Centre, 2ND FLOOR. N-7. CIDCO. OPP. BALIRAM PATIL HIGH SCHOOL, Ch. Sambhaji Nagar.

[cybette](https://matrix.to/#/@cybette:ansible.im) contributed

> There are several community meetups coming up! 
> 
> * [Ansible New Zealand](https://www.meetup.com/ansible-new-zealand/events/291902379/) on March 15 @ 12:00 PM NZDT
> * [Ansible Minneapolis](https://www.meetup.com/ansible-minneapolis/events/291857213/) on March 16 @ 6:30PM CDT
> * [Ansible Atlanta](https://www.meetup.com/ansible-atlanta/events/291919836/) on March 23 @ 7:00 PM EDT
> 
> Check out the respective event pages for details and RSVP!

## THAT'S ALL FOR NOW!

Have any questions you’d like to ask, or issues you’d like to see covered? Please ask in [#social:ansible.com](https://matrix.to/#/#social:ansible.com)! See you next time!
