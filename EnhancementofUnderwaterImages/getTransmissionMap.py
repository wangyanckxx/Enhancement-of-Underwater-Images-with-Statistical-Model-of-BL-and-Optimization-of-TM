import numpy as np
def getMinChannel(img,AtomsphericLight):
    imgGrayNormalization = np.zeros((img.shape[0], img.shape[1]), dtype=np.float16)
    for i in range(0, img.shape[0]):
        for j in range(0, img.shape[1]):
            localMin = 1
            for k in range(0, 3):
                # print('AtomsphericLight[k]',AtomsphericLight[k])
                imgNormalization = img.item((i, j, k)) / AtomsphericLight[k]
                if imgNormalization < localMin:
                    localMin = imgNormalization
            imgGrayNormalization[i, j] = localMin
    # print('imgGrayNormalization',imgGrayNormalization)
    # print('np.max(imgGrayNormalization)',np.max(imgGrayNormalization))
    return imgGrayNormalization

def getTransmission(img,AtomsphericLight ,blockSize):
    img = np.float16(img)
    img = getMinChannel(img,AtomsphericLight)
    AtomsphericLight = AtomsphericLight / 255.0
    addSize = int((blockSize - 1) / 2)
    newHeight = img.shape[0] + blockSize - 1
    newWidth = img.shape[1] + blockSize - 1
    # 中间结果
    imgMiddle = np.zeros((newHeight, newWidth))
    imgMiddle[:, :] = 1
    imgMiddle[addSize:newHeight - addSize, addSize:newWidth - addSize] = img
    # print('imgMiddle',imgMiddle)
    imgDark = np.zeros((img.shape[0], img.shape[1]))
    localMin = 1
    for i in range(addSize, newHeight - addSize):
        for j in range(addSize, newWidth - addSize):
            localMin = 1
            for k in range(i - addSize, i + addSize + 1):
                for l in range(j - addSize, j + addSize + 1):
                    if imgMiddle.item((k, l)) < localMin:
                        localMin = imgMiddle.item((k, l))
            imgDark[i - addSize, j - addSize] = localMin
        transmission = (1 - imgDark) / (1 - 0.1 / np.max(AtomsphericLight))
    transmission = np.clip(transmission, 0.1, 0.9)
    # for i in range(0, transmission.shape[0]):
    #     for j in range(0, transmission.shape[1]):
    #         if transmission[i, j] < 0.01:
    #             transmission[i, j] = 0.01
    #         if transmission[i, j] > 0.99:
    #             transmission[i, j] = 0.99

    return transmission