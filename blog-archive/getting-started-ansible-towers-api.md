---
author: Jake Jackson
date: 2018-04-03 00:00 UTC
description: This Getting Started post goes over Red Hat Ansible Tower's
  API and how you can use it to extract information to utilize in your
  playbooks and other tools.
lang: en-us
title: Getting Started with Ansible Tower's API
---

# Getting Started with Ansible Tower's API

Welcome to another entry in the Getting Started series.
The API (Application Programming
Interface) or, as I like to refer to it, the Magical Land of Automation
Information, can be used in quite a few ways. In this Getting Started
post, we will be discussing Red Hat Ansible Tower's API and how you can
use it to extract information to utilize in your playbooks and other
tools.

The idea for this blog post came about when David
Federlein was developing a new Ansible
Tower demo and presentation. I will be making references to [that
codebase](https://github.com/dfederlein/ansible-tower-demo), which you
can follow along with throughout this post. Please note that this demo
utilizes Vagrant and VirtualBox so you'll need to have those
applications installed if you would like to stand up the demo yourself.

## Ansible Tower's API

Ansible Tower's API is fully browsable. You can navigate to your
instance's REST API by typing this into your
browser: `http://<Tower server name>/api/v2`. Once there, you can click
any of the listed links and view the current objects loaded for that
particular attribute in Ansible Tower. Everything you can do in Ansible
Tower's UI can be done from the API; you can also use it to view
everything from credentials to users. As we'll review in the next
section, you can manually post to the API or make calls through a
playbook.

## Posting to the API

There are many different ways that you can make calls to the API, but
today we are going to focus on two of the most basic:

1.  Manually from the REST API interface of Ansible Tower
2.  From a playbook

What I mean by "basic" here is that these methods are done only through
Ansible Tower. As most of you might know, you can do some pretty amazing
stuff with the information from Ansible Tower with other applications.

We'll not only be able to configure and modify Ansible Tower via these
methods, but we'll also demonstrate that you can kick off jobs via API
call as well. This will allow tighter integration with other aspects of
your enterprise infrastructure and give the ability to run Red Hat
Ansible Engine workloads while still restrained by
the role-based access controls configured around those resources and Job
Templates.

### Posting Manually

For starters, the easiest (albeit not the quickest or most automated)
way to post to the API is from the API interface. Here you can select an
object to post to. Each object has a template at the bottom of the page
that displays the fields that can be contained in a post.

For example, let's say you want to add a project to your Ansible Tower
instance via the API. All you would have to do is navigate to your
Ansible Tower's API screen `(https://<towerip>/api/v2)`
select the project URL `(/api/v2/projects/)` and then scroll down to the
bottom. Displayed there will be the content, which will look like this:

```json
{
    "name": "",
    "description": "",
    "local_path": "",
    "scm_type": "",
    "scm_url": "",
    "scm_branch": "",
    "scm_clean": false,
    "scm_delete_on_update": false,
    "credential": null,
    "timeout": 0,
    "organization": null,
    "scm_update_on_launch": false,
    "scm_update_cache_timeout": 0
}
```

Once you have that content, fill in the quotes with the relative
information from your environment. After you paste it into your field,
hit POST. If that posted successfully, you can view the project in the
Ansible Tower UI and also through the API.

If it failed, you will receive a notification of a bad request. The
method for fixing the error will show up in quotes below it. For
example, if you are creating a user and fail to enter a password for
that user, it will fail and return the following error:

```json
{
    "password": [
        "This field may not be blank."
    ]
}
```

If you run into any issues with making a post to the API (like the above
error), the OPTIONS button found at the top right of the UI next to GET
can be of great help. The OPTIONS button describes the acceptable values
for POST, PUT and PATCH for the specific object or endpoint you are
wishing to post to.

Once the error you have found is fixed in the content field, hit
"Post" one more time and note that the object has now been added to
Ansible Tower successfully.

### Posting Via a Playbook

Another way to post to Ansible Tower's API is through a playbook. The
GitHub repo that I linked earlier in the post does this throughout the
post installation plays. Almost everything done after the installation
is done through the API.

To see it in action, let's sync that project that you just added into
your instance. This will require some prior knowledge on the
construction of Ansible Playbooks. If you need help or want to brush up
on your playbook knowledge, you can visit our
[documentation](http://docs.ansible.com/ansible/latest/playbooks.html).

The play that kicks off the job sync utilizes the
[URI module](http://docs.ansible.com/ansible/latest/modules/uri_module.html)
within Ansible. This module is used to interact with web services, such
as the Ansible Tower API. This exact play can be found in the codebase
that I linked above at `/roles/tower/main.yml`.

```yml
- name: kick off project sync
  uri:
    url:  https://localhost/api/v1/projects/7/update/
    method: POST
    user: admin
    password: "{{ towerpass }}"
    validate_certs: False
    status_code:
      - 200
      - 201
      - 202
  when: response.status == 201
```

In this playbook task, we are telling Ansible to navigate to the API URL
for your project. In this instance, it's
`https://localhost/api/v2/projects/7/update/`. Notice that the project
has a number before update. Projects are assigned a number in Ansible
Tower based on the timing of their entry into Ansible Tower. This number
can only be found by navigating to the API interface for projects
`https://<your_ip_here>/api/v2/projects/`. Once there, you will need to
find the project you wish to sync and then make a post to the update
endpoint of that project number. The example does the update on project
number 7.

Once you have found the correct project you want to update, you will
need to make a post to the update endpoint. In this example, since we
are updating project 7, the endpoint is
`https://localhost/api/v1/projects/7/update/`.

For this post to work successfully with the URI module, you will need to
also pass the API your user credentials that you log into Tower with. In
this example, we are using the default admin user. You can use whichever
user that has sufficient access to make such a post.

### Kicking Off a Job

Now, the header might seem a little ambiguous. "Jake, kicking off a job
isn't that hard in Ansible Tower." This is correct, but for this
example, we are going to kick off a job in Ansible Tower from a playbook
task, which is yet another thing you can do by making a call to the API.
The specific example I am going to reference can be found in the
vagrant-common role (`/roles/vagrant-common/main.yml`).

Now once you get your spectacles out, the task that I am narrowing is
found in the example below:

```yml
name: kick off the provisioning job template
  shell:  "curl -f -H 'Content-Type: application/json' -XPOST --user
admin:{{ towerpass }}
https://172.16.2.42/api/v2/job_templates/8/launch/ --insecure"
  when: inventory_hostname == 'demovm4'
```

At first glance, you are seeing the shell module in use, running a curl
command to a specific https endpoint. It just so happens that this https
endpoint is the API endpoint for launching a specific job template.

That specific job template is assigned a number in Ansible Tower. In
order to not have to go digging through the API to find your specific
job template endpoint, a quick and easy way to find it is to navigate to
the job template that you want to launch via the API. Once there, look
at the URL and the number it's assigned to will be there.

Once you find the correct job template, the https endpoint will look
something like `api/v2/job_templates/8/launch/`. Hit that endpoint with
a `-XPOST` in a curl command and you should be cooking with gas.
