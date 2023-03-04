from typing import List, Dict, Any

from pydantic import BaseModel


class SkuModel(BaseModel):
    id: int
    name: str
    brand: str
