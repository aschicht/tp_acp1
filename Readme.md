# Administracion y control de proyectos 1
****************************************

## Instrucciones de instalacion para ubuntu
(fuente: https://www.digitalocean.com/community/tutorials/how-to-install-django-and-set-up-a-development-environment-on-ubuntu-16-04)

#### Instalar python3 y pip3

Escribir en la terminal:

```
$ sudo apt-get update && sudo apt-get -y upgrade
```

Luego,

```
$ sudo apt-get install python3
```

Chequear que la instalacion fue exitosa:

```
$ python3 -V
```

El resultado deberia ser algo como: 

```
python 3.6.8
```

Ahora instalamos pip3. Pip es un manejador de dependencias.

```
$ sudo apt-get install -y python3-pip
```

Chequeamos que se haya instalado bien:

```
$ pip3 -V
```

Deberia mostrar algo parecido a:

```
pip 9.0.1 from /usr/lib/python3/dist-packages (python 3.6)
```

#### Instalar virtualenv

Virtualenv es una herramienta que nos permite crear un ambiente 
virtual que podemos activar y desactivar para instalar librerias
y que no conflictuen entre los distintos ambientes virtuales.

```
$ pip3 install virtualenv
```

Chequeamos que se haya instalado bien.

```
virtualenv --version
```
Deberiamos ver algo asi como:
```
15.1.0
```

#### Crear el ambiente virtual
Nos vamos en la terminal a la carpeta ANTERIOR a donde tenemos el proyecto que bajamos 
de github y escribimos:

```
$ virtualenv acp1
```

Eso nos crea un ambiente virtual. Para activarlo hacemos:

```
$ . env/bin/activate
```
Nos va a aparecer el nombre del ambiente virtual a la izquierda, eso significa que todo lo que
instalemos con pip3 va a vivir solamente en este ambiente virtual:
```
(acp1) alberto@prudence:~/workspace/facultad/acp1
```
Para desactivar el ambiente virtual:

```
$ deactivate
```
Siempre trabajamos en el ambiente virtual cuando codeamos.

#### Bajar las librerias requeridas

Vamos a usar un archivo que se llama requirements.txt que contiene 
un listado de las librerias necesarias para correr el proyecto

```
$ pip3 install -r requirements.txt
```


#### Crear la base de datos

Vamos a usar una base de datos sqlite que es lo mas facil, para crearla:

```
$ python3 manage.py migrate
```

Luego, para crear un usuario administrador escribimos:

```
$ python3 manage.py createsuperuser --username=admin --email=admin@admin.com 
```

Les va a pedir una password, usen la que mas les guste. Con eso tenemos creada una 
base de datos que se llama db.sqlite3 en el proyecto. POR FAVOR NO SUBAN ESO AL REPOSITORIO.

#### Correr las migraciones de la base de datos para crear el schema

Para que nos cree el schema de la base de datos usamos:

```
$ python3 manage.py migrate 
```

#### Correr el proyecto

En el repositorio ya esta subido todo lo necesario para levantar un server, que se levanta
asi:
 
```
$ python3 manage.py runserver localhost:8000
```

Si van a su browser y ponen la url: http://localhost:8000 les va a cargar la pagina default.
Tambien esta creada y subida una base de datos sqlite3 (esta en el proyecto y se llama db.sqlite3).
Si van a la url http://localhost:8000/admin ahi esta el administrador de django 
que propongo usar como backoffice. Pueden acceder con el usuarion que crearon en el paso 
anterior (en mi caso, admin)



