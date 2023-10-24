


#Comandos usados para crear la base de datos y usuario.

    CREATE DATABASE virtualOATI;
    CREATE USER 'aoti'@'%' IDENTIFIED BY 'S3AHNcsD9Sxg9N';
    GRANT ALL PRIVILEGES ON virtualOATI.* TO 'aoti'@'%';
    FLUSH PRIVILEGES;

#Comandos para eliminar un usuario
    SELECT user FROM mysql.user WHERE user = 'aoti';
    DROP USER 'aoti'@'%';

#Comando para saber el usuario actual
    SELECT CURRENT_USER();
