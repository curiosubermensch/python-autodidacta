class Persona():
	def __init__(self,n,e,l):
		self.nombre=n
		self.edad=e
		self.lugar_residencia=l

	def descripcion(self):
		print("Nombre: ",self.nombre,"\nEdad: ",self.edad,"\nResidencia: ",self.lugar_residencia)

#principio de sustitucion: "un empleado ES SIEMPRE UNA persona"; obj hijo ES SIEMPRE UN obj padre 
class Empleado(Persona):
	#con super podemos usar dos metodos constructores en conjunto sin que choquen ni causen problema:
	def __init__(self,s,a, n,e,l): #agregamos (n,e,l) como parametro al constructor 3 variables para pasarle al super constructor
		super().__init__(n,e,l) #no hay necesidad de pasarle "self", solo los parametros (3) definidos en la clase a la que pertenece. Usar super es una manera más elegante de herencia, mas elegante q copy paste de codigo redundante
		self.salario=s
		self.antiguedad=a

	def descripcion(self):
		super().descripcion() #reutilizamos la funcion del mismo nombre de la clase padre
		#y le agregamos lo que le falta:
		print("Salario:",self.salario,"\nAntiguedad: ",self.antiguedad)

class DePrueba():
	pass

print("===============una persona===================")
p=Persona("pepe","23","cuba")
p.descripcion()
print("==============un empleado:====================")
e=Empleado("600","4.5","lusho","26","chile")
e.descripcion()
#creamos un objeto para hacer pruebas de pertenencia:
d=DePrueba()

#================================
#que pasa si creamos a un empleado y no usamos super? R: no tendra ni nombre ni edad ni lugar
#================================
#isinstance(obj,clase): Informa si un objeto es instancia de una clase determinada
print("e pertenece a Persona?",isinstance(e,Persona))
print("p pertenece a Empleado?",isinstance(p,Empleado))
print("d pertenece a Persona?",isinstance(d,Persona))