-- crea la base de datos. hbtn_0d_usa y la tabla cities
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
states_id INT FOREIGN KEY NOT NULL,
name VARCHAR(256) NOT NULL);