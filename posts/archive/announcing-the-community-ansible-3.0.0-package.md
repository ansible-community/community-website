---
author: The Ansible Community Team
date: 2021-02-18 00:00 UTC
description: Version 3.0.0 of the Ansible community package marks the
  end of the restructuring of the Ansible ecosystem
lang: en-us
title: Announcing the Community Ansible 3.0.0 Package
---


# Announcing the Community Ansible 3.0.0 Package

Version 3.0.0 of the Ansible community package marks the end of the
restructuring of the Ansible ecosystem. This work culminates what began
in 2019 to [restructure the Ansible
project](https://www.ansible.com/blog/thoughts-on-restructuring-the-ansible-project)
and shape how [Ansible content was
delivered](https://www.ansible.com/blog/the-future-of-ansible-content-delivery).
Starting with Ansible 3.0.0, the versioning and naming reflects the new
structure of the project in the following ways: 

1.  The versioning methodology for the Ansible community package now
    adopts semantic versioning, and begins to diverge from the versions
    of the Ansible Core package (which contains the Ansible language and
    runtime)
2.  The forthcoming Ansible Core package will be renamed from
    ansible-base in version 2.10 to ansible-core in version 2.11 for
    consistency

First, a little history. In Ansible 2.9 and prior, every plugin and
module was in the Ansible project
([https://github.com/ansible/ansible](https://github.com/ansible/ansible))
itself. When you installed the \"ansible\" package, you got the
language, runtime, and all content (modules and other plugins). Over
time, the overwhelming popularity of Ansible created scalability
concerns. Users had to wait many months for updated content. Developers
had to rely on Ansible maintainers to review and merge their content.
These obvious bottlenecks needed to be addressed. 

During the Ansible 2.10 development cycle, the Ansible community
successfully migrated most modules and plugins into
[Collections](https://youtu.be/WOcqhk7TdYc). Collections, and the
modules and plugins within them, could now be developed, updated and
released independently of Ansible itself. When the migration was done,
what remained in the core project started shipping as ansible-base, and
the Ansible Community Team created a new Ansible community package. The
Ansible 2.10 community package included ansible-base 2.10 plus all the
Collections that contain modules and plugins that were migrated out of
the original repository. As of Ansible 2.10, community users had two
options:  continue installing everything with the Ansible community
package, or install ansible-base and then add selected Collections
individually.

Today, there are 3 distinct artefacts in the Ansible open source world:

-   Ansible Core - A minimal Ansible language and runtime (soon to be
    renamed from ansible-base)
-   Ansible Collections on Galaxy (community supported)
-   Ansible community package - Ansible installation including
    ansible-base/core plus community curated Collections

Now that these artefacts are managed separately, their versions are
diverging as well. Moving forward, Ansible Core will maintain its
existing numbering scheme (similar to the Linux Kernel). The next
version of Ansible Core after ansible-base 2.10 will be ansible-core
2.11. The Ansible community package (Ansible Core + community
Collections) is adopting semantic versioning. The next version of the
Ansible community package after 2.10 is 3.0.0.

How the package is maintained and created has changed, but when you
install the Ansible community package, you still get the functionality
that existed in Ansible 2.9, with newer versions of modules and plugins.
Ansible 3.0.0 includes more than 85 Collections containing thousands of
modules and other plugins.

With so many changes happening at once for the Ansible community, we
thought it was a good idea to put together a Q&A that can be found on
our blog.
