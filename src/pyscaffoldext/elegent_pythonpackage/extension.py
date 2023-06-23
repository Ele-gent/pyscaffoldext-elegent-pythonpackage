from functools import partial
from typing import List

from pyscaffold.actions import Action, ActionParams, ScaffoldOpts, Structure
from pyscaffold.extensions import Extension
from pyscaffold.operations import no_overwrite

# from pyscaffold.structure import merge
from pyscaffold.templates import get_template

from . import templates

template = partial(get_template, relative_to=templates)


class ElegentPythonpackage(Extension):
    """
    This class serves as the skeleton for your new PyScaffold Extension. Refer
    to the official documentation to discover how to implement a PyScaffold
    extension - https://pyscaffold.org/en/latest/extensions.html
    """

    def activate(self, actions: List[Action]) -> List[Action]:
        """Activate extension. See :obj:`pyscaffold.extension.Extension.activate`."""
        # actions = self.register(actions, add_doc_requirements)
        return self.register(actions, replace_files, before="verify_project_dir")


# def add_files(struct: Structure, opts: ScaffoldOpts) -> ActionParams:
#     """Add custom extension files. See :obj:`pyscaffold.actions.Action`"""

#     template = get_template("awesome_file", relative_to=__name__)
#     test_template = get_template("test_awesome_file", relative_to=__name__)

#     files: Structure = {
#         "src": {opts["package"]: {"awesome_file.py": (template, no_overwrite())}},
#         "tests": {"test_awesome_file.py": (test_template, no_overwrite())},
#     }

#     return merge(struct, files), opts


# NOTE: Avoid renaming/removing replace_files.
#       The dsproject extension depends on that name, any changes in the function
#       signature here should be followed by a PR to that repository.
def replace_files(struct: Structure, opts: ScaffoldOpts) -> ActionParams:
    """Replace all rst files to proper md and activate Sphinx md.
    See :obj:`pyscaffold.actions.Action`

    function adapted from pyscaffoldext-markdown.extension.replace_files
    """
    # Define new files
    NO_OVERWRITE = no_overwrite()
    files: Structure = {
        "README.md": (template("readme"), NO_OVERWRITE),
        "AUTHORS.md": (template("authors"), NO_OVERWRITE),
        # "CHANGELOG.md": (template("changelog"), NO_OVERWRITE),
        # "CONTRIBUTING.md": (template("contributing"), NO_OVERWRITE),
        # "docs": {
        #     "index.md": (template("index"), NO_OVERWRITE),
        #     "readme.md": (default_myst_include("README.md"), NO_OVERWRITE),
        #     "license.md": (template("license"), NO_OVERWRITE),
        #     "authors.md": (default_myst_include("AUTHORS.md"), NO_OVERWRITE),
        #     "changelog.md": (default_myst_include("CHANGELOG.md"), NO_OVERWRITE),
        #     "contributing.md": (default_myst_include("CONTRIBUTING.md"), NO_OVERWRITE), # noqa
        # },
    }

    # TODO: Automatically convert RST to MD
    #
    # >>> content, file_op = reify_leaf(struct.get("CONTRIBUTING.rst"), opts)
    # >>> md_content = rst_to_myst(content or "", **RST2MYST_OPTS).text
    # >>> files["CONTRIBUTING.md"] = (md_content, file_op)
    #
    # Currently there is a problem in rst-to-myst, preventing automatic conversion:
    # https://github.com/executablebooks/rst-to-myst/issues/33#issuecomment-922264030

    # Modify pre-existing files
    # content, file_op = reify_leaf(struct["setup.cfg"], opts)
    # files["setup.cfg"] = (add_long_desc(content), file_op)

    # content, file_op = reify_leaf(struct["docs"]["conf.py"], opts)
    # files["docs"]["conf.py"] = (add_myst(content), file_op)

    # # Remove all unnecessary .rst files from struct
    # unnecessary = [
    #     "README.rst",
    #     "AUTHORS.rst",
    #     "CHANGELOG.rst",
    #     "CONTRIBUTING.rst",
    #     "docs/index.rst",
    #     "docs/readme.rst",
    #     "docs/license.rst",
    #     "docs/authors.rst",
    #     "docs/changelog.rst",
    #     "docs/contributing.rst",
    # ]
    # struct = reduce(reject, unnecessary, struct)

    # return merge(struct, files), opts
    return files, opts
