---
title: "Bullhorn #81"
date: 2022-11-12 06:45 UTC
tags: news
category: bullhorn
type: text
---

![Ansible Bullhorn banner](/images/bullhorn-banner-mango.png)

*A Newsletter for the Ansible Developer Community*
*Issue #81, 2022-11-11 ([Past Issues](https://us19.campaign-archive.com/home/?u=56d874e027110e35dea0e03c1&id=d6635f5420))*

Welcome to [The Bullhorn](https://github.com/ansible/community/wiki/News#the-bullhorn), our newsletter for the Ansible developer community. If you have any questions or content you’d like to share, you're welcome to chat with us in the [Ansible Social room on Matrix](https://matrix.to/#/#social:ansible.com), and mention [`newsbot`](https://matrix.to/#/@newsbot:ansible.im) to have your news item tagged for review for the next weekly issue!

<!-- TEASER_END -->

## KEY DATES ⏱️

[cybette](https://matrix.to/#/@cybette:ansible.im) shared

> * 2022-11-15: [Ansible 7.0.0 rc1 (weekly release candidates as needed; test and alert us to any blocker bugs)](https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_7.html)
> * 2022-11-15: [DaWGs meeting](https://github.com/ansible/community/issues/643), 16:00 UTC
> * 2022-11-16: [Community WG meeting](https://github.com/ansible/community/issues/645), 19:00 UTC (propose topics [here](https://github.com/ansible-community/community-topics/issues))
> * 2022-11-17: [Bullhorn #82 content deadline](https://github.com/ansible/community/wiki/News#the-bullhorn), 18:00 UTC
> * 2022-12-05: ETA for Ansible-Core 2.14.1 and 2.13.7 releases

## GENERAL NEWS UPDATES 🔈️

[andersson007_](https://matrix.to/#/@andersson007_:matrix.org) shared

> New Matrix rooms:
> * [#postgresql:ansible.com](https://matrix.to/#/#postgresql:ansible.com): PostgreSQL Ansible automation
> * [#mysql:ansible.com](https://matrix.to/#/#mysql:ansible.com): MySQL/MariaDB Ansible automation
> * [#storage:ansible.com](https://matrix.to/#/#storage:ansible.com): External storage-related modules/plugins

[relrod](https://matrix.to/#/@relrod:matrix.org) contributed

> **Ansible AWX** has had its first Community Office Hours meeting this week. We had 8 community members join us and an hour of excellent discussion with you, the community! We will be posting updates here in The Bullhorn and on [Matrix](https://matrix.to/#/#awx:ansible.com) with future meeting dates. We'd love to hear from you and work with you to make [AWX](https://github.com/ansible/awx) as useful as possible! Your voice matters and is critical to the continued success of AWX! We appreciate you ❤️

## MAJOR NEW RELEASES 🏆️

### Ansible-Core [↗](https://github.com/ansible/ansible) ⚡️

The `ansible-core` package contains the base engine and a small subset of modules and plugins. To see what's planned for the next release, look at the [`ansible-core` roadmaps](https://docs.ansible.com/ansible-core/devel/roadmap/ansible_core_roadmap_index.html).

[cybette](https://matrix.to/#/@cybette:ansible.im) said

> [ansible-core 2.14.0](https://groups.google.com/g/ansible-devel/c/G5TB9zNKNDk) has been released. This is a major release with the following important changes:
> * Implement sidecar docs to support documenting filter/test plugins, as well as non Python modules
> * Proxy Display over queue from forks
> * Move handler processing into new PlayIterator phase to use the configured strategy
> * Convert FieldAttribute to data descriptors to avoid complex meta classes
> * Drop Python 3.8 support for controller
> * Enforce running controller code with the Python locale and filesystem encoding set to UTF-8
> * Ensure stdin/stdout/stderr file handles are using blocking IO
> * Evaluate variables lazily to allow defined tests to properly detect when dependent variables are undefined

[cybette](https://matrix.to/#/@cybette:ansible.im) contributed

> [ansible-core 2.13.6](https://groups.google.com/g/ansible-devel/c/uDceTGqyXeE) has been relased. This is a maintenance release containing numerous bugfixes.

### Ansible [↗](https://github.com/ansible-collections) 📦️

The `Ansible` package includes `ansible-core` and is a batteries-included package that provides a curated set of Ansible collections. See the [Ansible roadmaps](https://docs.ansible.com/ansible/devel/roadmap/ansible_roadmap_index.html) for future release plans.

[chadams](https://matrix.to/#/@chadams:ansible.im) said

> Ansible 6.6.0 is out! ❤️
> 🔗[https://groups.google.com/g/ansible-announce/c/GXZX8Yzc_F0](https://groups.google.com/g/ansible-announce/c/GXZX8Yzc_F0)
> 💽You can install it by running the following command or download the release tarball directly from [pypi](https://pypi.python.org/packages/source/a/ansible/ansible-6.6.0.tar.gz):
> 
> ```
> pip install ansible==6.6.0 --user
> ```
> 
> 🔆Try the `ansible-community` command-line utility added in Ansible 6 that prints the version of the Ansible Community package:
> 
> ```
> $ ansible-community --version
> Ansible community version 6.6.0
> ```
> 
> ➡️ Check [Release Notes📦️🗒️](https://github.com/ansible-community/ansible-build-data/blob/main/6/CHANGELOG-v6.rst) and [Ansible 6 Porting Guide](https://docs.ansible.com/ansible/devel/porting_guides/porting_guide_6.html) for more details!

## PROJECT UPDATES 🛠️

### AWX Project [↗](https://github.com/ansible/awx)

AWX provides a web-based user interface, REST API, and task engine built on top of Ansible.

[relrod](https://matrix.to/#/@relrod:matrix.org) contributed

> Do you like logs? _I_ like logs. They make life so much easier! Did you know that AWX lets you configure where its logs are sent? You can configure an external logging aggregation server within AWX's administration settings. A current goal for AWX is to work toward improving the Kubernetes deployment, making it possible to independently scale the task and web parts of the system (which currently live in the same pod).
> 
> One of the coupled pieces currently is the logging infrastructure, which makes use of rsyslog and lives in the web container currently. Surprisingly, though, for historical reasons, it is controlled and restarted from the task container using a shared supervisord control socket, when configuration changes. We need to change that to work toward the web/task separation goal. We have come up with a [proposal](https://github.com/ansible/awx/issues/13183) and possible plan to decouple rsyslog, which will allow for easier scaling of all parts of the system. We don't expect any end-user-facing changes as part of this proposal, but we would love thoughts/questions/comments/feedback from the community about the proposal!
> 
> Stop by in the [#awx:ansible.com](https://matrix.to/#/#awx:ansible.com) Matrix room and let us know how you use AWX's logging or any bottlenecks you've run into! We also have much more work to do toward this larger goal. We'll be posting more updates, but until then please reach out on Matrix if you wish to get involved or follow this work!

[relrod](https://matrix.to/#/@relrod:matrix.org) shared

> `awxkit`, the library backing the `awx` Command Line Interface to Ansible AWX, has been [fixed](https://github.com/ansible/awx/pull/13174) to support Python 3.11's argparse. This fix will go out in the next upstream AWX release. Using the latest and greatest Python? Give it a try and let us know how it works in the [#awx:ansible.com](https://matrix.to/#/#awx:ansible.com) matrix channel!

## COLLECTION UPDATES 🪄

[Simon Dodsley](https://matrix.to/#/@sdodsley:matrix.org) shared

> purestorage.flasharray 1.15.0 ([changelog](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/releases/tag/1.15.0)) has been released.

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) contributed

> community.general 3.8.10 ([changelog](https://github.com/ansible-collections/community.general/blob/stable-3/CHANGELOG.rst#v3-8-10)) and 4.8.9 ([changelog](https://github.com/ansible-collections/community.general/blob/stable-4/CHANGELOG.rst#v4-8-9)) have been released. The 3.x.y release stream is now End of Life and will not receive any new releases. The 4.x.y release stream is only updated for major bugfixes and security fixes, and will be End of Life in roughtly half a year once community.general 7.0.0 is released.

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) shared

> community.dns 2.4.0 ([changelog](https://github.com/ansible-collections/community.dns/blob/main/CHANGELOG.rst#v2-4-0)) has been released. It now supports module default groups for the Hetzner DNS and Hosttech DNS modules, fixes check mode for `community.dns.wait_for_txt`, updates the Public Suffix List, and improves the documenation by using attributes.

[briantist](https://matrix.to/#/@briantist:libera.chat) said

> [`community.hashi_vault` version `4.0.0`](https://github.com/ansible-collections/community.hashi_vault/releases/tag/4.0.0) has been released, with previously announced breaking changes to some default values, and improvements to module documentation with attributes that describe the use of action groups and check mode support.

[andersson007_](https://matrix.to/#/@andersson007_:matrix.org) contributed

> The [community.network](https://galaxy.ansible.com/community/network) collection versions 3.3.1 (Final `EOL` release, [changelog](https://github.com/ansible-collections/community.network/blob/stable-3/CHANGELOG.rst)) and 4.0.2 ([changelog](https://github.com/ansible-collections/community.network/blob/stable-4/CHANGELOG.rst)) have been released!

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) said

> community.general 6.0.0 ([changelog](https://github.com/ansible-collections/community.general/blob/stable-6/CHANGELOG.rst)) has been released! Besides a lot of new features and bugfixes, new modules and plugins, some deprecations and breaking changes, a major change to 5.x.y is that the plugins/modules/ directory tree structure has been removed. Please check out the changelog for more details!

[felixfontein](https://matrix.to/#/@felixfontein:libera.chat) contributed

> community.hrobot 1.6.0 ([changelog](https://github.com/ansible-collections/community.hrobot/blob/main/CHANGELOG.rst#v1-6-0)) has been released. It now supports a module defaults group `community.hrobot.robot`, and improves the documenation by using attributes.

## HELP WANTED 🙏

[andersson007_](https://matrix.to/#/@andersson007_:matrix.org) said

> The following collection inclusion requests are waiting for your review:
> 
> * [dellemc.unity](https://github.com/ansible-collections/ansible-inclusion/discussions/32)
> 
> See the [process description](https://github.com/ansible-collections/ansible-inclusion#review-process) to learn how to do it.
> 
> If you have any questions, just ping `andersson007` on [Matrix](https://docs.ansible.com/ansible/devel/community/communication.html#ansible-community-on-matrix) in the [#community:ansible.com](https://matrix.to/#/#community:ansible.com) room or on [Libera.Chat IRC](https://docs.ansible.com/ansible/devel/community/communication.html#ansible-community-on-irc) in the `#ansible-community` channel or directly.
> 
> Please help the community extend the Ansible package!

## COMMUNITY UPDATES 👂️

[cybette](https://matrix.to/#/@cybette:ansible.im) contributed

> ### Ansible Contributor Survey
> 
> Feedback is really important to us so we can keep on improving the Contributor Experience for our wonderful Ansible Community. Please take a few minutes to fill in the [Contributor Survey](https://www.surveymonkey.co.uk/r/7PK28F8) that we have put together!

## NEW TEAM MEMBERS ✨ 

[Don Naro](https://matrix.to/#/@orandon:ansible.im) shared

> Hello everyone! My name is Don Naro and I'm delighted to be joining the Ansible community engineering team!! I actually joined the team on October 1 so this is somewhat overdue. What can I say? Things are busy at Ansible! I'm excited to be here and feel it's an honour and a privilege to support the Ansible community. I've got a background as a content developer working with dev/ops teams and am quite passionate about open-source, collaborative workflows, and the value of community.
> 
> On the personal side I live in Galway, Ireland with my wife and our two kids. We're cat lovers and enjoy spending time in our garden, playing board games, and exploring nearby beaches.
> 
> Feel free to say hi to me on Matrix [@orandon:ansible.im](https://matrix.to/#/@orandon:ansible.im) or reach out if you think I can help with anything. Cheers!

[anwesha](https://matrix.to/#/@anwesha:ansible.im) said

> Hello everyone, Anwesha is on this side. A Master of Laws by education and a technologist by passion. Over the years, I have helped open-source communities around the globe with legal, technical and organizational skills. In my previous day jobs, I worked as a Cloud Engineer and as a System Administrator. I am an organizer at PyLadies Stockholm, a board member at Python Sweden, and a Python Software Foundation fellow. I maintain my blog at https://anweshadas.in. And I am the new joinee on the Ansible Community team. Though I am new to the team, I have been an Ansible user for years. I am thrilled to be a part of this fantastic community. You can find me on Matrix [@anwesha:ansible.im](https://matrix.to/#/@anwesha:ansible.im) and in good old IRC, where my nick is anwesha. 
> 
> In the coming days, I want to be a part of the community and grow together. Hopefully, in the coming months, from a name, I will be a person and friend to you all :).

## COMMUNITY EVENTS AND MEETUPS 📅

[cybette](https://matrix.to/#/@cybette:ansible.im) contributed

> [Ansible Zürich](https://www.meetup.com/ansible-zurich/) is planning their [11th Ansible Meetup](https://www.meetup.com/ansible-zurich/events/288952760/) for November 29 (Tuesday) and looking for your contributions! Check out the [details and RSVP](https://www.meetup.com/ansible-zurich/events/288952760/).

## THE ANSIBLE TEAM IS HIRING 💰️

[cybette](https://matrix.to/#/@cybette:ansible.im) shared

> We are looking for a **Senior Technical Marketing Manager** to oversee and develop technical messaging and content for the Ansible Community. You will be an integral part of the Ansible Technical Marketing and Community teams, working closely with Engineering as well as the Community. This role can be 100% remote for someone residing in a country where Red Hat is registered to do business. Check out the details [here](https://us-redhat.icims.com/jobs/92824/senior-technical-marketing-manager---ansible-community-projects/job?hub=7) and apply!

## THAT'S ALL FOR NOW!

Have any questions you’d like to ask, or issues you’d like to see covered? Please ask in [#social:ansible.com](https://matrix.to/#/#social:ansible.com)! See you next time!
