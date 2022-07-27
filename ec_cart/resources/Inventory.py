from typing import Any

from ec_cart import exceptions
from ec_cart.base import ActiveResource
from ec_cart.models.Inventory import InventoryModel


class Inventory(ActiveResource):
    _api_path = "/inventories/"

    class Meta:
        model = InventoryModel

    def create(self, **kwargs):
        return self._post(**kwargs)

    def delete(self, id_=None, **kwargs):
        raise exceptions.MethodNotAllowedError