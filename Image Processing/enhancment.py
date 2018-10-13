
# coding: utf-8

# In[1]:


import cv2
import imutils
import numpy as np


# In[2]:


red filter method
image = cv2.imread('Capture.png')
cv2.imshow("im",image)
b,g,r = cv2.split(image)
r[:,:] = r[:,:]+50
        
result = cv2.merge((b,g,r))
cv2.imshow("image",result)

cv2.waitKey(0)
cv2.destroyAllWindows()

