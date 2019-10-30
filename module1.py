import cv2
import numpy as np
img = cv2.imread('d:/org.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
template=cv2.imread('d:/ex.png')
surf = cv2.xfeatures2d.SURF_create(5000)

keypoints, descriptors = surf.detectAndCompute(gray, None)
print ("Number of keypoints Detected: ", len(keypoints))
img1 = cv2.drawKeypoints(img, keypoints, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
#img2 = cv2.drawKeypoints(template, keypoints, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow('Feature Method - SURF', img1)
#cv2.imshow('Example',img2)
#result=cv2.matchTemplate(img1,img2,cv2.TM_CCOEFF)
result=cv2.matchTemplate(img1,template,cv2.TM_CCOEFF)
sin_val, max_val, min_loc, max_loc=cv2.minMaxLoc(result)
top_left=max_loc

bottom_right=(top_left[0]+50,top_left[1]+50)
cv2.rectangle(img, top_left, bottom_right, (0,255,0),5)

cv2.imshow('object found',img)
cv2.waitKey()
cv2.destroyAllWindows()

