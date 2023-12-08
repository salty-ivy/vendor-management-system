FROM python:3.11

ENV PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PYTHONUNBUFFERED=1 \
    PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    POETRY_VERSION=1.7.1


# install poetry to manage python dependencies
RUN curl -sSL https://install.python-poetry.org | python3 -

ENV PATH="${PATH}:/root/.local/bin"

RUN poetry config virtualenvs.create true
# install python dependencies
COPY ./pyproject.toml .

COPY ./poetry.lock .

RUN /root/.local/bin/poetry install --no-interaction --no-ansi

# copy project
COPY . .

# run at port 8000
EXPOSE 8000

CMD ["poetry", "run", "python", "src/manage.py", "runserver"]
