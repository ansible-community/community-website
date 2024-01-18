---
author: Craig Brandt
date: 2023-06-26 00:00 UTC
description: An overview of what to expect with the technology preview
  of Ansible Lightspeed with IBM Watson Code Assistant, a new generative
  AI service available now.
lang: en-us
title: Welcome to the Ansible Lightspeed with IBM Watson Code Assistant Technical Preview
---

# Welcome to the Ansible Lightspeed with IBM Watson Code Assistant Technical Preview

At Red Hat Summit and AnsibleFest 2023, we [announced Ansible
Lightspeed with IBM Watson Code
Assistant](https://www.redhat.com/en/about/press-releases/red-hat-introduces-ansible-lightspeed-ai-driven-it-automation), a new generative AI service for Ansible automation.
Today, we are thrilled to announce the Ansible Lightspeed technical
preview launch.\
\
[In this blog, we'll walk through the steps to access the Ansible
Lightspeed with IBM Watson Code Assistant technical preview service and
get it up and running in your Visual Studio Code environment. Then we'll
share more about what you can expect from the experience and how to
generate your first Ansible tasks with generative
AI.]{style="color: #000000;"}]{style="color: #444444;"}

[This is exciting stuff, so let's dive right
in.]{style="color: #000000;"}

## Technical Preview: Empowering Ansible Users with AI

[Ansible Lightspeed with IBM Watson Code Assistant is a purpose-built
generative AI tool that aims to streamline the creation of Ansible
content. This capability is natively integrated into your VS Code editor
via the [Ansible VS Code
extension](https://marketplace.visualstudio.com/items?itemName=redhat.ansible){style="color: #000000;"}.
The AI capabilities are powered by Watson Code Assistant, a foundation
model trained on Ansible Galaxy, GitHub, and other open sources of
data.]{style="color: #000000;"}

[The technical preview is open and available, free of charge, to all
Ansible users. As more users engage with Ansible Lightspeed, the model
recommendations will continuously improve, thanks to the valuable input
and engagement from the community.]{style="color: #000000;"}

## Getting Connected: Installation and Configuration

You'll need [Visual Studio
Code](https://code.visualstudio.com/download) and Ansible installed on
your workstation and a GitHub account to access the Ansible Lightspeed
service. Let's get started!

-   Install the [Ansible VS Code
    extension](https://marketplace.visualstudio.com/items?itemName=redhat.ansible){rel="noopener"
    target="_blank"} from the Visual Studio Code Marketplace by
    searching for \"*ansible*\" and selecting the extension published by
    Red Hat.
-   Enable the Ansible Lightspeed service within the extension by
    accessing the \"*Extension Settings*\" via the gear icon.
-   In the settings, enable both \"*Ansible Lightspeed enabled*\" and
    \"*Enable Ansible Lightspeed with Watson Code Assistant inline
    suggestions*\" checkboxes.

[[Note: You can enable Ansible Lightspeed in the
"[User]{style="background-color: transparent; font-family: RedHatText, Overpass, sans-serif;"}"
or
"[Workspace]{style="background-color: transparent; font-family: RedHatText, Overpass, sans-serif;"}]{style="color: #000000;"}[["
settings, based on your preference. More information on VS Code User and
Workspace settings can be found in their]{style="color: #000000;"}
]{style="color: #666666;"}]{style="font-style: italic;"}[documentation](https://code.visualstudio.com/docs/getstarted/settings#){style="font-family: RedHatText, Overpass, sans-serif; font-style: italic;"
rel="noopener"
target="_blank"}[.]{style="background-color: transparent; color: #333333; font-family: RedHatText, Overpass, sans-serif; font-style: italic;"}

