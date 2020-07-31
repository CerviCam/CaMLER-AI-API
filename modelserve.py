import torch
import torchvision.models as models
import torchvision.transforms as transforms
import torch.nn.functional as F
import os
import requests
import json
import io
from PIL import Image

import pprint

pp = pprint.PrettyPrinter(indent=4)

if not(os.path.exists('./image_class_index.json')):
        print('ImageNet class is not found')
        r = requests.get('https://s3.amazonaws.com/deep-learning-models/image-models/imagenet_class_index.json')
        open('./image_class_index.json', 'wb').write(r.content)
        print('File saved!')
imagenet_classes = json.load(open('./image_class_index.json'))

resnet = models.resnet18(pretrained=True)
# Buat ngecek ada GPU atau ngga
# run_on_gpu = torch.cuda.is_available()
# if run_on_gpu:
#   resnet.cuda()
resnet.eval()



def transform_image(image_bytes):
    # ResNet ga perlu diubah/rescale karena bisa nerima beragam ukuran gambar
    # ResNet punya adaptive average pool 
    transformer = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize(
            [0.485, 0.456, 0.406],
            [0.299, 0.224, 0.225]
            )
        ])
    image = Image.open(io.BytesIO(image_bytes))
    return transformer(image).unsqueeze(0)

def get_prediction(image_bytes):
    torch.cuda.empty_cache()
    tensor = transform_image(image_bytes)
    outputs = resnet.forward(tensor)
    # outputs = resnet.forward(tensor.cuda()) # Jika pakai GPU
    _, result = outputs.max(1)
    probability = torch.max(F.softmax(outputs, 1)).item()
    result_idx = str(result.item())
    # Untuk melihat kelas dan probabilitasnya
    # for res in outputs:
    #     pr = F.softmax(res)
    #     for idx, prob in enumerate(pr):
    #         print(imagenet_classes[str(idx)][1], ' ', prob.item())
    return imagenet_classes[result_idx], probability

