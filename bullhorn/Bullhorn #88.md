---
title: "Bullhorn #88"
date: 2023-01-20 09:30 UTC
tags: news
category: bullhorn
type: text
---

![Ansible Bullhorn banner](/images/bullhorn-banner-mango.png)

*A Newsletter for the Ansible Developer Community*
*Issue #88, 2023-01-20 ([Past Issues](https://us19.campaign-archive.com/home/?u=56d874e027110e35dea0e03c1&id=d6635f5420))*

Welcome to [The Bullhorn](https://github.com/ansible/community/wiki/News#the-bullhorn), our newsletter for the Ansible developer community. If you have any questions or content you’d like to share, you're welcome to chat with us in the [Ansible Social room on Matrix](https://matrix.to/#/#social:ansible.com), and mention [`newsbot`](https://matrix.to/#/@newsbot:ansible.im) to have your news item tagged for review for the next weekly issue!

<!-- TEASER_END -->

## KEY DATES ⏱️

[cybette](https://matrix.to/#/@cybette:ansible.im) contributed

> * 2023-01-24: [DaWGs meeting](https://github.com/ansible/community/issues/678), 16:00 UTC
> * 2023-01-25: [Community WG meeting](https://github.com/ansible/community/issues/679), 19:00 UTC (propose topics [here](https://github.com/ansible-community/community-topics/issues))
> * 2023-01-26: [Bullhorn #89 content deadline](https://github.com/ansible/community/wiki/News#the-bullhorn), 18:00 UTC
> * 2023-01-30: [ETA for Ansible-Core 2.14.2 and 2.13.8 releases](https://groups.google.com/g/ansible-devel/c/IQ7VPnw9yS8)
> * 2023-01-31: [ETA for Ansible 7.2.0 release](https://groups.google.com/g/ansible-devel/c/htFjU7jZVYA)
> * 2023-02-08: [Ansible Contributor Summit 2023.02](https://hackmd.io/@ansible-community/cs202302-planning)

## GENERAL NEWS UPDATES 🔈️

[samccann](https://matrix.to/#/@samccann:ansible.im) said

> We will redirect Ansible 2.5 documentation requests to `/latest/` starting next week. If you use Ansible 2.5, please change your bookmarks to the archived location [here](https://docs.ansible.com/archive/ansible/2.5/).

[mariolenz](https://matrix.to/#/@mariolenz:matrix.org) contributed

> There are now some [scripts](https://github.com/ansible-community/community-topics/tree/main/scripts) that (we hope) can be helpful to generate the text for Bullhorn announcements, at least for some of our community processes.

## MAJOR NEW RELEASES 🏆️

### Antsibull [↗](https://github.com/ansible-community/antsibull) 🐂

Tooling for building the `Ansible` package and collection documentation.

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) contributed

> antsibull-docs 1.9.0 ([changelog](https://github.com/ansible-community/antsibull-docs/blob/1.9.0/CHANGELOG.rst#v1-9-0)) has been released. It improves the build script created by the `sphinx-init` subcommand (now uses the path of the script instead of something hardcoded), and shows the type of a callback plugin on its docsite page and adds indexes of callback plugins by type.

## COLLECTION UPDATES 🪄

[briantist](https://matrix.to/#/@briantist:libera.chat) contributed

> The `community.hashi_vault` collection has released [version `4.1.0`](https://github.com/ansible-collections/community.hashi_vault/releases/tag/4.1.0) with a new `vault_list` module and lookup from a new contributor! There are also some upcoming deprecation announcements for `hvac` and `ansible-core` support.

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) shared

> community.docker 3.4.0 ([changelog](https://github.com/ansible-collections/community.docker/blob/main/CHANGELOG.rst#v3-4-0)) has been released with several bugfixes and a new module `docker_container_copy_into`, which allows to copy files into a running or stopped container.

[resmo](https://matrix.to/#/@resmo:libera.chat) contributed

> vultr.cloud 1.6.0 ([changelog](https://github.com/vultr/ansible-collection-vultr/blob/v1.6.0/CHANGELOG.rst)) has been released and adds the use of IPv6 to the dynamic inventory and improves the documentation.

[mariolenz](https://matrix.to/#/@mariolenz:matrix.org) said

> The `community.fortios` collection [is considered unmaintained](https://github.com/ansible-community/community-topics/issues/162) and will be removed from Ansible 9 if no one starts maintaining it again before Ansible 9. See [the removal process for details on how this works](https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst#cancelling-removal-of-an-unmaintained-collection).
> 
> Please note that you can still manually install the collection with `ansible-galaxy collection install community.fortios` even when it has been removed from Ansible.

## HELP WANTED 🙏

[Don Naro](https://matrix.to/#/@orandon:ansible.im) shared

> Call for contributors! You might have noticed that a lot of the docs in the ecosystem have started applying the [Ansible Sphinx theme](https://pypi.org/project/sphinx-ansible-theme/) to documentation in recent weeks. [Ansible Sign](https://ansible.github.io/ansible-sign/) and [Ansible Builder](https://ansible-builder.readthedocs.io/en/latest/) are just two such projects that have recently adopted the theme. And, as more teams start using it for their docs, we're identifying maintaince and improvements to make the Ansible Sphinx theme even better. Fork the [sphinx-ansible-theme repository](https://github.com/ansible-community/sphinx_ansible_theme) and lend us your expertise!

## PROPOSALS - DISCUSS AND VOTE! 🗳️

[mariolenz](https://matrix.to/#/@mariolenz:matrix.org) contributed

> As mentioned in [The Bullhorn #83](https://mailchi.mp/redhat/the-bullhorn-83), we consider `community.google` an effectively unmaintained collection. Therefore, we've opened a community / steering committee [vote](https://github.com/ansible-community/community-topics/discussions/181) on removing it from the Ansible 9 community package.

[mariolenz](https://matrix.to/#/@mariolenz:matrix.org) contributed

> As mentioned in [The Bullhorn #84](https://mailchi.mp/redhat/the-bullhorn-84), we consider `community.skydive` an effectively unmaintained collection. Therefore, we've opened a community / steering committee [vote](https://github.com/ansible-community/community-topics/discussions/182) on removing it from the Ansible 9 community package.

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) contributed

> There is a new community vote on [cancelling the removal process of cyberark.pas from Ansible 9](https://github.com/ansible-community/community-topics/discussions/185), since the collection seems to be actively maintained again. See [the accompanying discussion issue](https://github.com/ansible-community/community-topics/issues/180) for details.

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) said

> There is a new community vote on [updating the Ansible PyPI description](https://github.com/ansible-community/community-topics/discussions/186) by merging [the proposal PR as-is](https://github.com/ansible-community/antsibull/pull/474). Further updates can be done in follow-up PRs if wanted and necessary.

[Don Naro](https://matrix.to/#/@orandon:ansible.im) contributed

> As a next step on the path to a new and improved Ansible docsite we want to hear from the community! We've narrowed down a set of key personas that we plan to use to create better entry points to Ansible documentation. The goal is to help community users find docs in a way that fully supports their automation journey. Please add your thoughts in this [community topic](https://github.com/ansible-community/community-topics/issues/175) or comment directly on the personas [here](https://hackmd.io/pZb5w5JFRQW3RJ73n23tlw).

## COMMUNITY UPDATES 👂️

[steampunks](https://matrix.to/#/@xlab_steampunk:matrix.org) shared

> We’ve prepared a [step by step guide](https://steampunk.si/blog/upgrading-your-ansible-playbooks-step-by-step-guide/) on how to upgrade your Ansible Playbook in minutes using Ansible Lint and Steampunk Spotter.

## COMMUNITY EVENTS AND MEETUPS 📅

[ompragash](https://matrix.to/#/@ompragash:ansible.im) shared

> 📣 We are excited to announce the upcoming **Ansible Community Day** in India!
> 
> Join us in-person for a day of presentations, workshops, and networking with other Ansible enthusiasts. Learn about the latest developments in Ansible and how it can help you automate your IT infrastructure. Don't miss out on this opportunity to connect with the Ansible community and take your skills to the next level.
> 
> Register now on [meetup.com](https://www.meetup.com/ansible-pune/events/290492160/). If you have an interesting Ansible use case or experience you would like to share, submit your talk proposal [here](https://forms.gle/DjTewB8GsgZdzJkc7).
> 
> 🗓 SAT, FEB 25, 2023, 9:30 AM IST
> 📍 Red Hat India Private Limited, Magarpatta Inner Circle · Pune, Maharashtra

[cybette](https://matrix.to/#/@cybette:ansible.im) said

> There are several community meetups coming up! Join [Ansible Singapore](https://www.meetup.com/ansible-singapore/events/290957740/) on Jan 31 @ 6:30 PM SST, [Ansible Zürich](https://www.meetup.com/ansible-zurich/events/290204496/) on Feb 28 @ 5:00 PM CET, or [Ansible München](https://www.meetup.com/ansible-munchen/events/289768549/) also on Feb 28 @ 6:00PM CET. Check out the respective event pages for details and RSVP!

## THE ANSIBLE TEAM IS HIRING 💰️

[samccann](https://matrix.to/#/@samccann:ansible.im) shared

> Ansible product documentation (AAP) have a few senior technical writing reqs open. See the following for details:
> * [Senior Technical Writer (US-MA-Westford)](https://us-redhat.icims.com/jobs/98391/senior-technical-writer/job?hub=7)
> * [Senior Technical Writer (US-NC-Raleigh)](https://us-redhat.icims.com/jobs/98388/senior-technical-writer/job?hub=7)
> * [Senior Technical Writer (IE-Remote)](https://us-redhat.icims.com/jobs/97562/senior-technical-writer---ansible-automation-platform/job?hub=7)

[samccann](https://matrix.to/#/@samccann:ansible.im) said

> Ansible product documentation (AAP) is looking for a senior content strategist!  See [Senior Content Strategist (US-Remote)](https://us-redhat.icims.com/jobs/98398/senior-content-strategist/job?hub=7) for details!

## THAT'S ALL FOR NOW!

Have any questions you’d like to ask, or issues you’d like to see covered? Please ask in [#social:ansible.com](https://matrix.to/#/#social:ansible.com)! See you next time!
