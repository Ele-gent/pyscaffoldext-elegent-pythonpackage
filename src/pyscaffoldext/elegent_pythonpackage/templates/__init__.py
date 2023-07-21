from functools import partial

from pyscaffold.templates import ScaffoldOpts, get_template

from .. import __version__ as elegent_pythonpackage_version

template = partial(get_template, relative_to=__name__)


def readme_md(opts: ScaffoldOpts) -> str:
    """Adds a basic README.md

    Args:
        opts: given options, see :obj:`create_project` for an extensive list.

    Returns:
        file content as string
    """
    opts["pkg"] = opts["package"].ljust(19)
    opts["elegent_pythonpackage_version"] = elegent_pythonpackage_version
    return template("readme").safe_substitute(opts)
