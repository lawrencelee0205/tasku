FROM python:3.10-bullseye

ARG ENVIRONMENT
ENV PYTHONUNBUFFERED 1
RUN pip install pipenv
RUN mkdir /code
WORKDIR /code

COPY Pipfile /code/Pipfile
COPY Pipfile.lock /code/Pipfile.lock
RUN pipenv install
COPY . /code/