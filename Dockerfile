ARG IMAGE_NAME="python:3.13-slim-bookworm"

FROM ${IMAGE_NAME}
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

COPY src/ src/
COPY pyproject.toml .
COPY uv.lock .

RUN uv sync --frozen 
RUN rm -rf /var/lib/apt/lists/* /root/.cache

ENV PYTHONPATH="src/"
ENV PYTHONUNBUFFERED 1

RUN adduser --disabled-password --gecos "" appuser
RUN chown -R appuser:appuser /app
USER appuser

CMD ["uv", "run","src/main.py"]
