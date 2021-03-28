""" Devices """

from typing import TypedDict


class PowerStateDatapoint(TypedDict):
    """ Power State Data Point """

    value: bool


class PowerState(TypedDict):
    """ Power State """

    datapoint: PowerStateDatapoint