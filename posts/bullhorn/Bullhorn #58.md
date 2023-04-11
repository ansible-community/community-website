---
title: "Bullhorn #58"
date: 2022-05-13 12:15 UTC
tags: news
category: bullhorn
type: text
---

![Ansible Bullhorn banner](/images/bullhorn-banner-mango.png)

*A Newsletter for the Ansible Developer Community*
*Issue #58, 2022-05-13 ([Past Issues](https://us19.campaign-archive.com/home/?u=56d874e027110e35dea0e03c1&id=d6635f5420))*

Welcome to [The Bullhorn](https://github.com/ansible/community/wiki/News#the-bullhorn), our newsletter for the Ansible developer community. If you have any questions or content you’d like to share, you're welcome to chat with us in the [Ansible Social room on Matrix](https://matrix.to/#/#social:ansible.com), and mention [`newsbot`](https://matrix.to/#/@newsbot:ansible.im) to have your news item tagged for review for the next weekly issue!

<!-- TEASER_END -->

## KEY DATES ⏱️

[cybette](https://matrix.to/#/@cybette:ansible.im) said

> * 2022-05-16: [ETA for Ansible-Core 2.13 GA](https://docs.ansible.com/ansible-core/devel/roadmap/ROADMAP_2_13.html) - note [schedule change](https://groups.google.com/g/ansible-devel/c/UlHhhRDVUzc)
> * 2022-05-17: [ETA for Ansible 5.8.0 release](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_5.html)
> * 2022-05-17: [DaWGs meeting](https://github.com/ansible/community/issues/643), 15:00 UTC
> * 2022-05-18: [Community WG meeting](https://github.com/ansible/community/issues/645), 18:00 UTC (propose topics [here](https://github.com/ansible-community/community-topics/issues))
> * 2022-05-19: [Bullhorn #59 content deadline](https://github.com/ansible/community/wiki/News#the-bullhorn), 18:00 UTC
> * 2022-05-23: [End-of-life for upstream Ansible 2.9 and Ansible-base 2.10](https://groups.google.com/g/ansible-announce/c/kegIH5_okmg/)
> * 2022-05-23: ETA for Ansible-Core 2.12.6 and Ansible-Core 2.11.12 releases
> * 2022-06-21: [ETA for Ansible 6.0.0 GA](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_6.html)

## GENERAL NEWS UPDATES 🔈️

[dmsimard](https://matrix.to/#/@dmsimard:matrix.org) shared

> Hi o/
> 
> We're working on implementing regular testing of ansible-test's sanity checks across every collection included in the Ansible community package and found that many are failing sanity tests. It would be great to fix as many as we can before the release of Ansible 6 around 2022-06-21.
> 
> Most failures are not critical and there's a lot of low-hanging fruits that could contribute to improving the quality of the modules and plugins that are released. It's OK to ignore rules that are not relevant but these should be specified in versioned files such as `tests/sanity/ignore-2.12.txt` in order to avoid warnings and errors.
> 
> There's documentation on sanity tests here: https://docs.ansible.com/ansible/latest/dev_guide/testing_sanity.html
> If you are the maintainer of an included collection or would like to help, you can learn more about the effort and the logs from the sanity tests in this issue: https://github.com/ansible-community/community-topics/issues/96
> 
> If you'd like to chat about Ansible packaging in general, find us in:
> - #ansible-community and #ansible-packaging on libera.chat, or
> - [#community:ansible.com](https://matrix.to/#/#community:ansible.com) and [#packaging:ansible.com](https://matrix.to/#/#packaging:ansible.com) on matrix

### Ansible [↗](https://github.com/ansible-collections) 📦️

The `Ansible` package includes `ansible-core` and is a batteries-included package that provides a curated set of Ansible collections. See the [Ansible roadmaps](https://docs.ansible.com/ansible/devel/roadmap/ansible_roadmap_index.html) for future release plans.

[ompragash](https://matrix.to/#/@ompragash:ansible.im) contributed

> Ansible 6 Alpha PPA package is available for the Ubuntu Jammy (22.04LTS) release!🎉
> 
> Contributors are welcome to test the package and provide us with feedback!❤️
> 
> Follow the instructions to install and test Ansible 6 Alpha on ubuntu:jammy docker container:
> 
> ~~~
> # docker run --name=test-ansible6 -td ubuntu:jammy bash
> # docker exec -it test-ansible6 bash
> 
> root@ed6c0c4e2adc:/# TZ=America/New_York && ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
> root@ed6c0c4e2adc:/# apt-get update && apt -y install software-properties-common
> root@ed6c0c4e2adc:/# add-apt-repository ppa:ansible/testing-ansible-6 -y && apt-get update
> root@ed6c0c4e2adc:/# apt install ansible -y
> ~~~
> 
> If you run into installation issues or technical errors, kindly report it on the `ansible-community/ppa` repo [here](https://github.com/ansible-community/ppa/issues/new).

## COLLECTION UPDATES 🪄

[andersson007_](https://matrix.to/#/@andersson007_:matrix.org) contributed

> The [vmware.vmware_rest](https://galaxy.ansible.com/vmware/vmware_rest) collection has been [included](https://github.com/ansible-community/ansible-build-data/pull/120) in Ansible 5. Thanks to everyone involved!

[andersson007_](https://matrix.to/#/@andersson007_:matrix.org) said

> The [community.mysql](https://github.com/ansible-collections/community.mysql) collection [1.4.5](https://github.com/ansible-collections/community.mysql/blob/stable-1/CHANGELOG.rst), [2.3.6](https://github.com/ansible-collections/community.mysql/blob/stable-2/CHANGELOG.rst) and [3.2.0](https://github.com/ansible-collections/community.mysql/blob/main/CHANGELOG.rst) versions have been released! Thanks to [rsicart](https://github.com/rsicart), [betanummeric](https://github.com/betanummeric), [nerijus](https://github.com/nerijus) , [kzinas-adv](https://github.com/kzinas-adv), [pookey](https://github.com/pookey), [the02](https://github.com/the02) and [hubiongithub](https://github.com/hubiongithub)!

[briantist](https://matrix.to/#/@briantist:libera.chat) contributed

> [community.hashi_vault version 2.5.0](https://github.com/ansible-collections/community.hashi_vault/releases/tag/2.5.0) has been released with new KV plugins and more. See the release notes and changelog for more information. This is the last expected release before 3.0.0.

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) shared

> community.crypto 2.3.0 ([changelog](https://github.com/ansible-collections/community.crypto/blob/main/CHANGELOG.rst#v2-3-0)) and 1.9.14 ([changelog](https://github.com/ansible-collections/community.crypto/blob/stable-1/CHANGELOG.rst#v1-9-14)) have been released with new features and bugfixes.

## PROPOSALS - DISCUSS AND VOTE! 🗳️

[mariolenz](https://matrix.to/#/@mariolenz:matrix.org) shared

> If you are maintaining a collection that is part of the Ansible community package, you might be interested in the discussion to have a [mandatory machine-readable maintainers file](https://github.com/ansible-community/community-topics/issues/100) in the collections.

[andersson007_](https://matrix.to/#/@andersson007_:matrix.org) said

> The Community and Steering committee will be grateful for any feedback on the [What to do with a lack of collection inclusion reviews](https://github.com/ansible-community/community-topics/issues/97) community topic. The backlog of [submitted collections](https://github.com/ansible-collections/ansible-inclusion/discussions/) is growing. How can we fix the situation? See the topic for details.

[mariolenz](https://matrix.to/#/@mariolenz:matrix.org) contributed

> For people using the Ansible community package, there is no generic way to find out the version they are running. `ansible --version` just gives the ansible-core version, so they have to rely on their specific package manager (pip, dpkg, rpm...). If you think there should be a generic way, please add your views to the [CLI program which prints the Ansible package's version](https://github.com/ansible-community/community-topics/issues/89) discussion.

## COMMUNITY UPDATES 👂️

[cybette](https://matrix.to/#/@cybette:ansible.im) shared

> ### Ansible Contributor Survey
> 
> Feedback is really important to us so we can keep on improving the Contributor Experience for our wonderful Ansible Community. Please take a few minutes to fill in the [Contributor Survey](https://www.surveymonkey.co.uk/r/TDB8YQK) that we have put together!

[hunleyd](https://matrix.to/#/@hunleyd:matrix.org) said

> The `community.postgresql` collection maintainers are pleased to announce the immediate availability of a new Matrix room (https://matrix.to/#/#postgresql:ansible.com) for all users interested in the collection! If you're a current user of the collection seeking help (or wanting to help others), a new user interested in finding out about the collection, or just curious about PostgreSQL and how to use it in your Ansible plays, please feel free to join us and have a chat.

## COMMUNITY EVENTS AND MEETUPS 📅

[cybette](https://matrix.to/#/@cybette:ansible.im) contributed

> [Ansible München](https://www.meetup.com/Ansible-Munchen/) group is organizing an [Ansible SpringFest!](https://www.meetup.com/Ansible-Munchen/events/284695940/) It will be on Tuesday, May 31st, starting from 18:00 CEST at Einstein Kultur. There will be 2 talks, "Ansible Automation for SAP - Deployment, Operations and Modernization" and "Ansible and Kubernetes - an alternative to Helm". See [here](https://www.meetup.com/Ansible-Munchen/events/284695940/) for more details and RSVP.

## THAT'S ALL FOR NOW!

Have any questions you’d like to ask, or issues you’d like to see covered? Please ask in [#social:ansible.com](https://matrix.to/#/#social:ansible.com)! See you next time!
