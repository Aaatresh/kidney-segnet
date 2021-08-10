# KidneyNet
Implementation of KidneyNet: Efficient Encoder–Decoder Architecture with Dimension-wisePyramid Pooling for Nuclei Segmentation of Histopathology Images 

![](./diagrams/encoder_aspp_decoder.png)

## Description
Image segmentation is a well explored task in the computer vision domain. However, the standard convolution operations performed in CNNs are inefficient in memory and computation. We address this issue by using dimensionwise convolutions (DICE blocks) to make our network more efficient. Moreover, in order to capture multi-scale information effectively, we use atrous spatial pyramid pooling on dense feature maps in the U-Net framework. 

## Getting Started

### Dependencies
* Python >= 3.6



### Installing
```
  git clone https://github.com/Aaatresh/kidney-segnet
```

### Data
The data this network was trained on H&E stained histopathology images of kidney and breast tissue. The kidney and breast datasets were obtained from [Crowdsourcing image
annotation for nucleus detection and segmentation in computational pathology: Evaluating experts, automated methods, and
the crowd][1] and [Segmentation of Nuclei in Histopathology Images by Deep Regression of the Distance Map][2] respectively.

### Running the Code
Jupyter Noteobook or Google Colab can be used to open these notebooks.
```
  jupyter notebook
```
Instructions in the notebooks guide the user through the steps to run each cell.

The file to be used to train KidneyNet is: "./DIST_dice_aspp_train.ipynb". 

Once the training process has been completed, the testing can be done through "./DIST_dice_aspp_test.ipynb".



## Authors

Contributors names and contact info:
* Anirudh Aatresh (aaa.171ec106@nitk.edu.in)

## Version History

* 0.1
    * Initial Release

## License

This project is licensed under the BSD-3-Clause License - see the LICENSE.md file for details


[1]: <https://www.researchgate.net/publication/266968190_CROWDSOURCING_IMAGE_ANNOTATION_FOR_NUCLEUS_DETECTION_AND_SEGMENTATION_IN_COMPUTATIONAL_PATHOLOGY_EVALUATING_EXPERTS_AUTOMATED_METHODS_AND_THE_CROWD>
[2]: <https://ieeexplore.ieee.org/document/8438559>

