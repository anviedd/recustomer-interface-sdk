from typing import Optional, List
from pydantic import BaseModel

from ec_cart.models.BillingAddress import BillingAddressModel
from ec_cart.models.Customer import CustomerModel
from ec_cart.models.LineItem import LineItemModel


class ShippingAddress(BaseModel):
    address1: Optional[str] = None
    address2: Optional[str] = None
    city: Optional[str] = None
    company: Optional[str] = None
    country: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    latitude: Optional[str] = None
    longitude: Optional[str] = None
    phone: Optional[str] = None
    province: Optional[str] = None
    zip: Optional[str] = None
    name: Optional[str] = None
    country_code: Optional[str] = None
    province_code: Optional[str] = None


class FulFillMent(BaseModel):
    id: int
    status: Optional[str] = None
    created_at: Optional[str] = None
    tracking_company: Optional[str] = None
    tracking_number: Optional[str] = None
    tracking_numbers: Optional[List[str]] = []
    tracking_url: Optional[str] = None
    tracking_urls: Optional[List[str]] = []
    line_items: Optional[List[Optional[LineItemModel]]] = []

class Customer(BaseModel):
    id: int = None
    email: str = None
    first_name: str = None
    last_name: str = None
    phone: str = None


class ShippingLinesObject(BaseModel):
    code: str = None
    price: str = None
    discounted_price: str = None
    id: int = None


class DiscountCodes(BaseModel):
    code: str = None
    amount: float = None
    type: str = None


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
    shipping_address: Optional[ShippingAddress] = None
    billing_address: Optional[BillingAddressModel] = None
    customer: Optional[CustomerModel] = None
    line_items: Optional[List[Optional[LineItemModel]]] = []
    fulfillments: Optional[List[Optional[FulFillMent]]] = []
    customer: Optional[Customer] = None
    email: Optional[str] = None
    gateway: Optional[str] = None
    location_id: Optional[int] = None
    payment_gateway_names: Optional[List[str]] = None
    shipping_lines: Optional[List[ShippingLinesObject]] = None
    tags: Optional[str] = None
    taxes_include: Optional[bool] = None
    total_discounts: Optional[float] = None
    total_line_items_price: Optional[float] = None
    total_price: Optional[float] = None
    updated_at: Optional[str] = None
    discount_codes: Optional[List[DiscountCodes]] = None
