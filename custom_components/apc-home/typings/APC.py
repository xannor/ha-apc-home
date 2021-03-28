""" APC Typings """

from dataclasses import dataclass, field
from typing import Any, List
import datetime as dt


@dataclass
class Outlet:
    """ APC Device Outlet """

    id: int
    name: str
    is_on: bool


@dataclass
class Device:
    """ APC Device """

    product_name: str
    model: str
    dsn: str
    oem_model: str
    sw_version: str
    template_id: str
    mac: str
    unique_hardware_id: Any
    hwsig: str
    lan_ip: str
    connected_at: dt.datetime
    key: int
    lan_enabled: bool
    has_properties: bool
    product_class: str
    connection_status: str
    lat: str
    lng: str
    locality: str
    device_type: str

    outlets: List[Outlet] = field(default_factory=list)
