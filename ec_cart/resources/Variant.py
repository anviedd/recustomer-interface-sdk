from typing import Any

from ec_cart import exceptions
from ec_cart.base import ActiveResource
from ec_cart.models.ProductVariant import ProductVariantModel


class Variant(ActiveResource):
    _api_path = "/variants/${id}"

    class Meta:
        model = ProductVariantModel

    def find(self, id_=None, **kwargs) -> Any:
        if not id_:
            raise exceptions.VariantIdNotFoundError
        kwargs['id'] = id_
        return super(Variant, self).find(id_=None, **kwargs)
