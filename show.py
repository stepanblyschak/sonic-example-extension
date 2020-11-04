import click


@click.command()
def example():
    """ This is an example extension command """

    click.echo("Hello from cpu-report example extension")


def register(cli):
    cli.add_command(example)
