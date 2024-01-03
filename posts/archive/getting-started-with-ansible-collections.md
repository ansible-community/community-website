---
author: Colin McNaughton
date: 2019-11-14 00:00 UTC
description: In this blog post, we go into how to get started with
  Ansible Content Collections, a part of Red Hat Ansible Automation
  Platform.
lang: en-us
title: Getting Started With Ansible Content Collections
---

# Getting Started With Ansible Content Collections

![blog_getting-started_content-collections](https://www.ansible.com/hs-fs/hubfs/Images/blog-social/blog_getting-started_content-collections.png?width=1024&name=blog_getting-started_content-collections.png){width="1024"
style="width: 1024px;"
srcset="https://www.ansible.com/hs-fs/hubfs/Images/blog-social/blog_getting-started_content-collections.png?width=512&name=blog_getting-started_content-collections.png 512w, https://www.ansible.com/hs-fs/hubfs/Images/blog-social/blog_getting-started_content-collections.png?width=1024&name=blog_getting-started_content-collections.png 1024w, https://www.ansible.com/hs-fs/hubfs/Images/blog-social/blog_getting-started_content-collections.png?width=1536&name=blog_getting-started_content-collections.png 1536w, https://www.ansible.com/hs-fs/hubfs/Images/blog-social/blog_getting-started_content-collections.png?width=2048&name=blog_getting-started_content-collections.png 2048w, https://www.ansible.com/hs-fs/hubfs/Images/blog-social/blog_getting-started_content-collections.png?width=2560&name=blog_getting-started_content-collections.png 2560w, https://www.ansible.com/hs-fs/hubfs/Images/blog-social/blog_getting-started_content-collections.png?width=3072&name=blog_getting-started_content-collections.png 3072w"
sizes="(max-width: 1024px) 100vw, 1024px"}

With the release of Red Hat Ansible Automation Platform, Ansible Content
Collections are now fully supported. Ansible Content Collections, or
collections, represent the new standard of distributing, maintaining and
consuming automation. By combining multiple types of Ansible content
(playbooks, roles, modules, and plugins), flexibility and scalability
are greatly improved.

## Who Benefits?

**Everyone!**

Traditionally, module creators have had to wait for their modules to be
marked for inclusion in an upcoming Ansible release or had to add them
to roles, which made consumption and management more difficult. By
shipping modules within Ansible Content Collections along with pertinent
roles and documentation, and removing the barrier to entry, creators are
now able to move as fast as the demand for their creations. For a public
cloud provider, this means new functionality of an existing service or a
new service altogether, can be rolled out along with the ability to
automate the new functionality.

For the automation consumer, this means that fresh content is
continuously made available for consumption. Managing content in this
manner also becomes easier as modules, plugins, roles, and docs are
packaged and tagged with a collection version. Modules can be updated,
renamed, improved upon; roles can be updated to reflect changes in
module interaction; docs can be regenerated to reflect the edits and all
are packaged and tagged together. 

