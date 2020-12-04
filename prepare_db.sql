CREATE DATABASE IF NOT EXISTS test_db;
CREATE USER IF NOT EXISTS 'kuchkr'@'localhost' IDENTIFIED BY 'g32cy2hg';
GRANT ALL PRIVILEGES ON test_db.* TO 'kuchkr'@'localhost';
FLUSH PRIVILEGES;

SHOW DATABASES;
SHOW GRANTS FOR 'kuchkr'@'localhost';
