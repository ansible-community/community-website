---
author: Jürgen Etzlstorfer
date: 2018-04-13 00:00 UTC
description: Jürgen Etzlstorfer from Dynatrace gives an overview of the
  features in the Ansible and Dynatrace integration.
lang: en-us
title: Enable self-healing applications with Ansible and Dynatrace
---

# Enable self-healing applications with Ansible and Dynatrace

The size, complexity and high rate of change in today's IT environments
can be overwhelming. Enabling the performance and availability of these
modern microservice environments is a constant challenge for IT
organizations.

One trend contributing to this rate of change is the adoption of IT
automation for provisioning, configuration management and ongoing
operations. For this blog, we want to highlight the repeatable and
consistent outcomes allowed by IT automation, and explore what is
possible when Ansible automation is extended to the application
monitoring platform Dynatrace.

## Monitoring Today

Considering the size, complexity and high rate of change in today\'s IT
environments, traditional methods of monitoring application performance
and availability are often necessary and commonplace in most operations
teams. Application performance monitoring (APM) platforms are used to
detect bottlenecks and problems that can impact the experience of your
customers.

Monitoring alone, however, isn't always enough to help keep your
applications running at peak performance. When issues are detected, APM
platforms are designed to alert the operator of the problem and its
root-cause. The Ops team can then agree on a corrective action, and
implement this action against the impacted systems.

What if common or time-consuming corrective actions could be automated?

## Dynatrace Automates Remediation

The Dynatrace APM platform provides AI-powered, full stack performance
monitoring of your microservice environments and its underlying
infrastructure. Dynatrace enables insights into your IT operation and
detects if areas of your environment do not meet performance or error
rate thresholds by an automated baselining.

Once Dynatrace detects abnormal system behavior that affects real users,
a problem alert is created that groups all incidents that share the same
root-cause.

Demo application triggers a Problem alert. Dynatrace detected a
degradation in response time, impacting 54 real users and more than 300
service calls:

![Dynatrace Problem Alert](/images/posts/archive/Ansible-Dynatrace-2.png)

As soon as Dynatrace detects a problem within an environment, a problem
notification can be sent out to third party systems to notify them about
the incidents. Dynatrace allows users to integrate with Ansible Tower as
a Notification System, allowing operators to launch Ansible Tower job
templates from Dynatrace Problem Notifications.

Ansible Tower is now available as a featured third-party integration
within the Dynatrace Notification System:

![Ansible Tower integration with Dynatrace](/images/posts/archive/Ansible-Dynatrace-4.png)

The integration also allows transferring contextual information for the
detected problem. This means Ansible job templates can leverage these
extra variables for a context-aware, finer grained remediation in terms
of executing a predefined playbook. 

Specify the Ansible Tower job template URL, credentials and an optional
custom message. The Notification can be saved and will be triggered as
soon as Dynatrace detects a problem in your
environment:

![Ansible Tower job template](/images/posts/archive/Ansible-Dynatrace-3.png)

Execution of a job template triggered by the Dynatrace problem
notification sent to\
Ansible Tower:

![Dynatrace executes Ansible Tower job](/images/posts/archive/Ansible-Dynatrace-1.png)

Note that extra variables are passed with the job template, designed to eliminate the need for the operator to provide this contextual information.

## Self-Healing Applications in Action

Once your Ansible job templates are in place and customized for
facilitating remediation tasks and the integration within Dynatrace is
set up, the workflow for your self-healing applications looks as
follows:

-   Dynatrace monitors your environment and detects problems once they
    affect real users
-   Dynatrace sends a problem notification to Ansible Tower
-   Ansible Tower launches the specified job template to start the
    remediation
-   Once the problem is resolved, Dynatrace closes the problem

As you can see, the Dynatrace - Ansible Tower integration is designed to
simplify the setup of IT management automation tasks. Furthermore, the
integration of Ansible Tower into the Dynatrace Problem Notifications
workflow enables self-healing applications by triggering pre-defined,
automatable Ansible job templates that are executed by Ansible Tower
each time a problem is detected.
