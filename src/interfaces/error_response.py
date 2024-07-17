from typing import Optional
from interfaces.message_response import MessageResponse


class ErrorResponse(MessageResponse):
    stack: Optional[str] = None
