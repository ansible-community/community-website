---
title: Event-Driven Ansible is Here
author: Joe Pisciotta
date: 2023-05-23 13:00:00
slug: event-driven-ansible-is-here
category: event-driven-ansible
tags: event-driven-ansible, release, announcement, eda
type: text
---

![event-driven-ansible-is-here](/images/posts/event-driven-ansible-is-here/event%20driven%20ansible%20is%20here.webp)

As you may recall, we introduced Event-Driven Ansible in developer preview last fall at AnsibleFest. Since that time, much work has been done across the community, the Red Hat development teams, customers, and last but not least, Red Hat partners. Today, [we are pleased to announce](https://www.redhat.com/en/about/press-releases/red-hat-accelerates-it-automation-event-driven-ansible) that Event-Driven Ansible will be concluding its developer preview and will become generally available as part of Red Hat Ansible Automation Platform 2.4.  

If you are new to Event-Driven Ansible, check out the [developer preview blog](https://www.ansible.com/blog/introducing-event-driven-ansible) I wrote last fall to learn the basics, and you may also be interested in this [video on Ansible Rulebooks](https://www.youtube.com/watch?v=PtevBKX1SYI&list=PLdu06OJoEf2a3fFl6uaoyGV526ilwD97R&index=3), as well as others in this playlist.

## Transform your work with Event-Driven Ansible
For many IT teams, there is too much work to do and not enough time to get it all done. Event-Driven Ansible can help your team work smarter, not harder. How often are you doing routine tasks that get in the way of key priorities? How often are you needing to “drop everything” to respond to a ticket enrichment request or handle a user administration issue? Have you had to wake up at night to remediate an issue? How often are you adjusting applications and underlying technologies to support fluctuating workloads? 

You will be happy to know there is a better way, and it is event-driven automation. Many pieces of recurring operational logic and processes can be automated by capturing them in Ansible Rulebooks, including issue remediation, fact gathering for service tickets, user administration tasks, and many more. But what are Ansible Rulebooks? Based on YAML, they are the basis of Event-Driven Ansible and contain conditional “if-this-then-that” logic.

Event-Driven Ansible can also be used with scalability logic, or using rulebooks to codify scalability actions for rapid and seamless response, such as adding capacity or adjusting buffer pool size when an application or workload calls for it, or scaling out hybrid-cloud solutions when certain conditions are met, and so on.

Event-driven patterns of automation make it faster to act on recurring events and also provide a simple way of distributing operational or scalability knowledge as an easy to read and verifiable structure. Event-Driven Ansible is accessible enough to be used by IT domain experts to solve a range of needs across use cases including infrastructure, networking, security, cloud and others. 

When your organization adopts event-driven automation techniques, your entire team can execute in a consistent and accurate way. You gain new levels of efficiency and can better focus on the innovations that give your business an edge. 

## New features and enhancements


What can you expect from Event-Driven Ansible as part of this release? Several new components and features have been added.  These include: 

* **Event-Driven Ansible controller**, which enables orchestration of multiple rulebooks and provides a single interface to manage and audit all responses across all event sources. These event sources are often third party monitoring and observability tools, but can be any source that provides intelligence about your IT environment.

* **Integration with automation controller in Ansible Automation Platform**, which allows you to call existing workflows that you’ve already built using the run_job_template action, thus extending existing, trusted automation into event-driven automation scenarios. This is an optional way to specify actions from within rulebooks. You can also call an existing Ansible Playbook within your rulebooks, if you prefer. 

* **Event throttling**, which allows you to handle “event storms” using either a reactive approach with the once_within <time> condition or a passive approach with the once_after <time> condition. This allows greater control over when and how actions are executed in response to many events. The Event-Driven Ansible controller also allows default throttling mechanisms that limit scenarios which may result in a greater number of actions than anticipated.

## Event-Driven Ansible Ecosystem Integrations
An ecosystem of Ansible Content Collections is important for Event-Driven Ansible because it works on the intelligence of changing IT conditions that come from event sources such as third party monitoring and observability tools. Ansible Content Collections are a variety of assets that help you jumpstart new automation projects. In the Event-Driven Ansible case, these assets typically are source plug-ins and rulebooks, but may also include other types of useful content. Red Hat Ansible Certified Content Collections are supported by Red Hat and/or partners and typically focus on the “how-to” of some type of automation. Ansible validated content focuses more on “what-to-do” scenarios, including best practices.  

There has been extensive work done across the Event-Driven Ansible ecosystem in terms of new content, by both the community and third party Red Hat partners. The following is an overview of the work that has been done and what is to come: 

* **Certified and validated content**
The initial list of partners who are or will be certifying or validating content includes: Cisco ThousandEyes, CrowdStrike, CyberArk, Dynatrace, F5, IBM, Palo Alto Networks, and Zabbix and there are more to come. Red Hat has also developed key integrations including  Apache Kafka, webhooks, Red Hat Insights, Red Hat OpenShift, Cisco NX-OS and Model-Driven Telemetry, AWS and more. Refer to the image below. More integrations are coming soon, including ServiceNow, Microsoft Azure, Google Cloud Platform and others.

![certified-and-validated-content](/images/posts/event-driven-ansible-is-here/Certified-and-validated-content.webp)

**Points to note**: Certified Content for Event-Driven Ansible generally is  certified event source plugins, written in python, which connect an event source to Ansible Rulebooks. Validated Content for Event-Driven Ansible is generally Ansible Rulebooks which have been validated and contains best practices for common use cases.

* **Community- and custom-developed content** <br>
Community and custom content is available either upstream or through private customer sources. Community-developed integrations have included gcp pubsub and syslogd, among others. Refer to the image above.

Whether you have homegrown monitoring tools or need a specific solution immediately, you can build your own plug-ins for Event-Driven Ansible. This [blog](https://www.ansible.com/blog/creating-custom-event-driven-ansible-source-plugins) explains how to get started. Once you build your plug-in, consider whether this can be contributed to the Ansible community.  

## Getting Involved with Event-Driven Ansible 
Ready to start exploring Event-Driven Ansible? There are a number of ways to do this.  Visit [ansible.com/event-driven](https://www.redhat.com/en/technologies/management/ansible/event-driven-ansible) where you will find a series of free, self-paced interactive labs, information and analyst research.  

You can also join a getting started with Event-Driven Ansible [webinar](https://www.redhat.com/en/events/webinar/work-smarter-using-event-driven-automation-across-IT-operations) on June 20, 2023. If you are attending AnsibleFest at Red Hat Summit 2023, there are many sessions that will support your [learning journey](https://www.ansible.com/blog/learn-about-event-driven-ansible-at-red-hat-summit-and-ansiblefest-2023).

## Resources
* [Press release: Red Hat Accelerates IT Automation with Event-Driven Ansible](https://www.redhat.com/en/about/press-releases/red-hat-accelerates-it-automation-event-driven-ansible)
* [Web page: Event-Driven Ansible](https://www.redhat.com/en/technologies/management/ansible/event-driven-ansible)
* [Partner and Ecosystem integration blog](https://www.ansible.com/blog/event-driven-ansible-partner-ecosystem)
* [Video: Creating Ansible Rulebooks](https://www.youtube.com/watch?v=PtevBKX1SYI)  and [Event-Driven Ansible playlist](https://www.youtube.com/watch?v=TH7_OqBmXD4&list=PLdu06OJoEf2a3fFl6uaoyGV526ilwD97R)
* [Event-Driven Ansible webinar](https://www.redhat.com/en/events/webinar/work-smarter-using-event-driven-automation-across-IT-operations), June 20, 2023
* [Event-Driven Ansible self paced labs](https://www.redhat.com/en/engage/event-driven-ansible-20220907)
* 451 Research paper: [The Impact of Event-Driven Automation](https://www.redhat.com/en/resources/event-driven-impact-on-it-operations-analyst-material)
* [Event-Driven Ansible blog](https://www.ansible.com/blog/topic/event-driven-ansible)
* [Event-driven automation e-book](https://www.redhat.com/en/engage/build-innovation-automation-20230414)

Share:

Topics:<br>
[Event-Driven Ansible](https://www.ansible.com/blog/topic/event-driven-ansible)