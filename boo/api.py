from flask import Blueprint
from flask_restful import Api
from . import resources

api_blueprint = Blueprint("api", __name__)
api = Api(api_blueprint)

api.add_resource(resources.Task, "/task")
