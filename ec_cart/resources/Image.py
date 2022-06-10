from typing import Any

from ec_cart import exceptions
from ec_cart.base import ActiveResource
from ec_cart.models.ProductImage import ProductImageModel


class Image(ActiveResource):
    _api_path = "/images/${id}"

    class Meta:
        model = ProductImageModel

    def find(self, variant_id=None, **kwargs) -> Any:
        if not variant_id:
            raise exceptions.VariantIdNotFoundError
        else:
            kwargs['id'] = variant_id
        return super(Image, self).find(id_=None, **kwargs)
