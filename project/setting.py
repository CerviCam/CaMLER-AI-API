import os
import torch
from dotenv import load_dotenv
import torchvision.models as models
from project.ai_model import AIModel

# Load local environment
load_dotenv()

HOST = os.getenv('AI_API_HOST', '0.0.0.0')
PORT = os.getenv('AI_API_PORT', '2020')
DEBUG = bool(int(os.getenv('DEBUG', 1)))

STORAGE_PATH = os.getenv('STORAGE_PATH', '/storage/')
AI_MODELS_PATH = os.path.join(STORAGE_PATH, "models/")

# Setup AI model
model_file_name = (list(filter( 
    lambda x: x.startswith("chosen"),
    os.listdir(AI_MODELS_PATH)
)) + [None])[0]

if model_file_name != None:
    AI_MODEL = AIModel(
        model = torch.load(
            os.path.join(AI_MODELS_PATH, model_file_name),
            map_location=torch.device('cpu')
        ),
    )
else:
    AI_MODEL = None