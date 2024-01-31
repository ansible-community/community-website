---
title: "Bullhorn #77"
date: 2022-10-07 23:00 UTC
tags: news
category: bullhorn
type: text
---

![Ansible Bullhorn banner](/images/bullhorn-banner-mango.png)

*A Newsletter for the Ansible Developer Community*
*Issue #77, 2022-10-07 ([Past Issues](https://us19.campaign-archive.com/home/?u=56d874e027110e35dea0e03c1&id=d6635f5420))*

Welcome to [The Bullhorn](https://github.com/ansible/community/wiki/News#the-bullhorn), our newsletter for the Ansible developer community. If you have any questions or content you’d like to share, you're welcome to chat with us in the [Ansible Social room on Matrix](https://matrix.to/#/#social:ansible.com), and mention [`newsbot`](https://matrix.to/#/@newsbot:ansible.im) to have your news item tagged for review for the next weekly issue!

<!-- TEASER_END -->

## KEY DATES ⏱️

[cybette](https://matrix.to/#/@cybette:ansible.im) said

> * 2022-10-10: ETA for Ansible-Core 2.13.5 and Ansible-Core 2.12.10 releases
> * 2022-10-11: [ETA for Ansible 6.5.0 release](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_6.html)
> * 2022-10-11: [DaWGs meeting](https://github.com/ansible/community/issues/643), 15:00 UTC
> * 2022-10-12: [Community WG meeting](https://github.com/ansible/community/issues/645), 18:00 UTC ([topic: List any backwards incompatible collection releases that beta1 should try to accommodate](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_7.html))
> * 2022-10-13: [Bullhorn #78 content deadline](https://github.com/ansible/community/wiki/News#the-bullhorn), 18:00 UTC
> * **2022-10-17: [Ansible Contributor Summit 2022.10](https://hackmd.io/@ansible-community/contrib-summit-202210)**
> * 2022-10-17: [ansible-core 2.14 release candidate 1](https://docs.ansible.com/ansible-core/devel/roadmap/ROADMAP_2_14.html)
> * **2022-10-18/19: [AnsibleFest 2022](https://www.ansible.com/ansiblefest?sc_cid=7013a000002i5g3AAA)**

## GENERAL NEWS UPDATES 🔈️

[gundalow](https://matrix.to/#/@gundalow:ansible.im) said

> Will you be joining [Hacktoberfest](https://hacktoberfest.com/)?
> * We've got some great first issues in the  [awx](https://github.com/ansible/awx/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22) and [awx-operator](https://github.com/ansible/awx-operator/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22) repos
> * New to contributing to AWX, checkout the [AWX Contributor Guide](https://github.com/ansible/awx/blob/devel/CONTRIBUTING.md)
> * Want to chat, join us in [Matrix](https://docs.ansible.com/ansible/latest/community/communication.html#ansible-community-on-matrix) or post a message in the [AWX Google Group](https://groups.google.com/g/awx-project)
> * Don't forget to register via the [Hacktoberfest](https://hacktoberfest.com/) portal to make your contributions count!

## MAJOR NEW RELEASES 🏆️

[relrod](https://matrix.to/#/@relrod:matrix.org) said

> We're happy to announce that the next release of AWX, version 21.7.0 is now available!
> Some notable features include:
> * Improves visibility of workflow approval notification bell
> * Adds project revision hash to inventory source views
> * Prompt on launch on templates
> * Ability to add execution nodes at runtime
> * Add a new Instance.health_check_started field
> * Add tooltips to Instance form; change `name` field to `host name`
> * Adding `prevent_instance_group_fallback` to job templates and inventory
> 
> In addition AWX Operator version 0.30.0 has also been released!
> Some notable features include:
> * change receptor ca secret to tls secret... with migration
> * Add docs for adding execution nodes and custom CA
> 
> Please see the releases pages for more details:
> AWX: [https://github.com/ansible/awx/releases/tag/21.7.0](https://github.com/ansible/awx/releases/tag/21.7.0)
> Operator: [https://github.com/ansible/awx-operator/releases/tag/0.30.0](https://github.com/ansible/awx-operator/releases/tag/0.30.0)

### DevTools [↗](https://github.com/ansible/vscode-ansible) ⛏️

Projects to make it easier to write and test Ansible Content. Includes [VScode extension](https://github.com/ansible/vscode-ansible), [language server](https://github.com/ansible/ansible-language-server), [ansible-lint](https://github.com/ansible-community/ansible-lint), [molecule](https://github.com/ansible-community/molecule), [ansible-navigator](https://github.com/ansible/ansible-navigator) and potentially other development goodies. To see what's planned, and how you can help checkout the [foundation-devtools project board](https://github.com/orgs/ansible/projects/86/views/4)

[ssbarnea](https://matrix.to/#/@ssbarnea:matrix.org) shared

> ansible-lint 6.8.0 is out and contains a huge number of bugfixes, also adding a nice summary report. Details at https://github.com/ansible/ansible-lint/discussions/2568

### Antsibull [↗](https://github.com/ansible-community/antsibull) 🐂

Tooling for building the `Ansible` package and collection documentation.

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) said

> antsibull 0.51.0 ([changelog](https://github.com/ansible-community/antsibull/blob/main/CHANGELOG.rst#v0-51-0)) has been released for Ansible 7. The `python_requires` information from ansible-core is now stored in the `.deps` files as well for easier access, and is used directly in the Ansible package instead of guessing its value based on the ansible-core version number.

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) contributed

> antsibull-docs 1.7.0 ([changelog](https://github.com/ansible-community/antsibull-docs/blob/main/CHANGELOG.rst#v1-7-0)) has been released with some new features and bugfixes. Use `antsibull-docs lint-collection-docs --plugin-docs /path/to/collection-root` to check whether the docs in your collection will render OK on the docsite!

## COLLECTION UPDATES 🪄

[jillr](https://matrix.to/#/@jillr:libera.chat) contributed

> The [community.aws](https://github.com/ansible-collections/community.aws) collection version 5.0.0 has been released. See the [changelog](https://github.com/ansible-collections/community.aws/blob/stable-5/CHANGELOG.rst) for details on new modules and features.

[jillr](https://matrix.to/#/@jillr:libera.chat) shared

> The [amazon.aws](https://github.com/ansible-collections/amazon.aws) collection version 5.0.0 has been released. See the [changelog](https://github.com/ansible-collections/amazon.aws/blob/stable-5/CHANGELOG.rst) for details on new modules and features.

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) shared

> community.general 5.7.0 ([changelog](https://github.com/ansible-collections/community.general/blob/stable-5/CHANGELOG.rst#v5-7-0)) has been released with new modules, features, and bugfixes. Please note that the next minor release (5.8.0) will be the last minor 5.x.0 release, from then on only bugfix releases 5.8.x will be released. After 5.8.0, the 6.0.0 release will be made; see [the current planning in the collection repository](https://github.com/ansible-collections/community.general/issues/582#issuecomment-1264404378) for details.

### Collection removal

[mariolenz](https://matrix.to/#/@mariolenz:matrix.org) contributed

> The `dellemc.os6` collection [is considered unmaintained](https://github.com/ansible-community/community-topics/issues/132) and will be removed from Ansible 8 if no one starts maintaining it again before Ansible 8. See [the removal process for details on how this works](https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst#cancelling-removal-of-an-unmaintained-collection).

[mariolenz](https://matrix.to/#/@mariolenz:matrix.org) shared

> The `dellemc.os9` collection [is considered unmaintained](https://github.com/ansible-community/community-topics/issues/133) and will be removed from Ansible 8 if no one starts maintaining it again before Ansible 8. See [the removal process for details on how this works](https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst#cancelling-removal-of-an-unmaintained-collection).

[mariolenz](https://matrix.to/#/@mariolenz:matrix.org) contributed

> The `dellemc.os10` collection [is considered unmaintained](https://github.com/ansible-community/community-topics/issues/134) and will be removed from Ansible 8 if no one starts maintaining it again before Ansible 8. See [the removal process for details on how this works](https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst#cancelling-removal-of-an-unmaintained-collection).

## HELP WANTED 🙏

[andersson007_](https://matrix.to/#/@andersson007_:matrix.org) contributed

> The following collection inclusion requests are waiting for your review:
> 
> * [dellemc.unity](https://github.com/ansible-collections/ansible-inclusion/discussions/32)
> * [grafana.grafana](https://github.com/ansible-collections/ansible-inclusion/discussions/52)
> 
> See the [process description](https://github.com/ansible-collections/ansible-inclusion#review-process) to learn how to do it.
> 
> If you have any questions, just ping `andersson007` on [Matrix](https://docs.ansible.com/ansible/devel/community/communication.html#ansible-community-on-matrix) in the [#community:ansible.com](https://matrix.to/#/#community:ansible.com) channel or on [Libera.Chat IRC](https://docs.ansible.com/ansible/devel/community/communication.html#ansible-community-on-irc) in the `#ansible-community` channel or directly.
> 
> Please help the community extend the Ansible package!

## PROPOSALS - DISCUSS AND VOTE! 🗳️

[briantist](https://matrix.to/#/@briantist:libera.chat) shared

> **Vote ends on 2022-10-12:** [Clarify inclusion requirements on temp files and editor configs](https://github.com/ansible-community/community-topics/discussions/146).

[mariolenz](https://matrix.to/#/@mariolenz:matrix.org) shared

> As mentioned in [The Bullhorn #72](https://mailchi.mp/redhat/the-bullhorn-72), we consider mellanox.onyx an effectively unmaintained collection. Therefore, we’ve opened a community / steering committee [vote](https://github.com/ansible-community/community-topics/discussions/144) on removing it from the Ansible 8 community package.

## COMMUNITY EVENTS AND MEETUPS 📅

[cybette](https://matrix.to/#/@cybette:ansible.im) contributed

> [Ansible Singapore](https://www.meetup.com/ansible-singapore/) is having their next in-person event on October 13, 2022 at 6:30 PM SST. Check out the [details](https://www.meetup.com/ansible-singapore/events/288946268/) and register!

## THAT'S ALL FOR NOW!

Have any questions you’d like to ask, or issues you’d like to see covered? Please ask in [#social:ansible.com](https://matrix.to/#/#social:ansible.com)! See you next time!
