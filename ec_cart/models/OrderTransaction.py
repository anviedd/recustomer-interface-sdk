from typing import Optional

from pydantic import BaseModel


class PaymentDetails(BaseModel):
    credit_card_bin: Optional[str] = None
    avs_result_code: Optional[str] = None
    cvv_result_code: Optional[str] = None
    credit_card_number: Optional[str] = None
    credit_card_company: Optional[str] = None


class PaymentsRefundAttributes(BaseModel):
    status: Optional[str] = None
    acquirer_reference_number: Optional[str] = None


class CurrencyExchangeAdjustment(BaseModel):
    id: Optional[int] = None
    adjustment: Optional[str] = None
    original_amount: Optional[str] = None
    final_amount: Optional[str] = None
    currency: Optional[str] = None


class OrderTransactionModel(BaseModel):
    id: Optional[int] = None
    order_id: Optional[int] = None
    kind: Optional[str] = None
    gateway: Optional[str] = None
    status: Optional[str] = None
    message: Optional[str] = None
    created_at: Optional[str] = None
    test: Optional[bool] = None
    authorization: Optional[str] = None
    location_id: Optional[str] = None
    user_id: Optional[int] = None
    parent_id: Optional[int] = None
    processed_at: Optional[str] = None
    device_id: Optional[int] = None
    error_code: Optional[str] = None
    source_name: Optional[str] = None
    payment_details: Optional[PaymentDetails] = {}
    currency_exchange_adjustment: Optional[CurrencyExchangeAdjustment] = {}
    payments_refund_attributes: Optional[PaymentsRefundAttributes] = {}
    amount: Optional[str] = None
    currency: Optional[str] = None
    authorization_expires_at: Optional[str] = None
