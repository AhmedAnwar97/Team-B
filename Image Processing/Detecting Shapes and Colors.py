
# coding: utf-8

# In[1]:


import cv2
import imutils
import numpy as np
import pytesseract
from PIL import Image


# In[2]:


def detect(c):

    approx = cv2.approxPolyDP(c,0.04*cv2.arcLength(c,True),True)
    shape=''
        
    if len(approx)==3:
        print ("triangle")
        shape = "triangle"
       
    elif len(approx)==4:
        print ("rectangle")
        shape = "rectangle"
    else:
        shape = "circle"
    
      
    return shape


# In[3]:


def detectShapes(image, mask, color):
    
    res = cv2.bitwise_and(image,image, mask=mask)
    kernel = np.ones((5,5),np.uint8)
    opening = cv2.morphologyEx(res, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(res, cv2.MORPH_CLOSE, kernel)


    edges = cv2.Canny(closing, 100, 200)

    lines = cv2.HoughLinesP(edges,1,np.pi/180,20,minLineLength=10,maxLineGap=100)
    if(lines is None):
        return
    N = lines.shape[0]
    for i in range(N):
        x1 = lines[i][0][0]
        y1 = lines[i][0][1]    
        x2 = lines[i][0][2]
        y2 = lines[i][0][3]    
        cv2.line(edges,(x1,y1),(x2,y2),(255,0,0),2)  
    # cv2.imshow('im', edges)
    mx = np.amax(edges)
    mn = np.amin(edges)

    thresh_val = np.average(np.arange(mn,mx))
    _, thresh = cv2.threshold(edges,thresh_val,255,cv2.THRESH_BINARY)
    # cv2.imshow('thresh', thresh)

    cnts = cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if imutils.is_cv2() else cnts[1]

    for c in cnts:
        M=cv2.moments(c)
        cX = int((M["m10"]/M["m00"])*ratio)
        cY = int((M["m01"]/M["m00"])*ratio)
        shape = detect(c)
        c = c.astype("float")
        c *= ratio
        c = c.astype("int")

        cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
        cv2.putText(image, color +" " + shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX,0.5, (0, 0, 0), 2)

    


# In[ ]:


image = cv2.imread('4.png')

ratio = image.shape[0] / float(image.shape[0])
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
color=""

lower_blue = np.array([100,50,40])
upper_blue = np.array([130,255,255])

lower_yellow = np.array([20,110,100])
upper_yellow = np.array([30,255,255])

lower_red = np.array([0,150,120])
upper_red = np.array([10,255,255])

mask1 = cv2.inRange(hsv, lower_blue, upper_blue)
mask2 = cv2.inRange(hsv, lower_yellow, upper_yellow)
mask3 = cv2.inRange(hsv, lower_red, upper_red)

detectShapes(image, mask1, 'blue')
detectShapes(image, mask2, 'yellow')
detectShapes(image, mask3, 'red')

cv2.imshow('image',image)    

cv2.waitKey(0)
cv2.destroyAllWindows()

