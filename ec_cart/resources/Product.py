from ec_cart import exceptions
from ec_cart.base import ActiveResource
from ec_cart.models.Product import ProductModel


class Product(ActiveResource):
    _api_path = "/products/${id}"

    class Meta:
        model = ProductModel

    def delete(self, id_=None, **kwargs):
        raise exceptions.MethodNotAllowedError
