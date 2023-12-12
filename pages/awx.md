---
slug: awx
title: Ansible AWX
type: text
---
<style>
h2 {
  font-size: 2rem;
  text-transform: none;
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
The AWX project is how Red Hat and Ansible demonstrate their commitment to creating a world-class open-source project on top of the Ansible Tower codebase.

Here are resources to help start using AWX and get involved with the community:

* Check the [frequently asked questions about AWX](#awx-faq) on this page.
* Fork the [AWX GitHub repository](https://github.com/ansible/awx).
* Check out the [AWX operator](https://github.com/ansible/awx-operator/) for Kubernetes.
* Visit the [AWX documentation](https://ansible.readthedocs.io/projects/awx/en/latest/).

You can [get help](https://forum.ansible.com/tags/c/help/6/all/awx) with AWX on the community forum or [join a project discussion](https://forum.ansible.com/tags/c/project/7/awx) and become an active voice in the community.

If you want to ask questions and talk with community experts, you can also visit the [#awx](https://matrix.to/#/#awx:ansible.com) channel on Matrix.

<a name="awx-faq"><a>

# Frequently Asked Questions

Find answers related to the AWX project in the following section.
You can also find lots of information about AWX in the [Ansible community forum](https://forum.ansible.com/tag/awx).

## What is the AWX project?

The AWX project—AWX for short—is an open source community project, sponsored by Red Hat, that enables users to better control their community Ansible project use in IT environments.
AWX is the upstream project from which the automation controller component is derived.

Visit the [Understanding Ansible, AWX, and Ansible Automation Platform](https://www.redhat.com/en/technologies/management/ansible/compare-awx-vs-ansible-automation-platform) to understand the differences between community Ansible and Red Hat Ansible Automation Platform.

## Why is Red Hat doing this?

Open sourcing everything is what Red Hat does.
When Ansible, Inc. was acquired by Red Hat, we told our users that we would open the source code for Ansible.
The AWX project is a fulfillment of that intent.

More importantly, the Ansible team believes deeply in the power of community-driven innovation.
The Ansible project itself has more than 3,000 contributors and we believe this will continue to grow and expand.
Many of the critical features we now provide for users and customers were built almost entirely by the Ansible community.
We believe that the open source model will bring many innovations to the AWX project.

## What is the difference between AWX and Automation Controller?

AWX is designed to be a frequently released, fast-moving project where all new development happens.

Automation Controller is produced by taking selected releases of AWX, hardening them for long-term supportability, and making them available to customers as a hosted service within Red Hat Ansible Automation Platform.
Ansible Automation Platform is fully supported by Red Hat, while AWX is supported by the community.

This is a tested and trusted method of software development for Red Hat, which follows a similar model to Fedora and Red Hat Enterprise Linux.

## Where can I get help for AWX?

You can [get help](https://forum.ansible.com/tags/c/help/6/all/awx) with AWX on the community forum or [join a project discussion](https://forum.ansible.com/tags/c/project/7/awx) and become an active voice in the community.

If you want to ask questions and talk with community experts, you can also visit the [#awx](https://matrix.to/#/#awx:ansible.com) channel on Matrix.

Because AWX is designed to be a rapidly moving project, Red Hat does not provide any paid support for it.
For a fully supported automation management platform, [read more about Red Hat Ansible Automation Platform](https://www.redhat.com/en/technologies/management/ansible).

## Can I upgrade from one version of AWX to another?

AWX is versionless and offers a "latest" release version only.
As such, it is not possible to perform direct, in-place upgrades between AWX versions.

## Under which open source license is AWX available?

The AWX source code is available under the [Apache License 2.0](https://github.com/ansible/awx/blob/devel/LICENSE.md).

## How can I get involved with the AWX project?

Fork or clone the [AWX GitHub repository](https://github.com/ansible/awx).
We welcome and encourage community contributions.
Read the [contributor guide](https://github.com/ansible/awx/blob/devel/CONTRIBUTING.md) to find out more.

## Where do I report an AWX bug?

You can file issues in the [issue tracking section](https://github.com/ansible/awx/issues) of the GitHub repository.

## How often is AWX released?

The AWX team currently plans to release new builds approximately every two weeks.
The AWX team will flag certain builds as "stable" at their discretion.
Note that the term "stable" does not imply fitness for production usage or any kind of warranty whatsoever.

## What is the governance structure of the AWX project?

For now, the AWX team will continue to make all decisions for the AWX project.
Over time, we will evaluate our governance structure, and we will do our best to choose a structure that balances community needs with product needs.

## If my software runs with AWX, can I say that it is certified to run on AWX or on Red Hat Ansible Automation Platform?

No.
Only Red Hat has the ability to say that software is "certified", although you may truthfully use the AWX name to describe the relationship between your software and AWX.
For more details, consult the [AWX trademark guidelines](https://github.com/ansible/awx-logos/blob/master/TRADEMARKS.md).

## I want to build my own forked version of AWX. Can I call it AWX? Can I call it Red Hat Ansible Automation Platform?

No.
You may fork AWX like any open source codebase, but you may not use Red Hat trademarks.
Red Hat reserves the exclusive right to decide what products can bear those marks.

## Will contributions to AWX require a "Contributor License Agreement"?

No.
However, all contributions to AWX will require agreement with the Developer Certificate of Origin (DCO) at the time of submission.
The text of the DCO can be read in full at [developercertificate.org](https://developercertificate.org/).

## Does Red Hat recommend AWX for production environments?

No.
Red Hat Ansible Automation Platform is suitable for production environments.

## Does Red Hat’s Open Source Assurance Program apply to AWX?

No, it does not.
