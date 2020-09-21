from PyQt5.QtWidgets import QApplication, QPushButton, QButtonGroup, QWidget, QMainWindow, QGridLayout, QLayout, \
    QLineEdit
import sys

class TicTacToe(QWidget):
    def __init__(self, widget, *args, **kwargs):
        super().__init__(widget, *args, **kwargs)
        self.step = 0
        self.player = [set(), set()]
        self.initUi()

    def initUi(self):
        self.line = QLineEdit()
        self.line.setReadOnly(True)
        size = self.parent().rect()
        self.setGeometry(size)
        self.layout = QGridLayout(self)
        self.layout.setSizeConstraint(QLayout.SetMaximumSize)
        self.setLayout(self.layout)
        self.layout.addWidget(self.line, 0, 0, 1, 3)
        self.buttons = []
        for i in range(9):
            self.buttons.append(QPushButton())
            self.layout.addWidget(self.buttons[i], (i%3)+1, (i//3))
            self.buttons[i].setText(str(i))
        self.buttonGroup = QButtonGroup()
        for i in range(9):
            self.buttonGroup.addButton(self.buttons[i], i)
        self.buttonGroup.buttonClicked["int"].connect(self.button_push)

    def button_push(self, a):
        self.player[self.step%2].add(a)
        self.buttons[a].setText("x" if self.step % 2 == 0 else "o")
        self.isWinner()
        self.step += 1
        self.buttons[a].setDisabled(True)

    def isWinner(self):
        def set_text(a):
            self.line.setText("player {} win!".format(str(a)))
        line = {0,3,6}
        for i in range(3):
            if line.issubset(self.player[self.step%2]):
                set_text(self.step%2 + 1)
            line = {i + 1 for i in line}
        line = {0,1,2}
        for i in range(3):
            if line.issubset(self.player[self.step%2]):
                set_text(self.step % 2 + 1)
            line = {i + 3 for i in line}
        line = {0, 4, 8}
        if line.issubset(self.player[self.step % 2]):
            set_text(self.step % 2 + 1)
        line = {2,4,6}
        if line.issubset(self.player[self.step % 2]):
            set_text(self.step % 2 + 1)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_windows = QMainWindow()
    main_windows.resize(300, 200)
    game = TicTacToe(main_windows)
    main_windows.show()
    app.exec_()