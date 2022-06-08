from typing import Any

from ec_cart import exceptions
from ec_cart.base import ActiveResource
from ec_cart.models.ProductVariant import ProductVariantModel


class Variant(ActiveResource):
    _api_path = "/variants/${id}"

    class Meta:
        model = ProductVariantModel

    def find(self, id=None, variant_ids=None, **kwargs) -> Any:
        if not id and not variant_ids:
            raise exceptions.VariantIdNotFoundError
        elif id:
            kwargs['id'] = id
        elif variant_ids:
            kwargs['variant_ids'] = variant_ids

        return super(Variant, self).find(id_=None, **kwargs)
