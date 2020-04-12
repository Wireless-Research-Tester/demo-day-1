""" Welcome Window created using Python Code only
    Author: Austin Langebeck-Fissinger
"""
import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc
from PyQt5.QtCore import Qt


class WelcomeWindow(qtw.QWidget):

    switch_window = qtc.pyqtSignal()

    def __init__(self):
        """ Welcome Window Constructor """

        super().__init__()
        # WelcomeWindow UI code goes here

        # WelcomeWindow Widgets
        self.instructions = qtw.QLabel('Create new project or open existing project.', margin=0)
        self.recent_label = qtw.QLabel('Recent Projects Files:')

        self.new_button = qtw.QPushButton('Create New')
        self.new_button.clicked.connect(self.createNew)

        self.open_button = qtw.QPushButton('Open')
        self.open_button.clicked.connect(self.switch)

        self.recent_list = qtw.QListWidget(parent=None)
        self.wrc_logo = qtw.QLabel()
        self.wrc_logo.setText('')
        self.wrc_logo.setPixmap(qtg.QPixmap("../WRC_logo.png"))

        # creating the nested layouts
        main_layout = qtw.QHBoxLayout()
        self.setLayout(main_layout)

        left_layout = qtw.QVBoxLayout()
        left_layout.setContentsMargins(0, 0, 0, 50)
        left_layout.setSpacing(25)
        main_layout.addLayout(left_layout)
        left_layout.addWidget(self.instructions)
        left_layout.addWidget(self.wrc_logo)
        left_layout.addWidget(self.new_button)
        left_layout.addWidget(self.open_button)

        right_layout = qtw.QVBoxLayout()
        main_layout.addLayout(right_layout)
        right_layout.addWidget(self.recent_label)
        right_layout.addWidget(self.recent_list)

        # Adjusting Widget Positioning
        self.instructions.setAlignment(Qt.AlignTop | Qt.AlignLeft)  # move instruction label to top left corner
        self.recent_label.setAlignment(Qt.AlignTop | Qt.AlignCenter)
        self.recent_list.addItems(["file_01", "file_02", "file_03", ".", ".", "."])  # temp place holder text
        self.new_button.setSizePolicy(
            qtw.QSizePolicy.Minimum,
            qtw.QSizePolicy.Maximum,
        )
        self.open_button.setSizePolicy(
            qtw.QSizePolicy.Minimum,
            qtw.QSizePolicy.Maximum,
        )

        # End WelcomeWindow UI code
        self.InitWelcome()

    def InitWelcome(self):
        self.setWindowTitle("Welcome!")
        self.resize(600, 375)
        self.show()

    # def test(self):
    #     print('test complete')

    def createNew(self):
        filename, _ = qtw.QFileDialog.getSaveFileName(
            self,
            "Select save location",
            qtc.QDir.homePath(),
            'Measurement File (*.wrc)'
        )
        fh = open(filename, 'w')
        fh.write(str(fh))
        self.switch_window.emit()

    def switch(self):
        self.switch_window.emit()


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    ww = WelcomeWindow()
    sys.exit(app.exec())
