""" APC Home API """

from typing import List
import aiohttp

from . import utils
from .typings import App, Login, APC, Devices

from .const import DEVICES_URL, DEVICE_PROPERTIES_URL, LOGIN_URL, POWERSTATE_URL


class APCService:
    """ API Service """

    def __init__(self, app: App.Context):

        self._app = app
        self._timeout = 30

    async def _send(self, url, headers: dict = None, data=None, json=None):
        if self._access_token:
            if not headers:
                headers = {}
            headers["Authorization"] = f"auth_token {self._access_token}"

        async with aiohttp.ClientSession(timeout=self._timeout) as session:
            if not data and not json:
                async with session.get(url, headers=headers) as response:
                    return await response.json()
            else:
                async with session.post(
                    url, headers=headers, data=data, json=json
                ) as response:
                    return await response.json()

    def _is_connected(self):
        return bool(self._access_token and self._refresh_token)

    async def login(self, email: str, password: str):
        """ Login to Service """

        if self._is_connected():
            return True

        login: Login.Request = {}
        user = login["user"]
        user["application"] = utils.App.as_data(self._app)
        user["email"] = email
        user["password"] = password

        response: Login.Response = await self._send(LOGIN_URL, json=login)

        self._access_token = response["access_token"]
        self._refresh_token = response["refresh_token"]

        return True

    async def get_devices(self):
        """ get all devices """
        if not self._is_connected:
            return None

        devices: List[APC.Device] = []

        _devices: List[dict] = await self._send(DEVICES_URL)
        for _device in _devices:
            device = utils.Devices.as_device(_device)
            devices.append(device)
            _outlets = await self._get_device_properties(_device["dsn"])
            for outlet in _outlets:
                device.outlets.append(outlet)

        return devices

    async def _get_device_properties(self, dsn: str):
        if not self._is_connected:
            return None

        outlets: List[APC.Outlet] = []

        _outlets: List[dict] = await self._send(DEVICE_PROPERTIES_URL.format(dsn=dsn))
        for _outlet in _outlets:
            outlets.append(utils.Devices.as_outlet(_outlet))

        return outlets

    async def set_power_state(self, outlet: APC.Outlet, value: bool):
        """ set the powerstate for an outlet """
        if not self._is_connected:
            return False

        state: Devices.PowerState = {}
        state["datapoint"] = {}
        dp = state["datapoint"]
        dp["value"] = bool(value)

        await self._send(POWERSTATE_URL.format(**outlet), json=state)
        return True
