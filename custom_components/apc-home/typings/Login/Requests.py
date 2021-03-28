""" Login typings """

from typing import TypedDict

from ..App import Data as AppData


class Data(TypedDict):
    """ Login Request Data """

    email: str
    password: str
    application: AppData
