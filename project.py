import pygame as pg
import robot

list_map = [
    "!!!!!!!!!!!!!!!!!!!!!!!!",  # "=" - universal block
    "+                     -",  # "-" - right wall
    "+                     -",  # "+" - left wall
    "+                  ",  # "0" - floor
    "+                   - -",  # "!" - empty block
    "+                   -  -",
    "+            ",
    "+    0       ",
    "0000000000000"]

pg.init()

# screen size
W = 1000
H = 600

# midle of screen
x = W // 2
y = H // 2

# grond
under_graund = 180
gr = H - under_graund
gr2 = gr

# size
kirp_size = 70
player_size_x = 50
player_size_y = 100
bg_size_x = 2000
bg_size_y = 1000
bg_x = -((bg_size_x // 2) - x)
size_of_landing = 5  # landing - призимление

# x, y for objects
x_Player = x  # const, midl of center
y_Player = gr

x_Bg = bg_x
y_Bg = y - bg_size_y // 2.4

x_Kirp = 0
y_Kirp = 0

x_Kirp_2 = x_Kirp

# img for player, bg and also
player_image = "D:\MartiN\картинки\мikipe-tan_pixel_art_x4.png"
bg_image = "D:\MartiN\картинки\с48a0abc8945f94fa4cb205342b074e.png"
kirpich_image = "D:\MartiN\картинки\kirpich.jpg"

# creat name of screen and also screen
#sc = pg.display.set_mode((0, 0), pg.FULLSCREEN)
sc = pg.display.set_mode((W, H))
pg.display.set_caption("тест")

# objects
bg = pg.image.load(bg_image).convert()
playe = pg.image.load(player_image).convert_alpha()
playe = pg.transform.scale(playe, (player_size_x, player_size_y))
playe = pg.transform.flip(playe, 1, 0)
player = playe
forward = 4
bg = pg.transform.scale(bg, (bg_size_x, bg_size_y))
kirpich = pg.image.load(kirpich_image).convert()
kirpich = pg.transform.scale(kirpich, (kirp_size, kirp_size))

# characters of objects
forse_of_jump = 30
forse_of_jump_2 = forse_of_jump
x_fors_of_jump = 1.1

# colore
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# FPS
FPS = 1
clock = pg.time.Clock()

fright = fleft = False
fjump_up = True
fjump_down = False
fjump = False
fleft_wall = False
fright_wall = False
fstay = False
jump_to_down2 = False

#exit
x = forse_of_jump
while True:
    print(jump_to_down2)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            print('exit')
            pg.quit()
        elif event.type == pg.KEYDOWN:  # keyboard
            if event.key == pg.K_SPACE:  # jump
                fjump = True
                fstay = False
            if event.key == pg.K_d or event.key == pg.K_a:  # move
                if pg.key.get_pressed()[pg.K_d]:  # right
                    player = playe
                    fright = True

                if event.key == pg.K_a:  # left
                    if player == playe:
                        player = pg.transform.flip(player, 1, 0)
                    fleft = True
        if event.type == pg.KEYUP:
            if event.key == pg.K_a:
                fleft = False
            if event.key == pg.K_d:
                fright = False

    if fright == True:
        movement_to_the_right2 = robot.movement_to_the_right(x_Bg, x_Kirp_2, fright_wall, forward)
        x_Bg = movement_to_the_right2["x_Bg"]
        x_Kirp_2 = movement_to_the_right2["x_Kirp_2"]

    if fleft == True:
        movement_to_the_left2 = robot.movement_to_the_left(x_Bg, x_Kirp_2, fleft_wall, forward)
        x_Bg = movement_to_the_left2["x_Bg"]
        x_Kirp_2 = movement_to_the_left2["x_Kirp_2"]

    if fjump == True and fjump_up == True:
        jump_to_up2 = robot.jump_to_up(forse_of_jump, x_fors_of_jump, y_Player, fjump_up, fjump_down, fjump)
        fjump_up = jump_to_up2['fjump_up']
        fjump_down = jump_to_up2['fjump_down']
        y_Player = jump_to_up2['y_Player']
        forse_of_jump = jump_to_up2['forse_of_jump']

    if (fjump == True and fjump_up == False) or (jump_to_down2 == True and fjump == False):
        jump_to_down2 = robot.jump_to_down(forse_of_jump, y_Player, x_fors_of_jump, fstay, forse_of_jump_2, fjump_down, fjump)
        fjump_up = jump_to_down2['fjump_up']
        fjump_down = jump_to_down2['fjump_down']
        y_Player = jump_to_down2['y_Player']
        forse_of_jump = jump_to_down2['forse_of_jump']
        fjump = jump_to_down2['fjump']
    sc.blit(bg, (x_Bg, y_Bg))

    # bild the blocks
    fstay = False
    fright_wall, fleft_wall = False, False
    jump_to_down2 = True
    for row in list_map:
        for col in row:
            # universal block
            if col == "=":
                sc.blit(kirpich, (x_Kirp, y_Kirp))
                if robot.right_wall(x_Kirp, y_Kirp, y_Player, x_Player, kirp_size, player_size_y, player_size_x) == True:
                    fright_wall = True
                else:
                    pass

                if robot.left_wall(x_Kirp, kirp_size, x_Player, y_Kirp, y_Player, player_size_y, player_size_x) == True:
                    fleft_wall = True
                else:
                    pass

                floor2 = robot.floor(y_Kirp, y_Player, player_size_y, x_Kirp, fjump_up, x_Player, kirp_size, fjump_down, player_size_x)
                y_Player = floor2['y_Player']
                if floor2['fstay'] == True:
                    fstay = True
                else:
                    pass
                if floor2['fjump_down'] == True:
                    fjump_down = True
                    fjump = True

                else:
                    print(4)
            # floor
            if col == "0":
                sc.blit(kirpich, (x_Kirp, y_Kirp))
                floor2 = robot.floor(y_Kirp, y_Player, player_size_y, x_Kirp, fjump_up, x_Player, kirp_size, fjump_down, player_size_x)
                y_Player = floor2['y_Player']
                if floor2['fstay'] == True:
                    fstay = True
                else:
                    pass
                if floor2['fjump_down'] == True:
                    pass
                else:
                    jump_to_down2 = False
            # right wall
            if col == "-":
                sc.blit(kirpich, (x_Kirp, y_Kirp))
                if robot.right_wall(x_Kirp, y_Kirp, y_Player, x_Player, kirp_size, player_size_y, player_size_x) == True:
                    fright_wall = True
                else:
                    pass
            # left wall
            if col == "+":
                sc.blit(kirpich, (x_Kirp, y_Kirp))
                if robot.left_wall(x_Kirp, kirp_size, x_Player, y_Kirp, y_Player, player_size_y, player_size_x) == True:
                    fleft_wall = True
                else:
                    pass
            # empty block
            if col == "!":
                sc.blit(kirpich, (x_Kirp, y_Kirp))

            #roof
            # if col == 1:
            #     sc.blit(kirpich, (x_Kirp, y_Kirp))
            #     if robot.
            x_Kirp += kirp_size
        y_Kirp += kirp_size
        x_Kirp = x_Kirp_2
    x_Kirp = x_Kirp_2
    y_Kirp = 0

    sc.blit(player, (x_Player, y_Player))
    pg.display.update()
    clock.tick(FPS)
    if forse_of_jump > x:
        print(forse_of_jump)
        x = forse_of_jump

#изза того что программа пытаеться прыгнуть и сразу пойти в низ это дает сбой