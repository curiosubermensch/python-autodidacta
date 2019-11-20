import pickle

class Persona:
	def __init__(self,n,g,e):
		self.nombre=n
		self.genero=g
		self.edad=e
		print("se ha creado a :",self.nombre)

	#STR: este metodo nos devuelve los datos de un objeto:
	def __str__(self):
		#cada parentesis corresponde a un atributo, es el formato (y orden) en q se mostraran los datos
		return "{} {} {}".format(self.nombre, self.genero, self.edad)

class ListaPersonas:
	personas=[]

	def __init__(self):
		listaDePersonas=open("ficheroExterno","ab+")
		listaDePersonas.seek(0) #el cursor se habia movido al final, lo dejamos de nuevo al principio para luego leerlo
		try:
			self.personas=pickle.load(listaDePersonas) #cargamos	
		except:
			#en caso de que no haya personas creadas, para que no se caiga
			print("el fichero está vacio")
		finally:
			listaDePersonas.close()
			del(listaDePersonas)

	def agregaPersonas(self,p):
		self.personas.append(p) #la agregamos a la lista
		self.savePersonasInFileExt() #lo llamamos aca, entonces si se rellama se setea 
	def mostrarPersonas(self):
		for i in self.personas:
			print(i) #al imprimir el objeto se verá con el formato definido en __str__
	def savePersonasInFileExt(self):
		listaDePersonas=open("ficheroExterno","wb")
		pickle.dump(self.personas,listaDePersonas) #volcamos la lista de personas en el archivo
		listaDePersonas.close
		del(listaDePersonas)
	def mostrarInfoFileExt(self):
		listaDePersonas=open("ficheroExterno","rb")
		l=pickle.load(listaDePersonas)
		print("*********info del archivo externo**********")
		for i in l:
			print(i)
		listaDePersonas.close()
		del(listaDePersonas)
	def mostrarInfoFileExternoPildoras():
		#esta es la version del video con la cual estoy disconforme
		print("========la info que deberia estar en el archivo externo es la sgte=======")
		for j in self.personas: #estamos leyendo la lista no el archivo (?)
			print(j)


#===========fin clases=============
lista=ListaPersonas()
p=Persona("cristian","masculino",27)
q=Persona("luz","femenino",21)
r=Persona("ramon","masculino",33)

lista.agregaPersonas(p)
lista.agregaPersonas(q)
lista.agregaPersonas(r)

lista.mostrarPersonas()
lista.mostrarInfoFileExt()