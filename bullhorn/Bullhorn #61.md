---
title: "Bullhorn #61"
date: 2022-06-02 21:45 UTC
tags: news
category: bullhorn
type: text
---

![Ansible Bullhorn banner](/images/bullhorn-banner-mango.png)

*A Newsletter for the Ansible Developer Community*
*Issue #61, 2022-06-02 ([Past Issues](https://us19.campaign-archive.com/home/?u=56d874e027110e35dea0e03c1&id=d6635f5420))*

Welcome to [The Bullhorn](https://github.com/ansible/community/wiki/News#the-bullhorn), our newsletter for the Ansible developer community. If you have any questions or content you’d like to share, you're welcome to chat with us in the [Ansible Social room on Matrix](https://matrix.to/#/#social:ansible.com), and mention [`newsbot`](https://matrix.to/#/@newsbot:ansible.im) to have your news item tagged for review for the next weekly issue!

<!-- TEASER_END -->

## KEY DATES ⏱️

[cybette](https://matrix.to/#/@cybette:ansible.im) contributed

> * 2022-06-07: [ETA for Ansible 5.9.0 release](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_5.html)
> * 2022-06-07: [ETA for Ansible 6.0.0 rc1](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_6.html)
> * 2022-06-07: [DaWGs meeting](https://github.com/ansible/community/issues/643), 15:00 UTC
> * 2022-06-08: [Community WG meeting](https://github.com/ansible/community/issues/645), 18:00 UTC (propose topics [here](https://github.com/ansible-community/community-topics/issues))
> * 2022-06-09: [Bullhorn #62 content deadline](https://github.com/ansible/community/wiki/News#the-bullhorn), 18:00 UTC
> * 2022-06-20: ETA for Ansible-Core 2.12.7 and Ansible-Core 2.11.13 releases (if those releases have updates)
> * 2022-06-21: [ETA for Ansible 6.0.0 GA](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_6.html)
> * 2022-07-15: Deadline for [CFP submission](https://reg.experiences.redhat.com/flow/redhat/rhaf22/cfp/login) for [AnsibleFest 2022](https://www.ansible.com/ansiblefest)

## GENERAL NEWS UPDATES 🔈️

[ompragash](https://matrix.to/#/@ompragash:ansible.im) shared

> We are happy to announce that we've issued the first set of "Ansible Badges"!🕺🏻🎉
> 
> Yes, you heard us right!
> 
> As we announced during the last Contributor Summit, we issued badges to Meetup Organizers and Speakers, and we're looking forward to issuing badges for GitHub contributions, completing Instruqt challenges, and more. To know more about "Ansible Badges", check out [ansible-community/ansible-badges](https://github.com/ansible-community/ansible-badges/blob/main/README.md)!
> 
> We love to hear your feedback❤️ Click [here](https://github.com/ansible-community/ansible-badges/discussions/new) and submit!

[samccann](https://matrix.to/#/@samccann:ansible.im) said

> Need help writing or editing your collection docs? We have community writers ready to help review docs PRs and provide basic help using the Edit on GitHub feature. These writers can provide grammar and readability advice for your collection docs or other Ansible community project docs. Ping us in the #docs [matrix](https://matrix.to/#/#docs:ansible.com)/[irc](https://web.libera.chat/#ansible-docs) channels to get details on how we can help, and see the project tracking board [here](https://github.com/orgs/ansible-community/projects/3/views/1).

[ompragash](https://matrix.to/#/@ompragash:ansible.im) shared

> Ansible 6 Beta 2 is out for testing!🎉
> 
> For more details about the changelog, installation, and included collections click [here](https://groups.google.com/g/ansible-project/c/ZFgxNPk9ITw).
> 
> If you face issues during installation, reach out to us in #ansible-packaging [Matrix room](https://matrix.to/#/#packaging:ansible.com) or [IRC channel](https://web.libera.chat/#ansible-packaging).
> 
> On behalf of the Ansible community, thank you, and happy automating!

## MAJOR NEW RELEASES 🏆️

[John Westcott](https://matrix.to/#/@john-westcotti-iv:matrix.org) contributed

> We're happy to announce that [AWX version 21.1.0](https://github.com/ansible/awx/releases/tag/21.1.0) is now available!
> 
> We're happy to announce that [AWX Operator version 0.22.0](https://github.com/ansible/awx-operator/releases/tag/0.22.0) is now available!

### DevTools [↗](https://github.com/ansible-community/molecule) ⛏️

Projects to make it easier to write and test Ansible Content. Includes [VScode extension](https://github.com/ansible/vscode-ansible), [language server](https://github.com/ansible/ansible-language-server), [ansible-lint](https://github.com/ansible-community/ansible-lint), [molecule](https://github.com/ansible-community/molecule), [ansible-navigator](https://github.com/ansible/ansible-navigator) and potentially other development goodies. To see what's planned, and how you can help checkout the [foundation-devtools project board](https://github.com/orgs/ansible/projects/86/views/4).

[ssbarnea](https://matrix.to/#/@ssbarnea:matrix.org) said

> [Molecule v4 pre-release](https://github.com/ansible-community/molecule/discussions/3569) is out and it contains more than 20 notable bugfixes and features.

### Antsibull [↗](https://github.com/ansible-community/antsibull) 🐂

Tooling for building the `Ansible` package and collection documentation.

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) contributed

> antsibull 0.46.0 has been released ([changelog](https://github.com/ansible-community/antsibull/blob/main/CHANGELOG.rst#v0-46-0)) with improvements for the release role, release building, and changelog generation.

## COLLECTION UPDATES 🪄

[Qalthos](https://matrix.to/#/@qalthos:ansible.im) contributed

> There have been a few networking releases this week:
> * [ansible.netcommon 3.0.1](https://github.com/ansible-collections/ansible.netcommon/tree/3.0.1) has been released with bugfixes ([changelog](https://github.com/ansible-collections/ansible.netcommon/blob/3.0.1/CHANGELOG.rst))
> * [arista.eos 5.0.1](https://github.com/ansible-collections/arista.eos/tree/5.0.1) has been released with bugfixes ([changelog](https://github.com/ansible-collections/arista.eos/blob/5.0.1/CHANGELOG.rst))
> * [cisco.ios 3.1.0](https://github.com/ansible-collections/cisco.ios/tree/3.1.0) has been released with new features ([changelog](https://github.com/ansible-collections/cisco.ios/blob/3.1.0/CHANGELOG.rst))
> * [vyos.vyos 3.0.1](https://github.com/ansible-collections/vyos.vyos/tree/3.0.1) has been released with bugfixes ([changelog](https://github.com/ansible-collections/vyos.vyos/blob/3.0.1/CHANGELOG.rst))

[andersson007_](https://matrix.to/#/@andersson007_:matrix.org) shared

> The [community.mysql](https://galaxy.ansible.com/community/mysql) collection versions [1.4.7](https://github.com/ansible-collections/community.mysql/blob/stable-1/CHANGELOG.rst), [2.3.8](https://github.com/ansible-collections/community.mysql/blob/stable-2/CHANGELOG.rst) and [3.3.0](https://github.com/ansible-collections/community.mysql/blob/main/CHANGELOG.rst) have been released. Special thanks to [betanummeric](https://github.com/betanummeric), [rsicart](https://github.com/rsicart), [hubiongithub](https://github.com/hubiongithub), [moledzki](https://github.com/moledzki) and our WG leader [bmalynovytch](https://github.com/bmalynovytch)!

[abuzachis](https://matrix.to/#/@aevelina:ansible.im) said

> [amazon.aws 3.3.0](https://github.com/ansible-collections/amazon.aws/tree/3.3.0) has been released with some new features and bugfixes ([see changelog for details](https://github.com/ansible-collections/amazon.aws/blob/3.3.0/CHANGELOG.rst#v3-3-0)).

[jatorcasso](https://matrix.to/#/@jatorcasso:ansible.im) contributed

> [amazon.aws 2.3.0](https://github.com/ansible-collections/amazon.aws/tree/2.3.0) has been released with bug-fixes (see [changelog](https://github.com/ansible-collections/amazon.aws/blob/2.3.0/CHANGELOG.rst) for details).

[markuman](https://matrix.to/#/@markuman:matrix.org) shared

> community.aws [3.3.0](https://github.com/ansible-collections/community.aws/releases/tag/3.3.0) and [2.5.0](https://github.com/ansible-collections/community.aws/releases/tag/2.5.0) have been released.

## PROPOSALS - DISCUSS AND VOTE! 🗳️

[mariolenz](https://matrix.to/#/@mariolenz:matrix.org) said

> There's a new [vote](https://github.com/ansible-community/community-topics/discussions/107) open about adding an `ansible-community` command to show the version of the community package that's installed. This would be independent from how people have installed the community package (pip, rpm, dpkg...). Please vote by **June 7, 2022**!

## THE ANSIBLE TEAM IS HIRING 💰️

[gundalow](https://matrix.to/#/@gundalow:ansible.im) said

> **Principal Software Engineer (Controller)**
> 
> We are looking for a Principal Software Engineer to work on [Controller](https://www.ansible.com/products/controller), which is the downstream of [AWX](https://github.com/ansible/awx). This is the main component of what was previously called Ansible Tower.
> 
> In this role, you’ll be part of the Controller team whose work powers the Red Hat Ansible Automation Platform and enables customers to centralize and control their IT infrastructure with a visual dashboard, role-based access control, and more. As a Principal Software Engineer, you’ll be working with engineers at a variety of experience levels, developing each other’s skills, trusting in each other’s strengths, and supporting one another as you deliver on team commitments. 
> 
> 
> * Write and maintain high quality code as a member of a team, leading best practice usage by example
> * Lead engineers in building implementations of new designs
> * Develop and mature habits in following engineering best practices
> * Work closely with lead architects and product managers to ensure features and fixes meet desired use-cases
> * Write unit and integration tests as well as understand debugging software 
> * Actively participate in code reviews with the team
> * Work with the Quality Engineering (QE) team to ensure that builds are tested correctly
> * Submit patches for bug fixes to the Red Hat Ansible Automation Platform as well as the open source community; review patches from other community members
> * Mentor other engineers; lead them in delivering quality software
> 
> If this sounds like you, please apply via [jobs.redhat.com](https://us-redhat.icims.com/jobs/93825/principal-software-engineer-%28controller%29/job?hub=7).

## THAT'S ALL FOR NOW!

Have any questions you’d like to ask, or issues you’d like to see covered? Please ask in [#social:ansible.com](https://matrix.to/#/#social:ansible.com)! See you next time!
