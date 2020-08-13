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

# Setup AI model
model = models.resnext101_32x8d(pretrained=True)
AI_MODEL = AIModel(
    model = models.resnext101_32x8d(pretrained=True),
    state_path = STORAGE_PATH + "models/" + "main_model.pt",
    fc_size = 2048,
    classes = ['Negatif', 'Positif'],
)