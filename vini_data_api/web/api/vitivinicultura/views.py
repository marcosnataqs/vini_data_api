from fastapi import Depends
from fastapi.routing import APIRouter

from vini_data_api.db.models.users import User, current_active_user
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
from vini_data_api.web.utils.utils import YearRangeValidation

router = APIRouter()


@router.get("/productions/{year}", response_model=ProductionResponse)
async def get_productions(
    year: int,
    _user: User = Depends(current_active_user),
) -> ProductionResponse:
    """
    Get productions.

    :param year: year to get productions.
    :returns: ProductionResponse.
    """
    YearRangeValidation(year=year)
    pe = ProductionExtraction()
    response = pe.extract(year)
    return response


@router.get("/processings/{year}", response_model=ProcessingResponse)
async def get_processings(
    year: int,
    _user: User = Depends(current_active_user),
) -> ProcessingResponse:
    """
    Get processing.

    :param year: year to get processing.
    :returns: ProcessingResponse.
    """
    YearRangeValidation(year=year)
    pe = ProcessingExtraction()
    response = pe.extract(year)
    return response


@router.get("/commercializations/{year}", response_model=CommercializationResponse)
async def get_commercializations(
    year: int,
    _user: User = Depends(current_active_user),
) -> CommercializationResponse:
    """
    Get commercialization.

    :param year: year to get commercialization.
    :returns: CommercializationResponse.
    """
    YearRangeValidation(year=year)
    ce = CommercializationExtraction()
    response = ce.extract(year)
    return response


@router.get("/imports/{year}", response_model=ImportResponse)
async def get_imports(
    year: int,
    _user: User = Depends(current_active_user),
) -> ImportResponse:
    """
    Get imports.

    :param year: year to get imports.
    :returns: ImportResponse.
    """
    YearRangeValidation(year=year)
    ie = ImportExtraction()
    response = ie.extract(year)
    return response


@router.get("/exports/{year}", response_model=ExportResponse)
async def get_exports(
    year: int,
    _user: User = Depends(current_active_user),
) -> ExportResponse:
    """
    Get exports.

    :param year: year to get exports.
    :returns: ExportResponse.
    """
    YearRangeValidation(year=year)
    ee = ExportExtraction()
    response = ee.extract(year)
    return response
