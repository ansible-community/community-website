---
title: "Bullhorn #8"
date: 2020-08-19 15:00 UTC
tags: news
category: bullhorn
type: text
---

![Ansible Bullhorn banner](/images/bullhorn-banner-mango.png)

<tr>
                        
                        <td class="mcnTextContent" style="padding: 0px 18px 9px;font-family: &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;word-break: break-word;color: #202020;font-size: 16px;line-height: 150%;text-align: left;" valign="top">
                        
                            <h1 class="null" dir="ltr" style="display: block;margin: 0;padding: 0;color: #202020;font-family: Helvetica;font-size: 26px;font-style: normal;font-weight: bold;line-height: 125%;letter-spacing: normal;text-align: left;">The Bullhorn</h1>

<p dir="ltr" style="font-family: &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif;margin: 10px 0;padding: 0;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #202020;font-size: 16px;line-height: 150%;text-align: left;"><em>A Newsletter for the Ansible Developer Community</em><br>
<br>
Welcome to <em>The Bullhorn</em>, our newsletter for the Ansible developer community. If you have any questions or content you’d like to share, please reach out to us at the-bullhorn@redhat.com, or comment on this <a href="https://github.com/ansible/community/issues/546" target="_blank" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #007C89;font-weight: normal;text-decoration: underline;">GitHub issue</a>.<br>
&nbsp;</p>

