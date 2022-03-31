import operator
import numpy as np
import cv2

korAlphabet=[
    "ㄱCho","ㄴCho","ㄷCho","ㄹCho","ㅁCho","ㅂCho","ㅅCho","ㅈCho","ㅊCho","ㅋCho","ㅌCho","ㅍCho","ㅎCho","multiCho",
    "ㄱJong","ㄴJong","ㄷJong","ㄹJong","ㅁJong","ㅂJong","ㅅJong","ㅇJong","ㅈJong","ㅋJong","ㅌJong","ㅍJong","ㅎJong",
    "ㅏ","ㅐ","ㅑ","ㅓ","ㅔ","ㅕ","ㅖ","ㅗ","ㅘ","ㅚ","ㅛ","ㅜ","ㅝ","ㅠ","ㅡ","ㅢ","ㅣ",
    "가","나","다","마","바","사","ㅆ","억","언","얼","연","열","영","옥","온","옹","운","울","은","을","인","자","카","타","파","하"
]

def alpha(num):
    if num == 26:
        return  ' '
    else:
        num_tr = num+97
        return chr(num_tr)

class Predic():
    result = []
    def Predict(self,model,real):
        my_list = model.predict(real)
        index, value = max(enumerate(my_list[0]), key=operator.itemgetter(1))
        # print(index,alpha(index))
        self.result.append(alpha(index))

        return self.result

    def reset(self):
        self.result = []

# def chk_trans():
#     for i in korAlphabet:
#         print(i + ':' + alpha(i),end='  ')
#         if i%3 ==2 :
#             print()
