---
title: New Ansible Galaxy
author: John Hardy
date: 2023-09-26 13:00:00
slug: new-ansible-galaxy
category: galaxy
tags: galaxy
type: text
---
# New Ansible Galaxy

For awhile, the Red Hat Ansible team behind the components Ansible automation hub and Ansible cloud automation hub at console.redhat.com have been on a special ops mission to enhance the [galaxy_ng](https://github.com/ansible/galaxy_ng/) code base that serves the aforementioned components to also serve galaxy.ansible.com, with the intention of replacing galaxy.ansible.com with a fresh code base.

 

## Galaxy, a legacy far far away…
The current Galaxy service has been running at galaxy.ansible.com for many years and is hugely successful in the community. It drives and nurtures Ansible adoption by sharing prebuilt Ansible content that solves many automation challenges. 

One of the statistics we are most proud of are the contributions of 33,965 individual automation answers by the community in either Ansible Content Collections or Ansible Roles. Some of the top ranking automation content includes AWS, VMware, Linux, and Windows. Community users are able to download content for free, self-supported and interact with authors via GitHub for any further help or enhancements. 

* We are excited to announce that the [galaxy.ansible.com](https://github.com/ansible/galaxy_ng/) code base is being updated with a host of exciting new features that the Ansible community can look forward to. Brought to you by the Red Hat Ansible team behind Ansible Automation Hub and Ansible Cloud Automation Hub on console.redhat.com, this new version will enhance the galaxy_ng code base that also serves the above listed components.
As galaxy.ansible.com ages, the frameworks it sits on requires consistent maintenance for security vulnerabilities, including frequent patching. The team is committed to keeping Galaxy secure and high-functioning, so we set out to enable Galaxy with an automation hub, otherwise known as the [galaxy_ng](https://github.com/ansible/galaxy_ng/) codebase.

 

## New Generation
The [galaxy_ng](https://github.com/ansible/galaxy_ng/) code base was always started with the intent to replace the original Galaxy at some point, and also serve as the same code base for the Ansible automation hub component found in Red Hat Ansible Automation Platform. Clearly maintaining one code base for more than one presentation has engineering and architecture benefits for Red Hat and the community, but also the community benefits from more QE, more usage of the code base and adoption of the various uses by organizations. This is a win for everyone. 

It's been a long road to get here. We have had to continue with the progression of an automation hub at the same time as delivering community-only features into the code base, likesocial authentication for GitHub being required in Galaxy but not in the automation hub. 

We are now at the point where we should make the switch and start the new journey on the [galaxy_ng](https://github.com/ansible/galaxy_ng/) code base, together. 

 

## The Switch
The new galaxy service has been running since the beginning of the year on a URL known as beta-galaxy.ansible.com. This URL has hosted many community members and some institutions, who have helped interact with us on the service. The old galaxy.ansible.com service has been running as per usual; we have a sync between the two to make sure the beta-galaxy.ansible.com site is up to date.

We already have a URL called old-galaxy.ansible.com pointing to a read-only version of the galaxy.ansible.com service as it is today.

On September 30, we will switch the IP records used by galaxy.ansible.com to use the records that beta-galaxy.ansible.com uses. 

* Summary: https://old-galaxy.ansible.com/ will point to old Galaxy
* https://galaxy.ansible.com/ will point to new [galaxy_ng](https://github.com/ansible/galaxy_ng/)
* https://beta-galaxy.ansible.com/ will point to new [galaxy_ng](https://github.com/ansible/galaxy_ng/)

This means if the switch is not successful, we can easily switch back or ask the community to try the older service. But we have tested a lot, so everything should go to plan.

 

## After the Switch
@rochacbruno has written up this awesome [table](https://github.com/ansible/galaxy_ng/discussions/1729) to show what was in Galaxy vs the new beta Galaxy site. You will notice not everything has been reimplemented into [galaxy_ng](https://github.com/ansible/galaxy_ng/) due to time constraints, but we are open to discussions on [forum.ansible.com](https://forum.ansible.com) if something should come back, and more importantly, we wish for the community to help design new features to be introduced. 

A good example of features that have not yet been reformulated is the current scoring system. We are retaining the old scores, so nobody loses out on the kudos they have earned already, however, we feel that a new scoring system needs to be implemented,and we’d love to begin soliciting community contributions for how we can improve it. 

| Feature                 | Galaxy  | Beta Galaxy | Reason    |
|-------------------------|-------- |-------------|-----------|
| Sign in/up via GitHub   | ✔️     | ✔️         |           |
| API Key                 | ✔️     | ✔️         |           |
| E-mail/App Notifications | ✔️     | ❌          | Low usage |
| Following authors and content | ✔️ | ❌        | Low usage  |
| Multiple e-mail address per account | ✔️ | ❌ | Low usage |
| Search with filters |✔️ | ✔️ | Improved on Beta |
| Download Count | ✔️ | ✔️ |  |
| Popular Tags | ✔️ | TBD | |
| Platform mark | ✔️ | ❌ | Feature replaced by tags |
| Content Score | ✔️ | TBD | Read only data will be kept, <br> scoring system will be redesigned |
| Content list and search | ✔️ | ✔️ | Improved on beta |
| Content docs | ✔️ | ✔️ | Improved on beta |
| Upload new collections| ✔️ | ✔️ | Improved on beta |
| Import logs | ✔️ | ✔️ | Improved on beta |
| List my namespaces | ✔️ | ✔️ | Simplified on beta |
| Admin namespace access for contributors | ✔️ |✔️ | Simplified on beta |
| Add multiple provider namespaces for collections | ✔️ | ❌ | Was not being used |
| UI to Import Role from Github | ✔️ | ❌ | Recommendation is to publish collections instead, <br> existing roles can still be maintainer via CLI |
| Task Management | ❌ | ✔️ | User can watch tasks spawned,<br> useful for watching status of CLI imports |
|

## The Future
With the new service running on [galaxy_ng](https://github.com/ansible/galaxy_ng/), we have a lot of new capabilities we can look to introduce going forward. Here are some to think about.

Zero downtime for Galaxy service with A-B deployments
Execution environment image hosting, serving.
Execution environment image introspection.
Improved NetFlix style dashboards for content.
Image building from content
Notification integrations 
Global searches
The single code base means we can be more agile, more responsive and more receptive to the community around the Galaxy service. We hope you'll enjoy it.

 

Call to Action
Saturday September 30th 2023 is the switch over date.

If you wish to participate in future enhancements by way of discussions or pull requests, you can find galaxy_ng [here](https://github.com/ansible/galaxy_ng/). We warmly invite all contributors to provide their valuable feedback on [forum.ansible.com](https://forum.ansible.com), utilizing the galaxy tag.

If you are having issues with the new Ansible Galaxy, please check out this forum topic for known issues, links for fixes, where to track updates, how to ask for help, and more.

 