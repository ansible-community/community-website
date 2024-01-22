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
to the "Select Realm" drop-down and click on "Add new realm":

![Ansible-Tower-SSO-Screen-16](/images/posts/archive/Ansible-Tower-SSO-Screen-16.png)

Once created, go to the "Keys" tab and delete all certificates, keys,
etc. that were created by default.

Now that we have a clean realm, let's populate it with the appropriate
information. Click on "Add Keystore" in the upper right corner and
click on RSA:

![Ansible-Tower-SSO-Screen-15](/images/posts/archive/Ansible-Tower-SSO-Screen-15.png)

Click on Save and create your Ansible Tower client information. It is
recommend to start with the Tower configuration so that you can inject
the metadata file and customize a few of the fields.

Log in as the admin user on Ansible Tower and go to "Settings >
Configure Tower > Authentication > SAML". Here you will find many
fields (two of them read-only), that give us the information necessary
to make this work:

-   Assertion Consumer Service
-   Metadata URL for the Service Provider (this will return the
    configuration for your IDP)

![Ansible-Tower-SSO-Screen-18](/images/posts/archive/Ansible-Tower-SSO-Screen-18.png)


Now let's fill all the required fields:

-   EntityID for SAML Service Provider: `tower.usersys.redhat.com` (must
    be the same on RHSSO as `client_id` name)
-   Pub Cert: use the saml.crt (`cat saml.crt` and copy/paste)
-   Private Key: use the same.key (`cat saml.key` and copy/paste)

![Ansible-Tower-SSO-Screen-17](/images/posts/archive/Ansible-Tower-SSO-Screen-17.png)

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

![Ansible-Tower-SSO-Screen-4](/images/posts/archive/Ansible-Tower-SSO-Screen-4.png)

-   Technical contact for SAML Service Provider:

```yml
{
  "givenName": "Juan Manuel Parrilla",
  "emailAddress": "jparrill@redhat.com"
}
```

![Ansible-Tower-SSO-Screen-7](/images/posts/archive/Ansible-Tower-SSO-Screen-7.png)

-   Support contact for SAML Service Provider:

```yml
{
  "givenName": "Juan Manuel Parrilla",
  "emailAddress": "jparrill@redhat.com"
}
```

![Ansible-Tower-SSO-Screen-7](/images/posts/archive/Ansible-Tower-SSO-Screen-7.png)

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
sed ':a;N;$!ba;s/\n//g' saml.crt
```

![Ansible-Tower-SSO-Screen-20](/images/posts/archive/Ansible-Tower-SSO-Screen-20.png)


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

![Ansible-Tower-SSO-Screen-10](/images/posts/archive/Ansible-Tower-SSO-Screen-10.png)

## Recommended Steps and Things to Check

-   RHSSO is the chosen name, which can be whatever you want and is not
    tied to DNS or server configurations. This is simply a visual
    marker.
-   All the `attr_ fields` are required to work and will be mappers on
    the client that we will create on the next step.
-   `Entity_id` will point to your realm. Go to your RHSSO realm through
    WebUI and in "General" you will see "OpenID Endpoint
    Configuration". Just click and catch the "issuer" field to
    fulfill the `entity_id`.
-   "For url" is a fixed field; put your `entity_id` there, followed by
    `/protocol/saml`.
-   If you generated your cert/key in RHSSO, you will have them in one
    line. To convert to PEM format you can just wrap them in
    "-----BEGIN CERTIFICATE-----" etc. and use `fold -w64` to
    split the single line.

## RHSSO Client Configuration

Now that you've configured SAML on Ansible Tower save the changes and
start with the RHSSO Client configuration.

First, log in as the admin user on the RHSSO platform and go to the
"Tower" realm. From there, go to "Clients" and select "Create". Click
on "select file" to import the data that we already have on Ansible
Tower (to get the configuration execute this command from your laptop:
`curl -L -k https://tower.usersys.redhat.com/sso/metadata/saml/`).
Modify the Client ID by pointing it to `tower.usersys.redhat.com`, then
set the "Client Protocol" to SAML as displayed below:

![Ansible-Tower-SSO-Screen-19](/images/posts/archive/Ansible-Tower-SSO-Screen-19.png)

Next, fix the configuration to fit the following screenshot:

![Ansible-Tower-SSO-Screen-1](/images/posts/archive/Ansible-Tower-SSO-Screen-1.png)

The last step to take is to create the mappers on Tower's RHSSO client.
The purpose of this is to define the information that comes from your
RHSSO, which will be mapped against Ansible Tower users.

To do this, we must go to Mappers tab:

![Ansible-Tower-SSO-Screen-14](/images/posts/archive/Ansible-Tower-SSO-Screen-14.png)

Displayed below are the necessary mappers:

![Ansible-Tower-SSO-Screen-6](/images/posts/archive/Ansible-Tower-SSO-Screen-6.png)

The following screenshot shows proper configuration of user name, last
name, email, user ID, and first name:

![Ansible-Tower-SSO-Screen-22](/images/posts/archive/Ansible-Tower-SSO-Screen-22.png)

![Ansible-Tower-SSO-Screen-11](/images/posts/archive/Ansible-Tower-SSO-Screen-11.png)

![Ansible-Tower-SSO-Screen-8](/images/posts/archive/Ansible-Tower-SSO-Screen-8.png)

![Ansible-Tower-SSO-Screen-9](/images/posts/archive/Ansible-Tower-SSO-Screen-9.png)

![Ansible-Tower-SSO-Screen-3](/images/posts/archive/Ansible-Tower-SSO-Screen-3.png)

Note: "firstName" and "lastName" are case sensitive since they map the RHSSO user property.

### Now you're all set!

Let's test with a user that we already have on our RHSSO (we have RHSSO
with a user federation against `ldap.example.com`). For testing
purposes, you can create a user on "Manage > Users" if you wish.

Now go to the Ansible Tower login page and you should see "Sign in With S":

![Ansible-Tower-SSO-Screen-21](/images/posts/archive/Ansible-Tower-SSO-Screen-21.png)

Click on this "S" and you will be redirected to login on your RHSSO
server:

![Ansible-Tower-SSO-Screen-2](/images/posts/archive/Ansible-Tower-SSO-Screen-2.png)

And that's it!
![Ansible-Tower-SSO-Screen-5](/images/posts/archive/Ansible-Tower-SSO-Screen-5.png)

Hope this was a helpful guide to Red Hat Single Sign-On integration with
Ansible Tower!
