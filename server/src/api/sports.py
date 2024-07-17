from typing import List
from fastapi import APIRouter


router = APIRouter()

SportsResponse = List[str]

@router.get("/", response_model=SportsResponse)
def get_sports():
    return ["football", "basketball", "baseball"]