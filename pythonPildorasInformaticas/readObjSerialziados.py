#si se quiere leer objetos serializados utilizando los metodos de la clase y que se interpreten los objetos en sí, hay que copiar la clase Vehiculos
import pickle

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


#abrir, cargar, imprimir:
file=open("losAutos","rb")
objetos=pickle.load(file)
file.close()
#imprimimos los objetos:
for o in objetos:
	print("Objeto: ",o)
	print(o.estado()) #usamos metodo de la clase para ver informacion clara

#output:
# Objeto:  <__main__.Vehiculos object at 0x000000366D8C2908>
# marca:  hyundai 
# modelo:  947tj 
# En marcha:  False 
# acelerado:  False 
# frenando: False
# None
# Objeto:  <__main__.Vehiculos object at 0x000000366D8CA548>
# marca:  dahiatsu 
# modelo:  djf84j 
# En marcha:  False 
# acelerado:  False 
# frenando: False
# None
# Objeto:  <__main__.Vehiculos object at 0x000000366D8CA648>
# marca:  shimaira 
# modelo:  K9999 
# En marcha:  False 
# acelerado:  False 
# frenando: False
# None