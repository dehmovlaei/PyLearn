import pyfiglet
import datetime
import random
from colorama import Fore

title = pyfiglet.figlet_format("Tic Tac Toe", font="slant")
print(title)

endGame = False
turn = 0
gameBoard = [["-","-","-"],
             ["-","-","-"],
             ["-","-","-"]]

def userInput():
    row = int(input("row: "))
    col = int(input("col: "))
    return row, col

def printBoard():
    for row in gameBoard:
        for cell in row:
            if cell == "-":
                print(Fore.WHITE + "", end="")
                print(cell, end=" ")
            elif cell == "X":
                print(Fore.RED + "X", end=" ")
                print(Fore.WHITE + "", end="")
            else:
                print(Fore.BLUE + "O", end=" ")
                print(Fore.WHITE + "", end="")
        print()

def player1():
    global turn
    print("Player 1")
    row, col = userInput()
    if  0 <= row <= 2 and 0 <= col <= 2 and gameBoard[row][col] == "-":
        gameBoard[row][col] = "X"
        turn += 1
        printBoard()
    else:
        if 0 <= row <= 2 and 0 <= col <= 2:
            print("Please select an empty cell!!!")
            player1()
        else:
            print("enter a valid cell index in range 0-2")
            player1()

def player2():
    global turn
    print("Player 2")
    row, col = userInput()
    if 0 <= row <= 2 and 0 <= col <= 2 and gameBoard[row][col] == "-":
        gameBoard[row][col] = "O"
        turn += 1
        printBoard()
    else:
        if 0 <= row <= 2 and 0 <= col <= 2:
            print("Please select an empty cell!!!")
            player2()
        else:
            print("enter a valid cell index in range 0-2")
            player2()

def cpu():
    global turn
    row, col = random.randint(0, 2), random.randint(0, 2)
    if 0 <= row <= 2 and 0 <= col <= 2 and gameBoard[row][col] == "-":
        print("CPU")
        gameBoard[row][col] = "O"
        turn += 1
        printBoard()
    else:
        if 0 <= row <= 2 and 0 <= col <= 2:
            cpu()
        else:
            cpu()

def checkGame():
    global endGame
    if (gameBoard[0][0] == "X" and gameBoard[0][1] == "X" and gameBoard[0][2] == "X") or (gameBoard[1][0] == "X" and gameBoard[1][1] == "X" and gameBoard[1][2] == "X") or (gameBoard[2][0] == "X" and gameBoard[2][1] == "X" and gameBoard[2][2] == "X") or (gameBoard[0][0] == "X" and gameBoard[1][0] == "X" and gameBoard[2][0] == "X") or (gameBoard[0][1] == "X" and gameBoard[1][1] == "X" and gameBoard[2][1] == "X") or (gameBoard[0][2] == "X" and gameBoard[1][2] == "X" and gameBoard[2][2] == "X") or  (gameBoard[0][0] == "X" and gameBoard[1][1] == "X" and gameBoard[2][2] == "X") or (gameBoard[0][2] == "X" and gameBoard[1][1] == "X" and gameBoard[2][0] == "X"):
        print(Fore.YELLOW + "Player 1 Win")
        endGame = True
        return endGame
    elif (gameBoard[0][0] == "O" and gameBoard[0][1] == "O" and gameBoard[0][2] == "O" and playMode == 2) or (gameBoard[1][0] == "O" and gameBoard[1][1] == "O" and gameBoard[1][2] == "O" and playMode == 2) or (gameBoard[2][0] == "O" and gameBoard[2][1] == "O" and gameBoard[2][2] == "O" and playMode == 2) or (gameBoard[0][0] == "O" and gameBoard[1][0] == "O" and gameBoard[2][0] == "O" and playMode == 2) or (gameBoard[0][1] == "O" and gameBoard[1][1] == "O" and gameBoard[2][1] == "O" and playMode == 2) or (gameBoard[0][2] == "O" and gameBoard[1][2] == "O" and gameBoard[2][2] == "O" and playMode == 2) or  (gameBoard[0][0] == "O" and gameBoard[1][1] == "O" and gameBoard[2][2] == "O" and playMode == 2) or (gameBoard[0][2] == "O" and gameBoard[1][1] == "O" and gameBoard[2][0] == "O" and playMode == 2):
        print(Fore.YELLOW + "Player 2 Win")
        endGame = True
        return endGame
    elif (gameBoard[0][0] == "O" and gameBoard[0][1] == "O" and gameBoard[0][2] == "O" and playMode == 1) or (gameBoard[1][0] == "O" and gameBoard[1][1] == "O" and gameBoard[1][2] == "O" and playMode == 1) or (gameBoard[2][0] == "O" and gameBoard[2][1] == "O" and gameBoard[2][2] == "O" and playMode == 1) or (gameBoard[0][0] == "O" and gameBoard[1][0] == "O" and gameBoard[2][0] == "O" and playMode == 1) or (gameBoard[0][1] == "O" and gameBoard[1][1] == "O" and gameBoard[2][1] == "O" and playMode == 1) or (gameBoard[0][2] == "O" and gameBoard[1][2] == "O" and gameBoard[2][2] == "O" and playMode == 1) or  (gameBoard[0][0] == "O" and gameBoard[1][1] == "O" and gameBoard[2][2] == "O" and playMode == 1) or (gameBoard[0][2] == "O" and gameBoard[1][1] == "O" and gameBoard[2][0] == "O" and playMode == 1):
        print(Fore.YELLOW + "CPU Win")
        endGame = True
        return endGame
    elif (turn == 9):
        print(Fore.YELLOW + "DRAW")
        endGame = True
        return endGame 

#Main
playMode = int(input("ONE PLAYER or TWO PLAYERS\nENTER 1 OR 2\n"))
printBoard()
startTime = datetime.datetime.now()

if playMode == 2:
    while(endGame != True):
        player1()
        if checkGame():
            break
        player2()
        if checkGame():
            break        
else:
    while(endGame != True):
        player1()
        if checkGame():
            break
        cpu()
        if checkGame():
            break
    
endTime = datetime.datetime.now()
endTime = endTime - startTime
print("Game Duration:", endTime)