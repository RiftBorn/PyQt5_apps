import sys
from PyQt5 import QtWidgets, QtGui


def window():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    b = QtWidgets.QPushButton(w)
    b.setText('Please push me.')
    l1 = QtWidgets.QLabel(w)
    l1.setText('Hello World')
    # l2 = QtWidgets.QLabel(w)
    # l2.setPixmap(QtGui.QPixmap('cat.jpeg'))
    v_box = QtWidgets.QVBoxLayout()
    h_box_1 = QtWidgets.QHBoxLayout()
    h_box_2 = QtWidgets.QHBoxLayout()
    h_box_1.addStretch()  # strech the h box so that it is to the right edge
    h_box_2.addStretch()
    h_box_1.addWidget(b)  # strech the h box so that the botton is at the middle 
    h_box_2.addWidget(l1)
    h_box_1.addStretch()
    h_box_2.addStretch()
    v_box.addLayout(h_box_1)
    v_box.addLayout(h_box_2)
    w.setLayout(v_box)
    w.setWindowTitle('PyQt5 Lession 2')
    # w.setGeometry(100, 100, 1500, 1000)
    # l2.move(120, 90)
    w.show()
    sys.exit(app.exec_())

window()
