from typing import Optional, List, Literal
from pydantic import BaseModel


class InventoryModel(BaseModel):
    available: float = None
    inventory_item_id: int = None
    location_id: int = None


class ArticleObject(BaseModel):
    id: int = None
    sku: str = None
    name: str = None


class WarehouseObject(BaseModel):
    id: int = None
    name: str = None


class InventoryGetModel(BaseModel):
    id: int = None
    free: int = None
    article: ArticleObject = None
    warehouse: WarehouseObject = None
