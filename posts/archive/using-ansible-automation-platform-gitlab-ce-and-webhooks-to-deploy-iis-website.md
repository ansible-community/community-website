---
author: Colin McNaughton
date: 2020-03-17 00:00 UTC
description: In this blog, we run through a simple scenario and apply
  the new integrated webhook feature.
lang: en-us
title: Using Ansible Automation Platform, GitLab CE and webhooks to deploy IIS website
---

# Using Ansible Automation Platform, GitLab CE and webhooks to deploy IIS website

![ansible-blog_automated-webhooks-series](https://www.ansible.com/hs-fs/hubfs/Images/blog-social/ansible-blog_automated-webhooks-series.png?width=1035&name=ansible-blog_automated-webhooks-series.png){width="1035"
style="width: 1035px;"
srcset="https://www.ansible.com/hs-fs/hubfs/Images/blog-social/ansible-blog_automated-webhooks-series.png?width=518&name=ansible-blog_automated-webhooks-series.png 518w, https://www.ansible.com/hs-fs/hubfs/Images/blog-social/ansible-blog_automated-webhooks-series.png?width=1035&name=ansible-blog_automated-webhooks-series.png 1035w, https://www.ansible.com/hs-fs/hubfs/Images/blog-social/ansible-blog_automated-webhooks-series.png?width=1553&name=ansible-blog_automated-webhooks-series.png 1553w, https://www.ansible.com/hs-fs/hubfs/Images/blog-social/ansible-blog_automated-webhooks-series.png?width=2070&name=ansible-blog_automated-webhooks-series.png 2070w, https://www.ansible.com/hs-fs/hubfs/Images/blog-social/ansible-blog_automated-webhooks-series.png?width=2588&name=ansible-blog_automated-webhooks-series.png 2588w, https://www.ansible.com/hs-fs/hubfs/Images/blog-social/ansible-blog_automated-webhooks-series.png?width=3105&name=ansible-blog_automated-webhooks-series.png 3105w"
sizes="(max-width: 1035px) 100vw, 1035px"}

Inside Red Hat Ansible Automation Platform, the Ansible Tower REST API
is the key mechanism that helps enable automation to be integrated into
processes or tools that exist in an environment. With Ansible Tower 3.6
we have brought direct integration with webhooks from GitHub and GitLab,
including the enterprise on-premises versions. This means that changes
in source control can trigger automation to apply changes to
infrastructure configuration, deploy new services, reconfigure existing
applications, and more. In this blog, I'll run through a simple scenario
and apply the new integrated webhook feature.

# Environment

My environment consists of Ansible Tower (one component of Red Hat
Ansible Automation Platform), GitLab CE with a project already created,
and a code server running an IDE with the same git repository cloned. A
single inventory exists on Ansible Tower with just one host, an instance
of Windows 2019 Server running on a certified cloud. For this example,
I'm going to deploy IIS on top of this Windows server and make some
modifications to the html file that I'd like to serve from this site. 

My playbook to deploy IIS is *very* simple:

```yml
 ---
- name: Configure IIS
  hosts: windows

  tasks:
  - name: Install IIS
    win_feature:
      name: Web-Server
      state: present

  - name: Start IIS service
    win_service:
      name: W3Svc
      state: started

  - name: Create website index.html
    win_copy:
      src: files/web.html
      dest: C:\Inetpub\wwwroot\index.html
```

All that I am doing here is adding the \`Web-Server\` feature, starting
IIS and copying my site's html file to the default location for web
content being served by IIS. 

My html file is just as basic:

```html
<html>
<title></title>
<body>

