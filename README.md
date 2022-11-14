# Aerial-segmentation
 제 1회 2022 국방 AI 경진대회 (군 장병 부문), AI Connect

Team : 지능보호 <br/>
Assignment : Making an aerial image segmentation model comparing with serial datas and weakily supervised labels 
Assignment URL : https://aiconnect.kr/competition/detail/214

## Main task
### To Do
 - 데이터 증강 통해 학습 데이터를 늘려야 함. V <br/>
  ○ 이미지의 각도 변경하기 V <br/>
  ○ RGB값 변경 또는 사진 반전(negative effect) 주어 색 변경하기 V <br/>
  
 - train model 테스트해보며 miou값 비교하기 <br/>
  ○ Unet / PSPnet / FPN :: Epoch 또는 Train Size 변경해가며 추가 비교 필요. 특히 Unet V
  
 - Dropout 적용하기 >> train.py에 적용해야합니다. how to ? V

### Test Case
  제출해본 결과들 
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
 12. DeepLabV3+_4depths / 0.8 / 4 - 깊이를 4로 줄이기 (유사 드롭아웃), 기본 제공 데이터로 학습 후 게시 (0.65)
 13. DeepLabV3+_withAugData / 0.8 / 5 - 데이터 증강후 학습 했지만 시간이 없어 끊고 게시 (0.64)
 
## Convention 
### 압축 파일 제작 방법
1. cd 명령어로 'predict' 대상 폴더 > mask로 들어감
2. zip (압축파일명).zip ./*

업로드 시에 과제제출란에 있는 curl 링크 가져와서
file path만 (압축파일명).zip으로 바꿔서 제출하시면 됩니다.

### 학습(train) 완료 후에는 
 _ 폴더 명을 '학습모델명'으로 변경해주십시오.
 _ predict.yaml에서 train model을 폴더 명으로 변경하여 주십시오

## requirements
python3 -m pip install -r requirements.txt

### Summary
<img src="/images/Public 순위.png"></img><br/>
<img src="/images/제출 결과.png"></img>

배운 것도 많고 부족한 것도 많이 느낀 공모전.

리눅스 개발 환경, CUDA, 알고리즘, 딥러닝 자체에 대한 직관력과 통찰력 모두 부족했다.

하지만 성장했고, 더 준비한다면 다음에는 더 좋은 결과가 있을 것 같다.

Thanks to [Ssogari](https://github.com/ssogari-dev)

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
