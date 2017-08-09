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
        WidgetPID.resize(598, 396)
        self.gridLayout = QtWidgets.QGridLayout(WidgetPID)
        self.gridLayout.setObjectName("gridLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.spin_td = QtWidgets.QDoubleSpinBox(WidgetPID)
        self.spin_td.setDecimals(2)
        self.spin_td.setMinimum(-1000.0)
        self.spin_td.setMaximum(1000.0)
        self.spin_td.setProperty("value", 1.0)
        self.spin_td.setObjectName("spin_td")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.spin_td)
        self.spin_ti = QtWidgets.QDoubleSpinBox(WidgetPID)
        self.spin_ti.setDecimals(2)
        self.spin_ti.setMinimum(-1000.0)
        self.spin_ti.setMaximum(1000.0)
        self.spin_ti.setProperty("value", 5.0)
        self.spin_ti.setObjectName("spin_ti")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.spin_ti)
        self.spin_max = QtWidgets.QDoubleSpinBox(WidgetPID)
        self.spin_max.setDecimals(1)
        self.spin_max.setMinimum(0.1)
        self.spin_max.setMaximum(99.9)
        self.spin_max.setProperty("value", 66.7)
        self.spin_max.setObjectName("spin_max")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.spin_max)
        self._label_3 = QtWidgets.QLabel(WidgetPID)
        self._label_3.setObjectName("_label_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self._label_3)
        self._label_4 = QtWidgets.QLabel(WidgetPID)
        self._label_4.setObjectName("_label_4")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self._label_4)
        self._label_5 = QtWidgets.QLabel(WidgetPID)
        self._label_5.setObjectName("_label_5")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self._label_5)
        self.spin_kc = QtWidgets.QDoubleSpinBox(WidgetPID)
        self.spin_kc.setDecimals(2)
        self.spin_kc.setMinimum(-1000.0)
        self.spin_kc.setMaximum(1000.0)
        self.spin_kc.setProperty("value", 20.0)
        self.spin_kc.setObjectName("spin_kc")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.spin_kc)
        self.spin_setpoint = QtWidgets.QDoubleSpinBox(WidgetPID)
        self.spin_setpoint.setMaximum(100.0)
        self.spin_setpoint.setProperty("value", 25.0)
        self.spin_setpoint.setObjectName("spin_setpoint")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.spin_setpoint)
        self._label_1 = QtWidgets.QLabel(WidgetPID)
        self._label_1.setObjectName("_label_1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self._label_1)
        self._label_2 = QtWidgets.QLabel(WidgetPID)
        self._label_2.setObjectName("_label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self._label_2)
        self._line_2 = QtWidgets.QFrame(WidgetPID)
        self._line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self._line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self._line_2.setObjectName("_line_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self._line_2)
        self.gridLayout.addLayout(self.formLayout, 0, 2, 1, 1)
        self.frame = QtWidgets.QFrame(WidgetPID)
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(2)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.ico_status = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ico_status.sizePolicy().hasHeightForWidth())
        self.ico_status.setSizePolicy(sizePolicy)
        self.ico_status.setMinimumSize(QtCore.QSize(32, 32))
        self.ico_status.setObjectName("ico_status")
        self.horizontalLayout_2.addWidget(self.ico_status)
        self.label_status = QtWidgets.QLabel(self.frame)
        self.label_status.setMinimumSize(QtCore.QSize(37, 0))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_status.setFont(font)
        self.label_status.setObjectName("label_status")
        self.horizontalLayout_2.addWidget(self.label_status)
        self.gridLayout.addWidget(self.frame, 3, 2, 1, 1)
        self._line_1 = QtWidgets.QFrame(WidgetPID)
        self._line_1.setFrameShape(QtWidgets.QFrame.VLine)
        self._line_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self._line_1.setObjectName("_line_1")
        self.gridLayout.addWidget(self._line_1, 0, 1, 5, 1)
        self.layout_graph = QtWidgets.QVBoxLayout()
        self.layout_graph.setObjectName("layout_graph")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_clear = QtWidgets.QPushButton(WidgetPID)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_clear.sizePolicy().hasHeightForWidth())
        self.btn_clear.setSizePolicy(sizePolicy)
        self.btn_clear.setObjectName("btn_clear")
        self.horizontalLayout.addWidget(self.btn_clear)
        self.check_autox = QtWidgets.QCheckBox(WidgetPID)
        self.check_autox.setChecked(True)
        self.check_autox.setObjectName("check_autox")
        self.horizontalLayout.addWidget(self.check_autox)
        self.check_autoy = QtWidgets.QCheckBox(WidgetPID)
        self.check_autoy.setChecked(True)
        self.check_autoy.setObjectName("check_autoy")
        self.horizontalLayout.addWidget(self.check_autoy)
        self.layout_graph.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.layout_graph, 0, 0, 5, 1)
        self.btn_start = QtWidgets.QPushButton(WidgetPID)
        self.btn_start.setObjectName("btn_start")
        self.gridLayout.addWidget(self.btn_start, 4, 2, 1, 1)
        self._line_3 = QtWidgets.QFrame(WidgetPID)
        self._line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self._line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self._line_3.setObjectName("_line_3")
        self.gridLayout.addWidget(self._line_3, 1, 2, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(WidgetPID)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.tableWidget, 2, 2, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)

        self.retranslateUi(WidgetPID)
        QtCore.QMetaObject.connectSlotsByName(WidgetPID)

    def retranslateUi(self, WidgetPID):
        _translate = QtCore.QCoreApplication.translate
        WidgetPID.setWindowTitle(_translate("WidgetPID", "Form"))
        self.spin_td.setSuffix(_translate("WidgetPID", " s"))
        self.spin_ti.setSuffix(_translate("WidgetPID", " s"))
        self.spin_max.setSuffix(_translate("WidgetPID", " %"))
        self._label_3.setText(_translate("WidgetPID", "Ti"))
        self._label_4.setText(_translate("WidgetPID", "Td"))
        self._label_5.setText(_translate("WidgetPID", "Maximum"))
        self.spin_setpoint.setSuffix(_translate("WidgetPID", " °C"))
        self._label_1.setText(_translate("WidgetPID", "Setpoint"))
        self._label_2.setText(_translate("WidgetPID", "Kc"))
        self.label_status.setText(_translate("WidgetPID", "Off"))
        self.btn_clear.setText(_translate("WidgetPID", "Clear chart"))
        self.check_autox.setText(_translate("WidgetPID", "Autoscale X"))
        self.check_autoy.setText(_translate("WidgetPID", "Autoscale Y"))
        self.btn_start.setText(_translate("WidgetPID", "Start"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("WidgetPID", "Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("WidgetPID", "Value"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WidgetPID = QtWidgets.QWidget()
    ui = Ui_WidgetPID()
    ui.setupUi(WidgetPID)
    WidgetPID.show()
    sys.exit(app.exec_())

