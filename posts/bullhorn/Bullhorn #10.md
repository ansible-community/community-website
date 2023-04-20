---
title: "Bullhorn #10"
date: 2020-09-16 15:00 UTC
tags: news
category: bullhorn
type: text
---

![Ansible Bullhorn banner](/images/bullhorn-banner-mango.png)

<tr>
                        
                        <td class="mcnTextContent" style="padding: 0px 18px 9px;font-family: &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;word-break: break-word;color: #202020;font-size: 16px;line-height: 150%;text-align: left;" valign="top">
                        
                            <h1 class="null" dir="ltr" style="display: block;margin: 0;padding: 0;color: #202020;font-family: Helvetica;font-size: 26px;font-style: normal;font-weight: bold;line-height: 125%;letter-spacing: normal;text-align: left;">The Bullhorn</h1>

<p dir="ltr" style="font-family: &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif;margin: 10px 0;padding: 0;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #202020;font-size: 16px;line-height: 150%;text-align: left;"><em>A Newsletter for the Ansible Developer Community<br>
Issue #10, 2020-09-16</em><br>
<br>
Welcome to <em>The Bullhorn</em>, our newsletter for the Ansible developer community. If you have any questions or content you’d like to share, please reach out to us at the-bullhorn@redhat.com, or comment on this <a href="https://github.com/ansible/community/issues/546" target="_blank" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #007C89;font-weight: normal;text-decoration: underline;">GitHub issue</a>.<br>
&nbsp;</p>

<h2 class="null" dir="ltr" style="display: block;margin: 0;padding: 0;color: #202020;font-family: Helvetica;font-size: 22px;font-style: normal;font-weight: bold;line-height: 125%;letter-spacing: normal;text-align: left;">KEY DATES</h2>

<ul dir="ltr">
	<li style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;">2020-09-15: ansible-2.10.0 rc1 (moved from 10-Sep)</li>
	<li style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;">2020-09-17: <a href="https://github.com/ansible/community/issues/539" target="_blank" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #007C89;font-weight: normal;text-decoration: underline;">community IRC meeting</a> (any blockers for release should be proposed and discussed here)</li>
	<li style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;">2020-09-22: ansible-2.10 GA release date</li>
</ul>
&nbsp;

<h2 class="null" dir="ltr" style="display: block;margin: 0;padding: 0;color: #202020;font-family: Helvetica;font-size: 22px;font-style: normal;font-weight: bold;line-height: 125%;letter-spacing: normal;text-align: left;">ANSIBLE 2.10.0 RC1 NOW AVAILABLE</h2>
The Ansible Community team announced the availability of Ansible 2.10.0 release candidate 1 on September 15th. This new Ansible package should be a drop-in replacement for Ansible 2.9; the roles and playbooks that you currently use should work out of the box with ansible-2.10.0 rc1. For more information on how to download, test, and report issues, read <a href="https://groups.google.com/forum/#!topic/ansible-devel/hgXx7CEugt0" target="_blank" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #007C89;font-weight: normal;text-decoration: underline;">Toshio Kuratomi’s announcement to the ansible-devel mailing list</a>.<br>
<br>
The ansible-2.10.0 prereleases continue to be updated for testing purposes. <a href="https://groups.google.com/forum/#!topic/ansible-devel/93ymbTaUwl4" target="_blank" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #007C89;font-weight: normal;text-decoration: underline;">Ansible 2.10.0 beta 2</a> was uploaded to pypi last week, and Ansible 2.10.0 rc1 is now available on pypi as mentioned above.<br>
<br>
For more release details, please take a look at:
<ul>
	<li style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;"><a href="https://github.com/ansible/ansible/blob/devel/docs/docsite/rst/roadmap/COLLECTIONS_2_10.rst" target="_blank" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #007C89;font-weight: normal;text-decoration: underline;">Ansible 2.10 release schedule</a></li>
	<li style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;"><a href="https://groups.google.com/forum/#!topic/ansible-devel/618bSHJ7K64" target="_blank" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #007C89;font-weight: normal;text-decoration: underline;">Changes to the ansible-2.10.0 pre-release schedule</a></li>
</ul>
&nbsp;

