""" Login typings """

from typing import TypedDict

from .Requests import Data as LoginData


class Request(TypedDict):
    """ Login Request """

    user: LoginData


class Response(TypedDict):
    """ Login Response """

    access_token: str
    refresh_token: str