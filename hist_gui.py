# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hist.ui'
#
# Created: Tue Jan 12 01:53:53 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(388, 280)
        self.loadButton = QtGui.QPushButton(Form)
        self.loadButton.setGeometry(QtCore.QRect(20, 50, 171, 31))
        self.loadButton.setObjectName(_fromUtf8("loadButton"))
        self.textEdit = QtGui.QTextEdit(Form)
        self.textEdit.setEnabled(False)
        self.textEdit.setGeometry(QtCore.QRect(20, 10, 171, 31))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(20, 140, 111, 101))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.grayRadio = QtGui.QRadioButton(self.groupBox)
        self.grayRadio.setGeometry(QtCore.QRect(0, 30, 116, 22))
        self.grayRadio.setObjectName(_fromUtf8("grayRadio"))
        self.colorRadio = QtGui.QRadioButton(self.groupBox)
        self.colorRadio.setGeometry(QtCore.QRect(0, 60, 121, 22))
        self.colorRadio.setObjectName(_fromUtf8("colorRadio"))
        self.comboBox = QtGui.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(160, 150, 101, 27))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.eqButton = QtGui.QPushButton(Form)
        self.eqButton.setGeometry(QtCore.QRect(280, 150, 101, 27))
        self.eqButton.setObjectName(_fromUtf8("eqButton"))
        self.showButton = QtGui.QPushButton(Form)
        self.showButton.setGeometry(QtCore.QRect(250, 10, 131, 71))
        self.showButton.setObjectName(_fromUtf8("showButton"))
        self.cmpButton = QtGui.QPushButton(Form)
        self.cmpButton.setGeometry(QtCore.QRect(160, 190, 221, 27))
        self.cmpButton.setObjectName(_fromUtf8("cmpButton"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 260, 371, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.saveImg = QtGui.QPushButton(Form)
        self.saveImg.setGeometry(QtCore.QRect(160, 230, 91, 27))
        self.saveImg.setObjectName(_fromUtf8("saveImg"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Histogram equalizer", None))
        self.loadButton.setText(_translate("Form", "Load Image", None))
        self.groupBox.setTitle(_translate("Form", "Image type", None))
        self.grayRadio.setText(_translate("Form", "Grayscale", None))
        self.colorRadio.setText(_translate("Form", "Color", None))
        self.eqButton.setText(_translate("Form", "Equalize", None))
        self.showButton.setText(_translate("Form", "Show", None))
        self.cmpButton.setText(_translate("Form", "Compare with origin", None))
        self.label.setText(_translate("Form", "Histogram equalizer", None))
        self.saveImg.setText(_translate("Form", "Save", None))

