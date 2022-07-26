from typing import Optional, Dict, Union, List

from pydantic import BaseModel


class CollectionsNode(BaseModel):
    id: str = None
    title: str = None


class CollectionsEdges(BaseModel):
    node: CollectionsNode = None


class Collections(BaseModel):
    edges: List[Union[CollectionsEdges, None]] = None

class ProductNode(BaseModel):
    tags: List[str] = None


class ProductsEdges(BaseModel):
    node: ProductNode = None


class Products(BaseModel):
    edges: List[Union[ProductsEdges, None]] = None


class OrdersNode(BaseModel):
    tags: List[str] = None


class OrdersEdges(BaseModel):
    node: OrdersNode = None


class Orders(BaseModel):
    edges: List[Union[OrdersEdges, None]] = None


class PriceRulesNode(BaseModel):
    title: str = None


class PriceRulesEdges(BaseModel):
    node: PriceRulesNode = None


class PriceRules(BaseModel):
    edges: List[Union[PriceRulesEdges, None]] = None


class IneligibleDataModel(BaseModel):
    price_rules: PriceRules = None
    order_tags: Orders = None
    collections: Collections = None
    product_tags: Optional[Products] = None
