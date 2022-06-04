from typing import Optional, List

from pydantic import BaseModel


class VariantOptionTitleModel(BaseModel):
    option1: Optional[str] = None
    option2: Optional[str] = None
    option3: Optional[str] = None


class PricesModel(BaseModel):
    currency_code: Optional[str] = None
    amount: Optional[float] = None


class PresentmentPriceModel(BaseModel):
    price: Optional[PricesModel] = {}
    compare_at_price: Optional[PricesModel] = {}


class PresentmentPricesModel(BaseModel):
    presentment_prices: Optional[List[PresentmentPriceModel]] = []


class ProductVariantModel(BaseModel):
    id: int
    barcode: Optional[str] = None
    compare_at_price: Optional[float] = None
    created_at: Optional[str] = None
    fulfillment_service: Optional[str] = None
    grams: Optional[int] = None
    image_id: Optional[int] = None
    inventory_item_id: Optional[int] = None
    inventory_management: Optional[str] = None
    inventory_policy: Optional[str] = None
    inventory_quantity: Optional[int] = None
    old_inventory_quantity: Optional[int] = None
    inventory_quantity_adjustment: Optional[int] = None
    option: Optional[VariantOptionTitleModel] = {}
    presentment_prices: Optional[PresentmentPricesModel] = {}
    position: Optional[int] = None
    price: Optional[float] = None
    product_id: Optional[int] = None
    requires_shipping: Optional[bool] = None
    sku: Optional[str] = None
    taxable: Optional[bool] = None
    tax_code: Optional[str] = None
    title: Optional[str] = None
    updated_at: Optional[str] = None
    weight: Optional[int] = None
    weight_unit: Optional[str] = None
