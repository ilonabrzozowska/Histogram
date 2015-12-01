#!/usr/bin/python

import Image
import matplotlib.pyplot as plt
import sys
import numpy as np



if __name__ == "__main__":

	file = sys.argv[1]
	img = Image.open(file)
	gray = img.convert('LA')
	flat = np.array(gray)

	plt.figure(1)
    	plt.subplot(2, 1, 1)
	plt.imshow(gray)
	plt.subplot(2, 1, 2)
	plt.hist(flat)
	plt.show()
