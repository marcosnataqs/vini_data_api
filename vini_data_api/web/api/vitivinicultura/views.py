from fastapi.routing import APIRouter

from vini_data_api.web.api.vitivinicultura.extractions.commercialization import (
    CommercializationExtraction,
)
from vini_data_api.web.api.vitivinicultura.extractions.exports import ExportExtraction
from vini_data_api.web.api.vitivinicultura.extractions.imports import ImportExtraction
from vini_data_api.web.api.vitivinicultura.extractions.processing import (
    ProcessingExtraction,
)
from vini_data_api.web.api.vitivinicultura.extractions.production import (
    ProductionExtraction,
)
from vini_data_api.web.api.vitivinicultura.schema import (
    CommercializationResponse,
    ExportResponse,
    ImportResponse,
    ProcessingResponse,
    ProductionResponse,
)

router = APIRouter()


@router.get("/productions/{year}", response_model=ProductionResponse)
async def get_productions(year: int) -> ProductionResponse:
    """
    Get productions.

    :param year: year to get productions.
    :returns: ProductionResponse.
    """
    pe = ProductionExtraction()
    response = pe.extract(year)
    return response


@router.get("/processings/{year}", response_model=ProcessingResponse)
async def get_processings(year: int) -> ProcessingResponse:
    """
    Get processing.

    :param year: year to get processing.
    :returns: ProcessingResponse.
    """
    pe = ProcessingExtraction()
    response = pe.extract(year)
    return response


@router.get("/commercializations/{year}", response_model=CommercializationResponse)
async def get_commercializations(year: int | None) -> CommercializationResponse:
    """
    Get commercialization.

    :param year: year to get commercialization.
    :returns: CommercializationResponse.
    """
    ce = CommercializationExtraction()
    response = ce.extract(year)
    return response

##Isso Aqui é Gambi só pra conseguir subir o codigo validar como adaptar mais tarde
@router.get("/commercializationsAll/")
async def get_commercializations():
    """
    Get commercialization.

    :param year: year to get commercialization.
    :returns: CommercializationResponse.
    """
    ce = CommercializationExtraction()
    response = ce.extract_history()
    return response


@router.get("/imports/{year}", response_model=ImportResponse)
async def get_imports(year: int) -> ImportResponse:
    """
    Get imports.

    :param year: year to get imports.
    :returns: ImportResponse.
    """
    ie = ImportExtraction()
    response = ie.extract(year)
    return response


@router.get("/exports/{year}", response_model=ExportResponse)
async def get_exports(year: int) -> ExportResponse:
    """
    Get exports.

    :param year: year to get exports.
    :returns: ExportResponse.
    """
    ee = ExportExtraction()
    response = ee.extract(year)
    return response
