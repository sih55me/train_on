import pygame, random,tkinter
from tkinter import messagebox


root = tkinter.Tk()
root.withdraw()

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

spwasdc =  pygame.USEREVENT + 1

skor = 0
hskor = 0

step_level = 1

bgmp3 = pygame.mixer.Sound("asset/mp3/Breaktime.wav")
bgmp3.set_volume(50)

bgmp3play = pygame.mixer.Sound("asset/mp3/bgsong.ogg")
bgmp3play.set_volume(30)

clicksfx = pygame.mixer.Sound("asset/mp3/click.wav")

clicksfx.set_volume(5)
#player
player_standbycostume = [
    pygame.image.load("asset/png/player_standby1.png").convert_alpha(),
    pygame.image.load("asset/png/player_standby2.png").convert_alpha()
]

bg =  [
    pygame.transform.scale(pygame.image.load("asset/png/bgmainmenu.png").convert(), (wsiz[0], wsiz[1])),
    pygame.transform.scale(pygame.image.load("asset/png/bgplay.png").convert(), (wsiz[0], wsiz[1]))
]

train = pygame.image.load("asset/png/train.png").convert_alpha()
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


trpoy = 85
train_cor = [wsiz[0]/2,trpoy]


def askQuit():
    isDialogQuit = True




    while isDialogQuit:
        window.fill((0,0,0))
        drect = (0,0,wsiz[0], wsiz[1])
        t = getzTitleFont(55).render("Quit the game?", True, pygame.color.Color(225,225,255))
        r = t.get_rect(center=(wsiz[0]/2, (wsiz[1]/4)-30))
        window.blit(t, r)
        t = getDefFont(20).render("Enter number 1 to quit. Other key to cancel", True, pygame.color.Color(225,0,0))
        r = t.get_rect(center=(wsiz[0]/2, (wsiz[1]/4)+20))
        window.blit(t, r)


        window.blit(t, r)
        pygame.display.update()
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                exit()
            if ev.type == pygame.KEYDOWN:
                isDialogQuit = False
                if ev.key == pygame.K_1:
                        pygame.quit()
                        exit()



def getDefFont(size=17):
    return pygame.font.Font("asset/fonta/HWYGNRRW.TTF", size)
def getzTitleFont(size=50):
    return pygame.font.Font("asset/fonta/HWYGWDE.TTF", size)
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
    global player_cor, train_cor, gameState, skor
    if trre.colliderect(pl) and (player_cor[1] >= 120 and player_cor[1] < 210):
        requestStop()
        gameState = 3
def runTrain(t,pl):
    global train_cor, train, trpoy
    if t == True:
        if train_cor[0] <= -450:
            if(random.randint(0,1) == 1):
                trpoy = 50
                train = pygame.image.load("asset/png/trainB.png").convert_alpha()
            else:
                trpoy = 85
                train = pygame.image.load("asset/png/train.png").convert_alpha()
            train_cor = [wsiz[0]+1/2,trpoy]
            t = False
            pygame.time.set_timer(spwasdc, random.randint(500, 3000),)
            return t
        train_cor[0] -= random.randint(10,15)
        rc = pygame.Rect(train_cor[0], train_cor[1],150, 120)
        window.blit(train, rc)
        touchTrain(rc, pl)
    return t
def renderskor():
    global skor
    et  = getDefFont(15)
    c = pygame.Color(255,255,100)
    titleS = et.render(f"Skor", True, c)
    window.blit(titleS, titleS.get_rect(center=(50, 25)))
    et  = getDefFont(30)
    summaryS = et.render(str(skor), True, c)
    smr = summaryS.get_rect(center=(50,50)) 
    window.blit(summaryS, smr)
def requestStop():
    global bgmp3play
    bgmp3play.stop()
def level0():
    global gameState
    window.fill((0,0,0))
    et = getzTitleFont(55)
    t = et.render("Level not found", True, pygame.color.Color(255,0,1))
    r = t.get_rect(center=(wsiz[0]/2, 55))
    window.blit(t, r)
    pygame.display.update()
    pygame.time.delay(1500)
