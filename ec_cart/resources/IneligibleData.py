from ec_cart import exceptions
from ec_cart.base import ActiveResource
from ec_cart.models.IneligibleData import IneligibleDataModel


class IneligibleData(ActiveResource):
    _api_path = "/ineligible_data"

    class Meta:
        model = IneligibleDataModel

    def delete(self, id_=None, **kwargs):
        raise exceptions.MethodNotAllowedError
