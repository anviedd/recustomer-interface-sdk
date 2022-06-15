from typing import Optional, List

from pydantic import BaseModel


class WebhookModel(BaseModel):
    id: Optional[int] = None
    address: Optional[str] = None
    api_version: Optional[str] = None
    fields: Optional[List[Optional[str]]] = []
    format: Optional[str] = None
    topic: Optional[str] = None
    updated_at: Optional[str] = None
    metafield_namespaces: Optional[List[Optional[str]]] = []
    private_metafield_namespaces: Optional[List[Optional[str]]] = []
