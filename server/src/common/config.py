import os
from dotenv import load_dotenv

load_dotenv()
ENV_LEVEL: str = os.environ.get("ENV", None)