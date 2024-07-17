from typing import Optional
from src.interfaces.message_response import MessageResponse


class ErrorResponse(MessageResponse):
    stack: Optional[str] = None

    # TODO: check on intention with this
