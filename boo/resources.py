from flask_restful import Resource


class Task(Resource):
    def get(self):
        return {"name": "mtask"}