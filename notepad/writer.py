import os
import sys
from PyQt5.QtWidgets import \
    QApplication, \
    QTextEdit, \
    QWidget, \
    QPushButton, \
    QVBoxLayout, \
    QHBoxLayout, \
    QFileDialog, \
    QMainWindow, \
    QAction, \
    qApp, \
    QDesktopWidget


class Notepad(QWidget):

    def __init__(self):
        super(Notepad, self).__init__()
        self.text = QTextEdit(self)
        self.clear_button = QPushButton('Clear')
        self.save_button = QPushButton('Save')
        self.open_button = QPushButton('Open')

        self.init_ut()

    def init_ut(self):
        v_layout = QVBoxLayout()
        h_layout = QHBoxLayout()

        h_layout.addWidget(self.clear_button)
        h_layout.addWidget(self.save_button)
        h_layout.addWidget(self.open_button)

        v_layout.addWidget(self.text)
        v_layout.addLayout(h_layout)

        self.clear_button.clicked.connect(self.clear_text)
        self.save_button.clicked.connect(self.save_text)
        self.open_button.clicked.connect(self.open_text)

        self.setLayout(v_layout)
        self.setWindowTitle('PyQt5 TextEdit')

    def save_text(self):
        filename = QFileDialog.getSaveFileName(self, 'Save File', os.getenv('HOME'))
        if not filename[0]:
            return
        with open(filename[0], 'w') as file:
            my_text = self.text.toPlainText()
            file.write(my_text)

    def clear_text(self):
        self.text.clear()

    def open_text(self):
        filename = QFileDialog.getOpenFileName(self, 'Open File', os.getenv('HOME'))
        if not filename[0]:
            return
        with open(filename[0], 'r') as file:
            file_text = file.read()
            self.text.setText(file_text)


class Writer(QMainWindow):

    def __init__(self):
        super().__init__()

        self.form_widget = Notepad()
        self.setCentralWidget(self.form_widget)

        self.init_ui()

    def init_ui(self):
        bar = self.menuBar()
        file = bar.addMenu('file')

        new_action = QAction('New', self)
        new_action.setShortcut('Ctrl+N')

        save_action = QAction('&Save', self)
        save_action.setShortcut('Ctrl+S')

        open_action = QAction('&Open', self)

        quit_action = QAction('&Quit', self)

        # add actions to menus
        file.addAction(new_action)
        file.addAction(open_action)
        file.addAction(save_action)
        file.addAction(quit_action)

        # events
        quit_action.triggered.connect(self.quit_trigger)
        file.triggered.connect(self.respond)

        self.set_location_on_the_screen()

        self.show()

    @staticmethod
    def quit_trigger():
        qApp.quit()

    def respond(self, q):
        signal = q.text()

        function_chart = {
            "New": self.form_widget.clear_text,
            "&Open": self.form_widget.open_text,
            "&Save": self.form_widget.save_text,
        }

        function_chart.get(signal)()

    def set_location_on_the_screen(self):
        available = QDesktopWidget().availableGeometry()
        screen = QDesktopWidget().screenGeometry()

        loc = self.geometry()
        x = available.width() - loc.width()
        y = 2 * available.height() - screen.height() - loc.height()
        self.move(x, y)


app = QApplication(sys.argv)
writer = Writer()
sys.exit(app.exec_())
