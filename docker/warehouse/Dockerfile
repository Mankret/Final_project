FROM python:3.10-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH "${PYTHONPATH}:/api:/app/shop:/api/warehouse"

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

COPY ./warehouse /api/warehouse
COPY ./docker/warehouse/entrypoint.sh /api/warehouse/entrypoint.sh
COPY warehouse/requirements.txt /api/warehouse/requirements.txt
WORKDIR /api/warehouse


RUN pip install -r /api/warehouse/requirements.txt

RUN chmod +x /api/warehouse/entrypoint.sh

ENTRYPOINT ["/api/warehouse/entrypoint.sh"]
