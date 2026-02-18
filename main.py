import pygame
from clases import Raqueta, Pelota

#pygame setup
pygame.init()
ALTO = 720
ANCHO = 1280
screen = pygame.display.set_mode((ANCHO,ALTO))
pygame.display.set_caption("Atari Pong_Kevin Erazo")
clock = pygame.time.Clock()
running = True

#OBJETOS
raqueta_izq = Raqueta(30, ALTO // 2 - 35)
raqueta_der = Raqueta(ANCHO - 45, ALTO // 2 - 35)
pelota = Pelota (ANCHO //2, ALTO //2)

#DIBUJO DE SPRITES
todos_los_sprites = pygame.sprite.Group()
todos_los_sprites.add(raqueta_izq, raqueta_der, pelota)

#bucle principal       
while running:
    #Ciclo de revisi[on actividad usuario
    for evento in pygame.event.get():
        #Si el evento presiona la x
       if evento.type == pygame.QUIT:
           running = False

    teclas = pygame.key.get_pressed()
    # Movemos las raquetas pasándole las teclas correspondientes de Pygame
    raqueta_izq.mover_raquetas(pygame.K_w, pygame.K_s, teclas, ALTO)
    raqueta_der.mover_raquetas(pygame.K_UP, pygame.K_DOWN, teclas, ALTO)
    
    # Movemos la pelota y le pasamos las raquetas para que detecte los choques
    pelota.mover_pelota(ALTO, raqueta_izq, raqueta_der)


    #sDibujado
    screen.fill((0, 0, 0)) #Color del fondo
    todos_los_sprites.draw (screen)
    #Mostrar los cambios
    pygame.display.flip()

#Control de FPS
clock.tick(60)



#Cierre del bucle
pygame.quit()
       
    


