# import the necessary packages
import numpy as np
import cv2

def blobdetect(file):
	im = cv2.imread("file", cv2.IMREAD_GRAYSCALE)
	params = cv2.SimpleBlobDetector_Params()
	detector = cv2.SimpleBlobDetector_create(params)
# Set up the detector with default parameters.
#detector = cv2.SimpleBlobDetector_create()
 
# Detect blobs.
	keypoints = detector.detect(im)
	 
# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
	im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
 
# Show keypoints
	cv2.imshow("Keypoints", im_with_keypoints)
	cv2.waitKey(0)
# construct the argument parse and parse the arguments
# load the image
image = cv2.imread("test_images/board_5.jpg")
hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
masks=[]
boundaries = [
	([100,50,50],[130,255,255]),([50, 100, 100],[70, 255, 255]),([0,50,50],[7,255,255]),([30,100,100],[40,255,255])]
for (lower, upper) in boundaries:
	# create NumPy arrays from the boundaries
	lower = np.array(lower, dtype = "uint8")
	upper = np.array(upper, dtype = "uint8")
	# find the colors within the specified boundaries and apply
	# the mask
	mask = cv2.inRange(hsv, lower, upper)
	masks+=[mask]
	non_zero=cv2.countNonZero(mask)
	res = cv2.bitwise_and(image,image, mask= mask)
	print (non_zero)
	# show the images
	cv2.imshow("mask",mask)
	cv2.imshow("res",res)
	cv2.imshow("img",image)
	cv2.waitKey(0)
for i in masks:
	mask+=i;
new=cv2.bitwise_and(image,image,mask=mask)
cv2.imshow("Final Mask",new)
blobdetect(file)
cv2.waitKey(0)

