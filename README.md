# iReporter
[![Build Status](https://travis-ci.org/astonetuhame/ireporter.svg?branch=develop-API)](https://travis-ci.org/astonetuhame/ireporter)
[![Coverage Status](https://coveralls.io/repos/github/astonetuhame/ireporter/badge.svg?branch=develop-API)](https://coveralls.io/github/astonetuhame/ireporter?branch=develop-API)


## About
iReporter enables any/every citizen to bring any form of corruption to the notice of appropriate authorities and the general public.
This project is part of the [Andela Fellowship](https://andela.com/) Bootcamp 15 Challenge.

 
#### Development setup
- Create a virtual environment and activate it
    ```bash
     virtualenv venv
     source /venv/bin/activate
    ```
- Install dependencies 
    ```bash
    pip3 install -r requirements.txt
    ```
- Run the application
    ```bash
    cd ireporter
    python app.py
    ```
- Now you can access the system api Endpoints:

| End Point                                           | Verb |Use                                       |
| ----------------------------------------------------|------|------------------------------------------|
|`/api/v1/red-flags/`                                 |POST  |Creating a red-flag                       |
|`/api/v1/red-flags/`                                 |GET   |Gets a list of all red-flags              |
|`/api/v1/red-flags/<int:red-flag-id>`                |GET   |Get a specific red-flag  					|
|`/api/v1/red-flags/<int:red-flag-id>/location`       |PATCH |Edit the location of a red-flag           |
|`/api/v1/red-flags/<int:red-flag-id>/comment`        |PATCH |Edit the comment of a red-flag            |
|`/api/v1/red-flags/<int:red-flag-id>`                |DELETE|Delete a red-flag                         |

## Running the tests

- To run the tests, run the following commands

```bash
pytest --cov .
```

## Built With

* [Flask](http://flask.pocoo.org/docs/1.0/) - The web framework used
* [Python](https://www.python.org/) - Framework language

## Acknowledgments

* Andela Software Development Community