<h2 class="null" dir="ltr" style="display: block;margin: 0;padding: 0;color: #202020;font-family: Helvetica;font-size: 22px;font-style: normal;font-weight: bold;line-height: 125%;letter-spacing: normal;text-align: left;">ANSIBLE 2.10.0 ALPHA 9&nbsp;NOW AVAILABLE</h2>
The Ansible Community team announced the availability of Ansible 2.10.0 Alpha 9 on August 14th. This new Ansible package should be a drop-in replacement for Ansible 2.9; the roles and playbooks that you currently use should work out of the box with ansible-2.10.0 alpha9. For more information on how to download, test, and report issues, read <a href="https://groups.google.com/forum/#!topic/ansible-devel/iZRpeNl0JNQ" target="_blank" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #007C89;font-weight: normal;text-decoration: underline;">Toshio Kuratomi’s announcement to the ansible-devel mailing list</a>.<br>
&nbsp;
<h2 class="null" style="display: block;margin: 0;padding: 0;color: #202020;font-family: Helvetica;font-size: 22px;font-style: normal;font-weight: bold;line-height: 125%;letter-spacing: normal;text-align: left;">ANSIBLE-BASE 2.10.0 NOW GENERALLY AVAILABLE</h2>
The Ansible Base team announced the general availability of ansible-base 2.10.0 on August 13th. This ansible-base package consists of only the Ansible execution engine, related tools (e.g. ansible-galaxy, ansible-test), and a very small set of built-in plugins, and is also bundled with the larger Ansible distribution. For more information on how to download, test, and report issues, read <a href="https://groups.google.com/forum/#!topic/ansible-devel/T6sZnzAPDZA" target="_blank" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #007C89;font-weight: normal;text-decoration: underline;">Rick Elrod’s announcement to the ansible-devel mailing list</a>.<br>
&nbsp;
<h2 class="null" style="display: block;margin: 0;padding: 0;color: #202020;font-family: Helvetica;font-size: 22px;font-style: normal;font-weight: bold;line-height: 125%;letter-spacing: normal;text-align: left;">ANSIBLE 2.9.12 AND 2.8.14 RELEASED</h2>
The Ansible Core team announced the availability of Ansible 2.9.12 and Ansible 2.8.14 on August 10th, both of which are maintenance releases. Follow <a href="https://groups.google.com/forum/#!topic/ansible-devel/YWwDsuo1Vs4" target="_blank" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #007C89;font-weight: normal;text-decoration: underline;">this link</a> for Rick Elrod’s email to the ansible-devel mailing list, to obtain details on what’s new, installation instructions, and links to the full changelogs.<br>
&nbsp;
<h2 class="mc-toc-title" style="display: block;margin: 0;padding: 0;color: #202020;font-family: Helvetica;font-size: 22px;font-style: normal;font-weight: bold;line-height: 125%;letter-spacing: normal;text-align: left;">NEW/UPDATED COMMUNITY COLLECTIONS</h2>
<a href="https://github.com/containers/ansible-podman-collections" target="_blank" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #007C89;font-weight: normal;text-decoration: underline;">Ansible Podman collection</a> has been updated recently with new Podman modules: <a href="https://github.com/containers/ansible-podman-collections/blob/master/plugins/modules/podman_volume.py" target="_blank" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #007C89;font-weight: normal;text-decoration: underline;">podman_volume</a> to manage Podman container volumes on the host, <a href="https://github.com/containers/ansible-podman-collections/blob/master/plugins/modules/podman_pod.py" target="_blank" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #007C89;font-weight: normal;text-decoration: underline;">podman_pod</a> and <a href="https://github.com/containers/ansible-podman-collections/blob/master/plugins/modules/podman_pod_info.py" target="_blank" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #007C89;font-weight: normal;text-decoration: underline;">podman_pod_info</a> - for managing Podman pods. <a href="https://github.com/containers/ansible-podman-collections/blob/master/plugins/connection/podman.py" target="_blank" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #007C89;font-weight: normal;text-decoration: underline;">Podman</a> and <a href="https://github.com/containers/ansible-podman-collections/blob/master/plugins/connection/buildah.py" target="_blank" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #007C89;font-weight: normal;text-decoration: underline;">Buildah</a> connection plugins now support non-root users connections. All modules and plugins support Podman both versions v1 and v2. A few bugs of idempotency for <a href="https://github.com/containers/ansible-podman-collections/blob/master/plugins/modules/podman_container.py" target="_blank" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #007C89;font-weight: normal;text-decoration: underline;">podman_container</a> module have been fixed. You can find updated documentation <a href="https://docs.ansible.com/ansible/2.10/collections/containers/podman/index.html#plugins-in-containers-podman" target="_blank" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #007C89;font-weight: normal;text-decoration: underline;">here</a>.<br>
<br>
The Red Hat Automation Community of Practice has created a Galaxy Collection for <a href="https://galaxy.ansible.com/redhat_cop/tower_configuration" target="_blank" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #007C89;font-weight: normal;text-decoration: underline;">AWX and Tower Configuration</a>. The goal is to allow users to define all AWX/Tower Objects as Code. If you manage large scale, complex AWX or Tower instances it is worth checking out.<br>
<br>
<a href="https://community.ibm.com/community/user/ibmz-and-linuxone/blogs/eric-su1/2020/08/07/ibm-zos-core-collection-v1-2-0-beta1-release" target="_blank" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #007C89;font-weight: normal;text-decoration: underline;">Here's an update</a> on the latest beta release of the <a href="https://galaxy.ansible.com/ibm/ibm_zos_core" target="_blank" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #007C89;font-weight: normal;text-decoration: underline;">IBM z/OS core collection</a>, including three new z/OS core modules in Ansible Galaxy: <a href="https://ansible-collections.github.io/ibm_zos_core/modules/zos_mvs_raw.html" target="_blank" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #007C89;font-weight: normal;text-decoration: underline;">zos_mvs_raw</a>, <a href="https://ansible-collections.github.io/ibm_zos_core/modules/zos_lineinfile.html" target="_blank" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #007C89;font-weight: normal;text-decoration: underline;">zos_lineinfile</a>, and <a href="https://ansible-collections.github.io/ibm_zos_core/modules/zos_copy.html" target="_blank" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #007C89;font-weight: normal;text-decoration: underline;">zos_copy</a>.<br>
<br>
The collections for Zabbix and Grafana are now both&nbsp;at version 1.0.0, freshly released by the community over the weekend on August 16th! They are available on Ansible Galaxy: <a href="https://galaxy.ansible.com/community/grafana" target="_blank" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #007C89;font-weight: normal;text-decoration: underline;">Grafana collection</a> and <a href="https://galaxy.ansible.com/community/zabbix" target="_blank" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #007C89;font-weight: normal;text-decoration: underline;">Zabbix collection</a>.<br>
&nbsp;
<h2 class="null" style="display: block;margin: 0;padding: 0;color: #202020;font-family: Helvetica;font-size: 22px;font-style: normal;font-weight: bold;line-height: 125%;letter-spacing: normal;text-align: left;">COLLECTION PROPOSALS</h2>
YANG and NETCONF are vendor agnostic IETF standards that are used mainly for network device management. The proposal <a href="https://github.com/ansible-collections/community.yang/issues/3" target="_blank" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #007C89;font-weight: normal;text-decoration: underline;">linked here</a> outlines how Ansible plugins in <a href="https://github.com/ansible-collections/community.yang" target="_blank" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #007C89;font-weight: normal;text-decoration: underline;">community.yang</a>&nbsp;collection will ease managing YANG and NETCONF enabled devices using structured data. The plugins will provide maximum flexibility (YANG variant independent) and provide a simple-to-use approach. Review comments/suggestions/feedback are welcomed from the community.<br>
&nbsp;
<h2 class="mc-toc-title" style="display: block;margin: 0;padding: 0;color: #202020;font-family: Helvetica;font-size: 22px;font-style: normal;font-weight: bold;line-height: 125%;letter-spacing: normal;text-align: left;">ANSIBLE-LINT 4.3.0 RELEASED WITH ANSIBLE 2.10 SUPPORT</h2>
The ansible-lint community is happy to <a href="https://www.reddit.com/r/ansible/comments/ibzaw7/ansiblelint_430_was_released_with_ansible_210/" target="_blank" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #007C89;font-weight: normal;text-decoration: underline;">announce the release</a> of ansible-lint 4.3.0. This release includes more than 330 commits since v4.2.0.1, made over the past 6 months.<br>
&nbsp;
<h2 class="null" style="display: block;margin: 0;padding: 0;color: #202020;font-family: Helvetica;font-size: 22px;font-style: normal;font-weight: bold;line-height: 125%;letter-spacing: normal;text-align: left;">ANSIBLE COMMUNITY STATS UPDATE</h2>
With two Virtual Contributor Summits under our belt (and thus two surveys) we can start to look at the data they provide. <a href="https://twitter.com/Gwmngilfen" target="_blank" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #007C89;font-weight: normal;text-decoration: underline;">Greg</a> plans to do a longer post after the next Summit, looking at trends and so forth, but for now, here’s how people felt about the July Summit - pretty positive!<br>
<br>
<a href="https://mcusercontent.com/56d874e027110e35dea0e03c1/images/e5c10386-1f0d-4c4c-ba34-d651c4e42359.png" target="_blank" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #007C89;font-weight: normal;text-decoration: underline;"><img data-file-id="5382545" src="https://mcusercontent.com/56d874e027110e35dea0e03c1/images/e5c10386-1f0d-4c4c-ba34-d651c4e42359.png" style="border: 0px initial;width: 600px;height: 333px;margin: 0px;outline: none;text-decoration: none;-ms-interpolation-mode: bicubic;" width="600" height="333"></a><br>
&nbsp;
<h2 class="null" style="display: block;margin: 0;padding: 0;color: #202020;font-family: Helvetica;font-size: 22px;font-style: normal;font-weight: bold;line-height: 125%;letter-spacing: normal;text-align: left;">CONTENT FROM THE ANSIBLE COMMUNITY</h2>

