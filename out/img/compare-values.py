
'''
@author: Kathleen Mullins

'''

# 3/30/15
## CHANGES
### -Added variation to CFA file
### -file outputs into CFA folder
### -some variation between images
## TODO
### -file should differ every time image is uploaded: second layer of variation
### -variation based on face detection/heaviness
### -variation based on region????
### -inspire by image

import sys, random
import cv2
import cv2.cv as cv
import numpy as np
import time, math, os
from colorweave import palette as cwp

# replace rules
# text detection
# find high saliency region and apply all things from there
#   randomly select region to use
# lines vs Zigzag
# feeling of image
#   heaviness
#   activeness: colors/shape
# change out rules 
# cutting up the CFA file

if len(sys.argv) == 2:
    file1 = sys.argv[1]
else:
    print "error! need an image to compare"

img1 = cv2.imread(file1)
img1 = cv2.resize(img1, (0,0), fx=0.5, fy=0.5) 

d = -1.0;
closestFile = "None"

for fn in os.listdir('.'):
     if os.path.isfile(fn) & fn.endswith(".png"):
        print "Comparing to " + fn
        img2 = cv2.imread(fn)
        img2 = cv2.resize(img2, (0,0), fx=0.5, fy=0.5)


        # Detect Circles 1
        tmpCir1 = img1;
        grayCir1 = cv2.cvtColor(tmpCir1, cv2.COLOR_BGR2GRAY)
        dst1 = cv2.GaussianBlur(grayCir1, (5,5), 0);
        dst1 = cv2.addWeighted(dst1, 1.5, grayCir1, -0.5, 0, dst1)

        circles1 = cv2.HoughCircles(dst1,cv.CV_HOUGH_GRADIENT,1,50,
                                    param1=50,param2=50,minRadius=10,maxRadius=0)

        if not circles1 is None and len(circles1) > 0:
            ncir1 = len(circles1[0]);
        else: 
            ncir1 = 0

        tmpCir2 = img2;
        grayCir2 = cv2.cvtColor(tmpCir2, cv2.COLOR_BGR2GRAY)
        dst2 = cv2.GaussianBlur(grayCir2, (5,5), 0);
        dst2 = cv2.addWeighted(dst2, 1.5, grayCir2, -0.5, 0, dst2)

        circles2 = cv2.HoughCircles(dst2,cv.CV_HOUGH_GRADIENT,1,50,
                                    param1=50,param2=50,minRadius=10,maxRadius=0)

        if not circles2 is None and len(circles2) > 0:
            ncir2 = len(circles2[0]);
        else: 
            ncir2 = 0
        # end detect circles
        # colors to meaning
         

        # edges variables
        gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
        gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
        # edges = cv2.Canny(gray,10,100)
        # lines = cv2.HoughLines(edges,1,np.pi/180,200)
        minLineLength = 200
        maxLineGap = 10
        lines1 = cv2.HoughLinesP(gray1,1,np.pi/180,100,minLineLength,maxLineGap)
        lines2 = cv2.HoughLinesP(gray2,1,np.pi/180,100,minLineLength,maxLineGap)


        # angles added up
        tot1 = 0 
        for x1,y1,x2,y2 in lines1[0]:
            dy = y2-y1
            dx = x2-x1
            mytan = math.atan2(dx, dy)
            tot1 = tot1+mytan

        # angle for images
        angle1 = math.floor(math.degrees(tot1/len(lines1[0])))
        nlines1 = len(lines1[0])

        tot2 = 0 
        for x1,y1,x2,y2 in lines2[0]:
            dy = y2-y1
            dx = x2-x1
            mytan = math.atan2(dx, dy)
            tot2 = tot2+mytan

        # angle for images
        angle2 = math.floor(math.degrees(tot2/len(lines2[0])))
        nlines2 = len(lines2[0])


        dAngle = abs(angle2-angle1)
        dLines = abs(nlines2-nlines1)
        dCircles = abs(ncir2-ncir1)
        dTotal = dAngle + dLines + dCircles
        if d == -1.0 or dTotal < d:
            d = dTotal 
            closestFile = fn;

print d
print closestFile




