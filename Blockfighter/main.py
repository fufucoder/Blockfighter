import pygame
import random
import variables as v
import colors as c

screen = pygame.display.set_mode((v.SCREEN_WIDTH,v.SCREEN_HEIGHT))

playerax = 100
playeray = 600
playera = pygame.Rect(playerax,playeray,50,50)
righta = True
jumpa = 0
healtha = 300
shoota = False
swoa = False
arta = 1

playerbx = 700
playerby = 600
playerb = pygame.Rect(playerbx,playerby,50,50)
rightb = False
jumpb = 0
healthb = 300
shootb = False
swob = False
artb = 3
swordtimea = 30000

thingtime = 0
thing = 0
thingrect = (0,0,0,0)
thingx = 0
thingy = 0
swordtimeb = 30000

strun = True
startx = 0
while strun:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()

  v.time()
  v.picture("assets/Bilder/Blockfighter.png",0,0,v.SCREEN_WIDTH,v.SCREEN_HEIGHT,screen)
  pygame.draw.rect(screen,c.BLACK,(startx,0,v.SCREEN_WIDTH,v.SCREEN_WIDTH))
  startx += 3
  if startx > v.SCREEN_WIDTH:
    strun = False

  pygame.display.update()

gamerun = True
while gamerun:

  run = True
  while run:
    v.time()

    thingtime += v.FPS

    swordtimea -= v.FPS
    swordtimeb -= v.FPS

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()

    screen.fill(c.GREY)

    if thingtime > 30000:
      thingtime = 0
      thing = random.randint(1,3)
      thingx = random.randint(50,950)
      thingy = 0
    if not thing == 0:
      thingy += 7.5
      thingrect = pygame.Rect(thingx,thingy,50,50)
      v.thingfall(screen,thingrect,thing)

    if playera.colliderect(thingrect):
      if thing == 1:
        arta = 2
        swordtimea = 30000
      if thing == 2:
        healtha += 100
        if healtha > 300:
          healtha = 300
        thing = 0
        thingrect = (0,0,0,0)
      if thing == 3:
        arta = 3
        swordtimea = 30000
    if playerb.colliderect(thingrect):
      if thing == 1:
        artb = 2
        swordtimeb = 30000
      if thing == 2:
        healthb += 100
        if healthb > 300:
          healthb = 300
        thing = 0
        thingrect = (0,0,0,0)
      if thing == 3:
        artb = 3
        swordtimeb = 30000

    v.drawswordtimea(arta,swordtimea/100,screen)
    v.drawswordtimeb(artb,swordtimeb/100,screen)
    if swordtimea < 0:
      arta = 1
    if swordtimeb < 0:
      artb = 1

    if thingy > 650:
      thing = 0
      thingrect = (0,0,0,0)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and not playera.colliderect(v.leftwall):
      playerax -= 5
      righta = False
    if keys[pygame.K_d] and not playera.colliderect(v.rightwall):
      playerax += 5
      righta = True
    if keys[pygame.K_w] and jumpa == 0:
      jumpa = 10
    if keys[pygame.K_s]:
      if arta == 1:
        shoota = True
        if righta == True:
          sworda = pygame.Rect(playerax+playera[2],playeray,playera[2],playera[3])
        else:
          sworda = pygame.Rect(playerax-playera[2],playeray,playera[2],playera[3])
        if sworda.colliderect(playerb) and swoa == False:
          healthb -= 10
        swoa = True
      if arta == 2:
        shoota = True
        if righta == True:
          sworda = pygame.Rect(playerax+playera[2],playeray,playera[2],playera[3])
        else:
          sworda = pygame.Rect(playerax-playera[2],playeray,playera[2],playera[3])
        if sworda.colliderect(playerb) and swoa == False:
          healthb -= 30
        swoa = True
      if arta == 3:
        shoota = True
        if righta == True:
          sworda = pygame.Rect(playerax + playera[2], playeray, playera[2]*2.5, playera[3])
        else:
          sworda = pygame.Rect(playerax - playera[2]*2.5, playeray, playera[2]*2.5, playera[3])
        if sworda.colliderect(playerb) and swoa == False:
          healthb -= 5
        swoa = True

    else:
      shoota = False
      swoa = False

    if keys[pygame.K_LEFT] and not playerb.colliderect(v.leftwall):
      playerbx -= 5
      rightb = False
    if keys[pygame.K_RIGHT] and not playerb.colliderect(v.rightwall):
      playerbx += 5
      rightb = True
    if keys[pygame.K_UP] and jumpb == 0:
      jumpb = 10
    if keys[pygame.K_DOWN]:
      if artb == 1:
        shootb = True
        if rightb == True:
          swordb = pygame.Rect(playerbx + playerb[2], playerby, playerb[2], playerb[3])
        else:
          swordb = pygame.Rect(playerbx - playerb[2], playerby, playerb[2], playerb[3])
        if swordb.colliderect(playera) and swob == False:
          healtha -= 10
        swob = True
      if artb == 2:
        shootb = True
        if rightb == True:
          swordb = pygame.Rect(playerbx + playerb[2], playerby, playerb[2], playerb[3])
        else:
          swordb = pygame.Rect(playerbx - playerb[2], playerby, playerb[2], playerb[3])
        if swordb.colliderect(playera) and swob == False:
          healtha -= 30
        swob = True
      if artb == 3:
        shootb = True
        if rightb == True:
          swordb = pygame.Rect(playerbx + playerb[2], playerby, playerb[2]*2.5, playerb[3])
        else:
          swordb = pygame.Rect(playerbx - playerb[2]*2.5, playerby, playerb[2]*2.5, playerb[3])
        if swordb.colliderect(playera) and swob == False:
          healtha -= 5
        swob = True
    else:
      shootb = False
      swob = False

    if not jumpa == 0:
      jumpa -= 0.51
    if not jumpb == 0:
      jumpb -= 0.51

    playeray -= jumpa
    playera = pygame.Rect(playerax,playeray,50,50)
    v.drawplayera(screen,playera,righta,healtha,shoota,arta)

    playerby -= jumpb
    playerb = pygame.Rect(playerbx,playerby,50,50)
    v.drawplayerb(screen,playerb,rightb,healthb,shootb,artb)

    ground = (0,650,1000,250)
    v.drawground(screen,ground)

    if playerby>600:
      playerby = 601
      jumpb = 0

    if playeray>600:
      playeray = 601
      jumpa = 0

    if healthb < 1:
      run = False

    if healtha < 1:
      run = False

    pygame.display.update()

  running = True
  while running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
      if mouse.colliderect(restartbutton) and event.type == pygame.MOUSEBUTTONDOWN:
        playerax = 100
        playeray = 600
        playera = pygame.Rect(playerax, playeray, 50, 50)
        righta = True
        jumpa = 0
        healtha = 300
        shoota = False
        swoa = False
        arta = 1
        playerbx = 700
        playerby = 600
        playerb = pygame.Rect(playerbx, playerby, 50, 50)
        rightb = False
        jumpb = 0
        healthb = 300
        shootb = False
        swob = False
        artb = 1
        running = False

    screen.fill(c.WHITE)

    if healthb < 1:
      v.picture("assets/Bilder/redwin.png",0,0,1000,500,screen)
    else:
      v.picture("assets/Bilder/bluewin.png",0,0,1050,500,screen)

    mouse = pygame.Rect(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1],3,3)
    pygame.draw.rect(screen,c.GREEN,(45,495,160,60))
    restartbutton = pygame.Rect(50,500,150,50)
    pygame.draw.rect(screen,c.LIGHTGREEN,restartbutton)
    v.picture("assets/Bilder/restart.png",50,500,150,50,screen)

    pygame.display.update()