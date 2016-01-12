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


if __name__ == "__main__":

	file = sys.argv[1]
	scriptPath = os.path.dirname(os.path.realpath(__file__))
	octave = oct2py.Oct2Py()
	octave.addpath(scriptPath)
	octave = oct2py.Oct2Py()
	
	img = cv2.imread(file,cv2.CV_LOAD_IMAGE_GRAYSCALE)
	image = Image.open(file).convert("L")


	#And here is the magic#
	img_cor = octave.histcor(image)

	im = Image.fromarray(img_cor)
	plt.figure(1)
	plt.subplot(2,1,1)
	plt.imshow(image.convert("LA"))
	plt.subplot(2,1,2)
	plt.imshow(im)
	plt.show()
	




	
