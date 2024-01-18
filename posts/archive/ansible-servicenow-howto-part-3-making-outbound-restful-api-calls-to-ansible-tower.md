---
author: Michael Ford
date: 2019-10-09 00:00 UTC
description: Making outbound RESTful API calls to Red Hat Ansible Tower
lang: en-us
title: Ansible and ServiceNow Part 3, Making outbound RESTful API calls to Red Hat Ansible Tower
---

# Ansible and ServiceNow Part 3, Making outbound RESTful API calls to Red Hat Ansible Tower

Red Hat Ansible Tower offers value by allowing automation to scale in a
checked manner - users can run playbooks for only the processes and
targets they need access to, and no further. 

Not only does Ansible Tower provide automation at scale, but it also
integrates with several external platforms. In many cases, this means
that users can use the interface they are accustomed to while launching
Ansible Tower templates in the background. 

One of the most ubiquitous self service platforms in use today is
ServiceNow, and many of the enterprise conversations had with Ansible
Tower customers focus on ServiceNow integration. With this in mind, this
blog entry walks through the steps to set up your ServiceNow instance to
make outbound RESTful API calls into Ansible Tower, using OAuth2
authentication.

The following software versions are used:

-   Ansible Tower: 3.4, 3.5
-   ServiceNow: London, Madrid

