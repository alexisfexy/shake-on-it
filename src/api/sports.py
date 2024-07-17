from typing import List
from fastapi import APIRouter

SportsResponse = List[str]

sports_router = APIRouter(tags=["sports"])


@sports_router.get("/", response_model=SportsResponse)
def get_sports():
    return ["football", "basketball", "baseball"]
