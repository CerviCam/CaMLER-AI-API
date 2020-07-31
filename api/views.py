from flask import request, jsonify
from io import BytesIO
from PIL import Image
import numpy as np

def predict():
    if request.method == 'POST':
        # Unclassified image in numpy array. The size is M x N x 3, M: width, N: height, 3: Num of RGB channels
        image = np.array(Image.open(BytesIO(request.files['image'].read())))

        # TODO: Predict the image in here and return the result as a JSON response
        # This is a dummy JSON response, change it as you like.
        return jsonify({
            'is_positive': True,
        })
