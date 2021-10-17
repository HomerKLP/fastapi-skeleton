from invoke import task


@task
def outdated(c):
    c.run("pip list --outdated --format=columns", pty=True)


@task
def test(c):
    c.run("pytest -v --cov && flake8 && black . --check", pty=True)


@task
def black(c):
    c.run("black .", pty=True)
