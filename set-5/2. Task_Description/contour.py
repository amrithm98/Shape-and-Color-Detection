import numpy as np
import cv2
im = cv2.imread('test_images/board_5.jpg')
hsv=cv2.cvtColor(im,cv2.COLOR_BGR2HSV)
mask=cv2.inRange(hsv,np.array([0,0,0],dtype = "uint8"),np.array([179,50,100],dtype = "uint8")); 
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
cv2.imshow("Threshold",thresh)
cv2.imshow("HSV",hsv)
im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.imshow("img",im)
im2=cv2.drawContours(im,contours, -1, (0,255,0), 3)
cv2.imshow("ctr",im2)
cv2.waitKey(0)