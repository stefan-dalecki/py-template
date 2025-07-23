# Foundations: Setting Up Your AI Project

Any Python project, whether it be centered aroundAI, an API, or a library, requires a solid foundation. It's crucial to set yourself up for success and programmatically enforce code quality standards. In a simple sense, this consists of the following files:

* `pyproject.toml`
* `.pre-commit-config.yaml`
* `.github/workflows/ci.yaml`

## Pre-Requisites

The following prerequisites are required to set up your AI project:

* [Python](https://www.python.org/downloads/) version 3.11 or higher
* [uv](https://docs.astral.sh/uv/) package manager

While some might consider `uv` to be supplemental, it is so efficient that it is becoming the defacto Python package manager. Just like how AI is looming, so is `uv`. It's best to these tools sooner rather than later.

### UV

If you know how to use `python` in the command line, you know how to use `uv`. After installation, executing code is as simple as typing `uv run <script.py>`.

```bash
python scripts/my_script.py
# is equivalent to...
uv run scripts/my_script.py
```

## pyproject.toml

This file defines your Python project (hence the name, `py(thon)project.toml`). Among other details, it declares your dependencies, sets up the project structure, and configures the build process. It also includes metadata about the project, such as its name, version, and author information. You might end up rarely touching this file, but it ensures that any other user and developer can easily understand and work with your project. When combined with [uv](https://docs.astral.sh/uv/) and [hatchling](https://hatch.pypa.io/latest/), it provides a seamless and efficient development experience. Consider the example below as a good place to start.

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.hatch.build.targets.wheel]
packages = ["src"]

[project]
name = "py-template"
requires-python = ">=python-version"
version = "0.1.0"
readme = "README.md"
description = ""
authors = [
    { name = "Your Name", email = "your.email@example.com" }
]
classifiers = [
    "Intended Audience :: Developers",
    "Programming Language :: Python :: 3.13",
]

dependencies = ["package>=version"]

[dependency-groups]
dev = ["package1", "package2", "package3"]

```

A `pyproject.toml` file serves as the "truth" as to what packages are needed in what scenarios. When adding a new package or updating dependencies, executing `uv sync` will automatically ensure that your virtual environment and `uv.lock` file reflects your changes.

## .pre-commit-config.yaml

Your code is constantly changing. It would be an impossible task for any developer to manually track changes and ensure their quality. Moreso, instead of waiting for all validations to happen in a serverless pipeline, fast checks can happen locally (and remotely, too). Pre-commit serves as a way to scan your changes before they are committed to the repository. It ensures that your code meets certain standards and quality criteria before it is ultimately merged into the main branch. A simple `pre-commit-config.yaml` file can be customized with [various hooks](https://github.com/pre-commit/pre-commit-hooks) such as linting, formatting, and type checking. Below are a handful of basics to get you started.

```yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v5.0.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-added-large-files
      - id: check-merge-conflict

  - repo: https://github.com/charliermarsh/ruff-pre-commit
    rev: v0.12.4
    hooks:
      - id: ruff
        args: [--fix]

  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.17.0
    hooks:
      - id: mypy
        args: [--ignore-missing-imports]

  - repo: https://github.com/astral-sh/uv-pre-commit
    # uv version.
    rev: 0.7.2
    hooks:
      - id: uv-sync
        entry: uv sync --no-active --check
        stages: [pre-commit]
        files: ^(uv\.lock|pyproject\.toml|uv\.toml)$

```

ATTENTION: These hooks are basic and could arguably be considered an _incomplete_ foundation. You will want to add hooks for your specific project needs. For example, you might want to check your codebase for [spelling errors](https://github.com/codespell-project/codespell), ensure [no breakpoints](https://github.com/pre-commit/pre-commit-hooks?tab=readme-ov-file#debug-statements) are included in production code, and even create your own [custom hooks](https://pre-commit.com/#creating-new-hooks) to enforce client specific coding standards or conventions.

## .github/workflows/ci.yaml

Each commit you make to your feature branch is secure, now it comes time to guarantee that your PR is ready for review. We should integrate pre-commit into our continuous integration (CI) workflow to ensure that all changes meet our quality standards before they are merged into the main branch. This will help us catch any issues early on and prevent them from causing problems later on. With minimal boilerplate, we can run all of our pre-commit checks and all unit tests. If any piece of any step fails, the entire workflow will fail and the PR will be unable to merge. Make sure to review documentation surrounding [GitHub workflows](https://docs.github.com/en/actions/concepts/workflows-and-actions/workflows) as you customize your CI pipeline for your needs.

```yaml
name: CI
on:
  pull_request:
    branches: [main]
    types: [
        edited,
        opened,
        ready_for_review,
        reopened,
        review_requested,
        synchronize,
    ]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.13'

      - name: install uv
        uses: astral-sh/setup-uv@v5
        with:
          python-version: '3.13'
          enable-cache: true
          cache-dependency-glob: "uv.lock"

      - name: Install the project
        run: uv sync --locked --all-extras --dev

      - name: Run pre-commit hooks
        run: |
          uv run pre-commit run --all-files

      - name: Run tests
        run: |
          uv run pytest tests/

```

## Summary

AI is an incredible tool which can help you set safeguards like those that are shown above. Though as you enter uncharted territory, you need to protect yourself and ensure that an AI tool is not leading you down the wrong path. Basic, configurable protections are sometimes all that is necessary to verify that today's changes do not interfere with those from years ago and that they do not introduce new bugs or regressions. The great news is that AI can help you along the way, even help you protect from itself! Let AI be your friend and let it help you write better code.
