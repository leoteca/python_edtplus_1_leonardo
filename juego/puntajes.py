import pygame.font

from pygame.sprite import Group

from corazones import Corazones

class TablaPuntos:
    def __init__(self, a_game):
        self.screen = a_game.screen 
        self.screen_rect = self.screen.get_rect()
        self.juego = a_game
        self.estadisticas = a_game.estadisticas

        self.colorTexto = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        self.prepara_puntos()
        self.prepara_puntosMaximos()
        self.prepara_corazones()

    def prepara_puntos(self):
        self.puntosStr = str(self.juego.puntos)
        self.puntosImagen = self.font.render(self.puntosStr, True, self.colorTexto, None)
        self.puntos_rect = self.puntosImagen.get_rect()
        self.puntos_rect.right = self.screen_rect.right - 20
        self.puntos_rect.top = 20

    def prepara_puntosMaximos(self):
        self.puntosMaximosStr = str(self.juego.puntajeMaximo)
        self.puntosMaximosImagen = self.font.render(self.puntosMaximosStr, False, self.colorTexto, None)

        self.puntosMaximos_rect = self.puntosMaximosImagen.get_rect()
        self.puntosMaximos_rect.centerx = self.screen_rect.centerx
        self.puntosMaximos_rect.top = self.screen_rect.top

    def verifica_puntosMaximos(self):
        if self.juego.puntos > self.juego.puntajeMaximo:
            self.juego.puntajeMaximo = self.juego.puntos
            self.prepara_puntosMaximos()

    def muestraPuntos(self):
        self.screen.blit(self.puntosImagen, self.puntos_rect)
        self.screen.blit(self.puntosMaximosImagen, self.puntosMaximos_rect)
        self.corazones.draw(self.screen)

    def prepara_corazones(self):
        self.corazones = Group()
        for numero_corazones in range(self.juego.naves_restantes):
            corazon = Corazones(self.juego)
            corazon.rect.x = 10 + numero_corazones * corazon.rect.width
            corazon.rect.y = 10
            self.corazones.add(corazon)