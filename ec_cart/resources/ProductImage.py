from typing import Any

from ec_cart import exceptions
from ec_cart.base import ActiveResource
from ec_cart.models.ProductImage import ProductImageModel


class ProductImage(ActiveResource):
    _api_path = "/products/${product_id}/images/"
    _detail_api_path = '${image_id}'

    class Meta:
        model = ProductImageModel

    def find(self, product_id, image_id, id_=None, **kwargs) -> Any:
        if not product_id or not image_id:
            raise exceptions.ProductIdAndImageIdNotFoundError

        kwargs['product_id'] = str(product_id)
        kwargs['image_id'] = str(image_id)

        return super(ProductImage, self).find(id_=None, **kwargs)

    def delete(self, id_=None, **kwargs):
        raise exceptions.MethodNotAllowedError
