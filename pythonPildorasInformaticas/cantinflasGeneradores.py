def gen_diez_numeros(inicio):
    fin = inicio + 10    
    while inicio < fin:
        inicio+=1
        yield inicio, fin #puede retornar 2 cosas

# for inicio, fin in gen_diez_numeros(1):
#     print(inicio, fin)

# print("..........")
# losdies=gen_diez_numeros(10)
# print(next(losdies))
# print(".....pausa.....")
# print(next(losdies))

#--------------------------------------

#crear un generador que nos 
#retorne una tabla de multi. full:
def genTabla(tabla):
	i=1
	while i<11:
		yield tabla*i
		i=i+1

#retornamos en una variable el obj
#iterable
t=genTabla(5)

print("5x1 = ",next(t)) 
print("-----------")
print("5x2 = ",next(t))
# output:
# 5x1 =  5
# -----------
# 5x2 =  10







