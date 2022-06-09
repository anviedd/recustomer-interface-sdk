from typing import Optional, List
from pydantic import BaseModel

from ec_cart.models.BillingAddress import BillingAddressModel
from ec_cart.models.Customer import CustomerModel
from ec_cart.models.LineItem import LineItemModel


class FulFillMent(BaseModel):
    id: int
    status: Optional[str] = None
    tracking_company: Optional[str] = None
    tracking_number: Optional[str] = None
    tracking_numbers: Optional[List[str]] = []
    tracking_url: Optional[str] = None
    tracking_urls: Optional[List[str]] = []


class OrderModel(BaseModel):
    id: int = None
    cancel_reason: Optional[str] = None
    cancelled_at: Optional[str] = None
    closed_at: Optional[str] = None
    created_at: Optional[str] = None
    confirmed: bool
    financial_status: Optional[str] = None
    fulfillment_status: Optional[str] = None
    name: Optional[str] = None
    note: Optional[str] = None
    number: int = None
    order_number: int = None
    phone: Optional[str] = None
    billing_address: Optional[BillingAddressModel] = None
    customer: Optional[CustomerModel] = None
    line_items: Optional[List[Optional[LineItemModel]]] = []
    fulfillments: Optional[List[Optional[FulFillMent]]] = []
