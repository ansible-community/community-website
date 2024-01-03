---
author: Ricardo Gerardi
date: 2020-08-25 00:00 UTC
description: Molecule is a complete testing framework that helps you
  develop and test Ansible roles, which allows you to focus on the
  content instead of focusing on managing testing infrastructure
lang: en-us
title: Developing and Testing Ansible Roles with Molecule and Podman - Part 1
---

# Developing and Testing Ansible Roles with Molecule and Podman - Part 1

One of the beauties of the Red Hat Ansible Automation Platform is that
the language to describe automation is readable not only by a few
dedicated experts, but by almost anyone across the IT ecosystem. That
means all IT professionals can take part in the automation, enabling
cross team collaboration and really drive automation as a culture inside
an organization. With so many people contributing to the automation, it
is crucial to test the automation content in-depth. So when you're
developing new Ansible Content like playbooks, roles and collections,
it's a good idea to test the content in a test environment before using
it to automate production infrastructure. Testing ensures the automation
works as designed and avoids unpleasant surprises down the road. 

Testing automation content is often a challenge, since it requires the
deployment of specific testing infrastructure as well as setting up the
testing conditions to ensure the tests are relevant. Molecule is a
complete testing framework that helps you develop and test Ansible
roles, which allows you to focus on the content instead of focusing on
managing testing infrastructure.

