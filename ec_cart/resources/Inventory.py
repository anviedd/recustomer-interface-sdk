from typing import Any

from ec_cart import exceptions
from ec_cart.base import ActiveResource
from ec_cart.models.Inventory import InventoryModel, InventoryGetModel


class Inventory(ActiveResource):
    _api_path = "/inventories/"

    class Meta:
        model = InventoryModel

    def create(self, **kwargs):
        return self._post(**kwargs)

    def find(self, **kwargs):
        self.Meta.model = InventoryGetModel
        return self._get(**kwargs)

    def delete(self, id_=None, **kwargs):
        raise exceptions.MethodNotAllowedError
