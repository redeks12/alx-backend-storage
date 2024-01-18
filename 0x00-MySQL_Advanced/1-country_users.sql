-- Write a SQL script that creates a table users following these requirements:
DROP TABLE IF EXISTS users;
CREATE TABLE users (id INTEGER PRIMARY KEY AUTO_INCREMENT, email VARCHAR(255) NOT NULL UNIQUE, name VARCHAR(255), country VARCHAR(20) ENUM ('US', 'CO', 'TN') NOT NULL)
