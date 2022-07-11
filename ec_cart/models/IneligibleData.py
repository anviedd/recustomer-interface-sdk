from typing import Optional, Dict

from pydantic import BaseModel


class IneligibleDataModel(BaseModel):
    data: Optional[Dict[str, Optional[str]]] = None
