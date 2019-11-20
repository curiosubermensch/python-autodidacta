#hacer pregunta de cual metodo sera tomado en cuenta esto para herencia de clases y sobrescritura de metodos
#con clases algebraicas tipo a(b)

#def a():
	#crear variable "guapo"
	#debe ser de tipo boolean
	#guapo=False
	#print(guapo)
	#output: False
	
#QUE IMPRIME?
# b=False
# c=0
# print("hola")
# while c<4:
# 	if b == False:
# 		break
# 	c=c+1
# else:
# 	print("chao")
#output: hola
#====================================================================================
#crear un generador que nos 
#retorne una tabla de multi. full:
#def genTabla(tabla):
    # i=1
    # while i<11:
    #     {{c1::yield tabla*i}}
    #     i=i+1

#retornamos en "t" el obj
#iterable (tabla del 5)
#{{c1::t=genTabla(5)}}

#print("5x1 = ",{{c1::next(t)}}) 
#print("-----------")
#print("5x2 = ",{{c1::next(t)}})
# output:
# 5x1 =  5
# -----------
# 5x2 =  10

#yield. Esta orden devolverá un valor (igual que hace return) pero, además, congelará la ejecución de la función hasta la próxima vez que le pidamos un valor, por eso un generador es más eficiente que generar una lista

#importar solo lo necesario para este caso:


def crear():
	from io import open 
	#crear arch.txt para escribir a continuacion  
	file=open("arch.txt", "w") 

	#escribir en el "hola mundo":
	file.write("hola mundo")
	file.write("\nk paza")

	#cierre del archivo:
	file.close()

def abrir():
	#abrir archivo en modo lectura
	from io import open #importar lo necesario
	file=open("arch.txt", "r") 
	
	#lectura del contenido para pasarlo a un string:
	txt=file.read() 

	#seguir procedimiento:
	file.close()
	print(txt) #imprimimos el contenido
	#output: hola mundo

def abrirYmanipular():
	from io import open
	#abrir arch.txt y pasar las lineas a una lista
	file=open("arch.txt", "r") 
	lineas=file.readlines() 
	#cierre:
	file.close()
	print(lineas)
	#output:
	#['hola mundo\n', 'k paza']

def abrirYagregar():
	from io import open
	#abrir arch.txt y agregarle texto
	#"chao mundo" en la ultima linea
	file=open("archivo.txt", "a") 
	file.write("\nchao mundo") 
	file.close()

def splitear():
	#archivo.txt
	#============================================
	# linea uno
	# linea dos
	# chao
	#============================================
	#separar las palabras del archivo por espacio 
	#y pasarlas a una lista, luego imprimir
	#item por item la lista (osea las palabras)
	file=open("archivo.txt","r+") 
	cadena=file.read()
	lista=cadena.split(" ") 
	for i in lista:
		print(i)
	#output:
	# linea
	# uno
	# linea
	# dos
	# chao

def modificaLinea():
	#modificar la segunda linea del archivo.txt: 
	#con el valor "setea3"
	#============archivo.txt==============
	# linea uno
	# linea dos
	# chao
	#=====================================
	file=open("archivo.txt","r+")
	lista=file.readlines() 
	lista[1]="setea3\n" 
	file.seek(0) 
	file.writelines(lista)  
	file.close()
	#============archivo.txt==============
	# linea uno
	# setea3
	# chao
	#=====================================


#modificaLinea()

def imprimeLineaByLinea(): 
	#imprimir las 2 lineas del archivo:
	#===========archivo.txt============
	#linea uno
	#linea dos
	file=open("archivo.txt", "r")
	print(file.readline()) 
	print(file.readline()) 
	file.close()

#imprimeLineaByLinea()
def serializarColeccion():
	#serializar una lista
	#el archivo debe llamarse
	#"serialfile"
	import pickle
	lista=["a","b","c","d"]
	binary_file=open("serialfile","wb")  
	pickle.dump(lista,binary_file) 
	binary_file.close() #lo cerramos
	del (binary_file) #lo eliminamos de la memoria 

def deserializarLeerColeccion():
	#leer un archivo serializado
	#(binario) q contiene una lista
	#e imprimir su contenido:
	import pickle
	file=open("serialfile","rb")
	laLista=pickle.load(file)
	print(laLista)
	#output:
	#['a', 'b', 'c', 'd']


#serializarColeccion()
#deserializarLeerColeccion()