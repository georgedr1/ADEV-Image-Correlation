# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 19:15:29 2016

This script will be used for our "Identical Webcam" test.

The purpose of this will be to determine if our webcams are acceptably identical or not.
If they are different, we will need to know the differences that make them distinct.

@author: mcdanitd
"""

import cv2
import numpy as np
#import antigravity

vc1 = cv2.VideoCapture(1)
vc2 = cv2.VideoCapture(2)

if vc1.isOpened(): # try to get the first frame
    rval1, frame1 = vc1.read()
else:
    rval1 = False

if vc2.isOpened(): # try to get the first frame
    rval2, frame2 = vc2.read()
else:
    rval2 = False

if rval1 == False:
    sys.exit("Camera 1 did not open correctly.")
if rval2 == False:
    sys.exit("Camera 2 did not open correctly.")

cam1 = 0    # 
for i in range(0,5):    #collect data from first camera
    rval1, frame1 = vc1.read()
    cam1 = cam1 + frame1

print("Program paused. Move second camera into place.")
raw_input()

cam2 = 0
for j in range(0,5):    #collect data from second camera
    rval2, frame2 = vc2.read()
    cam2 = cam2 + frame2

avgCam1 = cam1/i
avgCam2 = cam2/j

difference = avgCam1 - avgCam2    #difference between the two cameras
percentDiff = diff/frame1
  