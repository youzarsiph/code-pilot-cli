# Contributing to CodePilot CLI

We are grateful for your interest in contributing to the **CodePilot CLI** project! Your contributions are vital in helping us maintain and enhance this robust tool for developers. Below are the guidelines to ensure a smooth and productive contribution process.

## Table of Contents

- [Contributing to CodePilot CLI](#contributing-to-codepilot-cli)
  - [Table of Contents](#table-of-contents)
  - [Code of Conduct](#code-of-conduct)
  - [Getting Started](#getting-started)
    - [Fork the Repository](#fork-the-repository)
    - [Set Up Your Local Environment](#set-up-your-local-environment)
  - [Making Changes](#making-changes)
    - [Branching](#branching)
    - [Coding Standards](#coding-standards)
    - [Testing](#testing)
  - [Submitting a Pull Request](#submitting-a-pull-request)
    - [Commit Guidelines](#commit-guidelines)
    - [Opening a Pull Request](#opening-a-pull-request)
  - [Review Process](#review-process)
  - [License](#license)

## Code of Conduct

Conduct is important in any community, and we are no exception. Please read our [Code of Conduct](CODE_OF_CONDUCT.md) and adhere to it when contributing to this project.

## Getting Started

### Fork the Repository

To start contributing, fork the repository to your GitHub account:

1. Navigate to the [CodePilot CLI GitHub page](https://github.com/youzarsiph/code-pilot-cli).
2. Click the **Fork** button in the top-right corner.

### Set Up Your Local Environment

Once you have forked the repository, clone it locally and set up your environment:

```bash
# Clone your forked repository
git clone https://github.com/<your_username>/code-pilot-cli.git

# Navigate to the project directory
cd code-pilot-cli

# Set up a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows
.\venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Making Changes

### Branching

Before making any changes, create a new branch for your work:

```bash
# Create a new branch and switch to it
git checkout -b feature/your-feature-name
```

### Coding Standards

All contributions must adhere to the [PEP 8 style guide for Python code](https://www.python.org/dev/peps/pep-0008/). We also use [Black](https://black.readthedocs.io/en/stable/) for code formatting and [Ruff](https://beta.ruff.rs/) for linting. Ensure your code is formatted and linted before submitting a pull request:

```bash
# Format your code
black .

# Lint your code
ruff .
```

### Testing

We strive for high test coverage. Before submitting your changes, ensure all existing tests pass and add new tests if necessary:

```bash
# Run tests
pytest
```

## Submitting a Pull Request

### Commit Guidelines

Write clear and descriptive commit messages. Your commit message should include:

1. A concise summary of the changes.
2. A detailed description of the changes if necessary.
3. Any relevant references to issues or pull requests.

Example commit message:

```bash
git commit -m "Add feature: Allow users to specify AI model via CLI option

This commit introduces a new option `-m` which allows users to specify the AI model to be used for various commands. The option is added to the `document`, `enhance`, `review`, `scan`, and `test` commands. 

References:
- Closes #42
- Related to #37
"
```

### Opening a Pull Request

1. Push your changes to your forked repository:

    ```bash
    git push origin feature/your-feature-name
    ```

2. Navigate to the [CodePilot CLI GitHub page](https://github.com/youzarsiph/code-pilot-cli).
3. Click the **Compare & pull request** button.
4. Fill out the pull request template with the necessary information.
5. Submit your pull request.

## Review Process

Once your pull request is submitted, it will be reviewed by the maintainers. Please be patient and responsive to any feedback or comments. The review process may involve further changes to ensure code quality and alignment with project goals.

## License

By contributing to **CodePilot CLI**, you agree that your contributions will be licensed under the [MIT License](LICENSE).

Thank you for your contributions to making **CodePilot CLI** an even better tool for developers!
