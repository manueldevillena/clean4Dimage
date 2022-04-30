Tool to identify and (if possible) remove outliers in a 4D fMRI image.

# Installation
This tool is written in Python 3.10.3 as a python module, before installing it, make sure you have at least that version of Python.

## Option A
You can use Poetry (https://python-poetry.org) to install the python environment. To do so, in the root folder of the cloned repository, type:

```
poetry install
```

This will install the dependencies written in `poetry.lock`. These dependencies have been tested and should work with no issues.

After the environment is installed, activate it with:

```
source $(poetry env info --path)/bin/activate
```

## Option B
You can also install the dependencies using your preferred python environment manager. The dependencies are written in a requirements.txt. An example using `venv` is:

```
python -m venv <ENV_NAME>
source <ENV_NAME>/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

# Run
This tool can be run as a python module. The help function can be called as:

```
python -m clean4Dimage -h
```

An example can be run with:

```
python -m clean4Dimage -o results
```


