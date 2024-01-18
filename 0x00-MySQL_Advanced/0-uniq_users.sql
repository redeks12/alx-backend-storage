-- Write a SQL script that creates a table users following these requirements:
DROP TABLE IF EXISTS users;
CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, email VARCHAR(255) UNIQUE NOT NULL, name VARCHAR(255) NOT NULL);

