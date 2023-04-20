---
title: "Bullhorn #43"
date: 2022-01-28 11:00 UTC
tags: news
category: bullhorn
type: text
---

![Ansible Bullhorn banner](/images/bullhorn-banner-mango.png)

*A Newsletter for the Ansible Developer Community*
*Issue #43, 2022-01-28 ([Past Issues](https://us19.campaign-archive.com/home/?u=56d874e027110e35dea0e03c1&id=d6635f5420))*

Welcome to the Bullhorn, our newsletter for the Ansible developer community. If you have any questions or content you’d like to share, please reach out to us at the-bullhorn@redhat.com, or chat with us in the [Ansible Social room on Matrix](https://matrix.to/#/#social:ansible.com).

<!-- TEASER_END -->

## KEY DATES

[cybette](https://matrix.to/#/@cybette:ansible.im) contributed

> * 2022-01-28/29: [DevConf.CZ 2022](https://devconf.cz/) featuring a number of [Ansible sessions](https://devconfcz2022.sched.com/?searchstring=ansible)
> * 2022-01-31: ETA for Ansible-Core 2.12.2, Ansible-Core 2.11.8, and Ansible-Base 2.10.17 releases
> * 2022-02-01: [ETA for Ansible 5.3.0 release](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_5.html)
> * 2022-02-01: [DaWGs meeting](https://github.com/ansible/community/issues/643), 16:00 UTC
> * 2022-02-02: [Community WG meeting](https://github.com/ansible/community/issues/645), 18:00 UTC (propose topics [here](https://github.com/ansible-community/community-topics/issues))
> * 2022-02-03: [Bullhorn #44 content deadline](https://github.com/ansible/community/wiki/News#the-bullhorn)
> * 2022-02-05/06: [FOSDEM 2022](https://fosdem.org/2022/search/?q=ansible)
> * 2022-02-08: [DaWGs meeting](https://github.com/ansible/community/issues/643), 16:00 UTC
> * 2022-02-09: [Community WG meeting](https://github.com/ansible/community/issues/645), 18:00 UTC (propose topics [here](https://github.com/ansible-community/community-topics/issues))

## GENERAL NEWS UPDATES

[andersson007_](https://matrix.to/#/@andersson007_:matrix.org) contributed

> Dear collection maintainers,
> 
> This is important for your collections!
> 
> * In accordance with the [Community decision](https://github.com/ansible-community/community-topics/issues/51), we have created the [news-for-maintainers](https://github.com/ansible-collections/news-for-maintainers) repository for announcements of changes impacting collection maintainers (see the [examples](https://github.com/ansible-collections/news-for-maintainers#examples-of-news-posted-via-this-repository)) instead of [Issue 45](https://github.com/ansible-collections/overview/issues/45) that has just been closed.
>   - To keep yourself well-informed and, therefore, things in your collection working, please subscribe to the [repository](https://github.com/ansible-collections/news-for-maintainers) by using the `Watch` button in the upper right corner on the repository's home page.
>   - If you do not want to get notifications about related discussions, please subscribe only to `Issues`.
>   - Please read the brief [guidelines](https://github.com/ansible-collections/news-for-maintainers#guidelines) on how the repository should be used.
>   - Please avoid unnecessary discussions in issues, use the [Discussions](https://github.com/ansible-collections/news-for-maintainers/discussions) feature. Every comment posted will notify **a lot** of folks!
>   
> Thank you!

## COLLECTION UPDATES

[andersson007_](https://matrix.to/#/@andersson007_:matrix.org) shared

> [community.postgresql](https://github.com/ansible-collections/community.postgresql/blob/1.6.1/CHANGELOG.rst#v161) 1.6.1 has been released. Among other improvements, the `postgresql_info` module now works with AWS RDS PostgreSQL instances, thanks to [marcosdiez](https://github.com/marcosdiez)!

[andersson007_](https://matrix.to/#/@andersson007_:matrix.org) said

> [community.mysql](https://github.com/ansible-collections/community.mysql) 3.1.0, 2.3.3, and 1.4.4 have been released.

[markuman](https://matrix.to/#/@markuman:libera.chat) shared

> community.aws 3.0.1 has just been released.

[mariolenz](https://matrix.to/#/@mariolenz:matrix.org) shared

> [community.vmware 2.0.0](https://github.com/ansible-collections/community.vmware/blob/main/CHANGELOG.rst#v2-0-0) has been released. Note that this is a new major version, [meaning](https://semver.org/) backwards incompatible changes like breaking changes and removed features.

## PROPOSALS - DISCUSS AND VOTE!

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) contributed

> The proposal on semantic markup in plugin/module DOCUMENTATION has been updated to allow to more easily reference plugins in the `seealso:` section. See [this message](https://github.com/ansible-community/community-topics/issues/53#issuecomment-1015714024) for details.

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) shared

> The vote on whether to use FQCN for ansible.builtin modules (https://github.com/ansible-community/community-topics/issues/58) is completed. The proposal has been accepted with a broad majority both in the steering committee and in the community.

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) shared

> There is a new active vote on simplifying the collection inclusion procedure for adding new collections to the Ansible community package: https://github.com/ansible-community/community-topics/issues/63 The vote is active until 2022-02-02.

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) contributed

> The voting on the [proposed roadmap for Ansible 6](https://github.com/ansible/ansible/pull/76772) has concluded on 2022-01-26. You can see the discussions and result in [this issue](https://github.com/ansible-community/community-topics/issues/56).

[samccann](https://matrix.to/#/@smccann:matrix.org) contributed

> We're looking for feedback on how to write better changelogs so our porting guides give better information to users. Please comment at https://github.com/ansible-community/community-topics/issues/64 with your ideas.

[gundalow](https://matrix.to/#/@gundalow:ansible.im) shared

> *Changelogs* are an important way to let users know about new features, and more importantly potentially backwards incompatible changes which might require you to update how you use a certain Collection. Based on feedback, we've realised that these aren't always written consistently. We are looking for your feedback (especially from end users and maintainers) on how we can give a better experience. We'd love your thoughts via [community-topics#64](https://github.com/ansible-community/community-topics/issues/64).

[samccann](https://matrix.to/#/@smccann:matrix.org) contributed

> We're working on better community and contributor guidlines for Ansible. Please comment at https://github.com/ansible-community/community-topics/issues/60 with your ideas!

### Ansible-Core [↗](https://github.com/ansible/ansible)

The `ansible-core` package contains the base engine and a small subset of modules and plugins. To see what's planned for the next release, look at the [`ansible-core` roadmaps](https://docs.ansible.com/ansible-core/devel/roadmap/ansible_core_roadmap_index.html).

[gundalow](https://matrix.to/#/@gundalow:ansible.im) said

> `ansible-galaxy` is currently being updated to allow collection verification using gpg, this will be released in [ansible-core 2.13](https://docs.ansible.com/ansible-core/devel/roadmap/ROADMAP_2_13.html). 
> This will allow verifying the authenticity of `MANIFEST.json` before installing and manually at any time.
> 
> The Galaxy server will be queried for signatures and a list of supplemental URLs can be provided in the requirements file:
> ```
> collections:
>   - name: ns.coll
>     signatures:
>       - https://.../test.asc
>       - file:///.../test.asc
> 
> ```
> You can check out the progress and let us know if the proposal works for your use case. We'd love your feedback via [ansible#76681](https://github.com/ansible/ansible/pull/76681).

## COMMUNITY UPDATES

[csmart](https://matrix.to/#/@csmart:matrix.org) said

> In case it's useful, a blog post on how I'm currently setting up my Ansible dev environment https://blog.christophersmart.com/2021/12/27/setting-up-an-ansible-dev-environment/

## COMMUNITY EVENTS AND MEETUPS

[cybette](https://matrix.to/#/@cybette:ansible.im) said

> [DevConf.cz 2022](https://devconf.cz/) is happening right now (Jan 28-29), and you can find a list of Ansible related talks [here](https://devconfcz2022.sched.com/?searchstring=ansible). Sessions of note include [Ansible Community Meetup](https://sched.co/siJx) Jan 28 @ 16:00 UTC, and [What’s New & Ahead in the Ansible Community](https://sched.co/siJE) Jan 29 @ 15:30 UTC.

[cybette](https://matrix.to/#/@cybette:ansible.im) shared

> There's an "Ansible Anwendertreffen" (Ansible user meeting) which will be held on Feb 15, 2022. This is a virtual event conducted in German. If you are interested, you can find the details and registration info [here](https://www.ansible-anwender.de/post/2022/01/register/). The [CFP](https://www.ansible-anwender.de/cfp) is still available until Jan 31, so act fast if you'd like to present at this event!

## THAT'S ALL FOR NOW!

Have any questions you’d like to ask, or issues you’d like to see covered? Please ask in [#social:ansible.com](https://matrix.to/#/#social:ansible.com)! See you next time!
