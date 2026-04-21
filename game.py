import pygame, random,tkinter


pygame.init()
#state:
#0 berarti main menu
#1 berarti permainan berjalan 
#2 berarti permain menang
#3 berarti permain kalah
gameState = 0
#ukuran jendela
wsiz = [int(480*1.2), int(360*1.2)]
window = pygame.display.set_mode((wsiz[0],wsiz[1]))
pygame.display.set_caption("Train On Watch")
fps = 50
clock = pygame.time.Clock()

skor = 0
hskor = 0

bgmp3 = pygame.mixer.Sound("asset/mp3/bgsong.wav")
bgmp3.set_volume(50)

bgmp3play = pygame.mixer.Sound("asset/mp3/bgmp2.mp3")
bgmp3play.set_volume(30)

#player
player_standbycostume = [
    pygame.image.load("asset/png/player_standby1.png").convert_alpha(),
    pygame.image.load("asset/png/player_standby2.png").convert_alpha()
]

bg =  [
    pygame.transform.scale(pygame.image.load("asset/png/bgmainmenu.png").convert(), (wsiz[0], wsiz[1])),
    pygame.transform.scale(pygame.image.load("asset/png/bgplay.png").convert(), (wsiz[0], wsiz[1]))
]
#0 = standby
#1 = lari
#2 = pignsan
playerMode = 0

player_indexcos = 0
player = player_standbycostume[player_indexcos]
#player size
plasca = [
    [83,122],
    [72,122]
]
#x,y
player_cor = [
    int(wsiz[0]/2),
    int(60)
]


trpoy = 150
train_cor = [wsiz[0]/2,trpoy]


def askQuit():
    isDialogQuit = True
    drect = (0,0,wsiz[0], wsiz[1])
    dim = pygame.Surface(pygame.Rect(drect).size, pygame.SRCALPHA)
    dim.set_alpha(138)
    dim.fill((0,0,0))
    window.blit(dim, drect)
    t = getzTitleFont(25).render("Quit the game?", True, pygame.color.Color(225,225,255))
    r = t.get_rect(center=(wsiz[0]/2, (wsiz[1]/2)-30))
    window.blit(t, r)

    t = getDefFont(19).render("[ENTER]| Yes", True, pygame.color.Color(225,0,0),pygame.Color(55,0,0))
    r = t.get_rect(center=(wsiz[0]/2- 100, (wsiz[1]/2)+10))
    window.blit(t, r)

    t = getDefFont(19).render("[ESC]| No", True, pygame.color.Color(225,225,255))
    r = t.get_rect(center=(wsiz[0]/2+ 120, (wsiz[1]/2)+10))
    window.blit(t, r)
    pygame.display.update()
    while isDialogQuit:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                isDialogQuit = False
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_RETURN:
                    isDialogQuit = False
                    pygame.quit()
                    exit()
                elif ev.key == pygame.K_ESCAPE:
                    isDialogQuit = False


def getDefFont(size=17):
    return pygame.font.Font("asset/fonta/ocraextended.ttf", size)
def getzTitleFont(size=50):
    return pygame.font.Font("asset/fonta/Cantarell-Bold.ttf", size)
def getDefFontMinimal():
    return getDefFont(17)

def animplayer():
    global player_indexcos, playerMode, player
    if playerMode == 0:
        if player_indexcos >= 1.7:
            player_indexcos = 0
        player_indexcos += 0.1
        player = player_standbycostume[int(player_indexcos)]

def touchTrain(trre:pygame.Rect, pl:pygame.Rect):
    global player_cor, train_cor, gameState
    if trre.colliderect(pl):
        bgmp3play.stop()
        gameState = 3
        return
def runTrain(t,pl):
    global train_cor
    if t == True:
        if train_cor[0] <= -100:
            train_cor = [wsiz[0]+1/2,trpoy]
            t = False
            pygame.time.set_timer(67, 3000, loops=1)
        train_cor[0] -= 3
        rc = pygame.draw.rect(window, pygame.Color(120,120,130), pygame.Rect(train_cor[0], train_cor[1],150, 120 ))
        touchTrain(rc, pl)
    return t
