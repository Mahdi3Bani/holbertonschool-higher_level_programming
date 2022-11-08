-- create a new database and a new user
CREATE DATABASE hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_2' @'localhost';
