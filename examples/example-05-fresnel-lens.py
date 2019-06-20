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


twopi_lambda = 123
focal_length = float(sys.argv[1])

size = (1280, 1024)

x, y = np.meshgrid(np.arange(size[0]), np.arange(size[1]))
print(x,y, np.shape(x), np.shape(y))
d = ((x-size[0]/2)**2 + (y-size[1]/2)**2)
d/=focal_length
phase_mask = twopi_lambda*np.mod(d, 2*np.pi)/(2*np.pi)
np.save('Fresnel_lens_{}'.format(focal_length), phase_mask)
