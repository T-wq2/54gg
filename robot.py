# function

# move
# movement to the right
def movement_to_the_right(x_Bg, x_Kirp_2, fright_wall, forward):
    if fright_wall == True:
        all_Move_r = {
            "x_Bg": x_Bg,
            "x_Kirp_2": x_Kirp_2
        }

        return all_Move_r
    x_Bg -= forward
    x_Kirp_2 -= forward
    all_Move_r = {
        "x_Bg": x_Bg,
        "x_Kirp_2": x_Kirp_2
    }
    return all_Move_r


# movement to the left
def movement_to_the_left(x_Bg, x_Kirp_2, fleft_wall, forward):
    if fleft_wall == True:
        all_Move_l = {
            "x_Bg": x_Bg,
            "x_Kirp_2": x_Kirp_2
        }

        return all_Move_l
    x_Bg += forward
    x_Kirp_2 += forward
    all_Move_l = {
        "x_Bg": x_Bg,
        "x_Kirp_2": x_Kirp_2
    }
    return all_Move_l


# jump to up
def jump_to_up(forse_of_jump, x_fors_of_jump, y_Player, fjump_up, fjump_down, fjump):
    forse_of_jump //= x_fors_of_jump
    y_Player -= forse_of_jump
    if forse_of_jump <= 1:
        fjump_up = False
        fjump_down = True
        all_Jump_U = {
            'fjump_up': fjump_up,
            'fjump_down': fjump_down,
            'y_Player': y_Player,
            'forse_of_jump': forse_of_jump
          }
        return all_Jump_U
    all_Jump_U = {
        'fjump_up': fjump_up,
        'fjump_down': fjump_down,
        'y_Player': y_Player,
        'forse_of_jump': forse_of_jump
    }
    return all_Jump_U


# jump to down
def jump_to_down(forse_of_jump, y_Player, x_fors_of_jump, fstay, forse_of_jump_2, fjump_down, fjump):
    forse_of_jump *= x_fors_of_jump
    y_Player += forse_of_jump
    print(y_Player)
    if fstay == True:
        all_Jump_D = {
        'fjump_up': True,
        'fjump': False,
        'fjump_down': False,
        'y_Player': y_Player - forse_of_jump,
        'forse_of_jump': forse_of_jump_2
        }
        print("2", y_Player - forse_of_jump)
        return all_Jump_D
    all_Jump_D = {
    'fjump_up': False,
    'fjump': True,
    'fjump_down': True,
    'y_Player': y_Player,
    'forse_of_jump': forse_of_jump
     }
    print("3", y_Player)
    return all_Jump_D


# bild the blocks
# left wall
def left_wall(x_Kirp, kirp_size, x_Player, y_Kirp, y_Player, player_size_y, player_size_x):
    if x_Kirp + kirp_size >= x_Player >= x_Kirp - player_size_x + 1 and y_Kirp - player_size_y < y_Player < y_Kirp + kirp_size:
        fleft_wall = True
    else:
        fleft_wall = False

    return fleft_wall


# right wall
def right_wall(x_Kirp, y_Kirp, y_Player, x_Player, kirp_size, player_size_y, player_size_x):
    if x_Kirp - player_size_x - 1 <= x_Player <= x_Kirp + kirp_size - 1 and y_Kirp - player_size_y < y_Player < y_Kirp + kirp_size:
        fright_wall = True
    else:
        fright_wall = False
    return fright_wall


# floor
def floor(y_Kirp, y_Player, player_size_y, x_Kirp, fjump_up, x_Player, kirp_size, fjump_down, player_size_x):

    if y_Kirp <= y_Player + player_size_y <= y_Kirp + 60 and x_Kirp + kirp_size >= x_Player >= x_Kirp - kirp_size and fjump_up == False:
        print(1111111111111111)
        all_Floor = {
            'y_Player': y_Kirp - player_size_y,
            'fstay': True,
            'fjump_down': False
        }
        return all_Floor

    elif y_Kirp <= y_Player + player_size_y <= y_Kirp + 60 and fjump_down == False:
        if x_Player + player_size_x < x_Kirp or y_Kirp + kirp_size < x_Player:
            all_Floor = {
                'y_Player': y_Player,
                'fstay': False,
                'fjump_down': True
            }
            return all_Floor
        all_Floor = {
                'y_Player': y_Player,
                'fstay': False,
                'fjump_down': True
            }
        return all_Floor

    all_Floor = {
        'y_Player': y_Player,
        'fstay': False,
        'fjump_down': True
    }
    return all_Floor

# def roof(y_Kirp, y_Player, player_size_y, x_Kirp, fjump_up, x_Player, fstay, kirp_size):
#             #x cordinata                                            #y cordinata
#     if x_Kirp + kirp_size >= x_Player >= x_Kirp - kirp_size and
