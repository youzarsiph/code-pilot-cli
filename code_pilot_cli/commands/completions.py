""" Command to generate shell commands """

from typing import Annotated
import typer
from huggingface_hub import InferenceClient
from rich import print
from code_pilot_cli import COMPLETION_LLM, print_highlighted


def completions(
    code: Annotated[str, typer.Argument(help="Code snippet to complete.")],
    model: Annotated[
        str,
        typer.Option(
            "--model",
            "-m",
            help="The model to run inference with. Can be a model id hosted on the "
            "Hugging Face Hub, e.g. meta-llama/Meta-Llama-3-8B-Instruct or a URL "
            "to a deployed Inference Endpoint.",
        ),
    ] = COMPLETION_LLM,
) -> None:
    """
    Generate code completions based on the provided code snippet.

    Args:
        code (str): The code to complete.
    """

    client = InferenceClient(COMPLETION_LLM)

    try:
        generated_code = client.text_generation(code, max_new_tokens=1024)

        print("[bold green]CodePilot[/bold green]:")
        print_highlighted(code + generated_code)

    except Exception as error:
        print(f"[bold red]Error[/bold red]: {error}")
