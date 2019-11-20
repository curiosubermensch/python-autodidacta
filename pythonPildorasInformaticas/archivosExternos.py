#Archivos externos: Utiles para guardar datos de ejecucion de manera persistente, ej: logs, cnx bd 
#fases para guardar info en arch externos:
#creacion --> apertura --> manipulacion --> cierre

from io import open #importar io, en especifiico open pa abrir

def crear():
	#creacion y/o apertura
	archivo_texto=open("archivo.txt", "w") #nombre del archivo, modo (w=write/escritura); si el archivo no existe #lo crea

	#manipulacion:
	archivo_texto.write("Hola mundo")

	#cierre:
	archivo_texto.close()

def abrir():
	#apertura en modo lectura:
	archivo_texto=open("archivo.txt", "r") #nombre del archivo, modo (r=read/lectura)
	
	#lectura del contenido para pasarlo a un string:
	texto=archivo_texto.read() 

	#cierre:
	archivo_texto.close()
	print(texto) #imprimimos el string



def abrirYmanipular():
	#apertura en modo lectura:
	archivo_texto=open("archivo.txt", "r") #nombre del archivo, modo (r=read/lectura)
	
	#lectura del contenido para pasarlo a una lista:
	##readlines() lee la info linea a linea y la guarda en una lista para poder ser manipulada eventualmente
	lista_lineas=archivo_texto.readlines() 

	#cierre:
	archivo_texto.close()
	
	print(lista_lineas) #mostramos la lista

def abrirYagregar():

	archivo_texto=open("archivo.txt", "a") #modo "a" de append/agregar
	archivo_texto.write("\nAgregando texto e.e") #agregamos en la sgte linea
	archivo_texto.close() 

# crear()
# abrir()
# abrirYmanipular()
# abrirYagregar()
# abrir()

def imprimePuntero():
	#imprimir el contenido del archivo_texto desde el caracter 5
	#archivo_texto{Hola mundo} 
	archivo_texto=open("archivo.txt", "r")
	archivo_texto.seek(5) #el caracter donde queremos el puntero
	print(archivo_texto.read())
	#output:
	#mundo



def imprimeHasta():
	#imprimir el contenido del archivo_texto 
	#hasta el caracter 4
	#archivo_texto{Hola mundo} 
	archivo_texto=open("archivo.txt", "r")
	print(archivo_texto.read(4))
	#output:
	#Hola

#creo que hacia abajo no esta ankiado

def imprimePartes():
	archivo_texto=open("archivo.txt", "r")
	#le pasamos la cantidad de caracteres de la primera linea a seek
	archivo_texto.seek(len(archivo_texto.readline())) #dejamos el puntero en la segunda linea
	
	print(archivo_texto.read())

def imprimeMitad():
	archivo_texto=open("archivo.txt", "r")
	archivo_texto.seek(len(archivo_texto.read())/2) #dejamos el cursor en la mitad
	print(archivo_texto.read())

#imprimeMitad()

def imprimeSplit():
	#separar las palabras del texto del documento por espacio y pasarlas a una lista, luego imprimir
	#item por item la lista (osea las palabras)
	file=open("archivo.txt","r+") #modo read and write
	cadena=file.read()
	lista=cadena.split(" ") #lista=cadena.split(separador)
	for i in lista:
		print(i)

#imprimeSplit()

def modificaLinea():
	file=open("archivo.txt","r+")
	lista=file.readlines() #pasamos lineas a una lista
	lista[1]="holaaaaaa\n" #modificamos la linea 2
	file.seek(0) #volvemos el puntero al principio sino escribirá abajo
	file.writelines(lista) #tenemos que usar este metodo y pasarle la lista para q modifique el archivo
	#print(file.read()) imprimir no funka pero si se hace el procedimiento de modificacion de la linea 
	file.close()

modificaLinea()

def leerLinea(): 
	#leer la primera linea y la ultima e imprimirlas
	file=open("archivo.txt", "r")
	print(file.readline()) #imprime la 1ra linea
	print(file.readline()) # " la segunda
	print(file.readline()) # " la tercera

#leerLinea()