-- Sets up my database
-- Configures and grants necessary privileges

CREATE DATABASE IF NOT EXISTS holberton;
CREATE USER IF NOT EXISTS 'root'@'localhost' IDENTIFIED BY '';
GRANT ALL PRIVILEGES ON 'holberton'.* TO 'root'@'localhost';

USE holberton;

DROP TABLE IF EXISTS 'users';
CREATE TABLE users (
    email VARCHAR(255)
);

INSERT INTO users(email) VALUES ("egbuniwecemeka@gmail.com");
INSERT INTO users(email) VALUES ("uchep@gmail.com")
