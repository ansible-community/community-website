---
title: "Bullhorn #1"
date: 2020-04-23 15:00 UTC
tags: news
category: bullhorn
type: text
---

![Ansible Bullhorn banner](/images/bullhorn-banner-mango.png)

<tr>
                        
                        <td class="mcnTextContent" style="padding: 0px 18px 9px;font-family: &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;word-break: break-word;color: #202020;font-size: 16px;line-height: 150%;text-align: left;" valign="top">
                        
                            <h1 class="null" dir="ltr" style="display: block;margin: 0;padding: 0;color: #202020;font-family: Helvetica;font-size: 26px;font-style: normal;font-weight: bold;line-height: 125%;letter-spacing: normal;text-align: left;">The Bullhorn</h1>

<p dir="ltr" style="font-family: &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif;margin: 10px 0;padding: 0;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #202020;font-size: 16px;line-height: 150%;text-align: left;"><em>A Newsletter for the Ansible Developer Community</em></p>

<p dir="ltr" style="font-family: &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif;margin: 10px 0;padding: 0;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #202020;font-size: 16px;line-height: 150%;text-align: left;">Welcome to <em>The Bullhorn</em>, our newsletter for the Ansible developer community. There are a lot of changes happening in Ansible right now, so we thought this would be a good time to start a newsletter to help everyone stay up-to-date.</p>
For now, we’ll probably release a new issue every couple of weeks or so. If you have any particular topics you’d like to see discussed in this newsletter, please reach out to us at gdk@redhat.com.

