---
author: Roger Lopez
date: 2022-07-06 00:00 UTC
description: One of the great advantages of combining GitOps with
  Ansible is that you get to streamline the automation delivery and the
  lifecycle of a containerized application.
lang: en-us
title: Using Ansible and GitOps to Manage the Lifecycle of a Containerized Application
---

# Using Ansible and GitOps to Manage the Lifecycle of a Containerized Application

[![taking automation to the next level
blog](https://www.ansible.com/hs-fs/hubfs/taking%20automation%20to%20the%20next%20level%20blog.png?width=1200&name=taking%20automation%20to%20the%20next%20level%20blog.png){width="1200"
loading="lazy" style="width: 1200px;"
srcset="https://www.ansible.com/hs-fs/hubfs/taking%20automation%20to%20the%20next%20level%20blog.png?width=600&name=taking%20automation%20to%20the%20next%20level%20blog.png 600w, https://www.ansible.com/hs-fs/hubfs/taking%20automation%20to%20the%20next%20level%20blog.png?width=1200&name=taking%20automation%20to%20the%20next%20level%20blog.png 1200w, https://www.ansible.com/hs-fs/hubfs/taking%20automation%20to%20the%20next%20level%20blog.png?width=1800&name=taking%20automation%20to%20the%20next%20level%20blog.png 1800w, https://www.ansible.com/hs-fs/hubfs/taking%20automation%20to%20the%20next%20level%20blog.png?width=2400&name=taking%20automation%20to%20the%20next%20level%20blog.png 2400w, https://www.ansible.com/hs-fs/hubfs/taking%20automation%20to%20the%20next%20level%20blog.png?width=3000&name=taking%20automation%20to%20the%20next%20level%20blog.png 3000w, https://www.ansible.com/hs-fs/hubfs/taking%20automation%20to%20the%20next%20level%20blog.png?width=3600&name=taking%20automation%20to%20the%20next%20level%20blog.png 3600w"
sizes="(max-width: 1200px) 100vw, 1200px"}]{style="color: #000000;"}

[One of the great advantages of combining GitOps with Ansible is that
you get to streamline the automation delivery and the lifecycle of a
containerized application.]{style="color: #000000;"}

[With the abilities of GitOps we get to:]{style="color: #000000;"}

-   [Standardize configurations of our
    applications.]{style="color: #000000;"}
-   [Inherit the benefits of version control of our
    configurations.]{style="color: #000000;"}
-   [Easily track changes of the configuration settings making fixing
    issues easier.]{style="color: #000000;"}
-   [Have one source of truth for our
    applications.]{style="color: #000000;"}

[Combine the above with Ansible and you have everything you need to
accomplish configuration consistency for a containerized app anywhere
that you automate. ]{style="color: #000000;"}

