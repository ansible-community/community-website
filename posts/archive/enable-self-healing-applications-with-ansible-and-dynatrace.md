---
author: Jürgen Etzlstorfer
date: 2018-04-13 00:00 UTC
description: Jürgen Etzlstorfer from Dynatrace gives an overview of the
  features in the Ansible and Dynatrace integration.
lang: en-us
title: Enable self-healing applications with Ansible and Dynatrace
---

# Enable self-healing applications with Ansible and Dynatrace

[![Ansible_and_Dynatrace](https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Ansible_and_Dynatrace.png?width=1024&height=535&name=Ansible_and_Dynatrace.png){width="1024"
height="535" style="width: 1024px;"
srcset="https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Ansible_and_Dynatrace.png?width=512&height=268&name=Ansible_and_Dynatrace.png 512w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Ansible_and_Dynatrace.png?width=1024&height=535&name=Ansible_and_Dynatrace.png 1024w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Ansible_and_Dynatrace.png?width=1536&height=803&name=Ansible_and_Dynatrace.png 1536w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Ansible_and_Dynatrace.png?width=2048&height=1070&name=Ansible_and_Dynatrace.png 2048w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Ansible_and_Dynatrace.png?width=2560&height=1338&name=Ansible_and_Dynatrace.png 2560w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Ansible_and_Dynatrace.png?width=3072&height=1605&name=Ansible_and_Dynatrace.png 3072w"
sizes="(max-width: 1024px) 100vw, 1024px"} ]{#hs_cos_wrapper_post_body
.hs_cos_wrapper .hs_cos_wrapper_meta_field

*The size, complexity and high rate of change in today's IT environments
can be overwhelming. Enabling the performance and availability of these
modern microservice environments is a constant challenge for IT
organizations. *

*One trend contributing to this rate of change is the adoption of IT
automation for provisioning, configuration management and ongoing
operations. For this blog, we want to highlight the repeatable and
consistent outcomes allowed by IT automation, and explore what is
possible when Ansible automation is extended to the application
monitoring platform Dynatrace.*

*Thanks to [Jürgen
Etzlstorfer](https://www.ansible.com/blog/author/j%C3%BCrgen-etzlstorfer){.author-link} for
giving us an overview of the Ansible and Dynatrace integration.*\
*\
\-\--*

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

[**Demo application triggers a Problem alert. Dynatrace detected a
degradation in response time, impacting 54 real users and more than 300
service calls:**]{style="font-size: 14px; color: #333333;"}

![Dynatrace Problem
Alert](https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Dynatrace-Screenshots/Ansible-Dynatrace-2.png?width=1131&height=917&name=Ansible-Dynatrace-2.png){width="1131"
height="917" style="width: 1131px;"
srcset="https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Dynatrace-Screenshots/Ansible-Dynatrace-2.png?width=566&height=459&name=Ansible-Dynatrace-2.png 566w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Dynatrace-Screenshots/Ansible-Dynatrace-2.png?width=1131&height=917&name=Ansible-Dynatrace-2.png 1131w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Dynatrace-Screenshots/Ansible-Dynatrace-2.png?width=1697&height=1376&name=Ansible-Dynatrace-2.png 1697w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Dynatrace-Screenshots/Ansible-Dynatrace-2.png?width=2262&height=1834&name=Ansible-Dynatrace-2.png 2262w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Dynatrace-Screenshots/Ansible-Dynatrace-2.png?width=2828&height=2293&name=Ansible-Dynatrace-2.png 2828w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Dynatrace-Screenshots/Ansible-Dynatrace-2.png?width=3393&height=2751&name=Ansible-Dynatrace-2.png 3393w"
sizes="(max-width: 1131px) 100vw, 1131px"}\
 

As soon as Dynatrace detects a problem within an environment, a problem
notification can be sent out to third party systems to notify them about
the incidents. Dynatrace allows users to integrate with Ansible Tower as
a Notification System, allowing operators to launch Ansible Tower job
templates from Dynatrace Problem Notifications.

[**\
Ansible Tower is now available as a featured third-party integration
within the Dynatrace Notification System:**]{style="font-size: 14px;"}

![Ansible Tower integration with
Dynatrace](https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Dynatrace-Screenshots/Ansible-Dynatrace-4.png?width=1904&height=1068&name=Ansible-Dynatrace-4.png){width="1904"
height="1068" style="width: 1904px;"
srcset="https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Dynatrace-Screenshots/Ansible-Dynatrace-4.png?width=952&height=534&name=Ansible-Dynatrace-4.png 952w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Dynatrace-Screenshots/Ansible-Dynatrace-4.png?width=1904&height=1068&name=Ansible-Dynatrace-4.png 1904w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Dynatrace-Screenshots/Ansible-Dynatrace-4.png?width=2856&height=1602&name=Ansible-Dynatrace-4.png 2856w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Dynatrace-Screenshots/Ansible-Dynatrace-4.png?width=3808&height=2136&name=Ansible-Dynatrace-4.png 3808w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Dynatrace-Screenshots/Ansible-Dynatrace-4.png?width=4760&height=2670&name=Ansible-Dynatrace-4.png 4760w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Dynatrace-Screenshots/Ansible-Dynatrace-4.png?width=5712&height=3204&name=Ansible-Dynatrace-4.png 5712w"
sizes="(max-width: 1904px) 100vw, 1904px"} 

The integration also allows transferring contextual information for the
detected problem. This means Ansible job templates can leverage these
extra variables for a context-aware, finer grained remediation in terms
of executing a predefined playbook. 

[**\
Specify the Ansible Tower job template URL, credentials and an optional
custom message. The Notification can be saved and will be triggered as
soon as Dynatrace detects a problem in your
environment:**]{style="font-size: 14px;"}

![Ansible Tower job
template](https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Dynatrace-Screenshots/Ansible-Dynatrace-3.png?width=1462&height=1006&name=Ansible-Dynatrace-3.png){width="1462"
height="1006" style="width: 1462px;"
srcset="https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Dynatrace-Screenshots/Ansible-Dynatrace-3.png?width=731&height=503&name=Ansible-Dynatrace-3.png 731w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Dynatrace-Screenshots/Ansible-Dynatrace-3.png?width=1462&height=1006&name=Ansible-Dynatrace-3.png 1462w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Dynatrace-Screenshots/Ansible-Dynatrace-3.png?width=2193&height=1509&name=Ansible-Dynatrace-3.png 2193w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Dynatrace-Screenshots/Ansible-Dynatrace-3.png?width=2924&height=2012&name=Ansible-Dynatrace-3.png 2924w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Dynatrace-Screenshots/Ansible-Dynatrace-3.png?width=3655&height=2515&name=Ansible-Dynatrace-3.png 3655w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Dynatrace-Screenshots/Ansible-Dynatrace-3.png?width=4386&height=3018&name=Ansible-Dynatrace-3.png 4386w"
sizes="(max-width: 1462px) 100vw, 1462px"}

 

[**Execution of a job template triggered by the Dynatrace problem
notification sent to\
Ansible Tower: **]{style="font-size: 14px;"}\
![Dynatrace executes Ansible Tower
job](https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Dynatrace-Screenshots/Ansible-Dynatrace-1.png?width=1919&height=1065&name=Ansible-Dynatrace-1.png){width="1919"
height="1065" style="width: 1919px;"
srcset="https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Dynatrace-Screenshots/Ansible-Dynatrace-1.png?width=960&height=533&name=Ansible-Dynatrace-1.png 960w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Dynatrace-Screenshots/Ansible-Dynatrace-1.png?width=1919&height=1065&name=Ansible-Dynatrace-1.png 1919w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Dynatrace-Screenshots/Ansible-Dynatrace-1.png?width=2879&height=1598&name=Ansible-Dynatrace-1.png 2879w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Dynatrace-Screenshots/Ansible-Dynatrace-1.png?width=3838&height=2130&name=Ansible-Dynatrace-1.png 3838w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Dynatrace-Screenshots/Ansible-Dynatrace-1.png?width=4798&height=2663&name=Ansible-Dynatrace-1.png 4798w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Dynatrace-Screenshots/Ansible-Dynatrace-1.png?width=5757&height=3195&name=Ansible-Dynatrace-1.png 5757w"
sizes="(max-width: 1919px) 100vw, 1919px"}

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
