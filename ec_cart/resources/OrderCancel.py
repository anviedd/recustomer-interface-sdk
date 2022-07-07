from typing import Any

from ec_cart import exceptions
from ec_cart.base import ActiveResource
from ec_cart.models.OrderTransaction import OrderTransactionModel


class OrderCancel(ActiveResource):
    _api_path = "/orders/${order_id}/cancel/"

    class Meta:
        model = OrderTransactionModel

    def create(self, id_=None, **kwargs):
        if id_:
            kwargs['id'] = str(id_)

        return self._post(**kwargs)

    def delete(self, id_=None, **kwargs):
        raise exceptions.MethodNotAllowedError