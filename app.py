""" CodePilot CLI """

import json
from typing import Dict, List, Literal, Optional
import click
from dotenv import load_dotenv
from huggingface_hub import InferenceClient


@click.group()
@click.option(
    "-m",
    "--model",
    type=click.STRING,
    show_default=True,
    default="HuggingFaceH4/starchat2-15b-v0.1",
    help="Customize the LLM.",
)
@click.pass_context
def cli(ctx: click.Context, model: str) -> None:
    """
    CodePilot CLI

    Your customizable codding assistant in your CLI.
    """

    # Load secrets
    load_dotenv(override=True)

    # Add model to context
    ctx.obj = model


@cli.command()
@click.argument("prompt", type=click.STRING)
@click.pass_obj
def ai(model: str, prompt: str) -> None:
    """
    Generate shell commands using natural language

    \b
    Example:
    ```bash
    code-pilot ai 'list the top 10 process in CPU usage'
    ```
    """

    # HF Inference client
    client = InferenceClient(model)

    try:
        response = client.chat_completion(
            messages=[
                {
                    "role": "system",
                    "content": "You are CodePilot, an advanced AI coding assistant. "
                    "Your task is to assist users with coding queries by providing clear explanations, code snippets, and debugging help. "
                    "Always specify the programming language when applicable and ensure your responses are detailed yet concise. "
                    "Keep interactions friendly and supportive.",
                },
                {"role": "user", "content": prompt},
            ],
            max_tokens=512,
        )

        click.echo(
            f"{click.style('CodePilot', fg='green', bold=True)}: {response.choices[0].message.content}"
        )

    except Exception as error:
        click.echo(
            f"{click.style('Error', fg='red', bold=True, underline=True)}: {error}",
            err=True,
        )


@cli.command()
@click.option(
    "-sm",
    "--sys-message",
    type=click.STRING,
    help="Customize system message.",
)
@click.option(
    "-e",
    "--export",
    type=click.File(mode="w", encoding="utf-8"),
    help="File name to export chat history (JSON).",
)
@click.option(
    "-h",
    "--history",
    type=click.File(encoding="utf-8"),
    help="File name to import chat history (JSON).",
)
@click.pass_obj
def chat(
    model: str,
    sys_message: Optional[str] = None,
    export: Optional[click.File] = None,
    history: Optional[click.File] = None,
) -> None:
    """
    Chat with CodePilot

    \b
    Examples:
    ```bash
    code-pilot chat
    # Customize system message
    code-pilot chat -sm "You are a helpful coding assistant"
    # Export chat history
    code-pilot chat -e chat_history.json
    # Import chat history
    code-pilot chat -h chat_history.json
    ```
    """

    # HF Inference client
    client = InferenceClient(model)

    # Chat history
    messages: List[Dict[Literal["role", "content"], str]] = []

    # Import chat history if provided
    if history:
        messages = json.load(history)

    # Add system message if provided
    if sys_message and not history:
        messages.append({"role": "system", "content": sys_message})

    # Help message
    click.echo(
        f"{click.style('CodePilot Chat', fg='green', bold=True)}\n"
        f"Type {click.style('exit', fg='red', bold=True)} or {click.style('quit', fg='red', bold=True)} to exit.\n"
    )

    # Chat loop
    while True:
        # User message
        message = click.prompt(
            click.style("You", fg="green", bold=True),
            type=click.STRING,
        )

        if message in ("exit", "quit"):
            break

        # Add to chat history
        messages.append({"role": "user", "content": message})

        try:
            # LLM message
            response = client.chat_completion(messages=messages, max_tokens=1024)
            llm_message = str(response.choices[0].message.content)

            # Add to chat history
            messages.append({"role": "assistant", "content": llm_message})

            click.echo(
                f"{click.style('CodePilot', fg='green', bold=True)}: {llm_message}\n"
            )

        except Exception as error:
            click.echo(
                f"{click.style('Error', fg='red', bold=True, underline=True)}: {error}",
                err=True,
            )

            # Exit chat loop
            break

    # Export chat history
    if export:
        json.dump(messages, export)


@cli.command()
@click.argument("code", type=click.STRING)
@click.pass_obj
def completions(model: str, code: str) -> None:
    """
    Get code completions from CodePilot

    \b
    Example:
    ```bash
    code-pilot completions 'fn read_file(path: PathBuf) -> Result<String, Error> {'
    ```
    """

    # HF Inference client
    client = InferenceClient(model)

    try:
        generated_code = client.text_generation(code, max_new_tokens=128)

        click.echo(
            f"{click.style('CodePilot', fg='green', bold=True)}:\n{code + generated_code}"
        )

    except Exception as error:
        click.echo(
            f"{click.style('Error', fg='red', bold=True, underline=True)}: {error}",
            err=True,
        )


if __name__ == "__main__":
    cli(max_content_width=120)
