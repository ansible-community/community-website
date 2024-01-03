---
author: Colin McCarthy
date: 2019-07-19 00:00 UTC
description: This blog is part two in a series covering how Red Hat
  Ansible Automation can integrate with ticket automation. This time
  we'll cover dynamically adding a set of network facts from your
  switches and routers and into your ServiceNow tickets.
lang: en-us
title: Ansible and ServiceNow Part 2, Parsing facts from network devices using PyATS/Genie
---

# Ansible and ServiceNow Part 2, Parsing facts from network devices using PyATS/Genie

![blog_ansible-and-service-now-part2](https://www.ansible.com/hs-fs/hubfs/Images/blog-social/blog_ansible-and-service-now-part2.png?width=1024&name=blog_ansible-and-service-now-part2.png){width="1024"
style="width: 1024px;"
srcset="https://www.ansible.com/hs-fs/hubfs/Images/blog-social/blog_ansible-and-service-now-part2.png?width=512&name=blog_ansible-and-service-now-part2.png 512w, https://www.ansible.com/hs-fs/hubfs/Images/blog-social/blog_ansible-and-service-now-part2.png?width=1024&name=blog_ansible-and-service-now-part2.png 1024w, https://www.ansible.com/hs-fs/hubfs/Images/blog-social/blog_ansible-and-service-now-part2.png?width=1536&name=blog_ansible-and-service-now-part2.png 1536w, https://www.ansible.com/hs-fs/hubfs/Images/blog-social/blog_ansible-and-service-now-part2.png?width=2048&name=blog_ansible-and-service-now-part2.png 2048w, https://www.ansible.com/hs-fs/hubfs/Images/blog-social/blog_ansible-and-service-now-part2.png?width=2560&name=blog_ansible-and-service-now-part2.png 2560w, https://www.ansible.com/hs-fs/hubfs/Images/blog-social/blog_ansible-and-service-now-part2.png?width=3072&name=blog_ansible-and-service-now-part2.png 3072w"
sizes="(max-width: 1024px) 100vw, 1024px"}

This blog is part two in a series covering how Red Hat Ansible
Automation can integrate with ticket automation. This time we'll cover
dynamically adding a set of network facts from your switches and routers
and into your ServiceNow tickets. If you missed Part 1 of this blog
series, you can refer to it via the following link: [Ansible +
ServiceNow Part 1: Opening and Closing
Tickets](/blog/ansible-servicenow-opening-and-closing-tickets){rel=" noopener"}.

Suppose there was a certain network operating system software version
that contained an issue you knew was always causing problems and making
your uptime SLA suffer. How could you convince your management to
finance an upgrade project? How could you justify to them that the fix
would be well worth the cost? Better yet, how would you even know?

A great start would be having metrics that you could track. The ability
to data mine against your tickets would prove just how many tickets were
involved with hardware running that buggy software version. In this
blog, I'll show you how to automate adding a set of facts to all of your
tickets going forward. Indisputable facts can then be pulled directly
from the device with no chance of mistakes or accidentally being
overlooked and not created.

This blog post will demonstrate returning structured data in JSON using
Ansible in conjunction with Cisco pyATS and Cisco Genie. This allows us
to retrieve the output from operational show commands and convert them
in any format we want, in this case pushing them into ServiceNow.

