import subprocess
import sys

def run_flask_app_on_startup():
    # Check if the script is running on Windows
    if sys.platform.startswith('win'):
        # Create a batch file to run the Flask app
        with open('run_flask_app.bat', 'w') as bat_file:
            bat_file.write('@echo off\n')
            bat_file.write('set FLASK_APP=backend.py\n')
            bat_file.write('flask run --host=127.0.0.1 --port=5000\n')

        # Add the batch file to Windows startup folder
        startup_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft\\Windows\\Start Menu\\Programs\\Startup')
        subprocess.run(f'copy run_flask_app.bat "{startup_folder}"', shell=True)

        print(f'Batch file created and added to startup folder: {startup_folder}')

# Call the function to set up the Flask app to run on startup
run_flask_app_on_startup()

