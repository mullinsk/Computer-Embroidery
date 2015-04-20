import sys, random
import cv2
import cv2.cv as cv
import numpy as np
import time, math, os
from colorweave import palette as cwp

if len(sys.argv) == 3:
	openSVG = sys.argv[1]
	colors = sys.argv[2]

else:
	print "Error: Need an SVG file & List of Hex!"

with open (openSVG, "r") as myfile:
    svgFile=str(myfile.read())

with open (colors, "r") as myfile:
    colorFile=myfile.read()


newSVG = svgFile

c1 = colorFile[0:6]
c2 = colorFile[7:13]
c3 = colorFile[14:20]

newSVG = newSVG.replace("000000", c1)
newSVG = newSVG.replace('ff0400', c2)
newSVG = newSVG.replace('4000ff', c3)

base = os.path.splitext(os.path.basename(openSVG))[0]

with open ('final-'+base+".svg", "w") as myfile:
    myfile.write(newSVG)