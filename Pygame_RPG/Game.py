""" Main process of game. """
##import charector
##import inventory
##import hud
import pygame,random,math,time
from pygame.locals import *
from firebase import firebase
from copy import deepcopy ## for copy list and keep original val
## Firebase handle
url = 'https://pygame-rpg01-223910.firebaseio.com/'
messenger = firebase.FirebaseApplication(url)
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
Img_Player_up_idle = pygame.image.load("charector/player/up_idle.png")
Img_Player_up1 = pygame.image.load("charector/player/up1.png")
Img_Player_up2 = pygame.image.load("charector/player/up2.png")
Img_Player_down_idle = pygame.image.load("charector/player/down_idle.png")
Img_Player_down1 = pygame.image.load("charector/player/down1.png")
Img_Player_down2 = pygame.image.load("charector/player/down2.png")
Img_Player_left_idle = pygame.image.load("charector/player/left_idle.png")
Img_Player_left1 = pygame.image.load("charector/player/left1.png")
Img_Player_left2 = pygame.image.load("charector/player/left2.png")
Img_Player_right_idle = pygame.image.load("charector/player/right_idle.png")
Img_Player_right1 = pygame.image.load("charector/player/right1.png")
Img_Player_right2 = pygame.image.load("charector/player/right2.png")
Img_Eneme_up1 = pygame.image.load("charector/enemy/up1.png")
Img_Eneme_down1 = pygame.image.load("charector/enemy/down1.png")
Img_Eneme_down2 = pygame.image.load("charector/enemy/down2.png")
Img_Eneme_left1 = pygame.image.load("charector/enemy/left1.png")
Img_Eneme_left2 = pygame.image.load("charector/enemy/left2.png")
Img_Eneme_right1 = pygame.image.load("charector/enemy/right1.png")
Img_Eneme_right2 = pygame.image.load("charector/enemy/right2.png")

##
## Setup zone
name = input('Enter name: ')
display_width = 1600
display_height = 900
current_scence = "jungle_1"
scence_item_size = 32
clock = pygame.time.Clock()
pygame.font.init()
##
## Processing zone

screen = pygame.display.set_mode((display_width, display_height), pygame.FULLSCREEN)
pygame.display.set_caption("Pygame_RPG!")
pygame.display.set_icon(Img_Player_down_idle)

def draw_title():
    screen.fill(Color("Grey"))
    screen.blit(Img_Flower_1,(800,800))
    pygame.display.flip()

##draw_title()
    
def is_collisions(x1, y1, w1, h1, x2, y2, w2, h2):
    """ Check for collision"""
    if (x2+w2>=x1>=x2 and y2+h2>=y1>=y2) or (x2+w2>=x1+w1>=x2 and y2+h2>=y1>=y2) or (x2+w2>=x1>=x2 and y2+h2>=y1+h1>=y2) or (x2+w2>=x1+w1>=x2 and y2+h2>=y1+h1>=y2) :
        return True
    return False

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

def enemy(player_pos, bullet, enemy_box, wave, this_wave):
    """ Control enemy """
    Img_Eneme = Img_Eneme_down1
    enemy_mult = wave 
    enemy_speed = 4
    add_x = 0
    add_y = 0
    if this_wave != wave:
        for i in range(1,enemy_mult+1):
            enemy_box.append([random.randint(50, display_width-50), random.randint(0, 10), "down"])
            enemy_box.append([random.randint(50, display_width-50), random.randint(890, 900), "up"])
            enemy_box.append([random.randint(0, 10), random.randint(50, display_height-50), "right"])
            enemy_box.append([random.randint(display_width, display_width), random.randint(50, display_height-50), "left"])
        this_wave = wave
    for i in range(len(enemy_box)):
        if abs( enemy_box[i][0] - player_pos[0]) - abs( enemy_box[i][1] - player_pos[1]) > 1:
            if enemy_box[i][0] - player_pos[0]  > 2:
                add_x = -enemy_speed
                enemy_box[i][2] = "left"
            else:
                add_x = enemy_speed
                enemy_box[i][2] = "right"
        else:
            if enemy_box[i][1] - player_pos[1] > 10:
                 add_y = -enemy_speed
                 enemy_box[i][2] = "up"
            else:
                add_y = enemy_speed
                enemy_box[i][2] = "down"
        if enemy_box[i] != enemy_box[len(enemy_box)-1]:
            if is_collisions(enemy_box[i][0], enemy_box[i][1], 16, 16, enemy_box[i+1][0], enemy_box[i+1][1], 16, 16):
                add_x = -add_x
                add_y = -add_y
        else:
            if is_collisions(enemy_box[i][0], enemy_box[i][1], 16, 16, enemy_box[0][0], enemy_box[0][1], 16, 16):
                add_x = -add_x
                add_y = -add_y
        enemy_box[i][0] += add_x
        enemy_box[i][1] += add_y 

    for i in enemy_box:
        if i[2] == "up":
            Img_Eneme = Img_Eneme_up1
        screen.blit(Img_Eneme,  i[:2])
        if i[2] == "down":
            Img_Eneme = Img_Eneme_down1
        screen.blit(Img_Eneme,  i[:2])
        if i[2] == "left":
            Img_Eneme = Img_Eneme_left1
        screen.blit(Img_Eneme,  i[:2])
        if i[2] == "right":
            Img_Eneme = Img_Eneme_right1
        screen.blit(Img_Eneme,  i[:2])
    return enemy_box, this_wave

