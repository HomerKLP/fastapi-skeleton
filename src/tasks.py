from invoke import task


@task
def outdated(c):
    c.run("pip list --outdated --format=columns", pty=True)


@task
def test(c):
    c.run("pytest -v --cov && flake8", pty=True)
