FROM python:3.9-slim AS compile-image

RUN apt-get update; \
    apt-get install -y --no-install-recommends build-essential gcc

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt

FROM python:3.9-slim AS build-image
COPY --from=compile-image /opt/venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

COPY ./src module/src
COPY ./scripts module/scripts
COPY ./configs module/configs
COPY pyproject.toml module/pyproject.toml

WORKDIR module
