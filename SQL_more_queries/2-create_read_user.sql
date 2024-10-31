-- Crea la base de datos
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- crea el usuario con la indientifacion 
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- Otorga los privilegios
GRANT SELECT ON hbtn_0d_2.* 'user_0d_2'@'localhost'; 