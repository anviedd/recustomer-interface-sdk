from typing import Optional, List
from pydantic import BaseModel


class SubscriptionCreateModel(BaseModel):
    redirect_url: str = None
    charge_id: str = None
    line_item_id: str = None


class SubscriptionCancelModel(BaseModel):
    result: bool = False
