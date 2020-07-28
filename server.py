import os

from flask import Flask, jsonify, request
from dotenv import load_dotenv
import json

# Load local environment
load_dotenv()

# Initialize application
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        body = json.loads(request.get_data().decode('utf-8'))
        print(body['image_url'])

        # TODO: Integrate an AI model in here and return the result as a JSON response
        # This is a dummy response, change it as you like.
        return jsonify({
            'is_positive': True, 
        })


if __name__ == '__main__':
    app.run(
        host=os.getenv('AI_API_HOST', '0.0.0.0'),
        port=os.getenv('AI_API_PORT', '2020'),
    )
