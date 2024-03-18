import click

from click import Context

class Engine:

    @click.group()
    def main() -> None:
        ...