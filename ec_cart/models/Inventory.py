from typing import Optional, List, Literal
from pydantic import BaseModel


class InventoryModel(BaseModel):
    available: float = None
    inventory_item_id: int = None
    location_id: int = None