def level1():
    global  skor, hskor
    skor = 0
    global playerMode, gameState, player_cor, train_cor
    bgmp3play.play(loops=-1)
    pygame.time.set_timer(spwasdc, 3000,)
    player_cor = [
        int(wsiz[0]/2),
        int(60)
    ]
    train_cor = [wsiz[0]+1/2,trpoy]
    trainTr = False
    while gameState == 1:
        if player_cor[1] >= 270:
            gameState = 2
            requestStop()
            return
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
        renderskor()
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                askQuit()
            if ev.type == spwasdc:
                pygame.time.set_timer(spwasdc, 0)
                trainTr = True
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_DOWN:
                    playerMode = 1
                    player_cor[1] += 10
                    skor += 1
                    print('player x = ', player_cor[1])
                elif ev.key == pygame.K_ESCAPE:
                    askQuit()
        playerMode = 0
        
        pygame.display.update()
        clock.tick(fps)
    pygame.time.set_timer(spwasdc, 0)
    bgmp3play.stop()
def level2():
    global gameState
    window.fill((0,0,0))
    et = getzTitleFont(55)
    t = et.render("On progress", True, pygame.color.Color(255,0,1))
    r = t.get_rect(center=(wsiz[0]/2, 55))
    window.blit(t, r)
    pygame.display.update()
    pygame.time.delay(1500)
def runGame():
    if step_level == 1:level1()
    else:level0()

def prefs():
    def bg_sc(r):
        if r == True:
            return (255,100,1)
        else:return None
    slc = 0
    while True:
        global gameState
        window.fill((0,0,0))
        et = getzTitleFont(55)
        t = et.render("Settings", True, pygame.color.Color(255,255,255))
        r = t.get_rect(center=(wsiz[0]/2, 55))
        window.blit(t, r)
        iet = getDefFont(25)
        p = iet.render("[1] gameState test", True, pygame.color.Color(255,225,1), bg_sc(slc == 0))
        r = p.get_rect(center=(wsiz[0]/2, 120))
        window.blit(p, r)
        p = iet.render("[2] About", True, pygame.color.Color(255,225,225), bg_sc(slc == 1))
        r = p.get_rect(center=(wsiz[0]/2, 150))
        window.blit(p, r)
        p = iet.render("[ESC] Exit", True, pygame.color.Color(255,225,225), bg_sc(slc == 2))
        r = p.get_rect(center=(wsiz[0]/2, 185))
        window.blit(p, r)
        pygame.display.update()
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                askQuit()
            if ev.type == pygame.KEYDOWN:
                print(slc)
                if ev.key == pygame.K_1:
                    if(gsgtest() == 1):
                        return
                if ev.key == pygame.K_UP:
                    slc -=1
                    if slc < 0:
                        slc = 2
                if ev.key == pygame.K_DOWN:
                    slc +=1
                    if slc > 2:
                        slc = 0

                if ev.key == pygame.K_2:
                    root.update()
                    root.attributes("-topmost", True) 
                    messagebox.showinfo("About","""
This game is powered by python, tk(ui), and pygame.
                                        
(C) 4b56a 2026
                                        
music:
once upon a time toby fox - game over
???
                                        """)
                    root.update()
                elif ev.key == pygame.K_ESCAPE:
                    return
def gsgtest():
    global gameState

    while True:
        global gameState
        window.fill((0,0,0))
        et = getzTitleFont(55)
        t = et.render("gameState test", True, pygame.color.Color(255,0,1))
        r = t.get_rect(center=(wsiz[0]/2, 55))
        window.blit(t, r)
        iet = getDefFont(18)
        p = iet.render("Enter some number, ESC to back.", True, pygame.color.Color(255,220,220))
        r = p.get_rect(center=(wsiz[0]/2, 120))
        window.blit(p, r)
        pygame.display.update()
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                askQuit()
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_ESCAPE:
                    return -1
                if ev.key == pygame.K_0:
                    gameState = int(0)
                    return 1
                if ev.key == pygame.K_1:
                    gameState = int(1)
                    return 1
                if ev.key == pygame.K_2:
                    gameState = int(2)
                    return 1
                if ev.key == pygame.K_3:
                    gameState = int(3)
                    return 1
                
def mainMenu():
    global gameState
    bgmp3.play(loops=-1)
    while gameState == 0:
        window.blit(bg[0], (0,0))
        et = getzTitleFont(55)
        t = et.render("Train On Watch", True, pygame.color.Color(75,75,75))
        r = t.get_rect(center=(wsiz[0]/2, 55))
        window.blit(t, r)
        t = getDefFont(18).render("Press SPACE to start", True, pygame.color.Color(25,25,55))
        r = t.get_rect(center=(wsiz[0]/2, (wsiz[1]/2)-40))
        window.blit(t, r)
        et = getDefFont(16)
        et.set_bold(True)
        t = et.render(f"Last highscore: {int(hskor)}", True, pygame.color.Color(225,255,255))
        r = t.get_rect(center=(120, int(wsiz[1]/1.1)))
        window.blit(t, r)
    
        t = et.render("(c) 4a56b", True, pygame.color.Color(225,0,0))
        r = t.get_rect(center=(wsiz[0]-120, int(wsiz[1]/1.1)))
        window.blit(t, r)
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                askQuit()
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_SPACE:
                    gameState = 1
                    clicksfx.play()
                if ev.key == pygame.K_0:
                    clicksfx.play()
                    prefs()
                elif ev.key == pygame.K_ESCAPE:
                    askQuit()
        pygame.display.update()
        clock.tick(fps)
    bgmp3.stop()