![](https://www.ansible.com/hs-fs/hubfs/Google%20Drive%20Integration/WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch-Jun-23-2023-03-51-57-8383-PM.gif?width=1466&height=892&name=WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch-Jun-23-2023-03-51-57-8383-PM.gif){style="margin-left: 0.00px;"
width="1466" height="892" loading="lazy"
srcset="https://www.ansible.com/hs-fs/hubfs/Google%20Drive%20Integration/WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch-Jun-23-2023-03-51-57-8383-PM.gif?width=733&height=446&name=WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch-Jun-23-2023-03-51-57-8383-PM.gif 733w, https://www.ansible.com/hs-fs/hubfs/Google%20Drive%20Integration/WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch-Jun-23-2023-03-51-57-8383-PM.gif?width=1466&height=892&name=WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch-Jun-23-2023-03-51-57-8383-PM.gif 1466w, https://www.ansible.com/hs-fs/hubfs/Google%20Drive%20Integration/WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch-Jun-23-2023-03-51-57-8383-PM.gif?width=2199&height=1338&name=WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch-Jun-23-2023-03-51-57-8383-PM.gif 2199w, https://www.ansible.com/hs-fs/hubfs/Google%20Drive%20Integration/WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch-Jun-23-2023-03-51-57-8383-PM.gif?width=2932&height=1784&name=WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch-Jun-23-2023-03-51-57-8383-PM.gif 2932w, https://www.ansible.com/hs-fs/hubfs/Google%20Drive%20Integration/WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch-Jun-23-2023-03-51-57-8383-PM.gif?width=3665&height=2230&name=WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch-Jun-23-2023-03-51-57-8383-PM.gif 3665w, https://www.ansible.com/hs-fs/hubfs/Google%20Drive%20Integration/WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch-Jun-23-2023-03-51-57-8383-PM.gif?width=4398&height=2676&name=WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch-Jun-23-2023-03-51-57-8383-PM.gif 4398w"
sizes="(max-width: 1466px) 100vw, 1466px"}[*Installing the Ansible
Visual Studio Code extension.*]{style="font-size: 12px;"}

-   Click on the Ansible \"A\" in the VS Code activity bar on the
    left-hand side of your editor to open the extension.
-   Click \"*Connect*\" and follow the prompts to log into GitHub using
    your credentials.

![](https://www.ansible.com/hs-fs/hubfs/Google%20Drive%20Integration/WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch-3.gif?width=1466&height=892&name=WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch-3.gif){width="1466"
height="892" loading="lazy"
srcset="https://www.ansible.com/hs-fs/hubfs/Google%20Drive%20Integration/WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch-3.gif?width=733&height=446&name=WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch-3.gif 733w, https://www.ansible.com/hs-fs/hubfs/Google%20Drive%20Integration/WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch-3.gif?width=1466&height=892&name=WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch-3.gif 1466w, https://www.ansible.com/hs-fs/hubfs/Google%20Drive%20Integration/WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch-3.gif?width=2199&height=1338&name=WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch-3.gif 2199w, https://www.ansible.com/hs-fs/hubfs/Google%20Drive%20Integration/WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch-3.gif?width=2932&height=1784&name=WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch-3.gif 2932w, https://www.ansible.com/hs-fs/hubfs/Google%20Drive%20Integration/WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch-3.gif?width=3665&height=2230&name=WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch-3.gif 3665w, https://www.ansible.com/hs-fs/hubfs/Google%20Drive%20Integration/WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch-3.gif?width=4398&height=2676&name=WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch-3.gif 4398w"
sizes="(max-width: 1466px) 100vw, 1466px"}*[Log in using your GitHub
credentials.]{style="font-size: 12px;"}*

-   Read the Ansible Lightspeed technical preview terms and conditions
    and click "*Agree*".
-   Next, authorize Ansible Lightspeed for VS Code by clicking
    "*Authorize*".
-   Follow the browser prompts to redirect you back to VS Code, and,
    finally, click "*Open*" in the VS Code confirmation dialog box.

