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

#Win
startWinButton = pygame.Rect((250, 150, 300, 50))
exitWinButton = pygame.Rect((250, 350, 300, 50))
winText = pygame.Rect((250, 50, 300, 50))

#Menu
startButton = pygame.Rect((250, 150, 300, 50))
settingsButton = pygame.Rect((250, 250, 300, 50))
exitButton = pygame.Rect((250, 350, 300, 50))
menuText = pygame.Rect((250, 50, 300, 50))

#Settings Buttons
backButton = pygame.Rect((250, 350, 300, 50))
playerSelButton = pygame.Rect((250, 250, 300, 50))
enemyColorButton = pygame.Rect((250, 150, 300, 50))

#Pause
mainMenuButton = pygame.Rect((250, 250, 300, 50))

#Color Buttons
playerSelDefaultButton = pygame.Rect((250, 50, 300, 50))
playerSelRedButton = pygame.Rect((250, 150, 300, 50))
playerSelYellowButton = pygame.Rect((250, 250, 300, 50))
playerSelBlueButton = pygame.Rect((250, 350, 300, 50))
playerSelBackButton = pygame.Rect((250, 450, 300, 50))

#Enemy Color Buttons
enemyColorDefaultButton = pygame.Rect((250, 50, 300, 50))
enemyColorRedButton = pygame.Rect((250, 150, 300, 50))
enemyColorOrangeButton = pygame.Rect((250, 250, 300, 50))
enemyColorBlueButton = pygame.Rect((250, 350, 300, 50))
enemyColorBackButton = pygame.Rect((250, 450, 300, 50))

#Enemy/Moles
enemy = pygame.Rect(random.randint(0,800), random.randint(0,600), 50, 50)

#Colors
BG = (50, 50, 50)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 69, 0)
YELLOW = (255, 255, 0)
GREY = (128, 128, 128)
DARKGREY = (100, 100, 100)
BLACK = (0, 0, 0)
GREENRGB = (0, 255, 0)
YELLOWRGB = (255, 255, 0)

#Show Mouse
pygame.mouse.set_visible(True)

#Menu States
current_menu = "mainMenu"

