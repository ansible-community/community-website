---
title: Ansible data manipulation with a Filter
author: Sean Sullivan
date: 2023-08-03 13:00:00
slug: ansible-data-manipulation-with-a-filter
category: developer
tags: developer, filters, playbook
type: text
---
This year at Summit, an attendee posed a question about how to work with setting facts and changing data in Ansible. Many times we’ve come across people using task after task to manipulate data, to turn items into lists, filter our options, trying to do heavy data manipulation and to turn data from one source into another. Trying to make these programmatic changes using a mixture of YAML and Jinja inside of roles and playbooks is a headache of its own. While many of these options will work, they aren’t very efficient or easy to implement. Ansible Playbooks were never meant for programming.

One solution that is usually overlooked is to do the manipulation in Python inside of a module or a filter. This article will detail how to create a filter to manipulate data. In addition, [a repository for all code referenced](https://github.com/sean-m-sullivan/ansible_data_manipulation_examples) in this article has been created.

This example was first developed as a module. However after review, it was determined that these data transformations are best done as filters. Filters can take multiple data inputs, do the programmatic operations, and then can be used in line where they are used as input or set as a fact. In addition, this runs locally and not at the host level, so it can be faster and avoid unnecessary connections.

# Starting Point

To begin, we need a dataset to work on. For this we used data from the automation controller API, workflows; it gives nested data on the nodes in each workflow to loop around. The variable file used in this case [can be found in the repo](https://github.com/sean-m-sullivan/ansible_data_manipulation_examples/blob/main/workflows.yml).

The goal is to find what is being used in the automation controller looping over nested lists. While this is not a very practical example, it does give a starting point for creating a filter to manipulate any dataset.

# Filter Basics

The bones of this filter were taken from [ansible.netcommon.pop_ace](https://github.com/ansible-collections/ansible.netcommon/blob/main/plugins/filter/pop_ace.py). The start of every filter has some required options, such as FilterModule, and in addition AnsibleFilterError is good for troubleshooting.

```python
from ansible.errors import AnsibleFilterError
```


The class invocation sets the code as a filter, and invokes the function to use for the filter. This sets the filter called "used" in the playbook, and the function to invoke. Note that the function and the filter name do not need to match.

```python
class FilterModule(object):
    def filters(self):
        return {"example_filter": self.workflow_manip}
```

Then there is the documentation section: This can contain inputs, examples and other metadata. This is also how the ansible-docs are populated.

```python
EXAMPLES = r"""
    - name: Transform Data
        ansible.builtin.set_fact:
        data_out: "{{ workflow_job_templates | example_filter }}"
    """
```

For the most part this should be standard information. While the documentation field is not required for filters, it is best practice to include it. While not shown here, the [linked example](https://github.com/sean-m-sullivan/ansible_data_manipulation_examples/blob/main/filter_plugins/example_filter.py) also includes commented out expected output, which is great for going back and troubleshooting in the future.

# Setting things up


The first thing to do is set the filter arguments for data coming in. In our case the variable data_in, and that the input is of type dict. It is also best to set the return variable as empty here and any other defaults that need defined.

```python
def example_filter(self, data_in: dict):
        workflow_data = {}
        workflow_data["workflows"] = []
        workflow_data["job_templates"] = []
        workflow_data["inventory_sources"] = []
        workflow_data["approval_nodes"] = []
```

The next step is to do the actual data manipulation.

# In the thick of it

This is where we get to what we actually want to do, take data from a source, loop through it, and extract the data needed. As the data is contained in nested lists, there is an inner and outer loop to go through.

```python
for workflow in data_in:
        workflow_data["workflows"].append(workflow["name"])
        for node in workflow["related"]["workflow_nodes"]:
            if node["unified_job_template"]["type"] == "inventory_source":
                workflow_data["inventory_sources"].append(
                    	node["unified_job_template"]["name"]
                )
            elif node["unified_job_template"]["type"] == "job_template":
                workflow_data["job_templates"].append(
                    node["unified_job_template"]["name"]
                )
            elif node["unified_job_template"]["type"] == "workflow_approval":
                workflow_data["approval_nodes"].append(
                    node["unified_job_template"]["name"]
                )
            else:
                raise AnsibleFilterError(
                    "Failed to find valid node: {0}".format(workflow)
                )
```

The first loop is to find the workflow name field and append it to the workflow list. The next loop goes through each workflow node, finds what type it is, and appends it to the appropriate list.

At the end is the error message, which should not be hit with valid data, however it is a useful bit of code to insert elsewhere when building or troubleshooting modules to force output to console in order to figure out what is going on. At the end of our manipulations, return with the result variable. The alternative would be [three tasks](https://github.com/sean-m-sullivan/ansible_data_manipulation_examples/blob/main/data_manip_facts.yaml), of which two would use loops, to achieve the same results. By using an actual programming language, its available libraries, and internalized loops, it simplifies the playbook, and provides better logic then what could be cobbled together using YAML and Jinja2 alone.

# Summary

Hopefully this article provides a starting point for creating filters and simplifying tasks in playbooks. Just like everything in Ansible, there is not a single solution, there are 10 options to choose from. Not every solution fits the situation at hand. Hopefully this provides another better option to work with.
