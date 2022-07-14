from typing import Any

from ec_cart import exceptions
from ec_cart.base import ActiveResource
from ec_cart.models.UsageRecord import UsageRecordModel


class UsageRecord(ActiveResource):
    _api_path = "/usage_records/"

    class Meta:
        model = UsageRecordModel

    def create(self, **kwargs):
        return self._post(**kwargs)

    def delete(self, id_=None, **kwargs):
        raise exceptions.MethodNotAllowedError
