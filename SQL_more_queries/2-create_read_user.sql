-- Crea la base de datos
CREATE DATABASE hbtn_0d_2;
-- crea el usuario con la indientifacion 
CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- Otorga los privilegios
SELECT GRANTS ON hbtn_0d_2 * 'user_0d_1@localhost';