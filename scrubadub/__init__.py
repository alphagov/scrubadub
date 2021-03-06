
# convenient imports
from .scrubbers import Scrubber
from . import filth
from . import detectors

__version__ = VERSION = "2.0.1"


def clean(text, cls=None, **kwargs):
    """Public facing function to clean ``text`` using the scrubber ``cls`` by
    replacing all personal information with ``{{PLACEHOLDERS}}``.
    """
    cls = cls or Scrubber
    scrubber = cls()
    return scrubber.clean(text, **kwargs)
