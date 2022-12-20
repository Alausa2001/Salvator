-- creates a db for Salvator
-- creates a user and password
-- grants permission on salvator_db

-- SET GLOBAL validate_password.policy=LOW;
CREATE DATABASE IF NOT EXISTS salvator_db;
CREATE USER IF NOT EXISTS 'salvator'@'localhost' IDENTIFIED BY 'salvator_v1.0';
GRANT ALL PRIVILEGES ON salvator_db.* TO 'salvator'@'localhost';
GRANT SELECT ON performance_schema.* TO 'salvator'@'localhost';
FLUSH PRIVILEGES;
