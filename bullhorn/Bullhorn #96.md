---
title: "Bullhorn #96"
date: 2023-03-26 08:00 UTC
tags: news
category: bullhorn
type: text
---

![Ansible Bullhorn banner](/images/bullhorn-banner-mango.png)

*A Newsletter for the Ansible Developer Community*
*Issue #96, 2023-03-26 ([Past Issues](https://us19.campaign-archive.com/home/?u=56d874e027110e35dea0e03c1&id=d6635f5420))*

Welcome to [The Bullhorn](https://github.com/ansible/community/wiki/News#the-bullhorn), our newsletter for the Ansible developer community. If you have any questions or content you’d like to share, you're welcome to chat with us in the [Ansible Social room on Matrix](https://matrix.to/#/#social:ansible.com), and mention [`newsbot`](https://matrix.to/#/@newsbot:ansible.im) to have your news item tagged for review for the next weekly issue!

<!-- TEASER_END -->

## KEY DATES ⏱️

[cybette](https://matrix.to/#/@cybette:ansible.im) said

> * 2023-03-27: ETA for Ansible-Core 2.14.4
> * 2023-03-28: [ETA for Ansible 7.4.0 release](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_7.html)
> * 2023-03-28: [DaWGs meeting](https://github.com/ansible/community/issues/678), 16:00 UTC
> * 2023-03-29: [Community WG meeting](https://github.com/ansible/community/issues/679), 18:00 UTC (note [time "change"](https://github.com/ansible/community/pull/691) due to summer time/daylight savings time)
> * 2023-03-30: [Bullhorn #97 content deadline](https://github.com/ansible/community/wiki/News#the-bullhorn), 18:00 UTC
> * 2023-03-31: [Deadline to propose topics for Ansible Community Day](https://hackmd.io/@ansible-community/ACD2023-Boston)

## GENERAL NEWS UPDATES 🔈️

[Gwmngilfen](https://matrix.to/#/@gwmngilfen:ansible.im) contributed

> ### Website Working Group room
> 
> In addition to what mariolenz [said](https://matrix.to/#/!pMZboYFCScZJfXmOtH:ansible.im/$ziYMQXhswhYVsqT88KJDSOW3Q73Rha58Q-KWs1PLwIU?via=ansible.com&via=libera.chat&via=matrix.org), the Website Working Group now has its room set up - if you'd like to join in please hop into [#website:ansible.com](https://matrix.to/#/#website:ansible.com) (IRC bridge is coming but there's an issue with new Libera bridges at the moment, stay tuned if you're an IRC user).
> Let us know what your contribution interest is, and we'll be happy to get you up to speed!

[cybette](https://matrix.to/#/@cybette:ansible.im) shared

> ### Ansible Community Day @ Red Hat Summit 2023
> 
> **Ansible Community Day** will be part of [Red Hat Summit](https://www.redhat.com/en/summit) in Boston this year! It will be held on Monday May 22, 2023. When you have [registered for Red Hat Summit](https://reg.experiences.redhat.com/flow/redhat/sum23/regGenAttendee/login), you can RSVP to attend by adding [Ansible Community Day](https://events.experiences.redhat.com/widget/redhat/sum23/SessionCatalog2023/session/1678832216982001yETF) in the session catalog to your schedule.
> 
> We are looking for a few more talks for this day. If you have something interesting to share with the Ansible Community users and contributors, please propose your topics by March 31 in this [hackmd note](https://hackmd.io/@ansible-community/ACD2023-Boston). Ping me on matrix/irc if you have questions or would like to discuss more. Look forward to hearing from you!

[Gwmngilfen](https://matrix.to/#/@gwmngilfen:ansible.im) contributed

> ### Webhooks for Ansible Matrix Rooms
> 
> This is (mostly) news for our various Working Groups! If you're involved in a Working Group and would like to receive notifications in your Matrix room, then rejoice! For we have added the [Hookshot](https://matrix-org.github.io/matrix-hookshot/latest/hookshot.html) bridge to our homeserver, which means we can now relay incoming payloads into a given room. It also supports RSS feeds should you want it.
> 
> If this sounds like it would be of interest to you, then please reach out to [me](https://matrix.to/#/@gwmngilfen:ansible.im) and I'll help you out.

## COLLECTION UPDATES 🪄

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) shared

> community.routeros 2.8.0 ([changelog](https://github.com/ansible-collections/community.routeros/blob/main/CHANGELOG.rst#v2-8-0)) has been released with new features and bugfixes.

[tima](https://matrix.to/#/@tappnel:matrix.org) shared

> We have released an [Ansible provider for Terraform](https://registry.terraform.io/providers/ansible/ansible/latest) that can run Ansible playbooks and roles on infrastructure provisioned by Terraform. Paired with the inventory plugin in [the Ansible cloud.terraform collection](https://galaxy.ansible.com/cloud/terraform), this provider delivers a more straightforward means of running ansible-playbook and includes integrated ansible-vault support. For more info, see [this blog post](https://www.ansible.com/blog/providing-terraform-with-that-ansible-magic) and [the project repo](https://github.com/ansible-collections/cloud.terraform).

## PROJECT UPDATES 🛠️

### AWX Project [↗](https://github.com/ansible/awx)

AWX provides a web-based user interface, REST API, and task engine built on top of Ansible.

[relrod](https://matrix.to/#/@relrod:matrix.org) contributed

> Have you tried to contribute to AWX before? Did you struggle to set up the development environment? We want to improve the developer and contributor experience for AWX and make it easier to participate. What pain-points have you experienced? Please join the discussion [here](https://github.com/ansible/awx/issues/13737).

## HELP WANTED 🙏

[andersson007_](https://matrix.to/#/@andersson007_:matrix.org) said

> The [new collection inclusion requests](https://github.com/ansible-collections/ansible-inclusion/discussions/categories/new-collection-reviews) are waiting for your [reviews](https://github.com/ansible-collections/ansible-inclusion#review-process). Please help the community extend the package!

[Don Naro](https://matrix.to/#/@orandon:ansible.im) said

> Come join us and help build a new docsite! The community team has been working to update the Ansible documentation landing page based on a set of [user journeys](https://github.com/ansible/docsite/blob/personas/user-journeys/ansible-user-journey-maps.md ) with the goal of helping community users connect with relevant documentation more efficiently. To contribute, take the [prototype docsite](https://ansible.github.io/jinja-docsite/index.html) for a spin and open a [GitHub issue](https://github.com/ansible/jinja-docsite/issues) with your feedback. You can also [fork the repository](https://github.com/ansible/jinja-docsite/fork) and send us a PR with changes.

[samccann](https://matrix.to/#/@samccann:ansible.im) shared

> Looking to help out in Ansible but not sure where to start? Take a look at some easyfix or good first issues:
> * across multiple [collections](https://github.com/search?q=user%3Aansible-collections+label%3Aeasyfix%2C%22good+first+issue%22+state%3Aopen&type=Issues )
> * for all [other](https://github.com/search?q=user%3Aansible+user%3Aansible-community+label%3Aeasyfix%2C%22good+first+issue%22+state%3Aopen&type=Issues) Ansible projects

## PROPOSALS - DISCUSS AND VOTE! 🗳️

[mariolenz](https://matrix.to/#/@mariolenz:matrix.org) contributed

> As announced by [Gwmngilfen](https://github.com/GregSutcliffe) in [The Bullhorn #92](https://mailchi.mp/redhat/the-bullhorn-92), we started some discussions on the `Community strategy 2023`. The first result is that the [vote](https://github.com/ansible-community/community-topics/discussions/208) to register a DNS zone `ansible.community` to use for all things relating to Ansible Community has been accepted.
> 
> We would love if you would give your opinion on [using a forum to build project-wide participation & discussion](https://github.com/ansible-community/community-topics/issues/202) and [vote](https://github.com/ansible-community/community-topics/discussions/211) on it.
> 
> Also, feel free to discuss [what static site generator we should use for the new Ansible community web presence](https://github.com/ansible-community/community-topics/issues/210)!

[Don Naro](https://matrix.to/#/@orandon:ansible.im) shared

> Voting is open for Nikola! The Ansible community team has been gathering feedback and doing some evaluation for static site generators that can help us create a new documentation landing page and community sites. We looked at some really great options and, after some careful considerations, decided that [Nikola](https://getnikola.com/) is likely the best SSG to help us get the initial iteration up and running. In community spirit we're putting it to a [vote where you can add your +1 / -1 for Nikola](https://github.com/ansible-community/community-topics/discussions/216).

## COMMUNITY UPDATES 👂️

[steampunks](https://matrix.to/#/@xlab_steampunk:matrix.org) contributed

> [Steampunk Spotter](https://steampunk.si/spotter/), an Ansible Playbook scanning tool, now supports Visual Studio Code integration, so you can use all its features directly in the code editor. You can install the extension from the [Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=xlab-steampunk.steampunk-spotter) or [Open VSX Registry](https://open-vsx.org/extension/xlab-steampunk/steampunk-spotter).

## COMMUNITY EVENTS AND MEETUPS 📅

[cybette](https://matrix.to/#/@cybette:ansible.im) said

> [**Ansible Singapore**](https://www.meetup.com/ansible-singapore/) meetup group is having a session on [Event-Driven Ansible](https://www.meetup.com/ansible-singapore/events/292279388/), Wednesday **March 29** at 6:30 PM SST. Check out the meetup page for details and RSVP!

[Leo](https://matrix.to/#/@leo:ansible.im) said

> The [**Ansible Buenos Aires** Meetup](https://www.meetup.com/ansible-buenos-aires/) is back for 2023! We will be meeting in person on the **30th of March** from 18.30 at the Red Hat Argentina offices in Ing. Butty 240, Floor 14. We will be meeting for the first time in a while, so we will do some community introductions and share how to became a contributor for the Ansible project. Join us for food and beers while we talk all things Ansible! Register [here](https://bit.ly/ansible-ba-meetup-2023).

[anwesha](https://matrix.to/#/@anwesha:ansible.im) said

> It is time to meet for the April **Ansible Stockholm** meetup on **5th April, 2023** at 17:30 - 20:30 CEST. This time we will learn how to write Ansible Roles and then test them with Molecule. Join us, and let's learn it together.  Check out the [meetup page](https://www.meetup.com/ansible-stockholm/events/292379420/) for details and RSVP.

[anwesha](https://matrix.to/#/@anwesha:ansible.im) shared

> **Ansible Kolkata** meetup is rebooting its journey after a long pause on **8th April 2023**, at 11:00 - 14:00 IST. Check out the [meetup page](https://www.meetup.com/ansible-kolkata/events/292239211/) for details and RSVP. We are having sessions on Introduction to the Ansible ecosystem, Running automation jobs in AWX, and  How to connect to the Ansible Community? Join us for the adventure.

[cybette](https://matrix.to/#/@cybette:ansible.im) shared

> [**Ansible Dresden**](https://www.meetup.com/ansible-meetup-dresden/) meetup group is having a session on [Dynamic Inventories or How to handle AWS, Azure and more](https://www.meetup.com/ansible-meetup-dresden/events/291692249/), Thursday **April 13** at 5:30 PM CEST. Check out the meetup page for details and RSVP!

[resmo](https://matrix.to/#/@resmo:libera.chat) contributed

> The 13th **Ansible Zürich** in person meetup is happening on **May 31 2023**, [details and RSVP](https://www.meetup.com/ansible-zurich/events/291951930/).

## THAT'S ALL FOR NOW!

Have any questions you’d like to ask, or issues you’d like to see covered? Please ask in [#social:ansible.com](https://matrix.to/#/#social:ansible.com)! See you next time!
