import cv2
import numpy as np
img = np.zeros((5,4),dtype = np.uint8)
img[1,2]=1

for i in range (1,4):
    img[i,1]=1
#print(img)
kernel = np.array([[1,1],[1,0]],np.uint8)
imerode = cv2.erode(img,kernel)
print(imerode)
#cv2.imshow('fix',imdilate)



