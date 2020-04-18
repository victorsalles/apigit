from flask_restful import Resource
from models.user import UserModel, RepoModel
import requests

class UserData(Resource):
    def get(self, user_name):
        URL = f'https://api.github.com/users/{user_name}'
        user_data = requests.request('GET', URL)
        if str(user_data) == '<Response [404]>':
            return {'message': f"User '{user_name}' not found in GitHub."}, 404
        return user_data.json(), 200


class UserRepos(Resource):
    def get(self, user_name):
        URL = f'https://api.github.com/users/{user_name}/repos'
        lista_repos = requests.request('GET', URL)
        if str(lista_repos) == '<Response [404]>':
            return {'message': f"User '{user_name}' not found in GitHub."}, 404
        repo_names = [repo['name'] for repo in lista_repos.json()]
        return {f"{user_name}'s repositories": repo_names}, 200


class RepoDetails(Resource):
    def get(self, user_name, repo_name):
        URL = f'https://api.github.com/repos/{user_name}/{repo_name}'
        repo_details = requests.request('GET', URL)
        if str(repo_details) == '<Response [404]>':
            return {'message': 'Repository not found. Check user/repo name.'}, 404
        return repo_details.json(), 200


class DatabaseUsers(Resource):
    def get(self):
        return {'Users in database': [user for user, in UserModel.query.with_entities(UserModel.login).all()]}, 200


class Database(Resource):
    def post(self, user_name):
        # Save Users in DB
        if UserModel.find_user(user_name):
            return {'message': f"User '{user_name}' already exists in database."}, 400
        URL = f'https://api.github.com/users/{user_name}'
        user_data = requests.request('GET', URL)
        if str(user_data) == '<Response [404]>':
            return {'message': f"User '{user_name}' not found in GitHub."}, 404
        user = UserModel(user_data.json())
        user.save_user()
        # Save Repos in DB
        URL = f'https://api.github.com/users/{user_name}/repos'
        lista_repos = requests.request('GET', URL)
        if str(lista_repos) == '<Response [404]>':
            return {'message': f"User '{user_name}' not found."}, 404
        lista_repos = lista_repos.json()
        if not lista_repos:
            return {'message': f"User '{user_name}' added to the database but there are no repositories available."}, 200
        for repo_data in lista_repos:
            repository = RepoModel(repo_data)
            repository.save_repo()
        return {'message': f"User '{user_name}' and his/her repositories added to the database."}, 200

    def get(self, user_name):
        if not UserModel.find_user(user_name):
            return {'message': f"User '{user_name}' does not exist in database."}, 404
        user = [UserModel.find_user(user_name).json()]
        repos = [repo.json() for repo in RepoModel.find_repo(user_name)]
        return (user + repos), 200
