import sys
from PyQt5 import QtCore, QtWidgets
from UIskeleton import loadingUI, welcomeUI, settingsApp, graphwindowUI2, graphwindowApp


class Controller:

    def __init__(self):
        pass

    def show_welcome(self):
        self.welcome = welcomeUI.WelcomeWindow()
        self.welcome.switch_window.connect(self.show_settings)
        # close main window
        self.welcome.show()

    def show_settings(self):
        # self.settings = settingsUI.Ui_SettingsWindow()
        self.welcome.close()
        self.settings = settingsApp.SettingsWindow()
        self.settings.switch_window.connect(self.show_loading)
        self.settings.show()
        # self.SettingsWindow = QtWidgets.QWidget()
        # self.ui = settingsUI.Ui_SettingsWindow()
        # self.ui.setupUi(self.SettingsWindow)
        # self.SettingsWindow.show()

    def show_loading(self):
        self.loading = loadingUI.LoadWindow()
        self.loading.switch_window.connect(self.show_main)
        self.settings.close()
        self.loading.show()
        # self.loading.download()

    def show_main(self):
        self.graph = graphwindowApp.GraphWindow()
        self.graph.switch_window.connect(self.return_welcome)
        self.loading.close()
        self.graph.show()
        # print('reached main window')

    def return_welcome(self):
        self.back_home = welcomeUI.WelcomeWindow()
        self.back_home.switch_window.connect(self.show_settings)
        self.graph.close()
        self.back_home.show()

        # print('made it back to welcome')


def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_welcome()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
