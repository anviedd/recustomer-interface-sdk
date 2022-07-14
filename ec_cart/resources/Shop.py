from typing import Any

from ec_cart import exceptions
from ec_cart.base import ActiveResource
from ec_cart.models.Shop import ShopModel


class Shop(ActiveResource):
    _api_path = "/shop/"

    class Meta:
        model = ShopModel

    def delete(self, id_=None, **kwargs):
        raise exceptions.MethodNotAllowedError
