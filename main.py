import pygame
from keymap import *

#Setting
pygame.init()

screenResolution = (640, 480)
gameCaption = "test game"
gameFont = pygame.font.SysFont("Arial", 12)
FPS = 60

pygame.display.set_caption(gameCaption)
surface = pygame.display.set_mode(screenResolution)
clock = pygame.time.Clock()
keyboardPrev = []
keyboardInput = []
instanceList = []

class Object(object):
    def __init__(self, x=0, y=0):
        super(Object, self).__init__()
        self.x = x
        self.y = y

    def init(self):
        pass

    def update(self):
        pass

#--- Objects ---
#Player
class Player(Object):
    def init(self):
        print("the game is running on "+str(displayGetWidth())+"x"+str(displayGetHeight())+" screen")
        self.hp = 100;
        self.speed=2;
        ins = instanceCreate(GPS)
        ins.track = self

    def update(self):
        pygame.draw.rect(surface,(0,0,0),[self.x,self.y,32,32])
        if(keyboardButton(K_UP)):
            self.y-=self.speed
        if(keyboardButton(K_DOWN)):
            self.y+=self.speed
        if(keyboardButton(K_RIGHT)):
            self.x+=self.speed
        if(keyboardButton(K_LEFT)):
            self.x-=self.speed
#GPS
class GPS(Object):
    def update(self):
        if (self.track != self):
            drawText(10, 10, "x:"+str(self.track.x)+" y:"+str(self.track.y))



#Game End
def gameEnd():
    pygame.quit()
    quit()

#Useful Function
def drawText(x,y,text="", color=(000,000,000)):
    _txt = gameFont.render(str(text), True, color)
    surface.blit(_txt, (x, y))

def displayGetWidth():
    return screenResolution[0]

def displayGetHeight():
    return screenResolution[1]

def keyboardButton(key):
    try:
        if(keyboardInput[key]):
            return True
    except:
        return False

def keyboardReleased(key):
    try:
        if(keyboardPrev[key] and not keyboardInput[key]):
            return True
    except:
        return False

def keyboardPressed(key):
    try:
        if(not keyboardPrev[key] and keyboardInput[key]):
            return True
    except:
        return False

def instanceCreate(obj, x=0, y=0):
    ins = obj(x, y)
    instanceList.append(ins)
    return ins

#Game Init
def gameInit():
    instanceCreate(Player, 200, 200)

#Game Start
def gameStart():
    gameInit()
    for instance in instanceList:
        instance.init()
    while(True):
        #Background
        surface.fill((255,255,255))

        #Get Input
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                gameEnd()
            global keyboardInput
            keyboardInput = pygame.key.get_pressed()
        #Run through instances
        for instance in instanceList:
            instance.update()

        global keyboardPrev
        keyboardPrev = keyboardInput
        pygame.display.update()
        clock.tick(FPS)

gameStart()