![](https://www.ansible.com/hs-fs/hubfs/Google%20Drive%20Integration/WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch-4.gif?width=1466&height=892&name=WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch-4.gif){style="float: left;"
width="1466" height="892" loading="lazy"
srcset="https://www.ansible.com/hs-fs/hubfs/Google%20Drive%20Integration/WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch-4.gif?width=733&height=446&name=WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch-4.gif 733w, https://www.ansible.com/hs-fs/hubfs/Google%20Drive%20Integration/WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch-4.gif?width=1466&height=892&name=WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch-4.gif 1466w, https://www.ansible.com/hs-fs/hubfs/Google%20Drive%20Integration/WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch-4.gif?width=2199&height=1338&name=WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch-4.gif 2199w, https://www.ansible.com/hs-fs/hubfs/Google%20Drive%20Integration/WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch-4.gif?width=2932&height=1784&name=WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch-4.gif 2932w, https://www.ansible.com/hs-fs/hubfs/Google%20Drive%20Integration/WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch-4.gif?width=3665&height=2230&name=WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch-4.gif 3665w, https://www.ansible.com/hs-fs/hubfs/Google%20Drive%20Integration/WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch-4.gif?width=4398&height=2676&name=WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch-4.gif 4398w"
sizes="(max-width: 1466px) 100vw, 1466px"}\
[*Authorize Ansible Lightspeed.*]{style="font-size: 12px;"}**\
**

Congratulations! You've successfully configured Ansible Lightspeed in VS
Code.

You can confirm that Ansible Lightspeed is enabled by checking the VS
Code status bar at the bottom of the editor window.

Please ensure a Python environment is selected and your Ansible YAML
files are associated with the Ansible language. More information on VS
Code languages can be found in their
[documentation](https://code.visualstudio.com/docs/languages/overview#_change-the-language-for-the-selected-file){rel="noopener"
target="_blank"}.

![](https://www.ansible.com/hubfs/Google%20Drive%20Integration/WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch.png){style="margin-left: 0.00px;"
loading="lazy"}[*Ansible Lightspeed status.*]{style="font-size: 12px;"}

## A Quick Tour of Ansible Lightspeed: Generating Your First Task

Now that you are connected to Ansible Lightspeed, it\'s time to
experience its AI-enhanced content creation experience.

Let's use an
[example](https://github.com/craig-br/demos/blob/main/blogs/lightspeed_tech_preview_jun2023/deploy_monitoring.yml)[ Playbook](https://github.com/craig-br/demos/blob/main/blogs/lightspeed_tech_preview_jun2023/deploy_monitoring.yml){rel="noopener"
target="_blank"} to walk through asking Ansible Lightspeed for
AI-generated task suggestions and also highlight some of what you can
expect in the technical preview release. The example Playbook installs
[Cockpit](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html-single/managing_systems_using_the_rhel_9_web_console/index){rel="noopener"
target="_blank"} on a Red Hat Enterprise Linux system.

[*[Note: As more users engage with Ansible Lightspeed, the breadth,
depth, and quality of the recommendations generated by the model will
improve. Therefore, the Ansible task suggestions in the examples below
may differ from your
results.]{style="font-size: 18px;"}*]{style="color: #000000;"}[\
]{style="font-size: 10px;"}

## How do I generate an Ansible Lightspeed suggestion?

Let's use our first Playbook task in the
[deploy_monitoring.yml](https://github.com/craig-br/demos/blob/main/blogs/lightspeed_tech_preview_jun2023/deploy_monitoring.yml){rel="noopener"
target="_blank"} example Playbook to demonstrate asking Ansible
Lightspeed for an AI suggestion.

-   Move your cursor to the end of the  "*- name: Include
    redhat.rhel_system_roles.cockpit" task description.*
-   Press \"ENTER\" to generate a suggestion.
-   Press \"TAB\" to accept the suggestion.

![](https://www.ansible.com/hs-fs/hubfs/Google%20Drive%20Integration/WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch.gif?width=1466&height=892&name=WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch.gif){style="margin-left: 0.00px;"
width="1466" height="892" loading="lazy"
srcset="https://www.ansible.com/hs-fs/hubfs/Google%20Drive%20Integration/WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch.gif?width=733&height=446&name=WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch.gif 733w, https://www.ansible.com/hs-fs/hubfs/Google%20Drive%20Integration/WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch.gif?width=1466&height=892&name=WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch.gif 1466w, https://www.ansible.com/hs-fs/hubfs/Google%20Drive%20Integration/WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch.gif?width=2199&height=1338&name=WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch.gif 2199w, https://www.ansible.com/hs-fs/hubfs/Google%20Drive%20Integration/WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch.gif?width=2932&height=1784&name=WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch.gif 2932w, https://www.ansible.com/hs-fs/hubfs/Google%20Drive%20Integration/WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch.gif?width=3665&height=2230&name=WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch.gif 3665w, https://www.ansible.com/hs-fs/hubfs/Google%20Drive%20Integration/WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch.gif?width=4398&height=2676&name=WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch.gif 4398w"
sizes="(max-width: 1466px) 100vw, 1466px"}*Generating an Ansible task.*

