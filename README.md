# Rethinking the Architecture Design for Efficient Generic Event  Boundary Detection
[Rethinking the Architecture Design for Efficient Generic Event Boundary Detection  ](https://openreview.net/forum?id=sA2a5a5O4g&referrer=%5Bthe%20profile%20of%20Zechuan%20Zhang%5D(%2Fprofile%3Fid%3D~Zechuan_Zhang2)) , ACM MM 2024

[Ziwei Zheng](https://openreview.net/profile?id=~Ziwei_Zheng1 "~Ziwei_Zheng1"), [Zechuan Zhang](https://openreview.net/profile?id=~Zechuan_Zhang2 "~Zechuan_Zhang2"),[Yulin Wang](https://openreview.net/profile?id=~Yulin_Wang1 "~Yulin_Wang1"),[Shiji Song](https://openreview.net/profile?id=~Shiji_Song1 "~Shiji_Song1"),[Gao Huang](https://openreview.net/profile?id=~Gao_Huang1 "~Gao_Huang1"),[Le Yang](https://openreview.net/profile?id=~Le_Yang2 "~Le_Yang2")

## Overview
In this paper, we experimentally reexamine the architecture of GEBD models and uncover several surprising findings. Firstly, we reveal that a concise GEBD baseline model already achieves promising performance without any sophisticated design. Secondly, we find that the common design of GEBD models using image-domain backbones can contain plenty of architecture redundancy, motivating us to gradually “modernize” each component to enhance efficiency. Thirdly, we show that the GEBD models using image-domain backbones conducting the spatiotemporal learning in a spatial-then-temporal greedy manner can suffer from a distraction issue, which might be the inefficient villain for the GEBD. Using a video-domain backbone to jointly conduct spatiotemporal modeling for GEBD is an effective solution for this issue. 
The outcome of our exploration significantly outperforms the previous SOTA methods under the same backbone choice. 



## Preparing Kinetics-GEBD/TAPOS/SoccerNet Dataset
Please refer to [GUIDE](https://github.com/zechuan2024/EffGEBD/blob/master/data/GUIDE.md) for preparing Kinetics-GEBD/TAPOS dataset in the following path:
`EfficientGEBD/data/`
and preparing SoccerNet dataset in the following path:
`EfficientGEBD/EffSoccerNet/data`

**a) Kinetics-GEBD Dataset** is frequently used in most previous works, which contains 54,691 videos randomly selected from Kinetics-400. You can click [Kinetics-GEBD](https://github.com/StanLei52/GEBD) for more details. Since the annotations for the test set are not publicly accessible, we conducted training on the training set and subsequently evaluated model performance using the validation set.

**b) TAPOS Dataset** 
 we adapt [TAPOS](https://sdolivia.github.io/TAPOS/) by concealing each action instance’s label and conducting experiments based on this modified dataset.

**c) SoccerNet Dataset** 
SoccerNet-v2 is used as an additional benchmark for action spotting detection, which can be viewed as a sub-category of generic event boundaries.


## Getting started
1. Download [configs](https://drive.google.com/drive/folders/1_FvcIINdU4IXpUnTiMgSBnoYCxqY-BsS?usp=sharing) and [csn-ckpt](https://drive.google.com/drive/folders/12UVE-YpCm9nniZDJGBZbWEta2-4A3MRA?usp=sharing) and place them in `EfficientGEBD/`

2. git clone our repository, creating a python environment and activate it via the following command:
```
git clone https://github.com/Ziwei-Zheng/EfficientGEBD.git
cd EfficientGEBD
conda create --name EfficientGEBD python=3.10
conda activate EfficientGEBD
pip install -r requirements.txt
```

## Training scripts

Training EfficientGEBD via the following command (choose the model you want to train at 'EfficientGEBD/script/train/):
For example, training BasicGEBD-ResNet50-L1:
```
cd script/train
bash BasicGEBD-ResNet50-L1.sh
```
Training EfficientGEBD-ResNet50-L4:

```
cd script/train
bash EfficientGEBD-ResNet50-L4.sh
```
While training models with SoccerNet, use `bash EffSoccerNet/EffSoccerNet_train.sh` instead.

## Testing our trained model

We only provide the checkpoint that generating our highest score in the paper[[download](https://drive.google.com/file/d/1S4M-xnKpjWFGBimcRYzlEDFhDsWQWF_-/view?usp=drive_link)]. Unzip the specific folder below to your project(make sure the following path 'EfficientGEBD/output/ablation/`$YOUR_UNZIPPED_DIR$`'):

| _Method_| _Backbone_  | _F1 score_ | _GFLOPs_ | _FPS_ |
| :----: | :----: | :----: | :----: | :----: |
|  _BasicGEBD_ | ResNet50-L4  | **77.1** | 4.36 | 1562 |
| _BasicGEBD_  | ResNet50-L2  | **76.8** | 2.08 | 2325 |
| _BasicGEBD_  | ResNet34-L4  | **77.0** | 3.92 | 2386 |
| _BasicGEBD_  | ResNet18-L4  | **77.2** | 2.07 |2380  |
| _BasicGEBD_  | ResNet152-L4  | **77.2** | 11.77| 847 |
| _EfficientGEBD_  | ResNet50-L2*  | **78.3** | 2.10 | 2116 |
| _EfficientGEBD_  | ResNet50-L4*  | **78.7** | 4.39 |1541  |
| _EfficientGEBD_  | CSNR152-L2* | **80.6** | 2.00 | 1215 | 
| _EfficientGEBD_  | CSNR152-L4* | **82.9** | 6.40 | 1025 |


Testing EfficientGEBD via the following command (choose the model you want to test at 'EfficientGEBD/script/test/'):
```
cd script/test
bash BasicGEBD-ResNet50-L1.sh
```

While testing model with SoccerNet, use `bash EffSoccerNet/SoccerNet_test.sh` instead.

## Citation

If you find our work helps, please cite our paper:

## Contact

This repo is maintained by . Questions and discussions are welcome via 

## Acknowledgement
