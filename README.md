# Foundations: Setting Up Your AI Project

While AI is certainly empowering, it ultimately needs personal regulation. Is my model misleading me? Is it _almost_ correct? How do I know when my LLM is helping or hurting me? An attentive programmer should be able to identify when their AI model is not performing as expected and take corrective action. However, this expectation is exceedingly difficult to meet especially when AI is _teaching_ you something or providing insight into an _unknown_ domain.

Regardless of what AI is doing for us, we need guardrails. Below are some basic files that provide minimal and necessary code quality in your repo.

- [ ] `pyproject.toml`: a configuration file for Python projects
- [ ] `main.py`: root file for your code
- [ ] `pre-commit-config.yaml`: CI hooks for safely integrating code into your codebase
- [ ] `./.github/workflows/ci.yaml`: GitHub Actions workflow for continuous integration
