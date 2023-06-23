import pytest
from pyscaffold import __version__ as pyscaffold_version
from pyscaffold import api, cli

from pyscaffoldext.elegent_pythonpackage.extension import ElegentPythonpackage

CONV_FILES = [
    "README",
    "AUTHORS",
    # "CHANGELOG",
    # "CONTRIBUTING",
    # "docs/index",
    # "docs/readme",
    # "docs/authors",
    # "docs/changelog",
    # "docs/contributing",
]


@pytest.mark.slow
@pytest.mark.system
def test_cli_with_markdown_and_update(tmpfolder):
    # Given a project exists with the markdown extension
    opts = dict(
        project_path="proj",
        package="pkg",
        version=pyscaffold_version,
        extensions=[ElegentPythonpackage()],
        config_files=api.NO_CONFIG,
    )
    api.create_project(opts)

    # when the project is updated
    args = ["--no-config", "--update", "proj"]
    cli.main(args)

    # then markdown files should still exist, and not rst equivalent should be created
    for file in CONV_FILES:
        assert (tmpfolder / f"proj/{file}.md").exists()
