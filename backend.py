from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

DATA_PATH = 'DATA'
# Dummy function to simulate search
def search_images(search_term):
    print('ok')
    image_paths = []
    for root, dirs, files in os.walk(DATA_PATH):
        for file in files:
            if search_term.lower() in file.lower():
                image_paths.append(os.path.join(root, file))
    return image_paths

@app.route('/search')
def search():
    search_term = request.args.get('q', '')
    image_urls = search_images(search_term)
    print(image_urls)
    print(jsonify(image_urls))
    return jsonify(image_urls)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
