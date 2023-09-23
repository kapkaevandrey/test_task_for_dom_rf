from fastapi import APIRouter

from app.api.endpoints import cadastr_router

main_router = APIRouter()
main_router.include_router(cadastr_router, tags=["Operations with cadastr data"])
