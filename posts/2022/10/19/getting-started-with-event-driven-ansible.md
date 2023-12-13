---
title: Getting Started with Event-Driven Ansible
author: Nuno Martins
date: 2022-10-19 13:00:00
slug: getting-started-with-event-driven-ansible
category: event-driven-ansible
tags: event-driven-ansible, getting-started, eda, ansible-rulebook, rulebooks
type: text
---

# Getting Started with Event-Driven Ansible

![getting-started-with-event-driven-ansible](/images/posts/getting-started-with-event-driven-ansible/event-driven-ansible.png)

As one technology advances, it expands the possibilities for other technologies and offers the solutions of tomorrow for the challenges we face today. AnsibleFest 2022 brings us new advances in Ansible automation that are as bright as they are innovative. I am talking about the Event-Driven Ansible developer preview.

Automation allows us to give our systems and technology speed and agility while minimizing human error. However, when it comes to trouble tickets and issues, we are often left to traditional and manual methods of troubleshooting and information gathering. We inherently slow things down and interrupt our businesses. We have to gather information, try our common troubleshooting steps, confirm with different teams, and eventually, we need to sleep. 

###### Support lifecycle diagram with many manual steps and hand-offs.

![getting-started-with-event-driven-ansible](/images/posts/getting-started-with-event-driven-ansible/lifecycle-diagram.png)

One application of Event-Driven Ansible is to remediate technology issues before near real-time, or at least trigger troubleshooting and information collection in an attempt to find the root cause of an outage while your support teams handle other issues. 

###### Event driven automation used in the support lifecycle: fewer steps, faster Mean-Time-To-Resolution.

![getting-started-with-event-driven-ansible](/images/posts/getting-started-with-event-driven-ansible/event-driven-automation.png)

Event-Driven Ansible has the potential to change the way we respond to issues and illuminates many new automation possibilities. So, how do you take the next step with Event-Driven Ansible?

## Let’s get started! 
Event-Driven Ansible is currently in developer preview, however there is nothing stopping us from installing ansible-rulebook, which is the CLI component of Event-Driven Ansible, and building our first rulebook. Event-Driven Ansible contains a decision framework that was built using Drools. We need a rulebook to tell the system what events to flag and how to respond to them. These rulebooks are also created in YAML and are used like traditional Ansible Playbooks, so this makes it easier to understand and build the rulebooks we need. One key difference between playbooks and rulebooks is the If-this-then-that coding that is needed in a rulebook to make an event driven  automation approach work.  

A rulebook is comprised of three main components: 

* **Sources** define which event source we will use. These sources come from source plugins which have been built to accommodate common use cases. With time, more and more sources will be available. There are some source plugins that are available already, including: webhooks, Kafka, Azure service bus, file changes, and alertmanager. 

* **Rules** define conditionals we will try to match from the event source. Should the condition be met, then we can trigger an action.

* **Actions** trigger what you need to happen should a condition be met. Some of the current actions are: run_playbook, run_module, set_fact, post_event, and debug.

![getting-started-with-event-driven-ansible](/images/posts/getting-started-with-event-driven-ansible/event-source.png)

Now, let's install ansible-rulebook and start with our very first event.

To install ansible-rulebook, we can install our Galaxy Collection, which has a playbook to install everything we need.

`ansible-galaxy collection install ansible.eda`

Once the Collection is installed, you can run the install-rulebook-cli.yml playbook. This will install everything you need to get started with ansible-rulebook on the command line. This is currently supported for Mac and Fedora.

