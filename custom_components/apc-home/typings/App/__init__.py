""" App typings """

from typing import NamedTuple, TypedDict


class Context(NamedTuple):
    """ App Context """

    id: str
    secret: str


class Data(TypedDict):
    """ App Data """

    app_id: str
    app_secret: str
