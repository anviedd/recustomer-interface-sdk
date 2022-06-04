from ec_cart.base import ActiveResource
from ec_cart.models.Product import ProductModel


class Product(ActiveResource):
    _api_path = "/products/${id}"

    class Meta:
        model = ProductModel
