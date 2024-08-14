# Llamando las librerias/extenciones que utilizaremos más adelante; pygame siendo para crear juegos 2d.
import pygame


# Traemos la apariencia.

from pygame.sprite import Sprite

# Creamos una clase para realizar nuestro lazer.
class Bullet(Sprite):
    # Creamos una función para perzonalizar nuestro lazer.
    def __init__(self, a_game):
        super().__init__()
        self.screen = a_game.screen
        self.color = a_game.colorbala
        self.rect = pygame.Rect(0,0, a_game.anchobala, a_game.largobala)
        self.rect.midtop = a_game.nave.rect.midtop
        self.juego = a_game
        self.y = float(self.rect.y)
    
    # Creamos una variable para especificar como se va a dezplazar el lazer.
    def update(self):
        self.y -= self.juego.velocidad
        self.rect.y = self.y

    # y por último creamos una función para poner como se va a ver nuestro lazer. 
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
