FROM python:3.9.7-slim

ENV PYTHONUNBUFFERED=1 COLUMNS=200

ADD ./src/requirements/prod.txt \
    ./src/requirements/dev.txt /src/

RUN apt update -y && apt install -y gettext \
    && pip install --upgrade pip wheel setuptools \
    # Add project dependencies
    && pip install \
    --no-cache-dir -Ur /src/prod.txt \
    --no-cache-dir -Ur /src/dev.txt \
    # Remove build dependencies
    && apt clean

COPY ./src /src

WORKDIR /src
CMD ["./entrypoint.sh"]
