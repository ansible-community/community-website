---
title: Kubernetes Meets Event-Driven Ansible
author: Andrew Block
date: 2023-03-16 13:00:00
slug: kubernetes-meets-event-driven-ansible
category: event-driven-ansible
tags: event-driven-ansible, kubernetes, rulebooks, eda, ansible-rulebook
type: text
---

# __The Inside Playbook__

![Kubernetes Meets Event-Driven Ansible](/images/posts/kubernetes-meets-event-driven-ansible/Kubernetes%20+%20EDA.webp)

In today’s fast paced world, every second counts and the ability to react to activities in a timely fashion can mean the difference between satisfying the needs of consumers and meeting Service-Level Agreements. Each are goals of [Event-Driven Ansible](https://www.ansible.com/use-cases/event-driven-automation), which seeks to further the reach of Ansible based automation by responding to events that meet certain criteria. These events can originate from a variety of sources, such as from an HTTP endpoint, messages on a queue or topic, or from public cloud resources. Kubernetes has become synonymous with managing infrastructure and applications in cloud native architectures and many organizations are reliant on these systems for running their business critical workloads. Automation and Kubernetes go hand in hand and Ansible already plays a role within this ecosystem. A new capability leveraging the Event-Driven Ansible framework is now available that extends the integration between both Ansible and Kubernetes so that Ansible automation activities can be triggered based on events and actions occurring within a Kubernetes cluster.

Event-Driven Ansible is designed using a concept called Rulebooks which consists of three main components:

- Actions - Triggering the execution of assets including an Ansible Playbook or module 
- Rules - Determination of whether received events match certain conditions 
- Sources - Origination of events from external entities that are consumed and processed within the Ansible eventing framework

There is a wide ecosystem of solutions available to manage Kubernetes from Ansible, which is provided primarily through the [kubernetes.core collection](https://github.com/ansible-collections/kubernetes.core). This Collection contains everything ranging from mechanisms to manage resources within a Kubernetes cluster, support for the Helm package manager to leveraging a Kubernetes cluster as an inventory source. There are capabilities made available now through the integration of Kubernetes and the Event-Driven Ansible framework. Event sources enable the consumption of changes originating from a Kubernetes cluster, which can be used to trigger automation to respond and act based on the received content and the configured rules. Let’s explore how to take advantage of this newly created capability to further the integration between Kubernetes and Ansible.

The assets related to Event-Driven Ansible and Kubernetes are located within the [sabre1041.eda collection](https://galaxy.ansible.com/sabre1041/eda) within Ansible Galaxy. Ensure that the control node where the Ansible automation will be executed has the necessary tooling installed and configured. This includes Ansible Core, the tooling associated with Event-Driven Ansible, and the Collection containing the Event-Driven Ansible Kubernetes integration. Consult the associated documentation for both [Ansible Core](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html) and [Event-Driven Ansible](https://www.ansible.com/blog/getting-started-with-event-driven-ansible) for the target Operating System and installation method.

Once both Ansible Core and Event-Driven Ansible have been installed and configured, install the sabre1041.eda collection by executing the following command:

```
ansible-galaxy collection install sabre1041.eda
```

This Collection also requires that the Python [requests](https://requests.readthedocs.io/en/latest/) package be installed which can be facilitated by executing the following command:

```
pip install requests
```

Now that all of the prerequisite tooling has been met, attention can be turned to how a Rulebook can be configured to take advantage of the Kubernetes integration. Events in the Event-Driven Ansible architecture are configured within the sources section of a rulebook. One or more sources can be specified within a rulebook enabling a robust set of conditions and actions to be configured.

A basic rulebook that takes advantage of the k8s event source plugin from the Collection is shown below:

```
- name: Listen for newly added ConfigMap resources
  hosts: all
  sources:
    - sabre1041.eda.k8s:
        api_version: v1
        kind: ConfigMap
        namespace: default
  rules:
    - name: Notify
      condition: event.type == "ADDED"
      action:
        debug:  
```

The k8s plugin is modeled in a similar manner to that of the [k8s module](https://docs.ansible.com/ansible/latest/collections/kubernetes/core/k8s_module.html) from the kubernetes.core collection, so anyone with familiarity working with this module will feel at home when working with this k8s source plugin.





The logic of this rulebook is as follows:

1. Connect to a remote Kubernetes cluster and consume changes to ConfigMap resources that occur within the default namespace
2. The k8s source plugin includes the type and content to the event object whenever a change occurs within the Kubernetes cluster
3. Execute the debug action which will print out the event and any other associated variables only when the type property on the event is equal to “ADDED” (whenever a ConfigMap is added to the cluster).

While this rulebook monitors for changes in a specific namespace, support is available for monitoring changes across an entire Kubernetes cluster by omitting the use of the namespace parameter in the source plugin. If access to the default namespace is forbidden, feel free to select another namespace where access is granted.

To demonstrate the use of this rulebook, add the previously provided content to a new rulebook file called k8s-eda-demo.yaml. In addition, ensure that the local machine is authenticated to a Kubernetes cluster or customize the plugin parameters to specify the location of the Kubernetes cluster that should be used. Consult the [plugin documentation](https://github.com/sabre1041/sabre1041.eda/blob/main/docs/sabre1041.eda.k8s_source_plugin.rst) for the available options.

Create a simple [inventory](https://docs.ansible.com/ansible/latest//inventory_guide/intro_inventory.html#intro-inventory) in a file called inventory with the following content:

``` 
localhost
```

Run the rulebook to begin consuming events by executing the following command:

```
ansible-rulebook -i inventory --rulebook k8s-eda-demo.yaml --verbose

```

With the rulebook monitoring for ConfigMap changes in the default namespace, create a new ConfigMap in the default namespace to demonstrate events are being captured appropriately. This task can be accomplished by using the Kubernetes CLI (kubectl) by executing the following command:

 
~~~
kubectl create configmap -n default eda-example --from-literal=message=”Kubernetes Meets Event-Driven Ansible”
~~~

Observe the following has been captured and displayed in the window where the ansible-rulebook command is being executed.

```
kwargs:
{'facts': {},
 'hosts': ['all'],
 'inventory': 'localhost',
 'project_data_file': None,
 'ruleset': 'Listen for newly added ConfigMap resources',
 'source_rule_name': 'Notify',
 'source_ruleset_name': 'Listen for newly added ConfigMap resources',
 'variables': {'event': {'resource': {'apiVersion': 'v1',
                                      'data': {'message': 'Kubernetes Meets '
                                                          'Event-Driven '
                                                          'Ansible'},
                                      'kind': 'ConfigMap',
                                      'metadata': {'creationTimestamp': '2022-12-25T17:40:43Z',
                                                   'managedFields': [{'apiVersion': 'v1',
                                                                      'fieldsType': 'FieldsV1',
                                                                      'fieldsV1': {'f:data': {'.': {},
                                                                                              'f:message': {}}}, 
                                                                      'manager': 'kubectl-create',
                                                                      'operation': 'Update',
                                                                      'time': '2022-12-25T17:40:43Z'}],
                                                   'name': 'eda-example',
                                                   'namespace': 'default',
                                                   'resourceVersion': '119407',
                                                   'uid': '2862db59-8990-4a37-9433-50dcfbaa6d71'}},
                         'type': 'ADDED'},
               'fact': {'resource': {'apiVersion': 'v1',
                                     'data': {'message': 'Kubernetes Meets '
                                                         'Event-Driven '
                                                         'Ansible'},
                                     'kind': 'ConfigMap',
                                     'metadata': {'creationTimestamp': '2022-12-25T17:40:43Z',
                                                  'managedFields': [{'apiVersion': 'v1',
                                                                     'fieldsType': 'FieldsV1',
                                                                     'fieldsV1': {'f:data': {'.': {},
                                                                                             'f:message': {}}},
                                                                     'manager': 'kubectl-create',
                                                                     'operation': 'Update',
                                                                     'time': '2022-12-25T17:40:43Z'}],
                                                  'name': 'eda-example',
                                                  'namespace': 'default',
                                                  'resourceVersion': '119407',
                                                  'uid': '2862db59-8990-4a37-9433-50dcfbaa6d71'}},
                        'type': 'ADDED'}}}
```

As shown in the output above, the details associated with the newly created ConfigMap within the Kubernetes cluster and the event have been captured.

After confirming that the Kubernetes source plugin is capturing events successfully, let’s demonstrate how one could make use of these events within an Ansible Playbook. Create a new file called k8s-eda-demo-playbook.yaml with the following content.

```
- hosts: localhost
  connection: local
  tasks:
    - ansible.builtin.debug:
        msg: "ConfigMap in namespace '{{ event.resource.metadata.namespace }}' with name '{{ event.resource.metadata.name }} ‘{{ event.type | capitalize }}’ with the message ‘{{ event.resource.data.message}}'"

```

This playbook demonstrates how to obtain properties that are included on the captured event. The type property will display “Added” as the playbook will only execute when ConfigMaps that have been created. The ConfigMap object itself can be accessed by referencing the resource property on the event. The standard Kubernetes manifest for a ConfigMap can then be traversed, such as the _namespace, name_ as well as specific *data values*. 

Update the contents of the rulebook in the k8s-eda-demo.yaml file to invoke the newly created playbook instead of simply printing out the contents by using the run_playbook action as shown below:

```
- name: Listen for newly added ConfigMap resources
  hosts: all
  sources:
    - sabre1041.eda.k8s:
        api_version: v1
        kind: ConfigMap
        namespace: default
  rules:
    - name: Execute Playbook
      condition: event.type == "ADDED"
      action:
        run_playbook:
          name: k8s-eda-demo-playbook.yaml   
```

Once again, execute the k8s-eda-demo-playbook.yaml rulebook to begin listing for ConfigMap’s added to the _default_ namespace.

```
ansible-rulebook -i inventory --rulebook k8s-eda-demo.yaml --verbose 
```

Delete and recreate the ConfigMap to trigger the playbook.

```
kubectl delete configmap -n default eda-example

kubectl create configmap -n default eda-example --from-literal=message=”Kubernetes Meets Event-Driven Ansible”
```

Observe that the playbook has been triggered and produces output similar to the following:

```
TASK [ansible.builtin.debug] ***************************************************
ok: [localhost] => {
    "msg": "ConfigMap in namespace 'default' with name 'eda-example ‘Added’ with the message ‘Kubernetes Meets Event-Driven Ansible'"
}
```

While this example only prints out a simple message related to the content of the event received, it provides a demonstration of how to make use of the capabilities enabled by the Kubernetes integration. By adding Kuberentes as an event source and into the Event-Driven Ansible ecosystem, it becomes an essential integration to help support organizations that are leveraging Kubernetes to maintain crucial components of their business and to trigger automation as desired.

__Topics:__

[Event-Driven Ansible](https://www.ansible.com/blog/topic/event-driven-ansible)