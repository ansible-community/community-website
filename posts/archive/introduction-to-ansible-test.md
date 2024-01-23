---
author: Anshul Behl
date: 2021-02-22 00:00 UTC
description: How to perform unit and integration tests on Ansible
  automation code with ansible-test as part of devops and CI/CD
  pipelines.
lang: en-us
title: Introduction to ansible-test
---

# Introduction to ansible-test

As automation becomes crucial for more and more business cases, there is
an increased need to test the automation code itself. This is where
ansible-test comes in: developers who want to test their Ansible Content
Collections for sanity, unit and integration tests can use 
ansible-test  to achieve testing workflows that integrate with source
code repositories.

Both ansible-core and ansible-base come
[packaged](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html)
with a cli tool called ansible-test, which can be used by collection
developers to test their Collection and its content. The ansible-test
knows how to perform a wide variety of testing-related tasks, from
linting module documentation and code to running unit and integration
tests.

We will cover different features of ansible-test in brief below.

# How to run ansible-test?

With the general availability of Ansible Content Collections with Ansible-2.9,
a user can run ansible-test inside a collection to test the collection
itself. ansible-test needs to be run from the collection root or below
in order for ansible-test to run tests on the Collection.

If you try to run ansible-test from outside the above directory norms,
it will throw an error like below:

```bash
root@root ~/.ansible/collections ansible-test sanity
ERROR: The current working directory must be at or below:

- an Ansible collection: {...}/ansible_collections/{namespace}/{collection}/

Current working directory: /root/.ansible/collections
```

from the above output you can see how a collection root appears to
ansible-test, it has to be in the form of:

```bash
{...}/ansible_collections/{namespace}/{collection}/
```

When you install a collection from Ansible Galaxy or Automation Hub, the default installation location is:
`{...}/ansible_collections/{namespace}/{collection}/`, which already satisfies the above directory convention.

Even if you specify the installation path to the ansible-galaxy cli
(using the -p option), it will also install a collection inside the
ansible_collections directory by creating one in the given path, like
below:

```bash
root@root ~/temp ll
total 0

root@root ~/temp ansible-galaxy collection install arista.eos -p .
Process install dependency map
Starting collection install process
Installing 'arista.eos:1.2.0' to '/root/temp/ansible_collections/arista/eos'
Installing 'ansible.netcommon:1.4.1' to '/root/temp/ansible_collections/ansible/netcommon'

root@root ~/temp ll
total 4.0K
drwxrwxr-x. 4 root root 4.0K Jan 18 19:21 ansible_collections
```

Make sure you keep the above directory norm when you develop your
collections and test them with ansible-test too, in your local
development environment.

## How to test your collection using ansible-test?

ansible-test provides ways to run different types of tests on your
Collections, broadly these tests are of types listed below:

-   Sanity Tests
-   Unit Tests
-   Integration Tests

We will go through each of these tests in detail.

## Sanity Tests

Sanity tests are made up of scripts and tools used to perform static
code analysis. The primary purpose of these tests is to enforce Ansible
coding standards and requirements. ansible-test includes a variety of
sanity tests to perform the code analysis, which can be found
[in the documentation](https://docs.ansible.com/ansible/latest/dev_guide/testing/sanity/index.html#all-sanity-tests).

## How to run?

You can run the sanity test suite from the root directory of your
collection; below are different scenarios on how you can run the sanity
tests.

```bash
# Run all sanity tests
ansible-test sanity

# Run all sanity tests against against certain files
ansible-test sanity plugins/modules/files/eos_acls.py

# Run all tests with a specific version of python (3.7 in this case)
ansible-test sanity --python 3.7

# Run all tests inside docker (good if you don't have dependencies installed)
ansible-test sanity --docker default

# Run validate-modules against a specific file
ansible-test sanity --test validate-modules lib/ansible/modules/files/template.py
```

To list all the sanity tests available:

```bash
ansible-test sanity --list-tests
```

### How to ignore sanity tests?

Since sanity tests change between Ansible releases, a separate ignore
file is needed for each Ansible major release.

The filename is `tests/sanity/ignore-X.Y.txt`
where `X.Y` is the `ansible-core/ansible-base` release being used to test the collection.

Maintaining a separate file for each Ansible release allows a collection to pass tests for multiple versions of Ansible.

For information on the format of the ignore files, please refer to the
[dev guide](https://docs.ansible.com/ansible/latest/dev_guide/testing/sanity/ignores.html#ignore-file-format)

There are only a limited number of cases where ignores would be needed, so please refer to the
[collections documentation](https://github.com/ansible-collections/overview/blob/main/collection_requirements.rst#ci-testing)

## Unit Tests

Unit tests are small isolated tests that target a specific library or
module. As a collection developer/maintainer, you want to make sure that
your code is unit tested, and ansible-test provides a way to run and do
reporting of unit tests inside your collection.

1.  The tests/units is where all things related to unit testing live
2.  ansible-test uses PyTest underneath the surface to do unit testing, hence it expects the tests to be located in files starting with `test_` or ending with `_test.py`

For more information on how to write unit tests, please refer to the
[guide](https://docs.ansible.com/ansible/latest/dev_guide/testing_units_modules.html).

To run all the unit tests inside a collection, run the below command
from collection root:

```bash
# Run all tests inside docker (good if you don't have dependencies installed)
ansible-test units --docker -v
```

Against a single module file by doing:

```bash
# Only runs if the module directory path and unit test file path are similar
ansible-test units --docker -v apt
```

Or against a specific python version by doing:

```bash
ansible-test units --docker -v --python 2.7 apt
```

If you are running unit tests against things other than modules, such as
module utilities, specify the whole file path:

```bash
ansible-test units --docker -v test/units/module_utils/basic/test_imports.py
```

For advanced usage, see the help:

```bash
ansible-test units --help
```

## Code Coverage

Code coverage reports make it easy to identify untested code for which
more tests should be written.

Add the `--coverage`= option to any test
command to collect code coverage data. If you aren't using the
`--venv` or `--docker` options that create an isolated
python environment, then you may have to use the `--requirements`
option to ensure that the correct version of
the coverage module is installed:

```bash
ansible-test coverage erase
ansible-test units --coverage apt
ansible-test coverage html
```

Reports can be generated in several different formats:

-   `ansible-test coverage report` - Console report.
-   [`ansible-test coverage html` - HTML report.
-   [`ansible-test coverage xml` - XML report.

To clear data between test runs, use the ansible-test coverage erase
command. For a full list of features, see the online help:

```bash
ansible-test coverage --help
```

## Integration Tests

These are end to end tests to check code path functions as expected and
to catch breaking changes in the product that you are trying to
automate. In the context of ansible-test essentially:

1.  The `tests/integration` is where all things related to integration tests live.
2.  The `tests/integration/targets` directory contains all our test cases.
    Each test case is a barebones Ansible Role.

# Conclusion & Next Steps

As shown above, ansible-test can provide a lot of value testing Ansible
Content Collections thoroughly.

For further reading and information, visit the
[Ansible Testing Strategies documentation](https://docs.ansible.com/ansible/latest/dev_guide/testing.html).
If you are unfamiliar with Ansible Collections, check out our
[YouTube playlist for everything about Ansible Collections](https://youtube.com/playlist?list=PLdu06OJoEf2Z85Lrc7_Sdw6mTt4aSKfwt).
The videos will get you up to speed quickly.

Also, don't forget to check out our [Automate infrastructure workflows e-book](https://www.redhat.com/en/engage/infra-automation-ebook-s-202009020400)
if you want to learn more about building a unified, automated pipeline for infrastructure operations.