def winScreen():
    global step_level
    for i in range(200):
        drect = (0,0,wsiz[0], wsiz[1])
        dim = pygame.Surface(pygame.Rect(drect).size, pygame.SRCALPHA)
        dim.set_alpha(1)
        dim.fill((205,205,205))
        window.blit(dim, drect)
        pygame.display.update()
    global gameState, skor, hskor
    pygame.display.set_caption("Train On Watch - You win!!")
    pygame.mixer.Sound("asset/mp3/Bood.wav").play()
    window.set_alpha(100)
    #layout
    et = getzTitleFont(55)
    if skor >= hskor:
        hskor = skor
    t = et.render("You Win!", True, pygame.color.Color(0,55,0,1))
    r = t.get_rect(center=(wsiz[0]/2, 55))
    window.blit(t, r)
    et  = getzTitleFont(19)
    et.set_bold(False)
    t = et.render(f"Score : {int(skor)}", True, pygame.color.Color(25,25,25,1))
    r = t.get_rect(center=(wsiz[0]/2, 125))
    window.blit(t, r)
    t = et.render(f"HighScore : {int(hskor)}", True, pygame.color.Color(25,25,25,1))
    r = t.get_rect(center=(wsiz[0]/2, 130+t.get_height()))
    window.blit(t, r)
    ew = pygame.font.Font("asset/fonta/ocraextended.ttf", 17)
    ew.set_bold(True)
    t = ew.render("[SPACE] | Try again   [ESC] | Back", True, pygame.color.Color(25,25,55,1))
    r = t.get_rect(center=(wsiz[0]/2, (wsiz[1])-t.get_height()-10))
    window.blit(t, r)
    window.blit(t, r)
    while gameState == 2:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                gameState = 0
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_SPACE:
                    clicksfx.play()
                    gameState = 1
                elif ev.key == pygame.K_ESCAPE:
                    clicksfx.play()
                    gameState = 0
        pygame.display.update()
        clock.tick(fps)
    bgmp3.stop()
    

def lossScreen():
    bdsfx = pygame.mixer.Sound("asset/mp3/badending.wav")
    bdsfx.play(loops=-1)
    for i in range(170):
        drect = (0,0,wsiz[0], wsiz[1])
        dim = pygame.Surface(pygame.Rect(drect).size, pygame.SRCALPHA)
        dim.set_alpha(1)
        dim.fill((0,0,0))
        window.blit(dim, drect)
        pygame.display.update()
    pygame.time.set_timer(spwasdc, 0)
    global gameState
    et = getzTitleFont(55)
    et
    t = et.render("You LOSE!", True, pygame.color.Color(255,0,1))
    r = t.get_rect(center=(wsiz[0]/2, 55))
    window.blit(t, r)
    et  = getDefFont(19)
    et.set_bold(False)
    t = et.render(f"Score : {int(skor)}", True, pygame.color.Color(225,225,225,1),)
    r = t.get_rect(center=(wsiz[0]/2, 125))
    window.blit(t, r)
    t = et.render(f"HighScore : {int(hskor)}", True, pygame.color.Color(225,225,225,1))
    r = t.get_rect(center=(wsiz[0]/2, 130+t.get_height()))
    window.blit(t, r)
    ew = pygame.font.Font("asset/fonta/ocraextended.ttf", 17)
    ew.set_bold(True)
    t = ew.render("[SPACE] | Try again     [ESC] | Back", True, pygame.color.Color(110,110,255,1))
    r = t.get_rect(center=(wsiz[0]/2, (wsiz[1])-t.get_height()-10))
    window.blit(t, r)
    while gameState == 3:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                bdsfx.stop()
                gameState = 0
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_SPACE:
                    clicksfx.play()
                    gameState = 1
                    bdsfx.stop()
                    return
                elif ev.key == pygame.K_ESCAPE:
                    clicksfx.play()
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



    