import pygame
import colors as c

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = SCREEN_WIDTH * 0.7

FPS = 60

overwall = pygame.Rect(0,0,SCREEN_WIDTH,1)
underwall = pygame.Rect(0,SCREEN_HEIGHT,SCREEN_WIDTH,1)
leftwall = pygame.Rect(0,0,1,SCREEN_HEIGHT)
rightwall = pygame.Rect(SCREEN_WIDTH,0,1,SCREEN_HEIGHT)

def picture(picture,x,y,width,height,surface):
    pic = pygame.image.load(picture).convert_alpha()
    pic = pygame.transform.scale(pic,(width,height))
    surface.blit(pic,(x,y))

def drawrect(surface,color,rect):
    pygame.draw.rect((surface,color,rect))

def time():
    clock = pygame.time.Clock()
    clock.tick(FPS)

def drawsword(rect,surface,right):
    if right == False:
        pygame.draw.rect(surface,c.WHITE,(rect[0]-rect[2],rect[1],rect[2]*1.6,rect[3]/3))
    if right == True:
        pygame.draw.rect(surface,c.WHITE,(rect[0]+rect[2]/2.2,rect[1],rect[2]*1.6,rect[3]/3))
def drawswordbox(rect,surface):
    pygame.draw.rect(surface,c.BROWN,rect)
    pygame.draw.rect(surface,c.WHITE,(rect[0],rect[1]+rect[3]/4,rect[2],rect[3]/4))
def drawstick(rect,surface,right,shoot):
    if right == True:
        if shoot == False:
            pygame.draw.rect(surface,c.WHITE,(rect[0]+rect[2],rect[1],rect[2]/3,rect[3]/3))
        else:
            pygame.draw.rect(surface, c.WHITE, (rect[0] + rect[2], rect[1], rect[2]*2, rect[3] / 3))
    else:
        if shoot == False:
            pygame.draw.rect(surface,c.WHITE,(rect[0]-rect[2]/3,rect[1],rect[2]/3,rect[3]/3))
        else:
            pygame.draw.rect(surface, c.WHITE, (rect[0]-rect[2]*2, rect[1], rect[2]*2, rect[3] / 3))

def drawstickbox(rect,surface):
    pygame.draw.rect(surface,c.BROWN,rect)
    pygame.draw.rect(surface,c.WHITE,(rect[0]+rect[2]/2,rect[1]+rect[3]/2,rect[2]/5,rect[3]/5))

def drawplayera(surface,rect,right,health,shoot,art):
    if right == False:
        pygame.draw.rect(surface,(c.RED),rect)
        pygame.draw.rect(surface,(c.BLACK),(rect[0],rect[1]+(rect[3]/2),rect[2] / 2,rect[3]/7.5))
        if art == 1:
            if shoot == False:
                pygame.draw.rect(surface, c.WHITE, (rect[0] + rect[2] * 1.1-(rect[2]*1.5), rect[1] / 1.03, rect[2] / 3, rect[3]))
            else:
                pygame.draw.rect(surface, c.WHITE, ((rect[0] + rect[2] * 1.1-(rect[2]*1.5))-rect[3],(rect[1] / 1.03)+(rect[3]), rect[3],rect[2] / 3))
        if art == 2:
            if shoot == False:
                drawsword(rect,surface,right)
            else:
                drawsword((rect[0],rect[1]+30,rect[2],rect[3]),surface,right)
        if art == 3:
            drawstick(rect,surface,right,shoot)
    if right == True:
        pygame.draw.rect(surface,(c.RED),rect)
        pygame.draw.rect(surface,(c.BLACK),(rect[0]+(rect[2]/2),rect[1]+(rect[3]/2),rect[2] / 2,rect[3]/7.5))
        if art == 1:
            if shoot == False:
                pygame.draw.rect(surface, c.WHITE,(rect[0]+rect[2]*1.1,rect[1]/1.03,rect[2]/3,rect[3]))
            else:
                pygame.draw.rect(surface, c.WHITE,(rect[0]+rect[2]*1.1,(rect[1]/1.03)+rect[3],rect[3],rect[2]/3))
        if art == 2:
            if shoot == False:
               drawsword(rect,surface,right)
            else:
                drawsword((rect[0],rect[1]+30,rect[2],rect[3]),surface,right)
        if art == 3:
            drawstick(rect,surface,right,shoot)
    pygame.draw.rect(surface, c.WHITE, (47, 47, 306, 36))
    pygame.draw.rect(surface, c.YELLOW, (50, 50, 300, 30))
    pygame.draw.rect(surface, c.RED, (50, 50, health, 30))
