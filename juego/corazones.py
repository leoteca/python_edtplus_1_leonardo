# Llamando las librerias/extenciones que utilizaremos más adelante; pygame siendo para crear juegos 2d.
import pygame

from pygame.sprite import Sprite

# Creando la clase la cual nos permitira realizar nuestra nave.
class Corazones(Sprite):

    # Creamos una función que contenga como queremos que se vea nuestra nave.
    def __init__(self, a_game):
        super().__init__()
        self.screen = a_game.screen
        self.screen_rect = a_game.screen.get_rect()

        # Buscamos y cargamos la imagen.
        self.image = pygame.image.load ("juego/imagenes/nave.png")
        # Le damos un tamaño más adecuado.
        self.image = pygame.transform.scale(self.image, (50, 50))
        # Lo cargamos.
        self.rect = self.image.get_rect()