# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WidgetPump.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WidgetPump(object):
    def setupUi(self, WidgetPump):
        WidgetPump.setObjectName("WidgetPump")
        WidgetPump.resize(352, 452)
        self.gridLayout = QtWidgets.QGridLayout(WidgetPump)
        self.gridLayout.setObjectName("gridLayout")
        self.label_port = QtWidgets.QLabel(WidgetPump)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_port.setPalette(palette)
        self.label_port.setObjectName("label_port")
        self.gridLayout.addWidget(self.label_port, 11, 0, 1, 1)
        self.spin_rate = QtWidgets.QDoubleSpinBox(WidgetPump)
        self.spin_rate.setDecimals(4)
        self.spin_rate.setMaximum(1999.0)
        self.spin_rate.setObjectName("spin_rate")
        self.gridLayout.addWidget(self.spin_rate, 4, 2, 1, 1)
        self.list_baud = QtWidgets.QListWidget(WidgetPump)
        self.list_baud.setObjectName("list_baud")
        item = QtWidgets.QListWidgetItem()
        self.list_baud.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_baud.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_baud.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_baud.addItem(item)
        self.gridLayout.addWidget(self.list_baud, 1, 1, 10, 1)
        self.combo_units = QtWidgets.QComboBox(WidgetPump)
        self.combo_units.setObjectName("combo_units")
        self.combo_units.addItem("")
        self.combo_units.addItem("")
        self.combo_units.addItem("")
        self.combo_units.addItem("")
        self.gridLayout.addWidget(self.combo_units, 4, 3, 1, 1)
        self._label_2 = QtWidgets.QLabel(WidgetPump)
        self._label_2.setObjectName("_label_2")
        self.gridLayout.addWidget(self._label_2, 0, 1, 1, 1)
        self._label_1 = QtWidgets.QLabel(WidgetPump)
        self._label_1.setObjectName("_label_1")
        self.gridLayout.addWidget(self._label_1, 0, 0, 1, 1)
        self.list_port = QtWidgets.QListWidget(WidgetPump)
        self.list_port.setObjectName("list_port")
        self.gridLayout.addWidget(self.list_port, 1, 0, 10, 1)
        self.label_baud = QtWidgets.QLabel(WidgetPump)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_baud.setPalette(palette)
        self.label_baud.setObjectName("label_baud")
        self.gridLayout.addWidget(self.label_baud, 11, 1, 1, 1)
        self._label_3 = QtWidgets.QLabel(WidgetPump)
        self._label_3.setMinimumSize(QtCore.QSize(97, 13))
        self._label_3.setObjectName("_label_3")
        self.gridLayout.addWidget(self._label_3, 3, 2, 1, 2)
        self._label_5 = QtWidgets.QLabel(WidgetPump)
        self._label_5.setMinimumSize(QtCore.QSize(97, 13))
        self._label_5.setObjectName("_label_5")
        self.gridLayout.addWidget(self._label_5, 6, 2, 1, 2)
        self.btn_send = QtWidgets.QPushButton(WidgetPump)
        self.btn_send.setEnabled(False)
        self.btn_send.setMinimumSize(QtCore.QSize(97, 23))
        self.btn_send.setObjectName("btn_send")
        self.gridLayout.addWidget(self.btn_send, 1, 2, 1, 2)
        self.btn_get = QtWidgets.QPushButton(WidgetPump)
        self.btn_get.setEnabled(False)
        self.btn_get.setMinimumSize(QtCore.QSize(97, 23))
        self.btn_get.setObjectName("btn_get")
        self.gridLayout.addWidget(self.btn_get, 2, 2, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 10, 2, 1, 2)
        self.label_6 = QtWidgets.QLabel(WidgetPump)
        self.label_6.setMinimumSize(QtCore.QSize(97, 13))
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 8, 2, 1, 2)
        self.spin_diameter = QtWidgets.QDoubleSpinBox(WidgetPump)
        self.spin_diameter.setMinimumSize(QtCore.QSize(97, 20))
        self.spin_diameter.setDecimals(4)
        self.spin_diameter.setMaximum(1999.0)
        self.spin_diameter.setObjectName("spin_diameter")
        self.gridLayout.addWidget(self.spin_diameter, 7, 2, 1, 2)
        self.btn_conn = QtWidgets.QPushButton(WidgetPump)
        self.btn_conn.setEnabled(False)
        self.btn_conn.setObjectName("btn_conn")
        self.gridLayout.addWidget(self.btn_conn, 11, 2, 1, 2)
        self.spin_target = QtWidgets.QDoubleSpinBox(WidgetPump)
        self.spin_target.setMinimumSize(QtCore.QSize(97, 20))
        self.spin_target.setDecimals(4)
        self.spin_target.setMaximum(1999.0)
        self.spin_target.setObjectName("spin_target")
        self.gridLayout.addWidget(self.spin_target, 9, 2, 1, 2)
        self._label_2.setBuddy(self.list_baud)
        self._label_1.setBuddy(self.list_port)
        self._label_3.setBuddy(self.spin_rate)
        self._label_5.setBuddy(self.spin_diameter)
        self.label_6.setBuddy(self.spin_target)

        self.retranslateUi(WidgetPump)
        QtCore.QMetaObject.connectSlotsByName(WidgetPump)
        WidgetPump.setTabOrder(self.list_port, self.list_baud)
        WidgetPump.setTabOrder(self.list_baud, self.btn_send)
        WidgetPump.setTabOrder(self.btn_send, self.btn_get)
        WidgetPump.setTabOrder(self.btn_get, self.spin_rate)
        WidgetPump.setTabOrder(self.spin_rate, self.combo_units)
        WidgetPump.setTabOrder(self.combo_units, self.spin_diameter)
        WidgetPump.setTabOrder(self.spin_diameter, self.spin_target)
        WidgetPump.setTabOrder(self.spin_target, self.btn_conn)

    def retranslateUi(self, WidgetPump):
        _translate = QtCore.QCoreApplication.translate
        __sortingEnabled = self.list_baud.isSortingEnabled()
        self.list_baud.setSortingEnabled(False)
        item = self.list_baud.item(0)
        item.setText(_translate("WidgetPump", "1200"))
        item = self.list_baud.item(1)
        item.setText(_translate("WidgetPump", "2400"))
        item = self.list_baud.item(2)
        item.setText(_translate("WidgetPump", "9600"))
        item = self.list_baud.item(3)
        item.setText(_translate("WidgetPump", "19200"))
        self.list_baud.setSortingEnabled(__sortingEnabled)
        self.combo_units.setItemText(0, _translate("WidgetPump", "ml/min"))
        self.combo_units.setItemText(1, _translate("WidgetPump", "µl/min"))
        self.combo_units.setItemText(2, _translate("WidgetPump", "ml/hr"))
        self.combo_units.setItemText(3, _translate("WidgetPump", "µl/hr"))
        self._label_2.setText(_translate("WidgetPump", "Baudrate"))
        self._label_1.setText(_translate("WidgetPump", "Port"))
        self._label_3.setText(_translate("WidgetPump", "Infuse rate"))
        self._label_5.setText(_translate("WidgetPump", "Diameter"))
        self.btn_send.setText(_translate("WidgetPump", "Send config"))
        self.btn_get.setText(_translate("WidgetPump", "Get config"))
        self.label_6.setText(_translate("WidgetPump", "Target infusion"))
        self.spin_diameter.setSuffix(_translate("WidgetPump", " mm"))
        self.btn_conn.setText(_translate("WidgetPump", "Connect"))
        self.spin_target.setSuffix(_translate("WidgetPump", " ml"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WidgetPump = QtWidgets.QWidget()
    ui = Ui_WidgetPump()
    ui.setupUi(WidgetPump)
    WidgetPump.show()
    sys.exit(app.exec_())

