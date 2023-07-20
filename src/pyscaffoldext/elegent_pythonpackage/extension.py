from functools import partial
from typing import List

from pyscaffold.actions import Action, ActionParams, ScaffoldOpts, Structure
from pyscaffold.extensions import Extension, include
from pyscaffold.extensions.pre_commit import PreCommit
from pyscaffold.identification import get_id
from pyscaffold.operations import no_overwrite
from pyscaffold.structure import merge, reject
from pyscaffold.templates import get_template

from pyscaffoldext.markdown.extension import Markdown, replace_files

from . import templates

NO_OVERWRITE = no_overwrite()


template = partial(get_template, relative_to=templates)


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
        actions = Markdown().activate(actions)
        # ^  Wrapping the Markdown extension is more reliable than including it via CLI.
        #    This way we can trust the activation order for registering actions,
        #    and the Python API is guaranteed to work, even if the user does not include
        #    Markdown in the list of extensions.
        actions = self.register(
            actions, replace_elegentfiles, after=get_id(replace_files)
        )
        actions = self.register(
            actions, remove_files, after=get_id(replace_elegentfiles)
        )
        return actions


def replace_elegentfiles(struct: Structure, opts: ScaffoldOpts) -> ActionParams:
    """Replace the readme.md of the markdown extension by our own, and others
    See :obj:`pyscaffold.actions.Action`
    """

    files: Structure = {
        "AUTHORS.md": (template("authors"), NO_OVERWRITE),
        "README.md": (template("readme"), NO_OVERWRITE),
        "CONTRIBUTING.md": (template("contributing"), NO_OVERWRITE),
        "LICENSE.txt": (template("license"), NO_OVERWRITE),
        "tox.ini": (template("tox_ini"), NO_OVERWRITE),
    }
    return merge(struct, files), opts


def remove_files(struct: Structure, opts: ScaffoldOpts) -> ActionParams:
    """Remove files to structure"""
    struct = reject(struct, ".readthedocs.yml")
    struct = reject(struct, ".coveragerc")
    return struct, opts