def runGame():
    global playerMode, gameState, player_cor, train_cor
    bgmp3play.play(loops=-1)
    pygame.time.set_timer(67, 3000, loops=1)
    player_cor = [
        int(wsiz[0]/2),
        int(60)
    ]
    train_cor = [wsiz[0]+1/2,trpoy]
    trainTr = False

    while gameState == 1:
        if player_cor[1] >= 270:
            bgmp3play.stop()
            gameState = 2
        animplayer()
        window.blit(bg[1], (0,0))
        scl = (int(plasca[int(player_indexcos)][0]*1.2),int(plasca[int(player_indexcos)][1]*1.2))
        ps = pygame.transform.scale(player, scl).convert_alpha()
        plr = ps.get_rect(center = (player_cor[0], player_cor[1]))
        if player_cor[1] < 190:
            window.blit(ps, plr)
        trainTr = runTrain(trainTr, plr)
        if player_cor[1] >= 190:
            window.blit(ps, plr)
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                askQuit()
            if ev.type == 67:
                pygame.time.set_timer(67, 0)
                trainTr = True
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_DOWN:
                    playerMode = 1
                    player_cor[1] += 10
                    print('x = ', player_cor[1])
                elif ev.key == pygame.K_ESCAPE:
                    askQuit()
        playerMode = 0
        pygame.display.update()
        clock.tick(fps)
    pygame.time.set_timer(67, 0)
def prefs():
    windowPref = tkinter.Tk()
    box = tkinter.Frame(windowPref)
    box.pack()
    def l():
        gsgtest(windowPref)
    gsgbtn = tkinter.Button(box, text="Gamestate test", command=l)
    gsgbtn.pack()
    sclbtn = tkinter.Button(box, text="Scale")
    sclbtn.pack()
    windowPref.mainloop()
def gsgtest(d):
    global gameState
    windowPref1 = tkinter.Toplevel(d)
    box = tkinter.Frame(windowPref1)
    windowPref1.grab_set()
    windowPref1.transient(d)
    box.pack()
    testCategory = tkinter.Label(box, text="Testing")
    testCategory.pack()
    gameStateGo = tkinter.Entry(box)
    gameStateGo.pack()
    def testGsg(o):
        global gameState
        try:
            gameState = int(o)
            d.destroy()
        except:
            print("Invalid gs")
    gsgbtn = tkinter.Button(box, text="Send to gamestate", command=lambda:testGsg(gameStateGo.get()))
    gsgbtn.pack()
    windowPref1.mainloop()
def mainMenu():
    global gameState
    bgmp3.play(loops=-1)
    while gameState == 0:
        window.blit(bg[0], (0,0))
        et = getzTitleFont(55)
        et.set_bold(True)
        t = et.render("Train On Watch", True, pygame.color.Color(75,75,75))
        r = t.get_rect(center=(wsiz[0]/2, 55))
        window.blit(t, r)
        t = getDefFont(18).render("Press SPACE to start", True, pygame.color.Color(25,25,55))
        r = t.get_rect(center=(wsiz[0]/2, (wsiz[1]/2)-40))
        window.blit(t, r)
        t = getzTitleFont(14).render("Jangan ditiru di dunia nyata!", True, pygame.color.Color(225,0,0))
        r = t.get_rect(center=(120, int(wsiz[1]/1.1)))
        window.blit(t, r)
        et = getzTitleFont(14)
        et.set_bold(True)
        t = et.render("(c) 4a56b", True, pygame.color.Color(225,0,0))
        
        r = t.get_rect(center=(wsiz[0]-120, int(wsiz[1]/1.1)))
        window.blit(t, r)
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                askQuit()
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_SPACE:
                    gameState = 1
                if ev.key == pygame.K_0:
                    prefs()
                elif ev.key == pygame.K_ESCAPE:
                    askQuit()
        pygame.display.update()
        clock.tick(fps)
    bgmp3.stop()


