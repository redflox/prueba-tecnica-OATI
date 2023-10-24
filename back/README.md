# Sistema de Tutoriales para Aprendizaje Virtual

Un sistema de gestión de tutoriales con detalles específicos, construido con FastAPI y MySQL.

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

