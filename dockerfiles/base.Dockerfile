FROM python:3.11-slim-bullseye

LABEL maintainer="trazola" \
      email="przemyslaw.rozycki1996@gmail.com" \
      description="Dockerfile for Python 3.11.*"

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONPATH="${PYTHONPATH}:/app" \
    PATH="/app/.venv/bin:$PATH:/home/python_user/.local/bin" \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_VIRTUALENVS_IN_PROJECT=false \
    POETRY_NO_INTERACTION=1

RUN apt-get update \
    && pip install --upgrade --no-cache-dir pip \
    && apt-get -y autoremove \
    && useradd -ms /bin/bash python_user \
    && mkdir "app" \
    && chown python_user:python_user /app

USER python_user
