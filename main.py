from keras import models
from keras import layers
from keras.preprocessing import image
from keras import optimizer

import tensorflow as tf
import matplotlib.pyploy as plt
import numpy as np


# 데이터 가져오기


# 데이터 전처리


# 모델
model = models.sequential()

# 훈련 설정
model.compile(  
  optimizer='sgd',
  loss='mse',
  metrics=[tf.keras.metrics.MeanIoU(num_classes=2)])

# 훈련


# 그래프


# 저장
model.save('cats_and_dogs_small_1.h5')