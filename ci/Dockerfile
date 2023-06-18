FROM python:3.11.4-slim

RUN apt update && apt -y install \
    bash \
    binutils \
    coreutils \
    curl \
    postgresql-client \
    nano \
    vim \
    procps \
    && apt clean

RUN mkdir -p /app/src
RUN mkdir -p /app/logs
COPY ./src /app/src
WORKDIR /app/src

RUN pip install --no-cache poetry==1.5.1
RUN poetry config virtualenvs.create false && poetry install

ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH="${PYTHONPATH}:/app/src"

ENTRYPOINT ["./entrypoint.sh"]
