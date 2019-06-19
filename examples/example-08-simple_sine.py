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

monitor=1

phase_files = np.load(sys.argv[1]) 
#phase_mask = np.sum(phase_files)
phase_mask = phase_files

correctionFactor = 123 
print(correctionFactor)
slm = slmpy.SLMdisplay(monitor=monitor, isImageLock = True)
resX, resY = slm.getSize()
# We use images twice smaller than the resolution of the slm
#phase_mask[np.where(phase_mask<0)]+=2*np.pi
while True:
       testIMG = correctionFactor*((phase_mask)/(2*np.pi))

       disp_arr = np.round(testIMG).astype('uint8')
       slm.updateArray(disp_arr)
       time.sleep(1)
       print(np.max(disp_arr))
slm.close()