def hud(score, wave, life):
    """ Control other content that not in game sprite """
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    bar_1 = 'Score: %d' %score +"   "+ 'Wave: %d' %wave +"   "+ 'Life: %d' %life
    hud_1 = myfont.render(bar_1, False, (0, 0, 0))
    screen.blit(hud_1,(10,10))

def event_control(score,wave, life, name):
    """ Almost cvery action happend here """
    player_pos = [int(display_width * 0.5), int(display_height * 0.5)]
    bullet_pos = [0, 0]
    bullet = list() #bullet dict [[x,y,direction],[x,y,direction],[x,y,direction],....]
    enemy_box = list() # Box for keep all enemy position
    Img_Player = Img_Player_right_idle
    Idle_Player = Img_Player_down_idle
    player_speed = 5
    bul_speed = 10
    x_acc = 0
    y_acc = 0
    direction = 'right'
    bul_dicrec = 'up'
    bang = True
    this_wave = 0
    t3 = time.time()

    while True:
        draw_scence(current_scence)
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    end_time = time.time() - t3
                    let_exit(score, wave, end_time, name)
                    pygame.quit()
                    quit()
                if event.key == K_UP:
                    y_acc = -player_speed
                    Img_Player = Img_Player_up2
                    Idle_Player = Img_Player_up_idle
                    direction = 'up'
                if event.key == K_DOWN:
                    y_acc = player_speed
                    Img_Player = Img_Player_down2
                    Idle_Player = Img_Player_down_idle
                    direction = 'down'
                if event.key == K_LEFT:
                    x_acc = -player_speed
                    Img_Player = Img_Player_left2
                    Idle_Player = Img_Player_left_idle
                    direction = 'left'
                if event.key == K_RIGHT:
                    x_acc = player_speed
                    Img_Player = Img_Player_right2
                    Idle_Player = Img_Player_right_idle
                    direction = 'right'
                if event.key == K_SPACE: #create bullet 
                    bullet_pos = deepcopy(player_pos) # copy player_pos to new editable list
                    bullet.append([bullet_pos[0], bullet_pos[1],direction])
                    #bang = True
            if event.type == KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_acc = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_acc = 0
                Img_Player = Idle_Player
                
    ## remove bullet when it offscreen
        for i in range(len(bullet)-1 , -1, -1):
                if bullet[i][0] < 0 or bullet[i][0] > display_width or bullet[i][1] < 0 or bullet[i][1] > display_height:
                    del bullet[i]
    ## remove enemy when it offscreen
        for i in range(len(enemy_box)-1 , -1, -1):
                if is_collisions(enemy_box[i][0], enemy_box[i][1], 32, 32, player_pos[0], player_pos[1], 32, 32):
                    return score, wave
                if enemy_box[i][0] < 0 or enemy_box[i][0] > display_width or enemy_box[i][1] < 0 or enemy_box[i][1] > display_height:
                    del enemy_box[i]
    ## bullet handle
        for i in bullet:
            if i[2] == 'up':
                i[1] -= bul_speed
                pygame.draw.circle(screen, (255, 50, 50), i[:2], 5,)
            elif i[2] == 'down':
                i[1] += bul_speed
                pygame.draw.circle(screen, (255, 50, 50), i[:2], 5,)
            elif i[2] == 'left':
                i[0] -= bul_speed
                pygame.draw.circle(screen, (255, 50, 50), i[:2], 5,)
            elif i[2] == 'right' :
                i[0] += bul_speed
                pygame.draw.circle(screen, (255, 50, 50), i[:2], 5,)
    ##
        player_pos[0] += x_acc
        player_pos[1] += y_acc
        enemy_box, this_wave = enemy(player_pos, bullet, enemy_box, wave, this_wave)
        screen.blit(Img_Player,  player_pos) # cook player
    ## Collide of bullet and enemy handle
        for i in range(len(bullet)-1 , -1, -1):
            for a in range(len(enemy_box)-1 , -1, -1):
                if is_collisions(bullet[i][0], bullet[i][1], 10, 10, enemy_box[a][0], enemy_box[a][1], 32, 32):
                    del enemy_box[a]
                    del bullet[i]
                    score += 1
                    break
    ## Wave control
        if len(enemy_box) == 0:
            wave += 1
    ##
        hud(score, wave, life)
        pygame.display.update() # display cooked item
        clock.tick(30) # frame rate limit

##

def let_exit(score, wave, end_time, name):
    """ Acthion before exit game """
    pygame.quit()
    print("Uploading score....")
    messenger.put('/Score', name, score)
    messenger.put('/Wave', name, wave)
    messenger.put('/Time', name, int(end_time))
    print("Completed!")
    print("Score: ",score)
    print("Wave: ",wave)
    print("Time: ", int(end_time), 'seconds')
    print("!!Thank for playing!!")
    quit()

def game_loop(name):
    life = 3
    score = 0
    wave = 1
    draw_scence(current_scence)
    t0 = time.time()
    while life > 0:
        t0 = time.time()
        while time.time() - t0 < 1:
            pass
        score, wave = event_control(score, wave, life, name)
        life -= 1
    end_time = time.time() - t0
    let_exit(score, wave, end_time, name)
    pygame.quit()
    quit()

game_loop(name)

