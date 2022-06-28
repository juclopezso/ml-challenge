# Flask scripts

### App
- Correr aplicación en ambiente de desarrollo
```
flask run
```
### Base de datos
- Crear la base de datos
```
flask db init
```
- Crear o actualizar archivo de migraciones
```
flask db migrate --message 'my message'
```
- Aplicar migfraciones a la base de datos
```
flask db upgrade
```

# Instalación y pruebas

## Ambiente de desarrollo
La aplicación corre en el ambiente local con una base de datos sqlite3.
Para correr la aplicación en ambiente de desarrollo es necesario tener instalado python 3.8+ y seguir los siguientes pasos:
- Crear ambiente virtual (venv). Correr en la raíz del proyecto:
```
python3 -m venv venv
```
- Activar ambiente virtual. Correr en la raíz del proyecto:
```
source venv/bin/activate
```
- Instalar dependencias. Correr en la raíz del proyecto:
```
pip install -r requirements.txt
```
Si el paso anterior genera algún error, borrar la línea 10 del archivo requirements.txt (psycopg2==2.9.1)

- Exportar variable de entorno con ambiente de desarrollo. Correr:
```
export FLASK_ENV=dev
```
- Crear base de datos local. Correr en la raíz del proyecto:
```
flask db init
```
- Aplicar migfraciones a la base de datos. Correr en la raíz del proyecto:
```
flask db upgrade
```
- Correr aplicación:
```
flask run
```
La aplicación correrá en la url localhost:5000

## Pruebas
- Para correr las pruebas unitarias. Correr en la raíz del proyecto: 
```
flask test
```

## Ambiente de producción
La aplicación corre en un contenedor de Docker con el servidor de aplicaciones Wsgi y el servidor web Nginx. La base de datos configurada es Postgresql.
Para ejecutar la aplicación en ambiente de producción debe tener instalado docker, y se deben seguir los siguientes pasos:
- Crear archivo de variables de entorno con los valores:
```
FLASK_APP=wsgi.py
FLASK_ENV=prod
DATABASE_URL=postgresql://flasky:flask1234@db:5432/flask
```
Nota: "flasky" es el usuario de postgres con contraseña "flask1234". El usuario debe tener permisos en la base de datos "flask". Si estos datos son modificados, también deben ser modificados en el archivo docker-compose.yml.

- Correr la aplicación con Docker. Correr en la raíz del proyecto:
```
docker-compose up
```
Nota: Si realiza algún cambio al código de la aplación, se sugiere limpiar el build de docker. Puede realizarlo con el siguiente comando:
```
docker-compose down && docker-compose build --no-cache
```
La aplicación correrá en la url localhost:8008
