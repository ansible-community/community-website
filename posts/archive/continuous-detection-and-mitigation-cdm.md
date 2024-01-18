---
author: Ajay Chenampara
date: 2022-05-09 00:00 UTC
description: In this blog post we will explore a high level view of the
  CDM framework, review Ansible's role in security automation and
  finally understand how Ansible can help agencies with Day 0 through
  Day 2 tasks while working with the CDM framework
lang: en-us
title: Continuous Detection and Mitigation (CDM)
---


# Continuous Detection and Mitigation (CDM)

# Overview

![](https://lh6.googleusercontent.com/D9ATQOEShXCphHdiTFoeVPlnBDL5pwgm9YxFKFdzBQhcW4SU9UDt_tz5wnFGyEo4xLh2UYHT9E2ue1PWVHw27-28d4j-rbu9f6VFSweGjCTFvFr7mBSSC9QsP7pqrHjBECx_PhxDSDKhacp7gg){width="624"
height="301" loading="lazy"}

Per
[NASCIO](https://www.nascio.org/resource-center/resources/state-cio-top-ten-policy-and-technology-priorities-for-2022/),
the top priority for state CIOs is cybersecurity and risk management. A
key focus for this initiative is to leverage [the Continuous Diagnostics
and Mitigation (CDM) framework](https://cisa.gov/cdm) provided by the
Cybersecurity and Infrastructure Security Agency (CISA). In this blog
post we will explore a high level view of the CDM framework, review
Ansible's role in security automation and finally understand how Ansible
can help agencies with Day 0 through Day 2 tasks while working with the
CDM framework.

[]{#whatisCDM hs-anchor="true"}

# What is CDM?

Today more than ever, cyber threats mean that securing and defending our
networks are of utmost importance. A [recent
report](https://www.nlc.org/wp-content/uploads/2019/10/CS-Cybersecurity-Report-Final_0.pdf)
published by the National League of Cities revealed that an astonishing
44% of local governments report they experience a cyberattack daily or
even hourly. So it is not surprising to see that cybersecurity and risk
management is the number one priority for our state CIOs. With that
background, let's understand the CDM program.

![](https://lh4.googleusercontent.com/Ep2ca1JDo7KgvzfnQtoHFdgVKh2SqcQSA0Lu-dI9MeLdp3TRWTNYfO5yBdJau2CI5tGoF4KVM-wW8E130sH-ZJ5UmmIG11K7EP4mvJzhRTqN8FyUN2nRIa3mVYk_nyhj4QAmz8zYsh2oDSRPJg){width="624"
height="355" loading="lazy"}

Source:
[https://www.cisa.gov/cdm-training]{style="font-size: 14px; color: #ee0000;"}

 

The CDM framework is defined by CISA. CDM provides capabilities and
tools that help identify cybersecurity risks on an ongoing basis,
prioritize these risks and enable cybersecurity personnel to mitigate
them based on priority.

At its core it provides tools and dashboards that enable cybersecurity
professionals to understand what is on the network, who is on the
network, and what's happening on the network. CISA's CDM is leading that
effort to reduce cyber risk by delivering tools to federal/state
agencies to strengthen their ability to monitor and manage the threat of
cyber vulnerabilities.

 

[]{#CDMmodel hs-anchor="true"}

# The CDM model

The CDM framework provides an opinionated four layer architecture. The
first layer, layer A, consists of sensors and scanners that are deployed
in the network. These scanners and sensors continuously collect data
that match against fingerprints and send it up to the second layer,
layer B, or the integration layer. 

![](https://lh4.googleusercontent.com/hD08KUp3DTFPp37AUXLh2IQ35u4p1M2nalc0fG4qcJTR_ROrgFVS6f_MEbc3Lph6I2acgbChHyssmuT3VMVgz_xYQ1j5tEPmH0ctLokvjSbh1-GLENQwBWKIAIFXKXZQXBSPV0tx9veEEokOXw){width="384"
height="216" loading="lazy"}

**Source**: [CISA\'s YouTube
channel](https://www.youtube.com/watch?v=BPR_sTWgjPc){style="font-size: 14px; color: #ee0000;"}

The second layer, Layer B, normalizes the data sent in by the Layer A
sensors and scanners. This serves as the correlation point.

**![](https://lh4.googleusercontent.com/6nACWQrEMJz5v4KGBNBYv8Be8af-KL3lr92jbFmdPY5ChKW5gN9Bj5Vbk8O2Z2l7jfXiQYXu8c6MeZLtbwCffcNZWrHmXuAc4W9reAuGMrhTVa5M1XF6wCAuxz3y6AWZYhSUb-dM0RFb-UjQKw){width="384"
height="219" loading="lazy"}**

**Source:** [CISA\'s YouTube
channel](https://www.youtube.com/watch?v=BPR_sTWgjPc){style="font-size: 14px; color: #ee0000;"}

After normalization, the data is fed up into the C&D layers that consist
of agency level and federal level dashboards.

![](https://lh5.googleusercontent.com/Q5Sxxij2NwN1A8oT9ZhGxgFaJpVBw0UJMTZuqvhYoCfVHZNVasaRDtyQJTbrjW0nkX_IJldJIdIWS3sTXZ8H4T1IyVZypdcDkyQ62z8jv-wx5SGsXT4Oq9EssXO21qLaDQ-GscqB8OITLiKu-A){width="401"
height="209" loading="lazy"}

**Source:** [CISA\'s YouTube
channel](https://www.youtube.com/watch?v=BPR_sTWgjPc){style="font-size: 14px; color: #ee0000;"}

Agency security personnel then reviews the dashboards and makes
decisions on prioritizing and mitigating the alerts.

 

[]{#ansiblesecurity hs-anchor="true"}

# Ansible for security automation

Ansible has been a leader in the infrastructure automation domain for
years now. The value that Ansible brings to the infrastructure domain
easily translates into the security automation space, including:

-   **Increases speed:** Reduce the number of manual steps and
    GUI-clicks. Enables the integration between numerous security
    solutions at the agency.

```{=html}
<!-- -->
```
-   **Reduces human errors:** Minimizes risk with automated workflows
    and human operator errors in time-sensitive, stressful situations.

```{=html}
<!-- -->
```
-   **Enforces consistency:** Enables auditable and verifiable security
    processes by using a single framework across multiple security
    tools.

The scale and complexity of the modern infrastructure that needs to be
protected in combination with the challenge of speed brought by modern
cyberattacks using automation themselves require technology to support
human operators. The challenges for cybersecurity teams is managing
multiple security tools within the CDM architecture,integrating between
the tools and using the tool data to effectively manage changes to their
end-points.

 

[]{#AnsibleforCDMusecase hs-anchor="true"}

# Ansible for the CDM use case

CDM has an opinionated architecture and an [approved product
list](https://www.gsa.gov/technology/technology-products-services/it-security/continuous-diagnostics-mitigation-cdm/buy-continuous-diagnostics-and-mitigation-tools)
of over 240,000 products that agencies can use. You can imagine the
integration needs for CDM implementations across agencies for the
different products involved. Red Hat Ansible Automation Platform is one
of the approved products sanctioned for the CDM use case. So where does
Ansible fit in this four layered CDM model? Let's take a look at layer A
that consists of sensor and scanners:

 

![](https://lh4.googleusercontent.com/OusI5gJs98uMszK9-8qpyKgJ46h93Yzvj96kaaHov8n8C0NW1U2XzSH1QHBn3WyTAL-JO1bPqyRJmwdmyvh5XasM4sZk2iJljjf81OyHifLtTl2LqfZIDNpUjBp3MrkxWbYxl-8c7GbrAMC9Zw){width="456"
height="251" loading="lazy"}

The two use cases that are immediately apparent for this layer are:

1.  Log enrichment
2.  Fingerprint/signature updates

Each time the security operations center (SOC) needs to triage an
incident, they might need increased verbosity of logs from the sensors
or from the endpoint themselves. Typically this eliminates potential
false positives. Doing this manually means SOC personnel have to log in
and make these configuration changes. Doing this at scale across an
agency can be manually intensive and prone to human error. And of course
after investigation these log levels need to be reset to standard! Using
Ansible to automatically turn on log enrichment during the investigation
and subsequently turn off the verbosity at scale is an effective use
case for the CDM layer A sensors and scanners. 

Scanners and sensors that make up layer A will need timely updates to
fingerprints based on newer attack vectors. Imagine having to manually
update these fingerprints across thousands of sensors! Ansible can be a
good solution to automate this Day 2 operational task needed for layer
A.

What about layer B? If you recall, layer B collates the logs from layer
A and normalizes the data along with correlating it.

![](https://lh6.googleusercontent.com/_CADMtCRSHvHcR7FgkfBtYc2uY1OU6JEa5XYTTCxjjd-N-3w_-j_kOClsBTGDTDK60Q_VdRbcjdYe2SaQHiOUaQ0dAWT0Vgezwnh1afg02FBuIn0tfD6a70jYgfQ6y4QQ_yFh-vfzaglTmJa9g){width="479"
height="256" loading="lazy"}

These devices are servers, which are subject to all the traditional Day
2 operations that automation can help, such as patching, OS upgrades,
and software updates. 

Finally, the C and D layers serve dashboards that a SOC personnel
reviews and acts on. 

![](https://lh3.googleusercontent.com/K6K0MYWOey8WXsQjJcBIC0syOmrryZbEKnOI6wBJ26MYvL7GWbIxveXhHvdtYpE73OFhz6rqUBi8c4QHRUYW9jKD8JmGjKTNnS19H4R9EutCkK4SgxpIAUIX-JMRAPoALHoO8gZ7XBoOpf7btw){width="624"
height="307" loading="lazy"}

Having Ansible Playbooks to mitigate known vulnerabilities could be
leveraged at this layer with API integration with automation controller
. Ansible is a proven multi-vendor automation platform. Agencies could
adopt automated mitigation for known vulnerabilities by firing off an
automation request to Ansible. Another use case is automating some
aspects of triage coordination. For example, if multiple teams are
needed to look into a certain alert, Ansible could fire off tickets
automatically to the appropriate teams who can then start their triage
(and even use Ansible for that triage process).


# Summary

In summary, CDM is an opinionated security framework laid out by CISA
and adopted by agencies as a way to address cybersecurity and threat
response. CDM prescribes an approved list of products, which include
Ansible Automation Platform, that agencies can leverage. Ansible
Automation Platform can be a valuable platform for automating the
different layers of CDM. Benefits include:

1.  Sensors and scanners: 

2.  1.  Log enrichment
    2.  Update signatures

3.  Integration layer: 

4.  1.  Patching
    2.  Day 2 Operations

5.  Mitigation

6.  1.  Automated mitigation
    2.  Triage coordination

