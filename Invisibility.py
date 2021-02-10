import cv2 as cv
import numpy as np
import time

cap = cv.VideoCapture(0)
time.sleep(3)
background=0

for i in range(30):
    ret,background = cap.read()

background = np.flip(background,axis=1)

while(cap.isOpened()):
    ret, img = cap.read()
 
    img = np.flip(img, axis = 1)

    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    blurred = cv.GaussianBlur(hsv, (35, 35), 0)

    lower = np.array([0,120,70])
    upper = np.array([10,255,255])
    mask1 = cv.inRange(hsv, lower, upper)

    lower_red = np.array([150,120,90])
    upper_red = np.array([300,400,400])
    mask2 = cv.inRange(hsv, lower_red, upper_red)

    mask = mask1 + mask2
    mask = cv.morphologyEx(mask, cv.MORPH_OPEN, np.ones((10,10), np.uint8))

    img[np.where(mask == 255)] = background[np.where(mask == 255)]
    cv.imshow('Display',img)
    k = cv.waitKey(10)
    if k == 27:
        break