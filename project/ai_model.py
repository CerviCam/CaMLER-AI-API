import torch
import torchvision.transforms as transforms
import torch.nn.functional as F
from torch import nn
import io

class AIModel:
    def __init__(self, model):
        self.model = model
        # Buat ngecek ada GPU atau ngga
        # run_on_gpu = torch.cuda.is_available()
        # if run_on_gpu:
        #   resnet.cuda()
        self.model.eval()

    def __transform_image(self, image):
        # ResNet ga perlu diubah/rescale karena bisa nerima beragam ukuran gambar
        # ResNet punya adaptive average pool 
        transformer = transforms.Compose([
            transforms.Resize((299, 299)),
            transforms.ToTensor(),
            transforms.Normalize(
                [0.485, 0.456, 0.406],
                [0.299, 0.224, 0.225]
            )
        ])
        return transformer(image).unsqueeze(0)

    def predict(self, image):
        # torch.cuda.empty_cache() # If and only if the cuda is available
        tensor = self.__transform_image(image)
        outputs = self.model.forward(tensor)
        # outputs = resnet.forward(tensor.cuda()) # Jika pakai GPU
        _, result = outputs.max(1)
        probability = torch.max(F.softmax(outputs, 1)).item()
        result_idx = result.item()
        # Untuk melihat kelas dan probabilitasnya
        # for res in outputs:
        #     pr = F.softmax(res)
        #     for idx, prob in enumerate(pr):
        #         print(imagenet_classes[str(idx)][1], ' ', prob.item())
        return result_idx, probability