In this suggestion, we asked Ansible Lightspeed to include the
"*cockpit*" Role, part of the  [Red Hat Enterprise Linux System
Roles](https://access.redhat.com/articles/3050101){rel="noopener"
target="_blank"} Certified Content Collection. The suggestion used the
[Fully Qualified Collection
Name](https://docs.ansible.com/ansible/latest/collections_guide/collections_using_playbooks.html){rel="noopener"
target="_blank"} (FQCN) -
"[ansible.builtin.include_role](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/include_role_module.html){rel="noopener"
target="_blank"}".

Using FQCNs is a [recommended best
practice](https://docs.ansible.com/ansible/latest/porting_guides/porting_guide_2.10.html){rel="noopener"
target="_blank"} and an example of the many unique post-processing
capabilities we've baked into the Ansible Lightspeed service.

Let's move on to the next task.

## Ansible best practices. We've got you covered.

![](https://www.ansible.com/hs-fs/hubfs/Google%20Drive%20Integration/WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch-2.gif?width=1466&height=892&name=WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch-2.gif){style="margin-left: 0.00px;"
width="1466" height="892" loading="lazy"
srcset="https://www.ansible.com/hs-fs/hubfs/Google%20Drive%20Integration/WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch-2.gif?width=733&height=446&name=WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch-2.gif 733w, https://www.ansible.com/hs-fs/hubfs/Google%20Drive%20Integration/WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch-2.gif?width=1466&height=892&name=WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch-2.gif 1466w, https://www.ansible.com/hs-fs/hubfs/Google%20Drive%20Integration/WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch-2.gif?width=2199&height=1338&name=WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch-2.gif 2199w, https://www.ansible.com/hs-fs/hubfs/Google%20Drive%20Integration/WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch-2.gif?width=2932&height=1784&name=WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch-2.gif 2932w, https://www.ansible.com/hs-fs/hubfs/Google%20Drive%20Integration/WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch-2.gif?width=3665&height=2230&name=WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch-2.gif 3665w, https://www.ansible.com/hs-fs/hubfs/Google%20Drive%20Integration/WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch-2.gif?width=4398&height=2676&name=WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch-2.gif 4398w"
sizes="(max-width: 1466px) 100vw, 1466px"}[*Ansible Lightspeed best
practices example.*]{style="font-size: 12px;"}[\
]{style="font-size: 10px;"}

This Playbook task copies
[cockpit.conf](https://github.com/craig-br/demos/blob/main/blogs/lightspeed_tech_preview_jun2023/files/cockpit.conf){rel="noopener"
target="_blank"} to the target host. Note that the recommendation
included the "*mode:*" module argument and set the Linux file
permissions to "0*644*".

Ansible Lightspeed provided a robust example of setting file permissions
for the
[ansible.builtin.copy](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/copy_module.html){rel="noopener"
target="_blank"} module, another recommended best practice.

We'll continue to expand on these natively integrated best practices as
the service matures.

## Finalizing the Playbook

Let's ask Ansible Lightspeed to generate suggestions for the remaining
two Playbook tasks. The first task restarts the Cockpit service to apply
our custom
[cockpit.conf](https://github.com/craig-br/demos/blob/main/blogs/lightspeed_tech_preview_jun2023/files/cockpit.conf){rel="noopener"
target="_blank" style="font-style: normal;"} configuration file and the
second task permits Cockpit service traffic through the firewall.

