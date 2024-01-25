---
author: John Westcott
date: 2020-07-23 00:00 UTC
description: As part of the Red Hat Ansible Automation Platform, Ansible
  Tower can be a cornerstone of an enterprise automation strategy. As
  part of that, many customers wish to secure the Ansible Tower
  installer passwords.
lang: en-us
title: Securing Tower Installer Passwords
---

# Securing Tower Installer Passwords

One of the crucial pieces of the Red Hat Ansible Automation Platform is
Ansible Tower. Ansible Tower helps scaling IT automation, managing
complex deployments and speeding up productivity. A strength of Ansible
Tower is its simplicity that also extends to the installation routine:
when installed as a non-container version, a simple script is used to
read in variables from an initial configuration to deploy Ansible Tower.
The same script and initial configuration can even be re-used to extend
the setup and add, for example, more cluster nodes.

However, part of this initial configuration are passwords for the
database, Ansible Tower itself and so on. In many online examples, these
passwords are often stored in plain text. One question I frequently get
as a Red Hat Consultant is how to protect this information. A common
solution is to simply remove the file after you complete the
installation of Ansible Tower. But, there are reasons you may want to
keep the file around. In this article, I will present another way to
protect the passwords in your installation files.

# Ansible Tower's setup.sh

For some quick background, `setup.sh` is the script used to install
Ansible Tower and is provided in both the regular and bundled installer.
The `setup.sh` script only performs a couple of tasks, such as validating
that Ansible is installed on the local system and setting up the
installer logs; but most importantly, it launches Ansible to handle the
installation of Ansible Tower. An inventory file can be specified to the
installer using the `-i` parameter or, if unspecified, the default
provided inventory file (which sits alongside `setup.sh`) is used. In the
first section of the inventory file, we have groups to specify the
servers that Ansible Tower and the database will be installed on:

```ini
[tower]
localhost ansible_connection=local

[database]
```

And, after those group specifications, there are variables that can be
used to set the connections and passwords, and is where you would
normally enter your plain text passwords, such as:

```ini
[all:vars]
admin_password='T0w3r123!'

pg_host=''
pg_port=''

pg_database='awx'
pg_username='awx'
pg_password='DB_Pa55w0rd!'
```

In the example above, these passwords are displayed as plain text. Many
clients I have worked with are not comfortable with leaving their
passwords in plain text within the inventory file for security reasons.
Once Ansible Tower is installed, this file can be safely removed, but if
you ever need to modify your installation to add a node to a cluster or
add/remove inventory groups, this file will need to be regenerated.
Likewise, if you want to use the backup and restore functions of
`setup.sh`, you will also need the inventory file with all of the
passwords as it was originally installed.

# Vault to the Rescue

