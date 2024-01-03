---
author: Ricardo Gerardi
date: 2020-09-17 00:00 UTC
description: Apply Molecule and Podman to quickly iterate through
  testing cases while developing an Ansible role, ensuring it works
  according to its specifications.
lang: en-us
title: Developing and Testing Ansible Roles with Molecule and Podman - Part 2
---

# Developing and Testing Ansible Roles with Molecule and Podman - Part 2

Molecule is a complete testing framework that helps you develop and test
Ansible roles, which allows you to focus on role content instead of
focusing on managing testing infrastructure. In the [first
part](https://www.ansible.com/blog/developing-and-testing-ansible-roles-with-molecule-and-podman-part-1)
of this series, we've successfully installed, configured and used
Molecule to set up new testing instances.

Now that the instances are running, let's start developing the new role
and apply Molecule to ensure it runs according to the specifications.

This basic role deploys a web application supported by the Apache web
server. It must support Red Hat Enterprise Linux (RHEL) 8 and Ubuntu
20.04.

# Developing the Ansible Role with Molecule

Molecule helps in the development stage by allowing you to "converge"
the instances with the role content. You can test each step without
worrying about managing the instances and test environment. It provides
quick feedback, allowing you to focus on the role content, ensuring it
works in all platforms.

In the [first
part](https://www.ansible.com/blog/developing-and-testing-ansible-roles-with-molecule-and-podman-part-1)
of this series, we initialized a new role "mywebapp". If you're not
there yet, switch to the role directory "mywebapp" and add the first
task, installing the Apache package "httpd" using the "package" Ansible
module. Edit the file "tasks/main.yaml" and include this task:

``` 
$ vi tasks/main.yml
---
# tasks file for mywebapp
- name: Ensure httpd installed
  package:
    name: "httpd"
    state: present
```

Save the file and "converge" the instances by running "molecule
converge". The "converge" command applies the current version of the
role to all the running container instances. Molecule "converge" does
not restart the instances if they are already running. It tries to
converge those instances by making their configuration match the desired
state described by the role currently testing.

``` 
$ molecule converge
... TRUNCATED OUTPUT ... 
   TASK [mywebapp : Ensure httpd installed] ***************************************
    Saturday 27 June 2020  08:45:01 -0400 (0:00:00.060)       0:00:04.277 *********
fatal: [ubuntu]: FAILED! => {"changed": false, "msg": "No package matching 'httpd' is available"}
    changed: [rhel8]
... TRUNCATED OUTPUT ... 
```

Notice that the current version worked well on the RHEL8 instance, but
failed for the Ubuntu instance. By using Molecule, you can quickly
evaluate the result of your tasks in all platforms and verify if the
role works according to the requirements! In this example however, the
tasks failed because Ubuntu does not have a package named "httpd". For
that platform, the package name is "apache2".

So let's modify the role to include variables with the correct package
name for each platform. Start with RHEL8 by adding a file "RedHat.yaml"
under the "vars" sub-directory with this content:

``` 
$ vi vars/RedHat.yaml
---
httpd_package: httpd
```

Save this file and add the corresponding file "vars/Debian.yaml" for
Ubuntu:

[]{style="background-color: transparent;"}

``` 
$ vi vars/Debian.yaml
---
httpd_package: apache2
```

Save this file and modify the "tasks/main.yaml" file to include these
variable files according to the OS family identified by Ansible via the
[system fact
variable](https://docs.ansible.com/ansible/devel/user_guide/playbooks_vars_facts.html)
"ansible_os_family". We also have to include a task to update the
package cache for systems in the "Debian" family since their package
manager caches results otherwise. Last, we update the install task to
use the variable "httpd_package" that you defined in the variables
files:

``` 
$ vi tasks/main.yml
- name: Include OS-specific variables.
  include_vars: "{{ ansible_os_family }}.yaml"
 
- name: Ensure package cache up-to-date
  apt:
    update_cache: yes
    cache_valid_time: 3600
  when: ansible_os_family == "Debian"
 
- name: Ensure httpd installed
  package:
    name: "{{ httpd_package }}"
    state: present
```

Save this file, and "converge" the instances again to ensure it works
this time:

``` 
$ molecule converge
... TRUNCATED OUTPUT ... 
   TASK [mywebapp : Ensure httpd installed] ***************************************
    Saturday 27 June 2020  08:59:13 -0400 (0:00:07.338)       0:00:12.925 *********
    ok: [rhel8]
    changed: [ubuntu]
... TRUNCATED OUTPUT ...
```

Because the package was already installed in the RHEL8 instance, Ansible
returned the status "OK" and it did not make any changes. It installed
the package correctly in the Ubuntu instance this time.

We have installed the package - but the naming problem also exists with
the service itself: they are named differently in RHEL and Ubuntu. So we
add service name variables to the playbooks and variable files. Start
with RHEL8:

``` 
$ vi vars/RedHat.yaml
---
httpd_package: httpd
httpd_service: httpd
```

Save this file and then edit the file "vars/Debian.yaml" for Ubuntu:

``` 
$ vi vars/Debian.yaml
---
httpd_package: apache2
httpd_service: apache2
```

Save the file and add the new task at the end of the "tasks/main.yml"
file:

``` 
$ vi tasks/main.yml
- name: Ensure httpd svc started
  service:
    name: "{{ httpd_service }}"
    state: started
    enabled: yes
```

Save the file and "converge" the instances again to start the Apache
httpd service:

``` 
$ molecule converge
... TRUNCATED OUTPUT ... 
   TASK [mywebapp : Ensure httpd svc started] *************************************
    Saturday 27 June 2020  09:34:38 -0400 (0:00:06.776)       0:00:17.233 *********
    changed: [ubuntu]
    changed: [rhel8]
... TRUNCATED OUTPUT ...
```

Let's add a final task to create some content for the web application.
Each platform requires the HTML files owned by different groups. Add new
variables to each variable file to define the group name:

``` 
$ vi vars/RedHat.yaml
---
httpd_package: httpd
httpd_service: httpd
httpd_group: apache
```

Save this file then edit the file "vars/Debian.yaml" for Ubuntu:

``` 
$ vi vars/Debian.yaml
---
httpd_package: apache2
httpd_service: apache2
httpd_group: www-data
```

Save the file and add the new task at the end of the "tasks/main.yml"
file:

``` 
$ vi tasks/main.yml
- name: Ensure HTML Index
  copy:
    dest: /var/www/html/index.html
    mode: 0644
    owner: root
    group: "{{ httpd_group }}"
    content: "{{ web_content }}"
```

This task allows the role user to specify the content by using the
variable "web_content" when calling the role. Add a default value to
this variable in case the user does not specify it:

``` 
$ vi defaults/main.yml
---
# defaults file for mywebapp
web_content: There's a web server here
```

Save this file and "converge" the instances one more time to add the
content:

``` 
$ molecule converge
... TRUNCATED OUTPUT ... 
   TASK [mywebapp : Ensure HTML Index] ********************************************
    Saturday 27 June 2020  09:50:11 -0400 (0:00:03.261)       0:00:17.753 *********
    changed: [rhel8]
    changed: [ubuntu]
... TRUNCATED OUTPUT ...
```

At this time, both instances are converged. Manually verify that the
role worked by using the molecule login command to log into one of the
instances and running the "curl" command to get the content:

``` 
$ molecule login -h rhel8
[root@2ce0a0ea8692 /]# curl http://localhost
There's a web server here 
[root@2ce0a0ea8692 /]# exit
```

You used Molecule to aid with the role development by ensuring that it
is working properly across multiple platforms for each step of the way.

Next, let's automate the verification process.

# Verifying the Role with Molecule

In addition to helping you converge the instance to aid with the role
development, Molecule can also automate the testing process by executing
a verification task. To verify the results of your playbook, Molecule
can use either the "testinfra" framework or it can use Ansible itself. 

Let's use an Ansible Playbook to verify the results of this new role. By
default, Molecule provides a basic verifier playbook
"molecule/default/verify.yml" as a starting point. This playbook
contains the basic required structure but does not do any useful
verification. Update this playbook to test this role result by using the
Ansible's "uri" module to obtain the content from the running web server
and the "assert" module to ensure it's the correct content:

``` 
$ vi molecule/default/verify.yml 
---
# This is an example playbook to execute Ansible tests.
 
- name: Verify
  hosts: all
  vars:
    expected_content: "There's a web server here"
  tasks:
  - name: Get index.html
    uri:
      url: http://localhost
      return_content: yes
    register: this
    failed_when: "expected_content not in this.content"
 
  - name: Ensure content type is text/html
    assert:
      that:
      - "'text/html' in this.content_type"
 
  - name: Debug results
    debug:
      var: this.content
```

Save and close this file. Verify the results by running "molecule
verify":

``` 
$ molecule verify
... TRUNCATED OUTPUT ... 
   TASK [Ensure content type is text/html] ****************************************
    Saturday 27 June 2020  10:03:18 -0400 (0:00:03.131)       0:00:07.255 *********
    ok: [rhel8] => {
        "changed": false,
        "msg": "All assertions passed"
    }
    ok: [ubuntu] => {
        "changed": false,
        "msg": "All assertions passed"
    }
... TRUNCATED OUTPUT ... 
Verifier completed successfully.
```

Molecule runs the verifier playbook against all instances ensuring the
results match the expected values.

You can change the default values for the test by editing the converge
playbook to update the "web_content" variable:

``` 
$ vi molecule/default/converge.yml
---
- name: Converge
  hosts: all
  tasks:
    - name: "Include mywebapp"
      include_role:
        name: "mywebapp"
      vars:
         web_content: "New content for testing only"
```

Then, update the "expected_content" variable in the verifier playbook:

``` 
$ vi molecule/default/verify.yml 
---
# This is an example playbook to execute Ansible tests.
 
- name: Verify
  hosts: all
  vars:
    expected_content: "New content for testing only"
  tasks:
```

Converge the instances one more time to update the web server content,
then verify the results:

``` 
$ molecule converge
... TRUNCATED OUTPUT ... 
   TASK [mywebapp : Ensure HTML Index] ********************************************
    Saturday 27 June 2020  10:09:34 -0400 (0:00:03.331)       0:00:19.607 *********
    changed: [rhel8]
    changed: [ubuntu]
... TRUNCATED OUTPUT ... 
$ molecule verify
... TRUNCATED OUTPUT ... 
   TASK [Debug results] ***********************************************************
    Saturday 27 June 2020  10:10:15 -0400 (0:00:00.299)       0:00:10.142 *********
    ok: [rhel8] => {
        "this.content": "New content for testing only"
    }
    ok: [ubuntu] => {
        "this.content": "New content for testing only"
    }
... TRUNCATED OUTPUT ... 
Verifier completed successfully.
```

Using the verifier, you can define a playbook to execute checks and
ensure the role produces the required results.

In the final step, let's put it all together with automated tests.

# Automating the Complete Test Workflow

Now that all of the pieces are together, automate the complete testing
process workflow using the command "molecule test".

Unlike the "molecule converge", which aided with role development, the
goal with "molecule test" is to provide an automated and repeatable
environment to ensure the role works according to its specifications.
Therefore, the test process destroys and re-creates the instances for
every test.

By default, "molecule test" executes these steps in order:

1.  Install required dependencies
2.  Lint the project
3.  Destroy existing instances
4.  Run a syntax check
5.  Create instances
6.  Prepare instances (if required)
7.  Converge instances by applying the role tasks
8.  Check the role for idempotence
9.  Verify the results using the defined verifier
10. Destroy the instances

You can change these steps by adding the "test_sequence" dictionary with
the required steps to the Molecule configuration file. For additional
information, consult the official
[documentation](https://molecule.readthedocs.io/en/latest/configuration.html#scenario).

Execute the test scenario:

``` 
$ molecule test
... TRUNCATED OUTPUT ... 
--> Test matrix
    
└── default
    ├── dependency
    ├── lint
    ├── cleanup
    ├── destroy
    ├── syntax
    ├── create
    ├── prepare
    ├── converge
    ├── idempotence
    ├── side_effect
    ├── verify
    ├── cleanup
    └── destroy
    
--> Scenario: 'default'
... TRUNCATED OUTPUT ... 
```

If the test workflow fails at any point, the command returns a status
code different than zero. You can use that return code to automate the
process or integrate Molecule with CI/CD workflows.

# Conclusion

Now that you've successfully applied Molecule to develop and test a role
that is well written and works reliably across different environments,
you can integrate it into your development cycle to produce high
standard roles consistently without worrying about the testing
infrastructure.

Molecule helps during the role development process by providing constant
feedback, which ensures your role works as designed each step of the
way.

For more advanced scenarios, Molecule supports additional drivers that
allow you to test roles with different platforms, virtualization and
cloud providers.

Finally, you can integrate Molecule with CI/CD workflows to automate the
complete testing process for your Ansible roles.
