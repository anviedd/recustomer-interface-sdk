from typing import Optional, List

from pydantic import BaseModel


class VariantOptionModel(BaseModel):
    id: int
    position: int
    product_id: Optional[int] = None
    name: Optional[str] = None
    variant_ids: List[str] = []