Since the installer is using Ansible to install Ansible Tower, we can
leverage some Ansible concepts to secure our passwords. Specifically, we
will use [Ansible vault](https://docs.ansible.com/ansible/latest/user_guide/vault.html) to
have an encrypted password instead of a plain text password. If you are
not familiar with Ansible vault, it is a program shipped with Red Hat
Ansible Automation Platform itself and is a mechanism to encrypt and
decrypt data. It can be used against individual strings or it can
encrypt an entire file. In our example, we will encrypt individual
strings as passwords. This will be beneficial if you end up committing
your inventory file into a source control management tool. The SCM will
be able to show you individual passwords that were changed in a commit
versus just being able to say an encrypted file changed (but not being
able to show which password within the encrypted file changed).

To start, we are going to encrypt our admin password with the following
command (fields in `<>` indicate input to ansible-vault):

```bash
$ ansible-vault encrypt_string --stdin-name admin_password
New Vault password:
Confirm New Vault password:
Reading plaintext input from stdin. (ctrl-d to end input)
<t0w3r123!>admin_password: !vault |
          $ANSIBLE_VAULT;1.1;AES256
          66663534356430343166356461373464336332343439393731363365303063353032373564623537
          3466663861633936366463346135656130306538376637320a303738653264333737343463613366
          31396336633730323639303436653330386536363838646161653562373631323766346431663461
          6536646264633563660a343163303334336164376339363161373662613137633436393263376631
          3539
Encryption successful
</t0w3r123!>
```

In this example, we are running ansible-vault and asking it to encrypt a
string. We've told ansible-vault that this variable will be called
`admin_password` and it will have a value of **T0w3r123!** (what we would
have entered into our inventory file). In the example, we used a
password of '**password**' to encrypt these values. In a production
environment, a much stronger password should be used to perform your
vault encryption. In the output of the command, after the two ctrl-d
inputs, our encrypted variable is displayed on the screen. We will take
this output and put it into a file called `passwords.yml` next to our
inventory file. After encrypting the second `pg_password` our `password.yml`
file looks like this:

```bash
---
admin_password: !vault |
          $ANSIBLE_VAULT;1.1;AES256
          66663534356430343166356461373464336332343439393731363365303063353032373564623537
          3466663861633936366463346135656130306538376637320a303738653264333737343463613366
          31396336633730323639303436653330386536363838646161653562373631323766346431663461
          6536646264633563660a343163303334336164376339363161373662613137633436393263376631
          3539
pg_password: !vault |
          $ANSIBLE_VAULT;1.1;AES256
          65633239383761336539313437643733323235366337653164383934303563643464626562633865
          3130313231666531613131633736386134343664373039620a336237393631333532373066343135
          65316431626630633965623134623133353635376236306538653230363038333661623236376330
          3664346237396139610a376536373132313237653239353832623433663230393464343331356561
          3435
```

Now that we have our completed `passwords.yml` file, we have to tell the
installer to load the passwords from this file and also to prompt us for
the vault password to decrypt the value. To do this we will add three
parameters to our `setup.sh` command. The first option is
`-e@passwords.yml`, which is a
standard syntax to tell Ansible to load variables from a specified file
name (in this case `passwords.yml`). The second option will be `--`, which will tell the
`setup.sh` script that any following options should be passed on to
Ansible instead of being processed by `setup.sh`.
The final option will be `--ask-vault-pass`, which tells Ansible to prompt us for the
password to be able to decrypt the vault secrets.
All together our setup command will become:

```bash
$ ./setup.sh -e@passwords.yml -- --ask-vault-pass
```

If you normally add arguments to `setup.sh`, they will need to be merged
into this command structure. Arguments to `setup.sh` will need to go
before the `--` and any arguments you passed to Ansible would go after the `--`. 

When running `setup.sh` with these options you will now be prompted to
enter the vault password before the Ansible installer begins:

```bash
$ ./setup.sh -e@passwords.yml -- --ask-vault-pass
Using /etc/ansible/ansible.cfg as config file
Vault <password>:

PLAY [tower:database:instance_group_*:isolated_group_*] ******************************************************************************************
```

Here I have to enter my weak vault password of 'password' for the
decryption process to work. 

This technique will work even if you leave the blank password variables
in the inventory file because of the
[variable precedence from Ansible](https://docs.ansible.com/ansible/latest/user_guide/playbooks_variables.html#variable-precedence-where-should-i-put-a-variable).
The highest precedence any variable can take comes from extra_vars
(which is the `-e` option we added to the installer), so values in
our vault file will override any values specified in the inventory file.

Using this method allows you to keep the inventory file and password
files on disk or in an SCM and not have plain text passwords contained
within them.

# Another Solution

Another option you could take if you only wanted a single inventory file
would be to convert the existing ini inventory file into a yaml based
inventory. This would allow you to embed the variables as vault
encrypted values directly. While the scope of doing that is beyond this
article, an example `inventory.yml` file might look similar to this:

```yaml
all:
  children:
    database: {}
    tower:
      hosts:
        localhost:
  vars:
    admin_password: !vault |
        $ANSIBLE_VAULT;1.1;AES256
        66663534356430343166356461373464336332343439393731363365303063353032373564623537
        3466663861633936366463346135656130306538376637320a303738653264333737343463613366
        31396336633730323639303436653330386536363838646161653562373631323766346431663461
        6536646264633563660a343163303334336164376339363161373662613137633436393263376631
        3539
    ansible_connection: local
    pg_database: awx
    pg_host: ''
    pg_password: !vault |
        $ANSIBLE_VAULT;1.1;AES256
        65633239383761336539313437643733323235366337653164383934303563643464626562633865
        3130313231666531613131633736386134343664373039620a336237393631333532373066343135
        65316431626630633965623134623133353635376236306538653230363038333661623236376330
        3664346237396139610a376536373132313237653239353832623433663230393464343331356561
        3435
    pg_port: ''
    pg_sslmode: prefer
    pg_username: awx
    rabbitmq_cookie: cookiemonster
    rabbitmq_password: ''
    rabbitmq_username: tower
    tower_package_name: ansible-tower
    tower_package_release: '1'
    tower_package_version: 3.6.3
```

Using a file like this, `setup.sh` could then be called as:

```bash
$ ./setup.sh -i inventory.yml -- --ask-vault-pass
```

Using this method will require more work when upgrading Ansible Tower,
as any field changes in the provided inventory file will need to be
reflected in your yaml inventory, whereas the previous method only
requires new password fields added to the inventory file to be added
into the password.yml file.
