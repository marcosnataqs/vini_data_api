from fastapi import APIRouter

from vini_data_api.web.api.echo.schema import Production, ProductionResponse

router = APIRouter()


@router.post("/", response_model=ProductionResponse)
async def send_echo_message() -> ProductionResponse:
    """
    Sends echo back to user.

    :param incoming_message: incoming message.
    :returns: message same as the incoming.
    """
    production = Production(product="product", qtd=1, type="type")
    response = ProductionResponse(productions=[production])
    return response
