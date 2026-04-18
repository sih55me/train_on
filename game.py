import pygame, random


pygame.init()

window = pygame.display.set_mode((90,100))
pygame.display.toggle_fullscreen()
player_standby1 = pygame.image.load("asset/player_standby1.png")

while True:
    
    
    pygame.display.update()
    

    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_0:
                print("d")
                print("aa")
