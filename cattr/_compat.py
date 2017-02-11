import sys

version_info = sys.version_info[0:3]

if version_info < (3, 5, 4) or (3, 6, 0) <= version_info < (3, 6, 1):
    from .typing import *  # noqa
    from .typing import _Union  # noqa
else:
    from typing import *  # noqa
    from typing import _Union  # noqa