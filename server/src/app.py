from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from dotenv import load_dotenv
import uvicorn
import logging
import os

from api import api
from middlewares import not_found, error_handler
from db import start

load_dotenv()

# Create FastAPI app instance
app = FastAPI()

# Configure logging
logging.basicConfig(level=logging.INFO)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with specific origins as needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Example route for testing
@app.get("/", response_model=dict)
async def hello_world():
    return {"message": "Hello World!"}

# API routes
app.include_router(api, prefix="/api/v1")


# Starting the database connection
if __name__ == "__main__":
    start()
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 5000)))
