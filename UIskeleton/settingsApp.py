import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc
from PyQt5.QtCore import Qt
from UIskeleton import settingsUI
from UIskeleton.settingsUI import Ui_SettingsWindow
from UIskeleton import loadingUI
from PyQt5 import uic


# S_Ui, S_Base = uic.loadUiType('settingsUIui.ui')


class SettingsWindow(qtw.QWidget, Ui_SettingsWindow):
    switch_window = qtc.pyqtSignal()
    start_load = qtc.pyqtSignal()

    def __init__(self):
        """Settings Window constructor"""
        super().__init__()
        self.setupUi(self)

        ##################
        # Connect Events #
        ##################

        self.select_pbttn.clicked.connect(self.switch)
        # self.select_pbttn.clicked.connect(loadingUI.LoadWindow.onButtonClick)
        self.show()

    def switch(self):
        self.switch_window.emit()


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)

    # it's required to save a reference to MainWindow.
    # if it goes out of scope, it will be destroyed.
    mw = SettingsWindow()
    sys.exit(app.exec())
