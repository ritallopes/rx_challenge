# Usar uma imagem base com Python
FROM python:3.12

# Definir o diretório de trabalho
WORKDIR /app

# Copiar o arquivo de dependências
COPY pyproject.toml poetry.lock ./

# Instalar as dependências
RUN pip install --upgrade pip \
    && pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi

# Copiar o restante do código da aplicação
COPY . .

# Expôr a porta que o Uvicorn usará
EXPOSE 8000

# Comando para iniciar a aplicação FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
