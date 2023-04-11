FROM python:3.10-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH "${PYTHONPATH}:/app"

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

COPY ./docker/shop/entrypoint.sh /app/shop/entrypoint.sh
COPY shop/requirements.txt /app/shop/requirements.txt
COPY shop /app/shop
WORKDIR /app/shop


RUN pip install -r /app/shop/requirements.txt

RUN chmod +x /app/shop/entrypoint.sh

ENTRYPOINT ["/app/shop/entrypoint.sh"]
