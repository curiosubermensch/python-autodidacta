#raiz tk {frame{widgets (botones, menus, casillas de verificacion)}}


from tkinter import *

#crear un frame
raiz=Tk()
raiz.title("mi primera ventana")
raiz.resizable(1,1) #1/0 --> true/false #permitir o no el redimensionado de la ventana
#raiz.resizable(0,0) #la dejaria estatica
raiz.iconbitmap("C:/Users/Crisitan/Pictures/imagenes para mis programas/pithon.ico") #icono de la ventana
#la raiz se adapta al frame asi q no es necesario darle ancho y alto
#raiz.geometry("250x250") #ancho x alto
raiz.config(bg="brown")
#=====================================creacion del frame========================================
#(todo lo que se puede modificar del frame se puede hacer a la raiz)
miFrame=Frame()
#miFrame.pack(side="right") #empaquetado; side="right" --> al redimensionar se apega a la derecha
#miFrame.pack(side="left", anchor="s") #anchor="n/s/w/e" para combinar y que se ajuste en diagonal
#miFrame.pack(fill="y",expand=1) #expandir verticalmente
#miFrame.pack(fill="x") #expandir frame horizontalmente
#miFrame.pack(fill="both", expand="True") #el frame y la raiz ambos se expande en conjunto con la ventan
miFrame.pack()
miFrame.config(bg="blue") 
miFrame.config(width=500, height=350) #ancho del frame, la raiz se ajustará a este
miFrame.config(bd=35) #grosor del borde
miFrame.config(relief="groove") #tipo de borde
miFrame.config(cursor="pirate") #cada vez q se pase el cursor por el frame se transformará en pirata
raiz.mainloop() #para q una ventana este en ejecucion se necesita un loop q es este, SIEMPRE debe estar al ultimo!!! 

#con la extension .pyw no se abre la ventana de cmd


