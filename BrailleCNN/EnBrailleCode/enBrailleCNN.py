import os
import numpy as np
import pandas as pd
from PIL import Image
from shutil import copyfile
from keras.preprocessing.image import ImageDataGenerator, img_to_array, load_img
from keras import backend as K
from keras import layers as L
from keras.models import Model,load_model
from keras.regularizers import l2
from keras.callbacks import ModelCheckpoint,ReduceLROnPlateau,EarlyStopping
import operator

##GPU 오류 해결 (keras_scratch_graph)
#import keraserr
#keraserr.fixerr()

## 이미지 준비 *한번 실행되면 다시 실행할 필요 없음.
import Rdy_image
Rdy_image.Preset()



## data Generator 테스트, 검증 데이터 생성
import DATAGenerator
train_generator, val_generator = DATAGenerator.data_ready()

#MAKE MODEL *한번 모델이 생성되면 다시 실행할 필요 없음
# import Make_model
# hist = Make_model.Make_model(train_generator,val_generator)
# Make_model.print_acc_loss(hist)

# BrailleNet에 저장된 모델을 불러옴.
# acc확인
import Load_model
model = Load_model.load_model()
acc = Load_model.acc_chk(model,val_generator)

# 사진 데이터 불러오기, 예측
import divide
import Predict

path = 'E:/22-1/CapstoneDesign/Smart_Glass/BrailleCNN/EnBrailleCode/real/data2.png'

def action(path):
    
    Predict.chk_trans()
    b = Predict.Predic()
    a = divide.img_devide(path)

    a.create_dir()
    a.set_image()
    b.reset()

    for i in range(0,a.lengh):
        a.devide_img()
        real = DATAGenerator.load_image('E:/22-1/CapstoneDesign/Smart_Glass/BrailleCNN/EnBrailleCode/testDataset/')
        b.Predict(model,real)
        a.remove_file()


    print(b.result)
    result = ''.join(b.result)
    return result


action(path)

