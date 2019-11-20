def continua():
	for i in "hola a todos":
		if i=="o":
			continue #tu continua que este caso no importa, ignoralo
		print(i, end=" ")
    #h l a   a   t d s 		

def continua2():
	c=0
	f="hola mundo"
	for i in f:
		if i==" ":
			continue #tu sigue e ignora este caracter
		c+=1
	print("tu frase tiene ",c," letras")
	#tu frase tiene  9  letras

def funcionaMedias():
	pass #STAND BY: dejamos el trabajo a medias, para otro dia, es como que está y no está

def elsa():
	email="cristiancrack"
	for i in email:
		if i=="@":
			arroba=True
			break #si se mete en este if, el break rompe el for osea se sale de él y de su else q es parte de el
	else: #este else es parte del for, si hay break arriba, no pasará por el
		arroba=False #si el for se completa normalmente entonces pasa al else

	print("Correo: ",email,"; ¿Tiene arroba? ",arroba)



