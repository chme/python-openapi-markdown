from openapi_markdown.cli import main


def test_main():
    assert main([]) == 0
