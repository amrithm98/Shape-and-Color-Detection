import numpy as np
import cv2

image_src = cv2.imread("test_images/board_5.jpg")

gray = cv2.cvtColor(image_src, cv2.COLOR_BGR2GRAY)
ret, gray = cv2.threshold(gray, 127, 255,1)
cv2.imshow("mask",gray)
cv2.waitKey(0)
image, contours, hierarchy = cv2.findContours(gray, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
mask = np.zeros(image_src.shape, np.uint8)
cv2.imshow("mask",mask)
cv2.waitKey(0)
largest_areas = sorted(contours, key=cv2.contourArea)
print len(largest_areas)
for i in range(0,len(largest_areas)):
	cv2.drawContours(mask,[largest_areas[i]],0,(255,255,255),-1)
	removed = cv2.add(image_src, mask)
	cv2.imshow('rem',removed)
	cv2.waitKey(0)
cv2.imwrite("removed.png", removed)