---
author: Hicham Mourad
date: 2022-05-10 00:00 UTC
description: This blog provides some more details about this offering
  and why you should be considering Ansible Automation Platform on
  Azure.
lang: en-us
title: Introducing a brand new way to automate your Azure cloud
---

# Introducing a brand new way to automate your Azure cloud

In December of 2021, Red Hat and Microsoft announced [Red Hat Ansible
Automation
Platform](https://www.redhat.com/en/about/press-releases/red-hat-brings-industry-leading-ansible-automation-platform-microsoft-azure){rel="noopener"}
on [Microsoft
Azure](https://azure.microsoft.com/en-us/blog/expand-hybrid-management-tools-with-red-hat-ansible-automation-platform-on-azure/){rel="noopener"}. 

This year during Red Hat Summit 2022, Red Hat announced the general
availability of Red Hat Ansible Automation Platform on Microsoft Azure
across North America with global availability coming soon.  

I'd like to spend some time providing some more details about this
offering and why you should consider Red Hat Ansible Automation Platform
on Azure.

# Azure Marketplace deployment

Red Hat Ansible Automation Platform on Azure deploys from the Azure
Marketplace as a [managed
application](https://docs.microsoft.com/en-us/azure/azure-resource-manager/managed-applications/overview). 
It deploys directly into your Azure subscription, but as the publisher
of the application, Red Hat has access to a shared and secured managed
resource group to support, maintain, and upgrade your deployment. More
specifically, a dedicated Red Hat SRE team deals with all the ongoing
management of Red Hat Ansible Automation Platform on Azure, while you
focus on expanding your automation strategy within your organization
across the hybrid cloud.

 

![](https://lh3.googleusercontent.com/OPWL4IjTWPFdv4lZdcT42a1e0xJCHXSasDanWMlkXb3-kLei2Nu4c0YJwGIeYQy6vBUOY2hjgK5jPwwDH9cz7xmzanCULPaCr8KECGudX4qtbzx2dl4iezqVHR3LC_PRvwEPUCjBE7_iyFcS-Q){width="231"
height="304" loading="lazy"}

# Azure Integrations

For many organizations using Azure today, there are huge benefits to
take advantage of with Red Hat Ansible Automation Platform on Azure. It
runs in your Azure subscription. It integrates seamlessly with many of
the Azure services, including Azure billing. Also, if you have a
Microsoft Azure Consumption Commitment agreement (MACC), the Red Hat
Ansible Automation Platform on Azure deployment costs will count towards
your MACC, and will be reflected on your Azure bill.  Oh, and did I
mention that Red Hat supports the deployment, and you can automate,
automate, and automate some more!

Once you've deployed Red Hat Ansible Automation Platform on Azure, with
a few simple configuration steps you can integrate into your Azure
active directory (AD) environment for authentication.

![](https://lh5.googleusercontent.com/6CPitNcrDnyJBvZptP4c7SVFOhi5gv_wFt-93ok5k6IPx22JuAg0E9naCYr9kL_tBEBUEVg5iCW3PgkvH0Yv23lj4vjZrPLfsjo4p-vSs7oalKXri4kNReqywJ4YhjCxtdDJjLLCzn8yR5Hwsg){width="391"
height="213" loading="lazy"}

There's great automation content available for you to leverage with
examples to learn from if you\'re new to Red Hat Ansible Automation
Platform on Azure.

Here's a GitHub repository that has automation content for automating
many Azure resources, like Azure Load Balancers, Azure PostgreSQL, Azure
Networking, Azure Security groups, and more. Shortly, I'll highlight
some more as we discuss the [Red Hat Ansible Certified Content
Collection for Microsoft
Azure](https://github.com/ansible-collections/cloud.azure_roles.git){rel="noopener"}.

Here's an image of some sample content.

![](https://lh4.googleusercontent.com/M6I3hg7djn4eIRbOLJ1PBuSCOAru7niO8TUQ4LRBeKzNnqQPHQgHwQ1r7Hq6PgqMiyhrUDf0a-RLpPk8u4GtYIieMAOykjQg-G-JhFVvDoOlA2x8y-WbZxKaz6i-qKdSkhS_zYg2gYMmsRIF6w){width="499"
height="262" loading="lazy"}

# Content is King!

Anyone using Red Hat Ansible Automation Platform on Azure will
definitely want to use the Red Hat Ansible Certified Content Collection
for Microsoft Azure. But with your subscription, you have access to all
the Red Hat Ansible Certified Content at your fingertips!

![](https://lh5.googleusercontent.com/hMxljejVEJmfAFJ4qjrxcpvlPNFua7ij2p75CQPFPtKBRup1mGHOgxUDRslpFOaBA3VOFu50bwIWk_qTNlpdJggchX3-O2I2rG6m1OKB7XC_5zyazp0T4BaVJ4uPQjOQgheKUOSKhVTpevP-JA){width="506"
height="247" loading="lazy"}

The Azure Collection includes over 250 modules to interrogate, manage,
and automate numerous Azure resource types. From Azure AD, to
networking, to DB, to AKS, to storage, to backup, to VMs, to security
groups, to IAM... and so much more.  

![](https://lh4.googleusercontent.com/_ZPlkc11RoD-bMAXzTd-3XgwSuJWH2suXa1QlRJDUMyBcof8u4sUzaoUBrxh9g8OuCHEUi16xp6_I4fTvyv7zac-6ClJK-vxgdWSzMJE2Oxm0Q5HlGrQCJ560yA8EOD4PC7JIwoYRf5_Krkztg){width="429"
height="355" loading="lazy"}

If you'd like to see the full list of modules you can check it out
[here](https://console.redhat.com/ansible/automation-hub/repo/published/azure/azcollection/content)
on the Automation automation hub.  

Here's an example of an Ansible Automation Platform workflow template
linking together many job templates to perform a larger automation
task.  In this case, spinning up a full development environment for the
DevOps team.

![](https://lh3.googleusercontent.com/eVSv6_WgUH5x1e4zT98LPSVBgpro1y2cGqGT6c5OyxYSLkCJusAv5-oCPoDxsYULbcwxfHrW4RYMJ4J6BxFfv8iNLORkfEhOJBnZf0ld4Qyse9UIguSD6-W1J9yT822iv5qT8GNj3xR-b8VjCg){width="624"
height="145" loading="lazy"}

# Go deeper, go wider, and achieve more!

Red Hat Ansible Automation Platform on Azure includes an automation
execution environment already tailored for [cloud
automation](/use-cases/hybrid-cloud){rel="noopener"} so you have
everything you need to get started on Azure immediately. Having said
that, a question that often comes up is:  "if I'm using Red Hat Ansible
Automation Platform on Azure, does that mean I can only perform
automation against Azure resources?" The great thing about Ansible
Automation Platform in general is that it doesn't matter where you are
running it from. In the case Red Hat Ansible Automation Platform on
Azure, you are able to automate public cloud, private cloud, physical
and virtual environments, and edge resources.  Obviously, one of the
requirements here is having proper networking connectivity to other
environments. Deploy Red Hat Ansible Automation Platform on Azure, and
automate anywhere!

Often, when people think about the Ansible Automation Platform they
think configuration Management. However, configuration management is
just one of the many use cases that Ansible Automation Platform can
accomplish. So many organizations today take advantage of Ansible
Automation Platform to automate network and security use cases,
integrate into IT Service Management (ITSM) solutions like ServiceNow,
Linux automation, Windows automation, and monitoring and analytics
solutions.  

Additionally, with the aggressive push to application modernization,
many organizations use Ansible Automation Platform to integrate into
their DevOps CI/CD pipelines. Are you using Azure DevOps, Jenkins, or
other CI/CD tools? Cool, have your pipelines at any phase kick off
Ansible Automation Platform automation jobs!  

The automation use cases are endless, and there are so many efficiencies
and savings to be gained by leveraging Ansible Automation Platform, not
to mention the reduction in human errors, and the increased cross-silo
collaboration.
