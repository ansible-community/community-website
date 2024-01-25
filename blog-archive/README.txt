This directory contains markdown files of blog posts migrated from "ansible.com".

Nikola builds posts in this directory using the ("blog-archive/*.md", "blog", "post.tmpl"), tuple in conf.py.
We do this so that the resulting urls are at the root of the "blog" context and match the original url on "ansible.com".
This prevents the need to define redirects.

You should not move this folder or the markdown files within it.
Doing so risks 404 urls and broken links to blog posts.
