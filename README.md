# Vini Data API

Esse projeto foi desenvolvido para atender aos objetivos do Tech Challenge da Fase 1 da Pós Graduação em Machine Learning Engineering, turma 1MLET. Na Fase 1, o foco do projeto é a construção de uma API pública de consulta no site de vitivinicultura da Embrapa, a fim de alimentar uma base de dados que será utilizada para um modelo de Machine Learning.

## Poetry

Este projeto usa Poetry. Poetry é uma ferramenta moderna de gerenciamento de dependências.

Para executar o projeto use este conjunto de comandos:

```bash
poetry install
poetry run python -m vini_data_api
```

Isso iniciará o servidor no host configurado.

Você pode encontrar a documentação do swagger em `/api/docs`.

## Project structure

```bash
$ tree "vini_data_api"
vini_data_api
├── conftest.py  # Fixtures for all tests.
├── db  # module contains db configurations
│   ├── dao  # Data Access Objects. Contains different classes to interact with database.
│   └── models  # Package contains different models for ORMs.
├── __main__.py  # Startup script. Starts uvicorn.
├── services  # Package for different external services such as rabbit or redis etc.
├── settings.py  # Main configuration settings for project.
├── static  # Static content.
├── tests  # Tests for project.
└── web  # Package contains web server. Handlers, startup config.
    ├── api  # Package with all handlers.
    │   └── router.py  # Main router.
    ├── application.py  # FastAPI application configuration.
    └── lifetime.py  # Contains actions to perform on startup and shutdown.
```

## Configuration

Este aplicativo pode ser configurado com variáveis ​​de ambiente.

Você pode criar o arquivo `.env` no diretório raiz e colocar todos
variáveis ​​de ambiente aqui.

Todas as variáveis ​​de ambiente devem começar com o prefixo "VINI_DATA_API_".

Por exemplo, se você vir em "vini_data_api/settings.py" uma variável chamada como
`random_parameter`, você deve fornecer o "VINI_DATA_API_RANDOM_PARAMETER"
variável para configurar o valor. Este comportamento pode ser alterado substituindo a propriedade `env_prefix`
em `vini_data_api.settings.Settings.Config`.

Um exemplo de arquivo .env:
```bash
VINI_DATA_API_RELOAD="True"
VINI_DATA_API_PORT="8000"
VINI_DATA_API_ENVIRONMENT="dev"
```

## Pre-commit

Para instalar o pré-commit basta executar dentro do shell:
```bash
pre-commit install
```

pre-commit é muito útil para verificar seu código antes de publicá-lo.
Você pode ler mais sobre pré-commit aqui: https://pre-commit.com/

## Running tests

Execute o pytest.
```bash
pytest -vv .
```
