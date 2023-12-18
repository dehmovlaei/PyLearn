import sys
import random
from functools import partial
from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtUiTools import QUiLoader

def check():
    global keepon , count, p1_wins, p2_wins, cpu, draw
    winer = ""
    if (buttons[0][0].text() == "X" and buttons[0][1].text() == "X" and buttons[0][2].text() == "X") or (
            buttons[1][0].text() == "X" and buttons[1][1].text() == "X" and buttons[1][2].text() == "X") or (
            buttons[2][0].text() == "X" and buttons[2][1].text() == "X" and buttons[2][2].text() == "X") or (
            buttons[0][0].text() == "X" and buttons[1][0].text() == "X" and buttons[2][0].text() == "X") or (
            buttons[0][1].text() == "X" and buttons[1][1].text() == "X" and buttons[2][1].text() == "X") or (
            buttons[0][2].text() == "X" and buttons[1][2].text() == "X" and buttons[2][2].text() == "X") or (
            buttons[0][0].text() == "X" and buttons[1][1].text() == "X" and buttons[2][2].text() == "X") or (
            buttons[0][2].text() == "X" and buttons[1][1].text() == "X" and buttons[2][0].text() == "X"):
        winer = "player_1"
        p1_wins += 1
        ui.btn_10.setText(f"YOU\n{p1_wins}")
        keepon = False
    elif (buttons[0][0].text() == "O" and buttons[0][1].text() == "O" and buttons[0][2].text() == "O") or (
            buttons[1][0].text() == "O" and buttons[1][1].text() == "O" and buttons[1][2].text() == "O") or (
            buttons[2][0].text() == "O" and buttons[2][1].text() == "O" and buttons[2][2].text() == "O") or (
            buttons[0][0].text() == "O" and buttons[1][0].text() == "O" and buttons[2][0].text() == "O") or (
            buttons[0][1].text() == "O" and buttons[1][1].text() == "O" and buttons[2][1].text() == "O") or (
            buttons[0][2].text() == "O" and buttons[1][2].text() == "O" and buttons[2][2].text() == "O") or (
            buttons[0][0].text() == "O" and buttons[1][1].text() == "O" and buttons[2][2].text() == "O") or (
            buttons[0][2].text() == "O" and buttons[1][1].text() == "O" and buttons[2][0].text() == "O"):
        winer = "player_II"
        if cpu: winer = "CPU"
        p2_wins += 1
        ui.btn_12.setText(f"{winer}\n{p2_wins}")
        keepon = False
    elif count == 9:
        winer = "NO ONE"
        draw += 1
        keepon = False
        ui.btn_11.setText(f"DRAW\n{draw}")

    if winer not in "":
        msg_box(winer, "Has WIN This Turn", "Congratulations")


def reset():
    global player, count, cpu, keepon
    player, count, cpu, keepon = 1, 0, True, True
    for i in range(3):
        for j in range(3):
            buttons[i][j].setText("")


def mode(flag):
    global cpu
    cpu = flag


def play_cpu():
    global player, count
    if keepon and count <= 9:
        row, col = random.randint(0, 2), random.randint(0, 2)
        if buttons[row][col].text() == "":
            buttons[row][col].setText("O")
            buttons[row][col].setStyleSheet("color: rgb(241, 178, 55); background-color: rgb(31, 53, 64)")
            player = 1
            count += 1
            check()
        else:
            play_cpu()


def play(row, col):
    global player
    global buttons
    global cpu
    global count
    if player == 1 and buttons[row][col].text() == "" and keepon:
        buttons[row][col].setText("X")
        buttons[row][col].setStyleSheet("color: rgb(49, 196, 190); background-color: rgb(31, 53, 64)")
        player = 2
        count += 1
        check()
        if cpu:
            play_cpu()
    elif player == 2 and not cpu and buttons[row][col].text() == "" and keepon:
        buttons[row][col].setText("O")
        buttons[row][col].setStyleSheet("color: rgb(241, 178, 55); background-color: rgb(31, 53, 64)")
        player = 1
        count += 1
        check()


def msg_box(var_1, msg_1, title_1):
    msgBox = QMessageBox()
    msgBox.setText(f"{var_1} {msg_1}")
    msgBox.setWindowTitle(f"{title_1}!")
    msgBox.exec()


player = 1
p1_wins = 0
p2_wins = 0
draw = 0
count = 0
cpu = True
keepon = True

loader = QUiLoader()
app = QApplication(sys.argv)
ui = loader.load("mainWindow.ui")
ui.show()

buttons = [[ui.btn_1, ui.btn_2, ui.btn_3],
          [ui.btn_4, ui.btn_5, ui.btn_6],
          [ui.btn_7, ui.btn_8, ui.btn_9]]

for i in range(3):
    for j in range(3):
        buttons[i][j].clicked.connect(partial(play, i, j))

ui.radio_1.clicked.connect(partial(mode, False))
ui.radio_2.clicked.connect(partial(mode, True))
ui.btn_13.clicked.connect(reset)
ui.btn_14.clicked.connect(partial(msg_box, "Version:20231812", "Tic Tac Toe By AmirHossein Dehmovlaei", "About US"))

app.exec()