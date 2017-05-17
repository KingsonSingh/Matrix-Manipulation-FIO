# -*- coding: utf-8 -*-
"""
Created on Sat May 13 16:30:21 2017

@author: Vaibhav Singh
"""
import cv2
import numpy as np
##############Reading the Image 
image = cv2.imread("Player.png")
edged = cv2.Canny(image,10,250)
#displaying the edges form of original image(main image)
#cv2.imshow("Edges", edged)
#cv2.waitKey(0)
 
##############Applying closing function 
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2,2))
closed = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)
#displaying the closed form og original image(main image)
#cv2.imshow("Closed", closed)
#cv2.waitKey(0)
 
#####finding_contours 
(imaage,cnts, _) = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
index = 0
for c in cnts:
	x,y,w,h = cv2.boundingRect(c)
	if w>15 and h>15:  #this cover all objects those have height and weidth greater than 15
		index+=1
		new_img=image[y:y+h,x:x+w]
		cv2.imwrite("subfolder/"+str(index) + '.png', new_img) #Putting all subimages in different sunfolder
#cv2.imshow("im",image)
#cv2.waitKey(0)

 