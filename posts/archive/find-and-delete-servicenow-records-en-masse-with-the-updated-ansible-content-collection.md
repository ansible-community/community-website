---
author: Colin McNaughton
date: 2022-11-07 00:00 UTC
description: Learn how to find and delete ServiceNow records en masse
  with the updated Ansible Content Collection.
lang: en-us
title: Find and delete ServiceNow records en masse with the updated Ansible Content Collection
---

# Find and delete ServiceNow records en masse with the updated Ansible Content Collection

Have you ever had to query and remove a long list of ServiceNow records?
Yeah, neither have I until recently. Nobody broke into my instance, and
this isn't a one-time operation, I just happen to maintain an instance
that we use to test our Red Hat Ansible Certified Content Collection
for ServiceNow ITSM. 

To set up the environment, I use a demo system and another workflow to
create a random user and then allow a learner to progress through some
challenges using full Red Hat Ansible Automation Platform deployments
and a shared ServiceNow instance. Because this is a real live instance,
there\'s no telling what sort of records learners will create. For this
reason, I recently had to develop some automation to clean up records
created by these demo user accounts.

Although my use-case was to clean up demo user accounts, this could just
as well have been a critical ServiceNow instance that had erroneous
records that needed cleaning up. This Collection can be leveraged to
create, update, modify, or delete just about anything on ServiceNow.

If you're following along, make sure you install a version of the
servicenow.itsm Collection equal to or greater than 2.0.0 (Community on
[Ansible Galaxy](https://galaxy.ansible.com/servicenow/itsm) \|
Certified on [Ansible automation
hub](https://console.redhat.com/ansible/automation-hub/servicenow/itsm)).

 

# How did I do it?

## Using sys_tags

I have a tag setup in ServiceNow that gets applied to everything these
demo users create. I like this approach because tag creation and
auto-application of tags is something that can be limited to accounts
with elevated permissions. The tag is applied to any records created by
users as a part of my hands-on lab, and helps me to locate and clean up
anything those particular users created. First, I need to grab the
sys_id (this is like a global ID of a particular record) of the tag. For
this, I leverage the API module shipped in the servicenow.itsm
Collection against ServiceNow's label table:

``` yml
- name: Find tag ID by name
  servicenow.itsm.api_info:
    resource: label
    sysparm_query: name={{ tag_name }}
      columns:
        - name
        - sys_id
  register: tag_info
```

Once I have located the appropriate tag by name, I can query the
incident table for active records that have that tag applied:

``` yml
- name: Get tagged incidents
  servicenow.itsm.incident_info:
    sysparm_query:
    sys_tags.{{ tag_info.record[0].sys_id }}={{ tag_info.record[0].sys_id }}
    ^active=true
    sysparm_display_value: false
  register: incidents
```

*What\'s* sysparm_display_value*?* Fair enough, good question. This
parameter instructs my query to return the actual values, and not the
display values. Display values vary depending on the type of field, and,
in this case, sys_tags does not include the name of the tag returned by
the query. Setting this parameter to false means that this query returns
the actual value. 

After querying all active records in the incident table that have that
tag applied and registering the output as a variable called incidents, I
wanted to simplify things by creating an array of objects that contain
incident numbers and the date/time they were opened:

``` yml
- name: query incident number and creation time
  ansible.builtin.set_fact:
    incident_list: '{{ incident_list + [{"number": item.number, "opened_at": item.opened_at}] }}'
  loop: "{{ incidents.json.result }}"
  when: incidents
```

Each object in the array should look something like:

``` yml
- number: INC00001234
  opened_at: 2022-04-26 18:34:16
```

For my use case, having the time the record was created is super useful.
I don\'t really want to destroy records that were created less than two
hours ago. After all, I don\'t want to remove records in use by learners
progressing through my challenges.

The last task is to take my list of incidents, and remove them if
they\'re over two hours old. For this, I use the
servicenow.itsm.incident module and some conditional check against the
record creation time:

``` yml
- name: close old incidents from list
  servicenow.itsm.incident:
    state: closed
    number: "{{ item.number }}"
    close_code: "Solved (Permanently)"
    close_notes: "Closed with ansible servicenow.itsm"
  loop: "{{ incident_list }}"
  when: 
    - incident_list is defined
    - (( (ansible_date_time.date + ' ' + ansible_date_time.time) | to_datetime) - (item.opened_at | to_datetime)).total_seconds() > 7200
```

**See that second line under** **when?** It\'s not super pretty, but
it\'s basically making sure that the two time formats are the same
before trying to evaluate the difference in seconds between the two
dates. The first date/time is current execution time, the second
date/time is the time the record was created. If the difference is
greater than two hours (7200 seconds), then the condition is true, the
task continues and the record is closed.

## Without using sys_tags

What if I didn't have tags automatically applied to all of these
records? In that case, I can query records by other keys using
servicenow.itsm.\*\_info modules. For instance, I can query and close
all active incident records created by a specific user:

``` yml
- name: find user created incidents
  servicenow.itsm.incident_info:
    query:
        - sys_created_by: = {{ username }}
        active: = true
  register: incidents

- name: query incident number and creation time
  ansible.builtin.set_fact:
    incident_list: '{{ incident_list + [{"number": item.number, "opened_at": item.opened_at}] }}'
  loop: "{{ incidents.records }}"
  when: incidents

- name: close incidents from list
  servicenow.itsm.incident:
    state: closed
    number: "{{ item.number }}"
    close_code: "Solved (Permanently)"
    close_notes: "Closed with ansible servicenow.itsm"
    other:
      active: false
  loop: "{{ incident_list }}"
  when:
    - incident_list is defined
```

# Completing the picture

I have tasks that do similar things for different record types like
problems, change requests, etc., but they all follow the same pattern as
tasks shown above. I arrange these tasks in a workflow within automation
controller that executes each day to keep this ServiceNow instance tidy.

The 2.0.0 release of servicenow.itsm made all of these tasks much easier
by introducing performance improvements and new API modules to perform
operations on arbitrary tables. For instance, perhaps you'd like to
attach a role to a user. That is super easy by leveraging the API module
against the sys_user_has_role table:

``` yml
- name: attach role to new user
  servicenow.itsm.api:
    resource: sys_user_has_role
    action: post
    data:
      user: "{{ username }}"
      role: "{{ role }}"
```

Boom!

This is probably a non-standard operation. Why would you normally need
to destroy or close out records in your organization's source of truth?
I'm not sure! What I do know is that extending your organization's
automation strategy to other mainstay ITSM processes is made so much
easier by leveraging Ansible Automation Platform and the Red Hat Ansible
Certified Content Collection for ServiceNow ITSM.

# Anything else?

Yeah! Did you know there is a place to get hands-on experience with
Ansible Automation Platform right
[HERE](https://www.redhat.com/en/engage/redhat-ansible-automation-202108061218)?
That is where you'll find my ServiceNow automation challenges that walk
through the functionality of the Collection I leverage to keep my
instance tidy and CMDB up to date.
