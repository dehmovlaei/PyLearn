import sys
import random
from functools import partial
from sudoku import Sudoku
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from mainwindow import Ui_MainWindow


def help_func():
    msgBox = QMessageBox()
    msgBox.setText("Pay attention that there should not be duplicate numbers in any row or column, and also in "
                   "any block of three, considering that this entire table is made by putting together 9 blocks "
                   "of three.")
    msgBox.exec()


def exit_func():
    exit()


def about():
    msgBox = QMessageBox()
    msgBox.setText("First version of my SUDOKU designed by AmirHossein Dehmovlaei")
    msgBox.exec()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.menu_new.triggered.connect(self.new_game)
        self.ui.menu_open.triggered.connect(self.open_file)
        self.ui.menu_solve.triggered.connect(self.show_solve)
        self.ui.menu_help.triggered.connect(help_func)
        self.ui.menu_about.triggered.connect(about)
        self.ui.menu_exit.triggered.connect(exit_func)
        self.line_edits = [[None for _ in range(9)] for _ in range(9)]
        self.user_input = [[False for _ in range(9)] for _ in range(9)]
        self.win_flag = True
        self.solve = self.new_game()

    def new_game(self):
        layout = self.ui.grid_layout
        for i in (range(layout.count())):
            item = layout.itemAt(i)
            widget = item.widget()
            widget.deleteLater()
        for i in range(9):
            for j in range(9):
                new_cell = QLineEdit()
                new_cell.setFixedWidth(69)
                new_cell.setFixedHeight(69)
                new_cell.setFont("Adobe Arabic")
                new_cell.setStyleSheet("font-weight:bold; font-size:69px; color:rgb(25, 42, 50)")
                new_cell.setAlignment(Qt.AlignCenter)
                self.ui.grid_layout.addWidget(new_cell, i, j)
                item_index = self.ui.grid_layout.indexOf(new_cell)
                new_cell.textChanged.connect(partial(self.validation, i, j, item_index))
                self.line_edits[i][j] = new_cell
        puzzle = Sudoku(3, seed=random.randint(1, 1000)).difficulty(0.5)
        solve = puzzle.solve()
        for i in range(9):
            for j in range(9):
                self.line_edits[i][j].setReadOnly(False)
                if puzzle.board[i][j] is not None:
                    self.line_edits[i][j].setText(str(puzzle.board[i][j]))
                    self.line_edits[i][j].setReadOnly(True)
                    self.user_input[i][j] = True
                else:
                    self.line_edits[i][j].setText("")
        print(puzzle.board)
        print(self.user_input)
        self.solve = solve
        return solve

    def open_file(self):
        try:
            file_path = QFileDialog.getOpenFileName(self, 'Open file', './', '')[0]
            print(file_path)
            f = open(file_path, "r")
            big_text = f.read()
            rows = big_text.split("\n")
            puzzle_board = [[None for _ in range(9)] for _ in range(9)]
            for i in range(len(rows)):
                print(len(rows))
                cells = rows[i].split(" ")
                for j in range(len(cells)):
                    puzzle_board[i][j] = int(cells[j])
            for i in range(9):
                for j in range(9):
                    self.line_edits[i][j].setReadOnly(False)
                    if puzzle_board[i][j] != 0:
                        self.line_edits[i][j].setText(str(puzzle_board[i][j]))
                        self.line_edits[i][j].setReadOnly(True)
                    else:
                        self.line_edits[i][j].setText("")
            return True
        except:
            return False

    def show_solve(self):
        msgBox = QMessageBox()
        msgBox.setText(f"{self.solve}")
        msgBox.exec()

    def check(self, row, col, item_index):
        self.win_flag = True
        if 0 <= row <= 2 and 0 <= col <= 2:
            number_1 = self.line_edits[row][col].text()
            for i in range(3):
                for j in range(3):
                    number_2 = self.line_edits[i][j].text()
                    if number_1 == number_2 and number_1 != "" and i != row and j != col:
                        self.ui.grid_layout.itemAt(item_index).widget().setStyleSheet(
                            "font-weight:bold; font-size:69px; color:rgb(255, 0, 0)")
                        self.win_flag = False
        elif 0 <= row <= 2 and 3 <= col <= 5:
            number_1 = self.line_edits[row][col].text()
            for i in range(3):
                for j in range(3, 6):
                    number_2 = self.line_edits[i][j].text()
                    if number_1 == number_2 and number_1 != "" and i != row and j != col:
                        self.ui.grid_layout.itemAt(item_index).widget().setStyleSheet(
                            "font-weight:bold; font-size:69px; color:rgb(255, 0, 0)")
                        self.win_flag = False
        elif 0 <= row <= 2 and 6 <= col <= 8:
            number_1 = self.line_edits[row][col].text()
            for i in range(3):
                for j in range(6, 9):
                    number_2 = self.line_edits[i][j].text()
                    if number_1 == number_2 and number_1 != "" and i != row and j != col:
                        self.ui.grid_layout.itemAt(item_index).widget().setStyleSheet(
                            "font-weight:bold; font-size:69px; color:rgb(255, 0, 0)")
                        self.win_flag = False
        elif 3 <= row <= 5 and 0 <= col <= 2:
            number_1 = self.line_edits[row][col].text()
            for i in range(3, 6):
                for j in range(3):
                    number_2 = self.line_edits[i][j].text()
                    if number_1 == number_2 and number_1 != "" and i != row and j != col:
                        self.ui.grid_layout.itemAt(item_index).widget().setStyleSheet(
                            "font-weight:bold; font-size:69px; color:rgb(255, 0, 0)")
                        self.win_flag = False
        elif 3 <= row <= 5 and 3 <= col <= 5:
            number_1 = self.line_edits[row][col].text()
            for i in range(3, 6):
                for j in range(3, 6):
                    number_2 = self.line_edits[i][j].text()
                    if number_1 == number_2 and number_1 != "" and i != row and j != col:
                        self.ui.grid_layout.itemAt(item_index).widget().setStyleSheet(
                            "font-weight:bold; font-size:69px; color:rgb(255, 0, 0)")
                        self.win_flag = False
        elif 3 <= row <= 5 and 6 <= col <= 8:
            number_1 = self.line_edits[row][col].text()
            for i in range(3, 6):
                for j in range(6, 9):
                    number_2 = self.line_edits[i][j].text()
                    if number_1 == number_2 and number_1 != "" and i != row and j != col:
                        self.ui.grid_layout.itemAt(item_index).widget().setStyleSheet(
                            "font-weight:bold; font-size:69px; color:rgb(255, 0, 0)")
                        self.win_flag = False
        elif 6 <= row <= 8 and 0 <= col <= 2:
            number_1 = self.line_edits[row][col].text()
            for i in range(6, 9):
                for j in range(3):
                    number_2 = self.line_edits[i][j].text()
                    if number_1 == number_2 and number_1 != "" and i != row and j != col:
                        self.ui.grid_layout.itemAt(item_index).widget().setStyleSheet(
                            "font-weight:bold; font-size:69px; color:rgb(255, 0, 0)")
                        self.win_flag = False
        elif 6 <= row <= 8 and 3 <= col <= 5:
            number_1 = self.line_edits[row][col].text()
            for i in range(6, 9):
                for j in range(3, 6):
                    number_2 = self.line_edits[i][j].text()
                    if number_1 == number_2 and number_1 != "" and i != row and j != col:
                        self.ui.grid_layout.itemAt(item_index).widget().setStyleSheet(
                            "font-weight:bold; font-size:69px; color:rgb(255, 0, 0)")
                        self.win_flag = False
        elif 6 <= row <= 8 and 6 <= col <= 8:
            number_1 = self.line_edits[row][col].text()
            for i in range(6, 9):
                for j in range(6, 9):
                    number_2 = self.line_edits[i][j].text()
                    if number_1 == number_2 and number_1 != "" and i != row and j != col:
                        self.ui.grid_layout.itemAt(item_index).widget().setStyleSheet(
                            "font-weight:bold; font-size:69px; color:rgb(255, 0, 0)")
                        self.win_flag = False

        for i in range(0, 9):
            for j in range(0, 9):
                number_1 = self.line_edits[i][j].text()
                for k in range(1, 9):
                    number_2 = self.line_edits[i][k].text()
                    if number_1 == number_2 and number_1 != "" and j != k:
                        self.ui.grid_layout.itemAt(item_index).widget().setStyleSheet(
                            "font-weight:bold; font-size:69px; color:rgb(255, 0, 0)")
                        self.win_flag = False
        for j in range(0, 9):
            for i in range(0, 9):
                number_1 = self.line_edits[i][j].text()
                for k in range(1, 9):
                    number_2 = self.line_edits[k][j].text()
                    if number_1 == number_2 and number_1 != "" and i != k:
                        self.ui.grid_layout.itemAt(item_index).widget().setStyleSheet(
                            "font-weight:bold; font-size:69px; color:rgb(255, 0, 0)")
                        self.win_flag = False
        if self.win_flag:
            self.user_input[row][col] = True

    def validation(self, i, j, item_index, text):
        if text not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            self.line_edits[i][j].setText("")
        self.ui.grid_layout.itemAt(item_index).widget().setStyleSheet(
            "font-weight:bold; font-size:69px; color:rgb(25, 42, 50)")
        self.check(i, j, item_index)
        if self.win_check():
            msgBox = QMessageBox()
            msgBox.setText("YOU WIN ❤️")
            msgBox.exec()

    def win_check(self):
        for i in range(9):
            for j in range(9):
                if not self.user_input[i][j]:
                    return False
        return True


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