<h2 class="null" style="display: block;margin: 0;padding: 0;color: #202020;font-family: Helvetica;font-size: 22px;font-style: normal;font-weight: bold;line-height: 125%;letter-spacing: normal;text-align: left;"><br>
AN UPDATE ON ANSIBLE 2.10</h2>
If you’ve been following the development of Ansible 2.10, you know that we’re splitting out much of the code from the ansible/ansible repository on GitHub into new collections. We discussed the rationale for this change in a couple of blog posts in July of 2019 [<a href="https://www.ansible.com/blog/thoughts-on-restructuring-the-ansible-project" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #007C89;font-weight: normal;text-decoration: underline;">1</a>] [<a href="https://www.ansible.com/blog/the-future-of-ansible-content-delivery" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #007C89;font-weight: normal;text-decoration: underline;">2</a>].<br>
<br>
<strong>For end users, nothing much should change</strong>. Ansible 2.10 will contain all of the modules and plug-ins that were present in Ansible 2.9, and playbooks written for Ansible 2.9 should generally work in Ansible 2.10. Users who “pip install ansible” should get the same experience. We expect to have a long beta cycle to help ensure compatibility between 2.9 and 2.10.<br>
<br>
Under the hood, though, there’s quite a bit going on for developers to be aware of:&nbsp;
<ul>
	<li dir="ltr" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;">
	<p dir="ltr" role="presentation" style="font-family: &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif;margin: 10px 0;padding: 0;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #202020;font-size: 16px;line-height: 150%;text-align: left;"><em><strong>Content migration</strong></em>. In March, the Ansible Core development team froze the development tree for ansible/ansible and migrated most of the modules into one of the following repositories:</p>

	<ul>
		<li style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;">
		<p dir="ltr" role="presentation" style="font-family: &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif;margin: 10px 0;padding: 0;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #202020;font-size: 16px;line-height: 150%;text-align: left;">The community.general collection, which will be the new home for most community-written and community-supported content shipped in Ansible, built from a single community.general repository [<a href="https://github.com/ansible-collections/community.general" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #007C89;font-weight: normal;text-decoration: underline;">3</a>], and which will follow largely the same development process as Ansible has followed previously;</p>
		</li>
		<li style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;">
		<p dir="ltr" role="presentation" style="font-family: &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif;margin: 10px 0;padding: 0;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #202020;font-size: 16px;line-height: 150%;text-align: left;">A set of more specific community collections, including:&nbsp;</p>

		<ul>
			<li style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;">
			<p dir="ltr" role="presentation" style="font-family: &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif;margin: 10px 0;padding: 0;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #202020;font-size: 16px;line-height: 150%;text-align: left;">The community.networking collection [<a href="https://github.com/ansible-collections/community.network" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #007C89;font-weight: normal;text-decoration: underline;">4</a>], which provides a broad array of community-written and community-supported networking modules;</p>
			</li>
			<li style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;">
			<p dir="ltr" role="presentation" style="font-family: &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif;margin: 10px 0;padding: 0;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #202020;font-size: 16px;line-height: 150%;text-align: left;">The community.crypto collection [<a href="https://github.com/ansible-collections/community.crypto/" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #007C89;font-weight: normal;text-decoration: underline;">5</a>], a collection of related crypto modules with an active working group;</p>
			</li>
			<li style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;">
			<p dir="ltr" role="presentation" style="font-family: &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif;margin: 10px 0;padding: 0;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #202020;font-size: 16px;line-height: 150%;text-align: left;">The community.grafana collection [<a href="https://github.com/ansible-collections/community.grafana" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #007C89;font-weight: normal;text-decoration: underline;">6</a>], a collection of modules to manage Grafana;</p>
			</li>
			<li style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;">
			<p dir="ltr" role="presentation" style="font-family: &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif;margin: 10px 0;padding: 0;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #202020;font-size: 16px;line-height: 150%;text-align: left;">And various other collections that are managed by members of the Ansible community;</p>
			</li>
		</ul>
		</li>
		<li style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;">
		<p dir="ltr" role="presentation" style="font-family: &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif;margin: 10px 0;padding: 0;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #202020;font-size: 16px;line-height: 150%;text-align: left;">Partner collections, which are written, maintained, and supported by Ansible partners, a current list of which can be found here [<a href="https://access.redhat.com/articles/3642632" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #007C89;font-weight: normal;text-decoration: underline;">7</a>].</p>
		</li>
	</ul>
	</li>
	<li dir="ltr" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;">
	<p dir="ltr" role="presentation" style="font-family: &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif;margin: 10px 0;padding: 0;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #202020;font-size: 16px;line-height: 150%;text-align: left;"><em><strong>The new ansible-base project</strong></em>. Some modules remain in the ansible/ansible repository, which is now the home of the ansible-base project. Ansible-base is the core engine of Ansible itself, plus a small subset of key modules and libraries that are maintained by Red Hat. The ansible-base project is at the heart of everything Ansible does, and the Ansible team at Red Hat will keep a strong focus on maintaining it at a high level of quality and stability. As well as being packaged with Ansible, Ansible-base will now also release separately from Ansible, and will also ship with the Red Hat Ansible Automation Platform. Our current target date for release of ansible-base 2.10 is the end of July 2020. Follow our progress towards the release of ansible-base 2.10 here [<a href="https://github.com/ansible/ansible/blob/devel/docs/docsite/rst/roadmap/ROADMAP_2_10.rst" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #007C89;font-weight: normal;text-decoration: underline;">8</a>].</p>
	</li>
	<li dir="ltr" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;">
	<p dir="ltr" role="presentation" style="font-family: &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif;margin: 10px 0;padding: 0;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #202020;font-size: 16px;line-height: 150%;text-align: left;"><em><strong>Ansible 2.10 build tooling</strong></em>. Because Ansible 2.10 will be composed from separate collections, we are working on build tools that will assemble those collections into a single pip deliverable. Initial versions of that build code can be found here [<a href="https://github.com/ansible-community/ansible-infra/tree/master/build_acd" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #007C89;font-weight: normal;text-decoration: underline;">9</a>], and we expect to be putting together our first alpha builds of Ansible 2.10 in the coming days. Look for an announcement here on <em>The Bullhorn</em>, on the Ansible developer mailing list, and elsewhere.&nbsp;</p>
	</li>
	<li role="presentation" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;"><em><strong>GitHub redirection work</strong></em>. Now that much of the Ansible source code has moved, it might not always be clear to potential contributors where to submit issues or PRs. We will be working on workflow tools to direct contributors to the new content locations. We will also be working on tooling to make it easy for contributors to re-file existing PRs or issues in the new repositories. Follow the status of our GitHub redirection work here [<a href="https://github.com/ansible-collections/overview/blob/master/status.rst#moving-issues-and-prs-from-ansible-ansible" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #007C89;font-weight: normal;text-decoration: underline;">10</a>].</li>
</ul>

<p dir="ltr" role="presentation" style="font-family: &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif;margin: 10px 0;padding: 0;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #202020;font-size: 16px;line-height: 150%;text-align: left;">We’re still quite early in this process, but we’ve made a lot of progress. Assuming things continue to go well, we should be on track for a release of Ansible 2.10 by AnsibleFest in October 2020, or perhaps earlier.</p>
Follow our progress towards the release of Ansible 2.10 here [<a href="https://github.com/orgs/ansible-collections/projects/1" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #007C89;font-weight: normal;text-decoration: underline;">11</a>] and here [<a href="https://github.com/ansible-collections/overview/blob/master/status.rst" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #007C89;font-weight: normal;text-decoration: underline;">12</a>].<br>
&nbsp;
<h2 class="null" dir="ltr" style="display: block;margin: 0;padding: 0;color: #202020;font-family: Helvetica;font-size: 22px;font-style: normal;font-weight: bold;line-height: 125%;letter-spacing: normal;text-align: left;">ANSIBLE CONTRIBUTOR SUMMIT<span style="font-size:13px">&nbsp;</span></h2>

<p dir="ltr" style="font-family: &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif;margin: 10px 0;padding: 0;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #202020;font-size: 16px;line-height: 150%;text-align: left;">On March 29th, we held our first fully virtual Ansible Contributor Summit. The event was originally scheduled to be an in-person event co-located with FOSS North in Gothenburg, Sweden, but COVID-19 changed our plans. &nbsp;</p>

<p dir="ltr" style="font-family: &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif;margin: 10px 0;padding: 0;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #202020;font-size: 16px;line-height: 150%;text-align: left;">Despite our inability to meet in person, the Contributor Summit was a productive and successful event, with almost 50 contributors joining us over the course of the day. You can check out the videos [<a href="https://www.youtube.com/playlist?list=PL0FmYCf7ocraJzcnE3-VwVozQ0Zt7vm7z" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #007C89;font-weight: normal;text-decoration: underline;">13</a>] of the livestream event, along with a detailed summary [<a href="https://meetbot.fedoraproject.org/ansible-community/2020-03-29/ansible_contributor_summit_2020.2020-03-29-10.50.html" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #007C89;font-weight: normal;text-decoration: underline;">14</a>] and a full log [<a href="https://meetbot.fedoraproject.org/ansible-community/2020-03-29/ansible_contributor_summit_2020.2020-03-29-10.50.log.html" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #007C89;font-weight: normal;text-decoration: underline;">15</a>] of the accompanying IRC session.&nbsp;</p>

<p dir="ltr" style="font-family: &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif;margin: 10px 0;padding: 0;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #202020;font-size: 16px;line-height: 150%;text-align: left;">On March 30th, we followed the contributor summit with a virtual hackathon, in which we followed up on many of the issues that were discussed. Both a summary [<a href="https://meetbot.fedoraproject.org/ansible-community/2020-03-30/contributors_summit_hackathon.2020-03-30-09.02.html" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #007C89;font-weight: normal;text-decoration: underline;">16</a>] and a full log [<a href="https://meetbot.fedoraproject.org/ansible-community/2020-03-30/contributors_summit_hackathon.2020-03-30-09.02.log.html" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #007C89;font-weight: normal;text-decoration: underline;">17</a>] are available for the hackathon as well.&nbsp;</p>

<p dir="ltr" style="font-family: &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif;margin: 10px 0;padding: 0;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #202020;font-size: 16px;line-height: 150%;text-align: left;">In the future, we expect to have these virtual contributor summit&nbsp;events roughly once a quarter, which means the next event should happen near the end of June 2020. We will rotate the start times of these sessions to make them more accessible to people spread across the globe.&nbsp;<br>
&nbsp;</p>

<h2 class="null" dir="ltr" style="display: block;margin: 0;padding: 0;color: #202020;font-family: Helvetica;font-size: 22px;font-style: normal;font-weight: bold;line-height: 125%;letter-spacing: normal;text-align: left;">COMMUNITY METRIC HIGHLIGHT: COLLECTIONS GROWTH<span style="font-size:13px">&nbsp;</span></h2>

<p dir="ltr" style="font-family: &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif;margin: 10px 0;padding: 0;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #202020;font-size: 16px;line-height: 150%;text-align: left;">As the Ansible community continues to grow, we rely increasingly on metrics to keep track of our progress towards our goals. &nbsp;</p>

<p dir="ltr" style="font-family: &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif;margin: 10px 0;padding: 0;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #202020;font-size: 16px;line-height: 150%;text-align: left;">One of our key areas of focus is on contributors to collections. As we make the shift to collections, we want to ensure that our contributors are successful in making the switch. We’ve got a dashboard that shows us the progress of each collection in regaining its momentum from its original development in ansible/ansible. Here’s a small sample of that dashboard:&nbsp;</p>

<p dir="ltr" style="font-family: &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif;margin: 10px 0;padding: 0;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #202020;font-size: 16px;line-height: 150%;text-align: left;"><img src="https://lh3.googleusercontent.com/Izs8yviPW1ZLYYVlzbspiaKQrHGwhh4TKM61YowjSzNalFx2FI-b1cXEzCEyA67n_AiHFepD--RkSNuivfoLErHL_DTWvhX8v_oAkvr5d4lKOu7rPpw3UeP01-n7ykH9qJZUNQ58" style="border: 0;height: auto !important;outline: none;text-decoration: none;-ms-interpolation-mode: bicubic;" width="624" height="341"></p>
You can see the full dashboard here [<a href="https://stats.eng.ansible.com/apps/collections/contributors/" style="mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #007C89;font-weight: normal;text-decoration: underline;">18</a>].&nbsp;

<h2 class="null" dir="ltr" style="display: block;margin: 0;padding: 0;color: #202020;font-family: Helvetica;font-size: 22px;font-style: normal;font-weight: bold;line-height: 125%;letter-spacing: normal;text-align: left;"><br>
FEEDBACK<span style="font-size:13px">&nbsp;</span></h2>

<p dir="ltr" style="font-family: &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif;margin: 10px 0;padding: 0;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: #202020;font-size: 16px;line-height: 150%;text-align: left;">Have any questions you’d like to ask, or issues you’d like to see covered? Please send us an email to gdk@redhat.com.<br>
<br>
If you know somebody who could benefit from reading this newsletter, please feel free to&nbsp;forward it to them.</p>

                        </td>
                    </tr>
                