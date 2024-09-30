""" Command to chat with CodePilot """

import json
from typing import Annotated, Dict, List, Literal, Optional
import typer
from huggingface_hub import InferenceClient
from rich import print
from code_pilot_cli import CHAT_LLM, SYSTEM_MESSAGE, print_highlighted


def chat(
    model: Annotated[
        str,
        typer.Option(
            "--model",
            "-m",
            help="The model to run inference with. Can be a model id hosted on the "
            "Hugging Face Hub, e.g. meta-llama/Meta-Llama-3-8B-Instruct or a URL "
            "to a deployed Inference Endpoint.",
        ),
    ] = CHAT_LLM,
    export: Annotated[
        Optional[typer.FileTextWrite],
        typer.Option(
            "--export",
            "-e",
            help="File to export chat history.",
            encoding="utf-8",
        ),
    ] = None,
    history: Annotated[
        Optional[typer.FileText],
        typer.Option(
            "--history",
            "-h",
            help="File to import previous chat history.",
            encoding="utf-8",
        ),
    ] = None,
) -> None:
    """
    Engage in a chat session with CodePilot.

    Args:
        export (Optional[typer.FileTextWrite]): Optional file to save chat history.
        history (Optional[typer.FileText]): Optional file to load previous chat history.
    """

    client = InferenceClient(model)

    messages: List[Dict[Literal["role", "content"], str]] = [SYSTEM_MESSAGE]

    if history:
        messages = json.load(history)

    print(
        "CodePilot Chat\n"
        "Type [bold red]exit[/bold red] or [bold red]quit[/bold red] to exit\n"
    )
    print_highlighted(
        "Hey there, human! I'm CodePilot here, and I'm here to assist you with all coding-related needs. "
        "Feel free to ask questions, share ideas, or provide your Python code for a run! I'll optimize it "
        "with cutting-edge AI techniques like Overcode Detection and Enhancedsecrets Support, in order to "
        "provide the best services for you, while maintaining confidentiality and security. "
        "Have a great coding journey! 🚀 Let's get started!"
    )

    while True:
        message = typer.prompt(
            typer.style("You", fg=typer.colors.CYAN, bold=True),
            type=str,
        )

        if message.lower() in ("exit", "quit"):
            break

        messages.append({"role": "user", "content": message})

        try:
            response = client.chat_completion(messages=messages, max_tokens=2048)
            llm_message = str(response.choices[0].message.content)

            messages.append({"role": "assistant", "content": llm_message})

            print_highlighted(llm_message)

        except Exception as error:
            print(f"[bold red]Error[/bold red]: {error}")
            break

    export_requested = False

    if not export:
        export_requested: bool = typer.prompt(
            "Do you want to save this chat?",
            type=bool,
            default=False,
            show_default=True,
            confirmation_prompt=True,
        )

        if export_requested:
            file_name: str = typer.prompt(
                "Enter a file name to save the chat history",
                type=str,
                default="chat_history.json",
            )

            # Ensure the file type is JSON
            file_name = (
                file_name if file_name.endswith(".json") else file_name + ".json"
            )

            with open(file_name, "w", encoding="utf-8") as file:
                json.dump(messages, file, indent=2)

    if export:
        json.dump(messages, export, indent=2)
