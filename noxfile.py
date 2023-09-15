import nox

@nox.session
def spelling(session: nox.Session):
    """
    Spell check the website and blog
    """
    session.install("codespell", "tomli")
    session.run("codespell",
        *session.posargs,
        "--toml", f"pyproject.toml"
        )

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
