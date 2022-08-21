# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN mkdir /django-base
WORKDIR /django-base
ADD . /django-base/

COPY requirements.txt /django-base/
RUN pip install -r requirements.txt 

COPY ./compose/web/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start
