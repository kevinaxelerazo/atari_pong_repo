import pygame
import os
from clases import Raqueta, Pelota

os.environ['SDL_VIDEO_CENTERED'] = '1'

#pygame setup
pygame.init()
ALTO = 720
ANCHO = 1280
screen = pygame.display.set_mode((ANCHO,ALTO))
pygame.display.set_caption("Atari Pong_Kevin Erazo")
clock = pygame.time.Clock()
running = True
game_state = "menu"#Esta variable guarda el estado del juego sea menu o jugando
game_mode = "" #Esta variable guarda el modo de juego

#OBJETOS
raqueta_izq = Raqueta(30, ALTO // 2 - 35)
raqueta_der = Raqueta(ANCHO - 45, ALTO // 2 - 35)
pelota = Pelota (ANCHO //2, ALTO //2)

#DIBUJO DE SPRITES
todos_los_sprites = pygame.sprite.Group()
todos_los_sprites.add(raqueta_izq, raqueta_der, pelota)

#Variables de puntajes
puntaje_1=0
puntaje_2=0
puntaje_max=3
fuente = pygame.font.Font(None, 74)

#bucle principal       
while running:
    #Ciclo de revisi[on actividad usuario
    for evento in pygame.event.get():
        #Si el evento presiona la x
       if evento.type == pygame.QUIT:
           running = False 
       if evento.type == pygame.KEYDOWN:
            if game_state == "menu":
                if evento.key == pygame.K_1:
                    game_mode = "single_player"
                    game_state = "jugando"
                #Aque se decide modo multijugador    
                elif evento.key == pygame.K_2:
                    game_mode = "multi_player"
                    game_state = "jugando"
            if evento.key == pygame.K_ESCAPE:
              runing = False

    if game_state == "jugando":

       teclas = pygame.key.get_pressed()
       # Movemos las raquetas pasándole las teclas correspondientes de Pygame
       raqueta_izq.mover_raquetas(pygame.K_w, pygame.K_s, teclas, ALTO)
       if game_mode == "multi_player":
           #Segundo Jugador usa la raqueta de la derecha
           raqueta_der.mover_raquetas(pygame.K_UP, pygame.K_DOWN, teclas, ALTO)
       elif game_mode == "single_player":
           raqueta_der.mover_ia(pelota,ALTO)

    # Movemos la pelota y le pasamos las raquetas para que detecte los choques
       pelota.mover_pelota(ALTO, raqueta_izq, raqueta_der)
       # Si sale por la izquierda (menor a 0), punto para el Jugador 2
       if pelota.rect.left < 0:
           puntaje_2 += 1
           # Aquí llamaríamos a la función para devolverla al centro
           pelota.reiniciar_pelota() 
       # Si sale por la derecha (mayor al ANCHO), punto para el Jugador 1
       if pelota.rect.right > ANCHO:
            puntaje_1 += 1
            pelota.reiniciar_pelota()

       #Condicionamos marcador para finalizar juego en puntaje_max
       if (puntaje_1 >=puntaje_max or puntaje_2 >= puntaje_max):
          print("Juego Terminado")
          pelota.reiniciar_pelota()
          raqueta_der.reiniciar_posicion()
          raqueta_izq.reiniciar_posicion()
          puntaje_1 = 0
          puntaje_2 = 0
          game_state = "menu"

        



    #Dibujado del juego
    screen.fill((0, 0, 0)) #Color del fondo
    #Dibujamos el menu de inicio
     if game_state == "menu":
         texto_titulo = fuente.render("ATARI PONG", True, (255, 255, 255))
        texto_opcion1 = fuente.render("1. Un Jugador (vs PC)", True, (200, 200, 200))
        texto_opcion2 = fuente.render("2. Multijugador", True, (200, 200, 200))
        
        screen.blit(texto_titulo, (ANCHO//2 - 150, ALTO//2 - 150))
        screen.blit(texto_opcion1, (ANCHO//2 - 250, ALTO//2 + 10))
        screen.blit(texto_opcion2, (ANCHO//2 - 250, ALTO//2 + 80))
    elif game_state == "jugando":    
       todos_los_sprites.draw (screen)
       texto_p1 = fuente.render(str(puntaje_1), True, (255, 255, 255))
       texto_p2 = fuente.render(str(puntaje_2), True, (255, 255, 255))
       screen.blit(texto_p1, (320, 20))
       screen.blit(texto_p2, (960, 20))
    pygame.display.flip()

    #Control de FPS
    clock.tick(60)



#Cierre del bucle
pygame.quit()
       
    


