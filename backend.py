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


    # import subprocess
    # import sys

    # def run_flask_app_on_startup():
    #     # Check if the script is running on Windows
    #     if sys.platform.startswith('win'):
    #         # Create a batch file to run the Flask app
    #         with open('run_flask_app.bat', 'w') as bat_file:
    #             bat_file.write('@echo off\n')
    #             bat_file.write('set FLASK_APP=backend.py\n')
    #             bat_file.write('flask run --host=127.0.0.1 --port=5000\n')

    #         # Add the batch file to Windows startup folder
    #         startup_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft\\Windows\\Start Menu\\Programs\\Startup')
    #         subprocess.run(f'copy run_flask_app.bat "{startup_folder}"', shell=True)

    #         print(f'Batch file created and added to startup folder: {startup_folder}')

    # # Call the function to set up the Flask app to run on startup
    # run_flask_app_on_startup()

