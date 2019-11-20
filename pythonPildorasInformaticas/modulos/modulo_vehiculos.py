#esta es una copia/REUTILIZACION de las clases del archivo herenciaVehiculosMejorada

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

# class Moto(Vehiculos): #moto hereda de la clase "Vehiculos", todos sus atributos y propiedades
# 	pass #aunque lo dejemos en stand by hereda
class Moto(Vehiculos):
	hcaballito=False
	def caballito(self):
		self.hcaballito=True
	#SOBRESCRITURA DE METODOS: Si creamos un metodo con el mismo nombre del de la clase padre, se sobrescribe
	#osea que el que vale es el sobrescrito de la clase hijo:
	def estado(self):
		print("marca: ",self.marca,"\nmodelo: ",self.modelo,"\nEn marcha: ",self.enMarcha, "\nacelerado: ",self.acelera, "\nfrenando:", self.frena, "\nHaciendo el caballito: ",self.hcaballito)

class Quad(Moto): 
	pass

class Furgoneta(Vehiculos):
	def cargar(self, carga):
		self.cargar=carga
		if self.cargar:
			print("Furgoneta cargada")
		else:
			print("Furgoneta sin cargar")

class VehiElectricos(Vehiculos):
	cargando=False
	def __init__(self,ma,mo): #se le pasan parametros q se repasan al init de la clase padre (abajo) 
		super().__init__(ma,mo)
		self.autonomia=100
	def cargarEnergia():
		self.cargando=True
	def estado(self):
		super().estado() #reutilizamos el metodo estado de la clase padre
		print("Cargando: ",self.cargando,"\nAutonomia: ",self.autonomia) #le agregamos mas cosas

class BiciElectrica(VehiElectricos,Vehiculos): #HERENCIA MULTIPLE: LA PREFERENCIA DE CONSTRUCTOR VA EN ORDEN, EL 
	pass

