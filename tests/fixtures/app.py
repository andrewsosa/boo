import pytest
from flask import Flask
from boo import create_app


@pytest.fixture(scope="session")
def app(request) -> Flask:
    app = create_app(config="boo.config.Test")
    ctx = app.app_context()

    ctx.push()
    request.addfinalizer(lambda: ctx.pop())

    return app
