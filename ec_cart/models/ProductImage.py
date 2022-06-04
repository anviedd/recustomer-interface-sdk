from typing import Optional, List

from pydantic import BaseModel


class ProductImageModel(BaseModel):
    id: int
    position: int
    product_id: Optional[int] = None
    src: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    width: Optional[int] = None
    height: Optional[int] = None
    variant_ids: List[int] = []
