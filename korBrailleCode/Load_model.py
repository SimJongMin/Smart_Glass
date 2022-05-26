#COMMENT : 모델 불러오기


def load_model():
    from keras.models import load_model
    model = load_model('./korBrailleCode/KorBrailleNet.h5')     
    # model = load_model('./KorBrailleNet.h5')     
    return model


def load_noise_model():
    from keras.models import load_model
    model = load_model('./korBrailleCode/noiseKorBrailleNet.h5')     
    # model = load_model('./KorBrailleNet.h5')     
    return model


def load_capture_model():
    from keras.models import load_model
    model = load_model('./korBrailleCode/captureKorBrailleNet.h5')
    # model = load_model('./KorBrailleNet.h5')
    return model


def load_total_model():
    from keras.models import load_model
    model = load_model('./korBrailleCode/totalKorBrailleNet.h5')
    # model = load_model('./KorBrailleNet.h5')
    return model





#COMMENT : 모델 정확도 확인
def acc_chk(model, val):
    acc = model.evaluate_generator(val)[1]
    print('model accuracy: {}'.format(round(acc,4)))