<h2 class="null" style="display: block;margin: 0;padding: 0;color: #202020;font-family: Helvetica;font-size: 22px;font-style: normal;font-weight: bold;line-height: 125%;letter-spacing: normal;text-align: left;">ANSIBLE-BASE 2.10.1&nbsp;NOW GENERALLY AVAILABLE</h2>
The Ansible Base team announced the general release of Ansible 2.10.1 on September 14th. This ansible-base package consists of only the Ansible execution engine, related tools (e.g. ansible-galaxy, ansible-test), and a very small set of built-in plugins, and is also bundled with the larger Ansible distribution. For more information on how to download, test, and report issues, read <a href="https://groups.google.com/forum/#!topic/ansible-devel/rnkhV2gHZPo" target="_blank" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #007C89;font-weight: normal;text-decoration: underline;">Rick Elrod’s announcement to the ansible-devel mailing list</a>.<br>
&nbsp;
<h2 class="null" style="display: block;margin: 0;padding: 0;color: #202020;font-family: Helvetica;font-size: 22px;font-style: normal;font-weight: bold;line-height: 125%;letter-spacing: normal;text-align: left;">ROLE/COLLECTION PUBLISHERS: CHANGES TO ANSIBLE-GALAXY LOGIN</h2>
If you use the <span style="font-family:source sans pro,helvetica neue,helvetica,arial,sans-serif"><span style="background-color:#D3D3D3">ansible-galaxy</span></span> CLI to publish roles or collections to Galaxy, you may care about this. The GitHub API that underlies the <span style="font-family:source sans pro,helvetica neue,helvetica,arial,sans-serif"><span style="background-color:#D3D3D3">ansible-galaxy login</span></span> command is being removed in November. Without it, users doing role or collection publishing operations via the Galaxy CLI will need to find their Galaxy token interactively in a browser and pass it using a config file (as the ability to generate a token from the CLI will no longer function). We're not sure what people do today or how much this option is used out in the world, so please read and weigh in <a href="https://github.com/ansible/ansible/pull/71628" target="_blank" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #007C89;font-weight: normal;text-decoration: underline;">here</a> in the next few days if you have an opinion.<br>
&nbsp;
<h2 class="null" style="display: block;margin: 0;padding: 0;color: #202020;font-family: Helvetica;font-size: 22px;font-style: normal;font-weight: bold;line-height: 125%;letter-spacing: normal;text-align: left;">NEW/UPDATED COMMUNITY COLLECTIONS</h2>
The <a href="https://github.com/containers/ansible-podman-collections" target="_blank" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #007C89;font-weight: normal;text-decoration: underline;">Ansible Podman collection</a> has a new module <a href="https://github.com/containers/ansible-podman-collections/blob/master/plugins/modules/podman_network.py" target="_blank" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #007C89;font-weight: normal;text-decoration: underline;">podman_network</a> for the management of Podman networking.<br>
&nbsp;
<h2 class="null" style="display: block;margin: 0;padding: 0;color: #202020;font-family: Helvetica;font-size: 22px;font-style: normal;font-weight: bold;line-height: 125%;letter-spacing: normal;text-align: left;">THE ANSIBLE&nbsp;TEAM IS HIRING</h2>
The Ansible Community Team is hiring engineers to help with onboarding Ansible contributors. For more info, please see the following job descriptions:

<ul>
	<li style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;"><a href="https://global-redhat.icims.com/jobs/80815/senior-software-community-engineer---ansible-project/job?hub=7" target="_blank" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #007C89;font-weight: normal;text-decoration: underline;">Senior Software Community Engineer - Ansible Project - EU</a></li>
	<li style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;"><a href="https://us-redhat.icims.com/jobs/80814/senior-software-community-engineer---ansible-project/job?hub=7" target="_blank" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #007C89;font-weight: normal;text-decoration: underline;">Senior Software Community Engineer - Ansible Project - US</a></li>
</ul>
&nbsp;

<h2 class="null" style="display: block;margin: 0;padding: 0;color: #202020;font-family: Helvetica;font-size: 22px;font-style: normal;font-weight: bold;line-height: 125%;letter-spacing: normal;text-align: left;">CONTENT FROM THE ANSIBLE COMMUNITY</h2>

<ul>
	<li style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;"><a href="https://vincent.bernat.ch/en/blog/2020-custom-ansible-module" target="_blank" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #007C89;font-weight: normal;text-decoration: underline;">Writing a custom Ansible module</a> by <a href="https://twitter.com/vince2_" target="_blank" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #007C89;font-weight: normal;text-decoration: underline;">Vincent Bernat</a></li>
	<li style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;"><a href="https://willtham.es/2020/09/09/ansible-inventory-diff-github-action.html" target="_blank" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #007C89;font-weight: normal;text-decoration: underline;">Ansible Inventory Diff Github Action</a> by <a href="https://twitter.com/willthames" target="_blank" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #007C89;font-weight: normal;text-decoration: underline;">Will Thames</a></li>
</ul>
&nbsp;