On top of this, before collections, it was not uncommon for modules to
break or lack timely updates needed to interact with the services they
were interfacing with. This often required Ansible users or Ansible
Tower administrators to run multiple versions of Ansible in [virtual
environments](https://docs.ansible.com/ansible-tower/latest/html/administration/tipsandtricks.html#using-virtualenv-with-at)
in order to consume a patch that addressed a module issue. Ansible
Content Collections bring stability and predictability by breaking
modules out from the core distribution.

For automated organizations, this means that certified content is
readily available to be applied to use-cases ripe for automation from
day one.

## Where to Find Collections

With the launch of Red Hat Ansible Automation Platform, Automation Hub
will be the source for certified collections. Additionally, collections
creators can also package and distribute content on Ansible Galaxy.
Ultimately, it is up to the creator to decide the delivery mechanism for
their content, with Automation Hub being the only source for Red Hat
Certified Collections. Find more information regarding obtaining
certified collections from [Automation
Hub](https://www.ansible.com/blog/getting-started-with-ansible-hub)
here. 

## A Closer Look at Collections

An Ansible Content Collection can be described as a package format for
Ansible content:

![Screen Shot 2019-11-13 at 4.11.45
PM](https://www.ansible.com/hs-fs/hubfs/Screen%20Shot%202019-11-13%20at%204.11.45%20PM.png?width=564&name=Screen%20Shot%202019-11-13%20at%204.11.45%20PM.png){width="564"
style="width: 564px;"
srcset="https://www.ansible.com/hs-fs/hubfs/Screen%20Shot%202019-11-13%20at%204.11.45%20PM.png?width=282&name=Screen%20Shot%202019-11-13%20at%204.11.45%20PM.png 282w, https://www.ansible.com/hs-fs/hubfs/Screen%20Shot%202019-11-13%20at%204.11.45%20PM.png?width=564&name=Screen%20Shot%202019-11-13%20at%204.11.45%20PM.png 564w, https://www.ansible.com/hs-fs/hubfs/Screen%20Shot%202019-11-13%20at%204.11.45%20PM.png?width=846&name=Screen%20Shot%202019-11-13%20at%204.11.45%20PM.png 846w, https://www.ansible.com/hs-fs/hubfs/Screen%20Shot%202019-11-13%20at%204.11.45%20PM.png?width=1128&name=Screen%20Shot%202019-11-13%20at%204.11.45%20PM.png 1128w, https://www.ansible.com/hs-fs/hubfs/Screen%20Shot%202019-11-13%20at%204.11.45%20PM.png?width=1410&name=Screen%20Shot%202019-11-13%20at%204.11.45%20PM.png 1410w, https://www.ansible.com/hs-fs/hubfs/Screen%20Shot%202019-11-13%20at%204.11.45%20PM.png?width=1692&name=Screen%20Shot%202019-11-13%20at%204.11.45%20PM.png 1692w"
sizes="(max-width: 564px) 100vw, 564px"}

 This format has a simple, predictable data structure, with a
straightforward definition:

-   docs/: local documentation for the collection

-   galaxy.yml: source data for the MANIFEST.json that will be part of
    the collection package

-   playbooks/: playbooks reside here 

-   -   tasks/: this holds \'task list files\' for
        include_tasks/import_tasks usage

-   plugins/: all ansible plugins and modules go here, each in its own
    subdir

-   -   modules/: ansible modules
    -   lookups/: [lookup
        plugins](https://docs.ansible.com/ansible/latest/plugins/lookup.html)
    -   filters/: [Jinja2 filter
        plugins](https://docs.ansible.com/ansible/latest/user_guide/playbooks_filters.html)
    -   connection/: [connection
        plugins](https://docs.ansible.com/ansible/latest/plugins/connection.html)
        required if not using default

-   roles/: directory for ansible roles

-   tests/: tests for the collection\'s content

[More information regarding collection
metadata](https://docs.ansible.com/ansible/latest/dev_guide/collections_galaxy_meta.html)

## Interacting with Collections

In addition to downloading collections through the browser, the
\`ansible-galaxy\` command line utility has been updated to manage
collections, providing much of the same functionality as has always been
present to manage, create and consume roles. For example,
\`ansible-galaxy collection init\` can be used to create a starting
point for a new user created collection.

![IMG_0284](https://www.ansible.com/hs-fs/hubfs/IMG_0284.gif?width=1052&name=IMG_0284.gif){width="1052"
style="width: 1052px;"
srcset="https://www.ansible.com/hs-fs/hubfs/IMG_0284.gif?width=526&name=IMG_0284.gif 526w, https://www.ansible.com/hs-fs/hubfs/IMG_0284.gif?width=1052&name=IMG_0284.gif 1052w, https://www.ansible.com/hs-fs/hubfs/IMG_0284.gif?width=1578&name=IMG_0284.gif 1578w, https://www.ansible.com/hs-fs/hubfs/IMG_0284.gif?width=2104&name=IMG_0284.gif 2104w, https://www.ansible.com/hs-fs/hubfs/IMG_0284.gif?width=2630&name=IMG_0284.gif 2630w, https://www.ansible.com/hs-fs/hubfs/IMG_0284.gif?width=3156&name=IMG_0284.gif 3156w"
sizes="(max-width: 1052px) 100vw, 1052px"}

Along with the correct directory structure to start creating a
collection from, this command also generates a metadata file that will
be used while building the collection with namespace and collection name
pre-populated:

![Screen Shot 2019-11-13 at 4.10.36
PM](https://www.ansible.com/hs-fs/hubfs/Screen%20Shot%202019-11-13%20at%204.10.36%20PM.png?width=566&name=Screen%20Shot%202019-11-13%20at%204.10.36%20PM.png){width="566"
style="width: 566px;"
srcset="https://www.ansible.com/hs-fs/hubfs/Screen%20Shot%202019-11-13%20at%204.10.36%20PM.png?width=283&name=Screen%20Shot%202019-11-13%20at%204.10.36%20PM.png 283w, https://www.ansible.com/hs-fs/hubfs/Screen%20Shot%202019-11-13%20at%204.10.36%20PM.png?width=566&name=Screen%20Shot%202019-11-13%20at%204.10.36%20PM.png 566w, https://www.ansible.com/hs-fs/hubfs/Screen%20Shot%202019-11-13%20at%204.10.36%20PM.png?width=849&name=Screen%20Shot%202019-11-13%20at%204.10.36%20PM.png 849w, https://www.ansible.com/hs-fs/hubfs/Screen%20Shot%202019-11-13%20at%204.10.36%20PM.png?width=1132&name=Screen%20Shot%202019-11-13%20at%204.10.36%20PM.png 1132w, https://www.ansible.com/hs-fs/hubfs/Screen%20Shot%202019-11-13%20at%204.10.36%20PM.png?width=1415&name=Screen%20Shot%202019-11-13%20at%204.10.36%20PM.png 1415w, https://www.ansible.com/hs-fs/hubfs/Screen%20Shot%202019-11-13%20at%204.10.36%20PM.png?width=1698&name=Screen%20Shot%202019-11-13%20at%204.10.36%20PM.png 1698w"
sizes="(max-width: 566px) 100vw, 566px"}

## Where to Go Next

Ansible Content Collections were first introduced as tech preview in
Ansible Engine 2.8 and are now fully supported in Ansible Engine 2.9 and
are an integral part of Red Hat Ansible Automation Platform. Collections
allow Red Hat Ansible Automation Platform to offer certified, stable
content in order to continue expanding use cases for automation. Future
posts will dive deeper into developing new collections and converting
existing roles into collections.
