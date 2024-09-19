# code-pilot-cli

[![CI](https://github.com/youzarsiph/code-pilot-cli/actions/workflows/ci.yml/badge.svg)](https://github.com/youzarsiph/code-pilot-cli/actions/workflows/ci.yml)
[![Black](https://github.com/youzarsiph/code-pilot-cli/actions/workflows/black.yml/badge.svg)](https://github.com/youzarsiph/code-pilot-cli/actions/workflows/black.yml)
[![Ruff](https://github.com/youzarsiph/code-pilot-cli/actions/workflows/ruff.yml/badge.svg)](https://github.com/youzarsiph/code-pilot-cli/actions/workflows/ruff.yml)

Your customizable codding assistant in your CLI.

## Get started

Clone the repo:

```bash
git clone https://github.com/youzarsiph/code-pilot-cli
cd code-pilot-cli
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Overview

View help:

```bash
python app.py --help
```

Generate shell commands using natural language:

```bash
python app.py ai 'list all files in the current directory'
```

Chat with CodePilot:

```bash
python app.py chat

# Export chat history
python app.py chat -e chat.json

# Import chat history
python app.py chat -h chat.json
```

Get code completions from CodePilot:

```bash
python app.py completions 'fn add(x: i32, y: i32) -> i32{'
```

Use custom LLMs:

```bash
python app.py -m 'mistralai/Mistral-Nemo-Instruct-2407' chat
```

## License

Licensed under MIT license.
