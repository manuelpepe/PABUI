import tempfile
import json

from contextlib import contextmanager
from pathlib import Path
from unittest import TestCase


EXAMPLE_DATA =  [
    {
        "strategy": "MyStrat",
        "name": "Some Job",
        "repeat_every": {
            "hours": 12
        },
        "params": {
            "filepath": "file.log",
            "contract_name": "Controller"
        }
    }
]


@contextmanager
def temp_tasks(data: dict):
    with tempfile.TemporaryDirectory() as tmpdir:
        with open(Path(tmpdir) / "tasks.json", "w") as fp:
            json.dump(data, fp)
            fp.flush()
        yield tmpdir



def test_tasks_read(testapp):
    with temp_tasks(EXAMPLE_DATA) as tmpdir:
        testapp.post_json(
            "/api/app/set", 
            {"directory": tmpdir}
        )
        res = testapp.get("/api/tasks/get")
        assert res.json
        assert EXAMPLE_DATA == res.json


def test_tasks_read_fails_if_not_loaded(testapp):
    ...


def test_tasks_save(testapp):
    with tempfile.TemporaryDirectory() as tmpdir:
        testapp.post_json(
            "/api/app/set", 
            {"directory": tmpdir}
        )
        res = testapp.post_json(
            "/api/tasks/save", 
            EXAMPLE_DATA
        )
        assert res.json["saved"] == True
        with open(Path(tmpdir) / "tasks.json", "r") as fp:
            assert EXAMPLE_DATA == json.load(fp)

        res = testapp.get("/api/tasks/get")
        assert EXAMPLE_DATA == res.json