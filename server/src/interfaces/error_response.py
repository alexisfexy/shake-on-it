from typing import Optional
from server.src.interfaces.message_response import MessageResponse


class ErrorResponse(MessageResponse):
    stack: Optional[str] = None