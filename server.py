import os

from flask import Flask, jsonify, request
# from dotenv import load_dotenv
import json

import modelserve

# Load local environment
# load_dotenv()

# Initialize application
app = Flask(__name__)

# TODO: Change to production-ready. More: https://flask.palletsprojects.com/en/1.1.x/tutorial/deploy/

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # body = json.loads(request.get_data().decode('utf-8'))
        # print(body['image_url'])

        file = request.files['file']
        img_bytes = file.read()
        (class_id, class_name), probability = modelserve.get_prediction(img_bytes)

        # TODO: Integrate an AI model in here and return the result as a JSON response
        # This is a dummy response, change it as you like.
        # return jsonify({
        #     'is_positive': True, 
        # }) 
        return jsonify({'class_id': class_id, 'class_name':class_name, 'probability': probability}) 


if __name__ == '__main__':
    app.run(
        host=os.getenv('AI_API_HOST', '0.0.0.0'),
        port=os.getenv('AI_API_PORT', '2020'),
    )
