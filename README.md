# flask_clasico
Ejercicios de introduccion a la web

## Como lanzar el programa en desarrollo

1. Crear un entorno virtual
    """
        # windows 
        python - m venv env

        # Mac/Linux
        python3 -m venv env
    """
2. Activar el entorno virtual
    """
        #windows
        env\Scripts\activate

        #Mac / Linux
        source ./env/bin/activate


    """
3. Instalar las dependencias
    """ 
        pip freeze > requirements.txt
        pip install -r requirements.txt
    """
4. Hacer una copia del archivo '.env_template' como '.env'
    """
        #LINUX/MAC
        cp .env_template .env

        #Windows
        copy .env_template .env 

    """
5. Editar el archivo '.env' y cambiar (o no) el valor 'DEBUG' ('True'/'False')