**Note:** Now, you could also skip this method above and install ansible-rulebook with pip, followed by installing the ansible.eda collection. Java 11+ is required if you use this method and we suggest using [openjdk](https://jdk.java.net/19/). (This step is not required if you used the previous install method.)
~~~
`pip install ansible-rulebook`

`ansible-galaxy collection install ansible.eda`
~~~
If you want to contribute to ansible-rulebook, you can also fork the following [GitHub repository](https://github.com/ansible/ansible-rulebook). This repository also contains instructions for setting up your development environment and how to build a test container. 

Let's build an example rulebook that will trigger an action from a webhook. We will be looking for a specific payload from the webhook, and if that condition is met from the webhook event, then ansible-rulebook will trigger the desired action. Below is our example rulebook:

```
…webhook-example.yml
---
- name: Listen for events on a webhook
 hosts: all

 ## Define our source for events

 sources:
   - ansible.eda.webhook:
       host: 0.0.0.0
       port: 5000

 ## Define the conditions we are looking for

 rules:
   - name: Say Hello
     condition: event.payload.message == "Ansible is super cool!"

 ## Define the action we should take should the condition be met

     action:
       run_playbook:
         name: say-what.yml
```

If we look at this example, we can see the structure of the rulebook. Our sources, rules and actions are defined. We are using the webhook source plugin from our ansible.eda collection, and we are looking for a message payload from our webhook that contains “Ansible is super cool”. Once this condition has been met, our defined action will trigger, which in this case is to trigger a playbook. 

One important thing to take note of ansible-rulebook is that it is not like ansible-playbook which runs a playbook and once the playbook has been completed it will exit. With ansible-rulebook, it will continue to run waiting for events and matching those events. It will only exit upon a shutdown action or if there is an issue with the event source itself, for example if a website you are watching with the url-check plugin stops working. 

With our rulebook built, we will simply tell ansible-rulebook to use it as a ruleset and wait for events:

```
root@ansible-rulebook:/root# ansible-rulebook --rules webhook-example.yml -i inventory.yml --verbose

INFO:ansible_events:Starting sources
INFO:ansible_events:Starting sources
INFO:ansible_events:Starting rules
INFO:root:run_ruleset
INFO:root:{'all': [{'m': {'payload.message': 'Ansible is super cool!'}}], 'run': <function make_fn.<locals>.fn at 0x7ff962418040>}
INFO:root:Waiting for event
INFO:root:load source
INFO:root:load source filters
INFO:root:Calling main in ansible.eda.webhook
```

Now, ansible-rulebook is ready and it's waiting for an event to match. If a webhook is triggered but the payload does not match our condition in our rule, we can see it in the ansible-rulebook verbose output:

```
…
INFO:root:Calling main in ansible.eda.webhook
INFO:aiohttp.access:127.0.0.1 [14/Oct/2022:09:49:32 +0000] "POST /endpoint HTTP/1.1" 200 158 "-" "curl/7.61.1"
INFO:root:Waiting for event
```

But once our payload matches what we are looking for, that’s when the magic happens, so we will simulate a webhook with the correct payload:

```
curl -H 'Content-Type: application/json' -d "{\"message\": \"Ansible is super cool\"}" 127.0.0.1:5000/endpoint



INFO:root:Calling main in ansible.eda.webhook
INFO:aiohttp.access:127.0.0.1 [14/Oct/2022:09:50:28 +0000] "POST /endpoint HTTP/1.1" 200 158 "-" "curl/7.61.1"
INFO:root:calling Say Hello
INFO:root:call_action run_playbook
INFO:root:substitute_variables [{'name': 'say-what.yml'}] [{'event': {'payload': {'message': 'Ansible is super cool'}, 'meta': {'endpoint': 'endpoint', 'headers': {'Host': '127.0.0.1:5000', 'User-Agent': 'curl/7.61.1', 'Accept': '*/*', 'Content-Type': 'application/json', 'Content-Length': '36'}}}, 'fact': {'payload': {'message': 'Ansible is super cool'}, 'meta': {'endpoint': 'endpoint', 'headers': {'Host': '127.0.0.1:5000', 'User-Agent': 'curl/7.61.1', 'Accept': '*/*', 'Content-Type': 'application/json', 'Content-Length': '36'}}}}]
INFO:root:action args: {'name': 'say-what.yml'}
INFO:root:running Ansible playbook: say-what.yml
INFO:root:Calling Ansible runner

PLAY [say thanks] **************************************************************

TASK [debug] *******************************************************************
ok: [localhost] => {
    "msg": "Thank you, my friend!"
}

PLAY RECAP *********************************************************************
localhost                  : ok=1    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

INFO:root:Waiting for event
```

We can see from the output above, that the condition was met from the webhook and ansible-rulebook then triggered our action which was to run_playbook. The playbook we defined is then triggered and once it completes we can see we revert back to “Waiting for event”. 

Event-Driven Ansible opens up the possibilities of faster resolution and greater automated observation of our environments. It has the possibility of simplifying the lives of many technical and sleep-deprived engineers. The current ansible-rulebook is easy to learn and work with, and the graphical user interface EDA-Server will simplify this further. 

## What can you do next?

 Whether you are beginning your automation journey or a seasoned veteran, there are a variety of resources to enhance your automation knowledge:

* Watch the AnsibleFest keynote on the Future of Automation on Wednesday, October 19 at 9AM CT either in person or virtually. There will be a banner on [ansible.com](http://ansible.com/) for the livestream link if you are not attending in person. This keynote will also be available on demand after the event.

* [Self-paced lab exercises](https://www.redhat.com/en/engage/redhat-ansible-automation-202108061218) - We have interactive, in-browser exercises to help you get started with Event-Driven Ansible and ansible-rulebook. 

* [Event-Driven Ansible](https://www.ansible.com/event-driven) web page 

* [Introducing Event-Driven Ansible](https://www.ansible.com/blog/introducing-event-driven-ansible) blog

* [Why Event-Driven Matters](https://www.ansible.com/blog/why-event-driven-matters) - Have a look at another blog about why Event-Driven Ansible matters.

* [Event-Driven Rulebooks](https://youtu.be/PtevBKX1SYI) - Watch another example of Event-Driven Ansible on our YouTube channel.

* [Event-Driven Ansible and Gitops](https://youtu.be/Bb51DftLbPE) - Watch another example of Event-Driven Ansible, but with GitOps, on our YouTube channel.

* Learn more about Event-Driven Ansible at our office hours. The first one is [November 16, 2022,](https://www.redhat.com/en/events/webinar/event-driven-ansible-office-hours-november) followed by [December 14, 2022](https://www.redhat.com/en/events/webinar/event-driven-ansible-office-hours-december).

**Share:**

**Topics:**

[Event-Driven Ansible](https://www.ansible.com/blog/topic/event-driven-ansible)
