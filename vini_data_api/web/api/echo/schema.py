from typing import List

from pydantic import BaseModel


class Production(BaseModel):
    """Simple production model."""

    product: str
    qtd: int
    type: str


class ProductionResponse(BaseModel):
    """Simple production model."""

    productions: List[Production]
