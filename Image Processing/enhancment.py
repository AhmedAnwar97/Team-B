
# coding: utf-8

# In[1]:


import cv2
import imutils
import numpy as np


# In[2]:


# red filter method
# image = cv2.imread('Capture.png')
# cv2.imshow("im",image)
# b,g,r = cv2.split(image)
# r[:,:] = r[:,:]+50
        
# result = cv2.merge((b,g,r))
# cv2.imshow("image",result)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

def white_balance(img):
    result = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    avg_a = np.average(result[:, :, 1])
    avg_b = np.average(result[:, :, 2])
    result[:, :, 1] = result[:, :, 1] - ((avg_a - 128) * (result[:, :, 0] / 255.0) * 1.1)
    result[:, :, 2] = result[:, :, 2] - ((avg_b - 128) * (result[:, :, 0] / 255.0) * 1.1)
    result = cv2.cvtColor(result, cv2.COLOR_LAB2BGR)
    return result

image = cv2.imread('Capture.png')
cv2.imshow("im",image)

result = white_balance(image)
cv2.imshow("image",result)

cv2.waitKey(0)
cv2.destroyAllWindows()

