#SERIALIZACION: Guardar en un archivo externo una coleccion diccionario u objeto codificado en BINARIO para los sgtes fines: 
#- Distribuirlo por internet mas facilmente
#- Guardarlo en un dispositivo externo o disco duro
# - PAra guardarlo en una BD
#suele ser mas practico en estos casos serializar.

#se usa la biblioteca pickle y sus metodos dump() y load()

#serializar colecciones:
def volcado():
	import pickle
	lista=["juan","pepe","luis","dani"]
	binary_file=open("lista_nombres","wb") #le damos nombre al nuevo archivo y damos permiso de escritura binaria=wb
	#volcamos la lista en el fichero externo:
	pickle.dump(lista,binary_file) #dump(<info_a_volcar>,<archivo_binario>)
	binary_file.close() #lo cerramos
	del (binary_file) #lo eliminamos de la memoria (ya quedó guardado en el disco duro)
	#sin output

def lecturaBinario():
	#leer un archivo binario e imprimir su contenido
	import pickle
	file=open("lista_nombres","rb")
	laLista=pickle.load(file) #en la var laLista se guardara lo que se cargue del archivo binario (lo que se lea)
	print(laLista)
	#output: ['juan', 'pepe', 'luis', 'dani']

#lecturaBinario()


#================================================
#serializar objetos:

















