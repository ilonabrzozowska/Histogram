#!/usr/bin/python

import Image
import matplotlib.pyplot as plt
import sys



if __name__ == "__main__":

	file = sys.argv[1]
	img = Image.open(file)

	imgplot = plt.imshow(img)
	plt.show()
