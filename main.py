import tensorflow as tf
import matplotlib.pyploy as plt
import numpy as np
import os, shutil

from tensorflow.keras.models import sequential
from tensorflow.keras import layers
from tensorflow.keras.preprocessing import image
from tensorflow.keras import optimizer
from tensorflow.keras import applications



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

# 저장
model.save('cats_and_dogs_small_1.h5')


# 그래프
