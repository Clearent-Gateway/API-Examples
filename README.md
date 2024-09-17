# Clearent API Examples for Python

To being, install the `requests` package.

```
python -m pip install requests
```

Or if you're using [uv](https://docs.astral.sh/uv/) you can install from the requirements defined in `pyproject.toml`.

```
uv sync
```

Examples are provided for the following transaction types:

* sale
* authorization
* capture
* forcedsale
* refund
* void

Run the demo by passing your Clearent API key and the type of transaction.

```
python demo.py -k notarealkey123 authorization
```