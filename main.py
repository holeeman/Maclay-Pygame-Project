import pygame
from keymap import *
import math

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

class Sprite(object):
    def __init__(self, file_name, width=0, height=0, alpha=True, transparent=(000,000,000)):
        if(alpha):
            self.sprite_sheet = pygame.image.load(file_name).convert_alpha()
        else:
            self.sprite_sheet = pygame.image.load(file_name).convert()
        self.sprite = []
        self.sheet_width= self.sprite_sheet.get_size()[0]
        self.sheet_height= self.sprite_sheet.get_size()[1]
        self.image_count=0
        if(width==0 or height==0):
            width = self.sheet_width
            height = self.sheet_height

        for yy in range(self.sheet_height/height):
            for xx in range(self.sheet_width/width):
                image = pygame.Surface([width, height]).convert()
                image.blit(self.sprite_sheet, (0, 0), (xx*width, yy*height, width, height))
                image.set_colorkey(transparent)
                self.sprite.append(image)
                self.image_count+=1
        print self.image_count
    def get_image(self, index):
        try:
            return self.sprite[index]
        except:
            return self.sprite[0]


#--- Objects ---
#Player
class Player(Object):
    def init(self):
        print("the game is running on "+str(displayGetWidth())+"x"+str(displayGetHeight())+" screen")
        self.hp = 100;
        self.speed=2;
        self.test = Sprite("idle.png",150,150)
        self.image=self.test.get_image(0)
        self.image_index = 0;
        ins = instanceCreate(GPS)
        ins.track = self

    def update(self):
        self.image=self.test.get_image(int(math.floor(self.image_index/(FPS/(self.test.image_count-1)))))
        self.image_index += 1;
        if(self.image_index > FPS):
            self.image_index = 0

        surface.blit(self.image, (self.x,self.y))
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
