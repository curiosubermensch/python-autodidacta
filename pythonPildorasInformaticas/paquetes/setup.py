#crear paquetes distribuibles:
#1. crear en la raiz que contiene el paquete un archivo "setup.py" y completarlo como abajo
#2. Ir al directorio que CONTIENE el setup.py y el paquete y abrirlo en cmd
#3. cmd: estando en la carpeta ejecutar: python setup.py sdist
#4. se crearan dos carpetas: dist (contendrá nombre_archivo.tar.gz) y nombre_paquete.gg-info
#5. ir a dist en cmd y ejecutar: pip3 install nombre_paquete.tar.gz
#ahora el paquete esta listo para usarse


from setuptools import setup 

setup( 
	name="paquetecalculos", 
	version="1.0", 
	description="Paquete funciones avanzadas de matematicas, son 3 nomas", 
	author="cristian", 
	author_email="cristianpadilla02016@gmail.com", 
	url="google.com", 
	packages=["calculos","calculos.calculosAvanzados"] #[paquete_padre, paquete_padre.ruta_hasta_paquete_hijo]
)