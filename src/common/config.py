import os
from tkinter import E
from typing import Optional
from dotenv import load_dotenv

load_dotenv()
ENV_LEVEL: Optional[str] = os.environ.get("ENV")
if not ENV_LEVEL:
    raise Exception("no variable found")
