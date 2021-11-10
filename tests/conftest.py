import logging
import tempfile
import os
import pytest

from pathlib import Path
from contextlib import contextmanager

from webtest import TestApp

from pabui import create_app


@contextmanager
def temp_chdir() -> str:
    with tempfile.TemporaryDirectory() as tmpdir:
        pwd = Path().absolute()
        os.chdir(tmpdir)
        yield tmpdir
        os.chdir(pwd)


@pytest.fixture(scope="session")
def test_settings() -> dict:
    return {
        "ENV": "development",
        "FLASK_SECRET_KEY": "woo",
    }


@pytest.fixture(scope="session")
def app(test_settings):
    """Create application for the tests."""
    with temp_chdir() as rootdir:
        _app = create_app(test_settings)
        _app.logger.setLevel(logging.ERROR)
        _app.config["TESTING"] = True
        ctx = _app.test_request_context()
        ctx.push()
        setattr(_app, "_rootdir", rootdir)
        yield _app
        ctx.pop()


@pytest.fixture(scope="session")
def testapp(app):
    _app = TestApp(app)
    setattr(_app, "_rootdir", Path(app._rootdir))
    return _app
