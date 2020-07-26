import os

from flask import Flask, jsonify, request
from dotenv import load_dotenv
from skimage import io

# Load local environment
load_dotenv()

# Initialize application
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        body = request.json
        print(body)
        image = io.imread(body['image_url'])
        print(image)
        # TODO: Use AI model prediction and return the result as a JSON response
        # This is a dummy response, change it as you like.
        return jsonify({
            'is_positive': True, 
        })


if __name__ == '__main__':
    app.run(
        host=os.getenv('AI_API_HOST', '0.0.0.0'),
        port=os.getenv('AI_API_PORT', '2020'),
    )
