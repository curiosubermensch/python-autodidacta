from tkinter import *

#======================================raiz========================================
raiz=Tk()
raiz.title("Ventanita")
raiz.resizable(1,1) #1/0 --> true/false #permitir o no el redimensionado de la ventana
raiz.iconbitmap("C:/Users/Crisitan/Pictures/imagenes para mis programas/pithon.ico") #icono de la ventana
raiz.config(bg="brown")
raiz.config(bd=100) #grosor del borde
raiz.config(relief="sunken") #tipo de borde
raiz.config(cursor="hand2")
#=====================================frame========================================
miFrame=Frame()
miFrame.pack(fill="both", expand="True") #el frame y la raiz ambos se expande en conjunto con la ventan
miFrame.pack()
miFrame.config(bg="blue") 
miFrame.config(width=500, height=350) #ancho del frame, la raiz se ajustará a este
miFrame.config(bd=35) #grosor del borde
miFrame.config(relief="groove") #tipo de borde
miFrame.config(cursor="pirate") #cada vez q se pase el cursor por el frame se transformará en pirata
#===================================motor gui====================================
raiz.mainloop()