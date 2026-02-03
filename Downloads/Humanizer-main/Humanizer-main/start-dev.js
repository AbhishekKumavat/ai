const { spawn } = require('child_process');
const path = require('path');

console.log('🚀 Starting Humanizer Development Environment...');

// Start backend server
const backend = spawn('python', ['main.py'], {
  cwd: path.join(__dirname, '..'),
  stdio: 'inherit'
});

// Start frontend server
const frontend = spawn('npm', ['run', 'dev'], {
  cwd: path.join(__dirname, '..', 'frontend'),
  stdio: 'inherit'
});

// Handle process termination
process.on('SIGINT', () => {
  console.log('\n🛑 Shutting down servers...');
  backend.kill();
  frontend.kill();
  process.exit(0);
});

backend.on('error', (error) => {
  console.error('Backend error:', error);
});

frontend.on('error', (error) => {
  console.error('Frontend error:', error);
});

console.log('✅ Both servers started successfully!');
console.log('Frontend: http://localhost:5173');
console.log('Backend: http://localhost:8080');