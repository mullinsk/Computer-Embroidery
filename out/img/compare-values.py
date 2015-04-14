
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
import time, math
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


cfa0 = "startshape BIG rule BIG "
circularity = 0.5
cfa1 = "{VINE{r 45}} rule BIG "
circularityInverse = 0.5
cfa2 = "{SQ{}} rule BIG{ZAG{}} rule VINE { SEG{} VINE {x 9.1 r -15 y -1.2}}  rule VINE "
corner = 0.5
cfa3 = "{ SEG{} VINE {x 9.1 r 90 y -1.2}}  rule VINE "
# circularity repeat
cfa4 = "{VINE{f 0}} rule VINE "
# size of image?
cfa5 = "{} rule SEG{ LINE {} } rule SEG "
# floralness
cfa6 = "{ FLOWER { x 4.5 y -0.5 size 2.5 r 20 } } rule LINE "
#linearness
cfa7 = "{ 30 * { x 0.3 r -0.5} CIRCLE {}} rule LINE "
# linear2
cfa8 = "{ 20 * { x 0.3 r -0.5} CIRCLE { } }  rule LINE "
length = .05
cfa9 = "{ SQUARE {s 4 1 x 2}} rule FLOWER "
# circularityInverse
cfa10 = "{ SQUARE{s 1}} rule FLOWER "
cfa11 = "{ 5 * {r 72} TRIANGLE {s 1 x 1.2 hue 0 sat 1 b 0 a 1} FLOWER {r 20..30 size 0.5}} rule FLOWER {5 * {r 72} TRIANGLE {s 1 x 1.2 hue 0 sat 1 b 0 a -0.5} FLOWER {r 20..30 size 0.5}} rule FLOWER {5 * {r 72} TRIANGLE {s 1 x 1.2 hue 0 sat 1 b 0 a -0.25}FLOWER {r 20..30 size 0.5}} rule SQ "
cfa12 = "{4*{r 90 x 5} SQUIG{x 1..5 y 1..5}} rule SQ "
cfa13 = "{4*{y 10 r 90 x 10} SQUIG{x 1..5 y 1..5}} rule SQUIG "
cfa14 = "{5*{x 5..10 y 0..4 s 1.5} DOTS{}} rule SQUIG "
cfa15 = "{3*{x 5..10 y 0..4 s .9} DOTS{}} rule SQUIG "
linecut = 0.5
cfa15 = "{SQUARE{s 50 1}} rule DOTS "
# circularity Inverse
cfa16 = "{CIRCLE{s 2..4}} rule DOTS "
# circularity
cfa17 = "{SQUARE{s 2..5}} rule DOTS "
# floralness
cfa18 = "{FLOWER{}} rule ZAG "
#
cfa19 = "{3*{x 2} ZIG{r 45}} rule ZIG "

cfa20 = "{2*{r 135..150 x 2..4 y 2..4} DOTS{s .5}}"







if len(sys.argv) ==3:
    file1 = sys.argv[1]
    file2 = sys.argv[2]
else:
    print "error! need 2 images to compare"




img1 = cv2.imread(file1)
img1 = cv2.resize(img1, (0,0), fx=0.5, fy=0.5) 
img2 = cv2.imread(file2)
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


a = "Angles: " + str(dAngle)
l = "Lines: " + str(dLines)
c = "Circles: " + str(dCircles)
total = "Total: " + str(dAngle + dLines + dCircles)

with open("comparisons.txt", "a") as myfile:
    myfile.write("COMPARING: " + file1 + " & " + file2 + ": \n" + a +"\n" + l + "\n" + c + "\n" + total +"\n\n")




