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
state_file_name = (list(filter(
    lambda x: x.startswith("chosen"),
    os.listdir(AI_MODELS_PATH)
)) + [None])[0]

if state_file_name != None:
    model = models.resnext101_32x8d(pretrained=True)
    AI_MODEL = AIModel(
        model = models.resnext101_32x8d(pretrained=True),
        state_path = os.path.join(AI_MODELS_PATH, state_file_name),
        fc_size = 2048,
        classes = [
            {
                "code": 0,
                "label": 'Negatif',
            },
            {
                "code": 1,
                "label": 'Positif',
            }
        ],
    )