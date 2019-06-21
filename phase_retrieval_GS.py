import math
import numpy as np


def Ger_Sax_algo(img, max_iter=100, twopi_lambda=123):
    mon_h, mon_w = 1024, 1280
    target = np.zeros((mon_h, mon_w))

    h, w = img.shape
    print(img.shape)

    #img = 255.-img
    img/=255.

    target[:h, :w] = img

    pm_s = np.random.rand(mon_h, mon_w)
    A = np.exp(2*np.pi*pm_s * 1j) #A

    pm_f = np.ones((mon_h, mon_w))


    for it in range(max_iter):
        B = np.fft.fftshift(np.fft.fft2(A))
        pm_f = np.angle(B)
        B_ = target*np.exp(1j*pm_f)
        
        A = np.fft.ifft2(np.fft.fftshift(B_))
        pm_s = np.angle(A)
        A = np.exp(pm_s * 1j)
        print(it)
    
    pm_s = np.angle(A)
    phasemask = twopi_lambda*np.mod(pm_s+np.pi, 2*np.pi)/(2*np.pi)
    return phasemask

