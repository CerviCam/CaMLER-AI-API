import os
import torch
import json
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
model_file_name = None
with open(os.path.join(AI_MODELS_PATH, '.config.json'), 'r') as config_file:
    config = json.load(config_file)
    model_file_name = config.pop("chosen")

if model_file_name != None:
    AI_MODEL = AIModel(
        model = torch.load(
            os.path.join(AI_MODELS_PATH, model_file_name),
            map_location=torch.device('cpu')
        ),
    )
else:
    AI_MODEL = None