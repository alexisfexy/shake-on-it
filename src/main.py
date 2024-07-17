from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from src.api.core_router import api
import uvicorn
import logging
import os

from db import start

load_dotenv()
app = FastAPI(prefix="/api/v1")
logging.basicConfig(level=logging.INFO)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with specific origins as needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api, prefix="/api/v1")


@app.get("/", response_model=dict)
async def root():
    return {"message": "Hello World!"}


if __name__ == "__main__":
    start()
    port = int(os.getenv("PORT", 5000))
    uvicorn.run(app)  # , host="0.0.0.0", port=port)
    print(f"Listening: http://localhost:{port}")
