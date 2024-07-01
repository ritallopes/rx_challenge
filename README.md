# RX CHALLENGE

[Documentação](https://ritallopes.bitdocs.ai/share/d/ibbGUscZrsS51cUo)

Este é um projeto que consiste em uma API backend usando FastAPI e um frontend com React, Vite e TypeScript.

## Estrutura do Projeto

O projeto está organizado da seguinte maneira:

- **backend/**: Diretório contendo o código da API backend com FastAPI.
- **frontend/**: Diretório contendo o código do frontend com React, Vite e TypeScript.
- **Dockerfile** e **docker-compose.yml**: Arquivos na raiz do repositório para facilitar a configuração e execução do backend projeto com Docker.
- **example_upload**: Planilha de exemplo para upload.
- **erdiagram.png**: Diagrama entidade-relacionamento do banco de dados.

## Requisitos

Certifique-se de ter o seguinte instalado antes de prosseguir:

- Python >= 3.12
- Node.js >= 20
- npm ou yarn (recomendado)
- Docker e Docker Compose

## Configuração do Backend

### Instalação das Dependências

No diretório `backend/`, execute o seguinte comando para instalar as dependências usando Poetry:

```bash
poetry install
```

### Executando o Backend com Docker

Na raiz do repositório, execute o comando abaixo para subir o backend com Docker:

```bash
docker-compose up --build
```

## Banco de Dados
O banco de dados está hospedado na plataforma Neon e usamos SQLAlchemy e Alembic para integrações e migrações.

## Swagger API
A documentação da API pode ser acessada via Swagger em ˜http://localhost:8000/docs˜.

## Nginx
Configurado como proxy reverso para redirecionar as solicitações para o backend do FastAPI. Ele também lida com CORS, o que é importante para permitir que o frontend interaja com a API sem problemas de política de mesma origem. Além disso, a configuração de logs ajuda na depuração e monitoramento das atividades e erros do servidor.
O servidor escuta na porta 80, que é a porta padrão para HTTP.

## Configuração do Frontend

### Instalação das Dependências

No diretório `frontend/`, execute o seguinte comando para instalar as dependências:

```bash
npm install
# ou
yarn install
```

### Executando o Frontend

Para iniciar o servidor de desenvolvimento do frontend, execute o comando abaixo no diretório `frontend/`:

```bash
npm run dev
# ou
yarn dev
```

## Scripts Disponíveis

### Backend

No `backend/`, os seguintes scripts estão disponíveis via `task`:

- `lint`: Verifica o código com Ruff.
- `format`: Formata o código com Ruff.
- `run`: Executa a aplicação FastAPI localmente.
- `test`: Executa os testes com pytest.
- `cov_test`: Gera o relatório de cobertura de testes.

Para executar qualquer um desses scripts, use o comando:

```bash
poetry run task <gatilho do script>
```

### Frontend

No `frontend/`, os seguintes scripts estão disponíveis:

- `dev`: Inicia o servidor de desenvolvimento.
- `build`: Compila o projeto para produção.
- `lint`: Verifica o código com ESLint.
- `format`: Formata o código com Prettier.
- `preview`: Visualiza a build de produção localmente.
- `storybook`: Inicia o Storybook para componentes UI.
- `build-storybook`: Compila o Storybook para produção.

Para executar qualquer um desses scripts, use o comando:

```bash
npm run <script_name>
# ou
yarn <script_name>
```

## Contato

[LinkedIn](https://www.linkedin.com/in/ritallopes/)
```
