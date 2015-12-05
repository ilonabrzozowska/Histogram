#!/usr/bin/python

import Image
import matplotlib.pyplot as plt
import sys
import os
import numpy as np
import oct2py
import Image
import cv2

def myread(file):
	img = cv2.imread(file)
	img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

	return img

def rgb2yuv(image):opencv
	return


if __name__ == "__main__":

	file = sys.argv[1]
	scriptPath = os.path.dirname(os.path.realpath(__file__))
	octave = oct2py.Oct2Py()
	octave.addpath(scriptPath)
	octave.pkg('load', 'image')
	
	img = myread(file)
	print img[3].shap4


	#img_cor = octave.histcor(img)
	if 0:
		plt.figure(1)
		plt.imshow(img)
		plt.show()
	




	
