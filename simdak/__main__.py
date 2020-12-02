import click
import os
import shutil

from . import paud
from .template import TEMPLATE_FILE

CWD = os.getcwd()


class Setting(object):
    def __init__(self, email: str, password: str, debug: bool = False):
        self.email = email
        self.password = password
        self.debug = debug


@click.group()
@click.option("--email", prompt=True)
@click.password_option()
@click.option("--debug/--no-debug", default=False)
@click.pass_context
def main(ctx: click.Context, email: str, password: str, debug: bool):
    ctx.obj = Setting(email, password)


@click.command("template")
@click.argument("nama", default="Simdak-Paud.xlsx")
def template(nama: str):
    click.echo("Membuat template...")
    shutil.copy(
        TEMPLATE_FILE,
        os.path.join(CWD, nama),
    )


@click.command("export")
@click.pass_context
@click.argument("nama", default="Simdak-Paud.xlsx", required=True)
def exports(ctx, nama: str):
    setting: Setting = ctx.obj
    filepath = os.path.join(CWD, nama)
    paud.exports(filepath, setting.email, setting.password)


@click.command("import")
@click.pass_context
@click.argument("nama", default="Simdak-Paud.xlsx", required=True)
def imports(ctx, nama: str):
    setting: Setting = ctx.obj
    filepath = os.path.join(CWD, nama)
    paud.imports(filepath, setting.email, setting.password)


if __name__ == "__main__":
    main()
