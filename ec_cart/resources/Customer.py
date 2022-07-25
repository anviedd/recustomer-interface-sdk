from ec_cart import exceptions
from ec_cart.base import ActiveResource
from ec_cart.models.Customer import CustomerModel


class Customer(ActiveResource):
    _api_path = "/customers/${id}"

    class Meta:
        model = CustomerModel

    def delete(self, id_=None, **kwargs):
        raise exceptions.MethodNotAllowedError
