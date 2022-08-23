from typing import Optional
from pydantic import BaseModel


class ShopMoney(BaseModel):
    amount: Optional[str] = None
    currency_code: Optional[str] = None


class PriceSet(BaseModel):
    shop_money: Optional[ShopMoney] = None


class LineItemModel(BaseModel):
    id: int = None
    admin_graphql_api_id: Optional[str] = None
    grams: Optional[int] = None
    name: Optional[str] = None
    price: Optional[str] = None
    product_exists: Optional[bool] = None
    product_id: Optional[int] = None
    quantity: Optional[int] = None
    requires_shipping: Optional[bool] = None
    sku: Optional[str] = None
    title: Optional[str] = None
    total_discount: Optional[str] = None
    variant_id: Optional[int] = None
    variant_title: Optional[str] = None
    fulfillment_status: Optional[str] = None
    product_name: Optional[str] = None
    fulfillable_quantity: Optional[int] = None
    vendor: Optional[str] = None
    price_set: Optional[PriceSet] = None

    # return & cancelの処理内でパラメータをセットする
    cancel_deadline: Optional[bool] = None
    discounted_product: Optional[bool] = None
    sku_product: Optional[bool] = None
    discounted_code: Optional[bool] = None
    excluded_collection: Optional[bool] = None
    excluded_type: Optional[bool] = None
    excluded_order_tag: Optional[bool] = None
    excluded_tag: Optional[bool] = None
    excluded_customize: Optional[bool] = None
    partial_cancel_off: Optional[bool] = None
    partial_no_order: Optional[bool] = None
    options: Optional[dict] = None
    images: Optional[str] = None
    order_id: Optional[int] = None
    order_name: Optional[str] = None
    line_item_id: Optional[int] = None
    quantity_total: Optional[int] = None
    quantity: Optional[int] = None
    province_code: Optional[str] = None
    return_deadline: Optional[bool] = None
    discounted_product: Optional[bool] = None
    discounted_code: Optional[bool] = None
    excluded_sku: Optional[bool] = None
    excluded_collection: Optional[bool] = None
    excluded_type: Optional[bool] = None
    excluded_order_tag: Optional[bool] = None
    excluded_tag: Optional[bool] = None
    excluded_customize: Optional[bool] = None
