import os
import cv2
import numpy as np


def postproc2(img,kernel_size = (3,3),erosion_iters = [1,1],dilation_iters = [1,1]):
    
    # Otsu's thresholding
    ret, binary_img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    
    denoise_img = cv2.fastNlMeansDenoising(binary_img, None, 20)
    # dilation & erosion
    kernel = np.ones(kernel_size, np.uint8)
    erosion_1 = cv2.erode(denoise_img, kernel, iterations = erosion_iters[0])
    dilation_1 = cv2.dilate(erosion_1, kernel, iterations = dilation_iters[0])
    erosion_2 = cv2.erode(dilation_1, kernel, iterations = erosion_iters[1])
    result = cv2.dilate(erosion_2, kernel, iterations = dilation_iters[1])
    
    return result
