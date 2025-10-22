import pygame
import random

pygame.init()
pygame.font.init()

#Font
font = pygame.font.SysFont('Arial', 30)

#Screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#Main Menu
startButton = pygame.Rect((250, 150, 300, 50))
settingsButton = pygame.Rect((250, 250, 300, 50))
exitButton = pygame.Rect((250, 350, 300, 50))
menuText = pygame.Rect((250, 50, 300, 50))

#Settings Buttons
#Uses exit button for back button
shipColorButton = pygame.Rect((250, 150, 300, 50))
difficultyButton = pygame.Rect((250, 250, 300, 50))

#Pause Menu
#Uses exit button for back button
#Uses start button for resume button
#Uses settings button for settings menu

#Ship Colors Menu
shipColorDefaultButton = pygame.Rect((250, 50, 300, 50))
shipColorRedButton = pygame.Rect((250, 150, 300, 50))
shipColorYellowButton = pygame.Rect((250, 250, 300, 50))
shipColorBlueButton = pygame.Rect((250, 350, 300, 50))
shipColorBackButton = pygame.Rect((250, 450, 300, 50))

#Difficulty Menu
difficultyBackButton = pygame.Rect((250, 450, 300, 50))
normalModeButton = pygame.Rect((250, 350, 300, 50))
hardModeButton = pygame.Rect((250, 250, 300, 50))
insaneModeButton = pygame.Rect((250, 150, 300, 50))

#Ship & Meteors
meteor = pygame.Rect(random.randint(0,800), 50, 50, 50)
ship = pygame.Rect((380,450,50,50))
enemy = pygame.Rect((300,250,50,50))

meteorGroup4 = []
extra4 = 0
for i in range(7):
    meteor4 = pygame.Rect(random.randint(10 + extra4,100 + extra4), random.randint(0,15), random.randint(15,60), random.randint(15,60))
    meteorGroup4.append(meteor4)
    extra4 += 100

meteorGroup3 = []
extra3 = 0
for i in range(7):
    meteor3 = pygame.Rect(random.randint(10 + extra3,100 + extra3), random.randint(35,45), random.randint(15,60), random.randint(15,60))
    meteorGroup3.append(meteor3)
    extra3 += 100

meteorGroup2 = []
extra2 = 0
for i in range(7):
    meteor2 = pygame.Rect(random.randint(10 + extra2,100 + extra2), random.randint(65,75), random.randint(15,60), random.randint(15,60))
    meteorGroup2.append(meteor2)
    extra2 += 100

meteorGroup = []
extra = 0
for i in range(7):
    meteor = pygame.Rect(random.randint(10 + extra,100 + extra), random.randint(95,105), random.randint(15,60), random.randint(15,60))
    meteorGroup.append(meteor)
    extra += 100


#Health
heart1 = pygame.Rect((15, 15, 15, 15))
heart2 = pygame.Rect((35, 15, 15, 15))
heart3 = pygame.Rect((55, 15, 15, 15))


#Main Colors
BG = (50, 50, 50)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BROWN = (150, 75, 0)
ORANGE = (255, 69, 0)
YELLOW = (255, 255, 0)
GREY = (128, 128, 128)
DARKGREY = (100, 100, 100)
BLACK = (0, 0, 0)

#Other Colors
SHIPCOL = GREEN
MET1 = BLACK
MET = GREY

#Heart Colors
HRT1 = RED
HRT2 = RED
HRT3 = RED

#Difficulty Settings
health = 3
speed = 500
score = 0
timerDuration = 250
timerDuration2 = 10000

#Show Mouse
pygame.mouse.set_visible(True)

#Menu States
currentMenu = "mainMenu"

