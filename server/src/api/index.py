import os
from fastapi import FastAPI
from sports import router as sports_router

app = FastAPI()

app.include_router(sports_router, prefix="/sports")