# FastAPI CRUD

Este é um programa simples que demonstra um CRUD (Create, Read, Update, Delete) utilizando o framework FastAPI.

## Descrição

Este programa consiste em uma API para gerenciar objetos "veiacos". 

A estrutura do programa é a seguinte:

- O arquivo `models.py` define o modelo de dados do "veiaco" utilizando SQLAlchemy.

- O arquivo `main.py` contém as rotas e os métodos para cada uma das operações do CRUD. Ele utiliza o SQLAlchemy para interagir com o banco de dados e o Pydantic para a validação dos dados de entrada e saída.

## Endpoints

- `GET /veiacos`: Retorna uma lista de todos os veiacos cadastrados.
- `POST /veiacos`: Cria um novo veiaco com base nos dados fornecidos.
- `GET /veiacos/{veiaco_id}`: Retorna os detalhes de um veiaco específico com base no ID fornecido.
- `PUT /veiacos/{veiaco_id}`: Atualiza as informações de um veiaco existente com base no ID fornecido.
- `DELETE /veiacos/{veiaco_id}`: Exclui um veiaco existente com base no ID fornecido.

## Inspiração 
(https://realpython.com/fastapi-python-web-apis/)