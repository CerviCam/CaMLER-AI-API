import os
from dotenv import load_dotenv

# Load local environment
load_dotenv()

HOST = os.getenv('AI_API_HOST', '0.0.0.0')
PORT = os.getenv('AI_API_PORT', '2020')
DEBUG = bool(int(os.getenv('DEBUG', 1)))