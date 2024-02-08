---
author: Christian Adams
date: 2019-04-22 00:00 UTC
description: Ansible Tower 3.4 now has token authentication as a new
  method for authentication. This post summarizes the numerous
  enterprise authentication methods and the best use case for each.
lang: en-us
title: Summary of Authentication Methods For Red Hat Ansible Tower
---

# Summary of Authentication Methods For Red Hat Ansible Tower

Red Hat Ansible Tower 3.4.0 has added token authentication as a new
method for authentication so I wanted to use this post to summarize the
numerous enterprise authentication methods and the best use case for
each. Ansible Tower is designed for organizations to centralize and
control their automation with a visual dashboard for out-of-the box
control while providing a REST API to integrate with your other tooling
on a deeper level. We support a number of authentication methods to make
it easy to embed Ansible Tower into existing tools and processes to help
ensure the right people can access Ansible Tower resources. For this
blog post I will go over four of Ansible Tower's authentication methods:
Session, Basic, OAuth2 Token, and Single Sign-on (SSO). For each method
I will provide some quick examples and links to the relevant supporting
documentation, so you can easily integrate Ansible Tower into your
environment.

## Session Authentication

Session authentication is what's used when logging in directly to
Ansible Tower's API or UI. It is used when a user wants to remain logged
in for a prolonged period of time, not just for that HTTP request, i.e.
when browsing the UI or API in a browser like Chrome or Firefox. When a
user logs in, a session cookie is created, which enables the user to
remain logged in when navigating to different pages within Ansible
Tower.

![Blog-TAO-Login](/images/posts/archive/Blog-TAO-Login.png)

**How does it work?**

![Blog-TAO-API](/images/posts/archive/Blog-TAO-API.png)

Using the Curl tool, let's take a deeper look at what happens when you
log in to Ansible Tower.

1. GET to `/api/login/` endpoint to grab the `csrftoken` cookie

    ```bash
    curl -k -c - https://<tower-host>/api/login/

    localhost   FALSE   /   FALSE   0   csrftoken
    AswSFn5p1qQvaX4KoRZN6A5yer0Pq0VG2cXMTzZnzuhaY0L4tiidYqwf5PXZckuj
    ```


2. POST to the `/api/login/` endpoint with username, password, and
`X-CSRFToken=<token-value>`

    ```bash
    curl -X POST -H 'Content-Type: application/x-www-form-urlencoded' \
      --referer https://<tower-host>/api/login/ \
      -H 'X-CSRFToken: K580zVVm0rWX8pmNylz5ygTPamgUJxifrdJY0UDtMMoOis5Q1UOxRmV9918BUBIN' \
      --data 'username=root&password=reverse' \
      --cookie 'csrftoken=K580zVVm0rWX8pmNylz5ygTPamgUJxifrdJY0UDtMMoOis5Q1UOxRmV9918BUBIN' \
      https://<tower-host>/api/login/ -k -D - -o /dev/null
    ```

All of this is done by Ansible Tower when you log in to the UI or API in
the browser, and should only be used when authenticating in the browser.
For programmatic integration with Ansible Tower, you should use OAuth 2
tokens, not the process described above.

