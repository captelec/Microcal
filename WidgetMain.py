# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WidgetMain.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(712, 570)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.group_graph = QtWidgets.QGroupBox(Form)
        self.group_graph.setObjectName("group_graph")
        self.layout_graph = QtWidgets.QVBoxLayout(self.group_graph)
        self.layout_graph.setObjectName("layout_graph")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_clear = QtWidgets.QPushButton(self.group_graph)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_clear.sizePolicy().hasHeightForWidth())
        self.btn_clear.setSizePolicy(sizePolicy)
        self.btn_clear.setObjectName("btn_clear")
        self.horizontalLayout.addWidget(self.btn_clear)
        self.check_autox = QtWidgets.QCheckBox(self.group_graph)
        self.check_autox.setChecked(True)
        self.check_autox.setObjectName("check_autox")
        self.horizontalLayout.addWidget(self.check_autox)
        self.check_autoy = QtWidgets.QCheckBox(self.group_graph)
        self.check_autoy.setChecked(True)
        self.check_autoy.setObjectName("check_autoy")
        self.horizontalLayout.addWidget(self.check_autoy)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.layout_graph.addLayout(self.horizontalLayout)
        self.gridLayout.addWidget(self.group_graph, 0, 0, 11, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.group_pump = QtWidgets.QGroupBox(Form)
        self.group_pump.setObjectName("group_pump")
        self.verticalLayout_2.addWidget(self.group_pump)
        self.group_nvolt = QtWidgets.QGroupBox(Form)
        self.group_nvolt.setObjectName("group_nvolt")
        self.group_pump.raise_()
        self.verticalLayout_2.addWidget(self.group_nvolt)
        self.group_cSource = QtWidgets.QGroupBox(Form)
        self.group_cSource.setObjectName("group_cSource")
        self.verticalLayout_2.addWidget(self.group_cSource)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.groupBox = QtWidgets.QGroupBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.formLayout_2 = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.spin_interval = QtWidgets.QSpinBox(self.groupBox)
        self.spin_interval.setMinimum(500)
        self.spin_interval.setMaximum(10000)
        self.spin_interval.setSingleStep(100)
        self.spin_interval.setProperty("value", 1000)
        self.spin_interval.setObjectName("spin_interval")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.spin_interval)
        self.line = QtWidgets.QFrame(self.groupBox)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.line)
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setObjectName("label_12")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.edit_path = QtWidgets.QLineEdit(self.groupBox)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.edit_path.setPalette(palette)
        self.edit_path.setReadOnly(True)
        self.edit_path.setClearButtonEnabled(False)
        self.edit_path.setObjectName("edit_path")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.edit_path)
        self.btn_record = QtWidgets.QPushButton(self.groupBox)
        self.btn_record.setObjectName("btn_record")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.btn_record)
        self.line_2 = QtWidgets.QFrame(self.groupBox)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.SpanningRole, self.line_2)
        self.ico_state = QtWidgets.QLabel(self.groupBox)
        self.ico_state.setMinimumSize(QtCore.QSize(32, 32))
        self.ico_state.setObjectName("ico_state")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.ico_state)
        self.lbl_state = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.lbl_state.setFont(font)
        self.lbl_state.setObjectName("lbl_state")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lbl_state)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_Aquire = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_Aquire.sizePolicy().hasHeightForWidth())
        self.btn_Aquire.setSizePolicy(sizePolicy)
        self.btn_Aquire.setObjectName("btn_Aquire")
        self.horizontalLayout_2.addWidget(self.btn_Aquire)
        self.checkBox_Calib = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_Calib.setObjectName("checkBox_Calib")
        self.horizontalLayout_2.addWidget(self.checkBox_Calib)
        self.formLayout_2.setLayout(6, QtWidgets.QFormLayout.SpanningRole, self.horizontalLayout_2)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 3, 11, 1)
        self.gridLayout.setColumnStretch(0, 3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Microcal"))
        self.group_graph.setTitle(_translate("Form", "Chart"))
        self.btn_clear.setText(_translate("Form", "Clear chart"))
        self.check_autox.setText(_translate("Form", "Autoscale X"))
        self.check_autoy.setText(_translate("Form", "Autoscale Y"))
        self.group_pump.setTitle(_translate("Form", "Syringe pump"))
        self.group_nvolt.setTitle(_translate("Form", "nVoltmeter"))
        self.group_cSource.setTitle(_translate("Form", "Current Source"))
        self.groupBox.setTitle(_translate("Form", "Acquisition"))
        self.label.setText(_translate("Form", "Interval"))
        self.spin_interval.setSuffix(_translate("Form", " ms"))
        self.label_12.setText(_translate("Form", "Path"))
        self.edit_path.setPlaceholderText(_translate("Form", "File path"))
        self.btn_record.setText(_translate("Form", "Save"))
        self.lbl_state.setText(_translate("Form", "Not recording"))
        self.btn_Aquire.setText(_translate("Form", "Start Acquisition"))
        self.checkBox_Calib.setText(_translate("Form", "Calib"))

