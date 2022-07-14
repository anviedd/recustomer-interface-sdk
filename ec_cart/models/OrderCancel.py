from typing import Optional, List, Literal
from pydantic import BaseModel


class Transaction(BaseModel):
    id: int
    kind: Optional[
        Literal["authorization", "capture", "sale", "void", "refund"]]
    amount: Optional[float]
    created_at: Optional[str]
    currency: Optional[str]
    gateway: Optional[str]
    location_id: Optional[int]
    message: Optional[str]
    order_id: Optional[int]
    parent_id: Optional[int]
    processed_at: Optional[str]
    status: Optional[Literal["pending", "failure", "success", "error"]]


class Refunds(BaseModel):
    transactions: Optional[List[Transaction]]


class OrderCancelModel(BaseModel):
    notice: str = None
    refunds: Optional[Refunds] = None