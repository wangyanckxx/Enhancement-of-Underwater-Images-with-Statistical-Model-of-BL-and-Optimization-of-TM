# Enhancement-of-Underwater-Images-with-Statistical-Model-of-BL-and-Optimization-of-TM

<h3>This is python implementation for a underwater image enhancement paper "Enhancement of Underwater Images with Statistical Model of Background Light and Optimization of Transmission Map" </h3>


**ABSTRACT!**  Underwater images often have severe quality degradation and distortion due to light absorption and scattering in the water medium. A hazed image formation model is widely used to restore the image quality. It depends on two optical parameters: the background light (BL) and the transmission map (TM). Underwater images can also be enhanced by color and contrast correction from the perspective of image processing. In this paper, we propose an effective underwater image enhancement method for underwater images in composition of underwater image restoration and color correction. Firstly, a manually annotated background lights (MABLs) database is developed. With reference to the relationship between MABLs and the histogram distributions of various underwater images, robust statistical models of BLs estimation are provided. Next, the TM of R channel is roughly estimated based on the new underwater dark channel prior (NUDCP) via the statistic of clear and high resolution (HD) underwater images, then a scene depth map based on the underwater light attenuation prior (ULAP) and an adjusted reversed saturation map (ARSM) are applied to compensate and modify the coarse TM of R channel. Next, TMs of G-B channels are estimated based on the difference of attenuation ratios between R channel and G-B channels. Finally, to improve the color and contrast of the restored image with a dehazed and natural appearance, a variation of white balance is introduced as post-processing. In order to guide the priority of underwater image enhancement, sufficient evaluations are conducted to discuss the impacts of the key parameters including BL and TM, and the importance of the color correction. Comparisons with other state-of-the-art methods demonstrate that our proposed underwater image enhancement method can achieve higher accuracy of estimated BLs, less computation time, more superior performance, and more valuable information retention.


## Install
Here is the list of libraries you need to install to execute the code:
- python = 3.6
- cv2
- numpy
- scipy
- matplotlib
- scikit-image
- natsort
- math
- datetime

## Content
This repository contains the files:
- Dataset: contains original images and MABLs
- EnhancementofUnderwaterImages: the raw running code 

## Easy Usage
1. Complete the running environment configuration;
2. Put the inputs images to corresponding folders :
  - (create 'InputImages' and 'OutputImages' folders, then put raw images to 'InputImages' folder);
3. Python main.py;
4. Find the enhanced/restored images in "OutputImages" folder.


## If these codes prove useful for your research, please cite our pre-printed review paper and some related papers.

```
@article{Review of Image Enhancement and Image Restoration Methods,
    author    = {Wei Song, Yan Wang, Dongmei Huang, Antonio Liotta, Cristian Perra},
    title     = {Enhancement of Underwater Images with Statistical Model of Background Light and Optimization of Transmission Map},
    journal   = {IEEE Transactions on Broadcasting},
    year      = {2019}
}
@article{Review of Image Enhancement and Image Restoration Methods,
    author    = {Wei Song, Yan Wang, Dongmei Huang, Antonio Liotta, Cristian Perra},
    title     = {Enhancement of Underwater Images with Statistical Model of Background Light and Optimization of Transmission Map},
    journal   = {arXiv:1906.08673},
    year      = {2019}
}
```

## Authors
- Yan Wang, e-mail: 19110860017@fudan.edu.cn
- Wei Song, e-mail: wsong@shou.edu.cn
