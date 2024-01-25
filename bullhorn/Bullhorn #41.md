---
title: "Bullhorn #41"
date: 2022-01-07 14:00 UTC
tags: news
category: bullhorn
type: text
---

![Ansible Bullhorn banner](/images/bullhorn-banner-mango.png)

*A Newsletter for the Ansible Developer Community*
*Issue #41, 2022-01-07 ([Past Issues](https://us19.campaign-archive.com/home/?u=56d874e027110e35dea0e03c1&id=d6635f5420))*

Welcome to the Bullhorn, our newsletter for the Ansible developer community. If you have any questions or content you’d like to share, please reach out to us at the-bullhorn@redhat.com, or chat with us in the [Ansible Social room on Matrix](https://matrix.to/#/#social:ansible.com).

Happy New Year to our wonderful Ansible Developer Community! We look forward to collaborating more with all of you in 2022!

<!-- TEASER_END -->

## KEY DATES

[cybette](https://matrix.to/#/@cybette:ansible.im) contributed

> * 2022-01-11: [ETA for Ansible 5.2.0 release](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_5.html)
> * 2022-01-11: [DaWGs meeting](https://github.com/ansible/community/issues/643), 16:00 UTC
> * 2022-01-12: [Community WG meeting](https://github.com/ansible/community/issues/645), 18:00 UTC (propose topics [here](https://github.com/ansible-community/community-topics/issues))
> * 2022-01-13: [Bullhorn #42 content deadline](https://github.com/ansible/community/issues/546)
> * 2022-01-18: [DaWGs meeting](https://github.com/ansible/community/issues/643), 16:00 UTC
> * 2022-01-19: [Community WG meeting](https://github.com/ansible/community/issues/645), 18:00 UTC (propose topics [here](https://github.com/ansible-community/community-topics/issues))
> * 2022-01-31: ETA for Ansible-Core 2.12.2, Ansible-Core 2.11.8, and Ansible-Base 2.10.17 releases

## GENERAL NEWS UPDATES

[gundalow](https://matrix.to/#/@gundalow:ansible.im) shared

> We are happy to announce a new [Steering Committee](https://www.ansible.com/blog/ansible-community-steering-committee) member!
> Brian Scholer ([briantist](https://github.com/briantist)) has been a very active community member for several years.
> He has contributed to the Ansible project as a developer, reviewer, collection maintainer, documentation contributor; he has helped other contributors and users on IRC / Matrix and GitHub, as well as the Steering Committee make the right decisions.
> We are happy to get him on board!
> Our congratulations, Brian, and thank you for your great long-term contribution!

## MAJOR NEW RELEASES

### Antsibull [↗](https://github.com/ansible-community/antsibull)

Tooling for building various things related to ansible

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) said

> antsibull 0.40.0 has been released with a lot of features and bugfixes. A major new feature are responsive RST tables for parameters and return values. Also there's now a [changelog](https://github.com/ansible-community/antsibull/blob/main/CHANGELOG.rst).

## COLLECTION UPDATES

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) shared

> community.docker 2.1.0 has been released with bugfixes and new features, mainly for the `community.docker.docker_container_exec` module ([changelog](https://github.com/ansible-collections/community.docker/blob/main/CHANGELOG.rst)).

[briantist](https://matrix.to/#/@briantist:libera.chat) said

> [`community.hashi_vault` version `2.2.0` has been released](https://github.com/ansible-collections/community.hashi_vault/releases/tag/2.2.0).

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) contributed

> community.internal_test_tools 0.6.0 has been released ([changelog](https://github.com/ansible-collections/community.internal_test_tools/blob/main/CHANGELOG.rst)).

[markuman](https://matrix.to/#/@markuman:libera.chat) said

> community.proxysql 1.3.1 has just been released.

## HELP WANTED

[samccann](https://matrix.to/#/@smccann:matrix.org) shared

> Looking for a way to contribute to Ansible? How about starting with one of these easyfix issues? https://github.com/ansible/ansible/issues?q=is%3Aopen+is%3Aissue+label%3Aeasyfix

## PROPOSALS - DISCUSS AND VOTE!

[samccann](https://matrix.to/#/@smccann:matrix.org) said

> We are looking for collection owners to provide feedback on a new semantic markup proposal for plugin/module docs - https://github.com/ansible-community/community-topics/issues/53

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) contributed

> We are looking for feedback on improving the Ansible documentation by mentioning the plugin type more prominently in some cases. Please take a look here: https://github.com/ansible-community/community-topics/issues/57

[samccann](https://matrix.to/#/@smccann:matrix.org) shared

> We are looking for feedback on whether we should highlight FQCN for ansible-core built in modules, or use just the short name in our documentation and examples. Please provide your thoughts at https://github.com/ansible-community/community-topics/issues/58

## COMMUNITY UPDATES

[dmsimard](https://matrix.to/#/@dmsimard:libera.chat) said

> I had a holiday hacking project to stand up the latest version of AWX to find out and write down how to record playbooks with ara and I've finished it sooner than I thought I would, enjoy: https://ara.recordsansible.org/blog/2021/12/23/recording-ansible-playbooks-from-awx-with-ara/

[cybette](https://matrix.to/#/@cybette:ansible.im) contributed

> How to automate the Vulnerability Scanner/Detector for Log4Shell (CVE-2021–44228) using Ansible? Check out this [guide](https://www.ansiblepilot.com/articles/vulnerability-scanner-detector-log4shell-remote-code-execution-log4j-cve-2021-44228-ansible-log4j-cve-2021-44228/) thanks to [Luca Berton](https://github.com/lucab85/).
> 
> Ansible Playbook code available (via [Github](https://github.com/lucab85/log4j-cve-2021-44228), [Galaxy](https://galaxy.ansible.com/lucab85/ansible_role_log4shell)) to download the detector script (v1.2 released 2021-12-20), validate GPG signature, install dependencies, create work directory, run the detector with the right options and get the results.

## COMMUNITY EVENTS/MEETUPS

[cybette](https://matrix.to/#/@cybette:ansible.im) shared

> Join us at the open source community conference, [DevConf.CZ 2022](https://www.devconf.info/cz/) - virtual event, for an [Ansible Community Meetup](https://sched.co/siJx) on Friday Jan-28 and a session on [What’s New & Ahead in the Ansible Community](https://sched.co/siJE) on Saturday Jan-29.

## THAT'S ALL FOR NOW!

Have any questions you’d like to ask, or issues you’d like to see covered? Please ask in [#social:ansible.com](https://matrix.to/#/#social:ansible.com)! See you next time!
