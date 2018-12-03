""" Enermy AI test01 """

""" Main process of game. """
##import charector
##import inventory
##import hud
import pygame,random,math
from pygame.locals import *

## Import sprite zone
Img_Tree_A_1 = pygame.image.load("world/Tree/A_1.png")
Img_Tree_A_2 = pygame.image.load("world/Tree/A_2.png")
Img_Tree_B_1 = pygame.image.load("world/Tree/B_1.png")
Img_Tree_B_2 = pygame.image.load("world/Tree/B_2.png")
Img_Tree_C_1 = pygame.image.load("world/Tree/C_1.png")
Img_Tree_C_2 = pygame.image.load("world/Tree/C_2.png")
Img_Tree_D = pygame.image.load("world/Tree/D.png")
Img_Rock = pygame.image.load("world/rock.png")
Img_Floor = pygame.image.load("world/floor.png")
Img_Height_ground_01 = pygame.image.load("world/Height_ground_1/01.png")
Img_Height_ground_02 = pygame.image.load("world/Height_ground_1/02.png")
Img_Height_ground_03 = pygame.image.load("world/Height_ground_1/03.png")
Img_Height_ground_04 = pygame.image.load("world/Height_ground_1/04.png")
Img_Height_ground_05 = pygame.image.load("world/Height_ground_1/05.png")
Img_Height_ground_06 = pygame.image.load("world/Height_ground_1/06.png")
Img_Height_ground_07 = pygame.image.load("world/Height_ground_1/07.png")
Img_Height_ground_08 = pygame.image.load("world/Height_ground_1/08.png")
Img_Height_ground_09 = pygame.image.load("world/Height_ground_1/09.png")
Img_Height_ground_10 = pygame.image.load("world/Height_ground_1/10.png")
Img_Height_ground_11 = pygame.image.load("world/Height_ground_1/11.png")
Img_Height_ground_12 = pygame.image.load("world/Height_ground_1/12.png")
Img_Height_ground_door = pygame.image.load("world/Height_ground_1/door.png")
Img_Height_ground_door_closed = pygame.image.load("world/Height_ground_1/door_closed.png")
Img_Flower_1 = pygame.image.load("world/Flower/1.png")
Img_Flower_2 = pygame.image.load("world/Flower/2.png")
Img_Flower_3 = pygame.image.load("world/Flower/3.png")
Img_Player_up1 = pygame.image.load("charector/player/up1.png")
Img_Player_up2 = pygame.image.load("charector/player/up2.png")
Img_Player_down1 = pygame.image.load("charector/player/down1.png")
Img_Player_down2 = pygame.image.load("charector/player/down2.png")
Img_Player_left1 = pygame.image.load("charector/player/left1.png")
Img_Player_left2 = pygame.image.load("charector/player/left2.png")
Img_Player_right1 = pygame.image.load("charector/player/right1.png")
Img_Player_right2 = pygame.image.load("charector/player/right2.png")
##
## Setup zon
display_width = 1600
display_height = 900
current_scence = "jungle_1"
scence_item_size = 32
##
## Processing zone

screen = pygame.display.set_mode((display_width, display_height), pygame.FULLSCREEN)

def draw_title():
    screen.fill(Color("Grey"))
    screen.blit(Img_Flower_1,(800,800))
    pygame.display.flip()

##draw_title()

def draw_scence(scence):
    if scence == "jungle_1":
        screen.fill(Color("Grey"))
        screen.blit(Img_Height_ground_01, (0, 0))
        for i in range(1,10):
            screen.blit(Img_Height_ground_02, (scence_item_size*i, 0))
        screen.blit(Img_Height_ground_03, (scence_item_size*10, 0))
        for i in range(1,10):
            screen.blit(Img_Height_ground_04, (0, scence_item_size*i))
        screen.blit(Img_Height_ground_07, (0, scence_item_size*10))

    screen.blit(Img_Height_ground_01, (scence_item_size*0, 700))
    screen.blit(Img_Height_ground_02, (scence_item_size*1, 700))
    screen.blit(Img_Height_ground_03, (scence_item_size*2, 700))
    screen.blit(Img_Height_ground_04, (scence_item_size*3, 700))
    screen.blit(Img_Height_ground_05, (scence_item_size*4, 700))
    screen.blit(Img_Height_ground_06, (scence_item_size*5, 700))
    screen.blit(Img_Height_ground_07, (scence_item_size*6, 700))
    screen.blit(Img_Height_ground_08, (scence_item_size*7, 700))

def move(x, y):
    screen.blit(Img_Player, (x, y))

def event_control():
    x = (display_width * 0.5)
    y = (display_height * 0.5)
    x_acc = 0
    y_acc = 0
    Img_Player = Img_Player_down2
    while True:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                   pygame.quit()
                   quit()
                if event.key == K_UP:
                    y_acc = -3
                    Img_Player = Img_Player_up2
                if event.key == K_DOWN:
                    y_acc = 3
                    Img_Player = Img_Player_down2
                if event.key == K_LEFT:
                    x_acc = -3
                    Img_Player = Img_Player_left2
                if event.key == K_RIGHT:
                    x_acc = 3
                    Img_Player = Img_Player_right2

            if event.type == KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        x_acc = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_acc = 0
        x +=  x_acc
        y +=  y_acc
        draw_scence(current_scence)
        screen.blit(Img_Player, (x, y))
        pygame.display.update()

def game_loop():
    draw_scence(current_scence)
    event_control()
    pygame.quit()
    quit()

game_loop()

