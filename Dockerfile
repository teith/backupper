# syntax=docker/dockerfile:1
FROM python:3.11
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY pyproject.toml /code/
COPY poetry.lock /code/
RUN apt-get update && apt-get install p7zip-full -y && pip install poetry && poetry config virtualenvs.create false && poetry install
COPY src/ /code/