---
author: Jake Jackson
date: 2018-05-14 00:00 UTC
description: Ansible and Ansible Tower to help manage your Active
  Directory environment. We'll show you how you can configure some of
  those machines on your domain.
lang: en-us
title: Windows Package Management
---

# Windows Package Management

Welcome to the third installment of our Windows-centric Getting Started Series!

In the previous post we covered
how you can use Ansible and Ansible Tower to help manage your Active
Directory environment. This post will go into how you can configure some
of those machines on your domain. Most of this post is going to be
dominated by specific modules. Ansible has a plethora of Windows modules
that can be [found here](https://docs.ansible.com/ansible/latest/collections/index_module.html#ansible-windows).
As time is not a flat circle, I can't discuss all of them today but only
a few that are widely used.

## MSIs and the win_package Module

So you got your domain up, you have machines added to it, now let's
install some stuff on those machines. I do have a few notes before
moving forward in regards to the modules we'll be discussing. The module
win_msi is deprecated and will be removed in Ansible 2.8 (current
version as of this post is 2.5). In its place you can use
[win_package](http://docs.ansible.com/ansible/latest/modules/win_package_module.html#win-package-module)
which I will be using throughout this post.

Alright, back to installing stuff. The win_package module is the place
to be. It is used specifically for `.msi` and `.exe` files that need to
be installed or uninstalled. These files can also be sourced locally,
from a URL or from a network resource.

The parameters within the module add a lot of flexibility. As of Ansible
2.5, you can now list your arguments and the module will escape the
arguments as necessary. However, it is recommended to use a string when
dealing with MSI packages due to the unique escaping issues with
MsiExec.

Below are a few examples of how you can use the win_package module. The
first one shows how to install Visual C++ and list arguments:

```yml
- name: Install Visual C thingy with list of arguments instead of a string
  win_package:
    path:
http://download.microsoft.com/download/1/6/B/16B06F60-3B20-4FF2-B699-5E9B7962F9AE/VSU_4/vcredist_x64.exe
    product_id: '{CF2BEA3C-26EA-32F8-AA9B-331F7E34BA97}'
    arguments:
    - /install
    - /passive
    - /norestart
```

Above, we see that the product ID is listed. While Ansible can and does
extract the ID from the MSI when it's local, we don't want to force
the host to download the MSI if it's not necessary. When you supply the
product ID, Ansible can quickly check to see if the package is already
installed without downloading a potentially huge MSI from the internet
first. You can install without the product ID. An example of this can be
found below: 

```yml
- name: Install Remote Desktop Connection Manager locally omitting the product_id
  win_package:
    path: C:\temp\rdcman.msi
    state: present
```

As I stated earlier, you can also download from a network share and
specify the credentials needed to access that share. The example below
shows it in action, installing 7-zip from a network resource: 

```yml
- name: Install 7zip from a network share specifying the credentials
  win_package:
    path: \\domain\programs\7z.exe
    product_id: 7-Zip
    arguments: /S
    state: present
    user_name: DOMAIN\User
    user_password: Password
```

## Windows Package Management and Chocolatey

Unlike most Linux distros, Windows does not have a built-in package
manager. Windows does have the Windows App Store but I don't think that
a whole lot of those products are making their way into data centers.

There is, however, a community project called Chocolatey that provides a
full package management experience for Windows users. It helps take away
some of the pain that comes with managing raw `setup.exe` and `.msi`
files. And wouldn't you know, we have a module for it!

But before we get into talking about the module, let's talk a little bit
more about Chocolatey. A good comparison for people who might be Mac
users, Chocolatey is similar to that of Homebrew. Chocolatey is designed
to easily work with all aspects of managing Windows software
(installers, zip archives, runtime binaries, internal and 3rd party
software) using a packaging framework that understands both versioning
and dependency requirements.

The Chocolatey module is similar in use as its *nix counterparts,
simple and powerful. It does have a soft requirement in regards to the
version. And what I mean by soft requirement is that it needs v. 0.10.5
to run but if Chocolatey doesn't see that version, it will update it for
you. And to add some more sugar to that dessert, if Chocolatey is not
present on the machine, the module will install it for you as well
before going through with its assigned tasks.

To get started with the module, one of the easiest examples could be
installing a lightweight CLI tool. Let's use git because people's
workflows are all the same, right?

```yml
- name: Install git
  win_chocolatey:
    name: git
    state: present
```

All joking aside, it is that easy to install git. It is just as easy to
install a different version of something as well if you need to have a
specific version of something. Let's say you need Notepad++, version
6.6. It would look something like this: 

```yml
- name: Install notepadplusplus version 6.6
  win_chocolatey:
    name: notepadplusplus
    version: '6.6'
```

One key thing to note when you're stating a version: make sure to enter
it as a string (see the two tick marks around 6.6). Reason being is that
if it is not entered as a string, it's considered a YAML `float`. Many
valid version numbers don't translate properly into a `float` and
yield the same result (eg, '6.10' != '6.1' for most versioning
schemes, but 6.10 as a `float` will become 6.1), so it's a good habit
to always quote version numbers to ensure that they're not
re-formatted.

Some packages might require an interactive user logon to make an
installation. To pass the correct credentials, you can use `become` to
achieve this. The example below shows an installation of a package that
requires the use of `become`. Note that you can become: System and it
will not require you to supply a password.

```yml
- name: Install a package that requires 'become'
  win_chocolatey:
    name: officepro2013
  become: yes
  become_user: Administrator
  become_method: runas
```

The
[win_chocolatey](http://docs.ansible.com/ansible/latest/modules/win_chocolatey_module.html#win-chocolatey-module)
module is strong and powerful but in some scenarios will not work
without become. There is no easy way to find out if a package requires
become so the best course is to try it without and use `become` if that
fails. 

## Packages and Chocolate Bars in Windows Automation

To wrap up this blog post, we covered a couple of ways you can automate
the installation of packages for your Windows environment. Whether you
are all in on using Chocolatey or need to install some packages, Ansible
has the power to do all of that and more for you, in a simple and
easy-to-read format.

In our next and final post of the Getting Started with Windows
Automation series, we will talk about Security and Updates in Windows
using Ansible!