[That leads us to, "how do we combine Ansible and GitOps to manage the
lifecycle of a containerized application?"]{style="color: #000000;"}

[Simple. By creating an Ansible workflow that is associated with a Git
webhook that is part of my application's
repository.]{style="color: #000000;"}

[What is a Git webhook you ask?]{style="color: #000000;"}

[Git webhooks are defined as a method to deliver notifications to an
external web server whenever certain actions occur on a
repository.]{style="color: #000000;"}

[For example, when a repository is updated, this could trigger an event
that could trigger CI builds, deploy an environment, or in our case,
modify the configuration of our containerized
application. ]{style="color: #000000;"}

[A webhook provides the ability to execute specified commands between
apps over the web. Automation controller provides webhook integration
with GitHub and GitLab, but for the purposes of this blog we will be
integrating with GitHub. ]{style="color: #000000;"}

[In the following sections of this blog, I'm going to provide the
step-by-step process to:]{style="color: #000000;"}[\
\
]{style="color: #000000;"}

-   [Setup your Git webhook (using GitHub).]{style="color: #000000;"}
-   [Setting up an Ansible workflow that triggers via push events from
    your GitHub repository.]{style="color: #000000;"}

## Create a GitHub personal access token

[The GitHub personal access token (PAT) is one of the credentials needed
to associate the Ansible workflow with your Git
repository.]{style="color: #000000;"}

[Generate a personal access token (PAT) for use with automation
controller.]{style="color: #252525;"}

1.  [In the profile settings of your GitHub account, click
    ]{style="color: #252525;"}**[Settings]{style="color: #252525;"}**[.]{style="color: #252525;"}
2.  [Below the Personal settings, click
    ]{style="color: #252525;"}**[Developer
    Settings]{style="color: #252525;"}**[.]{style="color: #252525;"}[\
    ]{style="color: #252525;"}[![](https://lh6.googleusercontent.com/KbQ9AXespMw8Pq4r5QMj3BOXBNY8ckjjgBUIP8X52CyuJfaKNqbep0FHlpdbh6aWKRLCNlzr4Uuw2VaYgFEMi0j9SPPLEKO4__X1fbvqp8TeTweTVXNWkmwtxtkZ7LuAQrLv_9dy8jqQvtsHaQ){width="184"
    height="626" loading="lazy"}]{style="color: #000000;"}
3.  [In the Developer settings, click
    ]{style="color: #252525;"}**[Personal access
    tokens]{style="color: #252525;"}**[.]{style="color: #252525;"}
4.  [From the Personal access tokens screen, click
    ]{style="color: #252525;"}**[Generate new
    token]{style="color: #252525;"}**[ button.]{style="color: #252525;"}
5.  [When prompted, enter your GitHub account password to
    continue.]{style="color: #252525;"}
6.  [In the
    ]{style="color: #252525;"}**[Note]{style="color: #252525;"}**[
    field, enter a brief description about what this PAT will be used
    for.]{style="color: #252525;"}
7.  [In the
    ]{style="color: #252525;"}**[Expiration]{style="color: #252525;"}**[
    drop down, select ]{style="color: #252525;"}**[No
    expiration]{style="color: #252525;"}**[.]{style="color: #252525;"}
8.  [In the Scope fields, automation controller webhook only needs repo
    scope access, with the exception of invites. For information about
    other scopes, click the link right above the table to access the
    docs.]{style="color: #252525;"}

[![](https://lh3.googleusercontent.com/Y9YR7zzhl1-voDlrDANGo8X-RTeLeDLIZVHNLGeZvaWuSAbMZ9w3ICAiftZVVZT8eakTt6IFX4i3QO03-Ucp48NdQqVvETxdhXmGOLyO-PdI07sTQeBD09FvPNhuSXmbhygfNfD7lg4memz4wQ){width="624"
height="397" loading="lazy"}]{style="color: #252525;"}

1.  [Click the ]{style="color: #252525;"}**[Generate
    Token]{style="color: #252525;"}**[ button at the bottom of the
    page.]{style="color: #252525;"}

[Once we have our PAT in place, the next step is to create a Git
repository that will be triggered by our GitHub webhooks when changes
are made to the repository. ]{style="color: #252525;"}[\
]{style="color: #252525;"}[\
]{style="color: #252525;"}[For the purposes of this blog, I'll be using
my ]{style="color: #252525;"}[App Demo
Repository](https://github.com/rlopez133/app_demo)[. Feel free to use
your own or fork this repository to follow
along. ]{style="color: #252525;"}

## Familiarizing ourselves with the App Demo Repository

[The App Demo Repository is fairly simplistic, as it
contains:]{style="color: #000000;"}[\
\
]{style="color: #000000;"}

-   [container_playbook.yml ]{style="color: #000000;"}
-   [group_vars/all.yml]{style="color: #000000;"}
-   [requirements.yml ]{style="color: #000000;"}

[The container_playbook.yml is a simple playbook that creates a color
container, starts it on a specific port and sets two environment
variables, APP_COLOR and tree. ]{style="color: #252525;"}

[A sample of that container_playbook.yml]{style="color: #252525;"}

``` yml
---
- name: Playbook to setup prereqs
  hosts: all
  become: true
  tasks:
    - name: Create a color container
      containers.podman.podman_container:
        name: colors
        image: docker.io/mmumshad/simple-webapp-color:latest
        state: started
        network: host
        ports:
            - "{{ host_port }}:{{ container_port }}"
        env:
            APP_COLOR: "{{ color }}"
            tree: "{{ tree }}"
```

The group_vars/all.yml is where I'll be making modifications to my
Podman container that will trigger changes to the container.

A sample of that group_vars/all.yml file:

``` yml
color: "BLUE" 
tree: "trunk" 
host_port: 8080 
container_port: 8080
```

Finally, we have the requirements.yml file that ensures we have the
containers.podman collection available to use within the playbook. 

A sample of the requirements.yml

``` yml
collections:
- name: containers.podman
```

[With our repository in place and our GitHub PAT set, the next steps
involve creating our Red Hat Ansible Automation Platform resources that
will be triggered when GitHub push events happen in the App Demo
Repository.]{style="color: #252525;"}

## Creating our Ansible Automation Platform Resources

[Within my automation controller dashboard, I first need to create my
credential resources to ensure that when I create my new project,
workflow and job template -- they can all easily attach my App Demo PAT
credential. ]{style="color: #000000;"}

[Within the automation controller dashboard: ]{style="color: #000000;"}

1.  [Under
    ]{style="color: #252525;"}**[Resources]{style="color: #252525;"}**[→
    ]{style="color: #252525;"}**[Credentials]{style="color: #252525;"}**[
    click the blue
    ]{style="color: #252525;"}**[Add]{style="color: #252525;"}**[
    button.]{style="color: #252525;"}

2.  1.  [Provide a
        ]{style="color: #252525;"}**[Name]{style="color: #252525;"}**[,
        e.g. App Demo PAT.]{style="color: #252525;"}
    2.  [Select ]{style="color: #252525;"}**[GitHub Personal Access
        Token]{style="color: #252525;"}**[ as the
        ]{style="color: #252525;"}**[Credential
        Type]{style="color: #252525;"}**[.]{style="color: #252525;"}
    3.  [Within ]{style="color: #252525;"}**[Type
        Details]{style="color: #252525;"}**[, add the secret using the
        previously generated token from
        GitHub.]{style="color: #252525;"}

3.  [Click
    ]{style="color: #000000;"}**[Save.]{style="color: #000000;"}**

[Once my App Demo PAT credential is in place, I need an additional
credential to access my host that will be running the Podman container.
In my case, this is an AWS instance. ]{style="color: #000000;"}[\
]{style="color: #000000;"}[\
]{style="color: #000000;"}[In order to access this host, I will create a
new credential that stores my AWS private key.]{style="color: #000000;"}

1.  [Under
    ]{style="color: #252525;"}**[Resources]{style="color: #252525;"}**[→
    ]{style="color: #252525;"}**[Credentials]{style="color: #252525;"}**[
    click the blue
    ]{style="color: #252525;"}**[Add]{style="color: #252525;"}**[
    button.]{style="color: #252525;"}

2.  1.  [Provide a
        ]{style="color: #252525;"}**[Name]{style="color: #252525;"}**[,
        e.g. My AWS Private Key.]{style="color: #252525;"}
    2.  [Select
        ]{style="color: #252525;"}**[Machine]{style="color: #252525;"}**[
        as the ]{style="color: #252525;"}**[Credential
        Type.]{style="color: #252525;"}**
    3.  [Within ]{style="color: #252525;"}**[Type
        Details]{style="color: #252525;"}**[, add the
        ]{style="color: #252525;"}**[SSH Private
        Key]{style="color: #252525;"}**[ in the text
        area. ]{style="color: #252525;"}

3.  [Click
    ]{style="color: #252525;"}**[Save.]{style="color: #252525;"}**

[Once the credentials are in place, I need to create an inventory that
stores the details of my AWS instance.]{style="color: #000000;"}

[To add details of my AWS instance, I will create an inventory
file.]{style="color: #000000;"}

1.  [Under
    ]{style="color: #252525;"}**[Resources]{style="color: #252525;"}**[→
    ]{style="color: #252525;"}**[Inventories]{style="color: #252525;"}**[
    click the blue
    ]{style="color: #252525;"}**[Add]{style="color: #252525;"}**[→
    ]{style="color: #252525;"}**[Add inventory
    ]{style="color: #252525;"}**[button.]{style="color: #252525;"}

2.  1.  [Provide a
        ]{style="color: #000000;"}**[Name]{style="color: #000000;"}**[,
        e.g. App Demo Inventory.]{style="color: #000000;"}

3.  [Click
    ]{style="color: #000000;"}**[Save.]{style="color: #000000;"}**

4.  [Under
    ]{style="color: #252525;"}**[Resources]{style="color: #252525;"}**[→
    ]{style="color: #252525;"}**[Inventories]{style="color: #252525;"}**[
    click ]{style="color: #252525;"}**[App Demo
    Inventory.]{style="color: #252525;"}**

5.  [Click the tab labeled ]{style="color: #000000;"}**[Hosts
    ]{style="color: #000000;"}**[and click the
    ]{style="color: #000000;"}**[Add
    ]{style="color: #000000;"}**[button.]{style="color: #000000;"}

6.  1.  [Provide a
        ]{style="color: #000000;"}**[Name]{style="color: #000000;"}**[,
        e.g. App Demo Host.]{style="color: #000000;"}

[Within
]{style="color: #000000;"}**[Variables]{style="color: #000000;"}**[,
provide the following YAML.]{style="color: #000000;"}

``` yml
---
ansible_host: 
ansible_user: ec2-user
```

[With the credentials and inventory resources set, I will create my App
Demo project. The purpose of this project is to create a workflow that
contains a job template that automatically runs every time an update to
the App Demo repository takes place. ]{style="color: #000000;"}

[This ensures that as I make changes to my Podman container settings
within my Git repository, the container_playbook.yml runs to make the
appropriate changes. ]{style="color: #000000;"}

[Within the automation controller dashboard:]{style="color: #000000;"}

1.  Under **Resources**→ **Projects** click the blue **Add** button.
2.  Provide a **Name**, e.g. App Demo Project.
3.  Select **Default** as the Organization.
4.  Select **Default execution environment** as the **Execution
    Environment.**
5.  Select **Git** as the **Source Control Credential Type.**
6.  Within **Type Details**, add the **Source Control URL** (your GitHub
    repository).
7.  Within **Options, s**elect **Clean**, **Delete**, **Update Revision
    on Launch.**
8.  Click **Save**.

Next, create a workflow template.

1.  Under **Resources**→ **Templates** click the blue **Add** → **Add
    workflow template**.

2.  Provide a **Name**, e.g. App Demo Workflow.

3.  Within **Options**, checkmark **Enable Webhook**.

4.  1.  Within **Webhook details**, select **GitHub** as the **Webhook
        Service**.
    2.  Within **Webhook details**, select your GitHub PAT token
        previously created as the **Webhook Credential**, e.g. App Demo
        PAT.

5.  Click **Save**.

6.  Within the **Please click the Start button to begin** window, click
    the **Save** at the top right corner.

7.  Copy the **Webhook URL** and the **Webhook Key** as they will be
    used later.

## Enabling GitHub Webhooks for the App Demo Repository

With the Ansible Automation Platform workflow template created and the
GitHub repository with the required files in place, the next step is to
enable webhooks for our repository, e.g. *app_demo*.

1.  At the homepage of your GitHub repository, select the **Settings**
    tab.
2.  Within the **Settings** tab, select **Webhooks**.\
    ![](https://lh5.googleusercontent.com/PF0cXJ9Pe2Bh_IhDYWcIICejr-YE-zCX240Ngi7nWqrNoxgWBmD26FEK3Myw8dBnt58ZH-pF0PQrmBMCNWqYoXdaaaTKTzuHbgf3TbhLy9SFil-oXHYai72NnCqE31H5RKZyB6snJo9GPPifwQ){width="624"
    height="208" loading="lazy"}
3.  Within the **Webhooks** section, select the **Add webhook** button.
4.  Enter the **Payload URL** (Webhook URL of the workflow).
5.  Change the **Content type** drop down to *application/json*.
6.  Enter the **Secret** (Webhook key of the workflow).
7.  Leave the defaults to use push events, and click the button **Add
    webhook**.

[Warning]{style="color: #000000; font-size: 16px;"}

[By default, GitHub verifies SSL certificates when delivering payloads.
If your automation controller SSL certificates are not signed, ensure to
disableSSL verification.]{style="color: #000000; font-size: 16px;"}

## Creating the App Demo job template

The App Demo job template runs the *container_playbook.yml* file
automatically every time an update to the Git repository takes place. 

To create the job template within your automation controller dashboard:

1.  Under **Resources**→ **Templates** click the blue **Add** → **Add
    job template**.
2.  Provide a **Name**, e.g. App Demo Job.
3.  Select **Run** as the **Job Type.**
4.  Select **App** **Demo Inventory** as the **Inventory.**
5.  Select **App Demo Project** as the **Project.**
6.  Select **Default execution environment** as the **Execution
    Environment.**
7.  Select *container_playbook.yml* as the **Playbook.**
8.  Select **Credentials** and select **My AWS Private Key.**
9.  Within **Options**, select **Enable webhook**.
10. Select **GitHub** as the **Webhook Service**.
11. Select your GitHub PAT token previously created as the **Webhook
    Credential**, e.g. App Demo PAT.
12. Click **Save**.

## Updating the created App Demo Workflow

Previously, the App Demo workflow was created. The purpose of this
workflow is to ensure that the App Demo Project is always in sync and
that the App Demo Job runs the container playbook whenever changes are
made to the App Demo repository.

1.  Under **Resources**→ **Templates**, select your template. e.g *App
    Demo Workflow.*
2.  Within the **Details** section, select the **Visualizer** tab and
    click the green **Start**.
3.  For **Node Type** select **Project Sync** and select the appropriate
    project, e.g. *App Demo Project* and click **Save**.
4.  Hover over the **App Demo Project** and select the plus \"+\"
    symbol.
5.  Within the **Add Node** window, select **On Success** as to when
    this node should be executed and click **Next**.
6.  Select the **App Demo Job** as the **Node Type** and click **Save**.
7.  Once brought back to the **Visualizer**, select the **Save** button
    at the top right corner.

## Verify App Demo Setup

[To test if all is working correctly, head to your host that is running
the Podman container. Once there, the following podman ps command can be
run:]{style="color: #000000;"}

``` yml
$ sudo podman ps
CONTAINER ID  IMAGE  COMMAND     CREATED   STATUS    PORTS      NAMES
```

*NOTE: The first time you run podman ps, you should have no containers
running as you haven't run the App Demo workflow.*

Head over to your App Demo GitHub repository and modify the
app_demo/group_vars/all.yml file where you change the color: "BLUE" to
color: "YELLOW" and  git push your changes.

Head over to your automation controller dashboard and you should see the
App Demo workflow running. Once complete, within your host, verify the
container has the changes made:

``` yml
$ ssh -i </path/to/private-key.pem> ec2-user@<IP>


$ sudo podman exec -it colors env

PATH=/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
TERM=xterm
container=podman
PYTHON_VERSION=3.7.0
PYTHON_PIP_VERSION=18.0
LANG=C.UTF-8
GPG_KEY=0D96DF4D4110E5C43FBFB17A2A347FA6AA65421D
APP_COLOR=YELLOW
tree=trunk
HOME=/root
```

Notice how the Podman container is now running and has the color
YELLOW.\
\
Going back to the App Demo repository, change the color from YELLOW to
GREEN and git push your changes.

The automation controller dashboard will run the App Demo workflow and
once complete, you can re-run the same exec command from your host and
see the color has now changed to GREEN.

``` yml
$ ssh -i </path/to/private-key.pem> ec2-user@<IP>

$ sudo podman exec -it colors env

PATH=/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
TERM=xterm
container=podman
PYTHON_VERSION=3.7.0
PYTHON_PIP_VERSION=18.0
LANG=C.UTF-8
GPG_KEY=0D96DF4D4110E5C43FBFB17A2A347FA6AA65421D
APP_COLOR=GREEN
tree=trunk
HOME=/root
```

## Conclusion

The goal of this exercise was to show the power of Ansible and GitOps.
Together, they can provide key automation to your containerized
applications.

While in the demo we made a simplistic color value change of our
application, but imagine we applied this for:

-   patching our application because of a security threat.
-   updating our application to a newer version.
-   managing containerized applications at the edge. 

And all this doesn't even mention the inherited benefits of:

-   Standardizing configurations of our applications.
-   Inheriting the benefits of version control of our configurations.
-   Easily tracking changes of the configuration settings making fixing
    issues easier.
-   Have one source of truth for our applications.

The use cases and abilities that both tools provide together are
endless. 
