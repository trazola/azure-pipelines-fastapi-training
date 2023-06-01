FROM trazola/generic_images:python3.11-slim-bullseye AS base

FROM base AS generate-package-requirements

ARG PRD_REQUIREMENTS="Y"

WORKDIR /tmp

COPY ./pyproject.toml ./poetry.lock* /tmp/

RUN pip install --user poetry \
    && /bin/bash -c "if [[ "${PRD_REQUIREMENTS}" == "Y" ]]; then \
      poetry export -f requirements.txt --output requirements.txt --without-hashes --only main; \
    else \
      poetry export -f requirements.txt --output requirements.txt --without-hashes --with dev; \
    fi"

FROM base AS install-application-packages

USER 0

WORKDIR /app

RUN python -m venv /app/.venv

COPY --from=generate-package-requirements /tmp/requirements.txt .

RUN apt-get update \
    && apt-get -y install libpq-dev gcc

RUN pip install --no-cache-dir -r requirements.txt

FROM base AS runner

WORKDIR /app

COPY --from=install-application-packages /app/.venv .venv

COPY books books
COPY scripts scripts

ENTRYPOINT ["bash", "./scripts/entrypoint.sh"]
