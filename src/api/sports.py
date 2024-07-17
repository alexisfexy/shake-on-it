from typing import List
from fastapi import APIRouter, HTTPException

SportsResponse = List[str]

sports_router = APIRouter(tags=["sports"])


@sports_router.get("/", response_model=SportsResponse)
def get_sports():
    # raise HTTPException(status_code=200, detail="no thank you") ## Testing Middleware
    return ["football", "basketball", "baseball"]