startTime = pygame.time.get_ticks()
startTime2 = pygame.time.get_ticks()
run = True
while run:
    pos = pygame.mouse.get_pos()
    xP = enemy.x
    yP = enemy.y
    enemyPos = (xP, yP)

    if currentMenu == "mainMenu":
        #Background Color
        screen.fill(BG)

        STCOL = GREY
        if startButton.collidepoint(pos):
            STCOL = DARKGREY

        SCOL = GREY
        if settingsButton.collidepoint(pos):
            SCOL = DARKGREY

        EXCOL = GREY
        if exitButton.collidepoint(pos):
            EXCOL = DARKGREY

        pygame.draw.rect(screen, STCOL, startButton)
        pygame.draw.rect(screen, SCOL, settingsButton)
        pygame.draw.rect(screen, EXCOL, exitButton)
        pygame.draw.rect(screen, BG, menuText)

        text_surface = font.render("Start", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=startButton.center)
        screen.blit(text_surface, text_rect)

        text_surface = font.render("Settings", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=settingsButton.center)
        screen.blit(text_surface, text_rect)

        text_surface = font.render("Exit", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=exitButton.center)
        screen.blit(text_surface, text_rect)

        text_surface = font.render("Meteors!", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=menuText.center)
        screen.blit(text_surface, text_rect)

    elif currentMenu == "settings":
        screen.fill(BG)
        BBCOL = GREY
        if exitButton.collidepoint(pos):
            BBCOL = DARKGREY
        DBCOL = GREY
        if difficultyButton.collidepoint(pos):
            DBCOL = DARKGREY
        SCBCOL = GREY
        if shipColorButton.collidepoint(pos):
            SCBCOL = DARKGREY
        pygame.draw.rect(screen, BBCOL, exitButton)
        pygame.draw.rect(screen, DBCOL, difficultyButton)
        pygame.draw.rect(screen, SCBCOL, shipColorButton)

        text_surface = font.render("Back", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=exitButton.center)
        screen.blit(text_surface, text_rect)

        text_surface = font.render("Difficulty", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=difficultyButton.center)
        screen.blit(text_surface, text_rect)

        text_surface = font.render("Ship Color", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=shipColorButton.center)
        screen.blit(text_surface, text_rect)

    elif currentMenu == "shipColor":
        screen.fill(BG)
        CRCOL = GREY
        if shipColorRedButton.collidepoint(pos):
            CRCOL = DARKGREY
        CYCOL = GREY
        if shipColorYellowButton.collidepoint(pos):
            CYCOL = DARKGREY
        CBCOL = GREY
        if shipColorBlueButton.collidepoint(pos):
            CBCOL = DARKGREY
        CDCOL = GREY
        if shipColorDefaultButton.collidepoint(pos):
            CDCOL = DARKGREY
        CBBCOL = GREY
        if shipColorBackButton.collidepoint(pos):
            CBBCOL = DARKGREY
        pygame.draw.rect(screen, CRCOL, shipColorRedButton)
        pygame.draw.rect(screen, CYCOL, shipColorYellowButton)
        pygame.draw.rect(screen, CBCOL, shipColorBlueButton)
        pygame.draw.rect(screen, CDCOL, shipColorDefaultButton)
        pygame.draw.rect(screen, CBBCOL, shipColorBackButton)

        text_surface = font.render("Ship Color - Red", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=shipColorRedButton.center)
        screen.blit(text_surface, text_rect)
        text_surface = font.render("Ship Color - Yellow", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=shipColorYellowButton.center)
        screen.blit(text_surface, text_rect)
        text_surface = font.render("Ship Color - Blue", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=shipColorBlueButton.center)
        screen.blit(text_surface, text_rect)
        text_surface = font.render("Ship Color - Default", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=shipColorDefaultButton.center)
        screen.blit(text_surface, text_rect)
        text_surface = font.render("Back", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=shipColorBackButton.center)
        screen.blit(text_surface, text_rect)

    elif currentMenu == "pause":
        screen.fill(BLACK)
        BCOL = GREY
        if startButton.collidepoint(pos):
            BCOL = DARKGREY
        MMCOL = GREY
        if exitButton.collidepoint(pos):
            MMCOL = DARKGREY
        SPCOL = GREY
        if settingsButton.collidepoint(pos):
            SPCOL = DARKGREY
        pygame.draw.rect(screen, BCOL, startButton)
        pygame.draw.rect(screen, MMCOL, exitButton)
        pygame.draw.rect(screen, SPCOL, settingsButton)

        text_surface = font.render("Resume", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=startButton.center)
        screen.blit(text_surface, text_rect)
        text_surface = font.render("Main Menu", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=exitButton.center)
        screen.blit(text_surface, text_rect)
        text_surface = font.render("Settings", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=settingsButton.center)
        screen.blit(text_surface, text_rect)



    elif currentMenu == "game":
        screen.fill(BLACK)
        if health <= 0:
            currentMenu = "lose"
        if score >= 10000:
            currentMenu = "win"

        #Hearts
        if health == 3:
            HRT1 = RED
            HRT2 = RED
            HRT3 = RED
        elif health == 2:
            HRT1 = RED
            HRT2 = RED
            HRT3 = BLACK
        elif health == 1:
            HRT1 = RED
            HRT2 = BLACK
            HRT3 = BLACK
        elif health <= 0:
            HRT1 = BLACK
            HRT2 = BLACK
            HRT3 = BLACK
        pygame.draw.rect(screen, HRT1, heart1)
        pygame.draw.rect(screen, HRT2, heart2)
        pygame.draw.rect(screen, HRT3, heart3)


        #Ship Movement
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            ship.move_ip(-1, 0)
        if key[pygame.K_d]:
            ship.move_ip(1, 0)

        #Drawing Meteors
        for meteor in meteorGroup:
            pygame.draw.rect(screen, GREY, meteor)
        for meteor2 in meteorGroup2:
            pygame.draw.rect(screen, GREY, meteor2)
        for meteor3 in meteorGroup3:
            pygame.draw.rect(screen, GREY, meteor3)
        for meteor4 in meteorGroup4:
            pygame.draw.rect(screen, GREY, meteor4)

        #Health/Collisions
        for meteor in meteorGroup:
            if ship.colliderect(meteor):
                health -= 1
                #fix insta death
        for meteor2 in meteorGroup2:
            if ship.colliderect(meteor2):
                health -= 1
                # fix insta death
        for meteor3 in meteorGroup3:
            if ship.colliderect(meteor3):
                health -= 1
                # fix insta death
        for meteor4 in meteorGroup4:
            if ship.colliderect(meteor4):
                health -= 1
                # fix insta death

        pygame.draw.rect(screen, SHIPCOL, ship)


        currentTime = pygame.time.get_ticks()
        elapsedTime = currentTime - startTime

        if elapsedTime >= timerDuration:
            for meteor in meteorGroup:
                meteor.move_ip(0, random.randint(1,8))
            for meteor2 in meteorGroup2:
                meteor2.move_ip(0, random.randint(1,8))
            for meteor3 in meteorGroup3:
                meteor3.move_ip(0, random.randint(1,8))
            for meteor4 in meteorGroup4:
                meteor4.move_ip(0, random.randint(1,8))
            startTime = pygame.time.get_ticks()


    elif currentMenu == "difficulty":
        screen.fill(BG)

        HMCOL = GREY
        if hardModeButton.collidepoint(pos):
            HMCOL = DARKGREY
        NMCOL = GREY
        if normalModeButton.collidepoint(pos):
            NMCOL = DARKGREY
        IMCOL = GREY
        if insaneModeButton.collidepoint(pos):
            IMCOL = DARKGREY
        DBCOL = GREY
        if difficultyBackButton.collidepoint(pos):
            DBCOL = DARKGREY
        pygame.draw.rect(screen, HMCOL, hardModeButton)
        pygame.draw.rect(screen, NMCOL, normalModeButton)
        pygame.draw.rect(screen, IMCOL, insaneModeButton)
        pygame.draw.rect(screen, DBCOL, difficultyBackButton)

        text_surface = font.render("Insane Mode", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=insaneModeButton.center)
        screen.blit(text_surface, text_rect)

        text_surface = font.render("Hard Mode", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=hardModeButton.center)
        screen.blit(text_surface, text_rect)

        text_surface = font.render("Normal Mode", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=normalModeButton.center)
        screen.blit(text_surface, text_rect)

        text_surface = font.render("Back To Menu", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=difficultyBackButton.center)
        screen.blit(text_surface, text_rect)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if currentMenu == "game":
                    currentMenu = "pause"
                elif currentMenu == "pause":
                    currentMenu = "game"
            #elif event.key == pygame.K_SPACE:
                #if currentMenu == "game":
                    #Shoot Projectile
        if event.type == pygame.MOUSEBUTTONDOWN:
            if currentMenu == "mainMenu":
                if exitButton.collidepoint(pos):
                    run = False
                elif startButton.collidepoint(pos):
                    currentMenu = "game"
                elif settingsButton.collidepoint(pos):
                    currentMenu = "settings"
            elif currentMenu == "settings":
                if exitButton.collidepoint(pos):
                    currentMenu = "mainMenu"
                if shipColorButton.collidepoint(pos):
                    currentMenu = "shipColor"
                if difficultyButton.collidepoint(pos):
                    currentMenu = "difficulty"
            elif currentMenu == "shipColor":
                if shipColorBackButton.collidepoint(pos):
                    currentMenu = "settings"
                elif shipColorDefaultButton.collidepoint(pos):
                    SHIPCOL = GREEN
                elif shipColorRedButton.collidepoint(pos):
                    SHIPCOL = RED
                elif shipColorBlueButton.collidepoint(pos):
                    SHIPCOL = BLUE
                elif shipColorYellowButton.collidepoint(pos):
                    SHIPCOL = YELLOW
            elif currentMenu == "pause":
                if startButton.collidepoint(pos):
                    currentMenu = "game"
                elif exitButton.collidepoint(pos):
                    currentMenu = "mainMenu"
                elif settingsButton.collidepoint(pos):
                    currentMenu = "settings"
            elif currentMenu == "difficulty":
                if insaneModeButton.collidepoint(pos):
                    timerDuration = 80
                    timerDuration2 = 350
                    health = 1
                elif hardModeButton.collidepoint(pos):
                    timerDuration = 150
                    timerDuration2 = 600
                    health = 2
                elif normalModeButton.collidepoint(pos):
                    timerDuration = 250
                    timerDuration2 = 1000
                    health = 3
                elif difficultyBackButton.collidepoint(pos):
                    currentMenu = "settings"
    pygame.display.update()
pygame.quit()