---
author: Bianca Henderson
date: 2018-07-05 00:00 UTC
description: An overview of Red Hat Ansible Tower Workflow Job
  Templates.
lang: en-us
title: Getting Started with Workflow Job Templates
---

# Getting Started with Workflow Job Templates

[![](https://www.ansible.com/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Getting-Started-with-Tower-Workflows.png)
]{#hs_cos_wrapper_post_body .hs_cos_wrapper .hs_cos_wrapper_meta_field

Welcome to another post in the [Getting
Started](/blog/topic/getting-started) series! Today we're going to get
into the topic of Workflow Job Templates. If you don't know what regular
Job Templates are in Red Hat Ansible Tower, please read the [previously
published](/blog/getting-started-setting-up-an-ansible-job-template)
article that describes them. It'll provide you with some technical
details that'll be a useful jumping-off point for the topic of
workflows.\
\
Once you're familiar with the basics, read on! We'll be covering what
exactly Workflow Job Templates are, what makes them useful, how to
generate/edit one, and a few extra pointers as well as best practices to
make the most out of this great tool.

## What is a Workflow Job Template?

The word "workflow" says it all. This particular feature in Ansible
Tower (available as of version 3.1) enables users to create sequences
consisting of any combination of job templates, project syncs, and
inventory syncs that are linked together in order to execute them as a
single unit. Because of this, workflows can help you organize playbooks
and job templates into separate groups.

## Why are Workflows Useful?

By utilizing this feature, you can set up ordered structures for
different teams to use. For example, two different environments (i.e.,
networking and developers) can interface via workflows as long as they
have permissions to access it. Not everyone involved will need to know
what job run goes after what, since the structure is set up for them by
the user who created the workflow. This connects disparate job types and
unifies projects without each team needing to know everything about what
the other does.\
\
Another reason workflows are useful is because they allow the user to
take any number of playbooks and "daisy chain" them, with the ability to
make a decision tree depending on a job's success or failure. You can
make them as simple or as complex as they need to be!

### How Do You Create One?

[Go into the Templates section on the top menu of Ansible Tower:\
\
![Getting-Started-Tower-Workflows-13](https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-13.jpg?width=1999&name=Getting-Started-Tower-Workflows-13.jpg){width="1999"
style="width: 1999px;"
srcset="https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-13.jpg?width=1000&name=Getting-Started-Tower-Workflows-13.jpg 1000w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-13.jpg?width=1999&name=Getting-Started-Tower-Workflows-13.jpg 1999w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-13.jpg?width=2999&name=Getting-Started-Tower-Workflows-13.jpg 2999w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-13.jpg?width=3998&name=Getting-Started-Tower-Workflows-13.jpg 3998w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-13.jpg?width=4998&name=Getting-Started-Tower-Workflows-13.jpg 4998w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-13.jpg?width=5997&name=Getting-Started-Tower-Workflows-13.jpg 5997w"
sizes="(max-width: 1999px) 100vw, 1999px"}\
]{style="background-color: transparent;"}

From there, click on "Add", but make sure to select "Workflow Template":

![Getting-Started-Tower-Workflows-15](https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-15.jpg?width=1999&name=Getting-Started-Tower-Workflows-15.jpg){width="1999"
style="width: 1999px;"
srcset="https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-15.jpg?width=1000&name=Getting-Started-Tower-Workflows-15.jpg 1000w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-15.jpg?width=1999&name=Getting-Started-Tower-Workflows-15.jpg 1999w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-15.jpg?width=2999&name=Getting-Started-Tower-Workflows-15.jpg 2999w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-15.jpg?width=3998&name=Getting-Started-Tower-Workflows-15.jpg 3998w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-15.jpg?width=4998&name=Getting-Started-Tower-Workflows-15.jpg 4998w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-15.jpg?width=5997&name=Getting-Started-Tower-Workflows-15.jpg 5997w"
sizes="(max-width: 1999px) 100vw, 1999px"}

You'll see this new screen, where you can name your workflow template
anything you like and save it:

![Getting-Started-Tower-Workflows-10](https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-10.jpg?width=1999&name=Getting-Started-Tower-Workflows-10.jpg){width="1999"
style="width: 1999px;"
srcset="https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-10.jpg?width=1000&name=Getting-Started-Tower-Workflows-10.jpg 1000w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-10.jpg?width=1999&name=Getting-Started-Tower-Workflows-10.jpg 1999w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-10.jpg?width=2999&name=Getting-Started-Tower-Workflows-10.jpg 2999w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-10.jpg?width=3998&name=Getting-Started-Tower-Workflows-10.jpg 3998w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-10.jpg?width=4998&name=Getting-Started-Tower-Workflows-10.jpg 4998w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-10.jpg?width=5997&name=Getting-Started-Tower-Workflows-10.jpg 5997w"
sizes="(max-width: 1999px) 100vw, 1999px"}

Once you've done that, go into "Edit Workflow":

![Getting-Started-Tower-Workflows-1](https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-1.jpg?width=1999&name=Getting-Started-Tower-Workflows-1.jpg){width="1999"
style="width: 1999px;"
srcset="https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-1.jpg?width=1000&name=Getting-Started-Tower-Workflows-1.jpg 1000w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-1.jpg?width=1999&name=Getting-Started-Tower-Workflows-1.jpg 1999w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-1.jpg?width=2999&name=Getting-Started-Tower-Workflows-1.jpg 2999w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-1.jpg?width=3998&name=Getting-Started-Tower-Workflows-1.jpg 3998w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-1.jpg?width=4998&name=Getting-Started-Tower-Workflows-1.jpg 4998w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-1.jpg?width=5997&name=Getting-Started-Tower-Workflows-1.jpg 5997w"
sizes="(max-width: 1999px) 100vw, 1999px"}

This screen will come up, where you can add different job templates and
make sure they run on failure, success, or with either outcome:

![Getting-Started-Tower-Workflows-11](https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-11.jpg?width=1999&name=Getting-Started-Tower-Workflows-11.jpg){width="1999"
style="width: 1999px;"
srcset="https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-11.jpg?width=1000&name=Getting-Started-Tower-Workflows-11.jpg 1000w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-11.jpg?width=1999&name=Getting-Started-Tower-Workflows-11.jpg 1999w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-11.jpg?width=2999&name=Getting-Started-Tower-Workflows-11.jpg 2999w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-11.jpg?width=3998&name=Getting-Started-Tower-Workflows-11.jpg 3998w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-11.jpg?width=4998&name=Getting-Started-Tower-Workflows-11.jpg 4998w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-11.jpg?width=5997&name=Getting-Started-Tower-Workflows-11.jpg 5997w"
sizes="(max-width: 1999px) 100vw, 1999px"}

Note that you can decide if things run on success, on failure, or
always.

[**![Getting-Started-Tower-Workflows-9](https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-9.jpg?width=183&name=Getting-Started-Tower-Workflows-9.jpg){width="183"
style="width: 183px;"
srcset="https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-9.jpg?width=92&name=Getting-Started-Tower-Workflows-9.jpg 92w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-9.jpg?width=183&name=Getting-Started-Tower-Workflows-9.jpg 183w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-9.jpg?width=275&name=Getting-Started-Tower-Workflows-9.jpg 275w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-9.jpg?width=366&name=Getting-Started-Tower-Workflows-9.jpg 366w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-9.jpg?width=458&name=Getting-Started-Tower-Workflows-9.jpg 458w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-9.jpg?width=549&name=Getting-Started-Tower-Workflows-9.jpg 549w"
sizes="(max-width: 183px) 100vw, 183px"}**]{style="font-size: 11px; color: #808080;"}

As mentioned in the previous section, you can make your Ansible workflow
as simple\...

![Getting-Started-Tower-Workflows-4](https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-4.jpg?width=1542&name=Getting-Started-Tower-Workflows-4.jpg){width="1542"
style="width: 1542px;"
srcset="https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-4.jpg?width=771&name=Getting-Started-Tower-Workflows-4.jpg 771w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-4.jpg?width=1542&name=Getting-Started-Tower-Workflows-4.jpg 1542w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-4.jpg?width=2313&name=Getting-Started-Tower-Workflows-4.jpg 2313w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-4.jpg?width=3084&name=Getting-Started-Tower-Workflows-4.jpg 3084w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-4.jpg?width=3855&name=Getting-Started-Tower-Workflows-4.jpg 3855w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-4.jpg?width=4626&name=Getting-Started-Tower-Workflows-4.jpg 4626w"
sizes="(max-width: 1542px) 100vw, 1542px"}

\...or complex as you need to!

![Getting-Started-Tower-Workflows-12](https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-12.jpg?width=1541&name=Getting-Started-Tower-Workflows-12.jpg){width="1541"
style="width: 1541px;"
srcset="https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-12.jpg?width=771&name=Getting-Started-Tower-Workflows-12.jpg 771w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-12.jpg?width=1541&name=Getting-Started-Tower-Workflows-12.jpg 1541w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-12.jpg?width=2312&name=Getting-Started-Tower-Workflows-12.jpg 2312w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-12.jpg?width=3082&name=Getting-Started-Tower-Workflows-12.jpg 3082w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-12.jpg?width=3853&name=Getting-Started-Tower-Workflows-12.jpg 3853w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-12.jpg?width=4623&name=Getting-Started-Tower-Workflows-12.jpg 4623w"
sizes="(max-width: 1541px) 100vw, 1541px"}

After everything is set and saved, you're ready to launch your template,
which you can do by clicking on the rocket icon next to the workflow
you'd like to run:

![Getting-Started-Tower-Workflows-7](https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-7.jpg?width=1999&name=Getting-Started-Tower-Workflows-7.jpg){width="1999"
style="width: 1999px;"
srcset="https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-7.jpg?width=1000&name=Getting-Started-Tower-Workflows-7.jpg 1000w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-7.jpg?width=1999&name=Getting-Started-Tower-Workflows-7.jpg 1999w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-7.jpg?width=2999&name=Getting-Started-Tower-Workflows-7.jpg 2999w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-7.jpg?width=3998&name=Getting-Started-Tower-Workflows-7.jpg 3998w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-7.jpg?width=4998&name=Getting-Started-Tower-Workflows-7.jpg 4998w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-7.jpg?width=5997&name=Getting-Started-Tower-Workflows-7.jpg 5997w"
sizes="(max-width: 1999px) 100vw, 1999px"}

### What More Can You Do With Workflows?

You can [schedule your
workflows](https://docs.ansible.com/ansible-tower/latest/html/userguide/workflow_templates.html#scheduling)
to run when you need them to! Just click on the calendar icon next to
any workflow job template:

![Getting-Started-Tower-Workflows-5](https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-5.jpg?width=1328&name=Getting-Started-Tower-Workflows-5.jpg){width="1328"
style="width: 1328px;"
srcset="https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-5.jpg?width=664&name=Getting-Started-Tower-Workflows-5.jpg 664w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-5.jpg?width=1328&name=Getting-Started-Tower-Workflows-5.jpg 1328w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-5.jpg?width=1992&name=Getting-Started-Tower-Workflows-5.jpg 1992w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-5.jpg?width=2656&name=Getting-Started-Tower-Workflows-5.jpg 2656w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-5.jpg?width=3320&name=Getting-Started-Tower-Workflows-5.jpg 3320w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-5.jpg?width=3984&name=Getting-Started-Tower-Workflows-5.jpg 3984w"
sizes="(max-width: 1328px) 100vw, 1328px"}

\... and fill out the information for when you want the specified
workflow to automatically run:

![Getting-Started-Tower-Workflows-8](https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-8.jpg?width=1329&name=Getting-Started-Tower-Workflows-8.jpg){width="1329"
style="width: 1329px;"
srcset="https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-8.jpg?width=665&name=Getting-Started-Tower-Workflows-8.jpg 665w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-8.jpg?width=1329&name=Getting-Started-Tower-Workflows-8.jpg 1329w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-8.jpg?width=1994&name=Getting-Started-Tower-Workflows-8.jpg 1994w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-8.jpg?width=2658&name=Getting-Started-Tower-Workflows-8.jpg 2658w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-8.jpg?width=3323&name=Getting-Started-Tower-Workflows-8.jpg 3323w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-8.jpg?width=3987&name=Getting-Started-Tower-Workflows-8.jpg 3987w"
sizes="(max-width: 1329px) 100vw, 1329px"}\
 

If you have a workflow template created that works very well for you and
you'd like to copy it, click on the button highlighted below:

![Getting-Started-Tower-Workflows-2](https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-2.jpg?width=1311&name=Getting-Started-Tower-Workflows-2.jpg){width="1311"
style="width: 1311px;"
srcset="https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-2.jpg?width=656&name=Getting-Started-Tower-Workflows-2.jpg 656w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-2.jpg?width=1311&name=Getting-Started-Tower-Workflows-2.jpg 1311w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-2.jpg?width=1967&name=Getting-Started-Tower-Workflows-2.jpg 1967w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-2.jpg?width=2622&name=Getting-Started-Tower-Workflows-2.jpg 2622w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-2.jpg?width=3278&name=Getting-Started-Tower-Workflows-2.jpg 3278w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-2.jpg?width=3933&name=Getting-Started-Tower-Workflows-2.jpg 3933w"
sizes="(max-width: 1311px) 100vw, 1311px"}

Keep in mind that copying a workflow won't also copy over any of the
permissions, notifications, or schedules associated with the original.\
\
If you need to set extra variables for the playbooks involved in a
workflow template and/or allow for authorization of user input, then
[setting up
surveys](https://docs.ansible.com/ansible-tower/latest/html/userguide/workflow_templates.html#surveys)
is the way to go. In order to set one up, select a workflow template and
click on the "Add Survey" button:\
\

![Getting-Started-Tower-Workflows-3](https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-3.jpg?width=1330&name=Getting-Started-Tower-Workflows-3.jpg){width="1330"
style="width: 1330px;"
srcset="https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-3.jpg?width=665&name=Getting-Started-Tower-Workflows-3.jpg 665w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-3.jpg?width=1330&name=Getting-Started-Tower-Workflows-3.jpg 1330w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-3.jpg?width=1995&name=Getting-Started-Tower-Workflows-3.jpg 1995w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-3.jpg?width=2660&name=Getting-Started-Tower-Workflows-3.jpg 2660w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-3.jpg?width=3325&name=Getting-Started-Tower-Workflows-3.jpg 3325w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-3.jpg?width=3990&name=Getting-Started-Tower-Workflows-3.jpg 3990w"
sizes="(max-width: 1330px) 100vw, 1330px"}

A survey screen that you can fill out with specific questions and answer
types will show up:

![Getting-Started-Tower-Workflows-14](https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-14.jpg?width=1198&name=Getting-Started-Tower-Workflows-14.jpg){width="1198"
style="width: 1198px;"
srcset="https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-14.jpg?width=599&name=Getting-Started-Tower-Workflows-14.jpg 599w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-14.jpg?width=1198&name=Getting-Started-Tower-Workflows-14.jpg 1198w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-14.jpg?width=1797&name=Getting-Started-Tower-Workflows-14.jpg 1797w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-14.jpg?width=2396&name=Getting-Started-Tower-Workflows-14.jpg 2396w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-14.jpg?width=2995&name=Getting-Started-Tower-Workflows-14.jpg 2995w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-14.jpg?width=3594&name=Getting-Started-Tower-Workflows-14.jpg 3594w"
sizes="(max-width: 1198px) 100vw, 1198px"}

[Notifications](https://docs.ansible.com/ansible-tower/latest/html/userguide/workflow_templates.html#work-with-notifications)
can give you more control and knowledge related to specific workflows.
To activate one, select the workflow that you want to set notifications
for, then click the Notifications button:

![Getting-Started-Tower-Workflows-16](https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-16.jpg?width=1329&name=Getting-Started-Tower-Workflows-16.jpg){width="1329"
style="width: 1329px;"
srcset="https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-16.jpg?width=665&name=Getting-Started-Tower-Workflows-16.jpg 665w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-16.jpg?width=1329&name=Getting-Started-Tower-Workflows-16.jpg 1329w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-16.jpg?width=1994&name=Getting-Started-Tower-Workflows-16.jpg 1994w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-16.jpg?width=2658&name=Getting-Started-Tower-Workflows-16.jpg 2658w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-16.jpg?width=3323&name=Getting-Started-Tower-Workflows-16.jpg 3323w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-16.jpg?width=3987&name=Getting-Started-Tower-Workflows-16.jpg 3987w"
sizes="(max-width: 1329px) 100vw, 1329px"}

Keep in mind that you'll have to already have some notifications set up
in the Notifications list. The screen that comes up will enable you to
select specific notifications; in the example below the
"Workflow-Specific Notification" has been set to activate on either a
successful or failed run:

![Getting-Started-Tower-Workflows-6](https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-6.jpg?width=1303&name=Getting-Started-Tower-Workflows-6.jpg){width="1303"
style="width: 1303px;"
srcset="https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-6.jpg?width=652&name=Getting-Started-Tower-Workflows-6.jpg 652w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-6.jpg?width=1303&name=Getting-Started-Tower-Workflows-6.jpg 1303w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-6.jpg?width=1955&name=Getting-Started-Tower-Workflows-6.jpg 1955w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-6.jpg?width=2606&name=Getting-Started-Tower-Workflows-6.jpg 2606w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-6.jpg?width=3258&name=Getting-Started-Tower-Workflows-6.jpg 3258w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/Tower-Insights-Screens/Tower-Workflow-Screens/Getting-Started-Tower-Workflows-6.jpg?width=3909&name=Getting-Started-Tower-Workflows-6.jpg 3909w"
sizes="(max-width: 1303px) 100vw, 1303px"}

[**[Note: Make sure you have "update on launch" on your inventory
selected when you make a new workflow job template if you're acting
against a dynamic
inventory!]{style="color: #808080;"}**]{style="font-size: 11px;"}

### Conclusion

Now you know how to combine any number of playbooks into a customized
decision tree, with the ability to schedule those jobs, add
notifications, and much more. An added bonus is the fact that this isn't
an enterprise-only feature, so no matter your Ansible Tower license
type, you can log into your instance and have fun creating workflows!

To read more about how to create and modify workflow job templates,
check out our [official documentation
page](https://docs.ansible.com/ansible-tower/latest/html/userguide/workflow_templates.html)
on the topic. There is also an [on-demand
webinar](/resources/webinars-training/ansible-tower-basics-workflows)
that can provide additional information.

I hope this article was helpful, and that it enables you to take
advantage of the powerful automation features that are possible with
Ansible Tower!
