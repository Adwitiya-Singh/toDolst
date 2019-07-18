
from database_using_sqlalchemy import *
from jsonload import *
import click

@click.group()
def cli():
    """A simple todolist"""


@cli.command()
@click.argument("request", type=click.Path(exists=True, dir_okay=False), default="/Users/as74855/Documents/toDolst/sample_request.json")
@click.argument("template", type=click.Path(exists=True, dir_okay=False), default="/Users/as74855/Documents/toDolst/sample_template.json")
def insert(request: str, template: str):
    data = jsonread(template, request)
    # create_table()
    insert(data)


@cli.command()
@click.argument("key", type=click.INT)
def delete(key: int):
    delete(key)


@cli.command()
def deleteall():
    deleteall()


@cli.command()
def showall_incomplete():
    showall_incomp()


@cli.command()
def showall():
    showall()


@cli.command()
@click.argument("key", type=click.INT)
def mark_complete(key: int):
    mark_complete(key)


if __name__ == "__main__":
    cli()
