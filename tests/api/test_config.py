import tempfile
import json
import os

from contextlib import contextmanager
from pathlib import Path
from unittest import TestCase


@contextmanager
def temp_config(data: dict, parent: str):
    file_ = Path(parent) / "config.json"
    with file_.open("w") as fp:
        json.dump(data, fp)
        fp.flush()
    yield 
    os.remove(file_)


def test_config_defaults(testapp):
    res = testapp.get(
        "/api/config/defaults"
    )
    assert res.json


def test_config_currents(testapp):
    data = {"myAddress": 123, "endpoint": "http://example.com/"}
    with temp_config(data, testapp._rootdir):
        res = testapp.get(
            "/api/config/current"
        )
        assert res.json
        TestCase().assertDictEqual(data, res.json)


def test_config_current_fails_if_not_loaded(testapp):
    ...


def test_config_save(testapp):
    data = {"myAddress": 123, "endpoint": "http://example.com/"}
    res = testapp.post_json(
        "/api/config/save", 
        data
    )
    assert res.json["saved"] == True
    with open(Path(testapp._rootdir) / "config.json", "r") as fp:
        TestCase().assertDictEqual(data, json.load(fp))

    