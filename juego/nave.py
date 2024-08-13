# Llamando las librerias/extenciones que utilizaremos más adelante; pygame siendo para crear juegos 2d.
import pygame

# Creando la clase la cual nos permitira realizar nuestra nave.
class Nave:

    # Creamos una función que contenga como queremos que se vea nuestra nave.
    def __init__(self, a_game):
        self.screen = a_game.screen
        self.screen_rect = a_game.screen.get_rect()

        # Buscamos y cargamos la imagen.
        self.image = pygame.image.load ("C:/Users/mara/Documents/edtplus_python_1_leonardo/juego/imagenes/nave.png")
        # Le damos un tamaño más adecuado.
        self.image = pygame.transform.scale(self.image, (200, 200))
        # Lo cargamos.
        self.rect = self.image.get_rect()
        # Y centramos la nave.
        self.rect.midbottom = self.screen_rect.midbottom
        
       # Le especificamos que al principio no se mueva.

        self.mover_derecha = False

        self.mover_izquierda = False

        # Creamos una función que nos permita personaliza como se mueve la nave.r 
    def mover (self):

        # Movimiento derecha
        if self.mover_derecha and self.rect.right < self.screen_rect.right:
            self.rect.x += 5
        
        # Movimiento izqiuerda
        if self.mover_izquierda and self.rect.left > 0:
            self.rect.x -= 5

    # Creamos una función para reproducir nuestra nave en la pantalla.

    def correr(self):
        self.screen.blit(self.image, self.rect)