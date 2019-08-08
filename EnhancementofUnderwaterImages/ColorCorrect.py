import os
import numpy as np
import datetime
import cv2
import natsort

np.seterr(over='ignore')
if __name__ == '__main__':
    pass

def color_correction(r,u_r,u_ref,L2):
    L1 = np.max(r)
    gainFactor = L1 * (u_r/ u_ref) +L2
    Out = r / gainFactor
    return Out

def OptimalParameter(sceneRadiance):
    img = np.float64(sceneRadiance / 255)
    b, g, r = cv2.split(img)

    u_r = np.sum(r)
    u_g = np.sum(g)
    u_b = np.sum(b)
    u_ref = (u_r ** 2 + u_g ** 2 + u_b ** 2) ** 0.5
    L2 = 0.25
    r = color_correction(r, u_r, u_ref, L2)
    g = color_correction(g, u_g, u_ref, L2)
    b = color_correction(b, u_b, u_ref, L2)

    sceneRadiance = np.zeros((img.shape), 'float64')
    sceneRadiance[:, :, 0] = b
    sceneRadiance[:, :, 1] = g
    sceneRadiance[:, :, 2] = r
    sceneRadiance = sceneRadiance * 255
    sceneRadiance = np.clip(sceneRadiance,0, 255)
    sceneRadiance = np.uint8(sceneRadiance)
    return sceneRadiance



















