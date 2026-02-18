import pygame
import random

class Raqueta(pygame.sprite.Sprite):
    #Construccion
    def __init__(self, x_inicial, y_inicial):
        super().__init__() #Inicializar clase base de pygame

        # Dimensiones
        ancho = 15
        alto = 70

        self.image = pygame.Surface([ancho, alto])
        self.image.fill ((255, 255, 255)) #Color blanco por el momento

        # Posicion inicial
        self.rect = self.image.get_rect()
        self.rect.x = x_inicial
        self.rect.y = y_inicial

        #Movimiento 
        self.velocidad = 6 #cantidad de pixeles por fotograma

        #Sistema de iluminacion 
        self.color_normal = (255, 255, 255)
        self.color_choque = (0, 255, 255) #Color de raqueta en color
        self.brillando = False
        self.tiiempo_brillo = 0

    #Funcion de movimiento de raquetas
    def mover_raquetas(self, tecla_arriba, tecla_abajo, teclas_presionadas, alto_pantalla):
        #Tecla para subir está presionada
        if teclas_presionadas[tecla_arriba] and self.rect.top > 0:
            self.rect.y -= self.velocidad
            
        #Tecla para bajar está presionada
        if teclas_presionadas[tecla_abajo] and self.rect.bottom < alto_pantalla:
            self.rect.y += self.velocidad

    def reiniciar_posicion(self):
        # Reinicio de Posicion de raqueta en anotacion
        self.rect.y = self.y_inicial

class Pelota(pygame.sprite.Sprite):
    def __init__(self, centro_x, centro_y):
        super().__init__()
        self.image = pygame.Surface([12, 12]) #Dinbuja un pequeno cuadrado como pelota
        self.image.fill((255, 255, 255)) #Color pelota
        self.rect = self.image.get_rect()
        
        #Posición inicial en el centro de la pantalla
        self.rect.centerx = centro_x
        self.rect.centery = centro_y
        
        # Guardamos el posicion inicial de la pelota para despues de anotar
        self.x_inicial = centro_x
        self.y_inicial = centro_y
        
        #Velocidad inicial baja
        self.vel_baja = 3
        
        #Direccion inicial aleatoria
        opciones = [self.vel_baja, -self.vel_baja]
        self.velocidad_x = random.choice(opciones)
        self.velocidad_y = random.choice(opciones)

    def mover_pelota(self, alto_pantalla, raqueta_izq, raqueta_der):
        #Velocidad a posicion actual
        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y

        #Rebotes en techo y suelo
        if self.rect.top <= 0 or self.rect.bottom >= alto_pantalla:
            self.velocidad_y *= -1 #Invierte velocidad eje y
        #Rebote en raquetas
        if pygame.sprite.collide_rect(self, raqueta_izq) or pygame.sprite.collide_rect(self, raqueta_der):
            self.velocidad_x *= -1 #Velocidad invertida unicamente por ahora, se pretende levantar logica de incremento en 5% cuando choque con raquetas en movimiento

