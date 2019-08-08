import os

import datetime
import numpy as np
import cv2
import natsort
from ColorCorrect import OptimalParameter
from DepthMap_RTM import Depth_TM
from Saturation_Max import Sat_max
from getGBTransmission import getGBTransmissionESt
from getRefinedTransmission import Refinedtransmission
from getTransmissionMap import getTransmission
from global_histogram_stretching import stretching
from sceneRadiance import sceneRadianceRGB

np.seterr(over='ignore')
if __name__ == '__main__':
    pass

starttime = datetime.datetime.now()

folder = "C:/Users/Administrator/Desktop/UnderwaterImageEnhancement/Physical/SMBLOTM"
# folder = "C:/Users/Administrator/Desktop/Databases/Dataset"
path = folder + "/InputImages"
files = os.listdir(path)
files =  natsort.natsorted(files)

for i in range(len(files)):
    file = files[i]
    filepath = path + "/" + file
    prefix = file.split('.')[0]
    if os.path.isfile(filepath):
        print('********    file   ********',file)
        img = cv2.imread(folder +'/InputImages/' + file)
        blockSize = 9
        height = len(img)
        width = len(img[0])
        gimfiltR = 50  # 引导滤波时半径的大小
        eps = 10 ** -3  # 引导滤波时epsilon的值
        Nrer = [0.95, 0.93, 0.85]

        AtomsphericLight = np.zeros(3)
        AtomsphericLight[0] = (1.13 * np.mean(img[:, :, 0])) + 1.11 * np.std(img[:, :, 0]) - 25.6
        AtomsphericLight[1] = (1.13 * np.mean(img[:, :, 1])) + 1.11 * np.std(img[:, :, 1]) - 25.6
        AtomsphericLight[2] = 140 / (1 + 14.4 * np.exp(-0.034 * np.median(img[:, :, 2])))
        AtomsphericLight = np.clip(AtomsphericLight, 5, 250)
        print('AtomsphericLight', AtomsphericLight)
        # AtomsphericLight = np.array([76, 40, 35])
        # print('np.array([76, 40, 35])', AtomsphericLight)
        transmissionR = getTransmission(img, AtomsphericLight, blockSize)
        TM_R_modified = Depth_TM(img, AtomsphericLight)
        TM_R_modified_Art = Sat_max(img)
        transmissionR_new = np.copy(transmissionR)
        # for i in range(0, img.shape[0]):
        #     for j in range(0, img.shape[1]):
        #         if (transmissionR_new[i, j] > TM_R_modified[i, j]):
        #             transmissionR_new[i, j] = TM_R_modified[i, j]
        for i in range(0, img.shape[0]):
            for j in range(0, img.shape[1]):
                if(transmissionR_new[i, j] > TM_R_modified[i, j]):
                    transmissionR_new[i, j] = TM_R_modified[i, j]
                if(transmissionR_new[i, j] < TM_R_modified_Art[i, j]):
                    transmissionR_new[i, j] = TM_R_modified_Art[i, j]

        transmissionR_Stretched = stretching(transmissionR_new, height, width)
        transmissionB, transmissionG, depth_map = getGBTransmissionESt(transmissionR_Stretched, AtomsphericLight)
        transmission = Refinedtransmission(transmissionB, transmissionG, transmissionR_Stretched, img)
        transmissionR_Stretched = transmission[:, :, 2]

        # cv2.imwrite('Results_TMs/' + Num + 'TM_R.jpg', np.uint8(transmissionR  * 255))
        # cv2.imwrite('Results_temps/' + prefix + 'TM_R_Refi_fusion_Sat_lamba.jpg', np.uint8(transmissionR_Stretched  * 255))
        # cv2.imwrite('OutputImages/' + prefix + '_SMBLOTMOP_TM.jpg', np.uint8(transmissionR_Stretched  * 255))
        cv2.imwrite('Results_Enhance_fusion/' + prefix + '_SMBLOTMOP_TM_R.jpg', np.uint8(transmissionR_Stretched  * 255))
        # cv2.imwrite('Results_Enhance_fusion/' + prefix + '_SMBLOTMOP_TM_G.jpg', np.uint8(transmission[:, :, 1]  * 255))
        # cv2.imwrite('Results_Enhance_fusion/' + prefix + '_SMBLOTMOP_TM_B.jpg', np.uint8(transmission[:, :, 0]  * 255))

        sceneRadiance = sceneRadianceRGB(img, transmission, AtomsphericLight)
        # cv2.imwrite('OutputImages/' + prefix + '_SMBLOTM.jpg', sceneRadiance)
        cv2.imwrite('Results_Enhance_fusion/' + prefix + '_SMBLOTM.jpg', sceneRadiance)
        sceneRadiance = OptimalParameter(sceneRadiance)

        # cv2.imwrite('Results_temps/' + prefix + '_SMBLOTMOptimalParameters.jpg', sceneRadiance)
        # cv2.imwrite('OutputImages/' + prefix + '_SMBLOTMOP.jpg', sceneRadiance)
        cv2.imwrite('Results_Enhance_fusion/' + prefix + '_SMBLOTMOP.jpg', sceneRadiance)


Endtime = datetime.datetime.now()
Time = Endtime - starttime
print('Time', Time)


