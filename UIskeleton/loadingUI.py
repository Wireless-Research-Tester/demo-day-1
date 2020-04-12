""" Measurement Progress created using Python Code only
    Author: Austin Langebeck-Fissinger
"""
import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc
from PyQt5.QtCore import Qt, QThread, pyqtSignal
import time

TIME_LIMIT = 100

"""Thread used to make loading smooth"""
class External(QThread):
    """
    Runs a counter thread.
    """
    countChanged = pyqtSignal(int)
    # switch_window = qtc.pyqtSignal()

    def run(self):
        count = 0
        while count < TIME_LIMIT:
            count += .5
            time.sleep(.01)
            # if count == 100:
            #     self.switch_window.emit()
            self.countChanged.emit(count)


class LoadWindow(qtw.QWidget):
    switch_window = qtc.pyqtSignal()

    def __init__(self):
        super().__init__()

        # Code here
        # Insert Widgets
        self.prog_label = qtw.QLabel('Performing Measurement ...')
        self.prog_bar = qtw.QProgressBar()
        self.continue_buttn = qtw.QPushButton('Continue')
        self.continue_buttn.setDefault(True)
        self.continue_buttn.clicked.connect(self.onButtonClick)
        self.cancel_buttn = qtw.QPushButton('Cancel')
        self.wrc_logo = qtw.QLabel()
        self.wrc_logo.setText('')
        self.wrc_logo.setPixmap(qtg.QPixmap("../WRC_logo.png"))
        verticalSpacer = qtw.QSpacerItem(100, 40, qtw.QSizePolicy.Minimum, qtw.QSizePolicy.Expanding)
        main_layout = qtw.QVBoxLayout()
        self.setLayout(main_layout)

        top_layout = qtw.QVBoxLayout()
        top_layout.addWidget(self.prog_label)
        top_layout.addWidget(self.wrc_logo)
        top_layout.addWidget(self.prog_bar)
        top_layout.setContentsMargins(0, 0, 0, 10)
        main_layout.addLayout(top_layout)

        bottom_layout = qtw.QHBoxLayout()
        bottom_layout.addWidget(self.cancel_buttn)
        bottom_layout.addWidget(self.continue_buttn)
        main_layout.addLayout(bottom_layout)

        # Edit Widget Positioning
        self.prog_label.setAlignment(Qt.AlignTop | Qt.AlignLeft)  # move instruction label to top left corner
        top_layout.addItem(verticalSpacer)
        # End Code
        self.InitLoading()
        # self.download()

    def InitLoading(self):
        self.setWindowTitle("Measurement Progress Window")
        self.resize(600, 275)
        self.show()

    def onButtonClick(self):
        self.calc = External()
        self.calc.countChanged.connect(self.onCountChanged)
        self.calc.start()

    def onCountChanged(self, value):
        self.prog_bar.setValue(value)
        if value == 100:
            self.switch_window.emit()


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    pw = LoadWindow()  # pw = progress window
    sys.exit(app.exec())
