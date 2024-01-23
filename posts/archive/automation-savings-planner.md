---
author: Roger Lopez
date: 2021-06-14 00:00 UTC
description: Pre-plan your automation savings with Red Hat Insights for
  Red Hat Ansible Automation Platform.
lang: en-us
title: Automation Savings Planner
---

# Automation Savings Planner

Enterprise organizations understand that to be leaders in their
industries, they must change the way they deliver applications, improve
their relationships with customers and gain competitive advantages.

Positioning those advantages to have a positive return on investment
often starts with proper planning and automation.
But what does proper planning of your automation even look like?

For some enterprises, proper planning includes reducing automation
costs. For others, it's reducing time spent to open new opportunities.

With this in mind, Red Hat is excited to introduce Automation Savings
Planner, a new enhancement that puts
automation planning in the forefront within the hosted services on
*console.redhat.com*.

The Automation Savings Planner is designed to provide a one stop shop to
plan, track and analyze potential efficiency improvements and cost
savings of your automation initiatives.

## How does it work?

Users can create an automation savings plan within Automation Analytics
accessible at [cloud.redhat.com](https://cloud.redhat.com) by defining how long and often the work is done
manually, as well as a list of tasks needed to successfully automate
this job.

Once defined, you can integrate your newly automated savings plans to
automation controller's job templates to help accurately detect if the
automation is successfully running across your infrastructure. You can
also view projected cost and time savings from automating the job over
time.

With these enhancements, you get a detailed overview on how to optimize
and prioritize the various automation jobs throughout your organization,
based on time and money saved. This allows you to decide what things are
most important to automate first.

## Ready to start saving? Let's get started!

The first step is to create an automation savings plan that defines the
tasks needed to complete an automation job. 

First in the side navigation in Automation Analytics, select the
**Savings Planner** navigation item. Then, click on the blue button
labeled **Add plan**.

![ROI blog one](/images/posts/archive/roi-blog-one.png)

Within the **Create new plan** section, fill out the details for the
task you want to automate. The questions include:

-   What do you want to automate? (e.g., Provision an Apache server)
-   What type of task is it? (e.g., Operating System)
-   A description of your automation plan
-   How long does the process take to complete manually? (e.g., 4 hours)
-   How many hosts do you plan to run the automation on? (e.g., 1)
-   How often do you plan to run the automation? (e.g., weekly)

![ROI blog two](/images/posts/archive/roi-blog-two.png)

Once you've completed the **Details** section, select the blue **Next**
button on the lower left pane of the window.

Within the **Tasks** section, list out all the tasks that are needed to
complete this plan. Write out each task and select the (+) to add it to
your **Tasks** list. 

For example, if we were looking to successfully install an Apache web
server, we'd likely include tasks such as:

-   Install Apache package
-   Start HTTPD service
-   Enable HTTPD service
-   Enable firewall port 80
-   Configure VirtualHost
-   Secure Apache web server

![ROI blog three](/images/posts/archive/roi-blog-three.png)

Once you've completed the **Tasks** section for your specific plan,
select **Next**. 

**NOTE:** These tasks are for your planning purposes, and do not
currently factor into the savings estimates provided by Automation
Analytics.

Lastly, within the **Link template** section, select the appropriate
template to link to this plan and click **Save**. 

Once saved, you can view the newly created plan details. 

![ROI blog four](/images/posts/archive/roi-blog-four.png)

In this **Details** view you will find a summary of all the options
created and selected for your plan. 

If you notice something is amiss, you can easily make changes to your
plan using the **Edit** button located at the bottom left corner of the
**Details** section. 

## And that's it!

With this newly created plan we can use Automation Savings Planner to
share a projection of how much time and money you could save by
automating a specific job. Automation Analytics takes data from the plan
details and the associated job template to provide you with an accurate
projection of your cost savings when you complete this savings plan.

## Where can I find these stats?

Simply navigate to your Automation Savings Planner page, click on the
name of an existing plan and navigate to the **Statistics** tab. You can
also get to this screen by clicking the "Projected Savings" links in the
card-based list of savings plans.

The statistics chart displays a projection of your monetary and time
savings based on the information you provided when creating a savings
plan. Primarily, the statistics chart subtracts the automated cost from
the manual cost of executing the plan to provide the total resources
saved through automation. The chart then displays this data by year to
show you the cumulative benefits for automating the plan over time.

Click between **Money** and **Time** to view the different types of
savings for automating the plan. An example is shown below.

![ROI blog five](/images/posts/archive/roi-blog-five.png)

##  How are the Money and Time values determined?

Risk-adjusted factors are used to create a 3-year model projection of
costs and savings related to automation. The objective is to provide as
accurate a representation of cost and savings as possible but understand
that actual values may differ in practice.

The following information breaks down:

-   where we get the data
-   the risk-adjustment factors we use
-   the assumptions we make
-   the formula used to compute the values as displayed in the chart

The cost portion of the formula includes hours spent in

-   Implementation
-   Deployment
-   Training
-   Other expenditures for creating, maintaining & running the automation

The hours (cost of investment) are typically higher on the onset and are
greatly reduced once the automation has been created and only
maintenance is required. 

For the initial period (including the first year), the formula uses the
following variables for its calculation.

- TIME - time for manual run on one host (in hours) multiplied by 10
- BufferTime -extra time for unforeseen and unaccounted delays and familiarization with requirements
- RISK - a 40% risk adjustment¹ is applied for unforeseen situations

The formula for the initial period and first year is represented as
follows:

```
C1 = TIME + BufferTime

C2 = C1 * RISK

initial cost = (C1 + C2) * COST

year 1 cost = (C1 + C2) * COST²
```



The next two years after the first year, the formula uses the following
variables for its calculation. 

- TIME - time for manual run on one host (in hours) multiplied by 4
- RISK - a 40% risk adjustment¹ to account for unforeseen situations

The formula for the next two years is represented as follows:

```
C1 = TIME

C2 = C1 * RISK

year 2 cost = (C1 + C2) * COST²

year 3 cost = (C1 + C2) * COST²
```

With the details on how cost is calculated for the plan, let's talk about savings.

The savings indicates the time and money saved as a result of automating the plan. 

A 50% productivity recapture rate is taken to account for the
productivity that is gained by repeated manual implementation of a task
over a period of time. Included is a -5% risk adjustment for unforeseen
situations that may arise and need to be handled.

A savings growth rate of 15% year over year is used. 

The initial period of money savings results in $0. As such no formula
is necessary for that period. 

The formula to calculate savings for the initial period is shown below:

```
Initial period of Savings = $0 - initialCost

The  formula used for savings for year one are:

S1 = (HOSTS * (TIME/60) * FREQUENCY)

S2 = S1 * RECAPTURE

S3 = S2 * RISK * COST²

Year One Savings = S2 - S3 - Year One Cost
```

HOSTS - number of hosts
TIME - manual time in minutes
FREQUENCY - yearly frequency of automation
RECAPTURE - 50% productivity recapture
RISK - 5% Risk Adjustment

The formula used to capture savings for year two:

```
S1 = Year One Savings * GROWTH

Year Two Savings = Year One Savings  + S1 - Year 2 Cost

GROWTH - 15% Growth

The formula used to capture savings for year three:

S2 = Year Two Savings * GROWTH

Year Three Savings = Year Two Savings + S2 -Year 2 Cost
```

And there you have it! The inner workings of how money and savings are
calculated to give you the projected savings of automating tasks your
organization is currently doing manually.

By using Automation Savings Planner, enterprise organizations can gain
competitive advantages and a positive return on their investments by
automating key elements of their business. This not only saves time and
money, but allows businesses to expand their automation capabilities to
deliver applications, meet expectations and improve their relationships
with their customers. 

¹ [A Forrester Total Economic Impact™ Study](https://www.redhat.com/rhdc/managed-files/ma-forrester-ansible-economic-impact-analyst-paper-f13019bf-201808-en_0.pdf)

² Cost per hour in USD if applicable, based on display.
