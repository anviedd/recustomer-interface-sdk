from typing import Any

from ec_cart import exceptions
from ec_cart.base import ActiveResource
from ec_cart.models.ProductVariant import ProductVariantModel


class ProductVariant(ActiveResource):
    _api_path = "/products/${product_id}/variants"

    class Meta:
        model = ProductVariantModel

    def find(self, id_=None, **kwargs) -> Any:
        print("##########################################")
        print(kwargs)
        print("##########################################")
        if not id_:
            raise exceptions.ProductIdNotFoundError
        kwargs['product_id'] = id_
        return super(ProductVariant, self).find(id_=None, **kwargs)

    def delete(self, id_=None, **kwargs):
        raise exceptions.MethodNotAllowedError
