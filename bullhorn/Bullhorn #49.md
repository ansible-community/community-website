---
title: "Bullhorn #49"
date: 2022-03-10 22:00 UTC
tags: news
category: bullhorn
type: text
---

![Ansible Bullhorn banner](/images/bullhorn-banner-mango.png)

*A Newsletter for the Ansible Developer Community*
*Issue #49, 2022-03-10 ([Past Issues](https://us19.campaign-archive.com/home/?u=56d874e027110e35dea0e03c1&id=d6635f5420))*

Welcome to [The Bullhorn](https://github.com/ansible/community/wiki/News#the-bullhorn), our newsletter for the Ansible developer community. If you have any questions or content you’d like to share, you're welcome to chat with us in the [Ansible Social room on Matrix](https://matrix.to/#/#social:ansible.com), and mention [`newsbot`](https://matrix.to/#/@newsbot:ansible.im) to have your news item tagged for review for the next weekly issue!

<!-- TEASER_END -->

## KEY DATES

[cybette](https://matrix.to/#/@cybette:ansible.im) said

> * 2022-03-15: [ETA for Ansible 5.5.0 release](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_5.html)
> * 2022-03-15: [DaWGs meeting](https://github.com/ansible/community/issues/643), 16:00 UTC
> * 2022-03-16: [Community WG meeting](https://github.com/ansible/community/issues/645), 18:00 UTC (propose topics [here](https://github.com/ansible-community/community-topics/issues))
> * 2022-03-17: [Bullhorn #50 content deadline](https://github.com/ansible/community/wiki/News#the-bullhorn), 18:00 UTC
> * 2022-03-28: ETA for Ansible-Core 2.12.4 and Ansible-Core 2.11.10 releases (if those releases have updates)
> * 2022-04-12: [Contributor Summit 2022.04](https://hackmd.io/@ansible-community/contrib-summit-202204) 💾📅

## GENERAL NEWS UPDATES

[cybette](https://matrix.to/#/@cybette:ansible.im) contributed

> The next **Ansible Contributor Summit** will be on **April 12, 2022** (Tuesday). Please take a look at the [HackMD note](https://hackmd.io/@ansible-community/contrib-summit-202204) - add your names & propose topics - and [save the date](https://raw.githubusercontent.com/ansible/community/main/meetings/ical/contribsummit202204.ics)! (Subscribe to the ical from URL instead of importing it so that any updates to the event will be reflected in your calendar.)

## NEW RELEASES

### DevTools [↗](https://github.com/ansible-community/ansible-lint)

Projects to make it easier to write and test Ansible Content. Includes [VScode extension](https://github.com/ansible/vscode-ansible), [language server](https://github.com/ansible/ansible-language-server), [ansible-lint](https://github.com/ansible-community/ansible-lint), [molecule](https://github.com/ansible-community/molecule), [ansible-navigator](https://github.com/ansible/ansible-navigator) and potentially other development goodies. To see what's planned, and how you can help checkout the [foundation-devtools project board](https://github.com/orgs/ansible/projects/86/views/4)

[ssbarnea](https://matrix.to/#/@ssbarnea:matrix.org) shared

> First pre-release for ansible-lint v6 is out, now being able to reformat documents. More details at https://github.com/ansible-community/ansible-lint/discussions/1955

## COLLECTION UPDATES

[andersson007_](https://matrix.to/#/@andersson007_:matrix.org) shared

> [community.network](https://github.com/ansible-collections/community.network) collection versions [1.3.6](https://github.com/ansible-collections/community.network/blob/stable-1/CHANGELOG.rst), [2.2.1](https://github.com/ansible-collections/community.network/blob/stable-2/CHANGELOG.rst), and [3.1.0](https://github.com/ansible-collections/community.network/blob/stable-3/CHANGELOG.rst) have been released! Special thanks to [felixfontein](https://github.com/felixfontein)!

## HELP WANTED

[Markus @RealRockaut](https://matrix.to/#/@rockaut:matrix.org) contributed

> for [community.zabbix](https://github.com/ansible-collections/community.zabbix): With the release of Zabbix 6.0 LTS we would love to get some help on blocking issues like [with the integration of a new scripts module](https://github.com/ansible-collections/community.zabbix/issues/634). Thank you for your attention!

[samccann](https://matrix.to/#/@samccann:ansible.im) shared

> Looking for a way to contribute to Ansible? How about starting with one of these [easyfix issues](https://github.com/ansible/ansible/issues?q=is%3Aopen+is%3Aissue+label%3Aeasyfix)?

## PROPOSALS - FEEDBACK APPRECIATED!

[gundalow](https://matrix.to/#/@gundalow:ansible.im) shared

> ### Improving Ansible documentation by unversioning some guides
> 
> Today, we have multiple files that we only maintain in `/devel/`. Historically, we had problems keeping these files up to date in other branches (`latest` and older). The docs team chose to publish the following pages only to `devel` and put a stub page up in `latest` and earlier releases to point to `devel`:
> 
> * [Porting guides](https://docs.ansible.com/ansible/latest/porting_guides/porting_guides.html)
> * [Release and Maintenance](https://docs.ansible.com/ansible/latest/reference_appendices/release_and_maintenance.html)
> 
> While this has worked well to keep the relevant docs current, it can be a cause of confusion. One recent reader was confused that we were pointing them to a devel page which has the banner that says this is not a guaranteed stable branch.
> 
> We have another set of guides (the community and contributor guides) that are getting a significant overhaul in devel. These guides are not specific to any release (core or Ansible package), but because we publish only to versioned urls, we force these guides to be 'versioned'.
> 
> We'd really welcome feedback from users, contributors and folks that have helped with the documentation via [ansible-community/community-topics#68](https://github.com/ansible-community/community-topics/issues/68).

[gundalow](https://matrix.to/#/@gundalow:ansible.im) contributed

> ### Revamping the community and contributor documentation
> 
> We have docs in three places today for contributors:
> *  ansible/ansible in the [community folder](https://github.com/ansible/ansible/tree/devel/docs/docsite/rst/community)
> *  [ansible/community-docs](https://github.com/ansible/community-docs) - more collection focused
> *  [ansible-collections/overview](https://github.com/ansible-collections/overview) - has deeper collection contribution details
> 
> Since only the first one is published to docs.ansible.com, we need to find a way to publish the details from the other two repositories.
> 
> This is a complex issue, and will shape how we structure the wide range of Ansible Documentation in the future. We'd really like to get your thoughts, and to hear your ideas via [community-topics#60](https://github.com/ansible-community/community-topics/issues/60).

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) said

> We are looking for feedback on a new rule for collections included in Ansible on which files are allowed to be used by plugins, roles, and playbooks in this collection. If you maintain a collection that is included in Ansible, please look at [the corresponding community discussion topic](https://github.com/ansible-community/community-topics/issues/70) to see how this rule could look like and whether this is a problem for your collection. Thanks!

[mariolenz](https://matrix.to/#/@mariolenz:matrix.org) shared

> While most examples should go into the `EXAMPLES` block in the module documentation, some collections have an `examples/` directory for more complex ones showing how to combine several modules or roles to achieve something.
> 
> Discussion: [Should there be a standard place for examples?](https://github.com/ansible-community/community-topics/issues/73)

## COMMUNITY UPDATES

[JulianF](https://matrix.to/#/@julian:foad.me.uk) said

> ### Self-Host a Matrix Map Tile Server
> 
> Following Element's recent announcement of location sharing with support for self-hosted map tile server, I went ahead and set up one, and have written a [blog post](https://wrily.foad.me.uk/self-host-a-matrix-map-server) about it, explaining how to go a little further than the currently published guide, and with [Ansible scripts](https://lab.trax.im/matrix/map-tile-server-ansible) included.

## COMMUNITY EVENTS AND MEETUPS

[cybette](https://matrix.to/#/@cybette:ansible.im) said

> The Ansible Community will have a presence at [Chemnitz Linux Days 2022](https://chemnitzer.linux-tage.de/2022/en) this weekend (March 12-13), with some [talks](https://chemnitzer.linux-tage.de/2022/en/programm/vortraege) (in German) as well as a [virtual booth](https://chemnitzer.linux-tage.de/2022/en/programm/beitrag/155). Thanks to [Daniel Schier](https://twitter.com/dschier_wtd) for orchestrating the details!

[cybette](https://matrix.to/#/@cybette:ansible.im) contributed

> If you're in the Minneapolis area, join [Ansible Minneapolis](https://www.meetup.com/Ansible-Minneapolis/) on March 17 for [March Meetup at Utepils](https://www.meetup.com/Ansible-Minneapolis/events/284260692), grab a beverage and talk some Ansible.

## THAT'S ALL FOR NOW!

Have any questions you’d like to ask, or issues you’d like to see covered? Please ask in [#social:ansible.com](https://matrix.to/#/#social:ansible.com)! See you next time!
