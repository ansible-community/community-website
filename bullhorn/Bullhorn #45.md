---
title: "Bullhorn #45"
date: 2022-02-10 22:00 UTC
tags: news
category: bullhorn
type: text
---

![Ansible Bullhorn banner](/images/bullhorn-banner-mango.png)

*A Newsletter for the Ansible Developer Community*
*Issue #45, 2022-02-10 ([Past Issues](https://us19.campaign-archive.com/home/?u=56d874e027110e35dea0e03c1&id=d6635f5420))*

Welcome to [The Bullhorn](https://github.com/ansible/community/wiki/News#the-bullhorn), our newsletter for the Ansible developer community. If you have any questions or content you’d like to share, you're welcome to chat with us in the [Ansible Social room on Matrix](https://matrix.to/#/#social:ansible.com), and mention [`newsbot`](https://matrix.to/#/@newsbot:ansible.im) to have your news item tagged for review for the next weekly issue!

<!-- TEASER_END -->

## KEY DATES

[cybette](https://matrix.to/#/@cybette:ansible.im) shared

> * 2022-02-15: [DaWGs meeting](https://github.com/ansible/community/issues/643), 16:00 UTC
> * 2022-02-16: [Community WG meeting](https://github.com/ansible/community/issues/645), 18:00 UTC (propose topics [here](https://github.com/ansible-community/community-topics/issues))
> * 2022-02-17: [Bullhorn #46 content deadline](https://github.com/ansible/community/wiki/News#the-bullhorn), 18:00 UTC
> * 2022-02-22: [ETA for Ansible 5.4.0 release](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_5.html)
> * 2022-02-28: ETA for Ansible-Core 2.12.3, Ansible-Core 2.11.9, and Ansible-Base 2.10.18 releases (if those releases have updates)

## GENERAL NEWS UPDATES

[cybette](https://matrix.to/#/@cybette:ansible.im) shared

> We are closing [issue 546](https://github.com/ansible/community/issues/546) and will not be accepting news items for [The Bullhorn](https://github.com/ansible/community/wiki/News#the-bullhorn) via the GitHub issue any longer. Please continue to share your news reports with [newsbot](https://matrix.to/#/@newsbot:ansible.im) (in the [Ansible Social room on Matrix](https://matrix.to/#/#social:ansible.com)) as most of you have been doing already. Thank you!

[ssbarnea](https://matrix.to/#/@ssbarnea:matrix.org) contributed

> Both ansible-lint and molecule will require python 3.8+ on their next major change, following similar ansible-core move.  Once the pending PRs are merged, the main branches will be py38+ only. We will keep a stable branch for the older versions and backporting.

[trishnaguha](https://github.com/trishnaguha) said

> Ansible Networking CY22 Q1-Q2 Tentative Roadmap is published [HERE](https://github.com/ansible/community/wiki/Network:-CY22-Q1-Q2-Roadmap). 

## MAJOR NEW RELEASES

### DevTools [↗](https://github.com/ansible-community/molecule)

Projects to make it easier to write and test Ansible Content. Includes [VScode extension](https://github.com/ansible/vscode-ansible), [language server](https://github.com/ansible/ansible-language-server), [ansible-lint](https://github.com/ansible-community/ansible-lint), [molecule](https://github.com/ansible-community/molecule), [ansible-navigator](https://github.com/ansible/ansible-navigator) and potentially other development goodies. To see what's planned, and how you can help checkout the [foundation-devtools project board](https://github.com/orgs/ansible/projects/86/views/4)

[ssbarnea](https://matrix.to/#/@ssbarnea:matrix.org) contributed

> molecule 3.6.0 has been released https://github.com/ansible-community/molecule/releases/tag/v3.6.0

## COLLECTION UPDATES

[andersson007_](https://matrix.to/#/@andersson007_:matrix.org) said

> community.postgresql [1.7.0](https://github.com/ansible-collections/community.postgresql/blob/stable-1/CHANGELOG.rst) and [2.0.0](https://github.com/ansible-collections/community.postgresql/blob/main/CHANGELOG.rst) have been released. Many thanks to [hunleyd](https://github.com/hunleyd), [klando](https://github.com/klando), [MichaelDBA](https://github.com/MichaelDBA), [marcosdiez](https://github.com/marcosdiez), [tcraxs](https://github.com/tcraxs), [felixfontein](https://github.com/felixfontein), and [jtelcontar](https://github.com/jtelcontar)!

## HELP WANTED

[samccann](https://matrix.to/#/@samccann:ansible.im) contributed

> Looking for a way to contribute to Ansible? How about starting with one of these easyfix issues? https://github.com/ansible/ansible/issues?q=is%3Aopen+is%3Aissue+label%3Aeasyfix

## PROPOSALS - DISCUSS AND VOTE!

[cognifloyd (Jacob Floyd)](https://matrix.to/#/@cognifloyd:matrix.org) said

> RFR (please bikeshed the interface) https://github.com/ansible-community/ansible-lint/pull/1828
> This PR is the first of a series of PRs that will allow ansible-lint to modify files and not just lint them. Please help me figure out what interface we should use for these features.

[ssbarnea](https://matrix.to/#/@ssbarnea:matrix.org) said

> Due to reasons explained in https://github.com/ansible-community/ansible-lint/pull/1850 ansible-lint is about to drop support for py36/py37 on its main branch, but we will keep a stable branch for older version. Please review this PR, especially those that already contribute to the project.

[gundalow](https://matrix.to/#/@gundalow:ansible.im) contributed

> Now that CentOS 8 [has been fully discontinued](https://lists.centos.org/pipermail/centos-announce/2020-December/048208.html), most package mirrors have begun culling CentOS 8 content, which breaks all `ansible-test` CentOS 8 containers configured on discontinued production package mirrors. Rather than rebuilding all versions of the affected containers to use the `vault.centos.org` package mirrors or moving to a clone distro, we're just discontinuing test container support for CentOS 8. This decision is based largely on the fact that RHEL 8 test VM support via ansible-core-ci is available on all branches to provide nearly identical test coverage.
> 
> We recommend that projects immediately remove any `centos8/` ansible-test container entries in their CI matrices, as they will likely fail on tasks that require access to a package mirror. Projects running their CI under Ansible's Azure Pipelines subscription can replace those CentOS 8 matrix entries with `rhel8.2/` - `rhel8.5/` (depending on which version of ansible-test is in use) to get nearly identical coverage under a RHEL 8 VM, provided and paid for by Ansible.
> 
> If you want to discuss this, we welcome feedback in [ansible-collections/news-for-maintainers/discussions/4](https://github.com/ansible-collections/news-for-maintainers/discussions/4).

## COMMUNITY UPDATES

[Gwmngilfen](https://matrix.to/#/@gwmngilfen:ansible.im) shared

> ### FOSDEM Recordings
> 
> [FOSDEM](https://fosdem.org/2022/) was a blast! I gave a talk recapping the last 6 months of our journey with Ansible and Matrix. There's no surprises here, it's mostly a video version of my blogs from last year, along with some data about how it's going so far, but if you're interested, you can catch the video [on the FOSDEM site](https://fosdem.org/2022/schedule/event/matrix_ansible/).
> 
> If video is not your thing, then worry not as I also plan to write up a blog post of the situation so far in a month or so - so there'll be a written version for you soon!

[dmsimard](https://matrix.to/#/@dmsimard:matrix.org) said

> If you couldn't make it to FOSDEM, the recording of my talk `Simple (but useful) Ansible reporting with ara` is now available: https://fosdem.org/2022/schedule/event/ansible_reporting_ara/
> 
> I go into why I created the project back in 2016 and how it might be useful to you before doing a live demo where I stand up an instance of AWX and record a job's playbook results with ara.
> 
> It was fun and I hope you'll enjoy it too, feel free to reach out if you would like to chat or have any questions!

### Maintainers [↗](https://github.com/ansible-community)

Maintainers help to run the community!

[andersson007_](https://matrix.to/#/@andersson007_:matrix.org) shared

> We are happy to announce that the [community.rabbitmq](https://github.com/ansible-collections/community.rabbitmq) collection has found a new maintainer - Chris Smart ([csmart](https://github.com/csmart) on GitHub/Matrix). Chris is also a maintainer of the [community.libvirt](https://github.com/ansible-collections/community.libvirt) collection where he has been doing a great job.
> Our congratulations, Chris, and thank you again! :)

[IPvSean](https://github.com/IPvSean) shared

> For Ansible Network Automation I have produced two videos:
> 
> Five great use cases for Ansible Network Automation https://youtu.be/wXUgYfZKMHU
> Automated NetOps - Ansible for Network GitOps https://youtu.be/JqE13sP2sq8

## COMMUNITY EVENTS AND MEETUPS

[cybette](https://matrix.to/#/@cybette:ansible.im) contributed

> There’s an “Ansible Anwendertreffen” (Ansible user meeting) which will be held on Feb 15, 2022. This is a virtual event conducted mainly in German. If you are interested, you can find the details and registration info [here](https://www.ansible-anwender.de/post/2022/01/register/).

[cybette](https://matrix.to/#/@cybette:ansible.im) said

> [Ansible Minneapolis](https://www.meetup.com/Ansible-Minneapolis/) group is having a February Ansible Meetup at Waldman Brewing on Thursday, Feb 17. Check the details and RSVP [here](https://www.meetup.com/Ansible-Minneapolis/events/lndxqsydcdbwb/).

## THAT'S ALL FOR NOW!

Have any questions you’d like to ask, or issues you’d like to see covered? Please ask in [#social:ansible.com](https://matrix.to/#/#social:ansible.com)! See you next time!
