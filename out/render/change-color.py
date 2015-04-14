import sys, random
import cv2
import cv2.cv as cv
import numpy as np
import time, math
from colorweave import palette as cwp

if len(sys.argv) == 5:
	fileName = sys.argv[1]
	c1 = sys.argv[2]
	c2 = sys.argv[3]
	c3 = sys.argv[4]
else:
	print "Error: Need an SVG file & List of Hex!"

with open (fileName, "r") as myfile:
    svgFile=str(myfile.read())



newSVG = svgFile

newSVG = newSVG.replace("000000", c1)
newSVG = newSVG.replace('ff0400', c2)
newSVG = newSVG.replace('4000ff', c3)


with open ('final-'+fileName, "w") as myfile:
    myfile.write(newSVG)