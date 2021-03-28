""" App Typing Utils """

from collections import namedtuple
from typing import cast
from ..typings import App


def as_data(self: App.Context):
    """ convert App.Context to App.Data """
    return cast(
        cast(self, namedtuple)._asdict(), App.Data  # pylint: disable=maybe-no-member
    )
