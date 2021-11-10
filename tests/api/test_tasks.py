import os
import json

from contextlib import contextmanager
from pathlib import Path


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
def temp_tasks(data: dict, parent: str):
    file_ = Path(parent) / "tasks.json"
    with file_.open("w") as fp:
        json.dump(data, fp)
        fp.flush()
    yield 
    os.remove(file_)



def test_tasks_read(testapp):
    with temp_tasks(EXAMPLE_DATA, testapp._rootdir):
        res = testapp.get("/api/tasks/get")
        assert res.json
        assert EXAMPLE_DATA == res.json


def test_tasks_read_fails_if_not_loaded(testapp):
    ...


def test_tasks_save(testapp):
    res = testapp.post_json(
        "/api/tasks/save", 
        EXAMPLE_DATA
    )
    assert res.json["saved"] == True
    with open(testapp._rootdir / "tasks.json", "r") as fp:
        assert EXAMPLE_DATA == json.load(fp)

    res = testapp.get("/api/tasks/get")
    assert EXAMPLE_DATA == res.json