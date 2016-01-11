#!/usr/bin/python

import sys
import os
import oct2py
import Image
import cv2
from hist_gui import Ui_Form
import numpy
import matplotlib.pyplot as plt
from PyQt4 import QtCore, QtGui

class MyForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.octave = oct2py.Oct2Py()
        self.octave.addpath('./scripts')

        self.ui.comboBox.addItem("Uniform")
        self.ui.comboBox.addItem("Adaptive")
        self.ui.comboBox.setCurrentIndex(0)

        self.ui.loadButton.clicked.connect(self.openFile)
        self.ui.showButton.clicked.connect(self.imShow)
        self.ui.eqButton.clicked.connect(self.equalize)
        self.ui.cmpButton.clicked.connect(self.compare)

    def openFile(self):

        self.path = str(QtGui.QFileDialog.getOpenFileName(self, 'Open file', os.path.curdir))
        filename = os.path.basename(self.path)
        self.ui.textEdit.setText(filename)
        self.image = Image.open(self.path)

    def imShow(self):
        self.image.show()

    def equalize(self):

        run = 1

        if self.ui.grayRadio.isChecked():
            working_image = self.image.convert("L")
        elif self.ui.colorRadio.isChecked():
            print "color"
        else:
            run = 0
            QtGui.QMessageBox.information(self,"Warning", "Please check one of available options.", QtGui.QMessageBox.Ok)

        if run == 1:
            self.img_cor = Image.fromarray(self.octave.histcor(working_image))
            self.img_cor.show()

    def compare(self):
        self.octave.present(self.image.convert("L"), self.img_cor.convert("L"))
        # plt.figure(1)
        # plt.subplot(2,1,1)
        # plt.imshow(self.image.convert("LA"))
        # plt.subplot(2,1,2)
        # plt.hist(numpy.array(self.image).flatten(), 256, range=(0.0,1.0), fc='k', ec='k')
        # # plt.subplot(2,1,2)
        # # plt.imshow(self.img_cor)
        # # plt.show()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
