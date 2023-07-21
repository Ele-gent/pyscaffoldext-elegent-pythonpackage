from typing import List

from pyscaffold.actions import Action, ActionParams, ScaffoldOpts, Structure
from pyscaffold.extensions import Extension, include
from pyscaffold.extensions.pre_commit import PreCommit
from pyscaffold.identification import get_id
from pyscaffold.operations import no_overwrite
from pyscaffold.structure import ensure, merge, reject

from pyscaffoldext.markdown.extension import Markdown, replace_files

from .templates import readme_md, template

NO_OVERWRITE = no_overwrite()


class ElegentPythonpackage(Extension):
    """
    This class serves as the skeleton for your new PyScaffold Extension. Refer
    to the official documentation to discover how to implement a PyScaffold
    extension - https://pyscaffold.org/en/latest/extensions.html
    """

    _name = "elegent-pythonpackage"

    def augment_cli(self, parser):
        """Augments the command-line interface parser

        A command line argument ``--FLAG`` where FLAG=``self.name`` is added
        which appends ``self.activate`` to the list of extensions. As help
        text the docstring of the extension class is used.
        In most cases this method does not need to be overwritten.

        Args:
            parser: current parser object
        """

        parser.add_argument(
            self.flag,
            help=self.help_text,
            nargs=0,
            dest="extensions",
            action=include(PreCommit(), self),
        )
        return self

    def activate(self, actions: List[Action]) -> List[Action]:
        """Activate extension. See :obj:`pyscaffold.extension.Extension.activate`."""
        actions = self.register(actions, add_files, after="define_structure")
        actions = Markdown().activate(actions)
        # ^  Wrapping the Markdown extension is more reliable than including it via CLI.
        #    This way we can trust the activation order for registering actions,
        #    and the Python API is guaranteed to work, even if the user does not include
        #    Markdown in the list of extensions.
        actions = self.register(
            actions, replace_elegentfiles, after=get_id(replace_files)
        )
        actions = self.register(
            actions, replace_readme, after=get_id(replace_elegentfiles)
        )
        actions = self.register(actions, remove_files, after=get_id(replace_readme))
        return actions


def replace_elegentfiles(struct: Structure, opts: ScaffoldOpts) -> ActionParams:
    """Replace the readme.md of the markdown extension by our own, and others
    See :obj:`pyscaffold.actions.Action`
    """

    files: Structure = {
        "AUTHORS.md": (template("authors"), NO_OVERWRITE),
        # "README.md": (template("readme"), NO_OVERWRITE), # see separate function
        "CONTRIBUTING.md": (template("contributing"), NO_OVERWRITE),
        "LICENSE.txt": (template("license"), NO_OVERWRITE),
        "tox.ini": (template("tox_ini"), NO_OVERWRITE),
        ".pre-commit-config.yaml": (template("pre-commit-config"), NO_OVERWRITE),
    }
    return merge(struct, files), opts


def remove_files(struct: Structure, opts: ScaffoldOpts) -> ActionParams:
    """Remove files to structure"""
    struct = reject(struct, ".readthedocs.yml")
    struct = reject(struct, ".coveragerc")
    return struct, opts


def replace_readme(struct: Structure, opts: ScaffoldOpts) -> ActionParams:
    """Replace the readme.md of the markdown extension by our own
    See :obj:`pyscaffold.actions.Action`
    """
    return ensure(struct, "README.md", readme_md, NO_OVERWRITE), opts


def add_files(struct: Structure, opts: ScaffoldOpts) -> ActionParams:
    """Add in the folder .github/ISSUE_TEMPLATE/ the files bug_report.md and
    feature_request.md to the file structure

    Args:
        struct: project representation as (possibly) nested :obj:`dict`.
        opts: given options, see :obj:`create_project` for an extensive list.

    Returns:
        struct, opts: updated project representation and options
    """

    files: Structure = {
        ".github": {
            "ISSUE_TEMPLATE": {
                "feature_request.md": (template("feature_request"), no_overwrite()),
                "bug_report.md": (template("bug_report"), no_overwrite()),
            }
        },
    }

    return merge(struct, files), opts
