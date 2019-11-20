import pygame

# inicializar el motor de juego
pygame.init()


# colores RGB (red, green, blue)
# 0 = no hay color
# 255 = color al maximo
# Definir algunos colores
# por convencion para el curso si es mayuscula es una constante
NEGRO = (0,   0,   0)
BLANCO = (255, 255, 255)
VERDE = (0,   255,   0)
ROJO = (255,   0,   0)
# para dibujar arcos
PI = 3.141592653

# Abrir y establecer las dimensiones de una ventana
dimensiones = (700, 500)
# setmode permite juegos en ventana y a pantalla completa
pantalla = pygame.display.set_mode(dimensiones)

# Establecer el título de la ventana
pygame.display.set_caption("Mi primer juego en Pygame")

# Se usa para gestionar cuan rápido se actualiza la pantalla
reloj = pygame.time.Clock()

#funciones dibujadoras:
def dibujaRayasDiagonalesAbajo():
    for x in range(0, 300, 10): #20 de separacion
        pygame.draw.line(pantalla, VERDE, [0,x], [300,300], 5)

def dibujaRayasDiagonalesArriba():
    for x in range(0, 300, 10): #20 de separacion
        pygame.draw.line(pantalla, VERDE, [0,0], [300,x], 5)

def dibujaRayas():
	for i in range(0,300,10):
		pygame.draw.line(pantalla, ROJO, [i, 0], [i, 300], 5)
# Itera hasta que el usuario pincha sobre el botón de cierre.
hecho = False
# -------- Bucle Principal del Programa -----------
while not hecho:
    # TODOS LOS EVENTOS DE PROCESAMIENTO DEBERÍAN IR DEBAJO DE ESTE COMENTARIO
    for evento in pygame.event.get():  # El usuario hizo algo
        if evento.type == pygame.QUIT:  # Si el usuario pincha sobre cerrar
            hecho = True  # Esto que indica que hemos acabado y sale de este bucle
    # TODOS LOS EVENTOS DE PROCESAMIENTO DEBERÍAN IR ENCIMA DE ESTE COMENTARIO

    # TODA LA LÓGICA DEL JUEGO DEBERÍA IR DEBAJO DE ESTE COMENTARIO

        # fin de la logica del juego

    # TODO EL CÓDIGO DE DIBUJO DEBERÍA IR DEBAJO DE ESTE COMENTARIO:

    # Primero, limpia la pantalla con blanco. No vayas a poner otros comandos de dibujo encima
    # de esto, de otra forma serán borrados por este comando:
    pantalla.fill(BLANCO)

    # Dibujamos sobre la pantalla una línea verde de 5 píxeles de ancho
    # que vaya desde (0,0) hasta (100,100).
    pygame.draw.line(pantalla, VERDE, [0, 0], [100, 100], 5)
    # Dibujar sobre la pantalla varias líneas desde (0, 10) hasta (100, 110)
    # de 5 píxeles de grosor usando un bucle while
    dibujaRayasDiagonalesAbajo()
    dibujaRayasDiagonalesArriba()
    dibujaRayas()
    # --- Avanzamos y actualizamos la pantalla con lo que hemos dibujado.
    pygame.display.flip()

    # Limita a 20 fotogramas por segundo (frames per second)
    reloj.tick(20)

# Procesamiento de eventos:
# debe ser un y solo un bucle de eventos
for evento in pygame.event.get():
    if evento.type == pygame.QUIT:
        print("El usuario solicitó salir.")
    elif evento.type == pygame.KEYDOWN:
        print("El usuario presionó una tecla.")
    elif evento.type == pygame.KEYUP:
        print("El usuario soltó una tecla.")
    elif evento.type == pygame.MOUSEBUTTONDOWN:
        print("El usuario presionó un botón del ratón")

# La lógica básica y el orden de cada fotograma del juego se sigue por:

# While not hecho:
# Para cada evento (pulsar tecla, click del ratón, etc.):
# Usa una cadena de instrucciones if para ejecutar el código que maneje cada evento.
# Realiza los cálculos que determinan a dónde se mueven los objetos, qué sucede cuando colisionan, etc.
# Limpiar la pantalla
# Dibujar todo

# Cierre correcto de un programa Pygame
pygame.quit()

#Solución a “TabError: inconsistent use of tabs and spaces in indentation”
#pip install autopep8
#autopep8 -i nombre_archivo.py