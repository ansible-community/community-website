---
author: Jeff Geerling
date: 2018-09-28 00:00 UTC
description: Since starting my journey using Ansible in 2013, I've built Ansible Playbooks to automate many things.
lang: en-us
title: Make your Ansible Playbooks flexible, maintainable, and scalable
---

# Make your Ansible Playbooks flexible, maintainable, and scalable

In the years since, I've learned a lot of tricks to help ease the
maintenance burden for my work. It's important to me to have
maintainable projects, because many of my projects---like Hosted Apache
Solr---have been in operation for over a decade! If it's hard to
maintain the project or it's hard to make major architecture changes,
then I can lose customers to more nimble competitors, I can lose money,
and---most importantly---I can lose my sanity!

I'm presenting a session at AnsibleFest Austin this year,
"Make your Ansible Playbooks flexible, maintainable, and scalable",
and I thought I'd summarize some of the major themes here.

# Stay Organized

I love photography and automation, and so I spend a lot of time
building electronics projects that involve Raspberry Pis and cameras.
Without the organization system I use, it would be very frustrating putting
together the right components for my project.

Similarly, in Ansible, I like to have my tasks organized so I can
compose them more easily, test them, and manage them without too much
effort.

I generally start a playbook with all the tasks in one file. Once I hit
around 100 lines of YAML, I'll work to break related groups of tasks
into separate files and include them in the playbook with
`include_tasks`.

After the playbook starts becoming more complete, I often notice sets
of tasks that are related and can be isolated---like installing a piece
of software, copying a configuration for that software, then starting
(or restarting) a daemon. So I create a new role using
`ansible-galaxy init ROLE_NAME`,
and then put those tasks into that role.

If the role is generic enough, I'll either put it on GitHub and submit
it to Ansible Galaxy, or put it into a separate, private Git repository.
Now I can add a generic set of tests for the role (with
[Molecule](https://github.com/metacloud/molecule/)
or some other testing setup), and I can share the role with many
projects---even with projects managed by completely separate
teams!

Then I include the external roles into my project via a
`requirements.yml`
file. For some projects, where stability is the most important trait, I
will also define the version
(a git ref or tag) for each included Ansible role. For other projects,
where I can afford to sacrifice stability a little for easier
maintenance over time (like test playbooks, or one-off server
configurations), I'll just put the role name (and repo details if it's
not on Galaxy).

For most projects, I don't commit the external roles (those defined in
`requirements.yml`) to the repository---I have a task in my CI system which installs the
roles fresh on every run. However, there are some cases where it's best
to commit *all* the roles to the codebase. For example,
since developers can run my [Drupal VM](https://www.drupalvm.com/) playbook on
a daily basis, and these developers often don't live near where Ansible
Galaxy's servers are located, they had trouble installing the large
number of Ansible Galaxy roles required. So I committed the roles to the
codebase, and now they don't have to wait for all the roles to be
installed every time they build a new Drupal VM instance.

If you *do*
commit the roles to your codebase, you need to have a thorough process
for updating roles---make sure you don't let your
`requirements.yml` file go out of sync with the installed roles! I often run
`ansible-galaxy install -r requirements.yml --force`
to force-replace all the required roles in the codebase, and keep myself
honest!

## Simplify and Optimize

```
> YAML is not a programming language.
>
> ---Jeff Geerling
```

One of the reasons people enjoy using Ansible is because it uses YAML,
and has a declarative syntax. You want a package installed, so you have
the task package: `name=httpd state=present`. You want a
service running, so you have the task service: `name=httpd state=started`.

There are many cases where you need to add a little more intelligence,
though. For example, if you're using the same role to build both VMs
and containers and you don't want the service started in the container,
you need to add a when condition, like:

```yaml
- name: Ensure Apache is started.
  service:
    name: httpd
    state: started
  when: 'server_type != "container"'
```

This kind of logic is simple, and makes sense when reading a task and
figuring out what it does. But some may try to stuff tons of fancy logic
inside when
conditions or other places where Ansible gives a little exposure to
Jinja2 and Python, and that's when things can get off the
rails.

As a rule of thumb, if you've spent more than 10 minutes wrestling
with escaping quotes in a
when condition
in your playbook, it's probably time to consider writing a separate
module to perform the logic you need to do for the task. Python should
*generally* be in a separate module, not
inline with the rest of the YAML. There are exceptions to this (e.g.
when comparing more complex dicts and strings), but I try to avoid
writing any complex code in my Ansible
playbooks.

Besides avoiding complex logic, it's also helpful to have your
playbooks run faster. Many times, I'll profile a playbook timer in the `ansible.cfg`
file defaults section and run the playbook, and find that one or two
tasks or roles takes a really long time, compared to the rest of the
playbook.

For example, one playbook used the copy module
for a large directory with dozens of files. Because of the way Ansible
performs a file copy internally, this meant there were many seconds
wasted waiting for Ansible to ferry each file across the SSH
connection.

Converting that task to use `synchronize` instead saved many seconds per playbook run.
For one run, this doesn't
seem like much; but when the playbook is run on a schedule (e.g. to
enforce a certain configuration on a server), or run as part of your CI
suite, it's important to help make it efficient. Otherwise this can
burn extra CPU cycles on inefficient code, and developers often hate
waiting a long time for CI tests to pass before they can know if their
code broke something or not.