Note: The session expiration time can be changed by setting the
[SESSION_COOKIE_AGE](https://docs.ansible.com/ansible-tower/latest/html/administration/session_limits.html#working-with-session-limits)
setting.

Example with browsable API:

![Blog-TAO-Cred-List](/images/posts/archive/Blog-TAO-Cred-List.png)

## Basic Authentication

Basic Authentication is stateless, thus the base64 encoded \`username\`
and `password` must be sent along with each request via the
Authorization header.

Use Case: For API calls from curls, python scripts, or individual
requests to the API.  OAuth2 Authentication is recommended for accessing
the API when at all possible.  

Example with curl:

```bash
curl -X GET -H 'Authorization: Basic dXNlcjpwYXNzd29yZA==’
https://<tower-host>/api/v2/credentials -k -L

# the --user flag adds this Authorization header for us
curl -X GET --user 'user:password' https://<tower-host>/api/v2/credentials -k -L
```

For more information about the Basic HTTP Authentication scheme, see
[RFC 7617](https://tools.ietf.org/html/rfc7617).

Note: Basic Auth can be disabled for security purposes, see the
[docs](https://docs.ansible.com/ansible-tower/2.4.3/html/administration/social_auth.html#basic-authentication-settings)
for more info.

## OAuth 2 Token Authentication

OAuth (Open Authorization) is an open standard for token-based
authentication and authorization. OAuth 2 authentication is commonly
used when interacting with the Ansible Tower API programmatically. Like
Basic Auth, an OAuth 2 token is supplied with each API request via the
Authorization header. Unlike Basic Auth, OAuth 2 tokens have a
configurable timeout and are scopable. Tokens have a configurable
expiration time and can be easily revoked for one user or for the entire
Ansible Tower system by an admin if needed. This can be done with the
`tower-manage revoke_oauth2_tokens` management command. Here is[ more
information](https://docs.ansible.com/ansible-tower/latest/html/administration/tower-manage.html#revoke-oauth2-tokens)
on doing that. Additionally, the type of users able to create tokens can
be limited to users created in Ansible Tower, as opposed to external
users created from an SSO (see SSO section below). For more on how to do
this see the note in these
[docs](https://docs.ansible.com/ansible-tower/latest/html/administration/oauth2_token_auth.html#revoke-an-access-token).

Different methods for obtaining OAuth 2 Access Tokens in Ansible Tower:

-   Personal access tokens (PAT)
-   Application Token: Password grant type
-   Application Token: Implicit grant type
-   Application Token: Authorization Code grant type

First, a user needs to create an OAuth 2 Access Token in the API, or in
their User's `Token` tab in the UI. For the purposes of this article,
we will use the personal access token method (PAT) for creating a token.
Upon token creation, the user can set the scope. The expiration time of
the token can be configured system-wide as well.

Below is an example of creating a PAT in the UI:\
 ![Blog-TAO-Token](/images/posts/archive/Blog-TAO-Token.png)

Token authentication is best used for any programmatic use of Ansible
Tower's API, such as Python scripts or tools like curl. See the example
for a personal access token (PAT) below:

**Curl Example**

First, create an OAuth 2 token without an associated Application; in
other words, a personal access token. In this example, we will do so
through the API with curl.

```bash
curl -u user:password -k -X POST https://<tower-host>/api/v2/tokens/
```

You can now use that token to perform a GET request for an Ansible Tower
resource, e.g., Hosts.

```bash
curl -k -X POST \
    -H “Content-Type: application/json”
    -H “Authorization: Bearer <oauth2-token-value>” \
    https://<tower-host>/api/v2/hosts/
```

Similarly, a job can be launched by making a POST to the job template
that you want to launch.

```bash
curl -k -X POST \
    -H "Authorization: Bearer <oauth2-token-value>" \
    -H "Content-Type: application/json" \
    --data '{"limit" : "ansible"}' \
    https://<tower>/api/v2/job_templates/14/launch/
```

**Python Example**

Tower-CLI is an open source tool that makes it easy to use HTTP requests
to access Ansible Tower's API. You can have Tower-CLI authenticate to
Tower using your OAuth 2 token by setting it in `tower-cli config`, or
have it acquire a PAT on your behalf by using the `tower-cli login`
command. It is easy to use and I would recommend checking it out:

```bash
pip install ansible-tower-cli

tower-cli config tower
tower-cli login
```

For more information on how to use OAuth 2 in Ansible Tower in the
context of integrating external applications, check out these
[docs](https://docs.ansible.com/ansible-tower/latest/html/administration/oauth2_token_auth.html).

If you need to write custom requests, you can write a Python script
using the [Python library requests](https://pypi.org/project/requests/). Here is
an example.

```python
import requests

oauth2_token_value = 'y1Q8ye4hPvT61aQq63Da6N1C25jiA'   # your token value from Tower
url = 'https://<tower-host>/api/v2/users/'
payload = {}
headers = {'Authorization': 'Bearer ' + oauth2_token_value,}

# makes request to Tower user endpoint
response = requests.request('GET', url, headers=headers, data=payload,
allow_redirects=False, verify=False)

# prints json returned from Tower with formatting
print(json.dumps(response.json(), indent=4, sort_keys=True))
```

## SSO Authentication

Single sign-on (SSO) authentication methods are fundamentally different
because the authentication of the user happens external to Ansible
Tower. For example, with GitHub SSO GitHub is the single source of
truth, which verifies your identity based on the username and password
you gave Tower.

Once you have configured an SSO method in Ansible Tower, a button for
that SSO will be present on the login screen. If you click that button,
it will redirect you to the Identity Provider, in this case GitHub,
where you will present your credentials. If the Identity Provider
verifies you successfully, then Ansible Tower will make a user linked to
your GitHub user (if this is your first time logging in via this SSO
method), and log you in.

-   [LDAP](https://docs.ansible.com/ansible-tower/latest/html/administration/ldap_auth.html#ag-ldap) -
    a directory of identities external to Ansible Tower that can be used
    to check authentication credentials against. Active Directory can be
    configured via the LDAP SSO in Ansible Tower.
-   SAML - allows Ansible Tower users to authenticate via a single
    sign-on authentication service, so that authentication is consistent
    for the user across multiple services used by their team. SAML is
    particularly useful for maintaining permission groups across
    services.
-   [GitHub](https://docs.ansible.com/ansible-tower/latest/html/administration/social_auth.html#github-oauth2-settings) -
    allows Ansible Tower users to authenticate with their GitHub
    credentials if they are in the Github Organization, Team or User
    that the system admin specified in
    \`/api/v2/settings/authentication/\`. Ansible Tower uses OAuth 2 to
    verify the user's credentials with GitHub.
-   [Azure Active
    Directory](https://docs.ansible.com/ansible-tower/latest/html/administration/ent_auth.html#azure-active-directory-ad) -
    allows Ansible Tower users to authenticate with the Azure
    credentials. Ansible Tower uses OAuth 2 to authenticate to Azure to
    verify your credentials and obtain user group data.
-   [RADIUS](https://docs.ansible.com/ansible-tower/latest/html/administration/ent_auth.html#radius-authentication-settings) -
    is an authentication protocol generally used for network devices. It
    can minimize network traffic for authentication, as it is
    lightweight.
-   [Google OAuth](https://docs.ansible.com/ansible-tower/latest/html/administration/social_auth.html#google-oauth2-settings) -
    allows Ansible Tower users to authenticate with their Google Cloud.
    Ansible Tower authenticates to Google using the OAuth 2 protocol to
    check your username and password credentials against the identities
    in your Google organization.

## Which Authentication is right for me?

I've shown you four types of authentication you can use in Ansible
Tower. Each method has pros and cons and lends itself to certain use
cases.

-   **Session Authentication** (logging in to the UI or browsable API): I am using Ansible Tower to manually create resources (inventory, project, job template) and launch jobs in the browser.
-   **Basic Authentication:**  I am troubleshooting Ansible Tower with curl, HTTPie, or another similar tool and have not yet set up an OAuth 2 Token for my user
-   **OAuth 2 Token Authentication**
    -   Authorization Code Flow -I am a user of an application interfacing with Ansible Tower
    -   Personal Access Tokens (PAT) - I am automating my usage of Ansible Tower programmatically
-   **SSO:** I am using Ansible Tower inside a large organization and want to use a central Identity provider or want to allow users to authenticate using external authentication like Google SSO, Azure SSO, LDAP, SAML, or GitHub.

You now have the knowledge needed to choose the most effective
authentication methods for your needs! I hope this guide helps to
clarify your options for authenticating with Ansible Tower.
