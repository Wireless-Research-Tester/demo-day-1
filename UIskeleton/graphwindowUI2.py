# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'graphwindowUI.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GraphWindow(object):
    def setupUi(self, GraphWindow):
        GraphWindow.setObjectName("GraphWindow")
        GraphWindow.setEnabled(True)
        GraphWindow.resize(1661, 789)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(GraphWindow.sizePolicy().hasHeightForWidth())
        GraphWindow.setSizePolicy(sizePolicy)
        GraphWindow.setAnimated(True)
        GraphWindow.setDockNestingEnabled(False)
        self.centralwidget = QtWidgets.QWidget(GraphWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.MplWidget = MplWidget(self.centralwidget)
        self.MplWidget.setGeometry(QtCore.QRect(560, 120, 571, 401))
        self.MplWidget.setObjectName("MplWidget")
        GraphWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(GraphWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1661, 22))
        self.menubar.setObjectName("menubar")
        GraphWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(GraphWindow)
        self.statusbar.setObjectName("statusbar")
        GraphWindow.setStatusBar(self.statusbar)
        self.dockWidget_3 = QtWidgets.QDockWidget(GraphWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidget_3.sizePolicy().hasHeightForWidth())
        self.dockWidget_3.setSizePolicy(sizePolicy)
        self.dockWidget_3.setMaximumSize(QtCore.QSize(350, 524287))
        self.dockWidget_3.setFeatures(
            QtWidgets.QDockWidget.DockWidgetFloatable | QtWidgets.QDockWidget.DockWidgetMovable)
        self.dockWidget_3.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea | QtCore.Qt.RightDockWidgetArea)
        self.dockWidget_3.setObjectName("dockWidget_3")
        self.dock_contents = QtWidgets.QWidget()
        self.dock_contents.setObjectName("dock_contents")
        self.widget = QtWidgets.QWidget(self.dock_contents)
        self.widget.setGeometry(QtCore.QRect(30, 350, 281, 81))
        self.widget.setObjectName("widget")
        self.pos_info_form = QtWidgets.QFormLayout(self.widget)
        self.pos_info_form.setContentsMargins(0, 0, 0, 0)
        self.pos_info_form.setObjectName("pos_info_form")
        self.pos_info_label = QtWidgets.QLabel(self.widget)
        self.pos_info_label.setObjectName("pos_info_label")
        self.pos_info_form.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.pos_info_label)
        self.az_label = QtWidgets.QLabel(self.widget)
        self.az_label.setObjectName("az_label")
        self.pos_info_form.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.az_label)
        self.az_output_label = QtWidgets.QLabel(self.widget)
        self.az_output_label.setObjectName("az_output_label")
        self.pos_info_form.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.az_output_label)
        self.el_label = QtWidgets.QLabel(self.widget)
        self.el_label.setObjectName("el_label")
        self.pos_info_form.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.el_label)
        self.el_output_label = QtWidgets.QLabel(self.widget)
        self.el_output_label.setObjectName("el_output_label")
        self.pos_info_form.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.el_output_label)
        self.widget1 = QtWidgets.QWidget(self.dock_contents)
        self.widget1.setGeometry(QtCore.QRect(30, 500, 281, 161))
        self.widget1.setObjectName("widget1")
        self.bttns_vlayout = QtWidgets.QVBoxLayout(self.widget1)
        self.bttns_vlayout.setContentsMargins(0, 0, 0, 0)
        self.bttns_vlayout.setObjectName("bttns_vlayout")
        self.save_bttn = QtWidgets.QPushButton(self.widget1)
        self.save_bttn.setObjectName("save_bttn")
        self.bttns_vlayout.addWidget(self.save_bttn)
        self.save_as_bttn = QtWidgets.QPushButton(self.widget1)
        self.save_as_bttn.setObjectName("save_as_bttn")
        self.bttns_vlayout.addWidget(self.save_as_bttn)
        self.main_menu_bttn = QtWidgets.QPushButton(self.widget1)
        self.main_menu_bttn.setObjectName("main_menu_bttn")
        self.bttns_vlayout.addWidget(self.main_menu_bttn)
        self.widget2 = QtWidgets.QWidget(self.dock_contents)
        self.widget2.setGeometry(QtCore.QRect(30, 20, 281, 161))
        self.widget2.setObjectName("widget2")
        self.meas_info_form = QtWidgets.QFormLayout(self.widget2)
        self.meas_info_form.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.meas_info_form.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.meas_info_form.setContentsMargins(0, 0, 0, 0)
        self.meas_info_form.setObjectName("meas_info_form")
        self.meas_info_label = QtWidgets.QLabel(self.widget2)
        self.meas_info_label.setObjectName("meas_info_label")
        self.meas_info_form.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.meas_info_label)
        self.type_label = QtWidgets.QLabel(self.widget2)
        self.type_label.setObjectName("type_label")
        self.meas_info_form.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.type_label)
        self.antenna_label = QtWidgets.QLabel(self.widget2)
        self.antenna_label.setObjectName("antenna_label")
        self.meas_info_form.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.antenna_label)
        self.op_label = QtWidgets.QLabel(self.widget2)
        self.op_label.setObjectName("op_label")
        self.meas_info_form.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.op_label)
        self.date_label = QtWidgets.QLabel(self.widget2)
        self.date_label.setObjectName("date_label")
        self.meas_info_form.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.date_label)
        self.type_lineEdit = QtWidgets.QLineEdit(self.widget2)
        self.type_lineEdit.setObjectName("type_lineEdit")
        self.meas_info_form.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.type_lineEdit)
        self.antenna_lineEdit = QtWidgets.QLineEdit(self.widget2)
        self.antenna_lineEdit.setObjectName("antenna_lineEdit")
        self.meas_info_form.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.antenna_lineEdit)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget2)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.meas_info_form.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.dateEdit = QtWidgets.QDateEdit(self.widget2)
        self.dateEdit.setObjectName("dateEdit")
        self.meas_info_form.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.dateEdit)
        self.widget3 = QtWidgets.QWidget(self.dock_contents)
        self.widget3.setGeometry(QtCore.QRect(30, 230, 281, 81))
        self.widget3.setObjectName("widget3")
        self.freq_form = QtWidgets.QFormLayout(self.widget3)
        self.freq_form.setContentsMargins(0, 0, 0, 0)
        self.freq_form.setObjectName("freq_form")
        self.freq_cbox_label = QtWidgets.QLabel(self.widget3)
        self.freq_cbox_label.setObjectName("freq_cbox_label")
        self.freq_form.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.freq_cbox_label)
        self.freq_comboBox = QtWidgets.QComboBox(self.widget3)
        self.freq_comboBox.setObjectName("freq_comboBox")
        self.freq_form.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.freq_comboBox)
        self.freq_list_label = QtWidgets.QLabel(self.widget3)
        self.freq_list_label.setObjectName("freq_list_label")
        self.freq_form.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.freq_list_label)
        self.freq_list_lineEdit = QtWidgets.QLineEdit(self.widget3)
        self.freq_list_lineEdit.setObjectName("freq_list_lineEdit")
        self.freq_form.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.freq_list_lineEdit)
        self.dockWidget_3.setWidget(self.dock_contents)
        GraphWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget_3)

        self.retranslateUi(GraphWindow)
        QtCore.QMetaObject.connectSlotsByName(GraphWindow)

    def retranslateUi(self, GraphWindow):
        _translate = QtCore.QCoreApplication.translate
        GraphWindow.setWindowTitle(_translate("GraphWindow", "Graph Window"))
        self.pos_info_label.setText(_translate("GraphWindow", "Positioner Information"))
        self.az_label.setText(_translate("GraphWindow", "Azimuth:"))
        self.az_output_label.setText(_translate("GraphWindow", "TextLabel"))
        self.el_label.setText(_translate("GraphWindow", "Elevation: "))
        self.el_output_label.setText(_translate("GraphWindow", "TextLabel"))
        self.save_bttn.setText(_translate("GraphWindow", "Save "))
        self.save_as_bttn.setText(_translate("GraphWindow", "Save As "))
        self.main_menu_bttn.setText(_translate("GraphWindow", "Main Menu"))
        self.meas_info_label.setText(_translate("GraphWindow", "Measurment Information"))
        self.type_label.setText(_translate("GraphWindow", "Type:"))
        self.antenna_label.setText(_translate("GraphWindow", "Antenna:"))
        self.op_label.setText(_translate("GraphWindow", "Operator:"))
        self.date_label.setText(_translate("GraphWindow", "Date:"))
        self.freq_cbox_label.setText(_translate("GraphWindow", "Select Frequencies:"))
        self.freq_list_label.setText(_translate("GraphWindow", "Enter Frequencies:"))


from UIskeleton.graphwindowApp import MplWidget

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    GraphWindow = QtWidgets.QMainWindow()
    ui = Ui_GraphWindow()
    ui.setupUi(GraphWindow)
    GraphWindow.show()
    sys.exit(app.exec_())