<ul>
	<li style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;"><a href="https://dev.to/imjoseangel/release-and-deploy-ansible-collection-with-github-actions-4a62" target="_blank" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #007C89;font-weight: normal;text-decoration: underline;">Release and Deploy Ansible Collection with GitHub Actions</a> by <a href="https://dev.to/imjoseangel" target="_blank" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #007C89;font-weight: normal;text-decoration: underline;">Jose Angel Munoz</a></li>
	<li style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;"><a href="https://medium.com/@AbhijeetKasurde/ansible-generating-password-with-constraints-f475bb77d023" target="_blank" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #007C89;font-weight: normal;text-decoration: underline;">Ansible: Generating password with constraints</a> by <a href="https://akasurde.github.io/" target="_blank" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #007C89;font-weight: normal;text-decoration: underline;">Abhijeet Kasurde</a></li>
</ul>
&nbsp;

<h2 class="null" style="display: block;margin: 0;padding: 0;color: #202020;font-family: Helvetica;font-size: 22px;font-style: normal;font-weight: bold;line-height: 125%;letter-spacing: normal;text-align: left;">THE ANSIBLE COMMUNITY TEAM IS HIRING</h2>
The Ansible Community team is hiring engineers to help with onboarding Ansible contributors. For more info, please see the following job descriptions:

<ul>
	<li style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;"><a href="https://global-redhat.icims.com/jobs/80815/senior-software-community-engineer---ansible-project/job?hub=7" target="_blank" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #007C89;font-weight: normal;text-decoration: underline;">Senior Software Community Engineer - Ansible Project - EU</a></li>
	<li style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;"><a href="https://us-redhat.icims.com/jobs/80814/senior-software-community-engineer---ansible-project/job?hub=7" target="_blank" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #007C89;font-weight: normal;text-decoration: underline;">Senior Software Community Engineer - Ansible Project - US</a></li>
	<li style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;"><a href="https://us-redhat.icims.com/jobs/77049/technical-writer/job?hub=7" target="_blank" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #007C89;font-weight: normal;text-decoration: underline;">Technical Writer - Ansible Project - US</a></li>
