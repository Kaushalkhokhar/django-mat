# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /django-base
COPY requirements.txt /django-base/

RUN pip install -r requirements.txt 

COPY . /django-base/
