import sys
sys.path+= ['../slmPy/', '../Phase_retrieval_single_constraint/']
import time
import numpy as np
from numpy import matlib
import cv2
import slmPy as slmpy
from phase_retrieval_GS import *
import matplotlib
matplotlib.use('WXAgg')
import matplotlib.pyplot as plt
import numpy as np
import slmPy

filename = 'images.jpg'
img = np.zeros((500,500,4),np.uint8)
cv2.putText(img, "TENSS", (50,70),cv2.FONT_HERSHEY_PLAIN,5, (0,0,255,255), 20)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img = img.astype(float)
img = np.asarray(img, float)
max_iters = 1000
phase_mask = Ger_Sax_algo(img, max_iters)
plt.figure(1)
plt.subplot(131)
plt.imshow(img)
plt.title('Desired image')
plt.subplot(132)
plt.imshow(phase_mask)
plt.title('Phase mask')
plt.subplot(133)
recovery = np.fft.ifft2(np.exp(phase_mask * 1j))
plt.imshow(np.absolute(recovery)**2)
plt.title('Recovered image')
plt.show()

monitor=1
correctionFactor = int((64-54)/(633-532)*473*4)
print(correctionFactor)
slm = slmpy.SLMdisplay(monitor=monitor, isImageLock = True)
resX, resY = slm.getSize()
# We use images twice smaller than the resolution of the slm
ImgResX = resX//2
ImgResY = resY//2
#lam = 473.
#scalingFactor = (lam/633)*255
X,Y = np.meshgrid(np.linspace(0,ImgResX,ImgResX),np.linspace(0,ImgResY,ImgResY))
while True:
       testIMG = np.round(correctionFactor*((phase_mask+np.pi)/(2*np.pi))).astype('uint8')
       #print(testIMG)
       #addBuffer = np.full_like(testIMG,1) * 
       #addBuffer = matlib.repmat(np.linspace(0,500, ImgResY), ImgResX, 1).astype('uint8')
       
       slm.updateArray(np.mod(testIMG,correctionFactor))
       time.sleep(1)
       print(np.max(testIMG))
slm.close()
