# -*- coding: utf-8 -*-
""" Main process of game. """

import pygame,random,math,time,sys,os
from firebase import firebase
from copy import deepcopy ## for copy list and keep original val
## Firebase handle
url = 'https://pygame-rpg01-223910.firebaseio.com/'
messenger = firebase.FirebaseApplication(url)
pygame.mixer.init()

## Import sprite zone
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
Img_Big_bg = pygame.image.load("world/big_bg2.png")
img_end = pygame.image.load("object/gameover.jpg")
##
## Sound import
sound_bg = pygame.mixer.Sound("sound/bg.ogg")
sound_shoot = pygame.mixer.Sound("sound/shoot.ogg")
sound_collect = pygame.mixer.Sound("sound/collect.ogg")
sound_hit = pygame.mixer.Sound("sound/hit.ogg")
sound_pass = pygame.mixer.Sound("sound/wave_pass.ogg")
sound_end = pygame.mixer.Sound("sound/end.ogg")
##
## Setup zone
display_width = 1600
display_height = 900
current_scence = "jungle_1"
scence_item_size = 32
clock = pygame.time.Clock()
pygame.font.init()

sound_bg.set_volume(0.2)
sound_shoot.set_volume(0.4)
sound_collect.set_volume(0.4)
sound_hit.set_volume(0.4)
sound_pass.set_volume(0.4)
sound_end.set_volume(0.4)
##
## Processing zone

screen = pygame.display.set_mode((display_width, display_height), pygame.FULLSCREEN)
pygame.display.set_caption("Pygame_RPG!")
pygame.display.set_icon(Img_Player_down_idle)

