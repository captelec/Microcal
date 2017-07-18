# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WidgetPID.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WidgetPID(object):
    def setupUi(self, WidgetPID):
        WidgetPID.setObjectName("WidgetPID")
        WidgetPID.resize(352, 372)
        self.gridLayout = QtWidgets.QGridLayout(WidgetPID)
        self.gridLayout.setObjectName("gridLayout")
        self.spin_ti = QtWidgets.QDoubleSpinBox(WidgetPID)
        self.spin_ti.setDecimals(5)
        self.spin_ti.setMinimum(-100.0)
        self.spin_ti.setMaximum(100.0)
        self.spin_ti.setObjectName("spin_ti")
        self.gridLayout.addWidget(self.spin_ti, 11, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 14, 1, 1, 1)
        self._label_3 = QtWidgets.QLabel(WidgetPID)
        self._label_3.setObjectName("_label_3")
        self.gridLayout.addWidget(self._label_3, 10, 1, 1, 1)
        self._label_1 = QtWidgets.QLabel(WidgetPID)
        self._label_1.setObjectName("_label_1")
        self.gridLayout.addWidget(self._label_1, 3, 1, 1, 1)
        self.btn_start = QtWidgets.QPushButton(WidgetPID)
        self.btn_start.setObjectName("btn_start")
        self.gridLayout.addWidget(self.btn_start, 16, 1, 1, 1)
        self._line = QtWidgets.QFrame(WidgetPID)
        self._line.setFrameShape(QtWidgets.QFrame.HLine)
        self._line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self._line.setObjectName("_line")
        self.gridLayout.addWidget(self._line, 7, 1, 1, 1)
        self._label_4 = QtWidgets.QLabel(WidgetPID)
        self._label_4.setObjectName("_label_4")
        self.gridLayout.addWidget(self._label_4, 12, 1, 1, 1)
        self.spin_td = QtWidgets.QDoubleSpinBox(WidgetPID)
        self.spin_td.setDecimals(5)
        self.spin_td.setMinimum(-100.0)
        self.spin_td.setMaximum(100.0)
        self.spin_td.setObjectName("spin_td")
        self.gridLayout.addWidget(self.spin_td, 13, 1, 1, 1)
        self.label_status = QtWidgets.QLabel(WidgetPID)
        self.label_status.setObjectName("label_status")
        self.gridLayout.addWidget(self.label_status, 15, 1, 1, 1)
        self.spin_setpoint = QtWidgets.QDoubleSpinBox(WidgetPID)
        self.spin_setpoint.setMaximum(100.0)
        self.spin_setpoint.setProperty("value", 25.0)
        self.spin_setpoint.setObjectName("spin_setpoint")
        self.gridLayout.addWidget(self.spin_setpoint, 5, 1, 1, 1)
        self._label_2 = QtWidgets.QLabel(WidgetPID)
        self._label_2.setObjectName("_label_2")
        self.gridLayout.addWidget(self._label_2, 8, 1, 1, 1)
        self.spin_kc = QtWidgets.QDoubleSpinBox(WidgetPID)
        self.spin_kc.setDecimals(5)
        self.spin_kc.setMinimum(-100.0)
        self.spin_kc.setMaximum(100.0)
        self.spin_kc.setProperty("value", 1.0)
        self.spin_kc.setObjectName("spin_kc")
        self.gridLayout.addWidget(self.spin_kc, 9, 1, 1, 1)
        self.wid_graph = QtWidgets.QWidget(WidgetPID)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wid_graph.sizePolicy().hasHeightForWidth())
        self.wid_graph.setSizePolicy(sizePolicy)
        self.wid_graph.setObjectName("wid_graph")
        self.gridLayout.addWidget(self.wid_graph, 3, 0, 15, 1)
        self.btn_clear = QtWidgets.QPushButton(WidgetPID)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_clear.sizePolicy().hasHeightForWidth())
        self.btn_clear.setSizePolicy(sizePolicy)
        self.btn_clear.setObjectName("btn_clear")
        self.gridLayout.addWidget(self.btn_clear, 19, 0, 1, 1)

        self.retranslateUi(WidgetPID)
        QtCore.QMetaObject.connectSlotsByName(WidgetPID)

    def retranslateUi(self, WidgetPID):
        _translate = QtCore.QCoreApplication.translate
        WidgetPID.setWindowTitle(_translate("WidgetPID", "Form"))
        self._label_3.setText(_translate("WidgetPID", "Ti"))
        self._label_1.setText(_translate("WidgetPID", "Setpoint"))
        self.btn_start.setText(_translate("WidgetPID", "Start"))
        self._label_4.setText(_translate("WidgetPID", "Td"))
        self.label_status.setText(_translate("WidgetPID", "Off"))
        self.spin_setpoint.setSuffix(_translate("WidgetPID", " °C"))
        self._label_2.setText(_translate("WidgetPID", "Kc"))
        self.btn_clear.setText(_translate("WidgetPID", "Clear chart"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WidgetPID = QtWidgets.QWidget()
    ui = Ui_WidgetPID()
    ui.setupUi(WidgetPID)
    WidgetPID.show()
    sys.exit(app.exec_())

