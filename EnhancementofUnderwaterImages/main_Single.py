import os
import numpy as np
import datetime
import cv2
import natsort
from skimage.color import rgb2lab, lab2rgb
import matplotlib.pyplot as plt

from DepthMap_RTM import Depth_TM
from Saturation_Max import Sat_max
from depthMapEstimation import depthMap
from getGBTransmission import getGBTransmissionESt
from getRefinedTransmission import Refinedtransmission
from getTransmissionEstimation import getTransmission
from global_histogram_stretching import stretching
from sceneRadiance import sceneRadianceRGB

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
    gimfiltR = 50  # 引导滤波时半径的大小
    eps = 10 ** -3  # 引导滤波时epsilon的值
    blockSize = 9
    Nrer = [0.95, 0.93, 0.85]


    # cv2.imwrite('Results_Single_Channel/' + Num + 'Refined_transmissionR.jpg', np.uint8(img[:,:,2] ))
    # cv2.imwrite('Results_Single_Channel/' + Num + 'Refined_transmissionG.jpg', np.uint8(img[:,:,1] ))
    # cv2.imwrite('Results_Single_Channel/' + Num + 'Refined_transmissionB.jpg', np.uint8(img[:,:,0] ))

    AtomsphericLight = np.zeros(3)
    AtomsphericLight[0] = (1.13 * np.mean(img[:, :, 0])) + 1.11 * np.std(img[:, :, 0]) - 25.6
    AtomsphericLight[1] = (1.13 * np.mean(img[:, :, 1])) + 1.11 * np.std(img[:, :, 1]) - 25.6
    AtomsphericLight[2] = 140 / (1 + 14.4 * np.exp(-0.034 * np.median(img[:, :, 2])))
    AtomsphericLight = np.clip(AtomsphericLight, 10, 245)
    print('AtomsphericLight', AtomsphericLight)
    transmissionR = getTransmission(img, AtomsphericLight, blockSize)
    transmissionR_new = transmissionR
    # TM_R_modified = Depth_TM(img, AtomsphericLight)
    # # TM_R_modified_Art = Sat_max(img)
    # transmissionR_new = np.copy(transmissionR)
    #
    # for i in range(0, img.shape[0]):
    #     for j in range(0, img.shape[1]):
    #         if(transmissionR_new[i, j] > TM_R_modified[i, j]):
    #             # print('transmissionR_new[i, j]', transmissionR_new[i, j])
    #             # print('TM_R_modified[i, j]', TM_R_modified[i, j])
    #             transmissionR_new[i, j] = TM_R_modified[i, j]

    # for i in range(0, img.shape[0]):
    #     for j in range(0, img.shape[1]):
    #         if(transmissionR_new[i, j] > TM_R_modified[i, j]):
    #             # print('transmissionR_new[i, j]', transmissionR_new[i, j])
    #             # print('TM_R_modified[i, j]', TM_R_modified[i, j])
    #             transmissionR_new[i, j] = TM_R_modified[i, j]
    #         if(transmissionR_new[i, j] < TM_R_modified_Art[i, j]):
    #             transmissionR_new[i, j] = TM_R_modified_Art[i, j]



    # cv2.imwrite('Results_TMs/' + Num + 'TM_R_Refi_modified_fusion.jpg', np.uint8(transmissionR_new * 255))
    transmissionR_Stretched = stretching(transmissionR_new, height, width)

    cv2.imwrite('Results_TMs/' + Num + 'TM_R.jpg', np.uint8(transmissionR_Stretched * 255))

    # # transmissionR_Stretched = stretching(transmissionR, height, width)
    #
    # transmissionB, transmissionG, depth_map = getGBTransmissionESt(transmissionR_Stretched, AtomsphericLight)
    #
    # transmission = Refinedtransmission(transmissionB,transmissionG,transmissionR_Stretched, img)
    # transmissionR_Stretched = transmission[:, :, 2]
    # #
    # #
    # #
    # # cv2.imwrite('Results_TMs/' + Num + 'TM_R.jpg', np.uint8(transmissionR  * 255))
    # # cv2.imwrite('Results_TMs/' + Num + 'TM_R_Refi_fusion_Sat_lamba.jpg', np.uint8(transmissionR_Stretched  * 255))
    #
    #
    # sceneRadiance = sceneRadianceRGB(img, transmission, AtomsphericLight)
    # # cv2.imwrite('Results_TMs_minR_0point25/' + Num + 'Restoration_Sat_lamba.jpg', sceneRadiance)
    # cv2.imwrite('Results_TMs_minR_0point25/' + Num + 'Restoration_Fusion.jpg', sceneRadiance)
    # #
    # #
    # #
    # #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
