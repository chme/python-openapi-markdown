"""
Module that contains the command line app.

Why does this file exist, and why not put this in __main__?

  You might be tempted to import things from __main__ later, but that will
  cause problems: the code will get executed twice:

  - When you run `python -mopenapi_markdown` python will execute
    ``__main__.py`` as a script. That means there won't be any
    ``openapi_markdown.__main__`` in ``sys.modules``.
  - When you import __main__ it will get executed again (as a module) because
    there's no ``openapi_markdown.__main__`` in ``sys.modules``.

  Also see (1) from http://click.pocoo.org/5/setuptools/#setuptools-integration
"""
import click

from openapi_markdown.renderer import render


@click.command()
@click.option(
    "--input",
    prompt="Path to OpenAPI specification file",
    help="OpenAPI specification file.",
)
@click.option(
    "--output", default="api.md", prompt="Path to output file", help="Output file."
)
def main(input, output):
    # result = render(url="data/openapi.json")
    result = render(url=input)
    with open(output, "w") as f:
        f.write(result)

    return 0
