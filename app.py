""" CodePilot CLI """

from typing import Dict, List, Literal
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
)
@click.pass_context
def cli(ctx: click.Context, model: str) -> None:
    """CodePilot CLI"""

    # Load secrets
    load_dotenv(override=True)

    # Add model to context
    ctx.obj = model


@cli.command()
@click.argument("prompt", type=click.STRING)
@click.pass_obj
def ai(model: str, prompt: str) -> None:
    """Natural language interactions"""

    client = InferenceClient(model)

    try:
        response = client.text_generation(prompt, max_new_tokens=128)
        click.echo(response)

    except Exception as error:
        click.secho("Error: ", err=True, fg="red", nl=False)
        click.echo(f"{error}", err=True)


@cli.command()
@click.option("-sm", "--sys-message", type=click.STRING)
@click.pass_obj
def chat(model: str, sys_message: str | None = None) -> None:
    """Start a chat session"""

    # HF Inference client
    client = InferenceClient(model)

    # Chat history
    messages: List[Dict[Literal["role", "content"] | str, str]] = []

    # Add system message if provided
    if sys_message:
        messages.append({"role": "system", "content": sys_message})

    # Chat loop
    while True:
        # User message
        click.secho("You:", fg="green", nl=False)
        message = click.prompt("", type=click.STRING, prompt_suffix="")

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

            click.secho("CodePilot: ", fg="green", nl=False)
            click.echo_via_pager(llm_message)

        except Exception as error:
            click.secho("Error: ", err=True, fg="red", nl=False)
            click.echo(f"{error}", err=True)

            # Exit chat loop
            break


@cli.command()
@click.argument("code", type=click.STRING)
@click.pass_obj
def complete(model: str, code: str) -> None:
    """Code completions with CodePilot"""

    client = InferenceClient(model)

    try:
        response = client.text_generation(code, max_new_tokens=128)
        click.echo(response)

    except Exception as error:
        click.secho("Error: ", err=True, fg="red", nl=False)
        click.echo(f"{error}", err=True)


if __name__ == "__main__":
    cli()
