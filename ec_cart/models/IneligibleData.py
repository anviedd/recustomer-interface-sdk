from typing import Optional, Dict, Union, List

from pydantic import BaseModel


class CollectionsNode(BaseModel):
    id: int = None
    title: str = None


class CollectionsEdges(BaseModel):
    node: str = None


class Collections(BaseModel):
    edges: str = None


class OrdersNode(BaseModel):
    tags: List[str] = None


class OrdersEdges(BaseModel):
    node: OrdersNode = None


class Orders(BaseModel):
    orders: List[Dict[str, Union[int, str, float]]]


class PriceRulesNode(BaseModel):
    title: str = None


class PriceRulesEdges(BaseModel):
    node: PriceRulesNode = None


class PriceRules(BaseModel):
    edges: List[Union[PriceRulesEdges, None]] = None


class IneligibleData(BaseModel):
    priceRules: Optional[PriceRules] = None
    orders: Optional[Orders] = None
    collections: Optional[Collections] = None


class IneligibleDataModel(BaseModel):
    data: IneligibleData = None
