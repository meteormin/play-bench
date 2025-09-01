import os
from dotenv import load_dotenv

load_dotenv()

USE_MODEL = os.getenv("MCP_MODEL", "gemini")  # openai | gemini
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")
GEMINI_API_KEY=os.getenv("GEMINI_API_KEY")
LANGUAGE=os.getenv("LANGUAGE")