![](https://www.ansible.com/hs-fs/hubfs/Google%20Drive%20Integration/WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch-Jun-23-2023-03-51-58-2032-PM.gif?width=1466&height=892&name=WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch-Jun-23-2023-03-51-58-2032-PM.gif){style="margin-left: 0.00px;"
width="1466" height="892" loading="lazy"
srcset="https://www.ansible.com/hs-fs/hubfs/Google%20Drive%20Integration/WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch-Jun-23-2023-03-51-58-2032-PM.gif?width=733&height=446&name=WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch-Jun-23-2023-03-51-58-2032-PM.gif 733w, https://www.ansible.com/hs-fs/hubfs/Google%20Drive%20Integration/WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch-Jun-23-2023-03-51-58-2032-PM.gif?width=1466&height=892&name=WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch-Jun-23-2023-03-51-58-2032-PM.gif 1466w, https://www.ansible.com/hs-fs/hubfs/Google%20Drive%20Integration/WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch-Jun-23-2023-03-51-58-2032-PM.gif?width=2199&height=1338&name=WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch-Jun-23-2023-03-51-58-2032-PM.gif 2199w, https://www.ansible.com/hs-fs/hubfs/Google%20Drive%20Integration/WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch-Jun-23-2023-03-51-58-2032-PM.gif?width=2932&height=1784&name=WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch-Jun-23-2023-03-51-58-2032-PM.gif 2932w, https://www.ansible.com/hs-fs/hubfs/Google%20Drive%20Integration/WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch-Jun-23-2023-03-51-58-2032-PM.gif?width=3665&height=2230&name=WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch-Jun-23-2023-03-51-58-2032-PM.gif 3665w, https://www.ansible.com/hs-fs/hubfs/Google%20Drive%20Integration/WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch-Jun-23-2023-03-51-58-2032-PM.gif?width=4398&height=2676&name=WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch-Jun-23-2023-03-51-58-2032-PM.gif 4398w"
sizes="(max-width: 1466px) 100vw, 1466px"}[\
]{style="font-size: 10px;"}[*Generate remaining Ansible
tasks.*]{style="font-size: 12px;"}

## Ansible Lightspeed with Watson Code Assistant and context

Generating contextually aware, accurate Ansible content suggestions
saves you time and helps you create efficiently. One of Ansible
Lightspeed's superpowers is context.

Ansible Lightspeed uses the Ansible task description and YAML file
content to generate suggestions suited to what you're automating. Let's
use an example to illustrate this.

Imagine we want to set module defaults for the
[ansible.posix.firewalld](https://docs.ansible.com/ansible/latest/collections/ansible/posix/firewalld_module.html){rel="noopener"
target="_blank"} module in the last Ansible task. Specifically, always
making the firewall rule changes permanent. We can accomplish this by
using the
[module_defaults](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_module_defaults.html){rel="noopener"
target="_blank"} Playbook keyword, illustrated below.

