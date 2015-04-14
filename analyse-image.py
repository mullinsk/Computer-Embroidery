
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
# 	randomly select region to use
# lines vs Zigzag
# feeling of image
#	heaviness
# 	activeness: colors/shape
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







if len(sys.argv) ==2:
	fileName = sys.argv[1]
else:
	fileName = r'scream.jpg'

print "fileName: ", fileName

img = cv2.imread(fileName)
img = cv2.resize(img, (0,0), fx=0.5, fy=0.5) 
sift = cv2.SIFT()


# Detect Circles
tmpCir = img;
grayCir = cv2.cvtColor(tmpCir, cv2.COLOR_BGR2GRAY)
dst = cv2.GaussianBlur(grayCir, (5,5), 0);
dst = cv2.addWeighted(dst, 1.5, grayCir, -0.5, 0, dst)


circles = cv2.HoughCircles(dst,cv.CV_HOUGH_GRADIENT,1,50,
                            param1=50,param2=50,minRadius=10,maxRadius=0)

if not circles is None and len(circles) > 0:
	# this draws circles if you need to visualize it
	# for i in circles[0,:]:
	# 	# draw the outer circle
	#     cv2.circle(tmpCir,(i[0],i[1]),i[2],(0,255,0),2)
	#     # draw the center of the circle
	#     cv2.circle(tmpCir,(i[0],i[1]),2,(0,0,255),3)
	ncir = len(circles[0]);
	circularity = 1.0/ncir;
	circularityInverse = 1-circularity;
else: 
	circularity = 0
	circularityInverse = .9
	ncir = 0
# end detect circles
# colors to meaning
decol = []
colors = cwp(path=fileName, n=3)
for c in colors:
	hexa = c[1:3]
	hexa2 = c[3:5]
	hexa3 = c[5:7]
	dec = int(hexa, 16)
	dec2 = int(hexa2, 16)
	dec3 = int(hexa3, 16)
	decs = [dec, dec2, dec3]
	decol.append(random.choice(decs))

 

# edges variables
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,10,100)
lines = cv2.HoughLines(edges,1,np.pi/180,200)
minLineLength = 200
maxLineGap = 10
lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength,maxLineGap)

# angles added up
tot = 0 
for x1,y1,x2,y2 in lines[0]:
    dy = y2-y1
    dx = x2-x1
    mytan = math.atan2(dx, dy)
    tot = tot+mytan

# angle for images
angle = math.floor(math.degrees(tot/len(lines[0])))
nlines = len(lines[0])




start = "startshape BIG "
rule1 = "rule BIG {VINE{r 90}}"
# if > 30 lines, multiple lines at av angle
if len(lines[0])>30:
	rule1 = "rule BIG {"+ str(math.floor(nlines/4)) +"*{r "+ str(angle) +"} VINE{r 90}} rule BIG .05 {VINE{r 90}}"

rule2 = "rule VINE { SEG{} VINE {x 9.1 y -1.2 r "+str((90-angle)*1.5)+"}} rule VINE { SEG{} VINE {x 9.1 y -1.2 r "+str((90-angle)*1.5)+"}}"
# r is 90 - average angle

rule3 = "rule VINE {VINE{f 0}} "
# if > 50 circles: 1/c + .05 prob 
if ncir > 50:
	rule3 = "rule VINE "+str(1.0/ncir+.05)+" {VINE{f 0}} "

rule4 = "rule VINE .1 {} "

rule5 = "rule SEG {LINE {} } rule SEG {LINE {hue 255 sat 1 b 1} } rule SEG {LINE {hue 1 sat 1 b 1} }"
	# add rule5a if #/lines is < 20
if nlines < 20:
	rule5 = rule5+" rule SEG {LINE {x "+str(nlines*1.5)+" y "+str(nlines+3)+" } } rule SEG {LINE {x "+str(nlines*1.5)+" y "+str(nlines+3)+" hue 255 sat 1 b 1} } rule SEG {LINE {x "+str(nlines*1.5)+" y "+str(nlines+3)+" hue 1 sat 1 b 1} }"
	# - x / y = #/lines

rule6 = "rule SEG { FLOWER { x 5 y 1 s .5} } rule SEG { FLOWER { x 5 y 1 s .5 hue 1 sat 1 b 1} } rule SEG { FLOWER { x 5 y 1 s .5 hue 255 sat 1 b 1} }"
	# remove if #/cir < 10 & #/line > 40
if ncir < 10 & nlines > 40:
	rule6 = " "

rule7= "rule LINE { "+str(math.floor(nlines/2))+" * { x 0.3 r -.5} CIRCLE {}}"
	# repeats = # lines???
	# replace w/ rule7a when rule2a is used 
if ncir>60:
	rule7 = "rule LINE { 5 * { x 2 r -5} CIRCLE { } }"
if 90>angle>120:
	rule2 = "rule VINE { SEG{} VINE {x 5 y -1.2 r -5}}  "
	rule7 = "rule LINE{ 2*{r 90 x 2.3 y -1} SQUARE{s 4 1 r 120}}"
	# replace w/ rule 7b if circles > 75


rule8 = "rule FLOWER {CIRCLE{s 5}}"
	# replace with rule 8a if color >100
if dec > 100:
	rule8 =  "rule FLOWER {SQUARE{s 7 y -5 r 120}}"
	# replace with rule 8b if color >200
if dec > 200: 
	rule8 = "rule FLOWER {10 * {r 36 } CIRCLE{s 2 4 y -1}}"
	# replace with rule 8c if color = 0 
if 0<dec<90:
	rule8 = "rule FLOWER {}"
	# rule 8a + rule 8b if color2 > 150


colors = " //"+str(colors)








final = start+rule1+rule2+rule3+rule4+rule5+rule6+rule7+rule8+colors

with open('out/cfa/'+fileName+'.cfdg', 'w') as outfile: 
	outfile.write(final)


