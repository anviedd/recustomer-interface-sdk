from typing import Optional

from pydantic import BaseModel


class ScriptTagModel(BaseModel):
    id: Optional[int] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    cache: Optional[bool] = False
    display_scope: Optional[str] = None
    src: str
    event: str
