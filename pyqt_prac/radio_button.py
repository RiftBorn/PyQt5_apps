import sys
from PyQt5.QtWidgets import (QLabel, QRadioButton, QPushButton, QVBoxLayout, QApplication, QWidget)


class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.lbl = QLabel('Which do you like best?')
        self.dog = QRadioButton('Dogs')
        self.cat = QRadioButton('Cats')
        self.btn = QPushButton('Select')

        layout = QVBoxLayout()
        layout.addWidget(self.lbl)
        layout.addWidget(self.dog)
        layout.addWidget(self.cat)
        layout.addWidget(self.btn)

        self.setLayout(layout)
        self.setWindowTitle('PyQt5 Lesson 10')

        self.btn.clicked.connect(lambda: self.btn_clk(self.dog.isChecked(), self.cat.isChecked(), self.lbl))

        self.show()
        pass

    def btn_clk(self, dog_chk, cat_chk, lbl):
        print('dog check is: ', dog_chk)
        if dog_chk:
            lbl.setText('I guess you like dogs')
        elif cat_chk:
            lbl.setText('I guess you like cats')
        else:
            lbl.setText('I guess you like neither')


app = QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec_())
