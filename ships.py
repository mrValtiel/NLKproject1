#ships game for project NLKproject1
import os
import random

#function to clear screen
def cls():
    os.system('cls')

cls()
print("TOTALLY RANDOM SHIPS GAME")
print("*************************************************************")
playerMap = []
for i in range(0, 10):
    playerMap.append(['-' for j in range(0, 10)])

enemyMap = []
for i in range(0, 10):
    enemyMap.append(['-' for j in range(0, 10)])

enemyMapForPlayer = []
for i in range(0, 10):
    enemyMapForPlayer.append(['-' for j in range(0, 10)])

#PLAYER 1 SHIP
playerMap[1][1] = 'S'
#PLAYER 2 SHIP
playerMap[8][7] = 'S'
playerMap[8][8] = 'S'
#PLAYER 3 SHIP
playerMap[3][4] = 'S'
playerMap[4][4] = 'S'
playerMap[5][4] = 'S'
#PLAYER 4 SHIP
playerMap[5][6] = 'S'
playerMap[5][7] = 'S'
playerMap[5][8] = 'S'
playerMap[5][9] = 'S'
#PLAYER 5 SHIP
playerMap[4][2] = 'S'
playerMap[5][2] = 'S'
playerMap[6][2] = 'S'
playerMap[7][2] = 'S'
playerMap[8][2] = 'S'

#ENEMY 1 SHIP
enemyMap[2][2] = 'S'
#ENEMY 2 SHIP
enemyMap[5][5] = 'S'
enemyMap[5][6] = 'S'
#ENEMY 3 SHIP
enemyMap[7][2] = 'S'
enemyMap[8][2] = 'S'
enemyMap[9][2] = 'S'
#ENEMY 4 SHIP
enemyMap[3][4] = 'S'
enemyMap[3][5] = 'S'
enemyMap[3][6] = 'S'
enemyMap[3][7] = 'S'
#ENEMY 5 SHIP
enemyMap[8][4] = 'S'
enemyMap[8][5] = 'S'
enemyMap[8][6] = 'S'
enemyMap[8][7] = 'S'
enemyMap[8][8] = 'S'

gameRunning = True
xIndex = 0
yIndex = 0
xIndexEnemy = 0
yIndexEnemy = 0

playerShips = 15
enemyShips = 15

while gameRunning:
    cls()
    print("TOTALLY RANDOM SHIPS GAME")
    print("*************************************************************")
    print("Player\'s map:")
    for i in range(0, 10):
        print(playerMap[i])
    print("remaining hit points: ", str(playerShips))
    print("Enemy\'s map:")
    for i in range(0, 10):
        print(enemyMapForPlayer[i])
    print("remaining hit points: ", str(enemyShips))
    print("Enter X axis index:")
    xIndex = input()
    xIndex = int(xIndex)
    print("Enter Y axis index:")
    yIndex = input()
    yIndex = int(yIndex)
    if (xIndex >= 0 and xIndex <= 9 and yIndex >= 0 and yIndex <= 9):
        if (enemyMap[xIndex][yIndex] == 'S'):
            enemyMapForPlayer[xIndex][yIndex] = 'X'
            enemyShips -= 1
        else:
            enemyMapForPlayer[xIndex][yIndex] = 'O'

    #Enemy move
    xIndexEnemy = random.randint(0, 9)
    yIndexEnemy = random.randint(0, 9)
    if (playerMap[xIndexEnemy][yIndexEnemy] == 'S'):
        playerMap[xIndexEnemy][yIndexEnemy] = 'X'
        playerShips -= 1

    if ((playerShips == 0) or (enemyShips == 0)):
        gameRunning = False

cls()
print("TOTALLY RANDOM SHIPS GAME")
print("*************************************************************")
print("Player\'s map:")
for i in range(0, 10):
    print(playerMap[i])
print("\n")
print("Enemy\'s map:")
for i in range(0, 10):
    print(enemyMapForPlayer[i])
print("\n")
if (playerShips == 0):
    print("WINNER: computer")
elif (enemyShips == 0):
    print("WINNER: player")

print("Enter anything to exit")
anything = input()
