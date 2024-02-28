import sys
import random
from functools import partial
from sudoku import Sudoku
from PySide6.QtWidgets import *
from mainwindow import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.menu_new.triggered.connect(self.new_game)
        self.ui.menu_open.triggered.connect(self.open_file)
        self.line_edits = [[None for _ in range(9)] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                new_cell = QLineEdit()
                self.ui.grid_layout.addWidget(new_cell, i, j)
                new_cell.textChanged.connect(partial(self.validation, i, j))
                self.line_edits[i][j] = new_cell
        self.new_game()

    def new_game(self):
        puzzle = Sudoku(3, seed=random.randint(1, 1000)).difficulty(0.5)
        for i in range(9):
            for j in range(9):
                if puzzle.board[i][j] is not None:
                    self.line_edits[i][j].setText(str(puzzle.board[i][j]))
                    self.line_edits[i][j].setReadOnly(True)
                else:
                    self.line_edits[i][j].setText("")

    def open_file(self):
        file_path = QFileDialog.getOpenFileName(self, 'Open file', './', '')
        f = open(file_path, "r")
        big_text = f.read()
        rows = big_text.split("\n")
        for row in rows:

    def validation(self, i, j, text):
        if text not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            self.line_edits[i][j].setText("")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
