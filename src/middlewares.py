import traceback
from fastapi import Request, Response, HTTPException
from fastapi.responses import JSONResponse
import logging
from src.common.config import ENV_LEVEL

# Define logging configuration
logging.basicConfig(level=logging.INFO)


# Not Found Middleware
@app.exception_handler(HTTPException)  # type: ignore
async def not_found(request: Request, exc: HTTPException):
    if exc.status_code == 404:
        message = f"🔍 - Not Found - {request.url}"
        logging.warning(message)
        raise JSONResponse(status_code=404, content={"message": message})
    return None  # Return None to let other exception handlers deal with other HTTPException cases # TODO: test


# Error Handler Middleware
@app.exception_handler(Exception)  # type: ignore
async def error_handler(request: Request, response: Response, exc: Exception):
    status_code = response.status_code if response.status_code != 200 else 500
    stack = "🥞" if ENV_LEVEL == "production" else traceback.format_exc()
    return JSONResponse(
        status_code=status_code, content={"message": str(exc), "stack": stack}
    )
