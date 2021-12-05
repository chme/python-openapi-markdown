
``` openapi
{
    "openapi": "3.0.0",
    "info": {
        "title": "User example service",
        "version": "1.0.0",
        "description": "Example service specification to work with user storage"
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
```
