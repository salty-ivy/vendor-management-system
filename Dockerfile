FROM python:3.11 as development_build

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

RUN mkdir /code

WORKDIR /code

RUN pip install --upgrade pip

COPY docker-requirements.txt /code/

RUN pip install -r docker-requirements.txt

COPY . /code/

EXPOSE 8000
