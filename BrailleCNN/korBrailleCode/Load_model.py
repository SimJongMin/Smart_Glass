#COMMENT : 모델 불러오기
def load_model():
    from keras.models import load_model
    model = load_model('E:/22-1/CapstoneDesign/Smart_Glass/BrailleCNN/korBrailleCode/KorBrailleNet.h5')     #FIXME: fix path to relative path
    return model


#COMMENT : 모델 정확도 확인
def acc_chk(model, val):
    acc = model.evaluate_generator(val)[1]
    print('model accuracy: {}'.format(round(acc,4)))