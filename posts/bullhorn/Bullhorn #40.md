---
title: "Bullhorn #40"
date: 2021-12-21 22:30 UTC
tags: news
category: bullhorn
type: text
---

![Ansible Bullhorn banner](/images/bullhorn-banner-mango.png)

*A Newsletter for the Ansible Developer Community*
*Issue #40, 2021-12-21 ([Past Issues](https://us19.campaign-archive.com/home/?u=56d874e027110e35dea0e03c1&id=d6635f5420))*

Welcome to the Bullhorn, our newsletter for the Ansible developer community. If you have any questions or content you’d like to share, please reach out to us at the-bullhorn@redhat.com, or chat with us in the [Ansible Social room on Matrix](https://matrix.to/#/#social:ansible.com).

This will be the last issue for 2021. A big THANKS to every one of you for all of your contributions! Happy holidays and see you in 2022 :tada:

<!-- TEASER_END -->

## KEY DATES

[cybette](https://matrix.to/#/@cybette:ansible.im) shared

> * 2021-12-22: [Community WG meeting](https://github.com/ansible/community/issues/539), 18:00 UTC (last meeting of the year!)
> * 2022-01-04: [DaWGs meeting](https://github.com/ansible/community/issues/643), 16:00 UTC
> * 2022-01-05: [Community WG meeting](https://github.com/ansible/community/issues/539), 18:00 UTC (propose topics [here](https://github.com/ansible-community/community-topics/issues))
> * 2022-01-05: [Bullhorn #41 content deadline](https://github.com/ansible/community/issues/546)
> * 2022-01-06: [D&I working group meeting](https://github.com/ansible/community/issues/577), 19:00 UTC
> * 2022-01-11: [ETA for Ansible 5.2.0 release](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_5.html)
> * 2022-01-31: ETA for Ansible-Core 2.12.2, Ansible-Core 2.11.8, and Ansible-Base 2.10.17 releases

## GENERAL NEWS UPDATES

[andersson007_](https://matrix.to/#/@andersson007_:matrix.org) contributed

> Here's a reminder that the [community-docs](https://github.com/ansible/community-docs/) repository, among other useful documents, contains the following ones:
> * [Contributing to Ansible Guidelines](https://github.com/ansible/community-docs/blob/main/contribution_to_project.rst) describes many different ways you can contribute to the Open Source projects of the Ansible ecosystem.
> * [Contributor Path](https://github.com/ansible/community-docs/blob/main/contributor_path.rst) describes a contributor path in scope of the Ansible project from the early beginning.
> * [Quick-Start Development Guide](https://github.com/ansible/community-docs/blob/main/create_pr_quick_start_guide.rst) describes all the steps needed to create your first patch and submit a pull request.
> * [Collection Maintainer Guidelines](https://github.com/ansible/community-docs/blob/main/maintaining.rst) contains an overview of maintenance-related tasks, criteria for becoming a maintainer, along with recommendations on how to build a healthy and active community around your collection.
> 
> Community feedback will be very valuable! So if you know how to make the documents better, please create issues / pull requests.

[dmsimard](https://matrix.to/#/@dmsimard:libera.chat) said

> ansible 5.0.0 has been deleted, please use ansible 5.0.1 (or the just released 5.1.0) if you have python>=3.8 available, or ansible 4.10.0 if you have python version prior to 3.8 -- more information in https://groups.google.com/g/ansible-announce/c/t0JoB6evpt8/m/UHzmz8-2CgAJ

## MAJOR NEW RELEASES

### Ansible [↗](https://github.com/ansible-collections)

**ansible** is a batteries-included package providing a curated set of Ansible collections in addition to ansible-core

[dmsimard](https://matrix.to/#/@dmsimard:libera.chat) contributed

> ansible 4.10.0 has been released: https://groups.google.com/g/ansible-announce/c/BJxz60-mq7w -- it's the last 4.x maintenance release now that ansible 5.x is out. There's instructions included in the announcement for getting collection updates from Ansible 5 for users that wish to stay on ansible-core 2.11.x.

[dmsimard](https://matrix.to/#/@dmsimard:libera.chat) said

> ansible 5.1.0 has been released: https://groups.google.com/g/ansible-announce/c/_R6rfPkj028

### Antsibull [↗](https://github.com/ansible-community/antsibull)

Tooling for building various things related to ansible

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) contributed

> antsibull-changelog 0.13.0 has been released ([changelog](https://github.com/ansible-community/antsibull-changelog/blob/main/CHANGELOG.rst#v0-13-0)). This release should make releasing more reliable by fixing bugs and automatically linting before releasing.

### Ansible-Core [↗](https://github.com/ansible/ansible)

**ansible-core** is a minimal package containing the base engine, modules, and plugins

[nitzmahone](https://github.com/nitzmahone) shared

> New releases: [ansible-core 2.12.1, ansible-core 2.11.7, ansible-base 2.10.16](https://groups.google.com/g/ansible-devel/c/iJ4MjQWflsI).

## COLLECTION UPDATES

[briantist](https://github.com/briantist) shared

> [`community.hashi_vault` version `2.1.0` has been released](https://github.com/ansible-collections/community.hashi_vault/releases/tag/2.1.0), with some deprecations and a rename of the `aws_iam_login` auth method to `aws_iam`.

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) contributed

> community.crypto 2.0.2 has been released with some documentation fixes.

[akasurde](https://matrix.to/#/@akasurde:ansible.im) said

> community.vmware 1.17.0 has been released. You can read more information [here](https://github.com/ansible-collections/community.vmware/blob/1.17.0/CHANGELOG.rst#v1-17-0).

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) shared

> community.docker 1.10.2 and 2.0.2 have been released with bugfixes for the `community.docker.nsenter` and `community.docker.docker_api` connection plugins and the `community.docker.docker_container_exec` module ([2.0.2 changelog](https://github.com/ansible-collections/community.docker/blob/main/CHANGELOG.rst#v2-0-2), [1.10.2 changelog](https://github.com/ansible-collections/community.docker/blob/stable-1/CHANGELOG.rst#v1-10-2)).

[alinabuzachis](https://github.com/alinabuzachis) said

> [`amazon.aws` version `3.0.0` has been released.](https://github.com/ansible-collections/amazon.aws/releases/tag/3.0.0)

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) contributed

> community.general 3.8.3 has been released with some bugfixes ([changelog](https://github.com/ansible-collections/community.general/blob/stable-3/CHANGELOG.rst)).

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) said

> community.general 4.2.0 has been released with new features and bugfixes ([changelog](https://github.com/ansible-collections/community.general/blob/stable-4/CHANGELOG.rst)).

## HELP WANTED

[samccann](https://matrix.to/#/@smccann:matrix.org) said

> Looking for help with some `easyfix` Ansible docs issues - https://github.com/ansible/ansible/issues?q=is%3Aopen+is%3Aissue+label%3Adocs+label%3Aeasyfix

[jillr](https://github.com/jillr) shared

> The Ansible [Diversity Working Group](https://github.com/ansible/community/wiki/Diversity) is looking to grow! If you're interested in helping make the Ansible community a more representative and welcoming community for all, join us in `#ansible-diversity` on Matrix or IRC. We are also looking to learn from other Diversity groups so if you know of any, please add the link to [this issue](https://github.com/ansible/community/issues/641).

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) contributed

> We are looking for feedback on improving the Ansible documentation by mentioning the plugin type more prominently in some cases. Please take a look here: https://github.com/ansible-community/community-topics/issues/57

[samccann](https://matrix.to/#/@smccann:matrix.org) shared

> We are looking for feedback on whether we should highlight FQCN for ansible-core built in modules, or use just the short name in our documentation and examples. Please provide your thoughts at https://github.com/ansible-community/community-topics/issues/58

## COMMUNITY UPDATES

### Maintainers [↗](https://github.com/ansible-community)

Maintainers help to run the community!

[gundalow](https://matrix.to/#/@gundalow:ansible.im) shared

> A lot has been happening in the [community.zabbix](https://github.com/ansible-collections/community.zabbix/) collection. They've gained two new maintainers, [rockaut](https://github.com/rockaut) and [ragingpastry](https://github.com/ragingpastry), congratulations to both and thank you for your continued great work. The team has recently released version [1.5.1](https://github.com/ansible-collections/community.zabbix/blob/main/CHANGELOG.rst#v1-5-1). If you're interested in Zabbix, join the active discussion in [#community-zabbix_community:gitter.im](https://matrix.to/#/#community-zabbix_community:gitter.im) via Matrix.

## COMMUNITY EVENTS/MEETUPS

[cybette](https://matrix.to/#/@cybette:ansible.im) contributed

> [Calling for participation](https://cfp.cfgmgmtcamp.org/fosdem2022/cfp) for the [FOSDEM 2022](https://fosdem.org/2022/) Infra Management Devroom. Possible topics include configuration management, infrastructure automation, and much more! Check out the [details](https://cfp.cfgmgmtcamp.org/fosdem2022/cfp) and submit your proposals by 2021-12-31 23:55 (Europe/Brussels).

## THAT'S ALL FOR NOW!

Have any questions you’d like to ask, or issues you’d like to see covered? Please ask in [#social:ansible.com](https://matrix.to/#/#social:ansible.com)! See you next time!
