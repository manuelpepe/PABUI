# PAB UI

A Web-based GUI for PAB development


## Features

* Load project from host filesystem
* Read and edit configs
* Read, edit and create tasks
* List strategies and parameters
* Create/Restore private key
* Add new contracts
* List current contracts and ABIs


## Running the UI

```bash
	$ git clone https://github.com/manuelpepe/PABUI 
	$ python3 -m venv venv
	$ . venv/bin/activate
	$ pip install .
	$ cd ~/MyPABProject
	$ pabui  # TODO: Implement this command.
```


## Developing

After cloning the repo and installing all dependencies, make sure to install the pre-commit hooks for the
automatic formatter (see black):

```bash
	$ source venv/bin/activate
	$ pip install -r requirements-dev.txt
	$ pre-commit install
```

For UI development check [the frontend README](frontend/README.md)

### Running tests

```
	$ . venv/bin/activate
	$ pip install -r requirements-dev.txt
	$ pytest --cov=pabui
```