run = True
while run:
    pos = pygame.mouse.get_pos()
    if current_menu == "mainMenu":
        # Background Color
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

        text_surface = font.render("Wack-a-Mole", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=menuText.center)
        screen.blit(text_surface, text_rect)

    elif current_menu == "settings":
        screen.fill(BG)
        BCOL = GREY
        if backButton.collidepoint(pos):
            BCOL = DARKGREY
        BCCOL = GREY
        if playerSelButton.collidepoint(pos):
            BCCOL = DARKGREY
        ECCOL = GREY
        if enemyColorButton.collidepoint(pos):
            ECCOL = DARKGREY
        pygame.draw.rect(screen, BCOL, backButton)
        pygame.draw.rect(screen, BCCOL, playerSelButton)
        pygame.draw.rect(screen, ECCOL, enemyColorButton)

        text_surface = font.render("Back", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=backButton.center)
        screen.blit(text_surface, text_rect)

        text_surface = font.render("Player Select Color", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=playerSelButton.center)
        screen.blit(text_surface, text_rect)

        text_surface = font.render("Enemy Color", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=enemyColorButton.center)
        screen.blit(text_surface, text_rect)
    elif current_menu == "color":
        screen.fill(BG)
        COL1 = GREY
        if playerSelRedButton.collidepoint(pos):
            COL1 = DARKGREY
        COL2 = GREY
        if playerSelYellowButton.collidepoint(pos):
            COL2 = DARKGREY
        COL3 = GREY
        if playerSelBlueButton.collidepoint(pos):
            COL3 = DARKGREY
        COL4 = GREY
        if playerSelDefaultButton.collidepoint(pos):
            COL4 = DARKGREY
        COL5 = GREY
        if playerSelBackButton.collidepoint(pos):
            COL5 = DARKGREY
        pygame.draw.rect(screen, COL1, playerSelRedButton)
        pygame.draw.rect(screen, COL2, playerSelYellowButton)
        pygame.draw.rect(screen, COL3, playerSelBlueButton)
        pygame.draw.rect(screen, COL4, playerSelDefaultButton)
        pygame.draw.rect(screen, COL5, playerSelBackButton)

        text_surface = font.render("Player Select - Red", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=playerSelRedButton.center)
        screen.blit(text_surface, text_rect)
        text_surface = font.render("Player Select - Yellow", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=playerSelYellowButton.center)
        screen.blit(text_surface, text_rect)
        text_surface = font.render("Player Select - Blue", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=playerSelBlueButton.center)
        screen.blit(text_surface, text_rect)
        text_surface = font.render("Player Select - Default", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=playerSelDefaultButton.center)
        screen.blit(text_surface, text_rect)
        text_surface = font.render("Back", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=playerSelBackButton.center)
        screen.blit(text_surface, text_rect)

    elif current_menu == "Ecolor":
        screen.fill(BG)
        COL11 = GREY
        if enemyColorRedButton.collidepoint(pos):
            COL11 = DARKGREY
        COL22 = GREY
        if enemyColorOrangeButton.collidepoint(pos):
            COL22 = DARKGREY
        COL33 = GREY
        if enemyColorBlueButton.collidepoint(pos):
            COL33 = DARKGREY
        COL44 = GREY
        if enemyColorDefaultButton.collidepoint(pos):
            COL44 = DARKGREY
        COL55 = GREY
        if enemyColorBackButton.collidepoint(pos):
            COL55 = DARKGREY
        pygame.draw.rect(screen, COL11, enemyColorRedButton)
        pygame.draw.rect(screen, COL22, enemyColorOrangeButton)
        pygame.draw.rect(screen, COL33, enemyColorBlueButton)
        pygame.draw.rect(screen, COL44, enemyColorDefaultButton)
        pygame.draw.rect(screen, COL55, enemyColorBackButton)

        text_surface = font.render("Enemy Color - Red", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=enemyColorRedButton.center)
        screen.blit(text_surface, text_rect)
        text_surface = font.render("Enemy Color - Orange", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=enemyColorOrangeButton.center)
        screen.blit(text_surface, text_rect)
        text_surface = font.render("Enemy Color - Blue", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=enemyColorBlueButton.center)
        screen.blit(text_surface, text_rect)
        text_surface = font.render("Enemy Color - Default", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=enemyColorDefaultButton.center)
        screen.blit(text_surface, text_rect)
        text_surface = font.render("Back", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=enemyColorBackButton.center)
        screen.blit(text_surface, text_rect)


    elif current_menu == "game":
        screen.fill(BLACK)


        # Enemy Color
        SELCOL = GREEN
        ECOL = YELLOWRGB
        if enemy.collidepoint(pos):
            ECOL = SELCOL

        pygame.draw.rect(screen, ECOL, enemy)

        key = pygame.key.get_pressed()

    elif current_menu == "pause":
        screen.fill(BLACK)
        BCOL = GREY
        if backButton.collidepoint(pos):
            BCOL = DARKGREY
        MMCOL = GREY
        if mainMenuButton.collidepoint(pos):
            MMCOL = DARKGREY
        pygame.draw.rect(screen, BCOL, backButton)
        pygame.draw.rect(screen, MMCOL, mainMenuButton)
        text_surface = font.render("Back", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=backButton.center)
        screen.blit(text_surface, text_rect)
        text_surface = font.render("Main Menu", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=mainMenuButton.center)
        screen.blit(text_surface, text_rect)
    elif current_menu == "win":
        # Background Color
        screen.fill(BG)

        STWCOL = GREY
        if startButton.collidepoint(pos):
            STWCOL = DARKGREY

        SWCOL = GREY
        if settingsButton.collidepoint(pos):
            SWCOL = DARKGREY

        EXWCOL = GREY
        if exitButton.collidepoint(pos):
            EXWCOL = DARKGREY
        pygame.draw.rect(screen, BG, winText)
        pygame.draw.rect(screen, STWCOL, startWinButton)
        pygame.draw.rect(screen, EXWCOL, exitWinButton)

        text_surface = font.render("Replay", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=startWinButton.center)
        screen.blit(text_surface, text_rect)

        text_surface = font.render("Exit", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=exitWinButton.center)
        screen.blit(text_surface, text_rect)

        text_surface = font.render("You Win!", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=winText.center)
        screen.blit(text_surface, text_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if current_menu == "mainMenu":
                if exitButton.collidepoint(pos):
                    run = False
                elif startButton.collidepoint(pos):
                    current_menu = "game"
                elif settingsButton.collidepoint(pos):
                    current_menu = "settings"
            elif current_menu == "win":
                if exitWinButton.collidepoint(pos):
                    run = False
                elif startWinButton.collidepoint(pos):
                    current_menu = "game"
            elif current_menu == "settings":
                if backButton.collidepoint(pos):
                    current_menu = "mainMenu"
                if playerSelButton.collidepoint(pos):
                    current_menu = "color"
                if enemyColorButton.collidepoint(pos):
                    current_menu = "Ecolor"
            elif current_menu == "color":
                if playerSelBackButton.collidepoint(pos):
                    current_menu = "settings"
                elif playerSelDefaultButton.collidepoint(pos):
                    SELCOL = GREEN
                elif playerSelRedButton.collidepoint(pos):
                    SELCOL = RED
                elif playerSelBlueButton.collidepoint(pos):
                    SELCOL = BLUE
                elif playerSelYellowButton.collidepoint(pos):
                    SELCOL = YELLOW
            elif current_menu == "Ecolor":
                if enemyColorBackButton.collidepoint(pos):
                    current_menu = "settings"
                elif enemyColorDefaultButton.collidepoint(pos):
                    YELLOWRGB = YELLOW
                elif enemyColorRedButton.collidepoint(pos):
                    YELLOWRGB = RED
                elif enemyColorBlueButton.collidepoint(pos):
                    YELLOWRGB = BLUE
                elif enemyColorOrangeButton.collidepoint(pos):
                    YELLOWRGB = ORANGE
            elif current_menu == "pause":
                if backButton.collidepoint(pos):
                    current_menu = "game"
                elif mainMenuButton.collidepoint(pos):
                    current_menu = "mainMenu"
            elif current_menu == "game":
                if enemy.collidepoint(pos):
                    current_menu = "win"
                    enemy = pygame.Rect(random.randint(0,800), random.randint(0,600), 50, 50)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if current_menu == "game":
                    current_menu = "pause"
                elif current_menu == "pause":
                    current_menu = "game"
    pygame.display.update()
pygame.quit()