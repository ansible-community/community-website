[![Discuss at #website:ansible.com on Matrix](https://img.shields.io/matrix/website:ansible.com.svg?server_fqdn=ansible-accounts.ems.host&label=Discuss%20at%20%23website:ansible.com&logo=matrix)](https://matrix.to/#/#website:ansible.com)

This repository contains the assets required to build the Ansible Community website. Welcome!

See the WIP site at https://ansible-community.github.io/community-website/

## Contributing to the website

Please see [CONTRIBUTING](CONTRIBUTING.md)

## Governance

Please see [Governance](CONTRIBUTING.md#Governance)

## Contacting the maintainers

The Website Working group can be found in [Ansible Website WG](https://matrix.to/#/#website:ansible.com) on Matrix
or ``#ansible-website`` on IRC. Alternatively, a GitHub issue is also acceptable for asking
questions.

## Building the website locally

The Ansible community website is static HTML generated from this repository.
You can build the website locally if you want to evaluate changes or experiment.

### Setting things up

We recommend that you use a Python virtual environment.

    # Create a virtual environment named "venv" in your current directory.
    python3 -m venv venv

    # Activate the virtual environment.
    source venv/bin/activate

    # Install the required packages.
    python -m pip install --upgrade -r ./requirements.txt

### Building and viewing the site

The Ansible community website is built with [Nikola](https://getnikola.com/).

    # Build the site with Nikola.
    nikola build

    # View the site in your browser.
    nikola serve -b

    # List available commands.
    nikola help

> Check the [Nikola handbook](https://getnikola.com/handbook.html) for more details.

> Nikola configuration for the website is in ``conf.py``.

## Code of Conduct

The Ansible community team values diverse opinions and is committed to an inclusive
Please review and abide by our [CODE OF CONDUCT](CODE_OF_CONDUCT.md).

## License

[![License: CC BY-SA 4.0](https://licensebuttons.net/l/by-sa/4.0/80x15.png)](https://creativecommons.org/licenses/by-sa/4.0/)

## Thank you

Ansible depends on community involvement - thank you for being a part of it!
