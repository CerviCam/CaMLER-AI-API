from flask import request, jsonify
from io import BytesIO
from PIL import Image
import numpy as np
from project.setting import AI_MODEL
from flask_api import status

def predict():
    if request.method == 'POST':
        if AI_MODEL == None:
            return (None, status.HTTP_503_SERVICE_UNAVAILABLE)
        else:
            image = Image.open(BytesIO(request.files['image'].read()))
            _class, proba = AI_MODEL.predict(image)
            return (
                jsonify({
                    'class': _class,
                    'proba': proba,
                }), 
                status.HTTP_200_OK
            )