+-----------------------------------------------------------------------+
| [                                                                     |
| mo                                                                    |
| dule_defaults:]{style="background-color: #fafafa; color: #986801;"}[\ |
|                                                                       |
|  ]{style="background-color: #fafafa; color: #383a42;"}[ansible.po     |
| six.firewalld:]{style="background-color: #fafafa; color: #50a14f;"}[\ |
| ]{style="background-color: #fafafa; color: #383a42;"}[                |
| permanent:]{style="background-color: #                                |
| fafafa; color: #986801;"}[ ]{style="background-color: #fafafa; color: |
|  #383a42;"}[true]{style="background-color: #fafafa; color: #0184bb;"} |
+-----------------------------------------------------------------------+

*Ansible Playbook module_defaults section.*

The module defaults section tells Ansible to always add "*permanent:
true*" to every "*ansible.posix.firewall*" task in the Playbook. Let\'s
ask Ansible Lightspeed for an updated suggestion with the module
defaults.

![](https://www.ansible.com/hs-fs/hubfs/Google%20Drive%20Integration/WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch-Jun-23-2023-03-51-57-6177-PM.gif?width=1466&height=892&name=WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch-Jun-23-2023-03-51-57-6177-PM.gif){style="margin-left: 0.00px;"
width="1466" height="892" loading="lazy"
srcset="https://www.ansible.com/hs-fs/hubfs/Google%20Drive%20Integration/WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch-Jun-23-2023-03-51-57-6177-PM.gif?width=733&height=446&name=WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch-Jun-23-2023-03-51-57-6177-PM.gif 733w, https://www.ansible.com/hs-fs/hubfs/Google%20Drive%20Integration/WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch-Jun-23-2023-03-51-57-6177-PM.gif?width=1466&height=892&name=WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch-Jun-23-2023-03-51-57-6177-PM.gif 1466w, https://www.ansible.com/hs-fs/hubfs/Google%20Drive%20Integration/WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch-Jun-23-2023-03-51-57-6177-PM.gif?width=2199&height=1338&name=WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch-Jun-23-2023-03-51-57-6177-PM.gif 2199w, https://www.ansible.com/hs-fs/hubfs/Google%20Drive%20Integration/WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch-Jun-23-2023-03-51-57-6177-PM.gif?width=2932&height=1784&name=WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch-Jun-23-2023-03-51-57-6177-PM.gif 2932w, https://www.ansible.com/hs-fs/hubfs/Google%20Drive%20Integration/WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch-Jun-23-2023-03-51-57-6177-PM.gif?width=3665&height=2230&name=WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch-Jun-23-2023-03-51-57-6177-PM.gif 3665w, https://www.ansible.com/hs-fs/hubfs/Google%20Drive%20Integration/WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch-Jun-23-2023-03-51-57-6177-PM.gif?width=4398&height=2676&name=WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch-Jun-23-2023-03-51-57-6177-PM.gif 4398w"
sizes="(max-width: 1466px) 100vw, 1466px"}*Ansible Lightspeed context.*

Note that it used the full Playbook context and provided a revised
recommendation that excludes "*permanent: true*". You can also apply
this to other Playbook keywords, such as "*vars*".

## Transparency and openness. Ansible Lightspeed Content Source Matching

Last, and certainly not least, is Ansible Lightspeed Content Source
Matching.

![](https://www.ansible.com/hs-fs/hubfs/Google%20Drive%20Integration/WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch-1.gif?width=1466&height=892&name=WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch-1.gif){style="margin-left: 0.00px;"
width="1466" height="892" loading="lazy"
srcset="https://www.ansible.com/hs-fs/hubfs/Google%20Drive%20Integration/WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch-1.gif?width=733&height=446&name=WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch-1.gif 733w, https://www.ansible.com/hs-fs/hubfs/Google%20Drive%20Integration/WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch-1.gif?width=1466&height=892&name=WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch-1.gif 1466w, https://www.ansible.com/hs-fs/hubfs/Google%20Drive%20Integration/WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch-1.gif?width=2199&height=1338&name=WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch-1.gif 2199w, https://www.ansible.com/hs-fs/hubfs/Google%20Drive%20Integration/WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch-1.gif?width=2932&height=1784&name=WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch-1.gif 2932w, https://www.ansible.com/hs-fs/hubfs/Google%20Drive%20Integration/WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch-1.gif?width=3665&height=2230&name=WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch-1.gif 3665w, https://www.ansible.com/hs-fs/hubfs/Google%20Drive%20Integration/WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch-1.gif?width=4398&height=2676&name=WIP%20Blog%20%7C%20Ansible%20Lightspeed%20Technical%20Preview%20launch-1.gif 4398w"
sizes="(max-width: 1466px) 100vw, 1466px"}\
[*Ansible Lightspeed Content Source
Matching.*]{style="font-size: 12px;"}

We transparently share the potential source, Author, and content license
of the training data used for the recommendation. Building trust in the
community and supporting the relationships between authors and
contributors is part of Red Hat's DNA.  These suggestions came from the
Ansible community; we don't want to hide that.

## Wrap-up

Congratulations! You have successfully configured Ansible Lightspeed in
VS Code and experienced its generative AI capabilities with just a few
simple steps.

We encourage you to share your feedback on the technical preview
experience and stay updated on the project by joining the
[Ansible Lightspeed Matrix room](https://matrix.to/#/#lightspeed:ansible.com)
to ask questions and get the latest news. Please also
visit the [Ansible Lightspeed landing page.](http://www.redhat.com/ansible-lightspeed)

We'll update you with new resources to help you get the most out of your
Ansible Lightspeed with Watson Code Assistant experience.

Happy automating...with AI!
