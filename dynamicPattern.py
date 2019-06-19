import sys
sys.path.append('./slmPy/')
import slmPy as slmpy
import time
import numpy as np
from numpy import matlib
import matplotlib
matplotlib.use('AGG')
import matplotlib.pyplot as plt

monitor=1
correctionFactor = 123#int((64-54)/(633-532)*473*4)
print(correctionFactor)
slm = slmpy.SLMdisplay(monitor=monitor, isImageLock = True)
resX, resY = slm.getSize()
# We use images twice smaller than the resolution of the slm
ImgResX = resX
ImgResY = resY
#lam = 473.
#scalingFactor = (lam/633)*255
X,Y = np.meshgrid(np.linspace(0,ImgResX,ImgResX),np.linspace(0,ImgResY,ImgResY))
while True:
    for i in range(100):
       testIMG = np.round(correctionFactor*(0.5+0.5*np.sin(2*np.pi*Y/2))).astype('uint8')
       #addBuffer = np.full_like(testIMG,1) * 
       addBuffer = matlib.repmat(np.linspace(0,ImgResY*40, ImgResY), ImgResX, 1).astype('uint8')
       print(np.shape(addBuffer))
       
       #slm.updateArray(np.mod(testIMG,correctionFactor))
       slm.updateArray(np.mod(addBuffer.T,correctionFactor))
       time.sleep(1)
       print(np.max(testIMG))
slm.close()
