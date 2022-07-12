from typing import Optional, List
from pydantic import BaseModel


class UsageRecordModel(BaseModel):
    is_error: bool = False
    status_code: int = None
