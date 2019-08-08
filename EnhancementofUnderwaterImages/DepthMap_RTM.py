from depthMapEstimation import depthMap
from depthMin import minDepth


def Depth_TM(img, AtomsphericLight):

    DepthMap = depthMap(img)
    t0, t1 = 0.05, 0.95
    DepthMap = DepthMap.clip(t0, t1)
    d_0 = minDepth(img, AtomsphericLight)

    d_f = 8 * (DepthMap + d_0)
    TM_R_modified = 0.85 ** d_f
    return TM_R_modified