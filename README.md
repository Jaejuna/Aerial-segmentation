# Aerial-segmentation
Building an multi-class aerial image dataset segmentation model with weakily supervised labels

https://aiconnect.kr/competition/detail/214

## Main task
### To Do
 - 데이터 증강을 통해 학습 데이터를 늘려야 함.
   - 이미지의 각도 변경하기
   - RGB값 변경 또는 사진 반전(negative effect) 주어 색 변경하기
   - 이미지 자르기 (1/4 ~ 1/2씩 blank 처리)
  
 - train model 테스트해보며 miou값 비교하기
   - Unet / PSPnet / FPN :: Epoch 또는 Train Size 변경해가며 추가 비교 필요. 특히 Unet
  
 - Dropout 적용하기 >> train.py에 적용해야합니다. how to ?

### Test Case
  제출 후 제출 순서, 오류 내용, 설정 값을 정리하여 주십시오.
 1. Compress Error - 압축 오류로 인해 빈 파일이 업로드됨
 2. File Not Enough - 채점 간 비교 대상 파일의 부족으로 인한 오류
 3. Sample File Submit - 샘플용으로 제공된 파일을 업로드함 (테스트용, 0.24)
 4. File Not Enough - 2와 동일
 5. Unet / (train size) 0.8 / (depth) 5 - 기본 제공된 데이터로 학습 후 게시 (0.54)
 6. PSPnet / 0.8 / 5 - 기본 제공된 데이터로 학습 후 게시 (0.40)
 7. Unet++ / 0.8 / 5 - 기본 제공 데이터로 학습 후 게시 (0.55)
 8. MAnet / 0.8 / 5 - (0.47)
 9. FPN / 0.8 / 5 - (0.53)
 10. DeepLabV3Plus / 0.8 / 5 - 기본 제공 데이터로 학습 후 게시 (0.66) - 현재 TOP
 11. DeepLabV3+_GDLoss / 0.8 / 5 - 기본 제공 데이터로 학습 후 게시 (0.42)

 
 
## Convention 
### 압축 파일 제작 방법

1. cd 명령어로 'predict' 대상 폴더 > mask로 들어감
2. zip (압축파일명).zip ./*
끝

업로드 시에 과제제출란에 있는 curl 링크 가져와서
file path만 (압축파일명).zip으로 바꿔서 제출하시면 됩니다.

### 학습(train) 완료 후에는 
 _ 폴더 명을 '학습모델명'으로 변경해주십시오.
 _ predict.yaml에서 train model을 폴더 명으로 변경하여 주십시오


## requirements
python3 -m pip install -r requirements.txt

## ref in container
 - Models
   - https://smp.readthedocs.io/en/latest/ (SMP)
   - https://github.com/dmMaze/UNet3Plus-pytorch
   - https://paperswithcode.com/paper/unet-3-a-full-scale-connected-unet-for
   - https://wandb.ai/wandb_fc/korean/reports/---VmlldzoxNDI4NzEy
   - https://paperswithcode.com/paper/resattunet-detecting-marine-debris-using-an
   - https://www.kaggle.com/code/hsuyuhao/deeplabv3-plus
   - https://www.kaggle.com/code/balraj98/deeplabv3-resnet101-for-segmentation-pytorch
   - https://github.com/jfzhang95/pytorch-deeplab-xception (DeepLabV3+)
 
 
- Overfitting
   - https://www.kaggle.com/code/phoenigs/u-net-dropout-augmentation-stratification/notebook#Data-augmentation
   - https://gaussian37.github.io/dl-pytorch-snippets/
   - https://pytorch.org/docs/stable/generated/torch.nn.Dropout.html
 
 - Loss function
    - https://www.kaggle.com/code/sungjunghwan/loss-function-of-image-segmentation
  
  - papers
   -  https://arxiv.org/pdf/1802.02611v3.pdf

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
