import os
import numpy as np
import datetime
import cv2
import natsort
from skimage.color import rgb2lab, lab2rgb
import matplotlib.pyplot as plt


np.seterr(over='ignore')
if __name__ == '__main__':
    pass

path = "F:/PaperExperiments/ACMMM2018/OptimalTM_BLs_Restor/InputImages"
# path = "F:/PaperExperiments/ACMMM2018/OptimalTM_BLs_Restor/Temps"
files = os.listdir(path)
files =  natsort.natsorted(files)
starttime = datetime.datetime.now()

# BLs = read_xls_file()
# print('BLs',BLs)

for i in range(len(files)):
    file = files[i]
    Num  = file.split('.')[0]
    filepath = path + "/" + file
    # BL = BLs[i]
    print('********    file   ********', file)
    img = cv2.imread('InputImages/' + file)
    # img = cv2.imread('Temps/' + file)
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
    # print('Sat',Sat)
    Sat = 1- Sat
    lamba = 1 - np.mean(Sat)
    print('lamba',lamba)

    #
    # cv2.imwrite('Results_Saturation/' + Num + 'Sat_TM_lamba.jpg', np.uint8((Sat * lamba) * 255))

