from openapi_markdown.cli import main

from click.testing import CliRunner


def test_cli():
    runner = CliRunner()
    result = runner.invoke(
        main, ["--input", "data/openapi.json", "--output", "data/openapi.md"]
    )
    assert result.exit_code == 0
