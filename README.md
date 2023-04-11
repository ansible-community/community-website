(code for Matrix shield, etc, goes here)

This repository contains the assets required to build the Ansible Community website. Welcome!

## Contributing to the website

Please see [CONTRIBUTING](CONTRIBUTING.md)

## Governance

Please see [Governance](CONTRIBUTING.md#Governance)

## Contacting the maintainers

The Website Working group can be found in [TBD](#channel-name-here) on Matrix
or (IRC name here). Alternatively, a GitHub issue is also acceptable for asking
questions.

## Using this repository

This repo contains the source used to generate a static site using [Nikola](https://getnikola.com/).

Configuration file for the site is ``conf.py``.

### Requirements

- Visit [Nikola installation documentation](https://getnikola.com/getting-started.html#install).
- Install `sass` to compile scss files to css.

You can install `sass` as described in the [Sass install docs](https://sass-lang.com/install).
If you are a Fedora user, you can install and use `sassc` as follows:

- `sudo dnf install sassc`
- `sudo ln -s /usr/bin/sassc /usr/bin/sass` (Nikola expects a sass binary.)

### Building and viewing the site

To build the site::

    nikola build

To see it::

    nikola serve -b

To check all available commands::

    nikola help

## Code of Conduct

Please see [CODE OF CONDUCT](CODE_OF_CONDUCT.md)

## License

[![License: CC BY-SA 4.0](https://licensebuttons.net/l/by-sa/4.0/80x15.png)](https://creativecommons.org/licenses/by-sa/4.0/)

## Thank you

Ansible depends on community involvement - thank you for being a part of it!
