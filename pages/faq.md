---
slug: faq
title: Frequently asked questions
description: Find answers to some of the frequently asked questions here.
type: text
---
<style>
p {
  margin-bottom:6px;
}
h2 {
  font-size: 2rem;
  text-transform: none;
  padding-top:12px;
}
h3,
h4,
h5,
h6 {
  font-size: 1.125rem;
  font-weight: normal;
  text-transform: uppercase;
}
</style>
Find answers to many frequency asked questions below.  Please share any additional questions with us on the [Ansible forum](https://forum.ansible.com/c/help).

# Core

[Q: What is the difference between Ansible Core and AWX?](#1)

# AWX

[Q: What is The AWX Project?](#2)

[Q: Why is Red Hat doing this?](#3)

[Q: What’s the difference between AWX and automation controller?](#4)

[Q: Where can I find support for AWX?](#5)

[Q: Can I upgrade from one version of AWX to another?](#6)

[Q: Under which open source license is AWX available?](#7)

[Q: How can I get involved with the AWX Project?](#8)

[Q: Where do I report an AWX bug?](#9)

[Q: How often is AWX released?](#10)

[Q: What is the governance structure of the AWX project?](#11)

[Q: If my software runs with AWX, can I say that it is certified to run on AWX or on Red Hat Ansible Automation Platform?](#12)

[Q: I want to build my own forked version of AWX. Can I call it AWX? Can I call it Red Hat Ansible Automation Platform?](#13)

[Q: Will contributions to AWX require a “Contributor License Agreement”?](#14)

[Q: Does Red Hat recommend AWX for production environments?](#15)

[Q: Does Red Hat’s Open Source Assurance Program apply to AWX?](#16)

# Ansible Collaborative

[Q: How can I contribute back to the user ecosystem?](#17)

---

# Core

<a name="1"/>

**What is the difference between Ansible Core and AWX?**

Ansible Core is the command-line (CLI) tool that is installed from either community repositories or the official Red Hat repositories for Ansible.

ansible-core is the successor to the "batteries included" ansible CLI package prior to Ansible 2.10, minus most of the modules that were split into collections.

AWX provides a web-based user interface, REST API, and task engine built on top of Ansible.
It's the upstream of automation controller (formerly Ansible Tower).
Both are upstream projects for Red Hat Ansible Automation Platform.

---

# AWX

<a name="2"/>

**What is The AWX Project?**

The AWX project—AWX for short—is an open source community project, sponsored by Red Hat®, that enables users to better control their community Ansible project use in IT environments.
AWX is the upstream project from which the automation controller (formerly Ansible Tower) component in Red Hat Ansible Automation Platform is ultimately derived.

<a name="3"/>

**Why is Red Hat doing this?**

Open sourcing everything is what Red Hat does.
When Ansible®, Inc. was acquired by Red Hat, we told our users that we would open the source code for Ansible.
The AWX project is a fulfillment of that intent.

More importantly, the Ansible team—like all of Red Hat—believes deeply in the power of community-driven innovation.
The Ansible project itself has more than 5,000 contributors, and we believe this will continue to grow and expand.
Many of the critical features we now provide for users and customers were built almost entirely by the Ansible community.
We believe that the open source model has brought many innovations to the AWX Project.

[Learn more about Red Hat Ansible Automation Platform, the subscription-based, supported enterprise product](https://www.redhat.com/en/technologies/management/ansible)

<a name="4"/>

**What’s the difference between AWX and automation controller?**

AWX is designed to be a frequently released, fast-moving project where all new development happens.

Automation controller is produced by taking selected releases of AWX, hardening them for long-term supportability, and making them available to customers as a hosted service within Red Hat Ansible Automation Platform.
Ansible Automation Platform is fully supported by Red Hat, while AWX is supported by the community.

This is a tested and trusted method of software development for Red Hat, which follows a similar model to Fedora and Red Hat Enterprise Linux®.

[Learn more about the differences between AWX and Red Hat Ansible Automation Platform](https://www.redhat.com/en/technologies/management/ansible/compare-awx-vs-ansible-automation-platform)

<a name="5"/>

**Where can I find support for AWX?**

The community can help answer questions about AWX via the [Ansible Community Forum](https://forum.ansible.com) and Matrix.
You can also file bug reports or contribute bug fixes in the [AWX GitHub repository](https://github.com/ansible/awx).

Because AWX is designed to be a rapidly moving project, Red Hat does not provide any paid support for it.
For a fully supported automation management platform, read more about [Red Hat Ansible Automation Platform](https://www.redhat.com/en/technologies/management/ansible).

<a name="6"/>

**Can I upgrade from one version of AWX to another?**

Upgrading of AWX is only available for the awx-operator (Kubernetes) based install.
For upgrading awx-operator from version 0.18 or above, [follow the instructions in this document](https://github.com/ansible/awx-operator/blob/devel/docs/upgrade/upgrading.md).
Direct, in-place [upgrades between prior AWX versions are not supported](https://github.com/ansible/awx/blob/devel/DATA_MIGRATION.md).

<a name="7"/>

**Under which open source license is AWX available?**

The AWX source code is available under the Apache License 2.0.

<a name="8"/>

**How can I get involved with the AWX Project?**

The AWX Project is [hosted on GitHub](https://github.com/ansible/awx). We welcome community contributions.
Read the [contributor guide](https://github.com/ansible/awx/blob/devel/CONTRIBUTING.md).
Join the [Ansible Community Forum](https://forum.ansible.com).

<a name="9"/>

**Where do I report an AWX bug?**

The AWX project uses GitHub for its issue tracking. You can file your issues [on this page](https://github.com/ansible/awx/issues).

<a name="10"/>

**How often is AWX released?**

The AWX team currently plans to release new builds approximately every 2 weeks.
The AWX team will flag certain builds as “stable” at their discretion. Note that the term “stable” does not imply fitness for production usage or any kind of warranty.

<a name="11"/>

**What is the governance structure of the AWX project?**

For now, the Red Hat sponsored AWX team will continue to make the majority of decisions for the AWX project, with input from the community.
Over time, the team will evaluate its governance structure and choose a structure that balances community needs with product needs.

<a name="12"/>

**If my software runs with AWX, can I say that it is certified to run on AWX or on Red Hat Ansible Automation Platform?**

No. Only Red Hat has the ability to say that software is “certified,” although you may truthfully use the AWX name to describe the relationship between your software and AWX.
For more details, consult the [AWX trademark guidelines](https://github.com/ansible/awx-logos/blob/master/TRADEMARKS.md).

<a name="13"/>

**I want to build my own forked version of AWX. Can I call it AWX? Can I call it Red Hat Ansible Automation Platform?**

No.
You may fork AWX like any open source codebase, but you may not use Red Hat trademarks.
Red Hat reserves the exclusive right to decide what products can bear those marks.
Be sure to read the [AWX trademark guidelines](https://github.com/ansible/awx-logos/blob/master/TRADEMARKS.md) for more information.

<a name="14"/>

**Will contributions to AWX require a “Contributor License Agreement”?**

No.
However, all contributions to AWX will require agreement with the Developer Certificate of Origin (DCO) at the time of submission.
The text of the DCO can be read in full at [developercertificate.org](http://developercertificate.org/).

<a name="15"/>

**Does Red Hat recommend AWX for production environments?**

No.

<a name="16"/>

**Does Red Hat’s Open Source Assurance Program apply to AWX?**

No.

---

# Ansible Community

<a name="17"/>

**How can I contribute back to the user ecosystem?**

We are pleased to shared there are so many ways to contribute to the Ansible ecosystem.
Here are just a few examples:

* Organize meetups with other automation enthusiasts
* Present at conferences about Ansible
* Host Ansible workshops
* Share content on Galaxy
* Code a new module or collection
* Report or fix a bug
* Improve the documentation

Want to get involved?
Check out our [contributor resources](https://forum.ansible.com/pub/how-to-contribute) or chat with [other users](https://matrix.to/#/#social:ansible.com) - we'd love to have you.
