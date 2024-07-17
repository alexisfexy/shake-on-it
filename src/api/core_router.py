from fastapi import APIRouter

from src.api.sports import sports_router

api = APIRouter()
api.include_router(sports_router, prefix="/sports")
