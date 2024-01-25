---
author: Ganesh Nalawade
date: 2021-01-21 00:00 UTC
description: This blog post will walk through the automation workflow
  for validation of operational state and even automatic remediation of
  issues.
lang: en-us
title: Using New Ansible Utilities for Operational State Management and Remediation
---

# Using New Ansible Utilities for Operational State Management and Remediation

Comparing the current operational state of your IT infrastructure to
your desired state is a common use case for IT automation.  This allows
automation users to identify drift or problem scenarios to take
corrective actions and even proactively identify and solve problems. 
This blog post will walk through the automation workflow for validation
of operational state and even automatic remediation of issues.

We will demonstrate how the Red Hat supported and certified Ansible
content can be used to:

-   Collect the current operational state from the remote host and
    convert it into normalised structure data.
-   Define the desired state criteria in a standard based format that
    can be used across enterprise infrastructure teams.
-   Validate the current state data against the pre-defined criteria to
    identify if there is any deviation.
-   Take corrective remediation action as required.
-   Validate input data as per the data model schema

## Gathering state data from a remote host

The recently released
[ansible.utils](https://galaxy.ansible.com/ansible/utils)
version 1.0.0 Collection has added support for
[ansible.utils.cli_parse](https://github.com/ansible-collections/ansible.utils/blob/main/docs/ansible.utils.cli_parse_module.rst)
module, which converts text data into structured JSON format.  The
module has the capability to either execute the command on the remote
endpoint and fetch the text response, or read the text from a file on
the control node to convert it into structured data.  This module can
work with both traditional Linux servers as well as vendor appliances,
such as network devices that don't have the ability to execute Python,
and the module relies on well-known text parser libraries for this
conversion. The current supported CLI parser sub plugin engines are as
below:

1.  [ansible.utils.textfsm](https://github.com/ansible-collections/ansible.utils/blob/main/plugins/sub_plugins/cli_parser/textfsm_parser.py)
    Uses[ textfsm python library](https://pypi.org/project/textfsm/)
2.  [ansible.utils.ttp](https://github.com/ansible-collections/ansible.utils/blob/main/plugins/sub_plugins/cli_parser/ttp_parser.py)
    Uses[ ttp python library](https://pypi.org/project/ttp/)
3.  [ansible.netcommon.native](https://github.com/ansible-collections/ansible.netcommon/blob/main/plugins/sub_plugins/cli_parser/native_parser.py)
    Uses netcommon inbuilt parser engine
4.  [ansible.netcommon.ntc_templates](https://github.com/ansible-collections/ansible.netcommon/blob/main/plugins/sub_plugins/cli_parser/ntc_templates_parser.py)
    Uses [ntc_templates python library](https://pypi.org/project/ntc-templates/)
5.  [ansible.netcommon.pyats](https://github.com/ansible-collections/ansible.netcommon/blob/main/plugins/sub_plugins/cli_parser/pyats_parser.py)
    Uses [pyats python library](https://pypi.org/project/pyats/)
6.  [ansible.utils.xml](https://github.com/ansible-collections/ansible.utils/blob/main/plugins/sub_plugins/cli_parser/xml_parser.py)Uses
    [xmltodict python library](https://pypi.org/project/xmltodict/) 
7.  [ansible.utils.json](https://github.com/ansible-collections/ansible.utils/blob/main/plugins/sub_plugins/cli_parser/json_parser.py)

![state assessment blog](/images/posts/archive/state-assessment-blog.png)

The examples described in this blog uses Cisco network switch, NXOS
version 7.3(0)D1(1), as the remote endpoint and Ansible version 2.9.15
running on the control node and requires
[ansible.utils](https://galaxy.ansible.com/ansible/utils),
[ansible.netcommon](https://galaxy.ansible.com/ansible/netcommon) and
[cisco.nxos ](https://galaxy.ansible.com/cisco/nxos)Collections to be
installed on the control node.

The below [Ansible snippet](https://gist.github.com/ganeshrn/f763e299cb4896b548c586b57041ee73)
fetches the operational state of the interfaces and translates it to
structured data using **ansible.netcommon.pyats** parser. This parse
requires [pyats](https://pypi.org/project/pyats/) library to be
installed on the control node.

```yaml
---
- hosts: nxos
  connection: ansible.netcommon.network_cli
  gather_facts: false
  vars:
    ansible_network_os: cisco.nxos.nxos
    ansible_user: "changeme"
    ansible_password: "changeme"

  tasks:
  - name: "Fetch interface state and parse with pyats"
    ansible.utils.cli_parse:
      command: show interface
      parser:
        name: ansible.netcommon.pyats
    register: nxos_pyats_show_interface

  - name: print structured interface state data
    ansible.builtin.debug:
      msg: "{{ nxos_pyats_show_interface['parsed'] }}"
```

The value of the **command** option in **ansible.utils.cli_parse** task
is the command that should the executed on the remote host,
alternatively, the task can accept a **text** option that accepts the
value directly in string format and can be used in case the response of
the command is already prefetched. The **name** option under the
**parser** parent option can be any one of the above-discussed parser
sub plugins.

After running the playbook, the output of **ansible.utils.cli_parse**
task for the given host is as shown for reference:

```json
ok: [nxos] => {
   "changed": false,
   "parsed": {
       "Ethernet2/1": {
           "admin_state": "down",
           "auto_mdix": "off",
           "auto_negotiate": false,
           "bandwidth": 1000000,
           "beacon": "off"
           <--snip-->
       },
       "Ethernet2/10": {
           "admin_state": "down",
           "auto_mdix": "off",
           "auto_negotiate": false,
           "bandwidth": 1000000,
           "beacon": "off",
           <--snip-->
       }
   }
```

Notice the value of **admin_state** key for some of the interfaces is
**down**, for the complete output refer
[here](https://gist.github.com/ganeshrn/79a7a2670ce03fe381678f9796482089).

## Defining state criteria and validation

The [ansible.utils](https://galaxy.ansible.com/ansible/utils) Collection
has added support for the
[ansible.utils.validate](https://github.com/ansible-collections/ansible.utils/blob/main/docs/ansible.utils.validate_module.rst)
module, which validates the input JSON data with the provided criteria
based on the validation engine. The currently supported validation
engine is [jsonschema](https://pypi.org/project/jsonschema/), and in
future support for additional validation, engines will be added on a
need basis. 

In the above section, we fetched the interface state and converted to
structured JSON data. Suppose if we want the desired admin state for all
the interfaces to always be in **up** state the [criteria for
jsonschema](https://gist.github.com/ganeshrn/0a479d580caa96326a7c8186c4b12d7d)
will look like:

```json
$cat criterias/nxos_show_interface_admin_criteria.json
{
        "type" : "object",
        "patternProperties": {
                "^.*": {
                        "type": "object",
                        "properties": {
                                "admin_state": {
                                        "type": "string",
                                        "pattern": "up"
                                }
                        }
                }
        }
```

After the criteria for the desired state of the resource is defined, it
can be used with the **ansible.utils.validate** module to check if the
current state of the resource matches with the desired state as shown in
the below
[task](https://gist.github.com/ganeshrn/d9a3049673bd8bec1cbd4b717cf56c99).

```yaml
- name: validate interface for admin state
  ansible.utils.validate:
    data: "{{ nxos_pyats_show_interface['parsed'] }}"
    criteria:
      - "{{ lookup('file',  './criterias/nxos_show_interface_admin_criteria.json') | from_json }}"
    engine: ansible.utils.jsonschema
  ignore_errors: true
  register: result

- name: print the interface names that does not satisfy the desired state
  ansible.builtin.debug:
    msg: "{{ item['data_path'].split('.')[0] }}"
  loop: "{{ result['errors'] }}"
  when: "'errors' in result"
```

The **data** option of **ansible.utils.validate** task accepts a JSON
value and in this case, it is the output parsed from
**ansible.utils.cli_parse** module as discussed above. The value of
**engine** option is the sub plugin name of the validate module that is
[ansible.utils.jsonschema](https://github.com/ansible-collections/ansible.utils/blob/main/docs/ansible.utils.jsonschema_validate.rst),
and it identifies the underlying validation library to be used; in this
case, we are using **jsonschema** library. The value of the **criteria**
option can be a list and should be in a format that is defined by the
validation engine used. For the above to run
[jsonschema](https://pypi.org/project/jsonschema/), installing a library
is required on the control node. The output of the above task run will
be a list of errors indicating interfaces that do not have admin value
in **up** state. The reference output can be seen
[here](https://gist.github.com/ganeshrn/912d88b7ff5b6a959e82c4935d9b4d0c)
(note: the output will vary based on the state of the interfaces on the
remote host).

```bash
TASK [validate interface for admin state] ***********************************************************************************************************
fatal: [nxos02]: FAILED! => {"changed": false, "errors": [{"data_path": "Ethernet2/1.admin_state", "expected": "up", "found": "down", "json_path": "$.Ethernet2/1.admin_state", "message": "'down' does not match 'up'", "relative_schema": {"pattern": "up", "type": "string"}, "schema_path": "patternProperties.^.*.properties.admin_state.pattern", "validator": "pattern"}, {"data_path": "Ethernet2/10.admin_state", "expected": "up", "found": "down", "json_path": "$.Ethernet2/10.admin_state", "message": "'down' does not match 'up'", "relative_schema": {"pattern": "up", "type": "string"}, "schema_path": "patternProperties.^.*.properties.admin_state.pattern", "validator": "pattern"}], "msg": "Validation errors were found.\nAt 'patternProperties.^.*.properties.admin_state.pattern' 'down' does not match 'up'. \nAt 'patternProperties.^.*.properties.admin_state.pattern' 'down' does not match 'up'. \nAt 'patternProperties.^.*.properties.admin_state.pattern' 'down' does not match 'up'. "}
...ignoring
```

```bash
TASK [print the interface names that does not satisfy the desired state] ****************************************************************************
Monday 14 December 2020  11:05:38 +0530 (0:00:01.661)       0:00:28.676 *******
ok: [nxos] => {
   "msg": "Ethernet2/1"
}
ok: [nxos] => {
   "msg": "Ethernet2/10"
}

PLAY RECAP ******************************************************************************************************************************************
nxos                       : ok=4    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=1
```

As seen from the above output, the interface **Ethernet2/1** and
**Ethernet2/10** are not in the desired state as per the defined
criteria.

## Remediation

Based on the output of the **ansible.utils.validate** task, a number of
remediation actions can be taken using Ansible modules for configuration
management and/or reporting. In our case, we will be using the
[cisco.nxos.nxos_interfaces](https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_interfaces_module.rst)
resource module to configure the given interfaces in admin **up** state
as shown in the below
[snippet](https://gist.github.com/ganeshrn/58f1346aa3dad4ce771fe4cb9420349f).

```yaml
- name: Configure interface with drift in admin up state
  cisco.nxos.nxos_interfaces:
    config:
    - name: "{{ item['data_path'].split('.')[0] }}"
      enabled: true
  loop: "{{ result['errors'] }}"
  when: "'errors' in result"
```

This remediation task will be executed only when the validation from the
earlier task fails and will run only for those interfaces whose admin
state is not up.

## Data validation

It is often required to validate the data before giving it as an input
to the task to ensure the input data structure is  per the expected data
model.  This allows us to validate data model adherence prior to pushing
configuration to the network device. This use case is explained in the
[data validation](https://www.ipspace.net/kb/DataModels/70-Validation.html)
blog from [Ivan Pepelnjak](https://www.ipspace.net/Main_Page).

![state assessment blog two](/images/posts/archive/state-assessment-blog-two.png)

The blog uses command-line tools to validate the input data, however
with the support of the **ansible.utils.validate** module, this
functionality can now be added in the Ansible Playbook itself as shown
in the below
[snippet](https://gist.github.com/ganeshrn/11ef6cf725ee8fbc4f7a1bbffe5eb92b).

```yaml
- name: validate bgp data data with jsonschema bgp model criteria
  ansible.utils.validate:
    data: "{{ hostvars }}"
    criteria:
      - "{{ lookup('file', './bgp_data_model_criteria.json') |  from_json }}"
    engine: ansible.utils.jsonschema
  register: result
```

The criteria structure stored in **bgp_data_model_criteria.json** file
locally can be referred
[here](https://gist.github.com/ganeshrn/aef7f74d132199b5ddb379d49fe314f7) 
(modified example from the [original blog
post](https://www.ipspace.net/kb/DataModels/70-Validation.html)) and the
sample `host_vars` file as below:

```bash
$cat host_vars/nxos.yaml
---
bgp_as: 0
description: Unexpected
```

The output of the above task run can be seen as below:

```bash
TASK [validate bgp data data with jsonschema bgp model criteria] *******************************************************************************************
fatal: [nxos]: FAILED! => {"changed": false, "errors": [{"data_path": "nxos.bgp_as", "expected": 1, "found": 0, "json_path": "$.nxos.bgp_as", "message": "0 is less than the minimum of 1", "relative_schema": {"maximum": 65535, "minimum": 1, "type": "number"}, "schema_path": "patternProperties..*.properties.bgp_as.minimum", "validator": "minimum"}], "msg": "Validation errors were found.\nAt 'patternProperties..*.properties.bgp_as.minimum' 0 is less than the minimum of 1. "}
```
