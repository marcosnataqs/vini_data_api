from typing import List, Optional

from pydantic import BaseModel


class Production(BaseModel):
    """Production model."""

    product: str
    quantity: int
    type: Optional[str]


class ProductionResponse(BaseModel):
    """Production Response model."""

    productions: List[Production]


class Processing(BaseModel):
    """Processing model."""

    product: str
    quantity: int
    type: Optional[str]
    classification: str


class ProcessingResponse(BaseModel):
    """Processing Response model."""

    processings: List[Processing]


class Commercialization(BaseModel):
    """Commercialization model."""

    product: str
    quantity: int
    type: Optional[str]


class CommercializationResponse(BaseModel):
    """Commercialization Response model."""

    commercializations: List[Commercialization]


class Import(BaseModel):
    """Import model."""

    country: str
    quantity: int
    value: float
    classification: str


class ImportResponse(BaseModel):
    """Import Response model."""

    imports: List[Import]


class Export(BaseModel):
    """Export model."""

    country: str
    quantity: int
    value: float
    classification: str


class ExportResponse(BaseModel):
    """Export Response model."""

    exports: List[Export]
