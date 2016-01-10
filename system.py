#!/usr/bin/python

import Image
import matplotlib.pyplot as plt
import sys
import os
import numpy as np
import oct2py
import Image
import cv2
from hist_gui import Ui_Form
from PyQt4 import QtCore, QtGui

class MyForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())