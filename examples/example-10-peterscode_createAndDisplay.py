import sys
sys.path+= ['../slmPy/', '../']
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

twopi_lambda = 123
filename = sys.argv[1] 
writeFile = sys.argv[2]
img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
img = img.astype(float)
img = np.asarray(img, float)
print(np.max(img))
max_iters = 100
phase_mask = Ger_Sax_algo(img, max_iters)
plt.figure(1)
plt.subplot(131)
plt.imshow(img)
plt.title('Desired image')
plt.subplot(132)
plt.imshow(phase_mask)
plt.title('Phase mask')
plt.subplot(133)
recovery = np.fft.fftshift(np.fft.ifft2(-np.exp(((2*np.pi*(phase_mask/twopi_lambda ) + np.pi )* 1j) )))
plt.imshow(np.absolute(recovery)**2)
plt.title('Recovered image')
plt.show()
np.save(writeFile, phase_mask)
