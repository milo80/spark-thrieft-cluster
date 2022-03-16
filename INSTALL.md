## Instalación local en linux debian
### Se recomienda utilizar un ambiente virtual para python en el mismo directorio 
### donde se descarga el proyecto de pruebas.

Instalación de *virtualenv* con `pip`
```
pip install virtualenv
```

Creación de ambiente virtualenv con python3.8
```
virtualenv -p /usr/bin/python3.8 .my-venv
```

Levanta el ambiente virtual
```
source .my-venv/bin/activate
```

Una vez dentro de la sesión `.my-venv`, instalar las dependencias 
desde el archivo requirements.txt
```
pip install -r requirements.txt
```

Ya tienes listo tu ambiente para ejecutar las pruebas de conectividad
en el cluster siguiendo las indicaciones del archivo [README.md](./README.md)


## Instalación de ambiente de pruebas con docker
