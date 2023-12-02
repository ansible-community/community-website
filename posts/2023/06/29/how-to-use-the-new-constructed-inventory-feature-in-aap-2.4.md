---
title: How to use the new Constructed Inventory Feature in Ansible Automation Platform 2.4
author: Alan Rominger
date: 2023-06-29 13:00:00
slug: how-to-use-the-new-constructed-inventory-feature-in-aap-2.4
category: awx
tags: awx
type: text
---

# The New Constructed Inventory Feature

In this blog we introduced the idea for a new smarter way of handling inventory based on the Ansible constructed plugin. Now in Ansible Automation Platform 2.4, we have introduced this as a fully supported feature and this blog aims to introduce you to it! 

Constructed inventory is the successor to the existing Smart Inventory feature, and  is now presented as another choice when creating an Inventory in Ansible Automation Platform controller. This will take a list of ‘normal’ inventories as input, perform user-defined operations, filter, and produce a resultant inventory with content from the input inventories.

# What is Constructed Inventory?

The function is similar to the existing smart inventory - in that it allows users to run jobs against hosts in multiple inventories. 

Constructed inventory however introduces new capabilities, including the built in ability to define and use both hostvars and groupvars:

* **Groups** are present in constructed inventory and play a key role in its configuration.
* **User-defined logic** (to add groups, vars, and down-select hosts) is run via ansible-inventory, which controller does for you, and is shown in the UI through an inventory update.
* The format of user-defined logic is the widely-used Ansible-style [jinja2](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_templating.html#templating-jinja2).

A guiding principle is that to create a constructed inventory, you think the same as when writing a playbook. This is in contrast to smart inventory where you had to think about the inventory as the application saw it.

# Constructed Inventory in the UI

After you click ***“Add constructed inventory”*** under **Inventories**, this is the menu you will see:

![The New Constructed Inventory Feature](/images/posts/how-to-use-the-new-constructed-inventory-feature-in-aap-2.4/image1.webp)

There are three key items unique to constructed inventory.

* **Input inventories** is where you will list existing inventories that the constructed inventory will get inventory content (hosts, groups, etc.) from.
* **Limit** is passed directly to ansible-inventory, and allows filtering the hosts using the standard syntax for Ansible host patterns.
* **Source vars** is the input to the [ansible.builtin.constructed inventory plugin](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/constructed_inventory.html#ansible-builtin-constructed-inventory-uses-jinja2-to-construct-vars-and-groups-based-on-existing-inventory).

NOTE: The input inventories are ordered so that in the event of host name and variable conflicts, variables from the last inventory will take precedence. Variables are merged, so this will not unset a variable from a prior input inventory. If there are no host name conflicts this will not matter, so the example used here will mention ordering.

Don’t worry about these right now, as they will be explored using an example below.

# Constructed Inventory In Its Simplest Form
You must have at least **one** input inventory, but the other fields are not necessary to fill in. In some situations, it might make sense to *provide two or more input inventories and leave limit and source-vars blank.* Then you can run jobs that act on the combination of the inventory content from both of those input inventories. 

 

# More Advanced Constructed Inventory Use Cases
In order to explain the function of *limit* and *Source vars* which provides the ultimate feature power, it will help to have a concrete example.

# Setting up the Constructed Inventory
Imagine that you have two inventories that come from the same cloud provider, but cover different regions and so have different sets of hosts. These inventories are kept separate, due to separate accounts, separate functions, and separate locations. In this example, we imagine simple **East / West region** input inventories.

We will source the inventories from Git based *.ini files*, which we maintain using a config-as-code approach using devops type practices.

First set up a new **Project** and *sync* it so that we know where to source the inventory information from. Select **Projects** in the UI and click **Add**:
![Setting up the Constructed Inventory](/images/posts/how-to-use-the-new-constructed-inventory-feature-in-aap-2.4/setting-up-the-constructed-inventory.png)

Once filled out and saved, the project will automatically sync:

![once filled out and saved the project will automatically sync](/images/posts/how-to-use-the-new-constructed-inventory-feature-in-aap-2.4/create-new-project.png)

Now we create the new Inventories that will reference the information from the Project files. Under Inventories click Create:

![create the new Inventories](/images/posts/how-to-use-the-new-constructed-inventory-feature-in-aap-2.4/create-new-inventory.png)

Now click on the Inventory **Sources** and **Add**:
![Inventories sources](/images/posts/how-to-use-the-new-constructed-inventory-feature-in-aap-2.4/inventory-source.png)

We provide a **Name** for this source, in this case for the **East Region** hosts, define the **Source** as **Sourced from a Project**, and provide the just added Project and appropriate [east.ini](https://github.com/AlanCoding/Ansible-inventory-file-examples/blob/master/issues/AWX371/east.ini) source file:

![create new source](/images/posts/how-to-use-the-new-constructed-inventory-feature-in-aap-2.4/create-new-source.png)

Once saved, click the **Sync** button to pull in the information:

![inventory details](/images/posts/how-to-use-the-new-constructed-inventory-feature-in-aap-2.4/inventory-details.png)

Once synced, you’ll be able to see what’s been processed if you view the job output:
![inventory output](/images/posts/how-to-use-the-new-constructed-inventory-feature-in-aap-2.4/inventory-output.png)

In this case, you’ll see it’s discovered and automatically added 3 hosts and 3 groups. You can see this information in the UI, under **Hosts**.

Now we must do the same for the **West Region**. I’ll leave that up to you as an exercise following the above example, but using [west.ini](https://github.com/AlanCoding/Ansible-inventory-file-examples/blob/master/issues/AWX371/west.ini) information as the source.

For this hypothetical scenario, we would like to run jobs against some of the hosts from the **East** and **West** regions simultaneously, based on criteria that we define.

So let’s now create a new **Constructed Inventory** in the UI:

![new constructed inventory ](/images/posts/how-to-use-the-new-constructed-inventory-feature-in-aap-2.4/new-constructed-inventory.png)

We add both cloud inventories as inputs. Then we will use source-vars to construct a new group “target_group”, and then use limit to filter on that group:

![target group details](/images/posts/how-to-use-the-new-constructed-inventory-feature-in-aap-2.4/target-group-details.webp)

Once synced, you can see what happens through the job output:
![job group output](/images/posts/how-to-use-the-new-constructed-inventory-feature-in-aap-2.4/job-group-output.png)

We now have 4 groups with 4 hosts, which you’ll be able to browse under **Hosts** and **Groups** in the UI to confirm the result. Let’s look at groups for this particular example:

![constructed combination groups](/images/posts/how-to-use-the-new-constructed-inventory-feature-in-aap-2.4/constructed-combination-groups.png)

When the constructed inventory update ran, it copied the “account_1234”, “account_4321”, and the “accounts” groups from the input inventories into the resultant constructed inventory. 

We also see that the constructed inventory also includes the “**target_group**” group which we will talk about shortly.

If this constructed inventory was used by a job template to run a job, any of the groups defined would be usable by the job.

Now for the main magic, if you refer to the **source-vars** in the constructed inventory form, you can find the definition of the new “**target_group**” group.

   ``plugin: constructed
    strict: true
    groups:
        target_group: account_alias | default("") == "product_dev"``

The “**target_group**” was not present in the original East and West inventories. It was created by the constructed inventory plugin when the update happened. 

In this case, hosts are added to the group when the jinja2 template false resolves to a truthy value (like 1, “1”, or True) for a given host. 

During the update, these templates are rendered by Ansible for every host in the input inventories to make these evaluations. For larger input inventories, this can be expected to take in the order of minutes to complete the update. 

Constructed inventories will automatically update before a job run of any template that uses it, but if those updates are taking too long, you can relax the frequency of updates with the **Update cache timeout** option in the Constructed Inventory settings in the UI. Setting this option to a value > 1 will cache the results of the constructed inventory update for that many seconds.

The jinja2 template to create “**target_group**” will include a host if, when inspecting that host, the hostvar of “**account_alias**” exists **and** is equal to “**product_dev**”. 

The “**| default**” syntax is necessary in the event that the variable is not defined for some hosts. 

The “**strict: true**” dictates that referencing an undefined variable will fail the inventory update, making the “| default” necessary. 

Using “|default| and the strict parameter is best practice, in order to force you to make the undefined case explicit.

Constructing groups can be useful to add groups on-the-fly to be referenced by playbooks. Why would you want to? Sometimes it is convenient to synthesize groups from hostvars, because you can do things with groups that you can’t do with hostvars, like using in host patterns, like with **limit** in this example. 

If you look at all the produced hosts for our constructed inventory:
![inventory group host](/images/posts/how-to-use-the-new-constructed-inventory-feature-in-aap-2.4/inventory-group-host.png)

We can see in this example that **host3** in the **east** inventory and **host5** in the **west** inventory are not included. This is because in the input inventories, they are in a different account (account_4321) which has an “account_alias” that does not match our specified “product_dev” value. Note that even though the group for account_4321 was imported into the constructed inventory, no hosts in that group matched our requirement so the imported group is empty in our constructed inventory.

Source vars input can include **host** variables, in addition to adding groups.

Alan’s Github repository also contains another example, which you may find useful. In [construct.yml](https://github.com/AlanCoding/Ansible-inventory-file-examples/blob/master/issues/AWX371/construct.yml) we resolve the ‘state’ of a host, and assign it to a number of groups based on whether its shutdown or part of a particular environment (dev). The source of truth for this .yml file can come from other systems outside of Ansible Automation Platform, and we can use it to perform automation runs against subsets of hosts on-the-fly.

# Debugging Tips
To use the prior example, when developing the constructed inventory, consider that you delete the limit value and change the source-vars to the following content.

![constructed groups details](/images/posts/how-to-use-the-new-constructed-inventory-feature-in-aap-2.4/inventory-group--combine-details.webp)

This will run a similar template of and save it to a variable named “effective_account_alias”. By making *limit* blank, we will be sure to get all hosts from the input inventories. This would allow us to inspect fine-grained details of the inclusion criteria on individual hosts, shown below for host3.

![host3 host details](/images/posts/how-to-use-the-new-constructed-inventory-feature-in-aap-2.4/host3-host-details.webp)

Here, we see the **hostvar**“ effective_account_alias” evaluated value is “sustaining” and not “product_dev”. 

The constructed inventory plugin has a number of other options which can be very useful and powerful. Refer to the plugin documentation at https://docs.ansible.com/ansible/latest/collections/ansible/builtin/constructed_inventory.html for further details.

A few other examples can also be found in the user guide at https://docs.ansible.com/automation-controller/4.4/html/userguide/inventories.html#ug-inventories-constructed

 

# Summary:
Hopefully this has given a picture of the practical use of constructed inventory inside of Ansible Automation Platform. 

Because the underlying concepts like host pattern and the constructed inventory plugin are general Ansible concepts, users will be able to add groups, variables, or include hosts based on arbitrarily complex criteria.

The benefits include:

- The ability to create **groups** dynamically from multiple sources of truth.
- The ability to filter out, parse and limit hosts from multiple inventories, but allowing them to be used in automation runs.
- The ability to make use of pre-defined hostvars when filtering.
- Multiple teams can own their own inventory and metadata associated with their hosts and it can be used centrally through Ansible Automation Platform.
 

**Share:**    

**Topics:**

[AWX](https://www.ansible.com/blog/topic/awx), [Ansible Automation Platform](https://www.ansible.com/blog/topic/ansible-automation-platform)