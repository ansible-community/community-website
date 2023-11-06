[![Discuss at #website:ansible.com on Matrix](https://img.shields.io/matrix/website:ansible.com.svg?server_fqdn=ansible-accounts.ems.host&label=Discuss%20at%20%23website:ansible.com&logo=matrix)](https://matrix.to/#/#website:ansible.com)

This repository contains the assets required to build the Ansible Community website. Welcome!

See the WIP site at [https://ansible-community-website.readthedocs.io/](https://ansible-community-website.readthedocs.io/)

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

### Using nox

This project includes a ``nox`` configuration to automate and simplify the build.

Install ``nox``.

    # Install nox with pip
    python3 -m pip install nox

    # Install nox on MacOS
    brew install nox

Run ``nox -s build`` to build the website locally.
To see other available sessions, run ``nox --list``.

### Running nikola directly

The website is built with nikola.
If you prefer using ``nikola`` commands directly, instead of using ``nox``, you can.

#### Setting things up

We recommend that you use a Python virtual environment.

    # Create a virtual environment named "venv" in your current directory.
    python3 -m venv venv

    # Activate the virtual environment.
    source venv/bin/activate

    # Install the required packages.
    python -m pip install --upgrade -r ./requirements.in -c ./requirements.txt

#### Building and viewing the site

The Ansible community website is built with [Nikola](https://getnikola.com/).

    # Build the site with Nikola.
    nikola build

    # View the site in your browser.
    nikola serve -b

    # List available commands.
    nikola help

> Check the [Nikola handbook](https://getnikola.com/handbook.html) for more details.

> Nikola configuration for the website is in ``conf.py``.

## Checking your changes

This project includes some tests and checks that run against pull requests.
You can also run these checks before you commit changes.

    # Install nox if required.
    python -m pip install --upgrade nox

    # View available nox sessions.
    nox --list

### Linting and formatting templates

This project includes a linter and formatter to guard against unintended errors and to ensure high quality templates.
If you modify the templates you should lint and format prior to commit.

    # Check templates for issues.
    nox -s lint

    # Check templates and ignore rules.
    nox -s lint -- --ignore=H006,H013,T002,T003,T028

    # Check changes before formatting.
    nox -s format -- --check

    # Format templates.
    nox -s format

Default configuration for the linter and formatter is in the ``[tool.djlint]`` section of ``pyproject.toml``.
For more information about configuration options, see:

- [Linter](https://www.djlint.com/docs/linter/)
- [Formatter](https://www.djlint.com/docs/formatter/)

### Spelling check

    # Use the default session to check all templates, pages, and data for spelling errors.
    nox -s spelling

    # Check a specific blog post for spelling errors.
    nox -s spelling -- ./posts/2023/02/24/2023-02-24-ansible_community_strategy_2023.md

    # Automatically correct any spelling errors in a blog post.
    nox -s spelling -- ./posts/2023/02/24/2023-02-24-ansible_community_strategy_2023.md -w

## Code of Conduct

The Ansible community team values diverse opinions and is committed to an inclusive
Please review and abide by our [CODE OF CONDUCT](CODE_OF_CONDUCT.md).

## License

[![License: CC BY-SA 4.0](https://licensebuttons.net/l/by-sa/4.0/80x15.png)](https://creativecommons.org/licenses/by-sa/4.0/)

## Thank you

Ansible depends on community involvement - thank you for being a part of it!
