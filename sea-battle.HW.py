# Sea battle game
# * conditional flow
# * looping flow
# * lists
# * some new features
from os import system
from random import randint
# LEGEND
# Initial situation - □
WATER = 0           # □  
SHIP  = 1           # ■
MISS  = 2           # ◦
HIT   = 3           # ✕

colA = [
    0,   # 0
    0,   # 1
    0,   # 2
    0,   # 3
    0,   # 4
    0,   # 5
    0,   # 6
    0,   # 7
    0,   # 8
    0    # 9
]
for n in range(3):           ### 3 ships are randomnly created
    colA[randint(0,9)] = SHIP    

score              = 0       ### Variable that accumulates points obtained by the player
limit_shots        = 0       ### Variable that is introduced to count shots made by the player 

## Game loop
while limit_shots <= 5:      ### Player can make shots until shots counter reaches 5
    system("cls")
## draw the map
    for y in range(1,11):

        if colA[y-1] == WATER or colA[y-1] == SHIP:
            sign = "□"
        elif colA[y-1] == MISS:
            sign = "◦"
        elif colA[y-1] == HIT:
            sign = "✕"

        print(sign, y)
    print("Your score is ", score)

    
    shootY = int(input("shoot: "))
    limit_shots += 1         ### Registration of the shot made by the player


    if colA[shootY-1] == WATER:
        colA[shootY - 1] = MISS
    if colA[shootY-1] == SHIP:
        colA[shootY-1] = HIT
        score        += 1    ### Player's score in the game increases by 1 point if he/she shot at the ship     