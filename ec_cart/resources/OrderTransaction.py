from typing import Any

from ec_cart import exceptions
from ec_cart.base import ActiveResource
from ec_cart.models.OrderTransaction import OrderTransactionModel


class OrderTransaction(ActiveResource):
    _api_path = "/orders/${order_id}/transactions/"
    _detail_api_path = '${transaction_id}'

    class Meta:
        model = OrderTransactionModel

    def create(self, id_=None, **kwargs):
        if id_:
            kwargs['id'] = str(id_)

        return self._post(**kwargs)

    def find(self, order_id, id_=None, **kwargs) -> Any:
        if not order_id:
            raise exceptions.OrderIdNotFoundError

        kwargs['order_id'] = str(order_id)

        return super(OrderTransaction, self).find(id_=None, **kwargs)
