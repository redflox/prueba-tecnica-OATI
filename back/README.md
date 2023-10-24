# Sistema de Tutoriales para Aprendizaje Virtual

Un sistema de gestión de tutoriales con detalles específicos, construido con FastAPI y MySQL.

## Despliegue con Docker

Para garantizar un despliegue consistente y libre de problemas en cualquier entorno, esta aplicación ha sido contenerizada utilizando Docker. Esto facilita su despliegue, escalabilidad y gestión.

### URL de la Aplicación

La aplicación está desplegada y puede ser accedida en la siguiente dirección:

[https://oati-back.redflox.com/docs](https://oati-back.redflox.com/docs)

Desde esta URL, podrás acceder a la documentación generada por FastAPI y probar los endpoints de la aplicación directamente desde el navegador.


## Stack Tecnológico

- **Backend**: FastAPI
- **Base de datos**: MySQL
- **ORM**: SQLAlchemy


## Instrucciones de Instalación

1. **Clonar el Repositorio**:
   ```bash
   git clone [URL-del-repositorio.git]

2. **Crear entorno virtual**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows usar: venv\Scripts\activate

3. **Instalar dependencias**
    ```bash
    pip install -r requirements.txt

4. **Configurar base de datos**

    Tener MySQL instalado y en funcionamiento. Crear una base de datos para el proyecto.
    ```bash
    #Comandos usados para crear la base de datos y usuario.
    CREATE DATABASE virtualOATI;
    CREATE USER 'your_username'@'%' IDENTIFIED BY 'your_password';
    GRANT ALL PRIVILEGES ON virtualOATI.* TO 'your_username'@'%';
    FLUSH PRIVILEGES;

    #Comandos para eliminar un usuario
    SELECT user FROM mysql.user WHERE user = 'your_username';
    DROP USER 'your_username'@'%';

    #Comando para saber el usuario actual
    SELECT CURRENT_USER();


5. **Configurar variables de entorno**

    Para configurar las variables de entorno

    1. Navega hasta la carpeta `app`.
    2. Crea un fichero llamado `.env`.
    3. Dentro de este archivo, añade la siguiente variable de entorno:

    ```plaintext
    DATABASE_URL=su_cadena_de_conexion_aqui

6. **Ejecutar la aplicacion**

    ```bash
    uvicorn main:app --reload

## Estructura del proyecto

    ```plaintext
    /app
    |-- /core
    |   |-- config.py
    |-- /database
    |   |-- create_database.py
    |   |-- database.py
    |-- /models
    |   |-- tutorial_model.py
    |   |-- tutorial_detail_model.py
    |-- /schemas
    |   |-- tutorial_schema.py
    |   |-- tutorial_detail_schema.py
    |   |-- response_schema.py
    |-- /services
    |   |-- tutorial_service.py
    |   |-- tutorial_detail_service.py
    |   |-- exeption.py
    |-- /routers
    |   |-- tutorial_router.py
    |   |-- tutorial_detail_router.py
    |-- main.py
    |-- requirements.txt


## Modelo de datos

### Tutorial

- **id**: Integer (Primary Key)
- **title**: String (máximo 150 caracteres)
- **description**: String (máximo 1000 caracteres)
- **state**: Boolean
- **detail_id**: ForeignKey (apunta a `TutorialDetail`)

### TutorialDetail

- **id**: Integer (Primary Key)
- **creation_date**: Date
- **creator_user**: String (máximo 250 caracteres)

Cada `Tutorial` tiene una relación uno a uno con `TutorialDetail`.

## Funcionamiento imagenes

![swagger](https://retos.redflox.com/oati-prueba/endpoints.png)
![swagger](https://retos.redflox.com/oati-prueba/todos_los_tutoriales_con_detalle.png)
![swagger](https://retos.redflox.com/oati-prueba/todos_los_tutoriales_con_detalle_response.png)

![swagger](https://retos.redflox.com/oati-prueba/create_tutorial_with_details.png)

![swagger](https://retos.redflox.com/oati-prueba/create_tutorial_with_details_response.png)

![swagger](https://retos.redflox.com/oati-prueba/read_tutorial.png)

![swagger](https://retos.redflox.com/oati-prueba/read_tutorial_response.png)

![swagger](https://retos.redflox.com/oati-prueba/update_tutorial.png)

![swagger](https://retos.redflox.com/oati-prueba/update_tutorial_response.png)

![swagger](https://retos.redflox.com/oati-prueba/delete_tutorial.png)

![swagger](https://retos.redflox.com/oati-prueba/delete_tutorial_response.png)

![swagger](https://retos.redflox.com/oati-prueba/list_tutorials.png)

![swagger](https://retos.redflox.com/oati-prueba/list_tutorials_response.png)

![swagger](https://retos.redflox.com/oati-prueba/create_tutorial.png)

![swagger](https://retos.redflox.com/oati-prueba/create_tutorial_response.png)

![swagger](https://retos.redflox.com/oati-prueba/read_all_details.png)

![swagger](https://retos.redflox.com/oati-prueba/read_all_details_response.png)

![swagger](https://retos.redflox.com/oati-prueba/read_detail_for_tutorial.png)

![swagger](https://retos.redflox.com/oati-prueba/read_detail_for_tutorial_response.png)

![swagger](https://retos.redflox.com/oati-prueba/create_detail_for_tutorial.png)

![swagger](https://retos.redflox.com/oati-prueba/create_detail_for_tutorial_response.png)

![swagger](https://retos.redflox.com/oati-prueba/update_detail_by_id.png)

![swagger](https://retos.redflox.com/oati-prueba/update_detail_by_id_response.png)

![swagger](https://retos.redflox.com/oati-prueba/delete_detail_by_id.png)

![swagger](https://retos.redflox.com/oati-prueba/delete_detail_by_id_response.png)