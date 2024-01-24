---
author: The Ansible Community Team
date: 2021-02-18 00:00 UTC
description: Answering the most common questions we have received about the Ansible 3.0.0 release.
lang: en-us
title: Ansible 3.0.0 Q&A
---

# Ansible 3.0.0 Q&A

The Ansible community team has
[announced the release of Ansible 3.0.0](https://www.ansible.com/blog/announcing-the-community-ansible-3.0.0-package)
and here are the questions about the release that we've heard from
community members so far. If you have a question that is not answered
below, let us know on the [mailing lists or IRC](https://www.ansible.com/community).

**How can I stay up to date with changes in the Ansible community?**

Subscribe to the [ansible-announce mailing list](https://groups.google.com/forum/#!forum/ansible-announce)
for release announcements and to the [Bullhorn newsletter](https://us19.campaign-archive.com/home/?u=56d874e027110e35dea0e03c1&id=d6635f5420)
for community news. The Bullhorn is distributed every two weeks with key dates and updates. You may also consider
[registering for the Ansible contributor summit](https://www.eventbrite.com/e/ansible-contributor-summit-202103-registration-141735886853)
on March 9, 2021.

## About the Ansible community package and ansible-base/ansible-core

**Are there any changes to the Ansible language in 3.0.0?**

There are no significant changes since the Ansible 3.0.0 package depends on the same version of ansible-base as Ansible 2.10.x.

**Why are the versions of ansible-base/ansible-core packages diverging from the Ansible package?**

When the Ansible Community Team set out to restructure the Ansible project, Ansible was split into the following components: 

- The core engine, modules and plugins
- Community and partner supported Ansible Collections of modules and plugins

The former became known as ansible-base, soon to be
[ansible-core](https://github.com/ansible/ansible/blob/devel/docs/docsite/rst/roadmap/ROADMAP_2_11.rst).
The latter became additions on top of the core, available either ad-hoc
or as part of the Ansible community package, which includes a set of
curated and maintained Collections.

Semantic versioning of the Ansible package will let us signal
backwards-compatibility as well as breaking changes in the included
Collections independently of the core engine.

Because these are different components and different things, it is
appropriate for them to be versioned independently from each other.

**Will ansible-base/ansible-core also adopt semantic versioning?**

No, the team managing ansible-core does not currently plan to adopt semantic versioning.

**What is the correlation between Ansible 3.0.0 and ansible-base 2.10.x?**

Ansible 3.0.0 is a package that includes over [85 Ansible Collections](https://github.com/ansible-community/ansible-build-data/blob/main/3/ansible-3.build).
It doesn't include ansible-base: it *depends* on it and specifies a required version range such as *ansible-base>=2.10.6,<2.11* so that the appropriate core package gets installed automatically.
For Ansible 4.0.0, this dependency will shift to *ansible-core>=2.11,<2.12* instead.

ansible-base 2.10.x (as well as ansible-core in the near future) will continue to be available as a standalone package for users that prefer installing only the Collections they need.

**How is the range of included Collection versions established?**

The release build tooling queries the latest version of included Collections and determines the upper-limit based on that version.

For example, if a collection's version is 1.5, the range would be *>=1.5,<2.0*.
If the collection's version is 2.3, the range would be *>=2.3,<3.0*.

The general idea is to keep Collections within a single major version throughout the lifecycle of a single Ansible package major version.

**What version will ansible --version return?**

`ansible --version` will return the version of ansible-base, not the version of the Ansible package, because ansible-base is the one providing the ansible command.

### Installing and upgrading

**How can I install Ansible 3.0.0?**

The Ansible 3.0.0 Community package is [released to PyPI](https://pypi.org/project/ansible/) and can be installed
with `pip install ansible==3.0.0`.

**Can I upgrade to Ansible 3.0.0 from previous versions of Ansible? If so which ones?**

- To upgrade to Ansible-3.0 from Ansible-2.10: `pip install --upgrade ansible`.
- To upgrade to Ansible-3.0 from Ansible-2.9 or earlier: `pip uninstall ansible`; `pip install ansible`.
  This is due to a limitation in pip.

Yes, but the command to upgrade is different depending on the version you have now.

Ansible 3.0.0 is based on ansible-base 2.10, so playbook syntax remains
the same between Ansible-2.10 and Ansible-3.0. However, there may be
incompatibilities in some modules and plugins as Ansible-3.0.0 allows
backwards-incompatible changes in Collections.

**Will I be able to upgrade to Ansible 4.0.0 from Ansible 3.0.0?**

Yes, but you will have to uninstall and reinstall again, due to
the renaming of ansible-base to ansible-core: `pip uninstall ansible`; `pip install ansible`.

Ansible 4.0.0 will be based on
ansible-core 2.11, so playbook syntax in Ansible 4.0.0 may
include backwards incompatible changes (ansible-core does not
use semantic versioning, so updates to the minor version can
contain backwards incompatible changes).  When Ansible 4.0.0 is
ready to start its pre-release cycle, porting guides will be
available to help guide you through those
changes.

### Release cadence and scope

**What is the release cadence moving forward?**

Minor version releases of the Ansible package (such as 3.1.0,
3.2.0) are planned for every three weeks.  These releases will
include new backwards-compatible features, modules and plugins
as well as bug fixes.

Major version releases of the Ansible package (such as 4.0.0,
5.0.0) will happen after new releases of ansible-core. The
Ansible 4.0.0 release is planned for May 2021, soon after the
release of ansible-core 2.11 in April. After 4.0.0, a six month
release cycle for major versions will become the normal cadence,
with 5.0.0 releasing in November, trailing the planned 2.12
release of ansible-core.

**How much change will each minor and major version of Ansible contain?**

Each minor release of the Ansible community package will accept
only backwards-compatible changes in included Collections.
Collections must also use semantic versioning, so the Collection
version numbers will reflect this rule. For example, if Ansible
3.0.0 releases with community.general 2.0.0, then all minor
releases of Ansible 3.x (such as Ansible 3.1.0 or Ansible 3.5.0)
would include a 2.x release of community.general (such as 2.8.0
or 2.9.5).

Each major release of the Ansible community package will accept
the latest released version of each included Collection and may
include the latest released version of ansible-core. Major
releases of the Ansible community package can contain breaking
changes in the modules and other plugins within the included
Collections and/or in core features.

**What changes will each patch release contain, given the use of semantic versioning here?**

Patch releases will be used only when bugs are discovered that
warrant a targeted fix for with a quick turnaround.  For
instance, if a packaging bug is discovered in our release of
3.1.0 that prevents Debian packages from being built, a 3.1.1
release may occur the next day that fixes that issue. No new
features are allowed in patch releases.

### Packaging

**Will Ansible 3.0.0 be made available as an upstream RPM?**

No. RPM-based Linux distros, such as [Fedora](https://src.fedoraproject.org/rpms/ansible),
have been creating superior RPM packages of Ansible for a while
now. So we decided for Ansible-2.10 and ansible-base-2.10, the
Ansible project would no longer provide pre-built RPMs.

**Will Ansible 3.0.0 be available on Ubuntu Launchpad?**

Yes. The Ansible Community Team is catching up to the changes
in how the Ansible content is packaged but plan to have releases
in the PPA soon.  The team is currently testing a new GitHub
action to build the debs for the PPA.

### Terminology

- *The ansible package*

An all-in-one software package (Python, deb, rpm, etc) that
provides backwards compatibility with Ansible 2.9 by including
modules and plugins that have since been migrated to Ansible
Collections.

The Ansible package depends on ansible-base (soon ansible-core).
So when you do pip install ansible, pip installs ansible-base
automatically.

Ansible 3.0.0 contains more Collections thanks to the wider
Ansible community reviewing Collections against the community
checklist. This list of what's included can be found at
[ansible-build-data](https://github.com/ansible-community/ansible-build-data/tree/master/2.10).

- *Collection*

A packaging format for bundling and distributing Ansible
content: plugins, roles, modules, playbooks, documentation and
more. Can be released independent of other Collections or
ansible-base so features and bug
fixes can be made available sooner to users.
    Installed from source repositories, from
[galaxy.ansible.com](https://galaxy.ansible.com/) via
`ansible-galaxy collection install <namespace.collection>` or using a [requirements.yml file](https://galaxy.ansible.com/docs/using/installing.html#installing-multiple-roles-from-a-file).

- *ansible-base*

New for 2.10. The codebase that is now contained in
`github.com/ansible/ansible` for the Ansible 2.10 release. It
contains a minimal amount of modules and plugins and allows
other Collections to be installed. Similar to Ansible 2.9 though
without any content that has since moved into a Collection.

Renamed to ansible-core in the devel branch of Ansible and will
be released under that name from version 2.11 onwards.

- *Red Hat Ansible Automation Platform*

The commercially available enterprise offering from Red Hat,
combining multiple Ansible focused projects, including
ansible-core, awx, galaxy_ng, Collections and various Red Hat
tools focused on an integrated Ansible user experience.
