import os
import natsort
import cv2
import numpy as np
import unicode
import keras.models



b = ['ㄱ', 'ㄴ', 'ㄷ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅅ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ', 'ㄱ', 'ㄴ', 'ㄹ',
     'ㅁ', 'ㅂ', 'ㅅ', 'ㅇ', 'ㅏ', 'ㅑ', 'ㅓ', 'ㅕ', 'ㅗ', 'ㅛ', 'ㅜ', 'ㅠ', 'ㅡ',
     'ㅣ', 'ㅐ', 'ㅔ', 'ㅖ', 'ㅢ', 'ㅚ', 'ㅘ', 'ㅝ', '가', '다', '사', '자', '억', '언', '얼',
     '연', '열', '영']


model = keras.models.load_model('BrailleNet.h5')


def predict_img(path):
    img_list = os.listdir(path)                 #path내 항목들 이름의 리스트 반환
    img_list = natsort.natsorted(img_list, reverse=False)       #항목들 이름 리스트 정렬
    result_list = []                                #예측 결과를 저장하는 리스트
    for img_file in img_list:
        if img_file.endswith('.png'):                       #항목들 이름에서 PNG파일만 찾는다
            img = cv2.imread(os.path.join(path, img_file), cv2.IMREAD_COLOR)            #OPEN CV함수인 imread(경로, 옵션) 경로에 있는 이미지 파일을 Numpy array형태로 읽는다. BGR컬러로 읽어온다
            new_img = cv2.resize(img, dsize=(36, 36))           #이미지 크기 가공
            new_img = new_img.reshape(1, 36, 36, 3)         #이미지 Numpy array가 3차원 임으로 이를 1차원으로 차원 축소
            result = np.argmax(model.predict(new_img), axis=1)      #y축 기준으로 가장 큰 값을 찾아낸다.
            print(img_file, '-->', result[0] + 1)                   #이미지 파일 이름  ---> 가장 정확한 인덱스+1
            result_list.append(result[0])                           #예측 결과를 result_list에 저장
    return alpha(result_list)


def alpha(result_list):
    han_list = ''
    print(result_list)
    if 28 <= result_list[0] <= 44:
        han_list += 'ㅇ'
    for i, result in enumerate(result_list):
        if i > 0:
            z = (result_list[i - 1] >= 21)  # 앞에 글자 모음
            b2 = (result_list[i - 1] <= 37)  # 앞에글자 모음

            c = (result_list[i] >= 21)  # 현재글자 모음
            d = (result_list[i] <= 37)  # 현재 글자 모음

            e = (result_list[i - 1] >= 14)  # 앞에 글자 종성
            f = (result_list[i - 1] <= 20)  # 앞에 글자 종성

            # 현재 글자 초성
            g = (result_list[i] >= 1)
            h = (result_list[i] <= 13)
            # 현재 글자 종성
            j = (result_list[i] >= 14)
            k = (result_list[i] <= 20)
            # 앞에 글자 초성
            l = (result_list[i - 1] >= 1)
            m = (result_list[i - 1] <= 13)
            o = (i == (len(result_list) - 1))

            if (z & b2 & c & d) | (c & d & e & f):
                han_list += 'ㅇ'
            elif (j & k & l & m) | (g & h & l & m):
                han_list += 'ㅏ'
            if result == 42:
                han_list = han_list[:-1]
                han_list += '건'
            else:
                han_list += b[result]

            if g & h & o:
                han_list += 'ㅏ'
        elif i == 0:
            han_list += b[result]
    print(han_list)                         #han_list 출력 시 [ㅂㅗ건ㅈㅣㅅㅗ] 출력                
    result = unicode.join_jamos(han_list)
    return result


result = predict_img('./test')              #test폴더 내 사진 예측 시        result_list=[5, 24, 0, 42, 7, 29, 6, 24]           
print(result)

test_list=[5, 24, 0, 42, 7, 29, 6, 24]                  # 예측 결과로 받은 인덱스의 리스트를 b에 대입 시키면 [ㅂㅗㄱ언ㅈㅣㅅㅗ] 가 나온다
for i in test_list:
    print(b[i])
    
    
# alpha(test_list)


