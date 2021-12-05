# User example service

^v1.0.0^

Example service specification to work with user storage


## Users

User operations


### Get user

``` http
GET /user
```

Method to get the user

???+ abstract "Request"

    _No parameters_


???+ quote "Response"

    `200`
    
    :   successful operation

        === "Schema"

            Content-Types:

            - `application/json`


            ``` json
            {
              "type": "object",
              "properties": {
                "name": {
                  "type": "string",
                  "description": "User name"
                }
              }
            }
            ```





