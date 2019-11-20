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

class VehiElectricos():
	def __init__():
		self.autonomia=100
	def cargarEnergia():
		self.cargando=True

#las bicis son vehiculos electricos y son un vehiculos normales, comparten todos los metodos de esas clases
class BiciElectrica(VehiElectricos,Vehiculos): #HERENCIA MULTIPLE: LA PREFERENCIA DE CONSTRUCTOR VA EN ORDEN, EL DEL PRINCIPIO ES EL QUE SE TOMA EN CUENTA
	pass

moto1=Moto("honda","7364m")
moto1.caballito()
moto1.estado() #este es el sobreescrito ya que los metodos que mandan son los de la clase hija

print("----------[otra moto]-----------")
moto1=Moto("shizumi","26428hd")
moto1.estado()
#moto1.cargar(False) el metodo cargar es de la clase furgoneta nada q ver con moto

print("----------[quad]-----------")
quad=Quad("jeep","r15j92") #constructor de Vehiculos
quad.caballito()
quad.estado() #hereda el metodo estaoo() de la clase Moto, osea la que esta a continuacion en jerarquia
#Quad<Moto<Vehiculo

print("-------[furgoneta]----------")
furgo1=Furgoneta("Renault","kangoo")
furgo1.estado()
furgo1.cargar(True)

print("----------[bici electrica]-----------")
miBici=BiciElectrica() #constructor de VehiElectricos


