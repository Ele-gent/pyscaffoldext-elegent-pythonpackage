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

*NOTE*: can be used in combination with other options! Such as this more advanced usage:

```shell
putup \ # the command to call pyscaffold
	TEST-dash-app \ # name of the folder you are creating
	-p testdashapp \ # package name, i.e. what you will call in the import statement, this is the project_slug
	--description="Test for a dash app" \ # a small description (can be altered later in the corresponding files)
	-l="Proprietary" \ # type of license, if not open source, use proprietary
	--url https://github.com/Ele-gent/TEST-dash-app \ # URL to link to our github, use the name (first entry)
	--save-config ./TEST-dash-app/config_pyscaffold.cfg \ # save this configuration of options to a file
	--elegent-github-actions \ # use the Elegent github actions for CI
	--elegent-pythonpackage \ # this is a python package with the Elegent options
	--venv \ # create a python virtual environment
	--markdown \ # use markdown, not rst
	-vv \ # be very verbose (will print a lot of stuff to the cli)
```



<!-- pyscaffold-notes -->

## Note

This project has been set up using PyScaffold 4.5. For details and usage
information on PyScaffold see https://pyscaffold.org/.

created with

putup --custom-extension --markdown pyscaffoldext-elegent-pythonpackage
