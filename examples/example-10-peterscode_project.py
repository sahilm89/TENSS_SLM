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

monitor = 1

phase_files = np.array([np.load(i) for i in sys.argv[1:]])
phase_mask = np.sum(phase_files, axis=0)
#correctionFactor = 123 
#print(correctionFactor)
phase_mask = np.mod(phase_mask, 123)
#testIMG = correctionFactor*((phase_mask)/(2*np.pi))
disp_arr = np.round(phase_mask).astype('uint8')
#disp_arr = phase_mask
print(disp_arr)

slm = slmpy.SLMdisplay(monitor=monitor, isImageLock = True)

while True:
    slm.updateArray(disp_arr)
    time.sleep(0.5)
slm.close()
