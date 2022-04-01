FROM python:3.9-slim AS production

# install postgres stuff
RUN apt-get update && \
    apt-get install -y libpq5 libpq-dev gcc

WORKDIR /app
COPY . /app

RUN python -m pip install --upgrade pip && pip install poetry 
RUN poetry install --no-dev

FROM production AS development
RUN poetry install

FROM development AS qa
CMD make check_all
