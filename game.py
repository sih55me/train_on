import pygame, random


pygame.init()
#state:
#0 berarti main menu
#1 berarti permainan berjalan 
gameState = 0
#ukuran jendela
wsiz = [550, 480]
window = pygame.display.set_mode((wsiz[0],wsiz[1]))
pygame.display.set_caption("Train On Watch")
fps = 50
clock = pygame.time.Clock()

#player
player_standbycostume = [
    (pygame.image.load("asset/png/player_standby1.png").convert_alpha())
]

player_indexcos = 0
player = player_standbycostume[player_indexcos]
#x,y
player_cor = [
    int(wsiz[0]/2),
    int((wsiz[1]-player.get_height())/2)
]

def getDefFont(size=17):
    return pygame.font.Font("asset/fonta/ocraextended.ttf", size)
def getzTitleFont(size=50):
    return pygame.font.Font("asset/fonta/Cantarell-Bold.ttf", size)
def getDefFontMinimal():
    return getDefFont(17)


def runGame():
    while True:
        
        window.blit(player, (player_cor[0], player_cor[1]))
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                exit()
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_DOWN:
                    print('down')
        pygame.display.update()
        clock.tick(fps)

def mainMenu():
    global gameState
    while True:
        t = getzTitleFont(25).render("Train On Watch", True, pygame.color.Color(225,225,255))
        r = t.get_rect(center=(wsiz[0]/2, 45))
        window.blit(t, r)
        t = getDefFont(18).render("Press SPACE to start", True, pygame.color.Color(225,225,255))
        r = t.get_rect(center=(wsiz[0]/2, (wsiz[1]/2)-40))
        window.blit(t, r)
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                exit()
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_SPACE:
                    window.fill(pygame.color.Color(10,10,10))
                    gameState = 1
                    return
        pygame.display.update()
        clock.tick(fps)

while True:
    if gameState == 0:
        mainMenu()
    else:
        runGame()

    
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()
            exit()
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_0:
                print("d")
                print("aa")
    pygame.display.update()
    clock.tick(fps)
    