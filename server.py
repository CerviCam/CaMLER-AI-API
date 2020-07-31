import os

from flask import Flask, jsonify, request
from dotenv import load_dotenv
import json
from io import BytesIO
from PIL import Image
import numpy as np

# Load local environment
load_dotenv()

# Initialize application
app = Flask(__name__)

def parse_bytes_to_json(data):
    return json.loads(data.decode('utf-8'))

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Unclassified image in numpy array. The size is M x N x 3, M: width, N: height, 3: Num of RGB channels
        image = np.array(Image.open(BytesIO(request.files['image'].read())))

        # TODO: Predict the image in here and return the result as a JSON response
        # This is a dummy JSON response, change it as you like.
        return jsonify({
            'is_positive': True, 
        })


if __name__ == '__main__':
    app.run(
        host=os.getenv('AI_API_HOST', '0.0.0.0'),
        port=os.getenv('AI_API_PORT', '2020'),
        debug=bool(int(os.getenv('DEBUG', 1)))
    )
