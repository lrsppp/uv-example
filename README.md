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

- FastAPI.

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

uv run
```

### Tools

Tools are installed to `~/.local/bin/..` using `uv tool install toolname`, e.g.

```
uv tool install ruff

# run ruff formatter
uvx ruff format .
```

Notable tools:

* `ruff`
* `isort`
* `pre-commit`
    * [`detect-secrets`](https://github.com/Yelp/detect-secrets)

### Scripts

Define dependencies for scripts, for example:

```
# example.py
import numpy as np
print(np.add(5, [4, 3]))
```

Now `uv add --script example.py 'numpy'`:

```
# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "numpy",
# ]
# ///
import numpy as np

print(np.add(5, [4, 3]))
```

Run via `uv run example.py`. The dependency will be downloaded but not added to `.venv` or `pyproject.toml`.

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

- [Integration](https://docs.astral.sh/uv/guides/integration/)

## Docker

See `Dockerfile` and `docker-compose.yml`. Essentially, `uv` is copied from a second image (`ghcr.io/astral-sh/uv:latest`) to the base image.

```
# Dockerfile
FROM python:3.12-slim-bookworm
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
...
```

## Github Actions

See `.github/workflows`. Use `uv` action `astral-sh/setup-uv@v5` ([Link](https://github.com/astral-sh/setup-uv/tree/v5/)).
