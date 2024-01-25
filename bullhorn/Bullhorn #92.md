---
title: "Bullhorn #92"
date: 2023-02-24 20:40 UTC
tags: news
category: bullhorn
type: text
---

![Ansible Bullhorn banner](/images/bullhorn-banner-mango.png)

*A Newsletter for the Ansible Developer Community*
*Issue #92, 2023-02-24 ([Past Issues](https://us19.campaign-archive.com/home/?u=56d874e027110e35dea0e03c1&id=d6635f5420))*

Welcome to [The Bullhorn](https://github.com/ansible/community/wiki/News#the-bullhorn), our newsletter for the Ansible developer community. If you have any questions or content you’d like to share, you're welcome to chat with us in the [Ansible Social room on Matrix](https://matrix.to/#/#social:ansible.com), and mention [`newsbot`](https://matrix.to/#/@newsbot:ansible.im) to have your news item tagged for review for the next weekly issue!

<!-- TEASER_END -->

## KEY DATES ⏱️

[cybette](https://matrix.to/#/@cybette:ansible.im) contributed

> * 2023-02-27: ETA for Ansible-Core 2.14.3 and 2.13.8
> * 2023-02-28: [ETA for Ansible 7.3.0 release](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_7.html)
> * 2023-02-28: [DaWGs meeting](https://github.com/ansible/community/issues/678), 16:00 UTC
> * 2023-03-01: [Community WG meeting](https://github.com/ansible/community/issues/679), 19:00 UTC (propose topics [here](https://github.com/ansible-community/community-topics/issues))
> * 2023-03-02: [Bullhorn #93 content deadline](https://github.com/ansible/community/wiki/News#the-bullhorn), 18:00 UTC

## GENERAL NEWS UPDATES 🔈️

[Gwmngilfen](https://matrix.to/#/@gwmngilfen:ansible.im) shared

> ### Community strategy 2023 - have your say!
> 
> In recent weeks, the Red Hat Ansible Community Team has been writing up the state of the community in 2023, the issues that we see, and what we think we should do about it. I'm happy to announce that this is now **live** for your comments, questions, and **votes**.
> 
> This takes the form of two blog posts:
> 
> * [State of the Community 2023](https://ansible.github.io/community/posts/state_of_the_community_2023.html) on where we are at
> * [Community Strategy 2023](https://ansible.github.io/community/posts/ansible_community_strategy_2023.html) on what we think we should do
> 
> I also presented this strategy at the Ansible Contributor Summit two weeks ago in Ghent, so if you'd like to see that, head over to [YouTube](https://www.youtube.com/watch?v=B-AODeqjvss) for the recording.
> 
> In short, we believe the time has come to have a community DNS zone separate to ansible.com, and also to have a project-wide discussion space in the form of a Discourse forum. Crucially though, we don't get to call all the shots - so if you have opinions, or just want to give it a thumbs-up, you can head to the GitHub discussions [part 1](https://github.com/ansible-community/community-topics/issues/201) & [part 2](https://github.com/ansible-community/community-topics/issues/202).
> 
> See you in the discussion!

## MAJOR NEW RELEASES 🏆️

### DevTools [↗](https://github.com/ansible/vscode-ansible) ⛏️

Projects to make it easier to write and test Ansible Content. Includes [VScode extension](https://github.com/ansible/vscode-ansible), [language server](https://github.com/ansible/ansible-language-server), [ansible-lint](https://github.com/ansible-community/ansible-lint), [molecule](https://github.com/ansible-community/molecule), [ansible-navigator](https://github.com/ansible/ansible-navigator) and potentially other development goodies. To see what's planned, and how you can help checkout the [foundation-devtools project board](https://github.com/orgs/ansible/projects/86/views/4)

[Priyam Sahoo](https://matrix.to/#/@priyams:matrix.org) shared

> 1. [Ansible-lint 6.13](https://github.com/ansible/ansible-lint/releases/tag/v6.13.0) introduces a new feature that allows users to utilize a `.ansible-lint-ignore` file. This file contains skip-rules that are loaded from the ignore file which is adjacent to the config file. Additionally, users can take advantage of the `--generate-ignore` argument to dump any current violations into an ignore file.
> 
> 2. The Devtools team has just released a stable update for vscode-ansible extension, [version 1.2.44](https://marketplace.visualstudio.com/items?itemName=redhat.ansible), packed with important bugfixes and 2 exciting features:
>    * First addition is the information regarding a newer version ansible-lint availabilty in the status-bar itself. This ensures that users always have access to the most up-to-date tools and can stay ahead of the curve.
>    * Secondly, the update includes a feature that enables Red Hat telemetry gathering. This feature allows users to contribute to the ongoing development of the extension, ensuring that the tool remains cutting-edge and effective.

[ssbarnea](https://matrix.to/#/@ssbarnea:matrix.org) said

> DevTools team made a [pre-release of ansible-lint 6.14](https://github.com/ansible/ansible-lint/releases/tag/v6.14.0a0) which drops support for python 3.8 and includes 7 important bugfixes.

## PROJECT UPDATES 🛠️

[Sagar Paul](https://matrix.to/#/@sagpaul:matrix.org) said

> A few updates on what the Networking team is working on:
> * we are developing some content related to [interfaces and ospf](https://github.com/redhat-cop/network.ospf/pull/1)
> * we are working on extending the capabilities of nxos_bgp_global to [support the creation of neighbour templates](https://github.com/ansible-collections/cisco.nxos/issues/606); earlier we could use the module to just apply one that is already created
> * we are planning to release a [filter plugin (ace_popper)](https://github.com/ansible-collections/cisco.ios/pull/745) which acts on a set of acls facts gathered from a network appliance, and removes ace entries on the basis of some matching criteria

## COLLECTION UPDATES 🪄

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) shared

> community.crypto 2.11.0 ([changelog](https://github.com/ansible-collections/community.crypto/blob/main/CHANGELOG.rst#v2-11-0)) has been released with a new feature and some bugfixes.

[adhawkins](https://matrix.to/#/@adhawkins:libera.chat) contributed

> New version of the [adhawkins.borgbase collection](https://galaxy.ansible.com/adhawkins/borgbase) v1.0.2 includes some minor fixes regarding parameter types to borgbase_repo.

## PROPOSALS - DISCUSS AND VOTE! 🗳️

[andersson007_](https://matrix.to/#/@andersson007_:matrix.org) said

> As the concerns about the **future of the Ansible package** continue to show up, the [Community-approved collections instead of collection inclusion?](https://github.com/ansible-community/community-topics/issues/198) community topic has been created. Please share your thoughts!

[Felix Fontein](https://matrix.to/#/@felixfontein:matrix.org) contributed

> Some time ago we started a [community discussion](https://github.com/ansible-community/community-topics/issues/154) on how to **mark plugins in a collection as private**. Since ansible-core rejected to implement support for this in the ansible-doc CLI tool, I'm proposing to still standardize this so we can at least implement it in the community tooling, in particular antsibull-docs and antsibull-changelog. Please see my [call to action for how to continue](https://github.com/ansible-community/community-topics/issues/154#issuecomment-1441951838) for details. If you are interested in this, please use the [discussion issue](https://github.com/ansible-community/community-topics/issues/154) to voice your opinions on this.

[dmsimard](https://matrix.to/#/@dmsimard:matrix.org) contributed

> Do you have experience with **Prometheus and Ansible**?
> 
> ARA Records Ansible playbooks and it has a bunch of information and metrics about tasks, hosts and results.
> 
> What should a prometheus exporter to get Ansible metrics out of ara look like?
> 
> What kind of queries or monitoring would you like to do?
> 
> Your help and feedback would be appreciated!
> 
> Reach out on [Mastodon](https://fosstodon.org/@ara/109894741827696144) or see [this issue](https://github.com/ansible-community/ara/issues/177) on GitHub.

[Felix Fontein](https://matrix.to/#/@felixfontein:matrix.org) said

> More than two years ago the Ansible Docs Working Group started discussing the use of **semantic markup for Ansible plugin/module documentation**. This resulted in a [specification](https://hackmd.io/VjN60QSoRSSeRfvGmOH1lQ) that has been implemented as proofs of concept both for [ansible-doc and the validate-modules sanity test](https://github.com/ansible/ansible/pull/74937), as well as for [antsibull-docs](https://github.com/ansible-community/antsibull-docs/pull/4). From the docs perspective this will improve plugin, module, and now also role documentation a lot, and in particular separate markup from content. (Right now you have to use `C(...)` and `I(...)` for values and option names, which stand for 'code-style' and 'italics'.)
> 
> Unfortunately this has been on hold for a long time since changes to documentation now require approval of various Ansible-related projects. Since it is still unclear when/if this will ever continue, I am [proposing](https://github.com/ansible-community/community-topics/issues/53#issuecomment-1441965593) to start implementing this on the community side, i.e. antsibull-docs, so community collections can try to start playing around with this, which will hopefully put some pressure on other projects to move the semantic markup proposal forward. Please use the [associated discussion issue](https://github.com/ansible-community/community-topics/issues/53) in community-topics to voice your opinions on this.

## HELP WANTED 🙏

[Don Naro](https://matrix.to/#/@orandon:ansible.im) shared

> Are you interested in helping improve the navigation and layout of "docs.ansible.com"? Do you think you can help connect users with information in the docs more efficiently? If so, the Ansible community team invites you to contribute to [this](https://github.com/ansible/jinja-docsite) repository. We plan to use this repository to overhaul the landing pages for Ansible community documentation and create a more intuitive and modern user experience. See you in the PR queue!

[samccann](https://matrix.to/#/@samccann:ansible.im) said

> Looking to help out in Ansible but not sure where to start? Take a look at some easyfix or good first issues:
> * across multiple [collections](https://github.com/search?q=user%3Aansible-collections+label%3Aeasyfix%2C%22good+first+issue%22+state%3Aopen&type=Issues )
> * for all [other](https://github.com/search?q=user%3Aansible+user%3Aansible-community+label%3Aeasyfix%2C%22good+first+issue%22+state%3Aopen&type=Issues) Ansible projects

## COMMUNITY UPDATES 👂️

[steampunks](https://matrix.to/#/@xlab_steampunk:matrix.org) shared

> [Steampunk Spotter and Ansible Lint](https://steampunk.si/blog/why-use-steampunk-spotter-when-we-have-ansible-lint/) - it’s not about how they differ, but how they complement each other. Using both tools is a winning combination and guarantees reliable automation you can trust.

## COMMUNITY EVENTS AND MEETUPS 📅

[anwesha](https://matrix.to/#/@anwesha:ansible.im) said

> We are having the first-ever **Ansible Community Day India** on **25th February 2023**, i.e. tomorrow. It is a whole-day in-person community event with talks, workshops, and BoF sessions. Learn about the Ansible project and community, and share the story of your Ansible journey with us. We are excited to welcome you all tomorrow. Also join us in the [Ansible Contributor Summit Matrix room](https://matrix.to/#/#summit:ansible.com) during the event to chat (we recommend the [Element Web](https://app.element.io/) for a Matrix client).
> 
> You can get to know more about the event at the [Meetup page](https://www.meetup.com/ansible-pune/events/290492160/). 

[cybette](https://matrix.to/#/@cybette:ansible.im) shared

> [Ansible München](https://www.meetup.com/ansible-munchen/) is having their [1st Ansible Meetup of the year](https://www.meetup.com/ansible-munchen/events/289768549/) on **Feb 28** @ 18:00 CET. There will be 2 talks: "On-Containerized Ansible" by Guillermo Gomez and "Build Sovereign Cloud with Ansible" by Danny Afahounko. RSVP and attend!

[cybette](https://matrix.to/#/@cybette:ansible.im) said

> [Ansible Zürich](https://www.meetup.com/ansible-zurich/) will also be having an event on **Feb 28** @ 17:00 CET, as their [12th Ansible Meetup](https://www.meetup.com/ansible-zurich/events/290204496/). They have planned 3 topics: "Ansible LFOps - What's new in v2.0", "Getting started with Ansible Navigator", and "Ansible Sewing Box". RSVP and attend!

[cmrussell99](https://matrix.to/#/@cmrussell99:matrix.org) contributed

> Join the next office hours call on **Event-Driven Ansible**!  We share tips and techniques and most importantly answer your questions as you try Event-Driven Ansible. Next call is on **March 2, 2023** at 11AM ET. Register [here](https://www.redhat.com/en/events/webinar/event-driven-ansible-office-hours-march).

## THAT'S ALL FOR NOW!

Have any questions you’d like to ask, or issues you’d like to see covered? Please ask in [#social:ansible.com](https://matrix.to/#/#social:ansible.com)! See you next time!
