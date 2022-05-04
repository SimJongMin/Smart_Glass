import math
from operator import le
import os

lengh=0
height=42
# width=12564     # 349개
width=0     # 350개


# for x in range(1,351):
#     width=36*x
#     lengh = math.ceil(width / (float(height)/1.16))
#     if(width>=6300):
#         m=int(int((float(height)/1.16)*175)/100)*100
#         i=int(width/m)
#         lengh+=i
#     print(str(x)+" 번째 개수 : "+str(lengh))


korAlpha=[
'공백','ㄱ초','ㄱ종','ㄴ종','ㄷ종','ㄹ초',
'ㄹ종','ㅁ종','ㅂ종','ㅅ초','ㅅ종','ㅇ종',
'ㅈ종','ㅊ초','ㅊ종','ㅋ종','ㅌ종','ㅍ종',
'ㅎ종','ㅏ','ㅐ','ㅑ','ㅓ','ㅔ',
'ㅕ','ㅖ','ㅗ','ㅘ','ㅚ','ㅛ','ㅜ',
'ㅝ','ㅠ','ㅡ','ㅢ','ㅣ','가',
'것1','나','다','마','바','붙임,''사',
'수표','억','언','얼','연','열','영',
'옥','온','옹','운','울','은','을',
'인','자','카','타','파','하',
'ㅟ','ㅒ','ㅙ','ㅞ','것','그래서',
'그러나','그러면','그러므로','그런데','그리고','그리하여'
]



def chk_trans():
    for i in range(0,75):
        print(str(i)+ " : "+korAlpha[i],end=" | ")
        if(i%5 ==4):
            print()

chk_trans()