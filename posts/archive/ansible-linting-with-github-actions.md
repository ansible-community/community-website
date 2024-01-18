---
author: Colin McCarthy
date: 2020-04-30 00:00 UTC
description: Ansible Linting with GitHub Actions
lang: en-us
title: Ansible Linting with GitHub Actions
---

# Ansible Linting with GitHub Actions

## Want to trigger linting to your Ansible deployment on every Pull Request?

In this blog, I will show you how to add some great automation into your
Ansible code pipeline. 

CI/CD is currently a pretty hot topic for developers. Operations teams
can get started with some automated linting with GitHub actions. If you
use GitHub you can lint your playbooks during different stages including
git pushes or pull requests.

If you're following good git flow practices and have an approval
committee reviewing pull requests, this type of automated testing can
save you a lot of time and keep your Ansible code nice and clean.

## What is Ansible Lint?

Ansible Lint is an open source project that lints your Ansible code. The
[docs](https://docs.ansible.com/ansible-lint/) state that it checks
playbooks for practices and behavior that could potentially be improved.
It can be installed with pip and run manually on playbooks or set up in
a pre-commit hook and run when you attempt a commit on your repo from
the CLI.

The project can be found under the Ansible org on GitHub.

## What are GitHub Actions?

From the GitHub [documentation](https://help.github.com/en/actions):
GitHub actions enable you to create custom workflows to automate your
project's software development life cycle processes. A workflow is a
configurable automated process made up of one or more jobs. You must
create a YAML file to define your workflow configuration. You can
configure your workflows to run when specific activity on GitHub
happens, at a scheduled time, or when an event outside of GitHub occurs.

An Ansible Lint action can be found on GitHub's Actions Marketplace.

## Example repo

Let me show you an example of what this would look like. Here I have a
repo that has an Ansible Playbook.

[https://github.com/colin-mccarthy/ansible_lint_demo](https://github.com/colin-mccarthy/ansible_lint_demo)

I attempted to submit a pull request to add a new playbook. The Ansible
Lint Action kicked off and eventually detected an issue and returned a
failed message.

## Why did it fail?

I'm able to view the build logs under the Actions section of my repo. It
looks like I had some trailing white space and was comparing to an empty
string on one of my tasks.

![Colin M Blog
1](https://www.ansible.com/hs-fs/hubfs/Colin%20M%20Blog%201.png?width=1600&name=Colin%20M%20Blog%201.png){width="1600"
style="width: 1600px;"
srcset="https://www.ansible.com/hs-fs/hubfs/Colin%20M%20Blog%201.png?width=800&name=Colin%20M%20Blog%201.png 800w, https://www.ansible.com/hs-fs/hubfs/Colin%20M%20Blog%201.png?width=1600&name=Colin%20M%20Blog%201.png 1600w, https://www.ansible.com/hs-fs/hubfs/Colin%20M%20Blog%201.png?width=2400&name=Colin%20M%20Blog%201.png 2400w, https://www.ansible.com/hs-fs/hubfs/Colin%20M%20Blog%201.png?width=3200&name=Colin%20M%20Blog%201.png 3200w, https://www.ansible.com/hs-fs/hubfs/Colin%20M%20Blog%201.png?width=4000&name=Colin%20M%20Blog%201.png 4000w, https://www.ansible.com/hs-fs/hubfs/Colin%20M%20Blog%201.png?width=4800&name=Colin%20M%20Blog%201.png 4800w"
sizes="(max-width: 1600px) 100vw, 1600px"}

## Will I get an email notification?

I received an email notification as well, letting me know it had failed.

![Colin M blog
2](https://www.ansible.com/hs-fs/hubfs/Colin%20M%20blog%202.png?width=1024&name=Colin%20M%20blog%202.png){width="1024"
style="width: 1024px;"
srcset="https://www.ansible.com/hs-fs/hubfs/Colin%20M%20blog%202.png?width=512&name=Colin%20M%20blog%202.png 512w, https://www.ansible.com/hs-fs/hubfs/Colin%20M%20blog%202.png?width=1024&name=Colin%20M%20blog%202.png 1024w, https://www.ansible.com/hs-fs/hubfs/Colin%20M%20blog%202.png?width=1536&name=Colin%20M%20blog%202.png 1536w, https://www.ansible.com/hs-fs/hubfs/Colin%20M%20blog%202.png?width=2048&name=Colin%20M%20blog%202.png 2048w, https://www.ansible.com/hs-fs/hubfs/Colin%20M%20blog%202.png?width=2560&name=Colin%20M%20blog%202.png 2560w, https://www.ansible.com/hs-fs/hubfs/Colin%20M%20blog%202.png?width=3072&name=Colin%20M%20blog%202.png 3072w"
sizes="(max-width: 1024px) 100vw, 1024px"}

## Setting it up

To use the action simply create an Ansible Lint.yml (or choose custom `*.yml` name) in the `.github/workflows/` directory.

![Colin M blog
3](https://www.ansible.com/hs-fs/hubfs/Colin%20M%20blog%203.png?width=1600&name=Colin%20M%20blog%203.png){width="1600"
style="width: 1600px;"
srcset="https://www.ansible.com/hs-fs/hubfs/Colin%20M%20blog%203.png?width=800&name=Colin%20M%20blog%203.png 800w, https://www.ansible.com/hs-fs/hubfs/Colin%20M%20blog%203.png?width=1600&name=Colin%20M%20blog%203.png 1600w, https://www.ansible.com/hs-fs/hubfs/Colin%20M%20blog%203.png?width=2400&name=Colin%20M%20blog%203.png 2400w, https://www.ansible.com/hs-fs/hubfs/Colin%20M%20blog%203.png?width=3200&name=Colin%20M%20blog%203.png 3200w, https://www.ansible.com/hs-fs/hubfs/Colin%20M%20blog%203.png?width=4000&name=Colin%20M%20blog%203.png 4000w, https://www.ansible.com/hs-fs/hubfs/Colin%20M%20blog%203.png?width=4800&name=Colin%20M%20blog%203.png 4800w"
sizes="(max-width: 1600px) 100vw, 1600px"}

So here is the really cool part, you can run the action on various
events! This means every time someone submits a PR, or does a push, the
action will be triggered and a container will spin up and run Ansible
lint on your repo. You can define what events will trigger the action
using the on: parameter.

```
on: [push, pull_request]
```

## Pre-commit hooks

I would like to go a little deeper into linting by bringing up
pre-commit hooks.

Pre-commit hooks are little scripts run locally on your machine that can
help identify issues before submission for code review. When talking
about the Ansible Lint action, it would really come in handy to lint the
code before you submit your pull request. This would make sure you
always pass. The GitHub action would just serve as the final step that
guards the shared repo. If you are using pre-commit hooks you should
hypothetically never fail the GitHub action test.

Example:

![Colin M blog
4](https://www.ansible.com/hs-fs/hubfs/Colin%20M%20blog%204.png?width=1600&name=Colin%20M%20blog%204.png){width="1600"
style="width: 1600px;"
srcset="https://www.ansible.com/hs-fs/hubfs/Colin%20M%20blog%204.png?width=800&name=Colin%20M%20blog%204.png 800w, https://www.ansible.com/hs-fs/hubfs/Colin%20M%20blog%204.png?width=1600&name=Colin%20M%20blog%204.png 1600w, https://www.ansible.com/hs-fs/hubfs/Colin%20M%20blog%204.png?width=2400&name=Colin%20M%20blog%204.png 2400w, https://www.ansible.com/hs-fs/hubfs/Colin%20M%20blog%204.png?width=3200&name=Colin%20M%20blog%204.png 3200w, https://www.ansible.com/hs-fs/hubfs/Colin%20M%20blog%204.png?width=4000&name=Colin%20M%20blog%204.png 4000w, https://www.ansible.com/hs-fs/hubfs/Colin%20M%20blog%204.png?width=4800&name=Colin%20M%20blog%204.png 4800w"
sizes="(max-width: 1600px) 100vw, 1600px"}

[https://pre-commit.com](https://pre-commit.com/)

To set this up on my MacBook I simply did a pip install.

```
pip install pre-commit
```

To set it up on your repo just make sure you...​

```
pre-commit install
```

To use Ansible Lint with [pre-commit](https://pre-commit.com/), just add
the following to your local repo's `.pre-commit-config.yaml` file. Make
sure to change `rev:` to be either a git commit sha or tag of Ansible Lint
containing `hooks.yaml`.

![Colin M blog
5](https://www.ansible.com/hs-fs/hubfs/Colin%20M%20blog%205.png?width=1106&name=Colin%20M%20blog%205.png){width="1106"
style="width: 1106px;"
srcset="https://www.ansible.com/hs-fs/hubfs/Colin%20M%20blog%205.png?width=553&name=Colin%20M%20blog%205.png 553w, https://www.ansible.com/hs-fs/hubfs/Colin%20M%20blog%205.png?width=1106&name=Colin%20M%20blog%205.png 1106w, https://www.ansible.com/hs-fs/hubfs/Colin%20M%20blog%205.png?width=1659&name=Colin%20M%20blog%205.png 1659w, https://www.ansible.com/hs-fs/hubfs/Colin%20M%20blog%205.png?width=2212&name=Colin%20M%20blog%205.png 2212w, https://www.ansible.com/hs-fs/hubfs/Colin%20M%20blog%205.png?width=2765&name=Colin%20M%20blog%205.png 2765w, https://www.ansible.com/hs-fs/hubfs/Colin%20M%20blog%205.png?width=3318&name=Colin%20M%20blog%205.png 3318w"
sizes="(max-width: 1106px) 100vw, 1106px"}

## Markdown badge

Once you set up your action, Github will give you a snippet of markdown
code you can add to the README.md displaying the linting status of your
repo. A badge for your repo to show if it is passing the linting test.

![Colin M blog
6](https://www.ansible.com/hs-fs/hubfs/Colin%20M%20blog%206.png?width=1444&name=Colin%20M%20blog%206.png){width="1444"
style="width: 1444px;"
srcset="https://www.ansible.com/hs-fs/hubfs/Colin%20M%20blog%206.png?width=722&name=Colin%20M%20blog%206.png 722w, https://www.ansible.com/hs-fs/hubfs/Colin%20M%20blog%206.png?width=1444&name=Colin%20M%20blog%206.png 1444w, https://www.ansible.com/hs-fs/hubfs/Colin%20M%20blog%206.png?width=2166&name=Colin%20M%20blog%206.png 2166w, https://www.ansible.com/hs-fs/hubfs/Colin%20M%20blog%206.png?width=2888&name=Colin%20M%20blog%206.png 2888w, https://www.ansible.com/hs-fs/hubfs/Colin%20M%20blog%206.png?width=3610&name=Colin%20M%20blog%206.png 3610w, https://www.ansible.com/hs-fs/hubfs/Colin%20M%20blog%206.png?width=4332&name=Colin%20M%20blog%206.png 4332w"
sizes="(max-width: 1444px) 100vw, 1444px"}

After removing the trailing whitespace and fixing all issues my PR is
showing "All checks have passed" and my badge is showing passed.

![Colin M blog
7](https://www.ansible.com/hs-fs/hubfs/Colin%20M%20blog%207.png?width=1600&name=Colin%20M%20blog%207.png){width="1600"
style="width: 1600px;"
srcset="https://www.ansible.com/hs-fs/hubfs/Colin%20M%20blog%207.png?width=800&name=Colin%20M%20blog%207.png 800w, https://www.ansible.com/hs-fs/hubfs/Colin%20M%20blog%207.png?width=1600&name=Colin%20M%20blog%207.png 1600w, https://www.ansible.com/hs-fs/hubfs/Colin%20M%20blog%207.png?width=2400&name=Colin%20M%20blog%207.png 2400w, https://www.ansible.com/hs-fs/hubfs/Colin%20M%20blog%207.png?width=3200&name=Colin%20M%20blog%207.png 3200w, https://www.ansible.com/hs-fs/hubfs/Colin%20M%20blog%207.png?width=4000&name=Colin%20M%20blog%207.png 4000w, https://www.ansible.com/hs-fs/hubfs/Colin%20M%20blog%207.png?width=4800&name=Colin%20M%20blog%207.png 4800w"
sizes="(max-width: 1600px) 100vw, 1600px"}

![Colin M blog
8](https://www.ansible.com/hs-fs/hubfs/Colin%20M%20blog%208.png?width=1600&name=Colin%20M%20blog%208.png){width="1600"
style="width: 1600px;"
srcset="https://www.ansible.com/hs-fs/hubfs/Colin%20M%20blog%208.png?width=800&name=Colin%20M%20blog%208.png 800w, https://www.ansible.com/hs-fs/hubfs/Colin%20M%20blog%208.png?width=1600&name=Colin%20M%20blog%208.png 1600w, https://www.ansible.com/hs-fs/hubfs/Colin%20M%20blog%208.png?width=2400&name=Colin%20M%20blog%208.png 2400w, https://www.ansible.com/hs-fs/hubfs/Colin%20M%20blog%208.png?width=3200&name=Colin%20M%20blog%208.png 3200w, https://www.ansible.com/hs-fs/hubfs/Colin%20M%20blog%208.png?width=4000&name=Colin%20M%20blog%208.png 4000w, https://www.ansible.com/hs-fs/hubfs/Colin%20M%20blog%208.png?width=4800&name=Colin%20M%20blog%208.png 4800w"
sizes="(max-width: 1600px) 100vw, 1600px"}

## In conclusion

Enforcing linting on code changes can build trust that your code is
following best practices. Hopefully, you can try and add some linting to
your Ansible repos with GitHub Actions or pre-commit hooks. Setting up
this action was a lot of fun and I especially like the badge that was
provided.
