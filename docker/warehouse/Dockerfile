FROM python:3.10-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

COPY ./docker/warehouse/entrypoint.sh /api/warehouse/entrypoint.sh
COPY warehouse/requirements.txt /api/warehouse/requirements.txt
COPY warehouse /warehouse
WORKDIR /warehouse


RUN pip install -r /api/warehouse/requirements.txt

RUN chmod +x /api/warehouse/entrypoint.sh

ENTRYPOINT ["/api/warehouse/entrypoint.sh"]