According to its official
[documentation](https://molecule.readthedocs.io/en/latest/index.html#),
Molecule is a project:

* "designed to aid in the development and testing of Ansible roles. It
encourages an approach that results in consistently developed roles that
are well-written, easily understood and maintained."*

Molecule allows you to test your role with many instances, ensuring it
works properly across different combinations of operating systems and
virtualization environments. Without it, you would have to provision and
maintain a testing environment separately. You would also have to
configure connectivity to those instances and ensure they are clean and
ready before every test. Molecule manages those aspects for you in an
automated and repeatable manner.

In this two part series, we will use Molecule to develop and test a new
Ansible role. The first article will guide you through installing and
configuring Molecule. In Part 2, we will use Molecule to aid with the
role development.

If this role is part of a Collection, use this approach to develop and
"unit" test the role. In a future article, we'll see how to use Molecule
to run integrated tests in a Collection.

Molecule uses drivers to provision testing instances using different
technologies, including Linux containers, virtual machines and cloud
providers. By default, it comes with three drivers pre-installed: Docker
and Podman drivers to manage containers, and Delegated that allows you
to customize your integration. Drivers for other providers are available
through the open source community.

In this article, we will use the [Podman](https://podman.io/) driver to
develop and test a new role using Linux containers. Podman is a
lightweight container engine for Linux that does not require a running
daemon, and allows execution of containers in "rootless" mode for
increased security. 

By using Molecule with the Podman driver, we will develop and test a new
Ansible role from scratch. This basic role deploys a web application
supported by the Apache web server. It must run on Red Hat Enterprise
Linux (RHEL) 8 or Ubuntu 20.04 operating systems.

This example shows a common scenario where a role is expected to work on
different versions of operating systems. Using Podman and Linux
containers allows us to create many instances to test the role with the
specific required versions. Since containers are lightweight, they also
allow us to quickly iterate over the role functionality while developing
it. Using containers for testing roles is applicable in this situation
because the role is configuring the running Linux instances only. To
test other provisioning scenarios or cloud infrastructure, we can use
the delegated driver or another appropriate driver provided by the
community.

## What do you need?

To follow this tutorial, use a physical or virtual machine running Linux
with Python 3 and Podman installed. For these examples, we're running
RHEL 8.2. You also need Podman configured to run rootless containers.
The installation of Podman is out of the scope of this blog, so please
refer to the official
[documentation](https://podman.io/getting-started/installation) for more
information. To install Podman on RHEL 8, you can also check the RHEL 8
[container
documentation](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html-single/building_running_and_managing_containers/index#getting-container-tools_building-running-and-managing-containers).


## Getting Started

Molecule is available as a Python package and thus can be installed via
pip. As a first step, we create a dedicated Python environment for our
Molecule installation, and install it there:

``` 
$ mkdir molecule-blog
$ cd molecule-blog
$ python3 -m venv molecule-venv
$ source molecule-venv/bin/activate
(molecule-venv) $ pip install "molecule[lint]"
```

Note that we installed Molecule with the "lint" option. By using this
option, pip also installed the "yamllint" and "ansible-lint" tools that
allow you to use Molecule to  perform static code analysis of your role,
ensuring it complies with Ansible coding standards.

The installation downloads all of the dependencies from the Internet,
including Ansible. Verify the installed version:

``` 
$ molecule --version
molecule 3.0.4
   ansible==2.9.10 python==3.6
```

Next, let's use the "molecule" command to initialize a new Ansible role.

## Initializing a New Ansible Role

Generally speaking, when developing a new Ansible role, you initialize
it by running the "ansible-galaxy role init" command. In this case,
instead use "molecule" to initialize the new role. By doing this, you'll
have the same role structure provided by the "ansible-galaxy" command
and the basic boilerplate code required to run Molecule tests.

By default, Molecule uses the Docker driver to execute tests. Since we
want to execute tests using "podman", we need to specify the driver name
using the option "\--driver-name=podman" when initializing the role with
"molecule". 

Switch back to the "molecule-blog" directory and initialize the new role
"mywebapp" with this command: 

``` 
$ molecule init role mywebapp --driver-name=podman
--> Initializing new role mywebapp...
Initialized role in /home/ricardo/molecule-blog/mywebapp successfully.
```

Molecule created the structure for your new role in a directory named
"mywebapp". Switch into this directory and check the content created by
Molecule:

``` 
$ cd mywebapp
$ tree
.
├── defaults
│   └── main.yml
├── files
├── handlers
│   └── main.yml
├── meta
│   └── main.yml
├── molecule
│   └── default
│       ├── converge.yml
│       ├── INSTALL.rst
│       ├── molecule.yml
│       └── verify.yml
├── README.md
├── tasks
│   └── main.yml
├── templates
├── tests
│   ├── inventory
│   └── test.yml
└── vars
    └── main.yml
 
10 directories, 12 files
```

Molecule includes its configuration files under the "molecule"
subdirectory. When initializing a new role, Molecule adds a single
scenario named "default". Later, you can add more scenarios to test
different conditions. For this tutorial, we'll use the "default"
scenario.

Verify the basic configuration in the file
"molecule/default/molecule.yml":

``` 
$ cat molecule/default/molecule.yml 
---
dependency:
  name: galaxy
driver:
  name: podman
platforms:
  - name: instance
    image: docker.io/pycontribs/centos:7
    pre_build_image: true
provisioner:
  name: ansible
verifier:
  name: ansible
```

As per our requirements, this file specifies the Podman driver for
tests. It also defines a default platform "instance" using the container
image "docker.io/pycontribs/centos:7" that you'll change later.

Unlike Molecule v2, Molecule v3 does not specify a linter by default.
Open the configuration file "molecule/default/molecule.yml" using your
favorite editor to include the lint configuration at the end:

``` 
$ vi molecule/default/molecule.yml
...
verifier:
  name: ansible
lint: |
  set -e
  yamllint .
  ansible-lint .
```

Save and close the configuration file. Run "molecule lint" from the
project root to lint the entire project:

``` 
$ molecule lint
```

This command returns a few errors because the file "meta/main.yml" is
missing some required values. Fix these issues by editing the file
"meta/main.yml" and adding "author", "company", "license", "platforms",
and removing the blank line at the end. Without comments - for brevity -
the "meta/main.yaml" looks like this:

``` 
$ vi meta/main.yml
galaxy_info:
  author: Ricardo Gerardi
  description: Mywebapp role deploys a sample web app 
  company: Red Hat 
 
  license: MIT 
 
  min_ansible_version: 2.9
 
  platforms:
  - name: rhel
    versions:
    - 8 
  - name: ubuntu
    versions:
    - 20.04
 
  galaxy_tags: []
 
dependencies: []
```

Now re-lint the project and verify that there are no errors this time.

``` 
$ molecule lint
--> Test matrix
    
└── default
    ├── dependency
    └── lint
    
--> Scenario: 'default'
--> Action: 'dependency'
Skipping, missing the requirements file.
Skipping, missing the requirements file.
--> Scenario: 'default'
--> Action: 'lint'
--> Executing: set -e
yamllint .
ansible-lint . 
```

The role is initialized and the basic molecule configuration is in
place. Let's set up the test instances next.

## Setting up Instances

By default, Molecule defines a single instance named "instance" using
the "Centos:7" image. According to our requirements, we want to ensure
our role works with RHEL 8 and Ubuntu 20.04. In addition, because this
role starts the Apache web server as a system service, we need to use
container images that enable "systemd".

Red Hat provides an official [Universal Base
Image](https://www.redhat.com/en/blog/introducing-red-hat-universal-base-image)
for RHEL 8, which enables "systemd": 

-   registry.access.redhat.com/ubi8/ubi-init

For Ubuntu, there's no official "systemd" enabled images so we'll use an
image maintained by Jeff Geerling from the Ansible open-source
community:

-   geerlingguy/docker-ubuntu2004-ansible

To enable the "systemd" instances, modify the
"molecule/default/molecule.yml" configuration file, remove the
"centos:7" instance and add the two new instances.

``` 
$ vi molecule/default/molecule.yml
---
dependency:
  name: galaxy
driver:
  name: podman
platforms:
  - name: rhel8
    image: registry.access.redhat.com/ubi8/ubi-init
    tmpfs:
      - /run
      - /tmp
    volumes:
      - /sys/fs/cgroup:/sys/fs/cgroup:ro
    capabilities:
      - SYS_ADMIN
    command: "/usr/sbin/init"
    pre_build_image: true
  - name: ubuntu
    image: geerlingguy/docker-ubuntu2004-ansible
    tmpfs:
      - /run
      - /tmp
    volumes:
      - /sys/fs/cgroup:/sys/fs/cgroup:ro
    capabilities:
      - SYS_ADMIN
    command: "/lib/systemd/systemd"
    pre_build_image: true
provisioner:
  name: ansible
verifier:
  name: ansible
lint: |
  set -e
  yamllint .
  ansible-lint .
```

With these parameters, we're mounting the temporary filesystem "/run"
and "/tmp", as well as the "cgroup" volume for each instance. We're also
enabling the "SYS_ADMIN" capability, as they are required to run a
container with Systemd.

Also, if you're following this tutorial on a RHEL 8 machine with SELinux
enabled - as it should - you need to set the "container_manage_cgroup"
boolean to true to allow containers to run Systemd. See the RHEL 8
[documentation](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html-single/building_running_and_managing_containers/index#starting_services_within_a_container_using_systemd)
for more details:

``` 
sudo setsebool -P container_manage_cgroup 1
```

Molecule uses an Ansible Playbook to provision these instances. Modify
and add parameters for provisioning by modifying the "provisioner"
dictionary in the "molecule/default/molecule.yml" configuration file. It
accepts the same configuration options provided in an Ansible
configuration file "ansible.cfg". For example, update the provisioner
configuration by adding a "defaults" section. Set the Python interpreter
to "auto_silent" to prevent warnings. Enable the "profile_tasks",
"timer", and "yaml" callback plugins to output profiling information
with the playbook output. Then, add the "ssh_connection" section and
disable SSH pipelining because it does not work with Podman:

``` 
provisioner:
  name: ansible
  config_options:
    defaults:
      interpreter_python: auto_silent
      callback_whitelist: profile_tasks, timer, yaml
    ssh_connection:
      pipelining: false
```

Save the configuration file and create the instances by running
"molecule create" from the role root directory:

``` 
$ molecule create
```

Molecule runs the provisioning playbook and creates both instances. You
can check the instances by running "molecule list":

``` 
$ molecule list
Instance Name    Driver Name    Provisioner Name    Scenario Name    Created    Converged
---------------  -------------  ------------------  ---------------  ---------  -----------
rhel8            podman         ansible             default          true       false
ubuntu           podman         ansible             default          true       false
```

You can also verify that both containers are running in Podman:

``` 
$ podman ps
CONTAINER ID  IMAGE                                                   COMMAND               CREATED             STATUS                 PORTS  NAMES
2e2f14eaa37b  docker.io/geerlingguy/docker-ubuntu2004-ansible:latest  /lib/systemd/syst...  About a minute ago  Up About a minute ago         ubuntu
2ce0a0ea8692  registry.access.redhat.com/ubi8/ubi-init:latest         /usr/sbin/init        About a minute ago  Up About a minute ago         rhel8
```

While developing the role, Molecule uses the running instances to test
it. In case a test fails, or an error causes an irreversible change that
requires you to start over, delete these instances by running "molecule
destroy" and recreate them with "molecule create" at any time.
