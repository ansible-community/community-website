---
author: Juan Manuel
date: 2018-06-14 00:00 UTC
description: Red Hat Ansible Tower supports SAML authentication (both N
  and Z) by default. This document will guide you through the steps for
  configuring both products to delegate the authentication to
  RHSSO/Keycloak (Red Hat Single Sign-On).
lang: en-us
title: Red Hat Single Sign-on Integration with Ansible Tower
---

# Red Hat Single Sign-on Integration with Ansible Tower

[![RH-Ansible-Tower-SSO](https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-Ansible-Tower-SSO.png?width=1024&name=RH-Ansible-Tower-SSO.png){width="1024"
style="width: 1024px;"
srcset="https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-Ansible-Tower-SSO.png?width=512&name=RH-Ansible-Tower-SSO.png 512w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-Ansible-Tower-SSO.png?width=1024&name=RH-Ansible-Tower-SSO.png 1024w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-Ansible-Tower-SSO.png?width=1536&name=RH-Ansible-Tower-SSO.png 1536w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-Ansible-Tower-SSO.png?width=2048&name=RH-Ansible-Tower-SSO.png 2048w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-Ansible-Tower-SSO.png?width=2560&name=RH-Ansible-Tower-SSO.png 2560w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-Ansible-Tower-SSO.png?width=3072&name=RH-Ansible-Tower-SSO.png 3072w"
sizes="(max-width: 1024px) 100vw, 1024px"} ]{#hs_cos_wrapper_post_body
.hs_cos_wrapper .hs_cos_wrapper_meta_field

As you might know, Red Hat Ansible Tower supports SAML authentication
(both N and Z) by default. This document will guide you through the
steps for configuring both products to delegate the authentication to
RHSSO/Keycloak (Red Hat Single Sign-On).

Requirements:

-   A running RHSSO/Keycloak instance
-   Ansible Tower
-   Admin rights for both
-   DNS resolution

## Hands-On Lab

Unless you have your own certificate already, the first step will be to
create one. To do so, execute the following command:

`openssl req -new -x509 -days 365 -nodes -out saml.crt -keyout saml.key`

Now we need to create the Ansible Tower Realm on the RHSSO platform. Go
to the \"Select Realm\" drop-down and click on \"Add new realm\":

![Ansible-Tower-SSO-Screen-16](https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-16.png?width=383&name=Ansible-Tower-SSO-Screen-16.png){width="383"
style="width: 383px;"
srcset="https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-16.png?width=192&name=Ansible-Tower-SSO-Screen-16.png 192w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-16.png?width=383&name=Ansible-Tower-SSO-Screen-16.png 383w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-16.png?width=575&name=Ansible-Tower-SSO-Screen-16.png 575w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-16.png?width=766&name=Ansible-Tower-SSO-Screen-16.png 766w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-16.png?width=958&name=Ansible-Tower-SSO-Screen-16.png 958w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-16.png?width=1149&name=Ansible-Tower-SSO-Screen-16.png 1149w"
sizes="(max-width: 383px) 100vw, 383px"}

Once created, go to the \"Keys\" tab and delete all certificates, keys,
etc. that were created by default.

Now that we have a clean realm, let\'s populate it with the appropriate
information. Click on \"Add Keystore\" in the upper right corner and
click on RSA:

![Ansible-Tower-SSO-Screen-15](https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-15.png?width=1074&name=Ansible-Tower-SSO-Screen-15.png){width="1074"
style="width: 1074px;"
srcset="https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-15.png?width=537&name=Ansible-Tower-SSO-Screen-15.png 537w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-15.png?width=1074&name=Ansible-Tower-SSO-Screen-15.png 1074w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-15.png?width=1611&name=Ansible-Tower-SSO-Screen-15.png 1611w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-15.png?width=2148&name=Ansible-Tower-SSO-Screen-15.png 2148w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-15.png?width=2685&name=Ansible-Tower-SSO-Screen-15.png 2685w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-15.png?width=3222&name=Ansible-Tower-SSO-Screen-15.png 3222w"
sizes="(max-width: 1074px) 100vw, 1074px"}

Click on Save and create your Ansible Tower client information. It is
recommend to start with the Tower configuration so that you can inject
the metadata file and customize a few of the fields.

Log in as the admin user on Ansible Tower and go to \"Settings \>
Configure Tower \> Authentication \> SAML\". Here you will find many
fields (two of them read-only), that give us the information necessary
to make this work:

-   Assertion Consumer Service
-   Metadata URL for the Service Provider (this will return the
    configuration for your IDP)

 ![Ansible-Tower-SSO-Screen-18](https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-18.png?width=1869&name=Ansible-Tower-SSO-Screen-18.png){width="1869"
style="width: 1869px;"
srcset="https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-18.png?width=935&name=Ansible-Tower-SSO-Screen-18.png 935w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-18.png?width=1869&name=Ansible-Tower-SSO-Screen-18.png 1869w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-18.png?width=2804&name=Ansible-Tower-SSO-Screen-18.png 2804w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-18.png?width=3738&name=Ansible-Tower-SSO-Screen-18.png 3738w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-18.png?width=4673&name=Ansible-Tower-SSO-Screen-18.png 4673w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-18.png?width=5607&name=Ansible-Tower-SSO-Screen-18.png 5607w"
sizes="(max-width: 1869px) 100vw, 1869px"}

\
Now let\'s fill all the required fields:

-   EntityID for SAML Service Provider: `tower.usersys.redhat.com` (must
    be the same on RHSSO as `client_id` name)
-   Pub Cert: use the saml.crt (`cat saml.crt` and copy/paste)
-   Private Key: use the same.key (`cat saml.key` and copy/paste)

![Ansible-Tower-SSO-Screen-17](https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-17.png?width=1194&name=Ansible-Tower-SSO-Screen-17.png){width="1194"
style="width: 1194px;"
srcset="https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-17.png?width=597&name=Ansible-Tower-SSO-Screen-17.png 597w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-17.png?width=1194&name=Ansible-Tower-SSO-Screen-17.png 1194w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-17.png?width=1791&name=Ansible-Tower-SSO-Screen-17.png 1791w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-17.png?width=2388&name=Ansible-Tower-SSO-Screen-17.png 2388w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-17.png?width=2985&name=Ansible-Tower-SSO-Screen-17.png 2985w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-17.png?width=3582&name=Ansible-Tower-SSO-Screen-17.png 3582w"
sizes="(max-width: 1194px) 100vw, 1194px"}

-   Org info of Service Provider:

```yml
{
  "en-US": {
    "url": "https://rhsso.usersys.redhat.com:8443",
    "displayname": "RHSSO Solutions Engineering",
    "name": "RHSSO"
  }
}
```

![Ansible-Tower-SSO-Screen-4](https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-4.png?width=540&name=Ansible-Tower-SSO-Screen-4.png){width="540"
style="width: 540px;"
srcset="https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-4.png?width=270&name=Ansible-Tower-SSO-Screen-4.png 270w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-4.png?width=540&name=Ansible-Tower-SSO-Screen-4.png 540w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-4.png?width=810&name=Ansible-Tower-SSO-Screen-4.png 810w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-4.png?width=1080&name=Ansible-Tower-SSO-Screen-4.png 1080w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-4.png?width=1350&name=Ansible-Tower-SSO-Screen-4.png 1350w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-4.png?width=1620&name=Ansible-Tower-SSO-Screen-4.png 1620w"
sizes="(max-width: 540px) 100vw, 540px"}

-   Technical contact for SAML Service Provider:

```yml
{
  "givenName": "Juan Manuel Parrilla",
  "emailAddress": "jparrill@redhat.com"
}
```

![Ansible-Tower-SSO-Screen-7](https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-7.png?width=425&name=Ansible-Tower-SSO-Screen-7.png){width="425"
style="width: 425px;"
srcset="https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-7.png?width=213&name=Ansible-Tower-SSO-Screen-7.png 213w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-7.png?width=425&name=Ansible-Tower-SSO-Screen-7.png 425w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-7.png?width=638&name=Ansible-Tower-SSO-Screen-7.png 638w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-7.png?width=850&name=Ansible-Tower-SSO-Screen-7.png 850w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-7.png?width=1063&name=Ansible-Tower-SSO-Screen-7.png 1063w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-7.png?width=1275&name=Ansible-Tower-SSO-Screen-7.png 1275w"
sizes="(max-width: 425px) 100vw, 425px"}

-   Support contact for SAML Service Provider:

```yml
{
  "givenName": "Juan Manuel Parrilla",
  "emailAddress": "jparrill@redhat.com"
}
```

 ![Ansible-Tower-SSO-Screen-7](https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-7.png?width=425&name=Ansible-Tower-SSO-Screen-7.png){width="425"
style="width: 425px;"
srcset="https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-7.png?width=213&name=Ansible-Tower-SSO-Screen-7.png 213w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-7.png?width=425&name=Ansible-Tower-SSO-Screen-7.png 425w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-7.png?width=638&name=Ansible-Tower-SSO-Screen-7.png 638w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-7.png?width=850&name=Ansible-Tower-SSO-Screen-7.png 850w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-7.png?width=1063&name=Ansible-Tower-SSO-Screen-7.png 1063w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-7.png?width=1275&name=Ansible-Tower-SSO-Screen-7.png 1275w"
sizes="(max-width: 425px) 100vw, 425px"}

-   Enabled SAML Identity Providers:

```yml
{
   "RHSSO": {
      "attr_last_name": "last_name",
      "attr_username": "username",
      "entity_id": "https://rhsso.usersys.redhat.com:8443/auth/realms/tower",
      "attr_user_permanent_id": "name_id",
      "url": "https://rhsso.usersys.redhat.com:8443/auth/realms/tower/protocol/saml",
      "attr_email": "email",
      "x509cert": "",
      "attr_first_name": "first_name",
      "attr_groups": "groups"
   }
}
```

Note: To provide the x509cert field on the JSON, just execute this command and paste the result on the Ansible Tower interface:

```bash
[sed \':a;N;\$!ba;s/\\n//g\' saml.crt]
```

 ![Ansible-Tower-SSO-Screen-20](https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-20.png?width=685&name=Ansible-Tower-SSO-Screen-20.png){width="685"
style="width: 685px;"
srcset="https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-20.png?width=343&name=Ansible-Tower-SSO-Screen-20.png 343w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-20.png?width=685&name=Ansible-Tower-SSO-Screen-20.png 685w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-20.png?width=1028&name=Ansible-Tower-SSO-Screen-20.png 1028w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-20.png?width=1370&name=Ansible-Tower-SSO-Screen-20.png 1370w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-20.png?width=1713&name=Ansible-Tower-SSO-Screen-20.png 1713w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-20.png?width=2055&name=Ansible-Tower-SSO-Screen-20.png 2055w"
sizes="(max-width: 685px) 100vw, 685px"}

 

-   Organization SAML Map:

```yml
{
   "Default": {
      "users": true
   },
   "Systems Engineering": {
      "admins": [
         "acheron@redhat.com",
         "jparrill@redhat.com",
         "covenant@redhat.com",
         "olympia@redhat.com
      ],
      "remove_admins": false,
      "remove_users": false,
      "users": true
   }
}
```

 ![Ansible-Tower-SSO-Screen-10](https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-10.png?width=356&name=Ansible-Tower-SSO-Screen-10.png){width="356"
style="width: 356px;"
srcset="https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-10.png?width=178&name=Ansible-Tower-SSO-Screen-10.png 178w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-10.png?width=356&name=Ansible-Tower-SSO-Screen-10.png 356w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-10.png?width=534&name=Ansible-Tower-SSO-Screen-10.png 534w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-10.png?width=712&name=Ansible-Tower-SSO-Screen-10.png 712w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-10.png?width=890&name=Ansible-Tower-SSO-Screen-10.png 890w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-10.png?width=1068&name=Ansible-Tower-SSO-Screen-10.png 1068w"
sizes="(max-width: 356px) 100vw, 356px"}

## Recommended Steps and Things to Check

-   RHSSO is the chosen name, which can be whatever you want and is not
    tied to DNS or server configurations. This is simply a visual
    marker.
-   All the `attr_ fields` are required to work and will be mappers on
    the client that we will create on the next step.
-   `Entity_id` will point to your realm. Go to your RHSSO realm through
    WebUI and in "General" you will see \"OpenID Endpoint
    Configuration\". Just click and catch the \"issuer\" field to
    fulfill the `entity_id`.
-   "For url" is a fixed field; put your `entity_id` there, followed by
    `/protocol/saml`.
-   If you generated your cert/key in RHSSO, you will have them in one
    line. To convert to PEM format you can just wrap them in
    \"\-\-\-\--BEGIN CERTIFICATE\-\-\-\--\" etc. and use `fold -w64` to
    split the single line.

## RHSSO Client Configuration

Now that you\'ve configured SAML on Ansible Tower save the changes and
start with the RHSSO Client configuration.

First, log in as the admin user on the RHSSO platform and go to the
\"Tower\" realm. From there, go to "Clients" and select "Create". Click
on "select file" to import the data that we already have on Ansible
Tower (to get the configuration execute this command from your laptop:
`curl -L -k https://tower.usersys.redhat.com/sso/metadata/saml/`).
Modify the Client ID by pointing it to `tower.usersys.redhat.com`, then
set the "Client Protocol" to SAML as displayed below:

![Ansible-Tower-SSO-Screen-19](https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-19.png?width=419&name=Ansible-Tower-SSO-Screen-19.png){width="419"
style="width: 419px;"
srcset="https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-19.png?width=210&name=Ansible-Tower-SSO-Screen-19.png 210w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-19.png?width=419&name=Ansible-Tower-SSO-Screen-19.png 419w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-19.png?width=629&name=Ansible-Tower-SSO-Screen-19.png 629w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-19.png?width=838&name=Ansible-Tower-SSO-Screen-19.png 838w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-19.png?width=1048&name=Ansible-Tower-SSO-Screen-19.png 1048w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-19.png?width=1257&name=Ansible-Tower-SSO-Screen-19.png 1257w"
sizes="(max-width: 419px) 100vw, 419px"}

Next, fix the configuration to fit the following screenshot:

![Ansible-Tower-SSO-Screen-1](https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-1.png?width=500&name=Ansible-Tower-SSO-Screen-1.png){width="500"
style="width: 500px;"
srcset="https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-1.png?width=250&name=Ansible-Tower-SSO-Screen-1.png 250w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-1.png?width=500&name=Ansible-Tower-SSO-Screen-1.png 500w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-1.png?width=750&name=Ansible-Tower-SSO-Screen-1.png 750w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-1.png?width=1000&name=Ansible-Tower-SSO-Screen-1.png 1000w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-1.png?width=1250&name=Ansible-Tower-SSO-Screen-1.png 1250w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-1.png?width=1500&name=Ansible-Tower-SSO-Screen-1.png 1500w"
sizes="(max-width: 500px) 100vw, 500px"}

The last step to take is to create the mappers on Tower\'s RHSSO client.
The purpose of this is to define the information that comes from your
RHSSO, which will be mapped against Ansible Tower users.

To do this, we must go to Mappers tab:

![Ansible-Tower-SSO-Screen-14](https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-14.png?width=501&name=Ansible-Tower-SSO-Screen-14.png){width="501"
style="width: 501px;"
srcset="https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-14.png?width=251&name=Ansible-Tower-SSO-Screen-14.png 251w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-14.png?width=501&name=Ansible-Tower-SSO-Screen-14.png 501w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-14.png?width=752&name=Ansible-Tower-SSO-Screen-14.png 752w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-14.png?width=1002&name=Ansible-Tower-SSO-Screen-14.png 1002w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-14.png?width=1253&name=Ansible-Tower-SSO-Screen-14.png 1253w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-14.png?width=1503&name=Ansible-Tower-SSO-Screen-14.png 1503w"
sizes="(max-width: 501px) 100vw, 501px"}

\
Displayed below are the necessary mappers:

![Ansible-Tower-SSO-Screen-6](https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-6.png?width=1574&name=Ansible-Tower-SSO-Screen-6.png){width="1574"
style="width: 1574px;"
srcset="https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-6.png?width=787&name=Ansible-Tower-SSO-Screen-6.png 787w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-6.png?width=1574&name=Ansible-Tower-SSO-Screen-6.png 1574w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-6.png?width=2361&name=Ansible-Tower-SSO-Screen-6.png 2361w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-6.png?width=3148&name=Ansible-Tower-SSO-Screen-6.png 3148w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-6.png?width=3935&name=Ansible-Tower-SSO-Screen-6.png 3935w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-6.png?width=4722&name=Ansible-Tower-SSO-Screen-6.png 4722w"
sizes="(max-width: 1574px) 100vw, 1574px"}

\
The following screenshot shows proper configuration of user name, last
name, email, user ID, and first name:\
![Ansible-Tower-SSO-Screen-22](https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-22.png?width=419&name=Ansible-Tower-SSO-Screen-22.png){width="419"
style="width: 419px;"
srcset="https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-22.png?width=210&name=Ansible-Tower-SSO-Screen-22.png 210w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-22.png?width=419&name=Ansible-Tower-SSO-Screen-22.png 419w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-22.png?width=629&name=Ansible-Tower-SSO-Screen-22.png 629w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-22.png?width=838&name=Ansible-Tower-SSO-Screen-22.png 838w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-22.png?width=1048&name=Ansible-Tower-SSO-Screen-22.png 1048w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-22.png?width=1257&name=Ansible-Tower-SSO-Screen-22.png 1257w"
sizes="(max-width: 419px) 100vw, 419px"}

 ![Ansible-Tower-SSO-Screen-11](https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-11.png?width=419&name=Ansible-Tower-SSO-Screen-11.png){width="419"
style="width: 419px;"
srcset="https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-11.png?width=210&name=Ansible-Tower-SSO-Screen-11.png 210w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-11.png?width=419&name=Ansible-Tower-SSO-Screen-11.png 419w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-11.png?width=629&name=Ansible-Tower-SSO-Screen-11.png 629w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-11.png?width=838&name=Ansible-Tower-SSO-Screen-11.png 838w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-11.png?width=1048&name=Ansible-Tower-SSO-Screen-11.png 1048w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-11.png?width=1257&name=Ansible-Tower-SSO-Screen-11.png 1257w"
sizes="(max-width: 419px) 100vw, 419px"}

 ![Ansible-Tower-SSO-Screen-8](https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-8.png?width=419&name=Ansible-Tower-SSO-Screen-8.png){width="419"
style="width: 419px;"
srcset="https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-8.png?width=210&name=Ansible-Tower-SSO-Screen-8.png 210w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-8.png?width=419&name=Ansible-Tower-SSO-Screen-8.png 419w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-8.png?width=629&name=Ansible-Tower-SSO-Screen-8.png 629w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-8.png?width=838&name=Ansible-Tower-SSO-Screen-8.png 838w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-8.png?width=1048&name=Ansible-Tower-SSO-Screen-8.png 1048w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-8.png?width=1257&name=Ansible-Tower-SSO-Screen-8.png 1257w"
sizes="(max-width: 419px) 100vw, 419px"}

 ![Ansible-Tower-SSO-Screen-9](https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-9.png?width=419&name=Ansible-Tower-SSO-Screen-9.png){width="419"
style="width: 419px;"
srcset="https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-9.png?width=210&name=Ansible-Tower-SSO-Screen-9.png 210w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-9.png?width=419&name=Ansible-Tower-SSO-Screen-9.png 419w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-9.png?width=629&name=Ansible-Tower-SSO-Screen-9.png 629w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-9.png?width=838&name=Ansible-Tower-SSO-Screen-9.png 838w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-9.png?width=1048&name=Ansible-Tower-SSO-Screen-9.png 1048w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-9.png?width=1257&name=Ansible-Tower-SSO-Screen-9.png 1257w"
sizes="(max-width: 419px) 100vw, 419px"}

 ![Ansible-Tower-SSO-Screen-3](https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-3.png?width=419&name=Ansible-Tower-SSO-Screen-3.png){width="419"
style="width: 419px;"
srcset="https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-3.png?width=210&name=Ansible-Tower-SSO-Screen-3.png 210w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-3.png?width=419&name=Ansible-Tower-SSO-Screen-3.png 419w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-3.png?width=629&name=Ansible-Tower-SSO-Screen-3.png 629w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-3.png?width=838&name=Ansible-Tower-SSO-Screen-3.png 838w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-3.png?width=1048&name=Ansible-Tower-SSO-Screen-3.png 1048w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-3.png?width=1257&name=Ansible-Tower-SSO-Screen-3.png 1257w"
sizes="(max-width: 419px) 100vw, 419px"}

Note: \"firstName\" and \"lastName\" are case sensitive since they map the RHSSO user property.

### Now you're all set!

Let\'s test with a user that we already have on our RHSSO (we have RHSSO
with a user federation against `ldap.example.com`). For testing
purposes, you can create a user on \"Manage \> Users\" if you wish.