</ul>
&nbsp;

<h2 class="mc-toc-title" style="display: block;margin: 0;padding: 0;color: #202020;font-family: Helvetica;font-size: 22px;font-style: normal;font-weight: bold;line-height: 125%;letter-spacing: normal;text-align: left;">ANSIBLEFEST VIRTUAL EXPERIENCE 2020</h2>
This year’s AnsibleFest will be a virtual experience! Find out the latest details about the event in <a href="https://www.ansible.com/blog/ansiblefest-2020-the-biggest-ansiblefest-ever" target="_blank" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #007C89;font-weight: normal;text-decoration: underline;">this blog post</a>, and register <a href="https://www.ansible.com/ansiblefest" target="_blank" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #007C89;font-weight: normal;text-decoration: underline;">here</a>. We are also having our <a href="https://github.com/ansible/community/wiki/Contributor-Summit" target="_blank" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #007C89;font-weight: normal;text-decoration: underline;">Ansible Contributor Summit</a> alongside AnsibleFest. More details will be shared soon!<br>
&nbsp;
<h2 class="null" style="display: block;margin: 0;padding: 0;color: #202020;font-family: Helvetica;font-size: 22px;font-style: normal;font-weight: bold;line-height: 125%;letter-spacing: normal;text-align: left;">ANSIBLE VIRTUAL MEETUPS</h2>
The following virtual meetups are being held in the Ansible community over the next month:

<ul>
	<li style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;"><a href="https://www.meetup.com/Ansible-Minneapolis/events/sbqkgrybclbbc/" target="_blank" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #007C89;font-weight: normal;text-decoration: underline;">Ansible Minneapolis</a>: Enhancing Cisco ACI Automation with Ansible Tower and Collections

	<ul>
		<li style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;">Thu, Aug 20 · 6:30 PM CDT<br>
		&nbsp;</li>
	</ul>
	</li>
	<li style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;"><a href="https://www.meetup.com/Ansible-Toronto/events/272634401/" target="_blank" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #007C89;font-weight: normal;text-decoration: underline;">Ansible Toronto</a> August 2020 (virtual)
	<ul>
		<li style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;">Tue, Aug 25 · 12:00 PM EDT<br>
		&nbsp;</li>
	</ul>
	</li>
	<li style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;"><a href="https://www.meetup.com/Ansible-NYC/events/272498156/" target="_blank" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #007C89;font-weight: normal;text-decoration: underline;">Ansible NYC</a>: Multicloud Networking Leveraging Ansible and Pureport
	<ul>
		<li style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;">Tue, Aug 25 · 6:00 PM EDT<br>
		&nbsp;</li>
	</ul>
	</li>
	<li style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;"><a href="https://www.meetup.com/Ansible-London/events/272502539/" target="_blank" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #007C89;font-weight: normal;text-decoration: underline;">Ansible London</a> [virtual] meetup – 10th Sept
	<ul>
		<li style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;">Thu, Sep 10 · 5:45 PM GMT+1</li>
	</ul>
	</li>
</ul>
&nbsp;<br>
<em><strong>Note:</strong> For these virtual meetups, the links to participate will be visible once you RSVP to attend. If you’re interested in the topics presented, you can join from anywhere in the world as long as the time zone and language works for you!</em><br>
&nbsp;
<h2 class="null" dir="ltr" style="display: block;margin: 0;padding: 0;color: #202020;font-family: Helvetica;font-size: 22px;font-style: normal;font-weight: bold;line-height: 125%;letter-spacing: normal;text-align: left;">FEEDBACK</h2>

<p dir="ltr" style="font-family: &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif;margin: 10px 0;padding: 0;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #202020;font-size: 16px;line-height: 150%;text-align: left;">Have any questions you’d like to ask, or issues you’d like to see covered? Please send us an email at&nbsp;the-bullhorn@redhat.com.</p>
&nbsp;

<h1 class="null" dir="ltr" style="display: block;margin: 0;padding: 0;color: #202020;font-family: Helvetica;font-size: 26px;font-style: normal;font-weight: bold;line-height: 125%;letter-spacing: normal;text-align: left;">&nbsp;</h1>

                        </td>
                    </tr>
                
