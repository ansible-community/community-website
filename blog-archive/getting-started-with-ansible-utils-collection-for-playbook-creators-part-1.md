---
author: Ashwini Mhatre
date: 2022-01-24 00:00 UTC
description: The Ansible ansible.utils collection includes a variety of
  plugins that aid in the management, manipulation and visibility of
  data for the Ansible playbook developer.
lang: en-us
slug: getting-started-with-ansible.utils-collection-for-playbook-creators-part-1
title: Getting Started with Ansible.utils Collection for Playbook Creators
---

# Part 1: The Ansible.utils Collection for Playbook Creators

The Ansible `ansible.utils` collection includes a variety of plugins that
aid in the management, manipulation and visibility of data for the
Ansible playbook developer. The most common use case for this collection
is when you want to work with the complex data structures present in an
Ansible playbook, inventory, or returned from modules. See each plugin
[documentation](https://docs.ansible.com/ansible/latest/collections/ansible/utils/index.html)
page for detailed examples for how these utilities can be used in tasks.
In this two-part blog we will overview this collection in part one and
see an example use case of using the utils collection in detail in part
two.

# Plugins inside ansible.utils

Plugins are code which will augment ansible core functionality. This
code executes on control node.it and gives options and extensions for
the core features of Red Hat Ansible Automation Platform. This
`ansible.utils` plugin collection includes:

-   Filter plugins
-   Lookup plugins
-   Test plugins
-   Modules

## Filter plugins

Filter plugins manipulate data. With the right filter you can extract a
particular value, transform data types and formats, perform mathematical
calculations, split and concatenate strings, insert dates and times, and
do much more. Ansible Automation Platform uses the [standard filters](https://jinja.palletsprojects.com/en/3.0.x/templates/#builtin-filters)
shipped with Jinja2 and adds some specialized filter plugins. You can
[create custom Ansible filters as plugins](https://docs.ansible.com/ansible/latest/dev_guide/developing_plugins.html#developing-filter-plugins).
Please refer to the
[docs](https://docs.ansible.com/ansible/latest/plugins/filter.html) for
more information.

The `ansible.utils` filter plugins include the following:

- [ansible.utils.from_xml](https://github.com/ansible-collections/ansible.utils/blob/main/docs/ansible.utils.from_xml_filter.rst) - Convert a given XML string to native python dictionary.
- [ansible.utils.get_path](https://github.com/ansible-collections/ansible.utils/blob/main/docs/ansible.utils.get_path_filter.rst) - Retrieve the value in a variable using a path
- [ansible.utils.index_of](https://github.com/ansible-collections/ansible.utils/blob/main/docs/ansible.utils.index_of_filter.rst) - Find the indices of items in a list matching some criteria
- [ansible.utils.param_list_compare](https://github.com/ansible-collections/ansible.utils/blob/main/docs/ansible.utils.param_list_compare_filter.rst) - Generate the final param list combining/comparing base and provided parameters.
- [ansible.utils.to_paths](https://github.com/ansible-collections/ansible.utils/blob/main/docs/ansible.utils.to_paths_filter.rst) - Flatten a complex object into a dictionary of paths and values
- [ansible.utils.to_xml](https://github.com/ansible-collections/ansible.utils/blob/main/docs/ansible.utils.to_xml_filter.rst) - Convert given JSON string to XML
- [ansible.utils.usable_range](https://github.com/ansible-collections/ansible.utils/blob/main/docs/ansible.utils.usable_range_filter.rst) - Expand the usable IP addresses
- [ansible.utils.validate](https://github.com/ansible-collections/ansible.utils/blob/main/docs/ansible.utils.validate_filter.rst) - Validate data with provided criteria

## Lookup plugins

Lookup plugins are an Ansible-specific extension to the Jinja2
templating language. You can use lookup plugins to access data from
outside sources (files, databases, key/value stores, APIs, and other
services) within your playbooks. Like all
[templating](https://docs.ansible.com/ansible/latest/user_guide/playbooks_templating.html#playbooks-templating),
lookups execute and are evaluated on the Ansible Automation Platform
control machine. Ansible makes the data returned by a lookup plugin
available using the standard templating system. You can use lookup
plugins to load variables or templates with information from external
sources. You can also[create custom lookup plugins](https://docs.ansible.com/ansible/latest/dev_guide/developing_plugins.html#developing-lookup-plugins).
Please refer to the [docs](https://docs.ansible.com/ansible/latest/plugins/lookup.html) for more information.

The `ansible.utils` lookup plugins include:

- [ansible.utils.get_path](https://github.com/ansible-collections/ansible.utils/blob/main/docs/ansible.utils.get_path_lookup.rst) - Retrieve the value in a variable using a path
- [ansible.utils.index_of](https://github.com/ansible-collections/ansible.utils/blob/main/docs/ansible.utils.index_of_lookup.rst) - Find the indices of items in a list matching some criteria
- [ansible.utils.to_paths](https://github.com/ansible-collections/ansible.utils/blob/main/docs/ansible.utils.to_paths_lookup.rst) - Flatten a complex object into a dictionary of paths and values
- [ansible.utils.validate](https://github.com/ansible-collections/ansible.utils/blob/main/docs/ansible.utils.validate_lookup.rst) - Validate data with provided criteria

Note: In `ansible.utils` some plugins were
implemented as both filter and lookup plugins to give the playbook
developer flexibility depending on their use case.

## Test plugins

Test plugins evaluate template expressions and return a value of True or
False. With test plugins you can create
[conditionals](https://docs.ansible.com/ansible/latest/user_guide/playbooks_conditionals.html#playbooks-conditionals)
to implement the logic of your tasks, blocks, plays, playbooks, and
roles. Ansible Automation Platform uses the standard tests shipped as
part of Jinja, and adds some specialized test plugins. Please refer to
the [docs](https://docs.ansible.com/ansible/latest/plugins/test.html)
for more information.

The `ansible.utils` test plugins include:

- [ansible.utils.in_any_network](https://github.com/ansible-collections/ansible.utils/blob/main/docs/ansible.utils.in_any_network_test.rst) - Test if an IP or network falls in any network
- [ansible.utils.in_network](https://github.com/ansible-collections/ansible.utils/blob/main/docs/ansible.utils.in_network_test.rst) - Test if IP address falls in the network
- [ansible.utils.in_one_network](https://github.com/ansible-collections/ansible.utils/blob/main/docs/ansible.utils.in_one_network_test.rst) - Test if IP address belongs in any one of the networks in the list
- [ansible.utils.ip](https://github.com/ansible-collections/ansible.utils/blob/main/docs/ansible.utils.ip_test.rst) - Test if something in an IP address or network
- [ansible.utils.ip_address](https://github.com/ansible-collections/ansible.utils/blob/main/docs/ansible.utils.ip_address_test.rst) - Test if something in an IP address
- [ansible.utils.ipv4](https://github.com/ansible-collections/ansible.utils/blob/main/docs/ansible.utils.ipv4_test.rst) - Test if something is an IPv4 address or network
- [ansible.utils.ipv4_address](https://github.com/ansible-collections/ansible.utils/blob/main/docs/ansible.utils.ipv4_address_test.rst) - Test if something is an IPv4 address
- [ansible.utils.ipv4_hostmask](https://github.com/ansible-collections/ansible.utils/blob/main/docs/ansible.utils.ipv4_hostmask_test.rst) - Test if an address is a valid hostmask
- [ansible.utils.ipv4_netmask](https://github.com/ansible-collections/ansible.utils/blob/main/docs/ansible.utils.ipv4_netmask_test.rst) - Test if an address is a valid netmask
- [ansible.utils.ipv6](https://github.com/ansible-collections/ansible.utils/blob/main/docs/ansible.utils.ipv6_test.rst) - Test if something is an IPv6 address or network
- [ansible.utils.ipv6_address](https://github.com/ansible-collections/ansible.utils/blob/main/docs/ansible.utils.ipv6_address_test.rst) - Test if something is an IPv6 address
- [ansible.utils.ipv6_ipv4_mapped](https://github.com/ansible-collections/ansible.utils/blob/main/docs/ansible.utils.ipv6_ipv4_mapped_test.rst) - Test if something appears to be a mapped IPv6 to IPv4 mapped address
- [ansible.utils.ipv6_sixtofour](https://github.com/ansible-collections/ansible.utils/blob/main/docs/ansible.utils.ipv6_sixtofour_test.rst) - Test if something appears to be a 6to4 address
- [ansible.utils.ipv6_teredo](https://github.com/ansible-collections/ansible.utils/blob/main/docs/ansible.utils.ipv6_teredo_test.rst) - Test if something appears to be an IPv6 teredo address
- [ansible.utils.loopback](https://github.com/ansible-collections/ansible.utils/blob/main/docs/ansible.utils.loopback_test.rst) - Test if an IP address is a loopback
- [ansible.utils.mac](https://github.com/ansible-collections/ansible.utils/blob/main/docs/ansible.utils.mac_test.rst) - Test if something appears to be a valid MAC address
- [ansible.utils.multicast](https://github.com/ansible-collections/ansible.utils/blob/main/docs/ansible.utils.multicast_test.rst) - Test for a multicast IP address
- [ansible.utils.private](https://github.com/ansible-collections/ansible.utils/blob/main/docs/ansible.utils.private_test.rst) - Test if an IP address is private
- [ansible.utils.public](https://github.com/ansible-collections/ansible.utils/blob/main/docs/ansible.utils.public_test.rst) - Test if an IP address is public
- [ansible.utils.reserved](https://github.com/ansible-collections/ansible.utils/blob/main/docs/ansible.utils.reserved_test.rst) - Test for a reserved IP address
- [ansible.utils.resolvable](https://github.com/ansible-collections/ansible.utils/blob/main/docs/ansible.utils.resolvable_test.rst) - Test if an IP or name can be resolved via /etc/hosts or DNS
- [ansible.utils.subnet_of](https://github.com/ansible-collections/ansible.utils/blob/main/docs/ansible.utils.subnet_of_test.rst) - Test if a network is a subnet of another network
- [ansible.utils.supernet_of](https://github.com/ansible-collections/ansible.utils/blob/main/docs/ansible.utils.supernet_of_test.rst) - Test if a network is a supernet of another network
- [ansible.utils.unspecified](https://github.com/ansible-collections/ansible.utils/blob/main/docs/ansible.utils.unspecified_test.rst) - Test for an unspecified IP address
- [ansible.utils.validate](https://github.com/ansible-collections/ansible.utils/blob/main/docs/ansible.utils.validate_test.rst) - Validate data with provided criteria

## Modules

Modules are the main building blocks of Ansible playbooks. Although we
do not generally speak of "module plugins", a module is a type of
plugin. For a developer-focused description of the differences between
modules and other plugins, see
[Modules and plugins: what is the difference?](https://docs.ansible.com/ansible/latest/dev_guide/developing_locally.html#modules-vs-plugins).
Please refer to the [docs](https://docs.ansible.com/ansible/latest/plugins/module.html) for more information.

The `ansible.utils` modules include:

- [ansible.utils.cli_parse](https://github.com/ansible-collections/ansible.utils/blob/main/docs/ansible.utils.cli_parse_module.rst) - Parse cli output or text using a variety of parsers
- [ansible.utils.fact_diff](https://github.com/ansible-collections/ansible.utils/blob/main/docs/ansible.utils.fact_diff_module.rst) - Find the difference between currently set facts
- [ansible.utils.update_fact](https://github.com/ansible-collections/ansible.utils/blob/main/docs/ansible.utils.update_fact_module.rst) - Update currently set facts
- [ansible.utils.validate](https://github.com/ansible-collections/ansible.utils/blob/main/docs/ansible.utils.validate_module.rst) - Validate data with provided criteria

## Accessing and using the ansible.utils Collection

To download the utils Collection, refer to Automation hub (fully
supported, requires a Red Hat Ansible Automation Platform subscription)
or Ansible Galaxy (upstream):

- [Automation hub Collection](https://console.redhat.com/ansible/automation-hub/repo/published/ansible/utils): `ansible.utils`
- [Ansible Galaxy Collection](https://galaxy.ansible.com/ansible/utils): `ansible.utils`

​​Ansible.utils is also available in the Supported Execution environment
along with its required python libraries. Please refer to
[docs for more details about Execution Environments.](https://docs.ansible.com/automation-controller/latest/html/userguide/execution_environments.html)

## Different use cases of Utils

As we know, `ansible.utils` has a variety of plugins and it has various
use cases. The following are the most common use cases of `ansible.utils`:

-   Validating business logic before pushing configurations using validate and test plugins
-   Auditing architectural deposition and layouts using test plugins
-   Managing complex data structure in ansible playbook using `get_path`, `to_path` plugins
-   Conducting minor checks related to network address using test plugins
-   Operational state assessment using cli_parse, validate plugins

## Future scope

Here are some additional `ansible.utils` capabilities that are on the
horizon:

-   **Ipaddr filter plugin supports:**
    - The Ipaddr filter is designed to provide an interface to the [netaddr](https://pypi.org/project/netaddr/) Python package from within Ansible.
    - It can operate on strings or lists of items, test various data to check if they are valid IP addresses, and manipulate the input data to extract requested information.
    - `ipaddr()` works with both IPv4 and IPv6 addresses in various forms. 
    - There are also additional functions available to manipulate IP subnets and MAC addresses.
    - We are currently working on supporting the `ipaddr` filter as part of `ansible.utils` collection.

-   **Support of more number of validate engines in ansible.utils.validation plugin:**
    - Currently the validate plugin is supporting only `ansible.utils.jsonschema` validation engines, but there is plan to add more validation engines.

-   **Support different filter plugins to manipulate input data:**
    -   Recursive plugins: `remove_keys`, `replace_keys`, `keep_keys`

## Contributing to this collection

This collection is intended for plugins that are not platform or
discipline specific. Simple plugin examples should be generic in nature.
More complex examples can include real world platform modules to
demonstrate the utility of the plugin in a playbook.

We welcome community contributions to this collection. If you find
problems, please open an issue or create a PR against the
[ansible.utils collection repository](https://github.com/ansible-collections/ansible.utils).
See [Contributing to Ansible-maintained collections](https://docs.ansible.com/ansible/devel/community/contributing_maintained_collections.html#contributing-maintained-collections)
for complete details.
See the [Ansible Community Guide](https://docs.ansible.com/ansible/latest/community/index.html)
for details on contributing to Ansible.

## Takeaways and next steps

-   `ansible.utils` plugins makes playbook writing experience simple and smooth
-   Implementation of `ansible.utils` plugins is very fast as they executed locally
-   Easy to understand, code, use, and integrate with other modules
-   As its plugins ecosystem, it is so easy to add new plugins in `ansible.utils`
