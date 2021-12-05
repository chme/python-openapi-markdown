import markdown


def test_extension_oas3_json():
    # arrange
    configs = {}
    md = markdown.Markdown(
        extensions=[
            "markdown.extensions.fenced_code",
            "admonition",
            "pymdownx.snippets",
            "openapi_markdown.markdown_extension",
        ],
        extension_configs=configs,
    )

    text = '''
    ``` openapi
    {
        "openapi": "3.0.0",
        "info": {
            "title": "User example service",
            "version": "1.0.0",
            "description": "Example service specification"
        },
        "servers": [
            {
                "url": "https://users.app",
                "description": "production"
            }
        ],
        "tags": [
            {
                "name": "Users",
                "description": "User operations"
            }
        ],
        "paths": {
            "/user": {
                "get": {
                    "summary": "Get user",
                    "description": "Method to get the user",
                    "operationId": "GetUser",
                    "tags": [
                        "Users"
                    ],
                    "responses": {
                        "200": {
                            "description": "successful operation",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "type": "object",
                                        "properties": {
                                            "name": {
                                                "type": "string",
                                                "description": "User name"
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    ```'''

    # act
    actual = md.convert(text)

    # assert
    assert len(actual) > 0
