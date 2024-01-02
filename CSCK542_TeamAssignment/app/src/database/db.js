const mysql = require('mysql2');
const dotenv = require('dotenv');

dotenv.config();

try {
  const pool = mysql.createPool({
    host: process.env.DB_HOST,
    user: process.env.DB_USER,
    password: process.env.DB_PASSWORD,
    database: process.env.DB_NAME,
    port: process.env.DB_PORT
  });

  console.log('SQL Connection pool created');

  module.exports = pool.promise();
} catch (error) {
  console.error('Error creating SQL connection pool:', error.message);
  process.exit(1); // Exit the process with an error code
}