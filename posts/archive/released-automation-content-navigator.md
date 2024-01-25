---
author: Colin McNaughton
date: 2022-06-01 00:00 UTC
description: Navigator 2.0 introduces improvements to existing
  functionality alongside additional features to aid in the development
  of automation content.
lang: en-us
slug: released-automation-content-navigator-2.0
title: Automation content navigator releases with Ansible Automation Platform 2.2
---

# Automation content navigator releases with Ansible Automation Platform 2.2

## What is it?

Automation content navigator was released alongside Red Hat Ansible
Automation Platform 2.0 and changed the way content creators build and
test Ansible automation. Navigator 1.0 drew together multiple Ansible
command line tools like ansible-playbook, ansible-doc, ansible-config,
etc. and continues to accrue seriously useful new features to help
deliver greater flexibility to automation creators.

Coinciding with the release of Ansible Automation Platform 2.2,
navigator 2.0 introduces improvements to existing functionality
alongside additional features to aid in the development of automation
content.

Within navigator 2.0, you will find:

-   Automation execution environment image build support 
-   Ability to interact in real-time with automation execution
    environments 
-   Settings subcommand to view active configuration of local
    environment 
-   Generate a sample configuration file that can be used for new
    projects
-   Automatic mode selection (stdout vs. interactive) 
-   Technology preview lint support, UI improvements, Collections view
    support for Ansible built-ins, time zone support, color
    enhancements, and more!

## Looking closer

### Image builder support

Before the release of navigator 2.0, a separate command line application
(ansible-builder)  was needed to build execution environment images from
human readable YAML files. With this release, ansible-navigator installs
ansible-builder and includes a new build command that is used to pass
through arguments to ansible-builder allowing content creators to create
images from a single familiar interface.

### Why should I care?

All enhancements to ansible-builder can be leveraged from
ansible-navigator. This functionality helps to cement navigator's role
within the content creators workflow to allow not only content creation
and environment introspection, but also execution environment build
support from within navigator.

### Things to try:

-   Add the arista.avd Collection to the supported execution
    environment:

*==> ./builder/execution-environment.yml*

``` yml
---
version: 1
build_arg_defaults:
  EE_BASE_IMAGE: "registry.redhat.io/ansible-automation-platform-21/ee-supported-rhel8:latest"
dependencies:
  galaxy: requirements.yml
  system: ""
  python: ""
```

*==> ./builder/requirements.yml*

``` yml
---
collections:
  - arista.avd
```

``` bash
$ ansible-navigator builder build --workdir builder
```

## Introducing the exec command

With a new subcommand, exec, automation creators now have the ability to
open a shell in the default execution environment. This allows creators
to further inspect the execution environment and leverage utilities
installed within the execution environment without installing them on a
local workstation.

For example, imagine you're creating some new workflows and you need to
leverage an additional Collection from Ansible automation hub. Instead
of installing the ansible-galaxy command-line tool on the local
workstation, you can run a command within navigator to install the
Collection in a directory alongside the new workflows. Because the
current working directory is bind mounted to the running container, the
installed Collection is placed on the local filesystem.

``` bash
ansible-navigator exec -- ansible-galaxy collection install servicenow.itsm -p ./collections
```

After running the above command, a new directory called "Collections"
should exist in your current working directory (CWD). This directory
will be made available to the execution environment at runtime because
the CWD is bind mounted at runtime. This allows you to always tell which
Collections are installed within the execution environment and which
have been bind mounted to the container.

### Why should I care?

Navigator lowers the barrier for creating new content! A creator now
only needs to install ansible-navigator to begin creating new
automation. Leveraging execution environments, the content creator
doesn't even need to install ansible-core! Navigator pulls in a default
execution environment that contains ansible-core and common Ansible
command line utilities such as ansible-galaxy. The exec command allows
these to be leveraged from within the default execution environment
instead of relying on workstation configuration.

### Things to try:

-   Encrypt a secret using a vault password file:

``` bash
$ echo secret_vault_password > password_file
$ ansible-navigator exec -- ansible-vault encrypt_string --vault-password-file password_file 'secret'
!vault |
          $ANSIBLE_VAULT;1.1;AES256
          64323039613737313538666239363032396361613464393033343165663631653835356232373139

Encryption successful
```

-   Scaffold a new Collection in the CWD, in the playbook adjacent
    Collection directory:

``` bash
$ ansible-navigator exec -- env
ANSIBLE_CACHE_PLUGIN=jsonfile
DESCRIPTION=Red Hat Ansible Automation Platform Minimal Execution Environment
SSH_AUTH_SOCK=/run/user/1000/keyring/ssh
```