</body>
</html>
```

## Objective and setup

What I would like to happen is that, for each merge request that makes
changes to this one IIS site, the site should be redeployed with this
basic html file.

![Colin blog new
1](https://www.ansible.com/hs-fs/hubfs/Colin%20blog%20new%201.png?width=604&name=Colin%20blog%20new%201.png){style="width: 604px;"
width="604"
srcset="https://www.ansible.com/hs-fs/hubfs/Colin%20blog%20new%201.png?width=302&name=Colin%20blog%20new%201.png 302w, https://www.ansible.com/hs-fs/hubfs/Colin%20blog%20new%201.png?width=604&name=Colin%20blog%20new%201.png 604w, https://www.ansible.com/hs-fs/hubfs/Colin%20blog%20new%201.png?width=906&name=Colin%20blog%20new%201.png 906w, https://www.ansible.com/hs-fs/hubfs/Colin%20blog%20new%201.png?width=1208&name=Colin%20blog%20new%201.png 1208w, https://www.ansible.com/hs-fs/hubfs/Colin%20blog%20new%201.png?width=1510&name=Colin%20blog%20new%201.png 1510w, https://www.ansible.com/hs-fs/hubfs/Colin%20blog%20new%201.png?width=1812&name=Colin%20blog%20new%201.png 1812w"
sizes="(max-width: 604px) 100vw, 604px"}

## GitLab Access Token

As my webhook is triggered, I would like to update the merge request
created in GitLab with the status of my Ansible Tower job. 

To accomplish this, I first have to create a personal access token for
my GitLab account so that Ansible Tower can access the GitLab API. This
is pretty painless. All I have to do is navigate to my user settings and
select "Access Tokens" from the left side navigation panel:

![Colin blog
2](https://www.ansible.com/hs-fs/hubfs/Colin%20blog%202.png?width=1263&name=Colin%20blog%202.png){style="width: 1263px;"
width="1263"
srcset="https://www.ansible.com/hs-fs/hubfs/Colin%20blog%202.png?width=632&name=Colin%20blog%202.png 632w, https://www.ansible.com/hs-fs/hubfs/Colin%20blog%202.png?width=1263&name=Colin%20blog%202.png 1263w, https://www.ansible.com/hs-fs/hubfs/Colin%20blog%202.png?width=1895&name=Colin%20blog%202.png 1895w, https://www.ansible.com/hs-fs/hubfs/Colin%20blog%202.png?width=2526&name=Colin%20blog%202.png 2526w, https://www.ansible.com/hs-fs/hubfs/Colin%20blog%202.png?width=3158&name=Colin%20blog%202.png 3158w, https://www.ansible.com/hs-fs/hubfs/Colin%20blog%202.png?width=3789&name=Colin%20blog%202.png 3789w"
sizes="(max-width: 1263px) 100vw, 1263px"}

I give my access token an easily recognizable name of "Ansible Tower,"
set the expiration date to the end of the month, and scope this access
token to just the API. Upon clicking "Create personal access token," the
token itself becomes visible and a new entry is shown at the bottom of
this page:

![Colin blog
3](https://www.ansible.com/hs-fs/hubfs/Colin%20blog%203.png?width=1248&name=Colin%20blog%203.png){style="width: 1248px;"
width="1248"
srcset="https://www.ansible.com/hs-fs/hubfs/Colin%20blog%203.png?width=624&name=Colin%20blog%203.png 624w, https://www.ansible.com/hs-fs/hubfs/Colin%20blog%203.png?width=1248&name=Colin%20blog%203.png 1248w, https://www.ansible.com/hs-fs/hubfs/Colin%20blog%203.png?width=1872&name=Colin%20blog%203.png 1872w, https://www.ansible.com/hs-fs/hubfs/Colin%20blog%203.png?width=2496&name=Colin%20blog%203.png 2496w, https://www.ansible.com/hs-fs/hubfs/Colin%20blog%203.png?width=3120&name=Colin%20blog%203.png 3120w, https://www.ansible.com/hs-fs/hubfs/Colin%20blog%203.png?width=3744&name=Colin%20blog%203.png 3744w"
sizes="(max-width: 1248px) 100vw, 1248px"}

Next, I will use this token to create a new credential in Ansible Tower
of type "GitLab Personal Access Token":

![Colin blog
4](https://www.ansible.com/hs-fs/hubfs/Colin%20blog%204.png?width=1277&name=Colin%20blog%204.png){style="width: 1277px;"
width="1277"
srcset="https://www.ansible.com/hs-fs/hubfs/Colin%20blog%204.png?width=639&name=Colin%20blog%204.png 639w, https://www.ansible.com/hs-fs/hubfs/Colin%20blog%204.png?width=1277&name=Colin%20blog%204.png 1277w, https://www.ansible.com/hs-fs/hubfs/Colin%20blog%204.png?width=1916&name=Colin%20blog%204.png 1916w, https://www.ansible.com/hs-fs/hubfs/Colin%20blog%204.png?width=2554&name=Colin%20blog%204.png 2554w, https://www.ansible.com/hs-fs/hubfs/Colin%20blog%204.png?width=3193&name=Colin%20blog%204.png 3193w, https://www.ansible.com/hs-fs/hubfs/Colin%20blog%204.png?width=3831&name=Colin%20blog%204.png 3831w"
sizes="(max-width: 1277px) 100vw, 1277px"}

Upon saving, Ansible Tower now has API access to my GitLab account. 

## Ansible Tower Job Template

Now that Ansible Tower has the ability to update my merge requests, I
need to configure webhook access to my job template that is configured
to run my simple IIS playbook. Since the Ansible Tower 3.6 release,
there is now a checkbox on each job template called **ENABLE WEBHOOK**.

![coling blog new
3](https://www.ansible.com/hs-fs/hubfs/coling%20blog%20new%203.png?width=604&name=coling%20blog%20new%203.png){style="width: 604px;"
width="604"
srcset="https://www.ansible.com/hs-fs/hubfs/coling%20blog%20new%203.png?width=302&name=coling%20blog%20new%203.png 302w, https://www.ansible.com/hs-fs/hubfs/coling%20blog%20new%203.png?width=604&name=coling%20blog%20new%203.png 604w, https://www.ansible.com/hs-fs/hubfs/coling%20blog%20new%203.png?width=906&name=coling%20blog%20new%203.png 906w, https://www.ansible.com/hs-fs/hubfs/coling%20blog%20new%203.png?width=1208&name=coling%20blog%20new%203.png 1208w, https://www.ansible.com/hs-fs/hubfs/coling%20blog%20new%203.png?width=1510&name=coling%20blog%20new%203.png 1510w, https://www.ansible.com/hs-fs/hubfs/coling%20blog%20new%203.png?width=1812&name=coling%20blog%20new%203.png 1812w"
sizes="(max-width: 604px) 100vw, 604px"}

Once I select the option to **ENABLE WEBHOOK** I am presented with a few
new fields. I select GitLab as my **WEBHOOK SERVICE**, supply the
credential I created using my GitLab personal access token, **WEBHOOK
URL** is prepopulated with the path to this job template and, upon
saving my modifications, a **WEBHOOK KEY** is generated which I will use
to configure the project hook in GitLab. Also, note that my project
allows me to override the SCM branch. This means that the project will
pull updates from the "change-web-text" branch instead of Master. 

## GitLab Project Hook integration

The next step takes me back to GitLab, this time navigating to the
integrations page of the project I would like to execute the webhook.

![Colin blog
6](https://www.ansible.com/hs-fs/hubfs/Colin%20blog%206.png?width=1260&name=Colin%20blog%206.png){style="width: 1260px;"
width="1260"
srcset="https://www.ansible.com/hs-fs/hubfs/Colin%20blog%206.png?width=630&name=Colin%20blog%206.png 630w, https://www.ansible.com/hs-fs/hubfs/Colin%20blog%206.png?width=1260&name=Colin%20blog%206.png 1260w, https://www.ansible.com/hs-fs/hubfs/Colin%20blog%206.png?width=1890&name=Colin%20blog%206.png 1890w, https://www.ansible.com/hs-fs/hubfs/Colin%20blog%206.png?width=2520&name=Colin%20blog%206.png 2520w, https://www.ansible.com/hs-fs/hubfs/Colin%20blog%206.png?width=3150&name=Colin%20blog%206.png 3150w, https://www.ansible.com/hs-fs/hubfs/Colin%20blog%206.png?width=3780&name=Colin%20blog%206.png 3780w"
sizes="(max-width: 1260px) 100vw, 1260px"}

On the integrations page, I supply the URL (**WEBHOOK URL** from my job
template in Ansible Tower) and Secret Token (**WEBHOOK KEY** from my job
template in Ansible Tower). I also specify the Trigger as "Merge request
events" which means that the URL I specified will be launched anytime a
merge request is opened.

![colin blog new
2](https://www.ansible.com/hs-fs/hubfs/colin%20blog%20new%202.png?width=604&name=colin%20blog%20new%202.png){style="width: 604px;"
width="604"
srcset="https://www.ansible.com/hs-fs/hubfs/colin%20blog%20new%202.png?width=302&name=colin%20blog%20new%202.png 302w, https://www.ansible.com/hs-fs/hubfs/colin%20blog%20new%202.png?width=604&name=colin%20blog%20new%202.png 604w, https://www.ansible.com/hs-fs/hubfs/colin%20blog%20new%202.png?width=906&name=colin%20blog%20new%202.png 906w, https://www.ansible.com/hs-fs/hubfs/colin%20blog%20new%202.png?width=1208&name=colin%20blog%20new%202.png 1208w, https://www.ansible.com/hs-fs/hubfs/colin%20blog%20new%202.png?width=1510&name=colin%20blog%20new%202.png 1510w, https://www.ansible.com/hs-fs/hubfs/colin%20blog%20new%202.png?width=1812&name=colin%20blog%20new%202.png 1812w"
sizes="(max-width: 604px) 100vw, 604px"}

## In action: Updating my website text

Now that I've given Ansible Tower access to my projects using a personal
access token as a new credential type, configured my job template to
enable webhooks, and configured a Project Hook on GitLab to respond to
merge request events on my project, I'm ready to make a test commit of
my html file.

Here, I add text to the \`\<title\>\` and \`\<body\>\` tags of my html
document and save the file:

![Colin blog
8](https://www.ansible.com/hs-fs/hubfs/Colin%20blog%208.png?width=1271&name=Colin%20blog%208.png){style="width: 1271px;"
width="1271"
srcset="https://www.ansible.com/hs-fs/hubfs/Colin%20blog%208.png?width=636&name=Colin%20blog%208.png 636w, https://www.ansible.com/hs-fs/hubfs/Colin%20blog%208.png?width=1271&name=Colin%20blog%208.png 1271w, https://www.ansible.com/hs-fs/hubfs/Colin%20blog%208.png?width=1907&name=Colin%20blog%208.png 1907w, https://www.ansible.com/hs-fs/hubfs/Colin%20blog%208.png?width=2542&name=Colin%20blog%208.png 2542w, https://www.ansible.com/hs-fs/hubfs/Colin%20blog%208.png?width=3178&name=Colin%20blog%208.png 3178w, https://www.ansible.com/hs-fs/hubfs/Colin%20blog%208.png?width=3813&name=Colin%20blog%208.png 3813w"
sizes="(max-width: 1271px) 100vw, 1271px"}

Once I've committed my change on my "change-web-text" branch, I will
push my code, go back to GitLab and open a merge request to merge
changes back into master.

![colin new
blog](https://www.ansible.com/hs-fs/hubfs/colin%20new%20blog.png?width=604&name=colin%20new%20blog.png){style="width: 604px;"
width="604"
srcset="https://www.ansible.com/hs-fs/hubfs/colin%20new%20blog.png?width=302&name=colin%20new%20blog.png 302w, https://www.ansible.com/hs-fs/hubfs/colin%20new%20blog.png?width=604&name=colin%20new%20blog.png 604w, https://www.ansible.com/hs-fs/hubfs/colin%20new%20blog.png?width=906&name=colin%20new%20blog.png 906w, https://www.ansible.com/hs-fs/hubfs/colin%20new%20blog.png?width=1208&name=colin%20new%20blog.png 1208w, https://www.ansible.com/hs-fs/hubfs/colin%20new%20blog.png?width=1510&name=colin%20new%20blog.png 1510w, https://www.ansible.com/hs-fs/hubfs/colin%20new%20blog.png?width=1812&name=colin%20new%20blog.png 1812w"
sizes="(max-width: 604px) 100vw, 604px"}

Opening this merge request will now trigger my webhook which will deploy
my web page changes to my IIS site. Because I have configured Ansible
Tower with my personal access token, Ansible Tower will post a link to
the job executed as a result of the webhook trigger on the merge
request.

If all has been configured correctly, I should see a new job being
executed that corresponds to the job template with the configured
webhook. I should also see a job that has been kicked off, updating my
project which will pull in the latest changes from my GitLab project.

![Colin blog
9](https://www.ansible.com/hs-fs/hubfs/Colin%20blog%209.png?width=604&name=Colin%20blog%209.png){style="width: 604px;"
width="604"
srcset="https://www.ansible.com/hs-fs/hubfs/Colin%20blog%209.png?width=302&name=Colin%20blog%209.png 302w, https://www.ansible.com/hs-fs/hubfs/Colin%20blog%209.png?width=604&name=Colin%20blog%209.png 604w, https://www.ansible.com/hs-fs/hubfs/Colin%20blog%209.png?width=906&name=Colin%20blog%209.png 906w, https://www.ansible.com/hs-fs/hubfs/Colin%20blog%209.png?width=1208&name=Colin%20blog%209.png 1208w, https://www.ansible.com/hs-fs/hubfs/Colin%20blog%209.png?width=1510&name=Colin%20blog%209.png 1510w, https://www.ansible.com/hs-fs/hubfs/Colin%20blog%209.png?width=1812&name=Colin%20blog%209.png 1812w"
sizes="(max-width: 604px) 100vw, 604px"}

Selecting the job for "iis website create", which is the job template I
configured for webhook execution, shows that the job was **LAUNCHED BY**
webhook. **EXTRA VARIABLES** will show a lot of project specific
configuration facts, and more importantly the job output should show
that the job is executing what it's supposed to.

![Colin blog
10](https://www.ansible.com/hs-fs/hubfs/Colin%20blog%2010.png?width=1273&name=Colin%20blog%2010.png){style="width: 1273px;"
width="1273"
srcset="https://www.ansible.com/hs-fs/hubfs/Colin%20blog%2010.png?width=637&name=Colin%20blog%2010.png 637w, https://www.ansible.com/hs-fs/hubfs/Colin%20blog%2010.png?width=1273&name=Colin%20blog%2010.png 1273w, https://www.ansible.com/hs-fs/hubfs/Colin%20blog%2010.png?width=1910&name=Colin%20blog%2010.png 1910w, https://www.ansible.com/hs-fs/hubfs/Colin%20blog%2010.png?width=2546&name=Colin%20blog%2010.png 2546w, https://www.ansible.com/hs-fs/hubfs/Colin%20blog%2010.png?width=3183&name=Colin%20blog%2010.png 3183w, https://www.ansible.com/hs-fs/hubfs/Colin%20blog%2010.png?width=3819&name=Colin%20blog%2010.png 3819w"
sizes="(max-width: 1273px) 100vw, 1273px"}

Upon completion, I should be able to pull up the IP of my IIS server and
see the changes to my incredible html page:

![Colin blog
11](https://www.ansible.com/hs-fs/hubfs/Colin%20blog%2011.png?width=701&name=Colin%20blog%2011.png){style="width: 701px;"
width="701"
srcset="https://www.ansible.com/hs-fs/hubfs/Colin%20blog%2011.png?width=351&name=Colin%20blog%2011.png 351w, https://www.ansible.com/hs-fs/hubfs/Colin%20blog%2011.png?width=701&name=Colin%20blog%2011.png 701w, https://www.ansible.com/hs-fs/hubfs/Colin%20blog%2011.png?width=1052&name=Colin%20blog%2011.png 1052w, https://www.ansible.com/hs-fs/hubfs/Colin%20blog%2011.png?width=1402&name=Colin%20blog%2011.png 1402w, https://www.ansible.com/hs-fs/hubfs/Colin%20blog%2011.png?width=1753&name=Colin%20blog%2011.png 1753w, https://www.ansible.com/hs-fs/hubfs/Colin%20blog%2011.png?width=2103&name=Colin%20blog%2011.png 2103w"
sizes="(max-width: 701px) 100vw, 701px"}

## Takeaways

Webhooks introduced in Ansible Tower 3.6 are an incredibly powerful way
to launch automation in response to events in source control. While this
basic website is just a very quick and simple example, applying this
functionality to infrastructure as code where all service configurations
are defined in Ansible Playbooks greatly emphasizes this robust feature.