def title_handle():
    """ Handle begining of game """
    pressed = False
    name = ""
    max_name = 10
    while True:
        draw_scence(current_scence)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and not pressed:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    os._exit(0)
                    sys.exit()
                if len(name) > 0:
                    if event.key == pygame.K_BACKSPACE:
                        name = name[:-1]
                    if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                        return name
                if len(name) <= max_name:
                    if event.key == pygame.K_a: name += "A"
                    elif event.key == pygame.K_b: name += "B"
                    elif event.key == pygame.K_c: name += "C"
                    elif event.key == pygame.K_d: name += "D"
                    elif event.key == pygame.K_e: name += "E"
                    elif event.key == pygame.K_f: name += "F"
                    elif event.key == pygame.K_g: name += "G"
                    elif event.key == pygame.K_h: name += "H"
                    elif event.key == pygame.K_i: name += "I"
                    elif event.key == pygame.K_j: name += "J"
                    elif event.key == pygame.K_k: name += "K"
                    elif event.key == pygame.K_l: name += "L"
                    elif event.key == pygame.K_m: name += "M"
                    elif event.key == pygame.K_n: name += "N"
                    elif event.key == pygame.K_o: name += "O"
                    elif event.key == pygame.K_p: name += "P"
                    elif event.key == pygame.K_q: name += "Q"
                    elif event.key == pygame.K_r: name += "R"
                    elif event.key == pygame.K_s: name += "S"
                    elif event.key == pygame.K_t: name += "T"
                    elif event.key == pygame.K_u: name += "U"
                    elif event.key == pygame.K_v: name += "V"
                    elif event.key == pygame.K_w: name += "W"
                    elif event.key == pygame.K_x: name += "X"
                    elif event.key == pygame.K_y: name += "Y"
                    elif event.key == pygame.K_z: name += "Z"
                    elif event.key == pygame.K_KP0 or event.key == pygame.K_0: name += "0"
                    elif event.key == pygame.K_KP1 or event.key == pygame.K_1: name += "1"
                    elif event.key == pygame.K_KP2 or event.key == pygame.K_2: name += "2"
                    elif event.key == pygame.K_KP3 or event.key == pygame.K_3: name += "3"
                    elif event.key == pygame.K_KP4 or event.key == pygame.K_4: name += "4"
                    elif event.key == pygame.K_KP5 or event.key == pygame.K_5: name += "5"
                    elif event.key == pygame.K_KP6 or event.key == pygame.K_6: name += "6"
                    elif event.key == pygame.K_KP7 or event.key == pygame.K_7: name += "7"
                    elif event.key == pygame.K_KP8 or event.key == pygame.K_8: name += "8"
                    elif event.key == pygame.K_KP9 or event.key == pygame.K_9: name += "9"
                pressed = True
            if event.type == pygame.KEYUP:
                pressed = False
        myfont = pygame.font.SysFont('Comic Sans MS', 40)
        yourfont = pygame.font.SysFont('Comic Sans MS', 80)
        bar_0 = "!Pygame RPG!"
        bar_1 = "Enter your name"
        gname = name
        if len(name) == 0:
            gname = "_"
        bar_2 = "^"+ gname + "^"
        name_0 = yourfont.render(bar_0, False, (255, 255, 255))
        name_1 = myfont.render(bar_1, False, (0, 0, 0))
        name_2 = myfont.render(bar_2, False, (0, 0, 0))
        screen.blit(name_0,(display_width//3, display_height//3))
        screen.blit(name_1,(display_width//2, display_height//2))
        screen.blit( name_2,(display_width//2+200, display_height//2+100))
        pygame.display.update() # display cooked item
        clock.tick(30) # frame rate limit
    return name
        
    
def is_collisions(x1, y1, w1, h1, x2, y2, w2, h2):
    """ Check for collision"""
    if (x2+w2>=x1>=x2 and y2+h2>=y1>=y2) or (x2+w2>=x1+w1>=x2 and y2+h2>=y1>=y2) or (x2+w2>=x1>=x2 and y2+h2>=y1+h1>=y2) or (x2+w2>=x1+w1>=x2 and y2+h2>=y1+h1>=y2) :
        return True
    return False

def draw_scence(scence):
    screen.blit(Img_Big_bg, (0,0))


def enemy(player_pos, bullet, enemy_box, wave, this_wave):
    """ Control enemy """
    Img_Eneme = Img_Eneme_down1
    enemy_mult = wave * 2
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

def hud(score, wave, life, bullet):
    """ Control other content that not in game sprite """
    bul = "<= " * (8 - bullet)
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    bar_1 = 'Score: %d' %score +"   "+ 'Wave: %d' %wave +\
                 "   "+ 'Life: %d' %life + "   " + 'Bullet: ' + bul
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
    bul_max = 8
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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    end_time = time.time() - t3
                    let_exit(score, wave, end_time, name)
                    pygame.quit()
                    os._exit(0)
                if event.key == pygame.K_UP:
                    y_acc = -player_speed
                    Img_Player = Img_Player_up2
                    Idle_Player = Img_Player_up_idle
                    direction = 'up'
                if event.key == pygame.K_DOWN:
                    y_acc = player_speed
                    Img_Player = Img_Player_down2
                    Idle_Player = Img_Player_down_idle
                    direction = 'down'
                if event.key == pygame.K_LEFT:
                    x_acc = -player_speed
                    Img_Player = Img_Player_left2
                    Idle_Player = Img_Player_left_idle
                    direction = 'left'
                if event.key == pygame.K_RIGHT:
                    x_acc = player_speed
                    Img_Player = Img_Player_right2
                    Idle_Player = Img_Player_right_idle
                    direction = 'right'
                if event.key == pygame.K_SPACE and len(bullet) < bul_max: #create bullet
                    sound_shoot.play()
                    bullet_pos = deepcopy(player_pos) # copy player_pos to new editable list
                    bullet.append([bullet_pos[0], bullet_pos[1],direction])
                    #bang = True
            if event.type == pygame.KEYUP:
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
    ## Player offscreen fix
        if player_pos[0] < 5: player_pos[0] += 7
        if player_pos[0] > display_width-30: player_pos[0] -= 7
        if player_pos[1] < 5: player_pos[1] += 7
        if player_pos[1] > display_height-30: player_pos[1] -= 7
        player_pos[0] += x_acc
        player_pos[1] += y_acc
        enemy_box, this_wave = enemy(player_pos, bullet, enemy_box, wave, this_wave)
        screen.blit(Img_Player,  player_pos) # cook player
    ## Collide of bullet and enemy handle
        for i in range(len(bullet)-1 , -1, -1):
            for a in range(len(enemy_box)-1 , -1, -1):
                if is_collisions(bullet[i][0], bullet[i][1], 10, 10, enemy_box[a][0], enemy_box[a][1], 32, 32):
                    sound_collect.play()
                    del enemy_box[a]
                    del bullet[i]
                    score += 1
                    break
    ## Wave control
        if len(enemy_box) == 0:
            sound_pass.play()
            wave += 1
    ##
        hud(score, wave, life, len(bullet))
        pygame.display.update() # display cooked item
        clock.tick(30) # frame rate limit

##

def let_exit(score, wave, end_time, name):
    """ Acthion before exit game """
    screen.fill((0,0,0))
    sound_bg.stop()
    myfont = pygame.font.SysFont('Comic Sans MS', 40)
    mss = "Press ENTER to exit"
    mss_score = "Score: " + str(score)
    mss_wave = "Wave survived: " + str(wave)
    mss_time = "Time played:  " + str(int(end_time)) + "  s"
    hud_1 = myfont.render(mss, False, (255, 255, 255))
    hud_score = myfont.render(mss_score ,False, (255, 0, 0))
    hud_wave = myfont.render(mss_wave, False, (0,0, 255))
    hud_time = myfont.render(mss_time, False, (0, 255, 0))
    screen.blit(img_end, (200,100))
    ##screen.blit(hud_1,(display_width//2-120,display_height-300))
    screen.blit(hud_score,(display_width//3-400,display_height-400))
    screen.blit(hud_wave,(display_width//3+50,display_height-400))
    screen.blit(hud_time,(display_width//2+300,display_height-400))
    pygame.display.update()
    sound_end.play(loops=-1)
    print("Uploading score....")
    messenger.put('/Score', name, score)
    messenger.put('/Wave', name, wave)
    messenger.put('/Time', name, int(end_time))
    print("Completed!")
    print("!!Thank for playing!!")
    screen.blit(hud_1,(display_width//3,display_height-300))
    pygame.display.update()
    t5 = time.time()
    while time.time() - t5 < 14:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    break
        else:
            continue
        break
    pygame.quit()
    exit()
    os._exit(0)
    

def game_loop():
    name = title_handle()
    life = 3
    score = 0
    wave = 1
    sound_bg.play(loops=-1)
    draw_scence(current_scence)
    t0 = time.time()
    while life > 0: ##Keep game contionue when still have heart 
        t0 = time.time()
        while time.time() - t0 < 1:
            pass
        score, wave = event_control(score, wave, life, name)
        sound_hit.play()
        life -= 1
    end_time = time.time() - t0
    let_exit(score, wave, end_time, name)
    pygame.quit()
    os._exit(0)

game_loop()
