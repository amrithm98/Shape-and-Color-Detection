import cv2
import numpy as np
img = cv2.imread('test_files/board_5.jpg')
mask=inRange()
res = cv2.bitwise_and(img,img,mask = mask)