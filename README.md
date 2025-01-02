# uv example

Playground for [uv](https://docs.astral.sh/uv/).

## Initalizate project

```
uv python pin 3.13      # creates .python-version file
uv init
uv venv                 # creates .venv 
rm hello.py
mkdir src tests
uv add pytest
```

+ FastAPI.

## Development

For simplicity, add to `.vscode/settings.json` or install application as package into `.venv` using `uv pip install -e .`. In later stages, the `$PYTHONPATH` will be set to `src/` to allow absolute imports.

```
{
    ...
    "terminal.integrated.env.linux": {
        "PYTHONPATH": "${workspaceFolder}/src"
    }
}
```

# Integrations 

* [Integration](https://docs.astral.sh/uv/guides/integration/)

## Docker

```
# Dockerfile
FROM python:3.12-slim-bookworm
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
```