<h2 class="mc-toc-title" style="display: block;margin: 0;padding: 0;color: #202020;font-family: Helvetica;font-size: 22px;font-style: normal;font-weight: bold;line-height: 125%;letter-spacing: normal;text-align: left;">ANSIBLE CONTRIBUTOR SUMMIT - PART OF ANSIBLEFEST&nbsp;2020</h2>
Due to overwhelming interest in the <a href="https://www.ansible.com/ansiblefest" target="_blank" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #007C89;font-weight: normal;text-decoration: underline;">AnsibleFest 2020</a> edition of the <strong>Ansible Contributor Summit</strong>, we are planning 2 days of program for you, depending on where you are in your contribution journey. These will be held on October 12 and 15, 2020.<br>
<br>
Take a look at the <a href="https://github.com/ansible/community/wiki/Contributor-Summit" target="_blank" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #007C89;font-weight: normal;text-decoration: underline;">wiki page</a> to find out how the two days will be structured, and register via the corresponding links. We look forward to your participation at the Contributor Summit!<br>
&nbsp;
<h2 class="null" style="display: block;margin: 0;padding: 0;color: #202020;font-family: Helvetica;font-size: 22px;font-style: normal;font-weight: bold;line-height: 125%;letter-spacing: normal;text-align: left;">OPEN SOURCE AUTOMATION DAYS</h2>
We will be a part of <a href="https://osad-munich.org/en/" target="_blank" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #007C89;font-weight: normal;text-decoration: underline;">Open Source Automation Days</a>, which will be an online event from October 19-21, 2020. Check out the <a href="https://osad-munich.org/en/featured-speakers-2020/" target="_blank" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #007C89;font-weight: normal;text-decoration: underline;">speakers and topics</a>, as well as <a href="https://osad-munich.org/en/workshops/" target="_blank" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #007C89;font-weight: normal;text-decoration: underline;">workshops</a>, and get tickets <a href="https://osad-munich.org/en/osad-2020-tickets/" target="_blank" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #007C89;font-weight: normal;text-decoration: underline;">here</a> if you’re interested.<br>
&nbsp;
<h2 class="null" style="display: block;margin: 0;padding: 0;color: #202020;font-family: Helvetica;font-size: 22px;font-style: normal;font-weight: bold;line-height: 125%;letter-spacing: normal;text-align: left;">ANSIBLE VIRTUAL MEETUPS</h2>
The following virtual meetups are being held in the Ansible community over the next month:

<ul>
	<li style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;"><a href="https://www.meetup.com/Ansible-Minneapolis/events/sbqkgrybcmbwb/" target="_blank" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #007C89;font-weight: normal;text-decoration: underline;">Ansible Minneapolis</a> - Multicloud Networking for DevOps

	<ul>
		<li style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;">Thu, Sep 17 · 6:30 PM CDT<br>
		&nbsp;</li>
	</ul>
	</li>
	<li style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;"><a href="https://www.meetup.com/Ansible-New-Zealand/events/273239620/" target="_blank" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #007C89;font-weight: normal;text-decoration: underline;">Ansible New Zealand</a> - Infrastructure Automation with Ansible + HPE
	<ul>
		<li style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;">Thu, Sep 24 · 12:00 PM GMT+12<br>
		&nbsp;</li>
	</ul>
	</li>
	<li style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;"><a href="https://www.meetup.com/Ansible-in-DevOps-Torun-Bydgoszcz/events/272980420/" target="_blank" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #007C89;font-weight: normal;text-decoration: underline;">Ansible in DevOps Torun-Bydgoszcz</a> - #8 Meeting AiDO GCP Anthos
	<ul>
		<li style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;">Wed, Sep 30 · 5:00 PM GMT+2<br>
		&nbsp;</li>
	</ul>
	</li>
	<li style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;"><a href="https://www.meetup.com/Ansible-Montreal/events/272979731/" target="_blank" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #007C89;font-weight: normal;text-decoration: underline;">Ansible Montréal</a> and <a href="https://www.meetup.com/Ansible-Quebec/events/272985049/" target="_blank" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #007C89;font-weight: normal;text-decoration: underline;">Québec</a> - Rencontre Septembre 2020
	<ul>
		<li style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;">Wed, Sep 30 · 6:00 PM EDT</li>
	</ul>
	</li>
</ul>
<em><strong>Note:</strong> For these virtual meetups, the links to participate will be visible once you RSVP to attend. If you’re interested in the topics presented, you can join from anywhere in the world as long as the time zone and language works for you!</em><br>
&nbsp;
<h2 class="null" dir="ltr" style="display: block;margin: 0;padding: 0;color: #202020;font-family: Helvetica;font-size: 22px;font-style: normal;font-weight: bold;line-height: 125%;letter-spacing: normal;text-align: left;">FEEDBACK</h2>

<p dir="ltr" style="font-family: &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif;margin: 10px 0;padding: 0;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #202020;font-size: 16px;line-height: 150%;text-align: left;">Have any questions you’d like to ask, or issues you’d like to see covered? Please send us an email at&nbsp;the-bullhorn@redhat.com.</p>
&nbsp;

<h1 class="null" dir="ltr" style="display: block;margin: 0;padding: 0;color: #202020;font-family: Helvetica;font-size: 26px;font-style: normal;font-weight: bold;line-height: 125%;letter-spacing: normal;text-align: left;">&nbsp;</h1>

                        </td>
                    </tr>
                