Now go to the Ansible Tower login page and you should see "Sign in With
S":

![](https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-21.png?width=442&name=Ansible-Tower-SSO-Screen-21.png){width="442"
style="width: 442px;"
srcset="https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-21.png?width=221&name=Ansible-Tower-SSO-Screen-21.png 221w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-21.png?width=442&name=Ansible-Tower-SSO-Screen-21.png 442w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-21.png?width=663&name=Ansible-Tower-SSO-Screen-21.png 663w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-21.png?width=884&name=Ansible-Tower-SSO-Screen-21.png 884w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-21.png?width=1105&name=Ansible-Tower-SSO-Screen-21.png 1105w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-21.png?width=1326&name=Ansible-Tower-SSO-Screen-21.png 1326w"
sizes="(max-width: 442px) 100vw, 442px"}\
\

Click on this \"S\" and you will be redirected to login on your RHSSO
server:

![Ansible-Tower-SSO-Screen-2](https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-2.png?width=438&name=Ansible-Tower-SSO-Screen-2.png){width="438"
style="width: 438px;"
srcset="https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-2.png?width=219&name=Ansible-Tower-SSO-Screen-2.png 219w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-2.png?width=438&name=Ansible-Tower-SSO-Screen-2.png 438w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-2.png?width=657&name=Ansible-Tower-SSO-Screen-2.png 657w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-2.png?width=876&name=Ansible-Tower-SSO-Screen-2.png 876w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-2.png?width=1095&name=Ansible-Tower-SSO-Screen-2.png 1095w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-2.png?width=1314&name=Ansible-Tower-SSO-Screen-2.png 1314w"
sizes="(max-width: 438px) 100vw, 438px"} 

\
And that\'s it!\
![Ansible-Tower-SSO-Screen-5](https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-5.png?width=372&name=Ansible-Tower-SSO-Screen-5.png){width="372"
style="width: 372px;"
srcset="https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-5.png?width=186&name=Ansible-Tower-SSO-Screen-5.png 186w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-5.png?width=372&name=Ansible-Tower-SSO-Screen-5.png 372w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-5.png?width=558&name=Ansible-Tower-SSO-Screen-5.png 558w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-5.png?width=744&name=Ansible-Tower-SSO-Screen-5.png 744w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-5.png?width=930&name=Ansible-Tower-SSO-Screen-5.png 930w, https://www.ansible.com/hs-fs/hubfs/2018_Images/Social-Blog/RH-SSO-Ansible-Tower-Screens/Ansible-Tower-SSO-Screen-5.png?width=1116&name=Ansible-Tower-SSO-Screen-5.png 1116w"
sizes="(max-width: 372px) 100vw, 372px"}

\
Hope this was a helpful guide to Red Hat Single Sign-On integration with
Ansible Tower!
