from typing import Optional, List, Dict

from pydantic import BaseModel

from ec_cart.models.ProductImage import ProductImageModel
from ec_cart.models.ProductVariant import ProductVariantModel
from ec_cart.models.VariantOption import VariantOptionModel


class ProductModel(BaseModel):
    id: int
    title: Optional[str] = None
    body_html: Optional[str] = None
    created_at: Optional[str] = None
    handle: Optional[str] = None
    product_type: Optional[str] = None
    published_at: Optional[str] = None
    published_scope: Optional[str] = None
    status: Optional[str] = None
    tags: Optional[str] = None
    template_suffix: Optional[str] = None
    updated_at: Optional[str] = None
    vendor: Optional[str] = None
    images: Optional[List[Optional[ProductImageModel]]] = []
    variants: Optional[List[Optional[ProductVariantModel]]] = []
    options: Optional[VariantOptionModel] = []
