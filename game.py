import pygame, random


pygame.init()

window = pygame.display.set_mode((90,100))
pygame.display.toggle_fullscreen()

while True:
    radom = random.randint(0,225)
    window.fill(pygame.color.Color(radom,radom,radom))
    pygame.display.update()
    

    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_0:
                print("d")
