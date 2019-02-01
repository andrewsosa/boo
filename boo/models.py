from marshmallow import Schema, fields, pre_load, validate
from .db import db, ma


class Task(db.Model):
    __tablename__ = "tasks"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False)

    def __init__(self, name: str):
        self.name = name

    class Schema(ma.Schema):
        id = fields.Integer(dump_only=True)
        name = fields.String(required=True)
