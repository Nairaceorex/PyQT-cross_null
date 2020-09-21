from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QButtonGroup
import sys


class myMainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.step = 0
        self.initUi()

    def initUi(self):
        self.buttons = []
        width, height = 0, 0
        for i in range(9):
            if width % 300 == 0:
                height += 50
            self.buttons.append(QPushButton(self))
            self.buttons[i].move(width % 300 + 50, height)
            self.buttons[i].setText(str(i))
            width += 100
        self.buttonGroup = QButtonGroup()
        for i in range(9):
            self.buttonGroup.addButton(self.buttons[i], i)
        self.buttonGroup.buttonClicked["int"].connect(self.button_push)

    def button_push(self, a):
        self.buttons[a].setText("x" if self.step % 2 == 0 else "o")
        self.step += 1
        self.buttons[a].setDisabled(True)

    def check(self):
        if self.buttons[0] == 'x' and self.buttons[1]== 'x' and self.buttons[2]== 'x': print('win X')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_windows = myMainWindow()
    main_windows.check()
    main_windows.resize(400, 400)
    main_windows.show()
    app.exec_()