def drawplayerb(surface,rect,right,health,shoot,art):
    if right == False:
        pygame.draw.rect(surface,(c.BLUE),rect)
        pygame.draw.rect(surface,(c.BLACK),(rect[0],rect[1]+(rect[3]/2),rect[2] / 2,rect[3]/7.5))
        if art == 1:
            if shoot == False:
                pygame.draw.rect(surface, c.WHITE, (rect[0] + rect[2] * 1.1-(rect[2]*1.5), rect[1] / 1.03, rect[2] / 3, rect[3]))
            else:
                pygame.draw.rect(surface, c.WHITE, ((rect[0] + rect[2] * 1.1-(rect[2]*1.5))-rect[3],(rect[1] / 1.03)+(rect[3]), rect[3],rect[2] / 3))
        if art == 2:
            if shoot == False:
                drawsword(rect,surface,right)
            else:
                drawsword((rect[0],rect[1]+30,rect[2],rect[3]),surface,right)

    if right == True:
        pygame.draw.rect(surface,(c.BLUE),rect)
        pygame.draw.rect(surface,(c.BLACK),(rect[0]+(rect[2]/2),rect[1]+(rect[3]/2),rect[2] / 2,rect[3]/7.5))
        if art == 1:
            if shoot == False:
                pygame.draw.rect(surface, c.WHITE,(rect[0]+rect[2]*1.1,rect[1]/1.03,rect[2]/3,rect[3]))
            else:
                pygame.draw.rect(surface, c.WHITE,(rect[0]+rect[2]*1.1,(rect[1]/1.03)+rect[3],rect[3],rect[2]/3))
        if art == 2:
            if shoot == False:
                drawsword(rect,surface,right)
            else:
                drawsword((rect[0],rect[1]+30,rect[2],rect[3]),surface,right)

    if art == 3:
        drawstick(rect,surface,right,shoot)

    pygame.draw.rect(surface, c.WHITE, (647, 47, 306, 36))
    pygame.draw.rect(surface, c.YELLOW, (650, 50, 300, 30))
    pygame.draw.rect(surface, c.RED, (650, 50, health, 30))


def drawground(surface,rect):
    pygame.draw.rect(surface,c.GREEN,rect)


def picture(picture,x,y,width,height,surface):
    pic = pygame.image.load(picture).convert_alpha()
    pic = pygame.transform.scale(pic,(width,height))
    surface.blit(pic,(x,y))

def drawswordtimea(sword,swordtime,surface):
    if not sword == 1:
        pygame.draw.rect(surface, c.WHITE, (47, 147, 306, 36))
        pygame.draw.rect(surface, c.PINK, (50, 150, 300, 30))
        pygame.draw.rect(surface, c.PURPLE, (50, 150, swordtime, 30))
def drawswordtimeb(sword,swordtime,surface):
    if not sword == 1:
        pygame.draw.rect(surface, c.WHITE, (647, 147, 306, 36))
        pygame.draw.rect(surface, c.PINK, (650, 150, 300, 30))
        pygame.draw.rect(surface, c.PURPLE, (650, 150, swordtime, 30))

def thingfall(surface,rect,thing):
    if thing == 1:
        drawswordbox(rect,surface)
    if thing == 2:
        picture("assets/Bilder/live.png",rect[0],rect[1],rect[2],rect[3],surface)
    if thing == 3:
        drawstickbox(rect,surface)

clock = pygame.time.Clock()