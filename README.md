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


## `uv` cheat sheet

```
uv venv
uv init 
uv sync

uvx

uv add
uv remove

uv pip compile pyproject.toml -o requirements.txt
uv lock

uv pip freeze
```



## Development

For simplicity, set `PYTHONPATH` variable in `.vscode/settings.json` or install application as package into `.venv` using `uv pip install -e .`. 

```
{
    ...
    "terminal.integrated.env.linux": {
        "PYTHONPATH": "${workspaceFolder}/src"
    }
}
```

Alternatively, set `PYTHONPATH` in `.env` with absolute path:

```
# .env
PYTHONPATH=${PYTHONPATH}:/home/user/repos/uv-example/src
```

If scripts are started using VS Code launch, modify `.vscode/launch.json`:

```
    ...
    "env": {
        "PYTHONPATH": "${workspaceFolder}/src"
    }
    ...
```

# Integrations 

* [Integration](https://docs.astral.sh/uv/guides/integration/)

## Docker

```
# Dockerfile
FROM python:3.12-slim-bookworm
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
```

# TODO

- GitHub Actions with `uv`