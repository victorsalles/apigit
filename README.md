pip freeze:

aniso8601==8.0.0
certifi==2020.4.5.1
chardet==3.0.4
click==7.1.1
Flask==1.1.2
Flask-RESTful==0.3.8
Flask-SQLAlchemy==2.4.1
idna==2.9
itsdangerous==1.1.0
Jinja2==2.11.2
MarkupSafe==1.1.1
pkg-resources==0.0.0
pytz==2019.3
requests==2.23.0
six==1.14.0
SQLAlchemy==1.3.16
urllib3==1.25.9
Werkzeug==1.0.1


python --version
Python 3.8.2

Utilizei o Postman (https://www.postman.com/downloads) para testar a API
Para rodar a API:
python app.py

A aplicação:

- Contém um endpoint para listar os repositórios públicos de um usuário;
- Contém um endpoint para mostrar os detalhes de um repositório específico;
- Insere os dados obtidos do Github em uma base de dados;
- Cria um tabela para armazenar os dados de um usuário;
- Cria uma tabela para armazenar os dados de um repositório;
- Contém um endpoint que lista os usuários salvos na sua tabela;
- Contém um endpoint que recebe um id de um usuário e retorna os dados dele e os detalhes de todos seus repositórios.


Endpoints:

'/users/<string:user_name>' --- (GET) Lista os dados de um determinado usuário da base do GitHub
'/repos/<string:user_name>' --- (GET) Lista os nomes dos repositórios públicos de um determinado usuário da base do GitHub
'/repos/<string:user_name>/<string:repo_name>' --- (GET) Lista os dados de um determinado repositório de um determinado usuário da base do GitHub
'/database/users' --- (GET) Lista os nomes de todos os usuários armazenados na database
'/database/<string:user_name>' --- (POST) Armazena os dados de um determinado usuário na database
'/database/<string:user_name>' --- (GET) Lista os dados de um determinado usuário e os dados de seus repositórios públicos
