from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from UIskeleton.graphwindowUI2 import Ui_GraphWindow
import sys
import matplotlib
from PyQt5.QtWidgets import *

# Make sure that we are using QT5
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class GraphWindow(qtw.QMainWindow, Ui_GraphWindow):
    switch_window = qtc.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.main_widget = MplWidget(self)
        # sc = MyStaticMplCanvas(self.main_widget, width=5, height=4, dpi=100)
        self.main_widget.setFocus()
        self.setCentralWidget(self.main_widget)
        self.main_menu_bttn.clicked.connect(self.switch)
        self.show()

    def switch(self):
        self.switch_window.emit()


# Myplotlib widget
class MplWidget(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        filename = 'sample_output.csv'
        req_freq = 1000
        start_freq = 1000
        freq_inc = 100
        angle = 1
        self.canvas = FigureCanvas(Figure())
        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas)
        self.canvas.axes = self.canvas.figure.add_subplot(111, projection='polar', autoscale_on=True)
        self.setLayout(vertical_layout)

        # read the csv into pandas dataframe
        df = pd.read_csv(filename)

        # Sort the data by frequency, phi, and theta
        df = df.sort_values(by=['freq', 'phi', 'theta'])

        # Define the number of rows per frequency
        theta_max = 360 // angle - 1

        # Find the starting point in dataframe
        index = ((req_freq - start_freq) // freq_inc) * theta_max

        # Isolate phi column and convert to radians
        theta = df.iloc[index:index + theta_max, [3]]
        phi = theta['phi'] * np.pi / 180

        # Isolate value column
        r = df.iloc[index:index + theta_max, [4]]
        value = r['value']

        # Create polar plot
        req_freq_string = str(req_freq)
        # ax = plt.subplot(111, projection='polar', autoscale_on=True)
        self.canvas.axes.plot(phi, value, label=req_freq_string + ' MHz')
        self.canvas.axes.grid(True)
        plt.title('2D Plane (XY axis)')
        # plt.legend(loc='upper right')
        # plt.show()


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    filename = "sample_output.csv"
    gw = GraphWindow()
    sys.exit(app.exec())
