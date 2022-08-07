FROM python:3.10

RUN pip install poetry

COPY . /app
WORKDIR /app

RUN poetry install

ENTRYPOINT [\
    "poetry", "run", "uvicorn", \
    "--port", "8080", \
    "--host", "0.0.0.0", \
    "sztrittyu_web.app:app"]
