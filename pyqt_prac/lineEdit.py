import sys
from PyQt5.QtWidgets import (QLineEdit, QSlider, QPushButton, QVBoxLayout, QApplication, QWidget)


class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.le = QLineEdit()
        self.b1 = QPushButton('Clear')
        self.b2 = QPushButton('Print')

        v_box = QVBoxLayout()
        v_box.addWidget(self.le)
        v_box.addWidget(self.b1)
        v_box.addWidget(self.b2)

        self.setLayout(v_box)

        self.setWindowTitle('PyQt5 lesson 6')

        self.b1.clicked.connect(self.btn_clk)
        self.b2.clicked.connect(self.btn_clk)
        self.show()

    def btn_clk(self):
        sender = self.sender()
        if sender.text() == 'Print':
            print(self.le.text())
        else:
            self.le.clear()


print('sys.argv is: ', sys.argv)
app = QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec_())
