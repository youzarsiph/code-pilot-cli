# code-pilot-cli

[![CI](https://github.com/youzarsiph/code-pilot-cli/actions/workflows/ci.yml/badge.svg)](https://github.com/youzarsiph/code-pilot-cli/actions/workflows/ci.yml)
[![Black](https://github.com/youzarsiph/code-pilot-cli/actions/workflows/black.yml/badge.svg)](https://github.com/youzarsiph/code-pilot-cli/actions/workflows/black.yml)
[![Ruff](https://github.com/youzarsiph/code-pilot-cli/actions/workflows/ruff.yml/badge.svg)](https://github.com/youzarsiph/code-pilot-cli/actions/workflows/ruff.yml)

Your customizable codding assistant in your CLI.

## Demo

<iframe width="560" height="315" src="https://www.youtube.com/embed/VWiPISA9rKo?si=rW6ute2QXwq5KevI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

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

Create a `.env` file and add your `HF_TOKEN`:

```bash
# Create the file
touch .env
```

Open the file in your editor:

```bash
HF_TOKEN = hf_**********************************
```

Or you can export your `HF_TOKEN` as an env variable.

```bash
export HF_TOKEN=hf_**********************************
```

Install poetry:

```bash
pip install poetry
```

Build the project:

```bash
poetry build
poetry install
```

Now you are ready to go.

## Usage

View help:

```bash
code-pilot --help
```

Generate shell commands using natural language:

```bash
code-pilot ai 'list all files in the current directory'
```

Chat with CodePilot:

```bash
code-pilot chat

# Export chat history
code-pilot chat -e chat.json

# Import chat history
code-pilot chat -h chat.json
```

Get code completions from CodePilot:

```bash
code-pilot completions 'fn add(x: i32, y: i32) -> i32 {'
```

Use custom LLMs:

```bash
code-pilot -m 'mistralai/Mistral-Nemo-Instruct-2407' chat
```

## License

Licensed under MIT license.
