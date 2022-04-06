FROM python:3.9-slim AS production

# install postgres stuff
RUN apt-get update && \
    apt-get install -y libpq5 libpq-dev gcc

RUN python -m pip install --upgrade pip && pip install poetry

WORKDIR /app
COPY . /app

RUN poetry install --no-dev

FROM production AS development
RUN poetry install

FROM development AS qa
RUN apt-get install make
