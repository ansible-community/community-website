---
author: Jake Jackson
date: 2018-01-22 00:00 UTC
description: In this blog, you will find instructions on how to add
  proxy support within Red Hat Ansible Tower.
lang: en-us
title: Adding Proxy Support within Red Hat Ansible Tower
---

# Adding Proxy Support within Red Hat Ansible Tower

![Getting-Started-with-Tower-Adding-Proxy-Support.png](https://www.ansible.com/hubfs/2017_Images/Blog/Getting-Started-with-Tower-Adding-Proxy-Support.png)

## Getting Started with Adding Proxy Support

There are many reasons why proxies are implemented into an environment.
Some can be put in place for security, others as load balancers for your
systems. No matter the use, if you have a proxy in place, Red Hat
Ansible Tower may need to utilize it. For a more in-depth look at what
we will be doing in this post, you can visit our docs specifically on
Proxy Support within Ansible Tower
[here](http://docs.ansible.com/ansible-tower/3.2.1/html/administration/proxy-support.html){linktext="here"
rel=" noopener" target="_blank"}.

## Adding a Load Balancer (Reverse Proxy)

In some instances, you might have Ansible Tower behind a load balancer
and need that information added to your instance. Sessions in Ansible
Tower associate an IP address upon creation, and Ansible Tower's policy
requires that any use of the session match the original IP address.

To allow for support of a proxy, you will have to make a few changes to
your Ansible Tower configuration. Previously, this would have been done
in a settings.py file found on your Ansible Tower host, but as of 3.2
you can now make these changes in the UI. To make these edits, you must
be an admin on the instance and navigate to Settings, and then to
Ansible Tower configuration.

Once you are in the Ansible Tower Configuration, select the System tab
up at the top next to Jobs. Once there, we are going to be making an
edit to the Remote Host Headers box. There will already be some text in
there that is set after the installation. By default REMOTE_HOST_HEADERS
is set to [\[\'REMOTE_ADDR\', \'REMOTE_HOST\'\]]{.monospace}.

The edit you are going to make should reflect the following line with
the relevant information from your organization\'s environment.

```yml
REMOTE_HOST_HEADERS = ['HTTP_X_FORWARDED_FOR', 'REMOTE_ADDR', 'REMOTE_HOST']
```

Once you have entered the relevant information, click the green Save
button in the bottom right corner and you'll be all set.

## Outbound Proxy

Setting up Ansible Tower to utilize an outbound proxy is quick and easy.
One of the things that we see quite often when an outbound proxy needs
to be in place is a project sync failing (if you aren't using locally
stored playbooks). This error appears when Ansible Tower cannot resolve
the source control management (SCM) domain that you are using to manage
your versioned playbooks, such as github.com. To fix this issue, you
will need to make some configuration changes to Ansible Tower. To do
this, navigate to the admin settings (the gear in the top right hand
corner) and from there, select Configure Ansible Tower.

Navigate to the Jobs tab that can be found across the top of the page.
Once you are inside the Jobs tab, scroll down until you find the extra
environment variables.

You will need to enter three line entries to add your proxy to your
instance. Please note, you will need to know the server URL to make
these changes worth your while.

```yml
AWX_TASK_ENV['http_proxy'] = 'http://url:port/'

AWX_TASK_ENV['https_proxy'] = 'http://url:port/'

AWX_TASK_ENV['no_proxy'] = '127.0.0.1,localhost'
```

Once the information has been entered, select the green Save button in
the bottom right hand corner.

Please note, if you are upgrading from a prior release, you may need to
remove prior settings from configuration files before using the Ansible
Tower interface to configure these settings.

Now you can use Ansible Tower's power to automate while allowing it to
utilize your proxy server, ELB or whichever form of filtering you have
in place for your environment. It is not a hard process to implement,
but does require some prior knowledge about your particular
infrastructure.

If you are new to Ansible and want to get started with it, visit our
[Getting Started page](/get-started){linktext="Getting Started page"
rel=" noopener" target="_blank"} to get up and running quickly and gain
the knowledge of automation with [Ansible
Tower](//www.ansible.com/tower){target="_blank"}.

