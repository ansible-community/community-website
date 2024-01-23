---
author: Mark Phillips
date: 2018-09-26 00:00 UTC
description: Simple. Powerful. Agentless. This has been the Ansible
  messaging since the journey began. Mark Phillips reveals why as time
  has gone on, the definition of simple we're talking about may have
  been misunderstood.
lang: en-us
title: Large Scale Deployments Using Ansible
---

# Large Scale Deployments Using Ansible

The Ansible simplicity is about being easy to understand, learn and
share. It's about people. The often peddled notion that "Ansible doesn't
scale past 500 hosts" is shadowed by the customers we have with over
100,000 nodes under management. But the idea that scale is purely about
the number of hosts isn't recognising the greater relevance. Scale is so
much more, scale is about the context in your business.

## What is scale?

According to most dictionaries, scale is a noun that means the relative size or extent of something.

## Technological Scale

When it comes to IT, conclusions about 'scale' usually equate to numbers
of something technical. A frequent customer ask might go something like
"We need Ansible to scale to 70,000 hosts".

Once we look into that number though, the reality is no technical
operation will happen across them all at once. The jeopardy to a
business of this size is too great to chance a failure of every system.
Operations at large scale happen piecemeal for safety reasons -- rolling
updates are not only a safer way to operate, we see the results faster.

Business function, geography, application and networks all affect the
big number, and all can be 'sliced up' in ways which minimise risk --
with the added benefit of enabling large scale operation.

Looking at the other side of the equation, the technology itself, also
carries nuance. A large and complex operation takes more resources --
memory, compute, etc -- compared to a small and simple task. The numbers
of hosts we're able to operate on in parallel will change depending on
the ask.

### Human Scale

There are at least half a dozen different ways to achieve anything in
IT. The choice we settle on can depend on many factors, but a powerful
influencer will be people.

A startup might pick a high level programming language to write their
application in because it's quick and easy to get going with. A little
code produces a lot of results -- unlike writing in C, or even
assembler! We all know coding C will result in fast programs requiring
fewer compute resources. That will give us greater utilisation for a
given piece of hardware. But the act of programming will likely be
slower, and the pool of talent shallower. To kickstart a project a
'slower' language leads to faster growth. As the business grows it
will add coders with skills in the existing language used, as they'll
get up to speed the quickest.

Some technology is harder to learn than others. But a language that is
understandable by anyone, with or without existing skills, is going to
be faster to pick up.

There's a chapter in Malcolm Gladwell's "Outliers: The story of
success" titled "Rice paddies and math tests". In short, he tells us
how the Chinese number system means kids get to grips with maths far
quicker, so they enjoy it more. The enjoyment means they're happy to
indulge in it even further. It's easy to see the snowball effect.

When tech produces results with little effort we get that enjoyment
factor--it's not restricted to children :). This draws us to put more
time in, which produces results even faster.

Scaling a technology's use in a large organisation happens faster, with
a larger reach, when people enjoy using it. Rapid adoption follows.

### Scaling Ansible

Scaling across your organisation is going to be context specific, but
there are some fundamentals you can start with.

#### Scaling the Technology

Ensure the hardware you're working with fits the use case.
Documentation which will help ...

- [Red Hat Ansible Tower Requirements](https://docs.ansible.com/ansible-tower/latest/html/quickinstall/prepare.html#prerequisites-and-requirements)
- [Ansible Networking](https://docs.ansible.com/ansible/latest/network/user_guide/faq.html?highlight=memory#how-can-i-improve-performance-for-network-playbooks)

Most important will be the way you manage inventory (how you group
hosts). Spend time thinking about smallest viable reach. If you had to
upgrade the whole stack, which bits could you upgrade independently of
the others?

Ansible is fundamentally an orchestrator -- it doesn't have to be doing
the actual operation. You may already have a tool which Ansible can
instruct, so leverage the fact there's no new learning. You get the
best of all worlds, not least that the high level instruction set is an
easy to read Ansible Playbook.

#### Scale the Human Reach

Scaling any technology in a large company comes down to two fundamental
roots.

1. Education
2. Organisation

Everything else spans from these two starting points.

**Education**

From here two branches emerge -- first, adoption. For a new technology
to take hold it needs to be quick to get up and
running, and easy to learn. When you can solve
a problem in a few minutes it makes it easy to show to others -- and the
adoption spreads.

Second, education needs to be ongoing. And this is where implementing
other tools and practices
around what you do can help. For example, storing your Ansible playbooks
and roles in a source code repository allows others to share and learn.
We once saw a customer put in place a great system for helping their
staff learn Ansible from colleagues. New commits had to be submitted to
a source code repository as a 'pull request', which was reviewed by
more experienced staff. A feedback loop mimicking open source culture
was introduced and reinforced. We've also seen customers push commit
messages to their chat systems. Another great way to encourage sharing.

**Organisation**

"You can have any color as long as it's black". Uniformity is the
friend of scalability, as I'm sure Henry Ford would've told us. People
enjoy being creative, it's pleasing to finish a day's coding and sit
back admiring the job well done. At the same time, to scale we do need
to have some organisation around what we produce.

Security, auditing, and accountability all have a place in a large
company. We need to be able to give the right access to the right
people, as much to prevent accidents as anything. Managing access to
tens of thousands of devices is cumbersome without technological help.

Source code repositories, coding standards, credential management and
access control can all help put organisational structure around Ansible.
Bring together the simplicity of getting the job done, but wrap it in a
security blanket to enable safe, managed, scaling.

### Ansible, scaled

Scaling anything brings about new challenges, and not just around
numbers of hosts. But, a lot of those challenges are met by our
customers on a daily basis. If you have a scaling challenge on your
hands and would like some help, please get in touch. Our
consulting team have worked across every business segment, from the
smallest to the largest companies in the world. We'll have a story or
two you can relate to, and we can help you solve those difficult
problems.
