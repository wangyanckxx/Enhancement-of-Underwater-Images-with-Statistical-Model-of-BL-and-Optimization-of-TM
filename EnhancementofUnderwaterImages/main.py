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

folder = "F:/0000-Important/UnderwaterImageEnhancement/EnhancementofUnderwaterImages"

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
        gimfiltR = 50  # Radius size of guided filter
        eps = 10 ** -3  # Epsilon value of guided filter
        Nrer = [0.95, 0.93, 0.85] # Normalized residual energy ratio of G-B-R channels

        AtomsphericLight = np.zeros(3)
        AtomsphericLight[0] = (1.13 * np.mean(img[:, :, 0])) + 1.11 * np.std(img[:, :, 0]) - 25.6
        AtomsphericLight[1] = (1.13 * np.mean(img[:, :, 1])) + 1.11 * np.std(img[:, :, 1]) - 25.6
        AtomsphericLight[2] = 140 / (1 + 14.4 * np.exp(-0.034 * np.median(img[:, :, 2])))
        AtomsphericLight = np.clip(AtomsphericLight, 5, 250)
        transmissionR = getTransmission(img, AtomsphericLight, blockSize)
        TM_R_modified = Depth_TM(img, AtomsphericLight)
        TM_R_modified_Art = Sat_max(img)
        transmissionR_new = np.copy(transmissionR)
        for i in range(0, img.shape[0]):
            for j in range(0, img.shape[1]):
                if(transmissionR_new[i, j] > TM_R_modified[i, j]):
                    transmissionR_new[i, j] = TM_R_modified[i, j]
                if(transmissionR_new[i, j] < TM_R_modified_Art[i, j]):
                    transmissionR_new[i, j] = TM_R_modified_Art[i, j]

        transmissionR_Stretched = stretching(transmissionR_new, height, width)
        transmissionB, transmissionG, depth_map = getGBTransmissionESt(transmissionR_Stretched, AtomsphericLight)
        transmission = Refinedtransmission(transmissionB, transmissionG, transmissionR_Stretched, img)
        sceneRadiance = sceneRadianceRGB(img, transmission, AtomsphericLight)
        sceneRadiance = OptimalParameter(sceneRadiance)
        cv2.imwrite('OutputImages/' + prefix + '_SMBLOTMOP.jpg', sceneRadiance)

Endtime = datetime.datetime.now()
Time = Endtime - starttime
print('Time', Time)