## Navigator settings command

The settings command surfaces the configuration of the local environment
from within navigator. From the settings screen, creators are able to
view default values and values changed by local configuration
parameters. Leveraging this within an integrated development environment
(IDE) such as VS Code is especially helpful using features like
command+click to open a file path within the editor. For example, a
creator is able to see that a local ansible.cfg or ansible-navigator.yml
file is being sourced by navigator and can open that file within the
configured editor directly from the navigator settings screen.

### Why should I care?

Ansible is flexible! System-wide configuration files can be sourced for
multiple automation projects. It's very helpful to the content creator
to be able to view default configuration, which configuration parameters
have been defined in local configuration files and which files are being
sourced by the current project. All of this enhances a streamlined
creator workflow that becomes more predictable for content creators.

### Navigator sample settings

Imagine you are an automation content creator starting a new project.
You know that this new project will:

-    use a newly built execution environment
-    require navigator to have reasonable configuration defaults

In addition, you know you want to customize navigator to use your
preferred code editor.

Navigator sample settings allow creators to display a sample
ansible-navigator.yml configuration file with all parameters commented
out. This allows the creator to pick and choose which settings to adjust
for the new project. Things like default execution environment image
name, image pull policy, which code editor to use when opening files
from navigator, etc. are all configured from ansible-navigator.yml.
Additionally, this sample settings file can be written to the local
filesystem where, once edited for the new project, can be sourced by
navigator.

``` bash
$ ansible-navigator settings --sample > my.yaml
```

### Why should I care?

Multiple automation projects usually mean multiple execution
environments that need to be defined as the default execution
environment for the corresponding project. By allowing settings files to
be created from navigator, creators do not need to rely on memory to
define the parameters necessary to customize and deploy their projects.

### Things to try:

-   Use the TUI to review the current settings:

``` bash
$ ansible-navigator settings
```

-   Review the effective setting for ansible-navigator:

``` bash
$ ansible-navigator settings --effective
```

-   Show the source for each of the current settings:

``` bash
$ ansible-navigator settings --sources
```

## Automatic mode selection

Navigator consists of a textual user interface (TUI) that operates in
interactive mode by default. In interactive mode, creators run commands
and navigate the interface by using a series of keystrokes. Navigator
1.0 supported standard out mode for some commands. This means that
instead of opening up the full interactive user interface, creators
could run commands and query information about the local environment
without opening up the TUI. Standard out mode is helpful, for instance,
in CI/CD pipelines where there is no need to run commands interactively.

With navigator 2.0, more commands are supported in standard out mode.
For example, the collections subcommand can now run in standard out mode
and interactive mode. It's very useful to automation creators to see
which Collections are available in the environment to figure out which
modules can be leveraged in automated workflows.

Additionally, navigator now supports automatic mode selection for
commands that are only offered in a single mode. Previously the `--mode`
command line argument was necessary for commands that only supported
mode stdout.

### Why should I care?

Navigator is easily adapted to individual creators' workflows and
preferences. Even more, by adding standard out support for more
commands, navigator can now be utilized in automated build environments.

### Things to try:

-   Show the help for the ansible-playbook command without specifying
    `--mode stodut`

``` bash
$ ansible-navigator run --help-playbook
```

-   Show the help for the ansible-builder command:

``` bash
$ ansible-navigator builder --help-builder
```

## Lint functionality (technology preview)

One very nice use of interactive mode is in the newly added and
experimental feature for linting Ansible content. The lint subcommand,
when coupled with a path to an Ansible Playbook or directory of Ansible
content, opens a new screen in navigator where problems and suggestions
are displayed for the file(s) passed into the lint command. As the
problem files are corrected and saved, the list of problems and
suggestions shrinks. Coupled with a code editor's ability to
control+click to open a file path, editing files with potential issues
is quick and fits in well with the rest of the creator experience.

### Why should I care?

Consistent content produces reliable automation. Lint support allows
creators the ability to ensure that the content produced adheres to best
practices.

### Things to try:

-   Lint a playbook using the latest creator execution environment

``` bash
$ ansible-navigator lint site.yaml --eei quay.io/ansible/creator-ee:latest
```

## What now?

Automation content navigator 2.0 is available for use today! Navigator
offers improvements to the authoring and testing experience. As a
result, automation content creators have more tools on hand to assist in
the creation and maintenance of automated workflows. 
