import logging
import pytest

from pathlib import Path

from webtest import TestApp

from pabui import create_app


_res = Path(__file__).parent.absolute() / Path("resources")


@pytest.fixture(scope="session")
def test_settings() -> dict:
    return {
        "ENV": "development",
        "FLASK_SECRET_KEY": "woo",
        "SQLALCHEMY_DATABASE_URI": "mysql+pymysql://pabui:test@localhost/pabui_test",
        "SQLALCHEMY_TRACK_MODIFICATIONS": False,
        "PRESERVE_CONTEXT_ON_EXCEPTION": False,
    }


@pytest.fixture(scope="session")
def app(test_settings):
    """Create application for the tests."""
    _app = create_app(test_settings)
    _app.logger.setLevel(logging.ERROR)
    _app.config["TESTING"] = True
    ctx = _app.test_request_context()
    ctx.push()

    yield _app

    ctx.pop()


@pytest.fixture(scope="session")
def testapp(app):
    return TestApp(app)
