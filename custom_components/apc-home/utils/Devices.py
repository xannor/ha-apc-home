""" Device utils """

from typing import cast
from ..typings import Devices, APC


def as_device(self: dict):
    if "connectedAt" in self:
        self["connected_at"] = self["connectedAd"]
        self.pop("connectedAd")

    return APC.Device(**self)


def as_outlet(self: dict):
    return APC.Outlet(**self)