def winScreen():
    for i in range(200):
        drect = (0,0,wsiz[0], wsiz[1])
        dim = pygame.Surface(pygame.Rect(drect).size, pygame.SRCALPHA)
        dim.set_alpha(1)
        dim.fill((205,205,205))
        window.blit(dim, drect)
        pygame.display.update()
    global gameState
    pygame.display.set_caption("Train On Watch - YES!!")
    pygame.mixer.Sound("asset/mp3/win.mp3").play()
    window.set_alpha(100)
    while gameState == 2:
        et = getzTitleFont(55)
        et.set_bold(True)
        t = et.render("You Win!", True, pygame.color.Color(0,55,0,1))
        r = t.get_rect(center=(wsiz[0]/2, 55))
        window.blit(t, r)
        et  = getzTitleFont(19)
        et.set_bold(False)
        t = et.render(f"Score : {skor}", True, pygame.color.Color(25,25,25,1))
        r = t.get_rect(center=(wsiz[0]/2, 125))
        window.blit(t, r)
        t = et.render(f"HighScore : {hskor}", True, pygame.color.Color(25,25,25,1))
        r = t.get_rect(center=(wsiz[0]/2, 130+t.get_height()))
        window.blit(t, r)
        t = getDefFont(18).render("[SPACE] | Continue     [ESC] | Back", True, pygame.color.Color(25,25,55,1))
        r = t.get_rect(center=(wsiz[0]/2, (wsiz[1])-t.get_height()-10))
        window.blit(t, r)
        window.blit(t, r)
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                gameState = 0
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_SPACE:
                    gameState = 1
                elif ev.key == pygame.K_ESCAPE:
                    gameState = 0
        pygame.display.update()
        clock.tick(fps)
    bgmp3.stop()
    

def lossScreen():
    bdsfx = pygame.mixer.Sound("asset/mp3/badending.wav")
    bdsfx.play(loops=-1)
    for i in range(280):
        drect = (0,0,wsiz[0], wsiz[1])
        dim = pygame.Surface(pygame.Rect(drect).size, pygame.SRCALPHA)
        dim.set_alpha(random.randint(1,2))
        dim.fill((0,0,0))
        window.blit(dim, drect)
        pygame.display.update()
        clock.tick(40)
    global gameState
    pygame.display.set_caption("Train On Watch - --")
    window.set_alpha(100)
    while gameState == 3:
        et = getzTitleFont(55)
        et.set_bold(True)
        t = et.render("You LOSE!", True, pygame.color.Color(255,0,1))
        r = t.get_rect(center=(wsiz[0]/2, 55))
        window.blit(t, r)
        et  = getzTitleFont(19)
        et.set_bold(False)
        t = et.render(f"Score : {skor}", False, pygame.color.Color(225,225,225,1))
        r = t.get_rect(center=(wsiz[0]/2, 125))
        window.blit(t, r)
        t = et.render(f"HighScore : {hskor}", False, pygame.color.Color(225,225,225,1))
        r = t.get_rect(center=(wsiz[0]/2, 130+t.get_height()))
        window.blit(t, r)
        t = getDefFont(18).render("[SPACE] | Continue     [ESC] | Back", True, pygame.color.Color(25,25,55,1))
        r = t.get_rect(center=(wsiz[0]/2, (wsiz[1])-t.get_height()-10))
        window.blit(t, r)
        window.blit(t, r)
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                gameState = 0
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_SPACE:
                    gameState = 1
                    bdsfx.stop()
                    return
                elif ev.key == pygame.K_ESCAPE:
                    gameState = 0
                    bdsfx.stop()
                    return
        pygame.display.update()
        clock.tick(fps)
   


while True:
    pygame.display.set_caption("Train On Watch")
    if gameState == 0:
        mainMenu()
    elif gameState == 1:
        runGame()
    elif gameState == 2:
        winScreen()
    elif gameState == 3:
        lossScreen()



    