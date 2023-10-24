


#Comandos usados para crear la base de datos y usuario.

    CREATE DATABASE 'virtual-OATI';
    CREATE USER 'aoti'@'%' IDENTIFIED BY 'S3AHNcsD9Sxg9N';
    GRANT ALL PRIVILEGES ON 'virtual-OATI'.* TO 'oati'@'%';
    FLUSH PRIVILEGES;
