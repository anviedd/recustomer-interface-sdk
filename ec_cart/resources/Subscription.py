from typing import Any

from ec_cart import exceptions
from ec_cart.base import ActiveResource
from ec_cart.models.Subscription import (
    SubscriptionCreateModel,
    SubscriptionCancelModel)


class Subscription(ActiveResource):
    _api_path = "/subscriptions/"

    class Meta:
        model = SubscriptionCreateModel

    def create(self, **kwargs):
        return self._post(**kwargs)

    def cancel(self, **kwargs):
        # changes api path and model
        self._api_path = "/subscriptions/cancel/"
        self.Meta.model = SubscriptionCancelModel
        return self._post(**kwargs)

    def delete(self, id_=None, **kwargs):
        raise exceptions.MethodNotAllowedError
