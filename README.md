# Aerial-segmentation
Making an aerial image segmentation model

### Main task
Datasets : aerial images of cityscapes

Data preprocess
- classifying changed ones and unchanged ones 
  - then applying CAM..?

Applying models



### requirements
python3 -m pip install -r requirements.txt

## ref
- RS+EPM : https://github.com/OFRIN/RecurSeed_and_EdgePredictMix
- PPC : https://github.com/usr922/wseg
- RCA : https://github.com/maeve07/rca
- L2G : https://github.com/pengtaojiang/l2g
- Puzzle-CAM : 'Puzzle-CAM: Improved localization via matching partial and full features' - Jo et al., 2021
  - https://github.com/OFRIN/PuzzleCAM
- U-net : 'U-net: Convolutional networks for biomedical image segmentation' - Ronneberger et al., 2015 
  - https://dacon.io/codeshare/4245?dtype=recent
  - https://junstar92.tistory.com/151
  - https://www.kaggle.com/code/dikshabhati2002/image-segmentation-u-net
- PSPnet : https://medium.com/analytics-vidhya/semantic-segmentation-in-pspnet-with-implementation-in-keras-4843d05fc025
- CAM : 'Learning Deep Features for Discriminative Localization' - Bolei Zhou et al., 2015
  - https://junstar92.tistory.com/152
- etc
  - https://www.tensorflow.org/tutorials/images/data_augmentation?hl=ko
  - https://medium.com/ddiddu-log/이미지-인식-2-이미지-분할-semantic-segmentation-의-정의와-주요-모델-비교-f46c0197a82d
  - https://intuitive-robotics.tistory.com/79
  - ICNet for Real-Time Semantic Segmentation on High-Resolution Images - H.Zhao et al., 2018, https://github.com/hellochick/ICNet-tensorflow
  - Context Decoupling Augmentation for Weakly Supervised Semantic Segmentation - Y. Su et al., 2021, https://github.com/suyukun666/CDA
