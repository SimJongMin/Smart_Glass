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


def dataCreateDiv():
    #COMMENT : PresetData에 학습 데이터가 없는 경우에 실행한다.
    # Rdy_image.Preset()

    #COMMENT : data Generator 테스트, 검증 데이터 생성
    train_generator, val_generator = DATAGenerator.data_ready()
    return val_generator


def modelCreateLoad():
    val_generator=dataCreateDiv()
    #COMMENT : KorBrailleNet.h5 파일이 없는 경우 or korBrailleImage 내부의 학습데이터가 변경된 경우 실행한다.
    # hist = Make_model.Make_model(train_generator,val_generator)
    # Make_model.print_acc_loss(hist)

    #COMMENT: BrailleNet에 저장된 모델을 불러옴.
    #COMMENT: acc확인
    model = Load_model.load_model()
    acc = Load_model.acc_chk(model, val_generator)
    return model



def action():
    #COMMENT: 사진 데이터 불러오기, 예측
    #realBraillePicturePath = '/home/pi/camera/images/trimed_image.jpg'
    realBraillePicturePath='./images/운수좋은날.jpg'
    
    model=modelCreateLoad()
    
    Predict.chk_trans()
    b = Predict.Predic()
    a = divide.img_devide(realBraillePicturePath)
    
    a.create_dir()
    a.set_image()
    b.reset()
    
    for i in range(0,a.lengh):
        a.devide_img()
        real = DATAGenerator.load_image_single('./testDataset/')
        b.Predict_single(model,real)
        a.remove_file()
        
    b.composit()
    print(b.result)
    return b.result

<<<<<<< HEAD

=======
>>>>>>> 97e3271dfd8ba09ddac668b9aa15149e3023a569
action()