
import numpy as np

def depthMap(img):

    theta_0 = 0.51157954
    theta_1 = 0.50516165
    theta_2 = -0.90511117
    img = img / 255.0
    b = img[:, :, 0]
    g = img[:, :, 1]
    r = img[:, :, 2]
    x_1 = np.maximum(g, b)
    x_2 = r

    Deptmap = theta_0 + theta_1 * x_1 + theta_2 * x_2


    return Deptmap



