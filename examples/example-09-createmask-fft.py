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

filename = sys.argv[1] 
writeFile = sys.argv[2]
img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
img = img.astype(float)
img = np.asarray(img, float)
max_iters = 50
phase_mask = Ger_Sax_algo(img, max_iters)
plt.figure(1)
plt.subplot(131)
plt.imshow(img)
plt.title('Desired image')
plt.subplot(132)
plt.imshow(phase_mask)
plt.title('Phase mask')
plt.subplot(133)
recovery = np.fft.ifft2(np.exp(np.fft.fftshift(phase_mask * 1j)))
plt.imshow(np.absolute(recovery)**2)
plt.title('Recovered image')
plt.show()
np.save(writeFile,np.fft.fftshift( phase_mask))