If you sign up for a ServiceNow Developer account, ServiceNow offers a
free instance that can be used for replicating and testing this
functionality. Your ServiceNow instance needs to be able to reach your
Ansible Tower instance. Additionally, you can visit
<https://ansible.com/license> to obtain a trial license for Ansible
Tower. Instructions for installing Ansible Tower can be found
[here](https://docs.ansible.com/ansible-tower/latest/html/quickinstall/prepare.html). 

## Preparing Ansible Tower

1. In Ansible Tower, navigate to **Applications** on the left side of
the screen. Click the **green plus button** on the right, which will
present you with a Create Application dialog screen. Fill in the
following fields:

-   Name: Descriptive name of the application that will contact Ansible
    Tower
-   Organization: The organization you wish this application to be a
    part of
-   Authorization Grant Type: Authorization code
-   Redirect URIS:
    `https://\<snow_instance_id\>.service-now.com/oauth_redirect.do`
-   Client Type: Confidential

![image3-4](https://www.ansible.com/hs-fs/hubfs/image3-4.png?width=1913&name=image3-4.png){style="width: 1913px;"
width="1913"
srcset="https://www.ansible.com/hs-fs/hubfs/image3-4.png?width=957&name=image3-4.png 957w, https://www.ansible.com/hs-fs/hubfs/image3-4.png?width=1913&name=image3-4.png 1913w, https://www.ansible.com/hs-fs/hubfs/image3-4.png?width=2870&name=image3-4.png 2870w, https://www.ansible.com/hs-fs/hubfs/image3-4.png?width=3826&name=image3-4.png 3826w, https://www.ansible.com/hs-fs/hubfs/image3-4.png?width=4783&name=image3-4.png 4783w, https://www.ansible.com/hs-fs/hubfs/image3-4.png?width=5739&name=image3-4.png 5739w"
sizes="(max-width: 1913px) 100vw, 1913px"}

2. Click the green **Save** button on the right, at which point a
window will pop up, presenting you with the Client ID and Client Secret
needed for ServiceNow to make API calls into Ansible Tower. This will
only be presented **ONCE**, so capture these values for later use.

![image18](https://www.ansible.com/hs-fs/hubfs/image18.png?width=1714&name=image18.png){style="width: 1714px;"
width="1714"
srcset="https://www.ansible.com/hs-fs/hubfs/image18.png?width=857&name=image18.png 857w, https://www.ansible.com/hs-fs/hubfs/image18.png?width=1714&name=image18.png 1714w, https://www.ansible.com/hs-fs/hubfs/image18.png?width=2571&name=image18.png 2571w, https://www.ansible.com/hs-fs/hubfs/image18.png?width=3428&name=image18.png 3428w, https://www.ansible.com/hs-fs/hubfs/image18.png?width=4285&name=image18.png 4285w, https://www.ansible.com/hs-fs/hubfs/image18.png?width=5142&name=image18.png 5142w"
sizes="(max-width: 1714px) 100vw, 1714px"}

3. Next, navigate to **Settings->System** on the left side of the
screen. You'll want to toggle the **Allow External Users to Create
Oauth2 Tokens** option to **on**. Click the green **Save** button to
commit the change.

![image4-4](https://www.ansible.com/hs-fs/hubfs/image4-4.png?width=1914&name=image4-4.png){style="width: 1914px;"
width="1914"
srcset="https://www.ansible.com/hs-fs/hubfs/image4-4.png?width=957&name=image4-4.png 957w, https://www.ansible.com/hs-fs/hubfs/image4-4.png?width=1914&name=image4-4.png 1914w, https://www.ansible.com/hs-fs/hubfs/image4-4.png?width=2871&name=image4-4.png 2871w, https://www.ansible.com/hs-fs/hubfs/image4-4.png?width=3828&name=image4-4.png 3828w, https://www.ansible.com/hs-fs/hubfs/image4-4.png?width=4785&name=image4-4.png 4785w, https://www.ansible.com/hs-fs/hubfs/image4-4.png?width=5742&name=image4-4.png 5742w"
sizes="(max-width: 1914px) 100vw, 1914px"}

## Preparing ServiceNow

4. Moving over to ServiceNow, Navigate to **System Definition->Certificates**.
This will take you to a screen of all the
certificates Service Now uses. Click on the **blue New button**, and
fill in these details:

-   Name: Descriptive name of the certificate
-   Format: PEM
-   Type: Trust Store Cert
-   PEM Certificate: The certificate to authenticate against Ansible
    Tower with. You can use the built-in certificate on your Tower
    server, located at /etc/tower/tower.cert. Copy the contents of this
    file into the field in ServiceNow.

Click the **Submit** button at the bottom.

![image9-1](https://www.ansible.com/hs-fs/hubfs/image9-1.png?width=1914&name=image9-1.png){style="width: 1914px;"
width="1914"
srcset="https://www.ansible.com/hs-fs/hubfs/image9-1.png?width=957&name=image9-1.png 957w, https://www.ansible.com/hs-fs/hubfs/image9-1.png?width=1914&name=image9-1.png 1914w, https://www.ansible.com/hs-fs/hubfs/image9-1.png?width=2871&name=image9-1.png 2871w, https://www.ansible.com/hs-fs/hubfs/image9-1.png?width=3828&name=image9-1.png 3828w, https://www.ansible.com/hs-fs/hubfs/image9-1.png?width=4785&name=image9-1.png 4785w, https://www.ansible.com/hs-fs/hubfs/image9-1.png?width=5742&name=image9-1.png 5742w"
sizes="(max-width: 1914px) 100vw, 1914px"}

5. In ServiceNow, Navigate to **System OAuth->Application Registry**.
This will take you to a screen of all the Applications ServiceNow
communicates with. Click on the **blue New button**, and you will be
asked What kind of Oauth application you want to set up. Select
**Connect to a third party Oauth Provider**.

![image20](https://www.ansible.com/hs-fs/hubfs/image20.png?width=619&name=image20.png){style="width: 619px;"
width="619"
srcset="https://www.ansible.com/hs-fs/hubfs/image20.png?width=310&name=image20.png 310w, https://www.ansible.com/hs-fs/hubfs/image20.png?width=619&name=image20.png 619w, https://www.ansible.com/hs-fs/hubfs/image20.png?width=929&name=image20.png 929w, https://www.ansible.com/hs-fs/hubfs/image20.png?width=1238&name=image20.png 1238w, https://www.ansible.com/hs-fs/hubfs/image20.png?width=1548&name=image20.png 1548w, https://www.ansible.com/hs-fs/hubfs/image20.png?width=1857&name=image20.png 1857w"
sizes="(max-width: 619px) 100vw, 619px"}

6. On the new application screen, fill in these details:

-   Name: Descriptive Application Name
-   Client ID: The Client ID you got from Ansible Tower
-   Client Secret: The Client Secret you got from Ansible Tower
-   Default Grant Type: Authorization Code
-   Authorization URL: https://\<tower_url\>/api/o/authorize/
-   Token URL: https://\<tower_url\>/api/o/token/
-   Redirect URL:
    https://\<snow_instance_id\>.service-now.com/oauth_redirect.do

Click the **Submit** button at the bottom.

![image19](https://www.ansible.com/hs-fs/hubfs/image19.png?width=1916&name=image19.png){style="width: 1916px;"
width="1916"
srcset="https://www.ansible.com/hs-fs/hubfs/image19.png?width=958&name=image19.png 958w, https://www.ansible.com/hs-fs/hubfs/image19.png?width=1916&name=image19.png 1916w, https://www.ansible.com/hs-fs/hubfs/image19.png?width=2874&name=image19.png 2874w, https://www.ansible.com/hs-fs/hubfs/image19.png?width=3832&name=image19.png 3832w, https://www.ansible.com/hs-fs/hubfs/image19.png?width=4790&name=image19.png 4790w, https://www.ansible.com/hs-fs/hubfs/image19.png?width=5748&name=image19.png 5748w"
sizes="(max-width: 1916px) 100vw, 1916px"}

7. You should be taken out to the list of all Application Registries.
Click back into the Application you just created. At the bottom, there
should be two tabs: Click on the tab **Oauth Entity Scopes**. Under
here, there is a section called **Insert a new row...**. Double click
here, and fill in the field to say Writing Scope. Click on the **green
check mark** to confirm this change. Then, right-click inside the grey
area at the top where it says Application Registries and click Save in
the menu that pops up.

![image11-1](https://www.ansible.com/hs-fs/hubfs/image11-1.png?width=1033&name=image11-1.png){style="width: 1033px;"
width="1033"
srcset="https://www.ansible.com/hs-fs/hubfs/image11-1.png?width=517&name=image11-1.png 517w, https://www.ansible.com/hs-fs/hubfs/image11-1.png?width=1033&name=image11-1.png 1033w, https://www.ansible.com/hs-fs/hubfs/image11-1.png?width=1550&name=image11-1.png 1550w, https://www.ansible.com/hs-fs/hubfs/image11-1.png?width=2066&name=image11-1.png 2066w, https://www.ansible.com/hs-fs/hubfs/image11-1.png?width=2583&name=image11-1.png 2583w, https://www.ansible.com/hs-fs/hubfs/image11-1.png?width=3099&name=image11-1.png 3099w"
sizes="(max-width: 1033px) 100vw, 1033px"}

8. The writing scope should now be Clickable. Click on it, and in the
dialog window that you are taken to, type **write** in the Oauth scope
box. Click the Update button at the bottom.

![image7-1](https://www.ansible.com/hs-fs/hubfs/image7-1.png?width=1638&name=image7-1.png){style="width: 1638px;"
width="1638"
srcset="https://www.ansible.com/hs-fs/hubfs/image7-1.png?width=819&name=image7-1.png 819w, https://www.ansible.com/hs-fs/hubfs/image7-1.png?width=1638&name=image7-1.png 1638w, https://www.ansible.com/hs-fs/hubfs/image7-1.png?width=2457&name=image7-1.png 2457w, https://www.ansible.com/hs-fs/hubfs/image7-1.png?width=3276&name=image7-1.png 3276w, https://www.ansible.com/hs-fs/hubfs/image7-1.png?width=4095&name=image7-1.png 4095w, https://www.ansible.com/hs-fs/hubfs/image7-1.png?width=4914&name=image7-1.png 4914w"
sizes="(max-width: 1638px) 100vw, 1638px"}

9. Back in the Application Settings page, scroll back to the bottom and
click the **Oauth Entity Profiles** tab. There should be an entity
profile populated - click into it.

![image21](https://www.ansible.com/hs-fs/hubfs/image21.png?width=1626&name=image21.png){style="width: 1626px;"
width="1626"
srcset="https://www.ansible.com/hs-fs/hubfs/image21.png?width=813&name=image21.png 813w, https://www.ansible.com/hs-fs/hubfs/image21.png?width=1626&name=image21.png 1626w, https://www.ansible.com/hs-fs/hubfs/image21.png?width=2439&name=image21.png 2439w, https://www.ansible.com/hs-fs/hubfs/image21.png?width=3252&name=image21.png 3252w, https://www.ansible.com/hs-fs/hubfs/image21.png?width=4065&name=image21.png 4065w, https://www.ansible.com/hs-fs/hubfs/image21.png?width=4878&name=image21.png 4878w"
sizes="(max-width: 1626px) 100vw, 1626px"}

10. You will be taken to the Oauth Entity Profile Window. At the
bottom, Type **Writing Scope** into the Oauth Entity Scope field. Click
the green check mark and update.

![image23](https://www.ansible.com/hs-fs/hubfs/image23.png?width=1493&name=image23.png){style="width: 1493px;"
width="1493"
srcset="https://www.ansible.com/hs-fs/hubfs/image23.png?width=747&name=image23.png 747w, https://www.ansible.com/hs-fs/hubfs/image23.png?width=1493&name=image23.png 1493w, https://www.ansible.com/hs-fs/hubfs/image23.png?width=2240&name=image23.png 2240w, https://www.ansible.com/hs-fs/hubfs/image23.png?width=2986&name=image23.png 2986w, https://www.ansible.com/hs-fs/hubfs/image23.png?width=3733&name=image23.png 3733w, https://www.ansible.com/hs-fs/hubfs/image23.png?width=4479&name=image23.png 4479w"
sizes="(max-width: 1493px) 100vw, 1493px"}

11. Navigate to **System Web Services-\> REST Messages**. Click the
blue **New** button. In the resulting dialog window, fill in the
following fields:

-   Name: Descriptive REST Message Name
-   Endpoint: The url endpoint of the Ansible Tower action you wish to
    do. This can be taken from the browsable API at
    https://\<tower_url\>/api
-   Authentication Type: Oauth 2.0
-   Oauth Profile: Select the Oauth profile you created

Right-click inside the grey area at the top; click **Save**.

![image10-1](https://www.ansible.com/hs-fs/hubfs/image10-1.png?width=1632&name=image10-1.png){style="width: 1632px;"
width="1632"
srcset="https://www.ansible.com/hs-fs/hubfs/image10-1.png?width=816&name=image10-1.png 816w, https://www.ansible.com/hs-fs/hubfs/image10-1.png?width=1632&name=image10-1.png 1632w, https://www.ansible.com/hs-fs/hubfs/image10-1.png?width=2448&name=image10-1.png 2448w, https://www.ansible.com/hs-fs/hubfs/image10-1.png?width=3264&name=image10-1.png 3264w, https://www.ansible.com/hs-fs/hubfs/image10-1.png?width=4080&name=image10-1.png 4080w, https://www.ansible.com/hs-fs/hubfs/image10-1.png?width=4896&name=image10-1.png 4896w"
sizes="(max-width: 1632px) 100vw, 1632px"}

12. Click the **Get Oauth Token** button on the REST Message screen.
This will generate a pop-up window asking to authorize ServiceNow
against your Ansible Tower instance/cluster. Click Authorize. ServiceNow
will now have an OAuth2 token to authenticate against your Ansible Tower
server.

![image22](https://www.ansible.com/hs-fs/hubfs/image22.png?width=839&name=image22.png){style="width: 839px;"
width="839"
srcset="https://www.ansible.com/hs-fs/hubfs/image22.png?width=420&name=image22.png 420w, https://www.ansible.com/hs-fs/hubfs/image22.png?width=839&name=image22.png 839w, https://www.ansible.com/hs-fs/hubfs/image22.png?width=1259&name=image22.png 1259w, https://www.ansible.com/hs-fs/hubfs/image22.png?width=1678&name=image22.png 1678w, https://www.ansible.com/hs-fs/hubfs/image22.png?width=2098&name=image22.png 2098w, https://www.ansible.com/hs-fs/hubfs/image22.png?width=2517&name=image22.png 2517w"
sizes="(max-width: 839px) 100vw, 839px"}

13. Under the HTTP Methods section at the bottom, click the blue New
button. At the new dialog window that appears, fill in the following
fields:

-   HTTP Method: POST

-   Name: Descriptive HTTP Method Name

-   Endpoint: The url endpoint of the Ansible Tower action you wish to
    do. This can be taken from the browsable API at
    https://\<tower_url\>/api

-   HTTP Headers (under the HTTP Request tab)

-   -   The only HTTP Header that should be required is *Content-Type:
        application/json*

You can kick off a RESTful call to Ansible Tower using these parameters
with the **Test** link.

![image6-3](https://www.ansible.com/hs-fs/hubfs/image6-3.png?width=1633&name=image6-3.png){style="width: 1633px;"
width="1633"
srcset="https://www.ansible.com/hs-fs/hubfs/image6-3.png?width=817&name=image6-3.png 817w, https://www.ansible.com/hs-fs/hubfs/image6-3.png?width=1633&name=image6-3.png 1633w, https://www.ansible.com/hs-fs/hubfs/image6-3.png?width=2450&name=image6-3.png 2450w, https://www.ansible.com/hs-fs/hubfs/image6-3.png?width=3266&name=image6-3.png 3266w, https://www.ansible.com/hs-fs/hubfs/image6-3.png?width=4083&name=image6-3.png 4083w, https://www.ansible.com/hs-fs/hubfs/image6-3.png?width=4899&name=image6-3.png 4899w"
sizes="(max-width: 1633px) 100vw, 1633px"}

## Testing connectivity between ServiceNow and Ansible Tower

14. Clicking the **Test** link will take you to a results screen, which
should indicate that the Restful call was sent successfully to Ansible
Tower. In this example, ServiceNow kicks off an Ansible Tower job
Template, and the response includes the Job ID in Ansible Tower: 276.

![image
(8)](https://www.ansible.com/hs-fs/hubfs/image%20(8).png?width=1634&name=image%20(8).png){style="width: 1634px;"
width="1634"
srcset="https://www.ansible.com/hs-fs/hubfs/image%20(8).png?width=817&name=image%20(8).png 817w, https://www.ansible.com/hs-fs/hubfs/image%20(8).png?width=1634&name=image%20(8).png 1634w, https://www.ansible.com/hs-fs/hubfs/image%20(8).png?width=2451&name=image%20(8).png 2451w, https://www.ansible.com/hs-fs/hubfs/image%20(8).png?width=3268&name=image%20(8).png 3268w, https://www.ansible.com/hs-fs/hubfs/image%20(8).png?width=4085&name=image%20(8).png 4085w, https://www.ansible.com/hs-fs/hubfs/image%20(8).png?width=4902&name=image%20(8).png 4902w"
sizes="(max-width: 1634px) 100vw, 1634px"}

You can confirm that this Job Template was in fact started by going back
to Ansible Tower and clicking the **Jobs** section on the left side of
the screen; a Job with the same ID should be in the list (and, depending
on the playbook size, may still be in process):

![image15](https://www.ansible.com/hs-fs/hubfs/image15.png?width=1917&name=image15.png){style="width: 1917px;"
width="1917"
srcset="https://www.ansible.com/hs-fs/hubfs/image15.png?width=959&name=image15.png 959w, https://www.ansible.com/hs-fs/hubfs/image15.png?width=1917&name=image15.png 1917w, https://www.ansible.com/hs-fs/hubfs/image15.png?width=2876&name=image15.png 2876w, https://www.ansible.com/hs-fs/hubfs/image15.png?width=3834&name=image15.png 3834w, https://www.ansible.com/hs-fs/hubfs/image15.png?width=4793&name=image15.png 4793w, https://www.ansible.com/hs-fs/hubfs/image15.png?width=5751&name=image15.png 5751w"
sizes="(max-width: 1917px) 100vw, 1917px"}

## Creating a ServiceNow Catalog Item to Launch an Ansible Tower Job Template

15. Now that you are able to make outbound RESTful calls from
ServiceNow to Ansible Tower, it's time to create a catalog item for
users to select in ServiceNow in a production self-service fashion.
While in the HTTP Method options, click the **Preview Script Usage**
link:

![image
(9)](https://www.ansible.com/hs-fs/hubfs/image%20(9).png?width=1142&name=image%20(9).png){style="width: 1142px;"
width="1142"
srcset="https://www.ansible.com/hs-fs/hubfs/image%20(9).png?width=571&name=image%20(9).png 571w, https://www.ansible.com/hs-fs/hubfs/image%20(9).png?width=1142&name=image%20(9).png 1142w, https://www.ansible.com/hs-fs/hubfs/image%20(9).png?width=1713&name=image%20(9).png 1713w, https://www.ansible.com/hs-fs/hubfs/image%20(9).png?width=2284&name=image%20(9).png 2284w, https://www.ansible.com/hs-fs/hubfs/image%20(9).png?width=2855&name=image%20(9).png 2855w, https://www.ansible.com/hs-fs/hubfs/image%20(9).png?width=3426&name=image%20(9).png 3426w"
sizes="(max-width: 1142px) 100vw, 1142px"}

Copy the resulting script the appears, and paste it into a text editor
to reference later.

16. In ServiceNow, navigate to **Workflow-\>Workflow Editor.** This
will open a new tab with a list of all existing ServiceNow workflows.
Click on the blue **New Workflow** button:

![image16](https://www.ansible.com/hs-fs/hubfs/image16.png?width=1583&name=image16.png){style="width: 1583px;"
width="1583"
srcset="https://www.ansible.com/hs-fs/hubfs/image16.png?width=792&name=image16.png 792w, https://www.ansible.com/hs-fs/hubfs/image16.png?width=1583&name=image16.png 1583w, https://www.ansible.com/hs-fs/hubfs/image16.png?width=2375&name=image16.png 2375w, https://www.ansible.com/hs-fs/hubfs/image16.png?width=3166&name=image16.png 3166w, https://www.ansible.com/hs-fs/hubfs/image16.png?width=3958&name=image16.png 3958w, https://www.ansible.com/hs-fs/hubfs/image16.png?width=4749&name=image16.png 4749w"
sizes="(max-width: 1583px) 100vw, 1583px"}

17. In the **New Workflow** dialog box that appears, fill in the
following options:

-   Name: A descriptive name of the workflow
-   Table: Requested Item \[sc_req_item\]

Everything else can be left alone. Click the **Submit** button.

![image1-10](https://www.ansible.com/hs-fs/hubfs/image1-10.png?width=1506&name=image1-10.png){style="width: 1506px;"
width="1506"
srcset="https://www.ansible.com/hs-fs/hubfs/image1-10.png?width=753&name=image1-10.png 753w, https://www.ansible.com/hs-fs/hubfs/image1-10.png?width=1506&name=image1-10.png 1506w, https://www.ansible.com/hs-fs/hubfs/image1-10.png?width=2259&name=image1-10.png 2259w, https://www.ansible.com/hs-fs/hubfs/image1-10.png?width=3012&name=image1-10.png 3012w, https://www.ansible.com/hs-fs/hubfs/image1-10.png?width=3765&name=image1-10.png 3765w, https://www.ansible.com/hs-fs/hubfs/image1-10.png?width=4518&name=image1-10.png 4518w"
sizes="(max-width: 1506px) 100vw, 1506px"}

18. The resulting Workflow Editor will have only a Begin and End box.
Click on the line (it will turn blue to indicate it has been selected),
then press delete to get rid of it.

![image14-1](https://www.ansible.com/hs-fs/hubfs/image14-1.png?width=614&name=image14-1.png){style="width: 614px;"
width="614"
srcset="https://www.ansible.com/hs-fs/hubfs/image14-1.png?width=307&name=image14-1.png 307w, https://www.ansible.com/hs-fs/hubfs/image14-1.png?width=614&name=image14-1.png 614w, https://www.ansible.com/hs-fs/hubfs/image14-1.png?width=921&name=image14-1.png 921w, https://www.ansible.com/hs-fs/hubfs/image14-1.png?width=1228&name=image14-1.png 1228w, https://www.ansible.com/hs-fs/hubfs/image14-1.png?width=1535&name=image14-1.png 1535w, https://www.ansible.com/hs-fs/hubfs/image14-1.png?width=1842&name=image14-1.png 1842w"
sizes="(max-width: 614px) 100vw, 614px"}

19. On the right side of the Workflow Editor Screen, select the Core
tab and, under Core Activities-\>Utilities, drag the Run Script option
into the Workflow Editor. In the new dialog box that appears, type in a
descriptive name, and paste in the script you captured from before.
Click Submit to save the Script.

![image12-1](https://www.ansible.com/hs-fs/hubfs/image12-1.png?width=1912&name=image12-1.png){style="width: 1912px;"
width="1912"
srcset="https://www.ansible.com/hs-fs/hubfs/image12-1.png?width=956&name=image12-1.png 956w, https://www.ansible.com/hs-fs/hubfs/image12-1.png?width=1912&name=image12-1.png 1912w, https://www.ansible.com/hs-fs/hubfs/image12-1.png?width=2868&name=image12-1.png 2868w, https://www.ansible.com/hs-fs/hubfs/image12-1.png?width=3824&name=image12-1.png 3824w, https://www.ansible.com/hs-fs/hubfs/image12-1.png?width=4780&name=image12-1.png 4780w, https://www.ansible.com/hs-fs/hubfs/image12-1.png?width=5736&name=image12-1.png 5736w"
sizes="(max-width: 1912px) 100vw, 1912px"}

20. Draw a connection from **Begin**, to the newly created Run Script
Box, and another from the **Run Script** box to **End**. Afterward,
click on the three horizontal lines to the left of the Workflow name,
and select the **Publish** option. You are now ready to associate this
workflow with a catalog item.

![image8-1](https://www.ansible.com/hs-fs/hubfs/image8-1.png?width=524&name=image8-1.png){style="background-color: transparent; width: 524px;"
width="524"
srcset="https://www.ansible.com/hs-fs/hubfs/image8-1.png?width=262&name=image8-1.png 262w, https://www.ansible.com/hs-fs/hubfs/image8-1.png?width=524&name=image8-1.png 524w, https://www.ansible.com/hs-fs/hubfs/image8-1.png?width=786&name=image8-1.png 786w, https://www.ansible.com/hs-fs/hubfs/image8-1.png?width=1048&name=image8-1.png 1048w, https://www.ansible.com/hs-fs/hubfs/image8-1.png?width=1310&name=image8-1.png 1310w, https://www.ansible.com/hs-fs/hubfs/image8-1.png?width=1572&name=image8-1.png 1572w"
sizes="(max-width: 524px) 100vw, 524px"}

21. Navigate to **Service Catalog-\>Catalog Definitions-\>Maintain
Items**. Click the blue **New** button on the resulting item list. In
the resulting dialog box, fill in the following fields:

-   Name: Descriptive name of the Catalog Item
-   Catalog: The catalog that this item should be a part of
-   Category: Required if you wish users to be able to search for this
    item

In the Process Engine tab, populate the **Workflow** field with the
Workflow you just created. Click the Submit Button. You've not created a
new catalog item!

![image5-4](https://www.ansible.com/hs-fs/hubfs/image5-4.png?width=1629&name=image5-4.png){style="width: 1629px;"
width="1629"
srcset="https://www.ansible.com/hs-fs/hubfs/image5-4.png?width=815&name=image5-4.png 815w, https://www.ansible.com/hs-fs/hubfs/image5-4.png?width=1629&name=image5-4.png 1629w, https://www.ansible.com/hs-fs/hubfs/image5-4.png?width=2444&name=image5-4.png 2444w, https://www.ansible.com/hs-fs/hubfs/image5-4.png?width=3258&name=image5-4.png 3258w, https://www.ansible.com/hs-fs/hubfs/image5-4.png?width=4073&name=image5-4.png 4073w, https://www.ansible.com/hs-fs/hubfs/image5-4.png?width=4887&name=image5-4.png 4887w"
sizes="(max-width: 1629px) 100vw, 1629px"}

22. Lastly, to run this catalog item, navigate to
Self-Service-\>Homepage and search for the catalog item you just
created. Once found, click the **order now** button. You can see the
results page pop up in ServiceNow, and you can confirm that the Job is
being run in Ansible Tower.

Congratulations! After completing these steps, you can now use a
ServiceNow Catalog Item to launch Job and Workflow Templates in Ansible
Tower. This is ideal for allowing end users to use a front end they are
familiar with in order to perform automated tasks of varying
complexities. This familiarity goes a long way toward reducing the time
to value for the enterprise as a whole, rather than just the teams
responsible for writing the playbooks being used.
