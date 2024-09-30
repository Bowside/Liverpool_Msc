const express = require('express');
const apiRoutes = require('./routes/api.js');
const dotenv = require('dotenv');

dotenv.config();

const app = express();
const PORT = process.env.PORT;

// Middleware
app.use(express.json());

// Routes
app.use('/api', apiRoutes);

// Server startup
const server = app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});

// Error handling for server startup
server.on('error', (error) => {
  console.error('Error starting the server:', error.message);
  process.exit(1); // Exit the process with an error code
});

// Graceful shutdown
process.on('SIGINT', () => {
  console.log('Server is shutting down...');
  server.close(() => {
    console.log('Server has been shut down.');
    process.exit(0); // Exit the process gracefully
  });
});