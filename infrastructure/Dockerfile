FROM python:3.11-alpine as builder-base
RUN apk update && apk add  gcc libffi-dev g++ py-pip --no-cache cargo gettext
WORKDIR /app
COPY pyproject.toml poetry.lock ./
RUN pip install --upgrade pip && pip install "poetry==1.5.1" && poetry config virtualenvs.create false && poetry install --no-cache --without linters
COPY ./app ./app
