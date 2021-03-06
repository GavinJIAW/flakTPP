from flask_restful import Api

from apps.apis.movie_user.movie_user_api import MovieUsersResource

client_api = Api(prefix='/user')

client_api.add_resource(MovieUsersResource, '/movieusers/')
