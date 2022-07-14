from typing import Optional, List, Literal
from pydantic import BaseModel


class UserErrors(BaseModel):
    field: Optional[str] = None
    message: Optional[str] = None


class LineItemsNode(BaseModel):
    id: str = None


class LineItemsEdges(BaseModel):
    node: Optional[LineItemsNode] = None


class LineItems(BaseModel):
    edges: Optional[List[LineItemsEdges]] = None


class CalculatedOrder(BaseModel):
    id: str = None
    lineItems: LineItems = None


class userErrors(BaseModel):
    field: str = None
    message: str = None


class OrderEditCommitModel(BaseModel):
    order_calculated_id: str = None
