---
author: Vineeth Reddy Katuru
date: 2022-12-15 00:00 UTC
description: Learn about what Ansible Lint is and why you should use it.
lang: en-us
title: Creating Custom Rules for Ansible Lint
---

# Creating Custom Rules for Ansible Lint

## What is Ansible Lint?

Ansible Lint is a command-line tool, part of the
[ansible-lint upstream community project](https://github.com/ansible/ansible-lint),
for linting of Ansible Playbooks, Roles, and Collections. Ok, so what
exactly is "linting?" Its fundamental objective is to promote proven
behaviors, patterns, and practices while avoiding typical traps that can
quickly result in errors or make code more difficult to maintain. That
is - leverage community recommendations and opinions in writing Ansible
content by means of a tool to help ensure what you're writing is
generally valid.

Additionally, Ansible Lint is designed to assist users in updating
their code to function with more recent Ansible versions. Even though
the version of Ansible being used in production can be an older version
of ansible-core, we advise utilizing it with the most recent
version.

Ansible Lint is opinionated just like any other linter. However,
because community members contributed to its rules, each user has the
option to enable or disable them on an individual or category
basis.

## Why should I use Ansible Lint?

The goal of Ansible Lint is to flag
programming errors, bugs, stylistic errors and suspicious constructs and
also ensure that content created by different
people has a similar look and feel. This makes the adoption and use of
Ansible content easier in the community, and by extension, the
enterprise. By keeping the number of configurable features at a minimum,
authors can achieve more consistent outcomes.

Ansible Lint should be considered a trusted advisor to Ansible content
creators, helping them write and package higher quality Ansible content.
While not all rules may be applicable in all situations, they should be
followed whenever possible.

In 2022, additional rules have been added to help content creators
ready their content for production. With `ansible-lint`
and these rules, developers can have confidence that their playbooks,
roles, and task files are easy to understand and produce consistent
results, whether deployed  on servers in a home lab, or mission-critical
systems in the cloud.

Adopting Ansible Lint will save time by focusing on the quality of the
content and less so on the nuances of formatting and style. As code
formatting is not an art, we can save  time and effort on a project by
applying a standardized code style and formatting.

## Guidelines to add new rule

Multiple rules may be added based on the requirements. Adding a new rule
should combine implementation, testing and documentation. 

Some guidelines to create a new Ansible Lint rule include the following:

-   Use a short but clear class name, which must match the filename.
-   Pick an unused ID; the first number is used to determine the rule section.
    Refer to the rules page and pick one that matches the best your new rule and see which one fits best.
-   Include experimental tags.
    Any new rule must stay as experimental for at least two weeks until this tag is removed in the next major release.
-   Update all class level variables.
-   Implement linting methods needed by your rule, these are the ones starting with match prefix.
    Implement only those you need. For the moment you will need to look at how similar rules were implemented to figure out what to do.
-   Update the tests. It must have at least one test and likely also a negative match one.
-   If the rule is task specific, it may be best to include a test to verify its use inside blocks as well.
-   Optionally run only the rule specific tests with a command like: `tox -e py38-core -- -k NewRule`
-   Run tox in order to run all ansible-lint tests. Adding a new rule can break some other tests. Update them if needed.
-   Run `ansible-lint -L` and check that the rule description renders correctly.
-   Build the documentation using the `tox -e docs` command and check that the new rule is displayed correctly in them.

Here is a reference example [MetaTagValidRule](https://github.com/ansible/ansible-lint/blob/main/src/ansiblelint/rules/meta_no_tags.py)
that may be useful to create new rules.

## Creating Custom Rules

Rules are described using a class file per rule. For example, default
rules are named `DeprecatedVariableRule.py`, etc.

Each rule definition should have the following:

-   ID: A unique identifier.
-   Short description: Brief description of the rule.
-   Description: What the rule is looking for.
-   Tags: One or more tags that may be used to include or exclude the rule.
-   At least one of the following methods:
    -   Match that takes a line and returns none or false; if the line
        doesn't match the test, and true or a custom message, when it
        does. (This allows one rule to test multiple behaviors - see
        e.g. the CommandsInsteadOfModulesRule.)
    -   Matchtask that operates on a single task or handler, such that
        tasks get standardized to always contain a module key and
        module_arguments key. Other common task modifiers, such as when,
        with_items, etc., are also available as keys, if present in the
        task.

An example rule using `match` is:

```yml
from ansiblelint.rules import AnsibleLintRule
class DeprecatedVariableRule(AnsibleLintRule):
    """Deprecated variable declarations."""
    id = 'EXAMPLE002'
    description = 'Check for lines that have old style ${var} ' + \ 'declarations'
    tags = { 'deprecations' }
    def match(self, line: str) -> Union[bool, str]:
        return '${' in line
```

An example rule using `matchtask` is:

```yml
from typing import TYPE_CHECKING, Any, Dict, Union
import ansiblelint.utils
from ansiblelint.rules import AnsibleLintRule
if TYPE_CHECKING:
    from ansiblelint.file_utils import Lintable
class TaskHasTag(AnsibleLintRule):
    """Tasks must have tag."""
    id = 'EXAMPLE001'
    description = 'Tasks must have tag'
    tags = ['productivity']
    def matchtask(self, task: Dict[str, Any], file: 'Lintable' | None = None) -> Union[bool,str]:
        # If the task include another task or make the playbook fail
        # Don't force to have a tag
        if not set(task.keys()).isdisjoint(['include','fail']):
            return False
        # Task should have tags
        if not task.has_key('tags'):
              return True
        return False
```

The task argument to matchtask contains a number of keys - the critical
one is action. The value of task `action` contains the module being
used, and the arguments passed, both as key-value pairs and a list of
other arguments (e.g. the command used with shell).

In ansible-lint 2.0.0, task `action` `args` was renamed
task `action` `module_arguments` to avoid a clash when a
module actually takes args as a parameter key (e.g. ec2_tag)

In ansible-lint 3.0.0 task `action module` was renamed
task `action __ansible_module__` to avoid a clash when a
module takes a module as an argument. As a precaution,
task `action module_arguments` was renamed
task `action __ansible_arguments__`.

## Packaging Custom Rules

The ansible-lint provides a sub directory named custom in its built-in
rules, `/usr/lib/python3.8/site-packages/ansiblelint/rules/custom/` for
example, to install custom rules since v4.3.1. The custom rules, which
are packaged as a Python package installed into this directory, will be
loaded and enabled automatically by ansible-lint.

To make custom rules loaded automatically, you need the following:

-   Packaging your custom rules as a Python package named some descriptive ones like `ansible_lint_custom_rules_foo`.
-   Install it into `<ansible_lint_custom_rules_dir>/custom/<your_custom_rules_subdir>`.

You may accomplish the second by adding some configurations into the
`[options]` section of the `setup.cfg` of your custom rules python package
like the following:

``` yml
[options]
packages =
    ansiblelint.rules.custom.<your_custom_rules_subdir>
Package_dir = ansiblelint.rules.custom.<your_custom_rules_subdir> = <your_rules_source_code_subdir>
```

## Getting Started and Next Steps with Ansible Lint

### Where is the repo?

Ansible repository is open source code, which you can find on GitHub:

https://github.com/ansible/ansible-lint

### Any resources/documentation?

Full, in-depth upstream community documentation of Ansible Lint can be found at:

https://ansible-lint.readthedocs.io/

### How to contribute

As ansible-lint is open source, anyone in the community can also contribute new rules to the project.

Here are the steps that everyone should follow:

-   First create pull requests on a branch of your own fork.
-   After creating your fork on GitHub, do the following at the command-line:

```bash
$ git clone git@github.com:your-name/ansible-lint
$ cd ansible-lint
$ git checkout -b your-branch-name
# DO SOME CODING HERE
$ git add your new files
$ git commit -v
$ git push origin your-branch-name
```
