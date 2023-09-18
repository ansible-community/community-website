import os
from pathlib import Path

import nox


@nox.session
def lint(session: nox.Session):
    """
    Check the website templates for issues.
    """
    session.install("djlint")
    session.run("djlint",
        "-",
        "--lint",
        *session.posargs,
        )

@nox.session
def format(session: nox.Session):
    """
    Format the website templates.
    """
    session.install("djlint")
    session.run("djlint",
        "-",
        "--reformat",
        *session.posargs,
        )
