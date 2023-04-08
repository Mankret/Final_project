FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY shop/requirements.txt /app/shop/requirements.txt
COPY shop /shop
WORKDIR /shop


RUN apt update && apt install -y libpq-dev gcc

RUN pip install -r /app/shop/requirements.txt

