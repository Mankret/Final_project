FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY warehouse/requirements.txt /api/warehouse/requirements.txt
COPY warehouse /warehouse
WORKDIR /warehouse


RUN apt update && apt install -y libpq-dev gcc

RUN pip install -r /api/warehouse/requirements.txt

