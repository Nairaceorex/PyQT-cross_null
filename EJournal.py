from PyQt5.QtWidgets import QApplication, QPushButton, QButtonGroup, QWidget, QMainWindow, QGridLayout, QLayout, \
    QLineEdit, QTableWidget, QSpinBox, QTableWidgetItem
import sys

class Journal(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUi()
        self.button.clicked.connect(self.add_note)

    def initUi(self):
        self.resize(self.parent().size())
        self.table = QTableWidget(self)
        self.table.setGeometry(0, 0, 320, 470)
        self.table.move(10,10)
        self.line = QLineEdit("ФИО", self)
        self.line.move(340, 10)
        self.spinBox = QSpinBox(self)
        self.spinBox.move(340, 40)
        self.spinBox.setMaximum(5)
        self.spinBox.setMinimum(2)
        self.button = QPushButton("Добавить", self)
        self.button.move(340, 70)

    def add_note(self):
        student = self.line.text()
        mark = self.spinBox.value()
        if self.table.columnCount() == 0:
            self.table.setRowCount(1)
            self.table.setColumnCount(2)
            self.table.setItem(0, 0, QTableWidgetItem(student))
            self.table.setItem(0, 1, QTableWidgetItem(str(mark)))
        else:
            for i in range(self.table.rowCount()):
                if self.table.item(i, 0).text() == student:
                    index = 1
                    while index < self.table.columnCount():
                        try:
                            if self.table.item(i, index).text() == '':
                                print(i, index)
                                break
                        except:
                            self.table.setItem(i, index, QTableWidgetItem(str(mark)))
                            break
                        index += 1
                    else:
                        self.table.insertColumn(self.table.columnCount())
                        print(i, index)
                        self.table.setItem(i, index, QTableWidgetItem(str(mark)))
                    break
            else:
                c = self.table.rowCount()
                self.table.insertRow(c)
                self.table.setItem(c, 0, QTableWidgetItem(student))
                self.table.setItem(c, 1, QTableWidgetItem(str(mark)))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_windows = QMainWindow()
    j = Journal(main_windows)
    main_windows.resize(500, 500)
    main_windows.show()
    app.exec_()