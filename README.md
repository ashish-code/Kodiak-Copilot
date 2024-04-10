# Python Template Repo

This repository is a template for how to layout and manage a typical python package repository.

# Style

All python code will follow the [PEP8](https://www.python.org/dev/peps/pep-0008/) guidelines

## Tools

- [black](https://black.readthedocs.io/en/stable/) consistent style
- [mypy](https://pypi.org/project/mypy/) check type hinting
- [ruff](https://beta.ruff.rs/docs/) linter

# Setup Environment

## Requirements

- Python 3.9+ (see pyproject.toml for specific version)
- [poetry](https://python-poetry.org): for dependency management and a development
  and publish workflow.
- [poetry-dynamic-versioning](https://github.com/mtkennerly/poetry-dynamic-versioning): for git tag based versioning
  and release workflow.
- [tox](https://tox.wiki): for ci and local development workflows with automated virtualenv management.
- [awscli](https://pypi.org/project/awscli/): to obtain PyPI CodeArtifact credentials for Bright AI mirror

  - User must be [onboarded](https://backstage.uw2.sandbox.mgmt.bai-infra.net/catalog/default/component/infrastructure/docs/authentication/onboarding/)
    with their AWS Okta access.

## Useful tools:

- [pipx](https://pypa.github.io/pipx/): install tools that should exist outside the project virtualenv.
- [direnv](https://direnv.net/): activates automatically environmental settings that are required for developing.
  See [`.envrc`](.envrc) contents for additional information on how to setup the layout_poetry command.

### Example setup using pipx

```shell
pipx install awscli
pipx install poetry
pipx inject poetry poetry-dynamic-versioning
pipx install tox
```

## poetry workflow

### Install dependencies

```sh
poetry install
```

You will now have a shell in the `./.venv` virtualenv with all the dependencies and the current
project installed in editable mode for development.

## see simple CLI example

```sh
bai-template
```

### run a command in the virtualenv

```sh
poetry run template --help
```

### virtualenv shell

This will activate a shell with the dependencies loaded.

```sh
poetry shell
```

## tox dev workflow

To execute steps defined in [`tox.ini`](tox.ini) for a given python version execute the following:

```sh
tox -e py311-dev
```

This will create automatically a virtualenvironment for the Python version selected (`py310`) and run all the
steps that are marked for the given execution (`dev`).

## running tests

All testing will use [pytest](https://pypi.org/project/pytest/)

```sh
poetry run pytest --mypy --black
```

### Adding tests

Add your TEST PYTHON file in [tests](tests) directory, so you all tests are located together and run `pytest` to complete all tests.
