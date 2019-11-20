

class Vehiculos():
	def __init__(self,marc,model): #el constructor requiere dos parametros
		self.marca=marc
		self.modelo=model
		self.enMarcha=False
		self.acelera=False
		self.frena=False

	def arrancar(self):
		self.enMarcha=True

	def acelerar(self):
		self.acelera=True

	def frenar(self):
		self.frena=True

	def estado(self):
		print("marca: ",self.marca,"\nmodelo: ",self.modelo,"\nEn marcha: ",self.enMarcha, "\nacelerado: ",self.acelera, "\nfrenando:", self.frena)

def serializarObjetos():
	import pickle
	#crear 3 objetos y meterlos en una coleccion para luego serializarla:
	auto1=Vehiculos("hyundai","947tj")
	auto2=Vehiculos("dahiatsu","djf84j")
	auto3=Vehiculos("shimaira","K9999")

	#proceso de serializacion
	autos=[auto1,auto2,auto3] #los pasamos a una lista

	file=open("losAutos","wb") #creamos el archivo binario

	pickle.dump(autos,file) #volcado: dump(<coleccion>,<archivo_binario>)

	file.close()

	del (file) #eliminamos de memoria

#serializarObjetos()

def leerSerializadoObj():
	import pickle
	#abrir, cargar, imprimir:
	file=open("losAutos","rb")
	objetos=pickle.load(file)
	file.close()
	#imprimimos los objetos:
	for o in objetos:
		print("Objeto: ",o)
		print(o.estado()) #usamos metodo de la clase para ver informacion clara
		
#serializarObjetos()
#leerSerializadoObj()

