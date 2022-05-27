from korBrailleCode import Make_model
from korBrailleCode import Rdy_image
from korBrailleCode import DATAGenerator
from korBrailleCode import divide
from korBrailleCode import Predict
from korBrailleCode import Load_model
# import Make_model
# import Rdy_image
# import DATAGenerator
# import divide
# import Predict
# import Load_model



def dataCreateDiv():
    #COMMENT : PresetData에 학습 데이터가 없는 경우에 실행한다.
    #Rdy_image.Preset()

    #COMMENT : data Generator 테스트, 검증 데이터 생성
    train_generator, val_generator = DATAGenerator.data_ready()
    # train_generator, val_generator = DATAGenerator.noise_data_ready()
    # train_generator, val_generator = DATAGenerator.capture_data_ready()
    # train_generator, val_generator = DATAGenerator.total_data_ready()
    return train_generator, val_generator


def modelCreateLoad():
    train_generator, val_generator=dataCreateDiv()
    #COMMENT : KorBrailleNet.h5 파일이 없는 경우 or korBrailleImage 내부의 학습데이터가 변경된 경우 실행한다.
    # hist = Make_model.Make_model(train_generator,val_generator)
    # hist = Make_model.Make_noise_model(train_generator,val_generator)
    # hist = Make_model.Make_capture_model(train_generator,val_generator)
    # hist = Make_model.Make_total_model(train_generator,val_generator)
    # Make_model.print_acc_loss(hist)

    #COMMENT: BrailleNet에 저장된 모델을 불러옴.
    #COMMENT: acc확인
    model = Load_model.load_model()
    # model = Load_model.load_noise_model()
    # model = Load_model.load_capture_model()
    # model = Load_model.load_total_model()
    acc = Load_model.acc_chk(model, val_generator)
    return model


def action():
    #COMMENT: 사진 데이터 불러오기, 예측
    # realBraillePicturePath = './demoImage/Braille/인간_43.jpg'
    realBraillePicturePath='./demoImage/recieved.jpg'
    
    model=modelCreateLoad()
    
    # Predict.chk_trans()
    b = Predict.Predic()
    a = divide.img_devide(realBraillePicturePath)
    
    a.create_dir()
    a.set_image()
    b.reset()
    
    for i in range(0,a.lengh):
        a.devide_img()
        real = DATAGenerator.load_image_single('./korBrailleCode/testDataset/')
        b.Predict_single(model,real)
        a.remove_file()
        
    b.composit()
    print(b.result)
    return b.result


def serverAction(image):
    #COMMENT: 사진 데이터 불러오기, 예측
    # realBraillePicturePath = './images/위아더웨더.jpg'
    realBraillePicturePath=image
    
    model=modelCreateLoad()
    
    # Predict.chk_trans()
    b = Predict.Predic()
    a = divide.img_devide(realBraillePicturePath)
    
    a.create_dir()
    a.set_image()
    b.reset()
    
    for i in range(0,a.lengh):
        a.devide_img()
        real = DATAGenerator.load_image_single('./korBrailleCode/testDataset/')
        b.Predict_single(model,real)
        a.remove_file()
        
    b.composit()
    # print(b.result)
    return b.result