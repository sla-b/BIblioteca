# Biblioteca API

API REST desenvolvida em Python para gerenciamento de uma biblioteca, utilizando FastAPI, PostgreSQL, SQLAlchemy e Pydantic.

## Tecnologias utilizadas

* **Python** — Linguagem utilizada no desenvolvimento.
* **FastAPI** — Framework utilizado para construção da API REST.
* **PostgreSQL** — Banco de dados utilizado para persistência das informações.
* **SQLAlchemy** — ORM utilizado para comunicação com o banco de dados.
* **Pydantic** — Validação e estruturação dos dados.
* **Uvicorn** — Servidor ASGI utilizado para executar a aplicação FastAPI.

## Instalação

Clone o repositório:

```bash
git clone https://github.com/sla-b/BIblioteca.git
cd BIblioteca
```

Crie um ambiente virtual:

```bash
python -m venv venv
```

Ative o ambiente virtual no Windows:

```bash
venv\Scripts\activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

## Executando a aplicação

Após instalar as dependências e configurar o banco de dados PostgreSQL, execute a aplicação utilizando o **Uvicorn**:

```bash
uvicorn main:app --reload
```

O comando acima inicia o servidor da aplicação FastAPI.

Após executar o comando, a API estará disponível em:

```text
http://127.0.0.1:8000
```

### Acessando os endpoints

Com o servidor Uvicorn em execução, os endpoints da API podem ser acessados através das rotas definidas na aplicação.

Além disso, o FastAPI disponibiliza uma documentação interativa automaticamente.

**Swagger UI:**

```text
http://127.0.0.1:8000/docs
```

**ReDoc:**

```text
http://127.0.0.1:8000/redoc
```

Através do **Swagger UI**, é possível visualizar os endpoints disponíveis, seus parâmetros, os modelos de dados e também realizar requisições diretamente pelo navegador.

## Banco de dados

O projeto utiliza o **PostgreSQL** para armazenamento dos dados.

A comunicação entre a aplicação e o banco é realizada através do **SQLAlchemy**, enquanto o **Pydantic** é utilizado para validação e estruturação dos dados enviados e recebidos pela API.

## Objetivo

O projeto foi desenvolvido para colocar em prática conceitos de desenvolvimento backend e construção de APIs REST utilizando Python.

Entre os principais conceitos aplicados estão:

* APIs REST;
* FastAPI;
* Uvicorn;
* PostgreSQL;
* SQLAlchemy;
* Pydantic;
* Operações com banco de dados;
* Validação de dados;
* Documentação automática de APIs.

## Próximos passos

Possíveis melhorias para versões futuras:

* Implementação de autenticação com JWT;
* Sistema de usuários;
* Sistema de empréstimos e devoluções;
* Paginação;
* Filtros e pesquisa;
* Testes automatizados;
* Dockerização da aplicação.

## Autor

Desenvolvido por **Tiago**.


## Autor

Desenvolvido por **Tiago**.

Projeto criado com o objetivo de colocar em prática conhecimentos de desenvolvimento backend e construção de APIs com Python.
