from . import models
from .db import db


class TaskController:
    model = models.Task
    Schema = models.TaskSchema

    @classmethod
    def create(cls, name: str, **kwargs: dict) -> "models.Task":
        task = cls.model(name=name)
        db.session.add(task)
        db.session.commit()
        return task

    @classmethod
    def load(cls, data) -> "models.Task":
        data = cls.Schema().load(data)
        return cls.create(**data)
