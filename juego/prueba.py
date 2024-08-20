# Llamando las librerias/extenciones que utilizaremos más adelante; pygame siendo para crear juegos 2d y sys para cerrar programas en conjunto con pygame.
import pygame
import sys

# importamos la clase nave de nuestro achivo Nave para usarla.

from nave import Nave

# importamos la clase Bullet de nuestro achivo lazer para usarla.

from lazer import Bullet

# Creamos una clase en la cual especificaremos como queremos que se vea nuestra pantalla y los elmentos que aparezcan en ella.

from alien import Alien

from puntajes import TablaPuntos

from estadistacas import Estadisticas

from time import sleep

from botón import Boton

class GuerraEstelar:
    # Dentro de la clase definimos una función en donde personalizaremos la pantalla.
    def __init__(self):
        pygame.init()
        self.puntos = 0
        self.puntajeMaximo = 0
        self.ancho = 1250
        self.alto = 600
        # Le especificaremos a la pantalla su altura y su anchura.
        self.screen = pygame.display.set_mode((self.ancho,self.alto))
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height
        # Le especificaremos a la pantalla que título debe poner.
        pygame.display.set_caption("Guerra Estelar")
        # Y le diremos cual va a ser su color de fondo.
        self.color = (0, 0, 0)
        # Los paramatros del lazer.
        self.velocidad = 1
        self.anchobala = 3
        self.largobala = 15
        self.colorbala = (0, 0, 255)
        self.naves_restantes = 3
        self.velocidad_nave = 5
        self.estadisticas = Estadisticas(self)
        self.TablaPuntos = TablaPuntos(self)
        # Traemos nuestra clase nave y la anclamos a una variable.
        self.nave = Nave(self)
        # Traemos la apariencia de el lazer.
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.velocidad_Alien = 2.0
        self.flota_velocidad = 10
        self.flota_direccion = 1
        self.juego_activado = False
        self.play_boton = Boton(self, "Jugar")
        self.aumentar_velocidad = 1.5
        pygame.mixer.music.load("juego/música/Moon_Patrol_Music_-_Atari_2600__youconvert.net_.wav")
        pygame.mixer.music.play(-1)
        self.valoresdeSerie()
        self._create_fleet()

    # Creamos una función que nos permita reproducir la pantalla. 
    def correr_juego(self):
        # Y le decimos que si la función es llamada realize lo siguiente. 
        while True:
            # Primero le decimos  separe todos los eventos. 
            for event in pygame.event.get():
                # Y si una de esos eventos es cerrar la pantalla, entos que salga.
                if event.type == pygame.QUIT:
                    sys.exit()
                
                 # Tambien le decimos que si se presiona una tecla y ese es una de las nombradas más abajo que se mueva para el lado correspondiente.   
                
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_d:
                        self.nave.mover_derecha = True

                    if event.key == pygame.K_a:
                        self.nave.mover_izquierda = True

                    if event.key == pygame.K_SPACE:
                       self._fire_bullet()
                        
                
                # Y si se presiona una tecla y no es una de las nombradas anteriormente que no haga nada.

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_d:
                        self.nave.mover_derecha = False

                    if event.key == pygame.K_a:
                        self.nave.mover_izquierda = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    posiciónMouse =pygame.mouse.get_pos()

                    self.verificaBoton(posiciónMouse)

            # Y llamamos a la clase mover para que lo anterior se cumpla.
            if self.juego_activado:
                self.nave.mover()

                # Luego le asignamos el color.

                self.screen.fill(self.color)

                # Llamamos nuestra variable y la reproducimos.

                self.nave.correr()

                self.bullets.update()

                self.update_alien()

                for bullet in self.bullets.sprites():
                    bullet.draw_bullet()
                
                self.aliens.draw(self.screen)
                self.TablaPuntos.muestraPuntos()

            if not self.juego_activado:
                self.play_boton.dibujaBoton()

            pygame.display.flip()

            # Llamamos nuestra variable y la reproducimos.

    def _fire_bullet(self):
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)


    def _create_fleet(self):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        availableSpace = self.ancho - (2 * alien_width)
        numerodeAliens = availableSpace // (2 * alien_width)
        nave_height = self.nave.rect.height
        availableSpacey = self.alto - (3 * alien_height) - nave_height
        numerodeFilas = availableSpacey // (2 * alien_height)

        for fila in range(numerodeFilas):
         for numeroAlien in range(numerodeAliens):
           
              self._create_alien(numeroAlien, fila)
    

    def _create_alien(self, numeroAlien, fila):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * numeroAlien
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * fila
        self.aliens.add(alien)     


    def update_alien(self):
        self.valida_bordesFlota()
        self.aliens.update()

        if not self.aliens:
           self.bullets.empty()
           self.aumentoVelocidad()
           self._create_fleet()

        if pygame.sprite.spritecollideany(self.nave, self.aliens):
           self.nave_colisionada()

    def nave_colisionada(self):
       if self.naves_restantes > 0:
            self.naves_restantes -= 1
            self.TablaPuntos.prepara_corazones()
            self.sonidoExplosión = pygame.mixer.Sound("juego/música/Explosion_Sound_Effects (mp3cut.net).wav")
            self.sonidoExplosión.play()

            sleep(0.4)

            self.aliens.empty()
            self.bullets.empty()

            self._create_fleet()
            self.nave.centrar_nave()

            sleep(0.5)

            

       else:
           self.juego_activado = False
           self.sonidoExplosión = pygame.mixer.Sound("juego/música/Explosion_Sound_Effects (mp3cut.net).wav")
           self.sonidoExplosión.play()


    def valida_bordesFlota(self):
        for alien in self.aliens.sprites():
         if alien.valida_bordes():
           self.cambia_direccion()
           break

    def cambia_direccion(self):
       for alien in self.aliens.sprites():
          alien.rect.y += self.flota_velocidad
       self.flota_direccion *= -1

    def verificaBoton(self, posiciónMouse):
        self.botonPresionado = self.play_boton.rect.collidepoint(posiciónMouse)
        if self.botonPresionado and not self.juego_activado:
            self.valoresdeSerie()
            self.estadisticas.reinicia()
            self.juego_activado = True
            self.puntos = 0
            self.TablaPuntos.prepara_puntos()
            self.naves_restantes = 3
            self.TablaPuntos.prepara_corazones()

            self.aliens.empty()
            self.bullets.empty()

            self._create_fleet()
            self.nave.centrar_nave()

    def valoresdeSerie(self):
        self.nave.__init__(self)
        self.velocidad_nave = 5
        self.velocidad = 1
        self.velocidad_Alien = 2.0

        self.flota_direccion = 1

    def aumentoVelocidad(self):
        self.velocidad_nave *= self.aumentar_velocidad
        self.velocidad *= self.aumentar_velocidad
        self.velocidad_Alien *= self.aumentar_velocidad
        
# Y por último le decimos que si el nombre es igual al main, reproduzca la función correr juego.
if __name__ == "__main__":
      a = GuerraEstelar()

      a.correr_juego()