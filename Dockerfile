FROM python:3.13-slim-bookworm
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

COPY . app/
WORKDIR /app

ENV PYTHONPATH="."

RUN uv sync --frozen

CMD ["uv", "run","src/main.py"]