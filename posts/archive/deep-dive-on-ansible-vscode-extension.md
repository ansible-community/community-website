---
author: Ganesh Nalawade
date: 2022-04-18 00:00 UTC
description: In this blog, we will do a deep dive into the Ansible
  VSCode extension, giving an overview of how it works and the initial
  setup required to get it working after installation.
lang: en-us
title: Deep dive on Ansible VScode extension
---


# Deep dive on Ansible VScode extension

Ansible as part of the Red Hat Ansible Automation Platform continues to
grow and mature. Recent enhancements include Ansible Content
C[ollections](https://www.ansible.com/blog/the-future-of-ansible-content-delivery),
automation [execution
environments](https://www.ansible.com/blog/whats-new-in-ansible-automation-platform-2-automation-execution-environments),
and an increasing list of integrations using plugins and modules. It is
more important than ever that both new and experienced content creators
have access to tools that help them write better content faster. The
newly created Ansible Devtools initiative focuses on developing and
enhancing tools like
[ansible-navigator](https://www.ansible.com/blog/whats-new-in-ansible-automation-platform-2-automation-content-navigator)[,
]{style="font-size: 11px;"}[Ansible VScode
extension](https://marketplace.visualstudio.com/items?itemName=redhat.ansible),
[ansible-lint](https://pypi.org/project/ansible-lint/) and so on to help
ease the Ansible automation content creator experience. In this blog, we
will do a deep dive into the Ansible VSCode extension, giving an
overview of how it works and the initial setup required to get it
working after installation.

## Evolution

The [Ansible VSCode
extension](https://marketplace.visualstudio.com/items?itemName=redhat.ansible)
was initially a fork of [Tomasz
Maciążek](https://github.com/tomaciazek)'s VSCode extension. After the
fork, the server and client-side code were decoupled into their own
separate repositories to allow independent releases for both server and
client.

1.  [Ansible language
    server](https://github.com/ansible/ansible-language-server)
2.  [Ansible VSCode
    extension](https://github.com/ansible/vscode-ansible) 

The Ansible Language Server is released as a node module on the [npm
repository](https://www.npmjs.com/package/@ansible/ansible-language-server),
allowing it to be reused by other editors supporting language server
protocol, while the VSCode extension client was released on the
[marketplace](https://marketplace.visualstudio.com/items?itemName=redhat.ansible)
with many additional features.

Tomasz continues to be a core contributor to the Ansible extension and
we would like to thank him and all the other community members for their
contributions to help make the extension better for Ansible content
creators with every new release.

## Introduction to the language server protocol (LSP)

The Ansible Language Server implements [language server
protocol](https://microsoft.github.io/language-server-protocol/) (LSP),
which is an open, [JSON-RPC](https://www.jsonrpc.org/specification)
based protocol that is used between source code editors, integrated
development environments (IDEs) and servers that provide programming
language-specific features. The goal of the protocol is to allow
programming language support to be implemented and distributed
independently of any given editor or IDE.

 

![](https://lh4.googleusercontent.com/lWCkrg0DKBsyQFukrQ5T-4S1PGGeyw8GOT41HpuwlC-2DVSDU7uf_mbChNgiixX8Hgl4JmNofKAPJcC3uqfx5YuPGuTHmrloTWlwCeJdlg7KUwlA-jRHGnme8eJsAhNueV-ZwbLC){width="602"
height="280" loading="lazy"}

[Source:
]{style="font-size: 8px;"}[https://code.visualstudio.com/api/language-extensions/language-server-extension-guide](https://code.visualstudio.com/api/language-extensions/language-server-extension-guide){style="font-size: 8px;"}

 

As seen from the above diagram, the language server protocol allows a
single language server implementation to be reused by multiple code
editors or IDEs, thus avoiding the need to duplicate language-related
support for each editor as in the case of no LSP. The language server
runs as a separate process and the development tools like VSCode
communicate with the server using the language protocol over JSON-RPC.
For more details refer to the language server specification
[here](https://microsoft.github.io/language-server-protocol/overviews/lsp/overview/).

## Ansible Language Server

![](https://lh5.googleusercontent.com/YUrkbA0DepDWGL7kQI2TYZCC1pHd_iJdAkBhIWoeLih09CPbMRzFmCmpb21R2nuHuzuDimWe0wRVw47T_z1Tr6d6PGsEl5e7QH_ulj-Hpb6Vq3iRf3lWqSJA4_mxCBZaBMSqTFnE){width="602"
height="319" loading="lazy"}

The Ansible Language Server provides features like:

-   Code completion
-   Hover (display keyword description on hover)
-   Goto definition (for modules)
-   Diagnostics and so on

It serves the JSON-RPC request sent by the development tool (client).
The language server runs Ansible commands like ansible-config,
ansible-playbook and so on to support these features and thus requires
an Ansible[ package](https://pypi.org/project/ansible/) or
[ansible-core](https://pypi.org/project/ansible-core/) installed locally
or within an automation execution environment. In addition, the language
server relies on [ansible-lint](https://pypi.org/project/ansible-lint/)
for providing diagnostic information if installed and enabled (default).
While running with an automation execution environment, ansible-core and
optionally ansible-lint should be included.

## Extension installation

In the VSCode Extensions tab, search and install the "Ansible VS Code
Extension" as shown in the snapshot

![](https://lh4.googleusercontent.com/jysdtN7z0-uhXwBLGo5H0jjZIVKYKhxRPxV_cMCfkma0kW24DDycvpsP2pUZDbLOoeFBxrWATHzuW3lqD7TZ-b6_mOpmz4ZSLZIizo12A8o9ttxORZsdvNFb7irqe6FsNfd0b3GK){width="602"
height="363" loading="lazy"}

 

Note: 

-   When the extension is installed for the first time, the "Runtime
    Status" is "Not yet activated" which indicates that the extension is
    not yet running. The status will be activated only after a file is
    opened in the editor and the language identified for the file is
    "**Ansible**".
-   For Windows users, the extension works with WSL2 and not on native
    Windows.

## Ansible extension settings

The Ansible extension supports multiple configuration options allowing,
for instance, to change the executable path for Ansible, ansible-lint,
python interpreter and so on. There is also an option to enable the
automation execution environment and users can choose the container
engine, image name, pull policy and more. To see and change the
configuration options in the VSCode window, go to
"Code-\>Preference-\>Settings" and in the Search settings box type
"**ansible**" as shown in the below snapshot.

![](https://lh6.googleusercontent.com/RF8l-qI0wM0k12ozA7zpmEJnZ7qvzi4dfGpTDtwviV3iPJKPJyoZexZLJqLZPzZo7uUQaeX1F1697ttrYIKbHHkxPZuhdHV_EyEfsV87BaCwSmKZfYPy49OWrQ4Gj9py65O9Us6d){width="602"
height="363" loading="lazy"}

The preferences can be set for a given user or workspace, and depending
on the environment, also for remote type and workspace folder. Settings
in the user scope will be applied globally for any instance of VSCode
that is opened. Workspace scoped settings will be stored inside your
workspace and only apply when the current workspace is opened. For more
information refer to the VSCode documentation
[here](https://code.visualstudio.com/docs/getstarted/settings).
Alternatively, for workspace settings, you can also provide the Ansible
settings by editing the **.vscode/settings.json** file within the
workspace root folder as shown below.

![](https://lh4.googleusercontent.com/Yq0LfHcG7o_TeJkeIBOjxHMiVfHjE4MxowDPw_UIVfWlRGFMQIQY00oCFYwtmRONwbxbH8viAOwy67hBBwpXNcs0g7R94soKIEH48ySST_AgxPxQrfw7QuupcFQl9mnnFN8WWRsp){width="602"
height="365" loading="lazy"}

## Activating and using Ansible extension

As stated above, the
[vscode-ansible](https://marketplace.visualstudio.com/items?itemName=redhat.ansible)
extension depends on the [ansible-language-server
](https://www.npmjs.com/package/@ansible/ansible-language-server)running
as a background process to provide features for Ansible Playbooks and
task files like auto-completion, hover, diagnostics, goto and more. The
extension also depends on the Red Hat
[vscode-yaml](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-yaml)
extension to provide auto-completion and diagnostics information of
other related files like Ansible vars file, ansible-navigator settings
file,  ansible-galaxy requirements and metafiles, ansible-lint
configuration file and other YAML files. The extension uses file pattern
match to associate the file with the YAML language. For details about
the file pattern and associated schema file used by the [vscode-yaml
](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-yaml)extension,
read more
[here](https://github.com/ansible/vscode-ansible/blob/v0.8.1/package.json#L54-L125).

With this context set, you can now go ahead and open the root of your
Ansible project in the VSCode window. That folder will be a root of your
workspace, also treated as the current working directory by the Ansible
Language Server while executing Ansible commands in the background. If
you try to open an Ansible file without first setting up a workspace,
the plugin might not be able to determine the context (such as CWD)
correctly.

After an Ansible file is opened in the VSCode window, it might not be
identified correctly as an **Ansible** language type as seen in the
below snapshot. Most likely, the file will be identified as "**YAML**"
language since Ansible files have either "**yaml**" or "**yml**"
extension and installing the
[vscode-ansible](http://ketplace.visualstudio.com/items?itemName=redhat.ansible)
extension, in turn, installs the [vscode-yaml
](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-yaml)extension.

![](https://lh4.googleusercontent.com/X26H_z5K-nrVrFI0zlRaxlVSSqRZCdCT4ssssbCKussty-rDvogYeRICO81RrGvUnnuhqzgeCf1zBMMWqse00yGRyxH_A9ixmPq6WCEXz-6r7gR5-v-DCW0R9ix6i-J731veo45Y){width="602"
height="365" loading="lazy"}

Hovering the cursor on the language identified (YAML in this case) in
the bottom right corner you will see "Select Language Mode". By clicking
on the identified language name (YAML) it will open a drop-down menu;
type "**Ansible**" in the tab and then select it. After doing this, you
will notice the identified language for the file is changed to
"**Ansible**" as shown in the below snapshot.

![](https://lh3.googleusercontent.com/ng6QgvzHpsdw2ygx_18202VC5LRpqS7mznpg_hr2IQuDATH2j8AC6mPQiMBAStTriGAkPZOq8hEyzvTrRs0by0PhtnaDrsILo1G5z9gOzdn_NmEGFKSBPokzUZi4nq26vRFQnrCd){width="602"
height="363" loading="lazy"}

When the file language is identified as Ansible for the first time, the
**vscode-ansible** extension will be activated and the extension will
run the **ansible-language-server** process in the background which
provides auto-completion, hover and diagnostics information as you type
and/or hover within the file. The diagnostics information will be
available in the **PROBLEMS** tab. If it's installed and enabled, the
language server will run **ansible-lint** by default to generate
diagnostics information on the open file. If **ansible-lint** is not
installed, the server will run **ansible-playbook --syntax-check** to
generate diagnostics information.

Instead of changing the language for each file, you can set the file
associations setting by clicking on "**Code -\> Preferences -\>
Settings**" and typing "**file associations**" in the search box. Add an
item to associate the extension with the language type as shown in the
below snapshot.

![](https://lh5.googleusercontent.com/tVaVotRSS7lcWWWDDQSqDCwMz6O9uAiy90o8B52GVow_iuAMRcoVWe9eeOPCyJNO19zzon-9o7m6ajzcsAE8S9dXYqvBekajULu0iLFjZV4_0hDuV89Wyl97HiiXZl9PKG5nMAo7){width="602"
height="363" loading="lazy"}

For more information on file associations, refer to the document
[here](https://code.visualstudio.com/docs/languages/identifiers).

## Using automation execution environments

To see the automation execution environments supported by extension, you
can go to settings (Code -\> Preferences -\> Settings) and type
"**ansible.execution environment**".

![](https://lh3.googleusercontent.com/g8GBE9PSktpwQfUHYtcLriY5xH33y5D0sBoYZVodZa_z6y97IFAbYxLwcOkdhWLQOQ__xb6omQCfI2f45FHHprtcp1-4WNXfVQq3opKDDtKPqk8DSXjJARisMx7X_1S14hUsZNYE){width="602"
height="432" loading="lazy"}

After enabling the execution environment (EE), the extension will pull
the "**quay.io/ansible/creator-ee:latest**" image by default, if it is
not present locally. The value of the image can be changed by providing
the intended value for "ansible.executionEnvironment.image" setting.
After the EE pull is successful, the Ansible extension will copy the
plugins docs from within EE to the local cache folder and it will be
used to provide auto-completion, hover and goto functionality. Since the
"creator-ee" image has "**ansible-lint**" bundled, the Ansible extension
and **ansible-language-server** will volume mount the entire workspace
within the EE and run "**ansible-lint**" or **"ansible-playbook
---syntax-check**" based on settings to provide diagnostics information
in editor.

![](https://lh6.googleusercontent.com/J6kYUbNCThka84g7Ed-7Z8HTlFALOQPjCFg7PiPZRIkG7h3d5S6scVMV74nAjzBepz66u_AKam65yxG5Va5Q71p_IriwRY_qbdp5NKXnXKtY2crvmsWTP1q4l5vBnZHRzGd2wf25){width="602"
height="325" loading="lazy"}

Note: 

-   If auto-completion and other features are not working after enabling
    the execution environment, you can reload VS Code by opening the
    command palette ("**view -\> Command Palette**") and executing the
    "**Developer: Reload Window**" command, which also restarts the
    "**ansible-language-server**" process running in the background.
-   If the extension is not working as expected, you can follow the
    debug steps shown
    [here](https://www.youtube.com/watch?v=vfIbIIbtQYI). If it is still
    not working, please do raise an issue
    [here](https://github.com/ansible/vscode-ansible/issues). 

The auto-completions will now provide suggestions for plugins that are
part of the given execution environment image name.

![](https://lh6.googleusercontent.com/qC73awYh0bk7L1eRRCLOkvbL5alfqTX8uqnZ0OL-MLvNvht8xYHGS9AYbMIPdBT2XrqQw1Y1UbrEFd-9U5mu1fFfeFG3-Q8YwzuG0Sb22p1iMD1O5OlDeuk2P2ae0dkehRjb7_fn){width="602"
height="347" loading="lazy"}

The "trigger suggest" key depends on the keyboard shortcut. To view the
associated keys, go to "Code -\> Preferences -\> Keyboard Shortcuts"

![](https://lh3.googleusercontent.com/SvlOi0AkZz9oxMx7J9n4tuvB_xpBE8hB_vq31dPPamBtKLA_l_E31V6X3yIH4x5TrwsVKHco1UK8CynE1QbG1MgMJRwggj3OGVbWqQlYG5aw7RvqGSpRqkdK5tDkFjojtoTXW6xp){width="602"
height="245" loading="lazy"}

## Ansible Playbook run entry point

The extension also provides an option to run an Ansible Playbook from
within the extension either using "**ansible-navigator run**" or
"**ansible-playbook**" command as shown in the below snapshot.

![](https://lh6.googleusercontent.com/bSBh17BHxqJobAwOWxx8thfEMDwbUvM6k_dDe-0JfmRmp7jrfARPlRO-vc1AjqSbJdlXyoPfoIV2VsEYrL7l6rkMRukcO-V2LiKsv70BdtDFpiRe6WkZS1N8BZAcv1jKm0NBodpU){width="602"
height="404" loading="lazy"}

Note: 

-   There is currently an
    [issue](https://github.com/ansible/vscode-ansible/issues/468) using
    this feature when the execution environment setting is enabled. 

**Credit:** Thank you [Brad
Thornton](https://www.ansible.com/blog/author/brad-thornton), [Colin
McNaughton](https://www.ansible.com/blog/author/colin-mcnaughton) and
[Tomasz Maciążek](https://github.com/tomaciazek) for your valuable edits
and for making this blog more readable.
