FROM python:3.12

WORKDIR /app

COPY backend/pyproject.toml backend/poetry.lock ./

RUN pip install --upgrade pip \
    && pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi

COPY backend/app /app

EXPOSE 8000

CMD ["fastapi","dev", "app/main.py", "--host", "0.0.0.0", "--port", "8000"]
