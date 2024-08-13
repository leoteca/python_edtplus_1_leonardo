# Llamando las librerias/extenciones que utilizaremos más adelante; pygame siendo para crear juegos 2d y sys para cerrar programas en conjunto con pygame.
import pygame
import sys

# importamos la clase nave de nuestro achivo Nave para usarla.

from nave import Nave

# importamos la clase Bullet de nuestro achivo lazer para usarla.

from lazer import Bullet

# Creamos una clase en la cual especificaremos como queremos que se vea nuestra pantalla y los elmentos que aparezcan en ella.

class GuerraEstelar:
    # Dentro de la clase definimos una función en donde personalizaremos la pantalla.
    def __init__(self):
        pygame.init()
        # Le especificaremos a la pantalla su altura y su anchura.
        self.screen = pygame.display.set_mode((1000,600))
        # Le especificaremos a la pantalla que título debe poner.
        pygame.display.set_caption("Guerra Estelar")
        # Y le dirimos cual va a ser su color de fondo.
        self.color = (230, 230, 230)
        # Los paramatros del lazer.
        self.velocidad = 1
        self.anchobala = 3
        self.largobala = 15
        self.colorbala = (0, 0, 255)
        # Traemos nuestra clase nave y la anclamos a una variable.
        self.nave = Nave(self)
        # Traemos la apariencia de el lazer.
        self.bullets = pygame.sprite.Group()

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

            # Y llamamos a la clase mover para que lo anterior se cumpla.

            self.nave.mover()

            # Luego le asignamos el color.

            self.screen.fill(self.color)

            # Llamamos nuestra variable y la reproducimos.

            self.nave.correr()

            self.bullets.update()
            for bullet in self.bullets.sprites():
                bullet.draw_bullet()

            pygame.display.flip()

            # Llamamos nuestra variable y la reproducimos.

    def _fire_bullet(self):
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)


# Y por último le decimos que si el nombre es igual al main, reproduzca la función correr juego.
if __name__ == "__main__":

    a = GuerraEstelar()

    a.correr_juego()
