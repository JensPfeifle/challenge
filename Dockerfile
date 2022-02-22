# Base image
FROM python:3.10-slim-bullseye as base

ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_VERSION=1.1.13

RUN pip install "poetry==$POETRY_VERSION"

WORKDIR /app
COPY poetry.lock pyproject.toml /app/

# Development image
FROM base as dev

RUN poetry install --no-interaction --no-ansi

# Usually I would not copy, but instead mount the project into the container.
COPY . . 

CMD ["tail", "-f", "/dev/null"]

# Production image
FROM base as prod

COPY . .

RUN poetry install --no-dev --no-interaction --no-ansi

CMD ["poetry", "run", "python", "-m", "src"]
