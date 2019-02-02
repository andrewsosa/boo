import pytest
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from boo.db import db as _db


@pytest.fixture(scope="session")
def db(app: Flask, request) -> SQLAlchemy:
    _db.init_app(app)
    _db.create_all()
    request.addfinalizer(lambda: _db.drop_all())

    return _db


@pytest.fixture(scope="function")
def session(db: SQLAlchemy, request):
    connection = db.engine.connect()
    transaction = connection.begin()

    opts = dict(bind=connection, binds={})
    session = db.create_scoped_session(options=opts)
    db.session = session

    @request.addfinalizer
    def teardown():
        transaction.rollback()
        connection.close()
        session.remove()

    return session
