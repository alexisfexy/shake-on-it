from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from api.core_router import api
import uvicorn
import logging
import os

from db import start
from middlewares import not_found, error_handler

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

app.add_exception_handler(404, not_found)  # type: ignore
app.add_exception_handler(HTTPException, error_handler)  # type: ignore
app.include_router(api, prefix="/api/v1")


@app.get("/", response_model=dict)
async def root():
    return {"message": "Hello World!"}


if __name__ == "__main__":
    start()
    port = int(os.getenv("PORT", 5000))
    uvicorn.run(app)  # , host="0.0.0.0", port=port)
    print(f"Listening: http://localhost:{port}")
