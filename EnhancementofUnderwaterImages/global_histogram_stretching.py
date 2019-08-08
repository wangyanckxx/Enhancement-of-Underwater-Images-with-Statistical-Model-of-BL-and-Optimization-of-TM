import os

import datetime
import math


import numpy as np
from scipy import stats
import cv2

pi = math.pi
e = math.e






def global_stretching_depth(img_L):
    height = len(img_L)
    width = len(img_L[0])
    length = height * width
    R_rray = []
    for i in range(height):
        for j in range(width):
            R_rray.append(img_L[i][j])
    R_rray.sort()
    I_min = R_rray[int(length / 1000)]
    I_max = R_rray[-int(length / 1000)]
    print('I_min',I_min)
    print('I_max',I_max)
    array_Global_histogram_stretching_L = np.zeros((height, width))
    for i in range(0, height):
        for j in range(0, width):
            if img_L[i][j] < I_min:
                p_out = img_L[i][j]
                array_Global_histogram_stretching_L[i][j] = 0.2
            elif (img_L[i][j] > I_max):
                p_out = img_L[i][j]
                array_Global_histogram_stretching_L[i][j] = 0.9
            else:
                p_out = (img_L[i][j] - I_min) * ((0.9-0.2) / (I_max - I_min))+ 0.2
                array_Global_histogram_stretching_L[i][j] = p_out
    return (array_Global_histogram_stretching_L)



def stretching(sceneRadiance,height, width):

    r_array_Global_histogram_stretching = global_stretching_depth(sceneRadiance)
    sceneRadiance = r_array_Global_histogram_stretching


    return sceneRadiance
