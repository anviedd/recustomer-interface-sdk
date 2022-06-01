from typing import Optional

from pydantic import BaseModel


class BillingAddressModel(BaseModel):
    company: Optional[str] = None
    address1: Optional[str] = None
    address2: Optional[str] = None
    city: Optional[str] = None
    province: Optional[str] = None
    country: Optional[str] = None
    zip: Optional[str] = None
    phone: Optional[str] = None
    name: Optional[str] = None
    province_code: Optional[str] = None
    country_code: Optional[str] = None
    country_name: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
