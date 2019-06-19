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


size=(1280,1024)
x,y =np.meshgrid(np.arange(size[0]),np.arange(size[1]))
lens=((x-size[0]/2)**2+(y-size[1]/2)**2)
def fresnel_lens(focal_len):
   return np.mod(lens/focal_len,2*np.pi)

monitor = 1
phase_files = np.array([np.load(i) for i in sys.argv[1:]])
phase_mask = np.sum(phase_files, axis=0)
correctionFactor = 123 
print(correctionFactor)
phase_mask = np.mod(phase_mask, 2*np.pi)
testIMG = correctionFactor*((phase_mask)/(2*np.pi))
disp_arr = np.round(testIMG).astype('uint8')
print(disp_arr)

slm = slmpy.SLMdisplay(monitor=monitor, isImageLock = True)

while True:
    for fl in np.linspace(-500,-300,100):
        testIMG=correctionFactor*(phase_mask)
        slm.updateArray(disp_arr+fresnel_lens(fl))
        time.sleep(0.1)
slm.close()
