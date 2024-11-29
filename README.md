# API de Herramientas disponibles
# Proyecto para curso de Python + FastAPI
Implementación de una API que permite consultar las herramientas disponibles en PAÑOL.

## Python y dependencias:

Se utilizó la versión de **Python 3.12.6** para el desarrollo del proyecto.

Las dependencias necesarias son:
* uvicorn==0.32.1
* fastapi==0.115.5
* pydantic-settings==2.6.1
* requests==2.32.3
* SQLAlchemy==2.0.36
* psycopg2-binary==2.9.10

## Pasos necesarios para ejecutar la API:

Para activar el **entorno virtual** se ejecuta en Windows:
'''
**venv\Scripts\activate**
'''

Para poder utilizar la **API** se deben instalar las dependencias contenidas en el archivo 'requirements.txt' mediante el comando:
'''
**'pip install -r requirements.txt'**
'''

En el archivo .env.example se indican los formatos de variables de entorno. Para lograr ejecutar la **API** exitosamente se debe crear la base de datos y conectarla a la API colocando en el archivo **'.env'** las variables de entorno utilizadas.

Teniendo las dependencias instaladas y las variables de entorno definidas podremos inicializar la **API** mediante el archivo **'main.py'**
Ejecutamos entonces: 
'''
**'python main.py'**
'''

###### Alumno: Esteban David Galdames
