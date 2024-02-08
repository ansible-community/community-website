---
title: "Bullhorn #37"
date: 2021-11-06 06:30 UTC
tags: news
category: bullhorn
type: text
---

![Ansible Bullhorn banner](/images/bullhorn-banner-mango.png)

## The Bullhorn

*A Newsletter for the Ansible Developer Community*
*Issue #37, 2021-11-04 ([Past Issues](https://us19.campaign-archive.com/home/?u=56d874e027110e35dea0e03c1&id=d6635f5420))*

Welcome to the Bullhorn, our newsletter for the Ansible developer community. If you have any questions or content you’d like to share, please reach out to us at the-bullhorn@redhat.com, or comment on this [GitHub issue](https://github.com/ansible/community/issues/546). Take a look at the "Community Update" torwards the end of this edition for a new way of sharing news/content!

<!-- TEASER_END -->

### KEY DATES

* 2021-11-08: ETA for Ansible-Core 2.11.7 and Ansible-Base 2.10.16 releases
* 2021-11-08: [ETA for Ansible-Core 2.12.0 GA release](https://docs.ansible.com/ansible-core/devel/roadmap/ROADMAP_2_12.html)
* 2021-11-10: [community IRC meeting](https://github.com/ansible/community/issues/539), 18:00 UTC (propose topics [here](https://github.com/ansible-community/community-topics/issues))
* 2021-11-11: [D&I working group meeting](https://github.com/ansible/community/issues/577), 19:00 UTC
* 2021-11-16: [Bullhorn #38 content deadline](https://github.com/ansible/community/issues/546)
* 2021-11-17: [community IRC meeting](https://github.com/ansible/community/issues/539), 18:00 UTC (check possible new time [here](https://github.com/ansible-community/community-topics/issues/48))
* 2021-11-23: [ETA for Ansible 4.9.0 release](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_4.html)
* 2021-11-30: [ETA for Ansible 5.0.0 GA release](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_5.html)

## General News Updates

[dmsimard](https://matrix.to/#/@dmsimard:matrix.org) says

> Ansible 2.9 and ansible-base 2.10 EOL have been announced for May 23, 2022: https://groups.google.com/g/ansible-announce/c/kegIH5_okmg/

[gundalow](https://github.com/gundalow) reports

> **Python 2.6 support for modules**
> 
> We've just merged a guard preventing the use of Python 2.6 for executing modules into `ansible.module_utils.basic` for devel/2.13.
> 
> The `milestone` branch won't be advanced to include this until tentatively 2021 Dec 13.

## Major New Releases

### Ansible [↗](https://github.com/ansible-collections)

**Ansible** is the full-fat package containing Ansible Core & the Community Collections

[dmsimard](https://matrix.to/#/@dmsimard:matrix.org) says

> Ansible 4.8.0 has been released: https://groups.google.com/g/ansible-announce/c/at_Cjdu-gh4

[dmsimard](https://matrix.to/#/@dmsimard:matrix.org) reports

> Ansible 5.0.0a3 is available for testing: https://groups.google.com/g/ansible-devel/c/gm4oSevkabo

### DevTools [↗](https://github.com/ansible/vscode-ansible)

VScode extension, language server, linter, molecule, runner, navigator and potentially other development goodies

[ssbarnea](https://matrix.to/#/@ssbarnea:matrix.org) reports

> [vscode extension 0.6.1](https://marketplace.visualstudio.com/items?itemName=redhat.ansible) is out https://github.com/ansible/vscode-ansible/discussions/297 -- we will have weekly releases (when having something to release).

### Antsibull [↗](https://github.com/ansible-community/antsibull)

Tooling for building various things related to ansible

[felixfontein](https://github.com/felixfontein) says

> antsibull 0.39.0 has been released.

## Collection Updates

[briantist](https://github.com/briantist) reports

> [`community.hashi_vault` version `1.4.1` has been released with new content, bugfixes (including one for `aws_iam_login` auth), and a deprecation](https://github.com/ansible-collections/community.hashi_vault/releases/tag/1.4.1).

[Gwmngilfen (work)](https://matrix.to/#/@gwmngilfen:ansible.im) says

> community.routeros 2.0.0 released
> 
> A new major release with breaking changes in the behavior of community.routeros.command and community.routeros.api.
> 
> See [the release notes](https://github.com/ansible-collections/community.routeros/blob/main/CHANGELOG.rst) for all changes.

[Gwmngilfen (work)](https://matrix.to/#/@gwmngilfen:ansible.im) reports

> community.crypto 1.9.6 has been released (with a bugfix)

[felixfontein](https://github.com/felixfontein) says

> community.crypto 2.0.0 has been released!
> 
> community.general 3.8.1 has been released
> community.genreal 4.0.0 has been released

## Community Updates

[cybette](https://matrix.to/#/@cybette:ansible.im) reports

> ### Live News Reporting
> 
> We're trying out a new way to report news! If you have _anything_ to share about what you've been up to with Ansible lately, at any time, simply hop into [#social:ansible.com](https://matrix.to/#/#social:ansible.com) and leave a message, tagging [newsbot](https://matrix.to/#/@newsbot:ansible.im). Your update will then be included in the next edition of the Bullhorn (pending editor approval, of course).
> 
> The intention here is to drive discussion around the news - while we have the [GitHub issue](https://github.com/ansible/community/issues/546) for logging news, we felt it was a little dry. The Ansible community is a vibrant place, and we want to make it possible for others to comment easily on the news, give feedback, ask questions and so forth.
> 
> The newsbot only listens in [#social:ansible.com](https://matrix.to/#/#social:ansible.com) because we want to make it the place to discuss anything Ansible related, rather than fragmenting the news over many channels. We hope this is a low-effort way of getting the word out about your new release, new project, blog post, event, or anything Ansible-related.
> 
> Feel free to ask myself or [Gwmngilfen](https://matrix.to/#/@gwmngilfen:ansible.im) questions, and you can view a more detailed README [in the repo](https://github.com/ansible-community/ansible.im/blob/main/bots/README.md).

[Gwmngilfen (work)](https://matrix.to/#/@gwmngilfen:ansible.im) says

> If you want to see how this works with a room that is used to it, check out [#twim:matrix.org](https://matrix.to/#/#twim:matrix.org) and the resulting posts at https://matrix.org/blog/category/this-week-in-matrix

[cybette](https://matrix.to/#/@cybette:ansible.im) says

> Please take the [Contributor Survey](https://www.surveymonkey.co.uk/r/GSMSG7K) (whether or not you attended the Contributor Summit, we'd love your feedback!)

## That’s all for now!

Have any questions you’d like to ask, or issues you’d like to see covered? Please ask in [#social:ansible.com](https://matrix.to/#/#social:ansible.com)! See you next time!
