import os
import json

from contextlib import contextmanager
from pathlib import Path


EXAMPLE_DATA =  {
    "MyContract": {
        "address": "0x1234",
        "abifile": "MyContract.abi"
    }
}

EXAMPLE_ABI = '{"inputs":[{"internalType":"address","name":"_token","type":"address"},{"internalType":"address","name":"_controller","type":"address"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"}'


@contextmanager
def example_abi_data(parent: Path):
    contracts_file = parent / "contracts.json"
    abis_dir = parent / "abis"
    abi_file = abis_dir / "MyContract.abi"
    if not abis_dir.is_dir():
        os.mkdir(abis_dir)
    with contracts_file.open("w") as fp:
        json.dump(EXAMPLE_DATA, fp)
    with abi_file.open("w") as fp:
        fp.write(EXAMPLE_ABI)
    yield 
    os.remove(abi_file)
    os.remove(contracts_file)



def test_abi_get_data(testapp):
    with example_abi_data(testapp._rootdir):
        res = testapp.get("/api/contracts/get")
        data = res.json
        assert data["MyContract"]["address"] == EXAMPLE_DATA["MyContract"]["address"]
        assert data["MyContract"]["abifile"] == EXAMPLE_DATA["MyContract"]["abifile"]
        assert data["MyContract"]["abi"] == EXAMPLE_ABI
