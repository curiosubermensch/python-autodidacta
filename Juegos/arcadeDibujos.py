import pygame

# inicializar el motor de juego
pygame.init()


NEGRO = (0,   0,   0)
BLANCO = (255, 255, 255)
VERDE = (0,   255,   0)
ROJO = (255,   0,   0)
# para dibujar arcos
PI = 3.141592653

dimensiones = (700, 500)
pantalla = pygame.display.set_mode(dimensiones)

pygame.display.set_caption("Mi primer juego en Pygame")

reloj = pygame.time.Clock()

#funciones dibujadoras:
def imprimeCruces():
    for i in range(10,400,20):
        pygame.draw.line(pantalla, NEGRO, [i,10], [i+10,40], 2) #linea q parte de izq a derecha
    #linea q parte de derecha a izq

def imprimeCuadrado():
    """ ----> [x, y, ancho, alto]
        (x,y) --> coordenada esquina superior izquierda
    """
    pygame.draw.rect(pantalla, NEGRO, [2, 2, 400, 200], 2) 

def imprimeElipse():
    """ las elipses se dibujan dentro de un rectangulo, x e y son la esquina sup izq de dicho rectangulo
     [x,y,ancho,alto]
    """
    pygame.draw.ellipse(pantalla, VERDE,[2,2,400,200],3)

# Itera hasta que el usuario pincha sobre el botón de cierre.
hecho = False
# -------- Bucle Principal del Programa -----------
while not hecho:
    # TODOS LOS EVENTOS DE PROCESAMIENTO DEBERÍAN IR DEBAJO DE ESTE COMENTARIO
    for evento in pygame.event.get():  # El usuario hizo algo
        if evento.type == pygame.QUIT:  # Si el usuario pincha sobre cerrar
            hecho = True  # Esto que indica que hemos acabado y sale de este bucle
    

    # TODO EL CÓDIGO DE DIBUJO DEBERÍA IR DEBAJO DE ESTE COMENTARIO:

    pantalla.fill(BLANCO) #preparamos la pantalla para dibujar:
    imprimeCruces()
    imprimeCuadrado()
    imprimeElipse()
    
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


# Cierre correcto de un programa Pygame
pygame.quit()

