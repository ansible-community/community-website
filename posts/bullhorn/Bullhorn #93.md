---
title: "Bullhorn #93"
date: 2023-03-03 17:30 UTC
tags: news
category: bullhorn
type: text
---

![Ansible Bullhorn banner](/images/bullhorn-banner-mango.png)

*A Newsletter for the Ansible Developer Community*
*Issue #93, 2023-03-03 ([Past Issues](https://us19.campaign-archive.com/home/?u=56d874e027110e35dea0e03c1&id=d6635f5420))*

Welcome to [The Bullhorn](https://github.com/ansible/community/wiki/News#the-bullhorn), our newsletter for the Ansible developer community. If you have any questions or content you’d like to share, you're welcome to chat with us in the [Ansible Social room on Matrix](https://matrix.to/#/#social:ansible.com), and mention [`newsbot`](https://matrix.to/#/@newsbot:ansible.im) to have your news item tagged for review for the next weekly issue!

<!-- TEASER_END -->

## KEY DATES ⏱️

[cybette](https://matrix.to/#/@cybette:ansible.im) contributed

> * 2023-03-07: [DaWGs meeting](https://github.com/ansible/community/issues/678), 16:00 UTC
> * 2023-03-08: [Community WG meeting](https://github.com/ansible/community/issues/679), 19:00 UTC (propose topics [here](https://github.com/ansible-community/community-topics/issues))
> * 2023-03-09: [Bullhorn #94 content deadline](https://github.com/ansible/community/wiki/News#the-bullhorn), 18:00 UTC
> * 2023-03-27: ETA for Ansible-Core 2.14.4 and 2.13.9
> * 2023-03-28: [ETA for Ansible 7.4.0 release](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_7.html)

## GENERAL NEWS UPDATES 🔈️

[cybette](https://matrix.to/#/@cybette:ansible.im) shared

> ### Recordings from CfgMgmtCamp and Contributor Summit
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
> (And on the topic, if you didn't see last week's post about feedback on the Community Strategy for 2023, [check that out too](https://ansible.github.io/community/posts/state_of_the_community_2023.html)!)

[Ranabir Chakraborty](https://matrix.to/#/@ridetotheroots:matrix.org) said

> We are a new initiative called "[Ansible Middleware](https://github.com/ansible-middleware)", which utilizes the power of Ansible automation to orchestrate the installation, configuration, and management of Enterprise Middleware using several [collections](https://galaxy.ansible.com/middleware_automation). It provides you with several benefits such as a smoother release process, the same level of comfort as cloud infrastructure, making your application a first-class citizen of the Ansible ecosystem, and also making your middleware products easy to use and easy to automate. Currently, we have collections of [WildFly](https://galaxy.ansible.com/middleware_automation/wildfly), [Keycloak](https://galaxy.ansible.com/middleware_automation/keycloak), [Infinispan](https://galaxy.ansible.com/middleware_automation/infinispan), [JWS](https://galaxy.ansible.com/middleware_automation/jws), [Active MQ](https://github.com/ansible-middleware/amq), [Jcliff](https://galaxy.ansible.com/middleware_automation/jcliff) and we are rapidly growing.

## MAJOR NEW RELEASES 🏆️

### Ansible [↗](https://github.com/ansible-collections) 📦️

The `Ansible` package includes `ansible-core` and is a batteries-included package that provides a curated set of Ansible collections. See the [Ansible roadmaps](https://docs.ansible.com/ansible/devel/roadmap/ansible_roadmap_index.html) for future release plans.

[anwesha](https://matrix.to/#/@anwesha:ansible.im) contributed

> [Ansible 7.3.0 is out!](https://groups.google.com/g/ansible-devel/c/t9ohIIqRkLU) ❤️
> 
> 💽 You can install it by running the following command or download the release tarball directly from [pypi](https://pypi.python.org/packages/source/a/ansible/ansible-7.3.0.tar.gz):
> 
> ```
> python3 -m pip install ansible==7.3.0 --user
> ```
> 
> ➡️ Check [Release Notes📦️🗒️](https://github.com/ansible-community/ansible-build-data/blob/main/7/CHANGELOG-v7.rst) and [Ansible 7 Porting Guide](https://docs.ansible.com/ansible/devel/porting_guides/porting_guide_7.html) for more details!

### Antsibull [↗](https://github.com/ansible-community/antsibull) 🐂

Tooling for building the `Ansible` package and collection documentation.

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) shared

> antsibull 0.54.0 ([changelog](https://github.com/ansible-community/antsibull/blob/main/CHANGELOG.rst#v0-54-0)) has been released. It drops support for Python 3.8, removes the deprecated antsibull-lint CLI tool, and fixes some bugs.

### DevTools [↗](https://github.com/ansible/vscode-ansible) ⛏️

Projects to make it easier to write and test Ansible Content. Includes [VScode extension](https://github.com/ansible/vscode-ansible), [language server](https://github.com/ansible/ansible-language-server), [ansible-lint](https://github.com/ansible-community/ansible-lint), [molecule](https://github.com/ansible-community/molecule), [ansible-navigator](https://github.com/ansible/ansible-navigator) and potentially other development goodies. To see what's planned, and how you can help checkout the [foundation-devtools project board](https://github.com/orgs/ansible/projects/86/views/4)

[ssbarnea](https://matrix.to/#/@ssbarnea:matrix.org) shared

> [ansible-lint 6.14](https://github.com/ansible/ansible-lint/releases/tag/v6.14.0) was released, dropping support for py38 and including over 25 changes and bugfixes.

## PROJECT UPDATES 🛠️

[Priyam Sahoo](https://matrix.to/#/@priyams:matrix.org) contributed

> Devtools Update:
> 
> * As the ansible-lint project continues to gain momentum, with this growth comes an influx of new issues, both big and small. The devtools team has curated a list of `good first issues`, which can be found [here](https://github.com/ansible/ansible-lint/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+issue%22). These issues are an excellent opportunity for contributors to get involved and make a meaningful impact on the project's development. As you explore the issues in the repository, please take a moment to go through our [contribution guidelines](https://ansible-lint.readthedocs.io/contributing/).

[ruchip](https://matrix.to/#/@ruchip:ansible.im) contributed

> Devtools Update:
> 
> * We are planning to combine several pytest plugins like pytest-ansible, pytest-molecule & pytest-ansible-units into one, the idea is to pick the necessary features we need from each plugin, add the features which are missing/the ones we need and make the pytest-ansible plugin a common package for all the unit-testing work.
> 
> * We have opened a discussion for the same, you can follow it [here](https://github.com/ansible-community/community-topics/issues/203) and we look forward to any suggestions, feedback related to it. 😄

## COLLECTION UPDATES 🪄

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) shared

> community.general 6.4.0 ([changelog](https://github.com/ansible-collections/community.general/blob/stable-6/CHANGELOG.rst#v6-4-0)) has been released with new features and bugfixes.

[Sagar Paul](https://matrix.to/#/@sagpaul:matrix.org) said

> The Ansible networking team released the following collections
> 
> * [cisco.ios 4.4.0](https://github.com/ansible-collections/cisco.ios)
> * [junipernetworks.junos 5.0.0](https://github.com/ansible-collections/junipernetworks.junos)
> * [ansible.netcommon 5.0.0](https://github.com/ansible-collections/ansible.netcommon)
> * [vyos.vyos 4.0.1](https://github.com/ansible-collections/vyos.vyos)

## HELP WANTED 🙏

[Don Naro](https://matrix.to/#/@orandon:ansible.im) said

> The community engineering team has put together a first set of user journeys for Ansible docsite personas and would like your feedback. You can find the user journeys [in GitHub](https://github.com/ansible/docsite/blob/personas/user-journeys/ansible-user-journey-maps.md ).
> 
> The next step is to apply these journeys to an updated layout and navigation for `docs.ansible.com`. We're working to improve navigation and user experience for Ansible community documentation. Come [join us and help build a new docsite](https://github.com/ansible/jinja-docsite)!

[andersson007_](https://matrix.to/#/@andersson007_:matrix.org) shared

> The [new collection inclusion requests](https://github.com/ansible-collections/ansible-inclusion/discussions/categories/second-review-needed) are waiting for your [reviews](https://github.com/ansible-collections/ansible-inclusion#review-process). Please help the community extend the package!

[samccann](https://matrix.to/#/@samccann:ansible.im) said

> Looking to help out in Ansible but not sure where to start? Take a look at some easyfix or good first issues:
> * across multiple [collections](https://github.com/search?q=user%3Aansible-collections+label%3Aeasyfix%2C%22good+first+issue%22+state%3Aopen&type=Issues )
> * for all [other](https://github.com/search?q=user%3Aansible+user%3Aansible-community+label%3Aeasyfix%2C%22good+first+issue%22+state%3Aopen&type=Issues) Ansible projects

## PROPOSALS - DISCUSS AND VOTE! 🗳️

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) shared

> There is a community vote on whether to try to get semantic markup into ansible-core 2.15, or at least into antsibull-docs. Please look at [the discussion (in particular at the bottom)](https://github.com/ansible-community/community-topics/issues/53) and/or [participate in the vote](https://github.com/ansible-community/community-topics/discussions/205)!

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) shared

> There is a community vote on how a concrete proposal for hiding private plugins/modules in collections could look like. Please look at [the discussion (in particular at the bottom)](https://github.com/ansible-community/community-topics/issues/154) and/or [participate in the vote](https://github.com/ansible-community/community-topics/discussions/204)!

## COMMUNITY UPDATES 👂️

[dmsimard](https://matrix.to/#/@dmsimard:matrix.org) shared

> In this new blog post, we run benchmarks to find out the difference between running ansible-core 2.11 and 2.14 with python 3.9 and 3.11. Then, using the same methodology, we benchmark ara's different database backends. [Check it out.](https://ara.recordsansible.org/blog/2023/02/26/benchmarking-ara-with-different-databases-and-python3.11-for-fun-and-science/)
> 
> TL;DR:
> * ansible-core 2.14 is faster than 2.11
> * python 3.11 is faster than 3.9
> * django's mysql and postgresql performance is similar
> * sqlite is slower but mostly attributable to lack of multi-threading

[cybette](https://matrix.to/#/@cybette:ansible.im) shared

> Earlier this week there were 2 Ansible community meetups on the same day, one in Münich and the other in Zürich. If you were unable to attend one (because you were at the other one? :)) or both, their recorded streams are available - [Zürich](https://www.youtube.com/watch?v=A7-naalGSeU), [München](https://www.youtube.com/watch?v=NhjDiDdkhQI).

[Priyam Sahoo](https://matrix.to/#/@priyams:matrix.org) contributed

> Ansible Community Day India which happened in Pune (Red Hat Pune office on Saturday 25th February) was a day-long community-focused event to talk about Ansible project, community and wider ecosystem. It was an effort where the Ansible community both upstream and downstream meet in person to discuss about ansible and related things and kick start our events for pan India. This gave the opportunity to revive the old connections and get to make new ones.

[Sagar Paul](https://matrix.to/#/@sagpaul:matrix.org) said

> We had an in-person Ansible community day event in Pune, India. We were joined by ~82 attendees from all over the county. We had 6 talks and 2 workshops. These talks touched on different aspects of Ansible, including ansible-navigator, AWX, Network automation, and Middleware products automation. Overall, it was a great event full of productive discussion and enthusiasm from all the attendees to join the Ansible community and contribute. 🎉

## COMMUNITY EVENTS AND MEETUPS 📅

[cybette](https://matrix.to/#/@cybette:ansible.im) contributed

> [Chemnitz Linux Days 2023](https://chemnitzer.linux-tage.de/2023/en/) will take place March 11-12 in Chemnitz, Germany. There will be an [Ansible booth organized by community member Daniel Schier](https://www.meetup.com/ansible-meetup-dresden/events/291248823/)! Meet with the Ansible community face-to-face at the booth, with demos, experienced users, development insights, stickers and much more.

[cybette](https://matrix.to/#/@cybette:ansible.im) shared

> There are several community meetups coming up! 
> 
> * [Ansible Aurangabad](https://www.meetup.com/ansible-aurangabad/events/291861534/) on March 11 @ 11:00 AM IST
> * [Ansible New Zealand](https://www.meetup.com/ansible-new-zealand/events/291902379/) on March 15 @ 12:00 PM NZDT
> * [Ansible Minneapolis](https://www.meetup.com/ansible-minneapolis/events/291857213/) on March 16 @ 6:30PM CDT
> 
> Check out the respective event pages for details and RSVP!

## THAT'S ALL FOR NOW!

Have any questions you’d like to ask, or issues you’d like to see covered? Please ask in [#social:ansible.com](https://matrix.to/#/#social:ansible.com)! See you next time!
