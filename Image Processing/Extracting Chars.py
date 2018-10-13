
# coding: utf-8

# In[1]:


import cv2
import imutils
import numpy as np
import pytesseract
from PIL import Image


# In[2]:


img = cv2.imread("7.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

kernel = np.ones((1, 1), np.uint8)
img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
# cv2.imshow("thresh",img)
R= img.shape[0]
C= img.shape[1]
text = img[280:350,135:220] #7
# text = img[305:375,130:210] #9
# cv2.imshow("text",text)
image = np.ones((R,C))
image[280:350,135:220] = text #7
# image[305:375,130:210] = text #9
image[:,:] = image[:,:]*255
# cv2.imshow("image",image)

test = image[50:350,50:250]
test[:,:] = test[:,:]*255

result = pytesseract.image_to_string(test)
print (result)

cv2.waitKey(0)
cv2.destroyAllWindows()


# In[3]:





# In[4]:



              


# In[6]:




