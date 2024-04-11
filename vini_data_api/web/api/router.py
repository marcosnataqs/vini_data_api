from fastapi.routing import APIRouter

from vini_data_api.web.api import monitoring, users, vitivinicultura

api_router = APIRouter()
api_router.include_router(monitoring.router)
api_router.include_router(users.router)
api_router.include_router(
    vitivinicultura.router,
    prefix="/vitivinicultura",
    tags=["Vitivinicultura"],
)
