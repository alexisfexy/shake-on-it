import traceback
from fastapi import Request, Response
from fastapi.responses import JSONResponse
import logging
from common.config import ENV_LEVEL
from interfaces.error_response import ErrorResponse
from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse


# Not Found Middleware
async def not_found(request: Request, exc: HTTPException):
    if exc.status_code == 404:
        message = f"🔍 - Not Found - {request.url}"
        logging.warning(message)
        return JSONResponse(status_code=404, content={"message": message})
    return None  # Return None to let other exception handlers deal with other HTTPException cases


# Error Handler Middleware
async def error_handler(
    request: Request,
    exc: HTTPException,
):
    status_code = exc.status_code if exc.status_code != 200 else 500
    exc.status_code = status_code  # Hide internal codes
    stack = "🥞" if ENV_LEVEL == "production" else traceback.format_exc()
    return JSONResponse(
        status_code=status_code,
        content=ErrorResponse(message=str(exc), stack=stack).model_dump(),
    )
