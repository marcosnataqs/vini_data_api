from fastapi import HTTPException, status

from vini_data_api.web.api.vitivinicultura.schema import ValidateYear


def YearRangeValidation(year: int) -> None:
    try:
        year = ValidateYear(year=year)
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid year",
        )
