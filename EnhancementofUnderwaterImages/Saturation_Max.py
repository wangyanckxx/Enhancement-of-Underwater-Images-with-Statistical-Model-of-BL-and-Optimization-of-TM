import numpy as np


def Sat_max(img):
    height = len(img)
    width = len(img[0])
    # print('img[0,0,:]',img[0,0,:])
    Sat = np.zeros((height,width ))
    for i in range(0, img.shape[0]):
        for j in range(0, img.shape[1]):
            if(np.max(img[i,j,:]) == 0):
                Sat[i,j] = 1
            else:
                Sat[i, j] = (np.max(img[i,j,:]) - np.min(img[i,j,:]))/np.max(img[i,j,:])
    Sat = 1 - Sat

    # lamba = 1 - np.mean(Sat)
    lamba = 1

    Sat = Sat * lamba
    return Sat



