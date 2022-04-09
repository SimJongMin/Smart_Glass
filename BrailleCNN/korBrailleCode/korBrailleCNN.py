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
import Make_model
import Rdy_image
import DATAGenerator
import divide
import Predict
import Load_model

## 이미지 준비 *한번 실행되면 다시 실행할 필요 없음.
# Rdy_image.Preset()


## data Generator 테스트, 검증 데이터 생성
train_generator, val_generator = DATAGenerator.data_ready()


#MAKE MODEL *한번 모델이 생성되면 다시 실행할 필요 없음
# hist = Make_model.Make_model(train_generator,val_generator)
# Make_model.print_acc_loss(hist)                 


# BrailleNet에 저장된 모델을 불러옴.
# acc확인
model = Load_model.load_model()
acc = Load_model.acc_chk(model,val_generator)


# 사진 데이터 불러오기, 예측


path_single = 'E:/22-1/CapstoneDesign/Smart_Glass/BrailleCNN/korBrailleCode/real/위아더웨더.jpg'

def action_single(path):
    
    # Predict.chk_trans()  
    b = Predict.Predic()
    a = divide.img_devide(path)
    
    a.create_dir()
    a.set_image()
    b.reset()
    
    for i in range(0,a.lengh):
        a.devide_img()
        real = DATAGenerator.load_image_single('E:/22-1/CapstoneDesign/Smart_Glass/BrailleCNN/korBrailleCode/testDataset/')
        b.Predict_single(model,real)
        a.remove_file()
        
    b.composit()
    print(b.result)
    # result = ''.join(b.result)
    # return result

action_single(path_single)












'''-------------------------글자 인덱스 확인용도------------------
path = 'E:/22-1/CapstoneDesign/Smart_Glass/BrailleCNN/korBrailleCode/real/'
def action(path):
    
    # Predict.chk_trans()  
    b = Predict.Predic()
    for file in os.listdir(path):
        a = divide.img_devide(path+file)
        a.create_dir()
        a.set_image()
        b.reset()
        print(file)
        for i in range(0,a.lengh):
            a.devide_img()
            real = DATAGenerator.load_image('E:/22-1/CapstoneDesign/Smart_Glass/BrailleCNN/korBrailleCode/testDataset/')
            b.Predict(model,real)
            a.remove_file()


        # print(b.result)
        # result = ''.join(b.result)
        # return result


action(path)
'''






