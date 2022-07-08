from typing import Optional, List, Literal
from pydantic import BaseModel


class ShopModel(BaseModel):
    id: int = None
    name: str = None
