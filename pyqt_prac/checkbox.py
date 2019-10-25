import sys
from PyQt5.QtWidgets import (QLabel, QCheckBox, QPushButton, QVBoxLayout, QApplication, QWidget)


class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.lbl = QLabel()
        self.cbx = QCheckBox('Do you like dogs?')
        self.btn = QPushButton('Push Me!')

        layout = QVBoxLayout()
        layout.addWidget(self.lbl)
        layout.addWidget(self.cbx)
        layout.addWidget(self.btn)

        self.setLayout(layout)

        self.setWindowTitle('Some Title')

        self.btn.clicked.connect(lambda: self.btn_clk(self.cbx.isChecked(), self.lbl))
        self.show()

    @staticmethod
    def btn_clk(chk, lbl):
        if chk:
            lbl.setText('I guss you like dogs')
        else:
            lbl.setText('Dogs hater then')


app = QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec_())
