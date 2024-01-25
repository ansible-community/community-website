---
title: "Bullhorn #95"
date: 2023-03-21 16:00 UTC
tags: news
category: bullhorn
type: text
---

![Ansible Bullhorn banner](/images/bullhorn-banner-mango.png)

*A Newsletter for the Ansible Developer Community*
*Issue #95, 2023-03-20 ([Past Issues](https://us19.campaign-archive.com/home/?u=56d874e027110e35dea0e03c1&id=d6635f5420))*

Welcome to [The Bullhorn](https://github.com/ansible/community/wiki/News#the-bullhorn), our newsletter for the Ansible developer community. If you have any questions or content you’d like to share, you're welcome to chat with us in the [Ansible Social room on Matrix](https://matrix.to/#/#social:ansible.com), and mention [`newsbot`](https://matrix.to/#/@newsbot:ansible.im) to have your news item tagged for review for the next weekly issue!

<!-- TEASER_END -->

## KEY DATES ⏱️

[cybette](https://matrix.to/#/@cybette:ansible.im) said

> * 2023-03-22: [Community WG meeting](https://github.com/ansible/community/issues/679), 19:00 UTC (propose topics [here](https://github.com/ansible-community/community-topics/issues))
> * 2023-03-24: [Bullhorn #96 content deadline](https://github.com/ansible/community/wiki/News#the-bullhorn), 18:00 UTC
> * 2023-03-27: ETA for Ansible-Core 2.14.4 and 2.13.9
> * 2023-03-28: [ETA for Ansible 7.4.0 release](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_7.html)
> * 2023-03-28: [DaWGs meeting](https://github.com/ansible/community/issues/678), 16:00 UTC

## GENERAL NEWS UPDATES 🔈️

[cybette](https://matrix.to/#/@cybette:ansible.im) said

> ### Ansible Community Day @ Red Hat Summit 2023
> 
> **Ansible Community Day** will be part of [Red Hat Summit](https://www.redhat.com/en/summit) in Boston this year! It will be held on Monday May 22, 2023. To attend, please select the “Ansible Community Day” add-on when you [register for Red Hat Summit](https://reg.experiences.redhat.com/flow/redhat/sum23/regGenAttendee/login).
> 
> We are looking for a few more talks for this day. If you have something interesting to share with the Ansible Community users and contributors, please propose your topics in this [hackmd note](https://hackmd.io/@ansible-community/ACD2023-Boston). Ping me on matrix/irc if you have questions or would like to discuss more. Look forward to hearing from you!

## MAJOR NEW RELEASES 🏆️

### Antsibull [↗](https://github.com/ansible-community/antsibull) 🐂

Tooling for building the `Ansible` package and collection documentation.

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) contributed

> antsibull-docs 1.10.0 ([changelog](https://github.com/ansible-community/antsibull-docs/blob/main/CHANGELOG.rst#v1-10-0)) has been released. The main new feature is support for semantic markup!

### DevTools [↗](https://github.com/ansible/vscode-ansible) ⛏️

Projects to make it easier to write and test Ansible Content. Includes [VScode extension](https://github.com/ansible/vscode-ansible), [language server](https://github.com/ansible/ansible-language-server), [ansible-lint](https://github.com/ansible-community/ansible-lint), [molecule](https://github.com/ansible-community/molecule), [ansible-navigator](https://github.com/ansible/ansible-navigator) and potentially other development goodies. To see what's planned, and how you can help checkout the [foundation-devtools project board](https://github.com/orgs/ansible/projects/86/views/4)

[shatakshiiii](https://matrix.to/#/@shatakshiiii:matrix.org) contributed

> Ansible-Devtools team made a new release of Ansible-Lint [version 6.14.2](https://github.com/ansible/ansible-lint/releases/tag/v6.14.2) with couple of exciting bugfixes.
> 
> * Key fixes include implementation of `galaxy[no-runtime]` that checks and validates meta/runtime.yml for collections. As Ansible now requires collections to have a meta/runtime.yml file, through this fix ansible-lint is validating that this file exists when it detects it is running in a collection.
> * Other bugfixes include, ignore `risky-shell-pipe` with pwsh, fixes in `jinja[invalid]` rule and more.

## PROJECT UPDATES 🛠️

[shatakshiiii](https://matrix.to/#/@shatakshiiii:matrix.org) shared

> Ansible-Devtools Updates:
> 
> The team is planning to drop support for **Python 3.8** in the next major release of _**Ansible-Navigator**_. [Let us know](https://matrix.to/#/#devtools:ansible.com) if you have any concerns or thoughts on that!
> 
> We have already dropped Python 3.8 support from other devtools projects like Ansible Lint and Molecule prior to this.

## COLLECTION UPDATES 🪄

[Simon Dodsley](https://matrix.to/#/@sdodsley:matrix.org) shared

> purestorage.fusion 1.4.0 ([changelog](https://github.com/Pure-Storage-Ansible/Fusion-Collection/releases/tag/1.4.0)) has been released with significant updates, bugfixes and changes.

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) contributed

> community.hrobot 1.8.0 ([changelog](https://github.com/ansible-collections/community.hrobot/blob/main/CHANGELOG.rst#v1-8-0)) has been released with updates for the firewall module. Hetzner updated their dedicated firewall API in a way that the module from previous versions will disallow any outgoing traffic by default. You need to use the version of the module from this version with an `output` rule to avoid that.

## HELP WANTED 🙏

[Don Naro](https://matrix.to/#/@orandon:ansible.im) shared

> Come join us and help build a new docsite! The community team has been working to update the Ansible documentation landing page based on a set of [user journeys](https://github.com/ansible/docsite/blob/personas/user-journeys/ansible-user-journey-maps.md ) with the goal of helping community users connect with relevant documentation more efficiently. To contribute, take the [prototype docsite](https://ansible.github.io/jinja-docsite/index.html) for a spin and open a [GitHub issue](https://github.com/ansible/jinja-docsite/issues) with your feedback. You can also [fork the repository](https://github.com/ansible/jinja-docsite/fork) and send us a PR with changes.

[samccann](https://matrix.to/#/@samccann:ansible.im) said

> Looking to help out in Ansible but not sure where to start? Take a look at some easyfix or good first issues:
> * across multiple [collections](https://github.com/search?q=user%3Aansible-collections+label%3Aeasyfix%2C%22good+first+issue%22+state%3Aopen&type=Issues )
> * for all [other](https://github.com/search?q=user%3Aansible+user%3Aansible-community+label%3Aeasyfix%2C%22good+first+issue%22+state%3Aopen&type=Issues) Ansible projects

## PROPOSALS - DISCUSS AND VOTE! 🗳️

[cybette](https://matrix.to/#/@cybette:ansible.im) shared

> To move forward with some of the proposals we've discussed in the [Ansible Community Strategy](https://ansible.github.io/community/posts/ansible_community_strategy_2023.html) over the past few weeks, please vote on ["Use a forum to build project-wide participation & discussion"](https://github.com/ansible-community/community-topics/discussions/211), voting ends 2023-03-27.

[Don Naro](https://matrix.to/#/@orandon:ansible.im) contributed

> We want to hear from you! The Ansible community team is gathering feedback on a static site generator to build a new documentation landing page and community site, should the community be in favour of those efforts. If you have opinions or insights on which static site generator we should use, please let us know in the [static site generator community topic](https://github.com/ansible-community/community-topics/issues/210).

## COMMUNITY EVENTS AND MEETUPS 📅

[cybette](https://matrix.to/#/@cybette:ansible.im) contributed

> [Ansible Atlanta](https://www.meetup.com/ansible-atlanta/) meetup group is having a session on [Getting Started With Ansible](https://www.meetup.com/ansible-atlanta/events/291919836/), Thursday March 23 at 7:00 PM EDT. Check out the meetup page for details and RSVP!

[cybette](https://matrix.to/#/@cybette:ansible.im) contributed

> [Ansible Minneapolis](https://www.meetup.com/ansible-minneapolis/) meetup group is having a session on [Ansible playbook development tools & workflow](https://www.meetup.com/ansible-minneapolis/events/291857213/), Thursday March 23 at 6:30 PM CDT. Check out the meetup page for details and RSVP!

[cybette](https://matrix.to/#/@cybette:ansible.im) said

> [Ansible Singapore](https://www.meetup.com/ansible-singapore/) meetup group is having a session on [Event-Driven Ansible](https://www.meetup.com/ansible-singapore/events/292279388/), Wednesday March 29 at 6:30 PM SST. Check out the meetup page for details and RSVP!

[anwesha](https://matrix.to/#/@anwesha:ansible.im) said

> It is time to meet for the April Ansible Stockholm meetup on 5th April, 2023 at 17:30 - 20:30 CEST. This time we will learn how to write Ansible Roles and then test them with Molecule. Join us, and let's learn it together.  Check out the [meetup page](https://www.meetup.com/ansible-stockholm/events/292379420/) for details and RSVP.

[anwesha](https://matrix.to/#/@anwesha:ansible.im) shared

> Ansible Kolkata meetup is rebooting its journey after a long pause on 8th April 2023, at 11:00 - 14:00 IST. Check out the [meetup page](https://www.meetup.com/ansible-kolkata/events/292239211/) for details and RSVP. We are having sessions on Introduction to the Ansible ecosystem, Running automation jobs in AWX, and  How to connect to the Ansible Community? Join us for the adventure.

[cybette](https://matrix.to/#/@cybette:ansible.im) shared

> [Ansible Dresden](https://www.meetup.com/ansible-meetup-dresden/) meetup group is having a session on [Dynamic Inventories or How to handle AWS, Azure and more](https://www.meetup.com/ansible-meetup-dresden/events/291692249/), Thursday April 13 at 5:30 PM CEST. Check out the meetup page for details and RSVP!

## THAT'S ALL FOR NOW!

Have any questions you’d like to ask, or issues you’d like to see covered? Please ask in [#social:ansible.com](https://matrix.to/#/#social:ansible.com)! See you next time!
