import numpy as np
import math


def getGBTransmissionESt(transmissionR,AtomsphericLightTM):
    depth_map = np.zeros(transmissionR.shape)
    for i in range(0,transmissionR.shape[0]):
        for j in range(0, transmissionR.shape[1]):
            depth_map[i,j]  = math.log(transmissionR[i,j],0.82)
            # if(depth_map[i,j]>15):
            #     depth_map[i, j] = 15
            # if (depth_map[i, j] < 1):
            #     depth_map[i, j] = 1



    transmissionG = 0.93 ** depth_map
    transmissionB = 0.95 ** depth_map
    # transmissionG = np.zeros(transmissionR.shape)

    # transmissionB = np.zeros(transmissionR.shape)
    # ratioB = (AtomsphericLightTM[2] * (-0.00113 * 450 + 1.62517) )/(AtomsphericLightTM[0] * (-0.00113 * 620 + 1.62517))*1.3
    # ratioG = (AtomsphericLightTM[2] * (-0.00113 * 540 + 1.62517) )/(AtomsphericLightTM[1] * (-0.00113 * 620 + 1.62517))*1.2
    # print('ratioB',ratioB)
    # print('ratioG',ratioG)
    # transmissionG = transmissionR ** ratioG
    # transmissionB = transmissionR ** ratioB
    # print('getGBTransmissionESttransmissionB',transmissionB)
    return transmissionB,transmissionG,depth_map




# def getGBTransmissionESt(transmissionR,AtomsphericLightTM):
#     # transmissionG = np.zeros(transmissionR.shape)
#     # transmissionB = np.zeros(transmissionR.shape)
#     ratioB = (AtomsphericLightTM[2] * (-0.00113 * 450 + 1.62517) )/(AtomsphericLightTM[0] * (-0.00113 * 620 + 1.62517))
#     ratioG = (AtomsphericLightTM[2] * (-0.00113 * 540 + 1.62517) )/(AtomsphericLightTM[1] * (-0.00113 * 620 + 1.62517))
#     print('ratioB',ratioB)
#     print('ratioG',ratioG)
#     transmissionG = transmissionR ** ratioG
#     transmissionB = transmissionR ** ratioB
#     print('getGBTransmissionESttransmissionB',transmissionB)
#
#     return transmissionB,transmissionG


