---
author: Ajay Chenampara
date: 2020-06-01 00:00 UTC
description: In this blog post we\'ll walk through using Ansible
  Collections with Ansible Tower, part of the Red Hat Ansible Automation
  Platform.
lang: en-us
title: Installing and using collections on Ansible Tower
---

# Installing and using collections on Ansible Tower

Ansible Collections are the new way to distribute and manage content.
Ansible content can be modules, roles, plugins and even Ansible
Playbooks. In my [previous
blog](https://www.ansible.com/blog/hands-on-with-ansible-collections) I
provide a walkthrough of using Ansible Collections from Ansible Galaxy
and Automation Hub.  Ansible Galaxy is the upstream community for
sharing Ansible Collections.  Any community user can create a namespace
and share content with anyone. Access to Automation Hub is included with
a Red Hat Ansible Automation Platform subscription. Automation Hub only
contains fully supported and certified content from Red Hat and our
partners.

In this blog post we\'ll walk through using Ansible Collections with
Ansible Tower, part of the Red Hat Ansible Automation Platform.  There
are a few differences between using command-line Ansible for syncing
with Ansible Galaxy or the Automation Hub versus using Ansible Tower.
However, it is really easy and I will show you how!

## Accessing collections content from Automation Hub and Galaxy from Ansible Tower.

If the Ansible Collections are included in your project you do not need
to authenticate to Automation Hub. This method is where you are
downloading dynamically using a requirements file as outlined in my
[blog
post](https://www.ansible.com/blog/hands-on-with-ansible-collections).
In general there are three strategies for using Ansible Collections with
your environment:\

1.  Install the collection into your runtime environment or virtual
    environment
2.  Provide the collection as part of your SCM tree 
3.  Use a requirements file

When accessing content from Automation Hub, the authentication token and
authentication URL configuration has to be made in Ansible Tower's
settings. 

 

*Note: Even if you have the authorization details in your ansible.cfg
file within the project repo, it will not be picked up by Ansible Tower.
You will need to enter these details in the Ansible Tower settings*

 

In order to do this, navigate to the *Settings \> Jobs*  sidebar link
from the Ansible Tower administration section.

![Screen Shot 2020-06-01 at 12.07.38
PM](https://www.ansible.com/hs-fs/hubfs/Screen%20Shot%202020-06-01%20at%2012.07.38%20PM.png?width=578&name=Screen%20Shot%202020-06-01%20at%2012.07.38%20PM.png){width="578"
style="width: 578px;"
srcset="https://www.ansible.com/hs-fs/hubfs/Screen%20Shot%202020-06-01%20at%2012.07.38%20PM.png?width=289&name=Screen%20Shot%202020-06-01%20at%2012.07.38%20PM.png 289w, https://www.ansible.com/hs-fs/hubfs/Screen%20Shot%202020-06-01%20at%2012.07.38%20PM.png?width=578&name=Screen%20Shot%202020-06-01%20at%2012.07.38%20PM.png 578w, https://www.ansible.com/hs-fs/hubfs/Screen%20Shot%202020-06-01%20at%2012.07.38%20PM.png?width=867&name=Screen%20Shot%202020-06-01%20at%2012.07.38%20PM.png 867w, https://www.ansible.com/hs-fs/hubfs/Screen%20Shot%202020-06-01%20at%2012.07.38%20PM.png?width=1156&name=Screen%20Shot%202020-06-01%20at%2012.07.38%20PM.png 1156w, https://www.ansible.com/hs-fs/hubfs/Screen%20Shot%202020-06-01%20at%2012.07.38%20PM.png?width=1445&name=Screen%20Shot%202020-06-01%20at%2012.07.38%20PM.png 1445w, https://www.ansible.com/hs-fs/hubfs/Screen%20Shot%202020-06-01%20at%2012.07.38%20PM.png?width=1734&name=Screen%20Shot%202020-06-01%20at%2012.07.38%20PM.png 1734w"
sizes="(max-width: 578px) 100vw, 578px"}

Click on *Jobs* and update the following fields:

1.  PRIMARY GALAXY SERVER URL:
    https://cloud.redhat.com/api/automation-hub/
2.  PRIMARY GALAXY AUTHENTICATION URL: 
    https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token
3.  PRIMARY GALAXY SERVER TOKEN: xxxxxxxxxxxxxxxxxxxxxxxxx......\
    \

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Red Hat recommends using Automation Hub for your primary Galaxy Server URL to ensure you are using certified content that is fully supported via your Red Hat Ansible Automation Platform subscription
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

 

![Screen Shot 2020-06-01 at 12.09.22
PM](https://www.ansible.com/hs-fs/hubfs/Screen%20Shot%202020-06-01%20at%2012.09.22%20PM.png?width=569&name=Screen%20Shot%202020-06-01%20at%2012.09.22%20PM.png){width="569"
style="width: 569px;"
srcset="https://www.ansible.com/hs-fs/hubfs/Screen%20Shot%202020-06-01%20at%2012.09.22%20PM.png?width=285&name=Screen%20Shot%202020-06-01%20at%2012.09.22%20PM.png 285w, https://www.ansible.com/hs-fs/hubfs/Screen%20Shot%202020-06-01%20at%2012.09.22%20PM.png?width=569&name=Screen%20Shot%202020-06-01%20at%2012.09.22%20PM.png 569w, https://www.ansible.com/hs-fs/hubfs/Screen%20Shot%202020-06-01%20at%2012.09.22%20PM.png?width=854&name=Screen%20Shot%202020-06-01%20at%2012.09.22%20PM.png 854w, https://www.ansible.com/hs-fs/hubfs/Screen%20Shot%202020-06-01%20at%2012.09.22%20PM.png?width=1138&name=Screen%20Shot%202020-06-01%20at%2012.09.22%20PM.png 1138w, https://www.ansible.com/hs-fs/hubfs/Screen%20Shot%202020-06-01%20at%2012.09.22%20PM.png?width=1423&name=Screen%20Shot%202020-06-01%20at%2012.09.22%20PM.png 1423w, https://www.ansible.com/hs-fs/hubfs/Screen%20Shot%202020-06-01%20at%2012.09.22%20PM.png?width=1707&name=Screen%20Shot%202020-06-01%20at%2012.09.22%20PM.png 1707w"
sizes="(max-width: 569px) 100vw, 569px"}

This is the only step you need to do in Ansible Tower in order to
download the certified collection from Automation Hub which was defined
in the *collections/requirements.yml* file.

The playbook is invoked via a job template as usual.

![Screen Shot 2020-06-01 at 12.09.44
PM](https://www.ansible.com/hs-fs/hubfs/Screen%20Shot%202020-06-01%20at%2012.09.44%20PM.png?width=578&name=Screen%20Shot%202020-06-01%20at%2012.09.44%20PM.png){width="578"
style="width: 578px;"
srcset="https://www.ansible.com/hs-fs/hubfs/Screen%20Shot%202020-06-01%20at%2012.09.44%20PM.png?width=289&name=Screen%20Shot%202020-06-01%20at%2012.09.44%20PM.png 289w, https://www.ansible.com/hs-fs/hubfs/Screen%20Shot%202020-06-01%20at%2012.09.44%20PM.png?width=578&name=Screen%20Shot%202020-06-01%20at%2012.09.44%20PM.png 578w, https://www.ansible.com/hs-fs/hubfs/Screen%20Shot%202020-06-01%20at%2012.09.44%20PM.png?width=867&name=Screen%20Shot%202020-06-01%20at%2012.09.44%20PM.png 867w, https://www.ansible.com/hs-fs/hubfs/Screen%20Shot%202020-06-01%20at%2012.09.44%20PM.png?width=1156&name=Screen%20Shot%202020-06-01%20at%2012.09.44%20PM.png 1156w, https://www.ansible.com/hs-fs/hubfs/Screen%20Shot%202020-06-01%20at%2012.09.44%20PM.png?width=1445&name=Screen%20Shot%202020-06-01%20at%2012.09.44%20PM.png 1445w, https://www.ansible.com/hs-fs/hubfs/Screen%20Shot%202020-06-01%20at%2012.09.44%20PM.png?width=1734&name=Screen%20Shot%202020-06-01%20at%2012.09.44%20PM.png 1734w"
sizes="(max-width: 578px) 100vw, 578px"}

Launching this job template results in the collections being pulled down
from Automation Hub and Galaxy and invoking modules made available
through those collections.

![ajay collections blog
5](https://www.ansible.com/hs-fs/hubfs/ajay%20collections%20blog%205.png?width=1600&name=ajay%20collections%20blog%205.png){width="1600"
style="width: 1600px;"
srcset="https://www.ansible.com/hs-fs/hubfs/ajay%20collections%20blog%205.png?width=800&name=ajay%20collections%20blog%205.png 800w, https://www.ansible.com/hs-fs/hubfs/ajay%20collections%20blog%205.png?width=1600&name=ajay%20collections%20blog%205.png 1600w, https://www.ansible.com/hs-fs/hubfs/ajay%20collections%20blog%205.png?width=2400&name=ajay%20collections%20blog%205.png 2400w, https://www.ansible.com/hs-fs/hubfs/ajay%20collections%20blog%205.png?width=3200&name=ajay%20collections%20blog%205.png 3200w, https://www.ansible.com/hs-fs/hubfs/ajay%20collections%20blog%205.png?width=4000&name=ajay%20collections%20blog%205.png 4000w, https://www.ansible.com/hs-fs/hubfs/ajay%20collections%20blog%205.png?width=4800&name=ajay%20collections%20blog%205.png 4800w"
sizes="(max-width: 1600px) 100vw, 1600px"}

## Conclusion

Ansible Collections introduce a way to modularize and package automation
content effectively. The Red Hat Automation Hub hosts certified
collections that are validated and supported by Red Hat. Ansible Galaxy
hosts community contributed collections. Customers can access
collections from both content repositories. I think of collections as
superchargers to the "batteries included" approach that Ansible takes.
It up-levels the nuances involved in building out automation, allowing
users to plug-n-play the latest and greatest automation content being
built by certified partners and the community.
