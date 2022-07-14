from typing import Any

from ec_cart import exceptions
from ec_cart.base import ActiveResource
from ec_cart.models.OrderEditLineQuantity import OrderEditLineQuantityModel


class OrderEditLineQuantity(ActiveResource):
    _api_path = "/orders/edit/line_quantity/"

    class Meta:
        model = OrderEditLineQuantityModel

    def create(self, **kwargs):
        return self._post(**kwargs)

    def delete(self, id_=None, **kwargs):
        raise exceptions.MethodNotAllowedError