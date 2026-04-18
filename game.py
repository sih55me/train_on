import pygame, random


pygame.init()

window = pygame.display.set_mode((150,180))

player_standbycostume = [
    (pygame.image.load("asset/png/player_standby1.png").convert())
]
player_indexcos = 0
player = player_standbycostume[player_indexcos]

while True:
    
    r = player.get_rect(center = (0,0))
    window.blit(player, r)
    pygame.display.update()
    

    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_0:
                print("d")
                print("aa")
