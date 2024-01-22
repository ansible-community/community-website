---
author: Sean Cavanaugh
date: 2019-12-20 00:00 UTC
description: With the Red Hat Ansible Automation Platform release in
  November, we released over 50 network resource modules to help make
  automating network devices easier and more turn-key for network
  engineers.
lang: en-us
title: Rebooting Network Devices with Ansible
---

# Rebooting Network Devices with Ansible

With the Red Hat Ansible Automation Platform release in November, we
released over 50 network resource modules to help make automating
network devices easier and more turn-key for network engineers.  In
addition to the new resource modules, Andrius also discussed fact
gathering enhancements in his blog post,
which means with every new resource module, users gain increased fact
coverage for network devices.  For this blog post I want to cover
another cool enhancement that may have gone unnoticed. This is the
ability for network devices to make use of the
[wait_for_connection](https://docs.ansible.com/ansible/latest/modules/wait_for_connection_module.html)
module.  If you are a network engineer that has operational Ansible
Playbooks that need to reboot devices or take them offline, this module
will help you make more programmatic playbooks to handle disconnects. 
By leveraging wait_for_connection network automation playbooks can look
and behave more like playbooks for Linux or Windows hosts.

## Comparing wait_for and wait_for_connection 

There are two great modules that can wait for a condition to be met,
[wait_for](https://docs.ansible.com/ansible/latest/modules/wait_for_module.html)
and the wait_for_connection.  I highly recommend against using the pause
module if you can get away with it, and I equate it to using a
programming equivalent of a sleep within an Ansible Playbook.  Using
either of these two wait_for modules is superior to random pauses within
your Ansible Playbook because they are a more programmatic solution that
is more adaptable to devices taking different amounts of time to
complete a task.  The other problem with the pause module is that using
prompts does not work within Ansible Tower. A much better solution for
human interaction would be to use an Ansible Tower workflow with an
[approval
node](https://docs.ansible.com/ansible-tower/latest/html/userguide/workflow_templates.html#approval-nodes).

The wait_for module can wait until a path on a filesystem exists, or
until a port is active again.  This works great for most reboot use
cases, except for when a system is not able to be logged into
immediately after the port is up.  The wait_for_connection extends the
functionality of the wait_for use case a bit further. The
wait_for_connection module will make sure that Ansible can log back into
the device and receive the appropriate prompts before finishing
completing the task. For Linux and Windows hosts it will use the ping or
win_ping module, for network devices it will make sure the [connection
plugin](https://docs.ansible.com/ansible/latest/plugins/connection.html)
that was last used can fully connect to the device.  At the time of this
blog post this only works with the network_cli connection plugin.  This
means that subsequent tasks can begin operating as intended as soon as
wait_for_connection completes versus where wait_for just knows that port
is open.

## Dealing with prompts

With networking devices when we perform operational tasks such as a
reboot, there is often a prompt to confirm that you want to take an
action.

For example on a Juniper vSRX device:

    admin@rtr3> request system reboot
    Reboot the system ? [yes,no] (no)

The user has to confirm the reload to be able to proceed. Something I
neglected to cover on my deep dive with `cli_command` blog
was that [cli_command module](https://docs.ansible.com/ansible/latest/modules/cli_command_module.html) can handle prompts. The cli_command module can even handle multiple
prompts!  For this example the Cisco router had not saved its config,
and we are performing a reload.  First the Cisco router will alert me
that the System configuration has been modified, and ask me if I want to
save this before I lose my running-configuration:

    rtr1#reload

    System configuration has been modified. Save? [yes/no]:

[After confirming yes or no, you will receive a second
prompt:]{style="background-color: transparent;"}

    Proceed with reload? [confirm]

[We need to build a task that can handle both prompts using the
cli_command module:]{style="background-color: transparent;"}

``` {.line-numbers .language-yaml}
---
- name: reboot ios device
  cli_command:
    command: reload
    prompt:
      - Save?
      - confirm
    answer:
     - y
     - y
```

[The above task will answer yes to both prompts, saving the config and
reloading the device.  The list for prompt answer and the list for
answer must match and be in the same order. This means that the answer
for prompt\[0\] must be
answer\[0\].]{style="background-color: transparent;"}

If you want to see a more detailed example of handling multiple prompts,
[here is an example of a password reset on a Juniper vSRX
device](https://github.com/ansible/workshops/blob/master/provisioner/roles/configure_routers/tasks/juniper_default.yml).

## Using reset_connection in combination 

Now that you understand how to reboot the device with cli_command we can
combine that with the wait_for_connection to create a reusable Ansible
Playbook.  However, we need to add one more task, a [meta:
reset_connection](https://docs.ansible.com/ansible/latest/modules/meta_module.html)
to make this work programmatically.  

We need to make sure the current connection to the network device is
closed so that the socket can be reestablished to the network device
after the reboot takes place.  If the connection is not closed and the
command timeout is longer than the time it takes to reboot, the
persistent connection will attempt to reuse the closed SSH connection
resulting in the failure "Socket is closed". A correct Ansible Playbook
looks like this:

``` {.line-numbers .language-yaml}
- reboot task (this is a snippet, full task removed for brevity)

- name: reset the connection
  meta: reset_connection

- name: Wait for the network device to reload
  wait_for_connection:
    delay: 10
```

Now we have an Ansible Playbook that can reconnect to network devices
after a reboot is issued!  For a full example please [refer to this
reboot.yml](https://gist.github.com/IPvSean/56f6522cc73629984d3e47013240a1fa)
Ansible Playbook for Arista vEOS network devices.

## Where to go next?

This blog helped outline how to create reusable Ansible Playbooks for
rebooting network devices.  One of the next steps is obviously building
out an Ansible Role that can reboot multiple network platforms.  I have
gone ahead and [created one and uploaded it to Github
here](https://github.com/network-automation/tower_workshop/blob/master/network_reload.yml). 
This role will work on Juniper Junos, Cisco IOS and Arista EOS devices
and can be easily modified to handle many more network operating
systems.
