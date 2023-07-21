[![Project generated with PyScaffold](https://img.shields.io/badge/-PyScaffold-005CA0?logo=pyscaffold)](https://pyscaffold.org/)
[![tests](https://github.com/Ele-gent/pyscaffoldext-elegent-pythonpackage/actions/workflows/ci.yml/badge.svg)](https://github.com/Ele-gent/pyscaffoldext-elegent-pythonpackage/actions/workflows/ci.yml)

# pyscaffoldext-elegent-pythonpackage

> a custom pyscaffold extension for python packages in Elegent style

To be used with PyScaffold if you want the custom Elegent python package format instead of the standard ones from PyScaffold.

## Installation

**NOTE**:
The recommandation is to have 1 conda environment to put all your pyscaffold-shenanigans in (pyscaffold, and all the elegent custom extensions).

To install it, either clone this repo locally and install:

```bash
# cloning the repo via SSH
git clone git@github.com:Ele-gent/pyscaffoldext-elegent-pythonpackage.git
# or via GitHub CLI
gh repo clone Ele-gent/pyscaffoldext-elegent-pythonpackage
# move to the folder
cd pyscaffoldext-elegent-pythonpackage
# activate your desired environment, either via conda
source activate CONDA_ENV
# or a venv
source /path/to/venv/location/.venv/bin/activate
# install this package in editable mode
python -m pip install -e pyscaffoldext-elegent-pythonpackage
```

or download straight from github:

```bash
# activate your desired environment, either via conda
source activate CONDA_ENV
# or a venv
source /path/to/venv/location/.venv/bin/activate
# install this package
python -m pip install git+https://github.com/Ele-gent/pyscaffoldext-elegent-pythonpackage.git
```

Specific version can be installed through specifying branches (only recommended for work in progress) or using one of the [tags](https://github.com/Ele-gent/pyscaffoldext-elegent-pythonpackage/tags):
```bash
# some branch
python -m pip install git+https://github.com/Ele-gent/pyscaffoldext-elegent-pythonpackage.git@hotfix-feature-xxx
# some version
python -m pip install git+https://github.com/Ele-gent/pyscaffoldext-elegent-pythonpackage.git@v1.0.0
```

Note that `putup -h` shows a new option `--elegent-pythonpackage`.

## Usage

```shell
putup TEST --elegent-pythonpackage
```

*NOTE*: can be used in combination with other options!

<!-- pyscaffold-notes -->

## Note

This project has been set up using PyScaffold 4.5. For details and usage
information on PyScaffold see https://pyscaffold.org/.

created with

putup --custom-extension --markdown pyscaffoldext-elegent-pythonpackage
