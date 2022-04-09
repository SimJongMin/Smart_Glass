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

#COMMENT : PresetData에 학습 데이터가 없는 경우에 실행한다.
# Rdy_image.Preset()        


#COMMENT : data Generator 테스트, 검증 데이터 생성
train_generator, val_generator = DATAGenerator.data_ready()



#COMMENT : KorBrailleNet.h5 파일이 없는 경우 or input data가 변경된 경우 실행한다.
# hist = Make_model.Make_model(train_generator,val_generator)           
# Make_model.print_acc_loss(hist)                   


#COMMENT: BrailleNet에 저장된 모델을 불러옴.
#COMMENT: acc확인
model = Load_model.load_model()
acc = Load_model.acc_chk(model,val_generator)   # 


#COMMENT: 사진 데이터 불러오기, 예측
path_single = 'E:/22-1/CapstoneDesign/Smart_Glass/BrailleCNN/korBrailleCode/real/위아더웨더.jpg'        #FIXME: fix path to relative path

def action_single(path):
    
    b = Predict.Predic()
    a = divide.img_devide(path)
    
    a.create_dir()
    a.set_image()
    b.reset()
    
    for i in range(0,a.lengh):
        a.devide_img()
        real = DATAGenerator.load_image_single('E:/22-1/CapstoneDesign/Smart_Glass/BrailleCNN/korBrailleCode/testDataset/')     #FIXME: fix path to relative path
        b.Predict_single(model,real)
        a.remove_file()
        
    b.composit()
    print(b.result)
    return b.result

action_single(path_single)
