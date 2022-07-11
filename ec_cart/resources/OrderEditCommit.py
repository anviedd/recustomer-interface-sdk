from typing import Any

from ec_cart import exceptions
from ec_cart.base import ActiveResource
from ec_cart.models.OrderEditCommit import OrderEditCommitModel

class OrderEditCommit(ActiveResource):
    _api_path = "/orders/edit/commit/"

    class Meta:
        model = OrderEditCommitModel

    def create(self, **kwargs):
        return self._post(**kwargs)

    def delete(self, id_=None, **kwargs):
        raise exceptions.MethodNotAllowedError