from typing import Any

from ec_cart import exceptions
from ec_cart.base import ActiveResource
from ec_cart.models.OrderEditBegin import OrderEditBeginModel


class OrderEditBegin(ActiveResource):
    _api_path = "/orders/edit/begin/"

    class Meta:
        model = OrderEditBeginModel

    def create(self, **kwargs):
        return self._post(**kwargs)

    def delete(self, id_=None, **kwargs):
        raise exceptions.MethodNotAllowedError