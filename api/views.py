from flask import request, jsonify
from io import BytesIO
from PIL import Image
import numpy as np
from project.setting import AI_MODEL

def predict():
    if request.method == 'POST':
        image = Image.open(BytesIO(request.files['image'].read()))
        return jsonify({
            'result': AI_MODEL.predict(image),
        })
