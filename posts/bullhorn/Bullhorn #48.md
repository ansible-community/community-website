---
title: "Bullhorn #48"
date: 2022-03-04 01:30 UTC
tags: news
category: bullhorn
type: text
---

![Ansible Bullhorn banner](/images/bullhorn-banner-mango.png)

*A Newsletter for the Ansible Developer Community*
*Issue #48, 2022-03-03 ([Past Issues](https://us19.campaign-archive.com/home/?u=56d874e027110e35dea0e03c1&id=d6635f5420))*

Welcome to [The Bullhorn](https://github.com/ansible/community/wiki/News#the-bullhorn), our newsletter for the Ansible developer community. If you have any questions or content you’d like to share, you're welcome to chat with us in the [Ansible Social room on Matrix](https://matrix.to/#/#social:ansible.com), and mention [`newsbot`](https://matrix.to/#/@newsbot:ansible.im) to have your news item tagged for review for the next weekly issue!

<!-- TEASER_END -->

## KEY DATES

[cybette](https://matrix.to/#/@cybette:ansible.im) shared

> * 2022-03-08: [DaWGs meeting](https://github.com/ansible/community/issues/643), 16:00 UTC
> * 2022-03-09: [Community WG meeting](https://github.com/ansible/community/issues/645), 18:00 UTC (propose topics [here](https://github.com/ansible-community/community-topics/issues))
> * 2022-03-10: [Bullhorn #49 content deadline](https://github.com/ansible/community/wiki/News#the-bullhorn), 18:00 UTC
> * 2022-03-15: [ETA for Ansible 5.5.0 release](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_5.html)
> * 2022-03-28: ETA for Ansible-Core 2.12.4 and Ansible-Core 2.11.10 releases (if those releases have updates)
> * 2022-04-12: [Contributor Summit 2022.04](https://hackmd.io/@ansible-community/contrib-summit-202204) 💾📅

## GENERAL NEWS UPDATES

[cybette](https://matrix.to/#/@cybette:ansible.im) shared

> The next Ansible Contributor Summit will be on April 12, 2022 (Tuesday). More details to follow, please bookmark the [HackMD note](https://hackmd.io/@ansible-community/contrib-summit-202204) and [save the date](https://raw.githubusercontent.com/ansible/community/main/meetings/ical/contribsummit202204.ics)! (Subscribe to the ical from URL instead of importing it so that any updates to the event will be reflected in your calendar.)

## MAJOR NEW RELEASES

### Ansible-Core [↗](https://github.com/ansible/ansible)

The `ansible-core` package contains the base engine and a small subset of modules and plugins. To see what's planned for the next release, look at the [`ansible-core` roadmaps](https://docs.ansible.com/ansible-core/devel/roadmap/ansible_core_roadmap_index.html).

[cybette](https://matrix.to/#/@cybette:ansible.im) contributed

> New releases: [ansible-core 2.12.3 and ansible-core 2.11.9](https://groups.google.com/g/ansible-devel/c/xhLaz9jZ6PQ)

## COLLECTION UPDATES

[hunleyd](https://matrix.to/#/@hunleyd:matrix.org) said

> `community.postgresql` [1.7.1](https://github.com/ansible-collections/community.postgresql/releases/tag/1.7.1) and [2.1.1](https://github.com/ansible-collections/community.postgresql/releases/tag/2.1.1) have been released. Many thanks to [Andersson007](https://github.com/Andersson007), [amossc](https://github.com/amossc), and [jtelcontar](https://github.com/jtelcontar)!

## HELP WANTED

[Rémi Rey](https://matrix.to/#/@rrey:matrix.org) contributed

> The [community.grafana](https://github.com/ansible-collections/community.grafana) collection is looking for help. There are major changes in Grafana 8 that requires adaptations in the modules. We are also looking for [good souls to join the maintainers](https://github.com/ansible-collections/community.grafana/issues/217) <3

## PROPOSALS - FEEDBACK APPRECIATED!

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) said

> We are looking for feedback on a new rule for collections included in Ansible on which files are allowed to be used by plugins, roles, and playbooks in this collection. If you maintain a collection that is included in Ansible, please look at [the corresponding community discussion topic](https://github.com/ansible-community/community-topics/issues/70) to see how this rule could look like and whether this is a problem for your collection. Thanks!

[mariolenz](https://matrix.to/#/@mariolenz:matrix.org) shared

> While most examples should go into the `EXAMPLES` block in the module documentation, some collections have an `examples/` directory for more complex ones showing how to combine several modules or roles to achieve something.
> 
> Discussion: [Should there be a standard place for examples?](https://github.com/ansible-community/community-topics/issues/73)

[Gwmngilfen](https://matrix.to/#/@gwmngilfen:ansible.im) said

> ### Chatrooms Feedback
> 
> It is coming up on 6 months since the vote to adopt Matrix alongside IRC. At that time, I said we should treat this as an ongoing process, and I meant it! I am preparing a blogpost covering the adoption so far, data to show, nice wins, pain points, and so on.
> 
> I would love to hear from the community about how the last few months have felt for you! Are you a long-term community member, or perhaps someone who just joined? Are the rooms discoverable enough? Are some things causing issues? Good, bad, or just interesting, I'd like to hear it. Note that nothing I hear will be made public without consent - but I hope I can publish some comments, and gain an idea of the sentiment.
> 
> If you are comfortable having a direct chat, then message me (`@gwmngilfen:ansible.im` or `gwmngilfen-work` on Libera), otherwise please feel free to leave anonymous comments [on this form](https://www.surveymonkey.co.uk/r/ZDYBFB5). The feedback window will be open for another 2 weeks, as I plan to write the blogpost in mid-March. Thanks!

## COMMUNITY UPDATES

### Maintainers [↗](https://github.com/ansible-community)

Maintainers help to run the community!

[steampunks](https://matrix.to/#/@xlab_steampunk:matrix.org) shared

> [ansible-doc-extractor](https://github.com/xlab-steampunk/ansible-doc-extractor/commit/4b0c3f68e6ddc509f8eb121ea9f4241951cce2bc), a tool that enables maintainers to extract documentation from Ansible Collections, in addition to .rst format now also supports markdown format.

## COMMUNITY EVENTS AND MEETUPS

[cybette](https://matrix.to/#/@cybette:ansible.im) contributed

> Join [Ansible NOVA](https://www.meetup.com/Ansible-NOVA/) group in “Ansible NOVA March Spring Soiree!” on Thursday, March 24 at 16:30 EDT / 20:30 UTC. It'll be a virtual meetup and they are looking for speakers/content. Check the details and RSVP [here](https://www.meetup.com/Ansible-NOVA/events/284181915/).

## THAT'S ALL FOR NOW!

Have any questions you’d like to ask, or issues you’d like to see covered? Please ask in [#social:ansible.com](https://matrix.to/#/#social:ansible.com)! See you next time!