There are many ways to parse facts from network devices with Ansible.
The following blog example could also all be done via the open source
[Network Engine Ansible
Role](https://galaxy.ansible.com/ansible-network/network-engine), but
for this example we are using Cisco's sponsored pyATS/Genie
implementation to parse the following show version command. As you can
see this is not very friendly to programmatically interact with:

![image7](https://www.ansible.com/hubfs/image7.png)


# Step 1: Create a Python3 virtual environment in Red Hat Ansible Tower

With the release of Ansible Tower 3.5, we can now use Python 3 virtual
environments (virtualenv) for added playbook flexibility and
compatibility across Python versions. This is great news because Python3
is required to use the pyATS and Genie packages. We need to create a new
(virtualenv) that is running Python3 and install all of the
dependencies.

    su -
    yum -y install rh-python36
    yum -y install python36-devel gcc
    scl enable rh-python36 bash
    python3.6 -m venv /var/lib/awx/venv/pyats-sandbox
    source /var/lib/awx/venv/pyats-sandbox/bin/activate
    umask 0022
    pip install pyats genie python-memcached psutil pysnow paramiko
    pip install -U "ansible == 2.8

Once a custom virtualenv is created a new field appears in the Job
Templates section in Ansible Tower. You can select your newly created
venv from the following dropdown
menu:![image1-6](https://www.ansible.com/hs-fs/hubfs/image1-6.png?width=930&name=image1-6.png){width="930"
style="width: 930px;"
srcset="https://www.ansible.com/hs-fs/hubfs/image1-6.png?width=465&name=image1-6.png 465w, https://www.ansible.com/hs-fs/hubfs/image1-6.png?width=930&name=image1-6.png 930w, https://www.ansible.com/hs-fs/hubfs/image1-6.png?width=1395&name=image1-6.png 1395w, https://www.ansible.com/hs-fs/hubfs/image1-6.png?width=1860&name=image1-6.png 1860w, https://www.ansible.com/hs-fs/hubfs/image1-6.png?width=2325&name=image1-6.png 2325w, https://www.ansible.com/hs-fs/hubfs/image1-6.png?width=2790&name=image1-6.png 2790w"
sizes="(max-width: 930px) 100vw, 930px"}

Cisco has released two Python3 packages that are very useful for network
automation - pyATS, and Genie. The first one, pyATS, functions as a
python framework while Genie builds on top of it. Genie can be used to
parse, learn, and diff. Implementing Genie is accomplished by installing
and calling the Galaxy role in our playbook named parse_genie.

# Step 2: Create a requirements.yml file in your roles directory

roles/requirements.yml

    ---
    - name: parse_genie
      src: https://github.com/clay584/parse_genie
      scm: git
      version: master

By default, Ansible Tower has a system-wide setting that allows roles to
be dynamically downloaded via a requirements.yml file in your Git repo.
So there is no need to run the
`ansible-galaxy install -r roles/requirements.yml` command like you
might do if using Ansible Engine on the CLI.\
For more information about Projects in Ansible Tower, [refer to the
documentation](https://docs.ansible.com/ansible-tower/latest/html/userguide/projects.html){rel=" noopener"}.

# Step 3: Call the parse_genie Ansible Role

Now that you have a Python 3 virtualenv in Tower and a
roles/requirements.yml file, you can write and test a playbook. In the
first play of the playbook, define the name, hosts identified for
Ansible to run against, the connection plugin and disabling gather_facts
for network devices. Next, create a roles: section and invoke the
parse_genie role:

    ---
    - name: parser example
      hosts: ios
      gather_facts: no
      connection: network_cli
      roles:
        - parse_genie

Then create the tasks: section and add a show version task. This will
execute the show version command via the ios_command module, then store
the output to a variable named version.

      tasks:
      - name: show version
        ios_command:
          commands:
            - show version
          register: version

The next tasks will apply the parse_genie filter plugin to create
structured data out of the show version command we executed. As well as
set the structured data as a fact and debug it.

      - name: Set Fact Genie Filter
        set_fact:
          pyats_version: "{{ version['stdout'][0] | parse_genie(command='show version', os='ios') }}"
        
      - name: Debug Genie Filter
        debug:
          var: pyats_version

# Step 4: Run the Ansible Playbook

At this point the playbook is largely complete and you can execute and
then test it.

    ---
    - name: parser example 
      hosts: ios
      gather_facts: no
      connection: network_cli
      roles:
        - parse_genie
     
      tasks:
      - name: show version
        ios_command:
          commands:
            - show version
        register: version
     
      - name: Set Fact Genie Filter
        set_fact:
          pyats_version: "{{ version['stdout'][0] | parse_genie(command='show version', os='ios') }}"

      - name: Debug Genie Filter
        debug:
          var: pyats_version

The parser takes the command output and creates a structured data in
JSON format. The facts that you want to use later in your playbook, are
now easily accessible.

# Step 5: Validate the Ansible Playbook run

After running the playbook (we did it via Ansible Tower), the following
is the debug Genie Filter Task from playbook
run:![image6-2](https://www.ansible.com/hs-fs/hubfs/image6-2.png?width=1930&name=image6-2.png){width="1930"
style="width: 1930px;"
srcset="https://www.ansible.com/hs-fs/hubfs/image6-2.png?width=965&name=image6-2.png 965w, https://www.ansible.com/hs-fs/hubfs/image6-2.png?width=1930&name=image6-2.png 1930w, https://www.ansible.com/hs-fs/hubfs/image6-2.png?width=2895&name=image6-2.png 2895w, https://www.ansible.com/hs-fs/hubfs/image6-2.png?width=3860&name=image6-2.png 3860w, https://www.ansible.com/hs-fs/hubfs/image6-2.png?width=4825&name=image6-2.png 4825w, https://www.ansible.com/hs-fs/hubfs/image6-2.png?width=5790&name=image6-2.png 5790w"
sizes="(max-width: 1930px) 100vw, 1930px"}

The full output:

    TASK [Debug Genie Filter] ******************************************************
     
    ok: [192.168.161.9] => {
        "msg": {
            "version": {
                "chassis": "WS-C3550-24",
                "chassis_sn": "CAT0651Z1E8",
                "curr_config_register": "0x10F",
                "hostname": "nco-rtr-9",
                "image_id": "C3550-IPSERVICESK9-M",
                "image_type": "developer image",
                "last_reload_reason": "warm-reset",
                "main_mem": "65526",
                "number_of_intfs": {
                    "FastEthernet": "24",
                    "Gigabit Ethernet": "2"
                },
                "os": "C3550 boot loader",
                "platform": "C3550",
                "processor_type": "PowerPC",
                "rom": "Bootstrap program is C3550 boot loader",
                "rtr_type": "WS-C3550-24",
                "system_image": "flash:c3550-ipservicesk9-mz.122-44.SE3/c3550-ipservicesk9-mz.122-44.SE3.bin",
                "uptime": "44 minutes",
                "version": "12.2(44)SE3",
                "version_short": "12.2"
            }
           }
    }

# Step 6: Integrate parsed content into ServiceNow tickets

What I would like to do now is add some new fields in the ServiceNow
incident layout. Let's add the version, uptime, hostname, platform,
device type, serial number, and last reload reason facts to every
incident ticket Ansible creates.

In the ServiceNow Web dashboard, add these new fields in Configure \>
Form
Layout.![image2-6](https://www.ansible.com/hs-fs/hubfs/image2-6.png?width=1590&name=image2-6.png){width="1590"
style="width: 1590px;"
srcset="https://www.ansible.com/hs-fs/hubfs/image2-6.png?width=795&name=image2-6.png 795w, https://www.ansible.com/hs-fs/hubfs/image2-6.png?width=1590&name=image2-6.png 1590w, https://www.ansible.com/hs-fs/hubfs/image2-6.png?width=2385&name=image2-6.png 2385w, https://www.ansible.com/hs-fs/hubfs/image2-6.png?width=3180&name=image2-6.png 3180w, https://www.ansible.com/hs-fs/hubfs/image2-6.png?width=3975&name=image2-6.png 3975w, https://www.ansible.com/hs-fs/hubfs/image2-6.png?width=4770&name=image2-6.png 4770w"
sizes="(max-width: 1590px) 100vw, 1590px"}

Now when you run your playbook from part one of this blog with the table
parameter set as incident. When you debug the incident.record dictionary
it should now have the new fields you just created, such as
u_device_up_time, u_ios_version, etc.

Snippet of the record dictionary the ServiceNow API sends
back![image4-3](https://www.ansible.com/hs-fs/hubfs/image4-3.png?width=956&name=image4-3.png){width="956"
style="width: 956px;"
srcset="https://www.ansible.com/hs-fs/hubfs/image4-3.png?width=478&name=image4-3.png 478w, https://www.ansible.com/hs-fs/hubfs/image4-3.png?width=956&name=image4-3.png 956w, https://www.ansible.com/hs-fs/hubfs/image4-3.png?width=1434&name=image4-3.png 1434w, https://www.ansible.com/hs-fs/hubfs/image4-3.png?width=1912&name=image4-3.png 1912w, https://www.ansible.com/hs-fs/hubfs/image4-3.png?width=2390&name=image4-3.png 2390w, https://www.ansible.com/hs-fs/hubfs/image4-3.png?width=2868&name=image4-3.png 2868w"
sizes="(max-width: 956px) 100vw, 956px"}

We can use these new fields in the data section of our Ansible Playbook
that uses the [snow_record
module](https://docs.ansible.com/ansible/latest/modules/snow_record_module.html){rel=" noopener"}.
The following is the complete playbook that runs the show version
command, parses the output and adds the parameters into the new fields:

    ---
    - name: create ticket with notes
      hosts: ios
      gather_facts: no
      connection: network_cli
      roles:
        - parse_genie


      tasks:

      - name: include vars
        include_vars: incident_vars.yml

      - name: show version
        ios_command:
          commands:
            - show version
        register: version

      - name: Set Fact Genie Filter
        set_fact:
          pyats_version: "{{ version['stdout'][0] | parse_genie(command='show version', os='ios') }}"

    # Example 1 showing version information
      - name: Debug Pyats facts
        debug:
          var: pyats_version.version.version

    # Example 2 showing uptime
      - name: Debug Pyats facts
        debug:
          var: pyats_version.version.uptime

      - name: Create an incident
        snow_record:
          state: present
          table: incident
          username: "{{ sn_username }}"
          password: "{{ sn_password }}"
          instance: "{{ sn_instance }}"
          data:
            priority: "{{ sn_priority}}"
            u_device_up_time: "{{ pyats_version.version.uptime }}"
            u_ios_version: "{{ pyats_version.version.version }}"
            u_hostname: "{{ pyats_version.version.hostname }}"
            u_platform: "{{ pyats_version.version.platform }}"
            u_device_type: "{{ pyats_version.version.rtr_type }}"
            u_serial_number: "{{ pyats_version.version.chassis_sn }}"
            u_last_reload_reason: "{{ pyats_version.version.last_reload_reason }}"
            short_description: "This ticket was created by Ansible"

      - debug: var=new_incident.record.number

Two additional debug examples are provided above to show how to work
with the pyATS dictionary that was returned. With structured output it
is much easier to grab the specific information you want using the key
(e.g. pyats_version.version.uptime is the key that returns the value for
the uptime of the system). The full dictionary is provided above in step
5.

The following screenshot is the output of the playbook shown from Red
Hat Ansible Tower:

![image3-3](https://www.ansible.com/hs-fs/hubfs/image3-3.png?width=1918&name=image3-3.png){width="1918"
style="width: 1918px;"
srcset="https://www.ansible.com/hs-fs/hubfs/image3-3.png?width=959&name=image3-3.png 959w, https://www.ansible.com/hs-fs/hubfs/image3-3.png?width=1918&name=image3-3.png 1918w, https://www.ansible.com/hs-fs/hubfs/image3-3.png?width=2877&name=image3-3.png 2877w, https://www.ansible.com/hs-fs/hubfs/image3-3.png?width=3836&name=image3-3.png 3836w, https://www.ansible.com/hs-fs/hubfs/image3-3.png?width=4795&name=image3-3.png 4795w, https://www.ansible.com/hs-fs/hubfs/image3-3.png?width=5754&name=image3-3.png 5754w"
sizes="(max-width: 1918px) 100vw, 1918px"}The new fields are now
populated in our ServiceNow incident ticket:

![image5
copy](https://www.ansible.com/hs-fs/hubfs/image5%20copy.png?width=900&name=image5%20copy.png){width="900"
style="width: 900px;"
srcset="https://www.ansible.com/hs-fs/hubfs/image5%20copy.png?width=450&name=image5%20copy.png 450w, https://www.ansible.com/hs-fs/hubfs/image5%20copy.png?width=900&name=image5%20copy.png 900w, https://www.ansible.com/hs-fs/hubfs/image5%20copy.png?width=1350&name=image5%20copy.png 1350w, https://www.ansible.com/hs-fs/hubfs/image5%20copy.png?width=1800&name=image5%20copy.png 1800w, https://www.ansible.com/hs-fs/hubfs/image5%20copy.png?width=2250&name=image5%20copy.png 2250w, https://www.ansible.com/hs-fs/hubfs/image5%20copy.png?width=2700&name=image5%20copy.png 2700w"
sizes="(max-width: 900px) 100vw, 900px"}

During an outage things can become chaotic. We have all seen how on
certain days in the network field, tickets can become a very low
priority. Automating the creation and dynamic facts solves this and
allows engineers to remain focused on the outage.

# Final thoughts

Something like this may help your organization adopt automation in
steps. These Ansible Playbooks are low risk because they do not modify
any configurations, they are read-only. This might be a great first step
for network engineers, without having to be doing holistic automation or
even config management. You may consider replacing the ios entry in the
filter plugin to use ansible_network_os variable that was introduced
with the network_cli connection plugin. That way you could run against
nxos, ios, junos, etc. all in the same inventory and playbook run. In
this blog we left it as ios so it could be easier to grasp if this is
your first time seeing it.

Stay tuned for part 3 of this series - we will cover integration from
ServiceNow to Ansible Tower's API. Where you can automatically have
ServiceNow execute Ansible Playbooks.
