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
import glob

monitor = 1

phase_masks = sys.argv[1]

slm = slmpy.SLMdisplay(monitor=monitor)#, isImageLock = True)
rangeFile = np.arange(30)
while True:
    for fname in [phase_masks + '/einstein-{}.png_mask.npy'.format(i) for i in rangeFile] :
        print(fname)
        phase_files = np.array(np.load(fname))
        phase_mask = np.mod(phase_files, 123)
        disp_arr = np.round(phase_mask).astype('uint8')
        #slm = slmpy.SLMdisplay(monitor=monitor)#, isImageLock = True)
        slm.updateArray(disp_arr)
        time.sleep(0.2) 
slm.close()
