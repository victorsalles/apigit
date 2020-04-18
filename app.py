from flask import Flask
from flask_restful import Api
from resources.classes import UserData, UserRepos, RepoDetails, Database, DatabaseUsers

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

@app.before_first_request
def cria_banco():
    banco.create_all()

api.add_resource(UserData, '/users/<string:user_name>')
api.add_resource(UserRepos, '/repos/<string:user_name>')
api.add_resource(RepoDetails, '/repos/<string:user_name>/<string:repo_name>')
api.add_resource(DatabaseUsers, '/database/users')
api.add_resource(Database, '/database/<string:user_name>')

if __name__ == '__main__':
    from sql_alchemy import banco
    banco.init_app(app)
    app.run()
