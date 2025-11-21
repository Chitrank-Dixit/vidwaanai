#!/usr/bin/env python3
"""VidwaanAI CLI Entry Point."""

import typer
from pathlib import Path
from rich.console import Console
from rich.table import Table
from typing import Optional
import os
import sys

from src.core.config import settings
from src.core.logger import get_logger
from src.agent.vidwaan_agent import VidwaanAI

# Initialize
app = typer.Typer(
    name="vidwaan",
    help="VidwaanAI - Multilingual AI Agent for Indian Scriptures",
    rich_markup_mode="rich"
)
console = Console()
logger = get_logger(__name__)

# Initialize agent (lazy loading)
agent: Optional[VidwaanAI] = None

def get_agent() -> VidwaanAI:
    """Get or initialize the VidwaanAI agent."""
    global agent
    if agent is None:
        console.print("[bold blue]Initializing VidwaanAI agent...[/bold blue]")
        try:
            agent = VidwaanAI(
                db_url=settings.DATABASE_URL,
                openai_key=settings.OPENAI_API_KEY,
                lmstudio_url=settings.lmstudio_base_url,

            )
        except Exception as e:
            console.print(f"[red]Error initializing agent: {str(e)}[/red]", file=sys.stderr)
            console.print(f"[yellow]Make sure database is running: docker-compose up -d[/yellow]", file=sys.stderr)
            raise typer.Exit(1)
    return agent

@app.command()
def query(
    question: str = typer.Argument(..., help="Question about Indian scriptures"),
    language: Optional[str] = typer.Option("en", "--language", "-l", help="Query language"),
    scripture: Optional[str] = typer.Option(None, "--scripture", "-s", help="Specific scripture"),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Show retrieval details"),
):
    """Query VidwaanAI about Indian scriptures."""
    try:
        agent = get_agent()
        console.print("\n[bold cyan]Processing query...[/bold cyan]")

        response = agent.query(
            question=question,
            language=language,
            scripture_filter=scripture,
            verbose=verbose
        )

        console.print(f"\n[bold green]Answer:[/bold green]\n{response['answer']}")

        if verbose and response.get('retrieved_verses'):
            console.print("\n[bold yellow]Retrieved Verses:[/bold yellow]")
            for i, verse in enumerate(response['retrieved_verses'][:3], 1):
                ref = f"{verse.get('scripture', 'N/A')} {verse.get('chapter', '')}:{verse.get('verse', '')}"
                console.print(f"  {i}. {ref}")
                text_preview = verse.get('translation', verse.get('text', 'N/A'))[:100]
                console.print(f"     {text_preview}...")

        confidence = response.get('confidence', 'N/A')
        console.print(f"\n[dim]Confidence: {confidence}[/dim]")

    except Exception as e:
        console.print(f"[red]Error: {str(e)}[/red]", file=sys.stderr)
        raise typer.Exit(1)

@app.command()
def list_scriptures(
    detailed: bool = typer.Option(False, "--detailed", "-d", help="Show detailed info"),
):
    """List all loaded scriptures."""
    try:
        agent = get_agent()
        scriptures = agent.get_loaded_scriptures()

        if not scriptures:
            console.print("[yellow]No scriptures loaded yet. Load them with: python scripts/load_sample_data.py[/yellow]")
            return

        table = Table(title="[bold]Loaded Scriptures[/bold]")
        table.add_column("Name", style="cyan")
        table.add_column("Language", style="green")
        table.add_column("Status", style="yellow")

        for scripture in scriptures:
            table.add_row(
                scripture.get('name', 'N/A'),
                scripture.get('language', 'N/A'),
                "✓ Indexed"
            )

        console.print(table)

    except Exception as e:
        console.print(f"[red]Error: {str(e)}[/red]", file=sys.stderre)
        raise typer.Exit(1)

# @app.command()
# def settings(
#     action: str = typer.Argument("show", help="show or configure"),
# ):
#     """Manage VidwaanAI settings."""
#     try:
#         if action == "show":
#             console.print("[bold]Current Settings:[/bold]")
#             console.print(f"  LLM Model: {settings.LLM_MODEL}")
#             console.print(f"  Embedding Model: {settings.EMBEDDING_MODEL}")
#             console.print(f"  Retrieval Top-K: {settings.RETRIEVAL_TOP_K}")
#             console.print(f"  Chunk Size: {settings.CHUNK_SIZE}")
#         else:
#             console.print("[yellow]Configuration mode not yet implemented[/yellow]")

#     except Exception as e:
#         console.print(f"[red]Error: {str(e)}[/red]", file=sys.stderr)
#         raise typer.Exit(1)

@app.command()
def system(
    action: str = typer.Argument("status", help="status, health, or info"),
):
    """System administration commands."""
    try:
        if action == "status":
            console.print("[bold]VidwaanAI System Status[/bold]")
            console.print("[green]✓ CLI Ready[/green]")
            console.print("[green]✓ Configuration Loaded[/green]")
            try:
                agent = get_agent()
                console.print("[green]✓ Database Connected[/green]")
            except:
                console.print("[red]✗ Database Not Connected[/red]")
        else:
            console.print(f"[yellow]Action '{action}' not implemented yet[/yellow]")

    except Exception as e:
        console.print(f"[red]Error: {str(e)}[/red]", file=sys.stderr)
        raise typer.Exit(1)

if __name__ == "__main__":
    app()
