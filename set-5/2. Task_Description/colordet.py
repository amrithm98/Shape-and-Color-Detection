# import the necessary packages
import numpy as np
import cv2
shapes=[0,0,0,0]
def circle(image):
	output=image.copy()
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.2, 100)
# ensure at least some circles were found
	if circles is not None:
	# convert the (x, y) coordinates and radius of the circles to integers
		circles = np.round(circles[0, :]).astype("int")
 
	# loop over the (x, y) coordinates and radius of the circles
		for (x, y, r) in circles:
		# draw the circle in the output image, then draw a rectangle
		# corresponding to the center of the circle
			cv2.circle(output, (x, y), r, (0, 255, 0), 4)
			cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
 
	# show the output image
		cv2.imshow("output", np.hstack([image, output]))
		cv2.waitKey(0)
def cont(mask):
	gray = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
	ret,thresh = cv2.threshold(gray,127,255,1)
	cv2.imshow("Threshold",thresh)
	count=0
	'''cnts= cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
	print "I found %d black shapes" % (len(cnts))
	cv2.imshow("Mask",mask)'''
	_,contours,h= cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	print (len(contours))
	for cnt in contours:
		count+=1;
		#print (cnt)
		approx=cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
		print len(approx)
		cv2.imshow("Cont"+str(count),cv2.drawContours(thresh,cnt,-1, (70,70,34), 3))
		cv2.waitKey(0)
image = cv2.imread("test_images/board_5.jpg")
#image = cv2.imread("download.png")
hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
masks=[]
boundaries = [
	([100,50,50],[130,255,255]),([50, 100, 100],[70, 255, 255]),([0,50,50],[7,255,255]),([30,100,100],[40,255,255])]
for (lower, upper) in boundaries:
	lower = np.array(lower, dtype = "uint8")
	upper = np.array(upper, dtype = "uint8")
	mask = cv2.inRange(hsv, lower, upper)
	masks+=[mask]
	non_zero=cv2.countNonZero(mask)
	res = cv2.bitwise_and(image,image, mask= mask)
	print (non_zero)
	# show the images
	cv2.imshow("mask",mask)
	cv2.imshow("res",res)
	cv2.imshow("img",image)
	#cont(mask)
	cv2.waitKey(0)
for i in masks:
	mask+=i;
new=cv2.bitwise_and(image,image,mask=mask)
cv2.imshow("Final Mask",new)
cont(image)
#circle(image)
cv2.waitKey(0)

