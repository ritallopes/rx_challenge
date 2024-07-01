from fastapi import APIRouter

from app.api.v1.endpoints.equipments import router as equipments_router
from app.api.v1.endpoints.equipments_data import router as equipments_data_router
from app.api.v1.endpoints.token import router as token_router
from app.api.v1.endpoints.upload import router as upload_router
from app.api.v1.endpoints.users import router as users_router

api_router = APIRouter()

api_router.include_router(users_router)
api_router.include_router(equipments_router)
api_router.include_router(equipments_data_router)
api_router.include_router(upload_router)
api_router.include_router(token_router)
