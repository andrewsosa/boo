from functools import wraps
from typing import Any, Callable, Tuple
from flask import request
from flask_restful import Resource
from marshmallow import exceptions
from .controllers import TaskController


Response = Tuple[Any, int]


def res_handler(func: Callable[..., Response]):
    @wraps(func)
    def _handler(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except exceptions.ValidationError as err:
            return err.messages, 400
        except TypeError as err:
            if "unexpected keyword argument" in err.message:
                return "Method not allowed", 405
            raise

    return _handler


class Task(Resource):

    schema = TaskController.Schema()
    schema_multi = TaskController.Schema(many=True)

    @res_handler
    def get(self, task_id: int = None) -> Response:
        if not task_id:
            tasks = self.schema_multi.dump(TaskController.model.query.all())
            return tasks, 200
        else:
            task = self.schema.dump(
                TaskController.model.query.filter_by(id=task_id).first()
            )
            return task, 200

    @res_handler
    def post(self) -> Response:
        jsn = request.get_json(force=True)
        task = TaskController.load(jsn)
        return self.schema.dump(task), 201
