from typing import Optional
from pydantic import BaseModel


class LineItemModel(BaseModel):
    id: int = None
    admin_graphql_api_id: Optional[str] = None
    grams: Optional[int] = None
    name: Optional[str] = None
    price: Optional[str] = None
    product_exists: Optional[bool] = None
    product_id: Optional[int] = None
    quantity: Optional[int] = None
    requires_shipping: Optional[bool] = None
    sku: Optional[str] = None
    title: Optional[str] = None
    total_discount: Optional[str] = None
    variant_id: Optional[str] = None
    variant_title: Optional[str] = None
