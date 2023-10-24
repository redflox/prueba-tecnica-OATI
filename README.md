# DATOS PERSONALES
- NOMBRE: Bryan Felipe Muñoz Molina
- CORREO: swsbmm@gmail.com

## Documentacion de la prueba

La documentacion de la prueba esta en el directorio "back".

## Alcances

- back: 100%
- front: 50%
- deploy: 100%
- database: 100%

### Comandos usados para crear la base de datos y usuario.

    CREATE DATABASE virtualOATI;
    CREATE USER 'aoti'@'%' IDENTIFIED BY 'S3AHNcsD9Sxg9N';
    GRANT ALL PRIVILEGES ON virtualOATI.* TO 'aoti'@'%';
    FLUSH PRIVILEGES;

    #Comandos para eliminar un usuario
    SELECT user FROM mysql.user WHERE user = 'aoti';
    DROP USER 'aoti'@'%';

    #Comando para saber el usuario actual
    SELECT CURRENT_USER();
