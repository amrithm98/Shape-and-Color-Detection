import cv2
import numpy as np

cap = cv2.VideoCapture(0)
i=1;
if i==1:
    # Take each frame
    frame=cv2.imread("test_images/board_5.jpg")
    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    i=i+1
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        quit()

cv2.destroyAllWindows()
