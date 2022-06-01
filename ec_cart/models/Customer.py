from typing import Optional

from pydantic import BaseModel

from ec_cart.models.DefaultAddress import DefaultAddressModel


class CustomerModel(BaseModel):
    id: int = None
    email: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    note: Optional[str] = None
    verified_email: bool
    phone: Optional[str] = None
    tags: Optional[str] = None
    addresses: Optional[str] = None
    default_address: Optional[DefaultAddressModel] = None
