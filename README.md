# python_oidc_client

python_oidc_client is a Python package that simplifies OpenID Connect (OIDC) client operations within Flask applications. This package provides functionalities to interact with OIDC providers, making authentication and authorization processes easier.

## Installation

You can install the python_oidc_client package using pip:

```bash
pip install python_oidc_client
```

## Usage

Please check the [examples folder](./examples/)

### Running Tests

To run tests, install the required dependencies and execute:

```bash
pytest
```

## Running Flake8

To check the code for style compliance using Flake8, run:

```bash
flake8
```


## Publish in PyPI

Build the dist folder:
```bash
python setup.py sdist bdist_wheel
```
Upload it:
```bash
twine upload dist/*
```
Insert creds:
```bash
username = __token__
password = pypi-XXXXXX-XXXXXX
```

## Contributing

Bug reports and pull requests are welcome on GitHub at [https://github.com/idpartner-app/python_oidc_client](https://github.com/idpartner-app/python_oidc_client).

## License

The package is available as open source under the terms of the [MIT License](https://opensource.org/licenses/MIT).
```
