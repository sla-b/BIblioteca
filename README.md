# Biblioteca API

API REST desenvolvida em Python para gerenciamento de uma biblioteca, utilizando FastAPI, PostgreSQL, SQLAlchemy e Pydantic.

O projeto foi desenvolvido com foco na aplicação prática de conceitos de desenvolvimento de APIs, integração com banco de dados relacional, validação de dados e organização de uma aplicação backend.

## Tecnologias utilizadas

* **Python** — Linguagem utilizada no desenvolvimento da aplicação.
* **FastAPI** — Framework utilizado para construção da API REST.
* **PostgreSQL** — Banco de dados relacional utilizado para persistência das informações.
* **SQLAlchemy** — ORM utilizado para comunicação e manipulação dos dados no banco de dados.
* **Pydantic** — Biblioteca utilizada para validação e serialização dos dados recebidos pela API.

## Arquitetura

A aplicação utiliza uma arquitetura baseada na separação entre:

* **Rotas/Endpoints** — Responsáveis por receber e processar as requisições HTTP.
* **Schemas** — Responsáveis pela validação e estruturação dos dados utilizando Pydantic.
* **Models** — Representam as entidades armazenadas no banco de dados através do SQLAlchemy.
* **Database** — Responsável pela configuração da conexão com o PostgreSQL e gerenciamento das sessões do banco.

## Banco de dados

O projeto utiliza o **PostgreSQL** como sistema de gerenciamento de banco de dados.

A comunicação entre a aplicação e o banco é realizada através do **SQLAlchemy**, permitindo trabalhar com as entidades do banco por meio de modelos Python.

## Instalação

Clone o repositório:

```bash
git clone https://github.com/sla-b/BIblioteca.git
```

Entre no diretório do projeto:

```bash
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

## Configuração

Antes de executar a aplicação, configure a conexão com o PostgreSQL de acordo com as configurações utilizadas no projeto.

Caso utilize variáveis de ambiente, configure o arquivo `.env` com as informações necessárias para conexão com o banco de dados.

## Executando a aplicação

Inicie o servidor utilizando o Uvicorn:

```bash
uvicorn main:app --reload
```

Após iniciar a aplicação, ela estará disponível localmente em:

```text
http://127.0.0.1:8000
```

## Documentação da API

Por utilizar FastAPI, o projeto disponibiliza documentação interativa automaticamente.

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

### ReDoc

```text
http://127.0.0.1:8000/redoc
```

Essas interfaces permitem visualizar os endpoints disponíveis e realizar requisições diretamente pelo navegador.

## Objetivo do projeto

O projeto foi desenvolvido como uma aplicação prática para consolidar conhecimentos em desenvolvimento backend com Python, trabalhando conceitos como:

* Desenvolvimento de APIs REST;
* Métodos HTTP;
* Integração com banco de dados PostgreSQL;
* ORM com SQLAlchemy;
* Validação de dados com Pydantic;
* Estruturação de aplicações FastAPI;
* Documentação automática de APIs.

## Próximos passos

Algumas funcionalidades que podem ser adicionadas futuramente ao projeto:

* Autenticação e autorização de usuários;
* JWT;
* Sistema de empréstimos e devoluções;
* Controle de usuários;
* Paginação de resultados;
* Filtros e pesquisa de livros;
* Testes automatizados;
* Dockerização da aplicação.

## Autor

Desenvolvido por **Tiago**.

Projeto criado com o objetivo de colocar em prática conhecimentos de desenvolvimento backend e construção de APIs com Python.
