import pygame

#pygame setup
pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
running = True

#bucle principal       
while running:
    #Ciclo de revisi[on actividad usuario
    for evento in pygame.event.get():
        #Si el evento presiona la x
       if evento.type == pygame.QUIT:
           running = False

#screen color
screen.fill("purple")

#MAIN GAME

#Flip screen
pygame.display.flip()

clock.tick(60)



#Cierre del bucle
pygame.quit()
       
    


